"""Collect unlabeled HN comments; never predict labels or print comment bodies."""

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import csv
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import io
import json
from pathlib import Path
import random
import re
import sys
import time
import unicodedata

import requests


ROOT = Path(__file__).resolve().parent
API = "https://hacker-news.firebaseio.com/v0/item/{}.json"


def utc_now():
    return datetime.now(timezone.utc).isoformat()


class CommentText(HTMLParser):
    """Decode rendered text once, retaining block/code layout and link targets."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts, self.links, self.lists, self.quotes = [], [], [], []

    def boundary(self):
        if self.parts and not self.parts[-1].endswith("\n\n"):
            self.parts.append("\n\n")

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a":
            self.links.append((attrs.get("href", ""), len(self.parts)))
        elif tag == "br":
            self.parts.append("\n")
        elif tag == "blockquote":
            self.boundary()
            self.quotes.append(len(self.parts))
        elif tag in {"p", "div", "pre"}:
            self.boundary()
        elif tag in {"ul", "ol"}:
            self.boundary()
            self.lists.append([tag, 0])
        elif tag == "li":
            self.parts.append("\n" + "  " * max(0, len(self.lists) - 1))
            if self.lists and self.lists[-1][0] == "ol":
                self.lists[-1][1] += 1
                self.parts.append(f"{self.lists[-1][1]}. ")
            else:
                self.parts.append("- ")

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag != "br":
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag == "a" and self.links:
            href, start = self.links.pop()
            label = "".join(self.parts[start:]).strip()
            if href and href != label:
                self.parts.append(f" ({href})" if label else href)
        elif tag == "blockquote" and self.quotes:
            start = self.quotes.pop()
            block = "".join(self.parts[start:]).strip("\r\n")
            self.parts[start:] = ["\n".join("> " + line if line else ">" for line in block.splitlines())]
            self.boundary()
        elif tag in {"p", "div", "pre", "ul", "ol"}:
            self.boundary()
            if tag in {"ul", "ol"} and self.lists:
                self.lists.pop()

    def handle_data(self, data):
        self.parts.append(data)


def decode_comment(raw_html):
    parser = CommentText()
    parser.feed(raw_html)
    parser.close()
    # Keep meaningful code indentation, including a code block at the start.
    return "".join(parser.parts).strip("\r\n")


def normalized(text):
    return " ".join(unicodedata.normalize("NFKC", text).split()).casefold()


def fetch_item(item_id):
    for attempt in range(3):
        try:
            response = requests.get(API.format(item_id), timeout=(10, 30))
            response.raise_for_status()
            value = response.json()
            if value is not None and not isinstance(value, dict):
                raise ValueError("Expected an item object or null")
            return value, utc_now()
        except (requests.RequestException, ValueError) as exc:
            if attempt == 2:
                raise RuntimeError(f"Unable to retrieve HN item {item_id}") from exc
            time.sleep(0.5 * (2 ** attempt))


def excluded_comment_ids():
    notes = (ROOT / "milestone1_reading_notes.md").read_text(encoding="utf-8")
    # Match numbered source-table rows, not thread links or repeated examples.
    ids = {int(value) for value in re.findall(
        r"^\|\s*\d+\s*\|\s*\[(\d+)\s*—", notes, flags=re.MULTILINE
    )}
    if len(ids) < 36:
        raise ValueError("Expected at least 36 excluded comment IDs in Milestone 1 notes")
    return ids


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stories", type=Path, required=True)
    parser.add_argument("--limit", type=int, default=240)
    parser.add_argument("--per-thread", type=int, default=12)
    parser.add_argument("--seed", type=int, default=20261017)
    args = parser.parse_args()
    if args.limit < 200 or args.per_thread < 1:
        parser.error("--limit must be at least 200 and --per-thread must be positive")

    outputs = [ROOT / "labels.csv", ROOT / "data/comment_sources.jsonl",
               ROOT / "data/collection_manifest.json"]
    existing = [str(path) for path in outputs if path.exists() or path.is_symlink()]
    if existing:
        raise FileExistsError("Refusing to overwrite existing outputs: " + ", ".join(existing))
    source = json.loads(args.stories.read_text(encoding="utf-8"))
    if not isinstance(source, dict) or not isinstance(source.get("stories"), list):
        raise ValueError("--stories must contain an object with a stories list")
    story_ids = list(dict.fromkeys(int(story["id"]) for story in source["stories"]))
    if not story_ids or any(item_id < 1 for item_id in story_ids):
        raise ValueError("Supply at least one valid positive story ID")
    excluded_ids = excluded_comment_ids()
    counts, thread_counts, threads = Counter(), Counter(), []
    rows, seen_ids, seen_text = [], set(), set()
    started = utc_now()

    with ThreadPoolExecutor(max_workers=4) as pool:
        # Refetch old sources to exclude repeated text without a temporary-file dependency.
        excluded_text = set()
        for item_id, (item, _) in zip(sorted(excluded_ids), pool.map(fetch_item, sorted(excluded_ids))):
            if not item or not isinstance(item.get("text"), str):
                raise ValueError(f"Cannot reconstruct excluded source text for item {item_id}")
            text = normalized(decode_comment(item["text"]))
            if not text:
                raise ValueError(f"Excluded source {item_id} has no readable text")
            excluded_text.add(text)

        for story_id, (story, _) in zip(story_ids, pool.map(fetch_item, story_ids)):
            if not story or story.get("type") != "story" or story.get("deleted") or story.get("dead"):
                counts["unavailable_story"] += 1
                continue
            title = story.get("title", "")
            threads.append({"id": story_id, "title": title})
            candidates = list(story.get("kids", []))
            random.Random(args.seed + story_id).shuffle(candidates)
            position = 0
            while position < len(candidates) and thread_counts[story_id] < args.per_thread and len(rows) < args.limit:
                batch = candidates[position:position + 4]
                position += len(batch)
                wanted = []
                for item_id in batch:
                    if item_id in excluded_ids:
                        counts["excluded_known_id"] += 1
                    elif item_id in seen_ids:
                        counts["duplicate_id"] += 1
                    else:
                        seen_ids.add(item_id)
                        wanted.append(item_id)
                for item_id, (item, retrieved) in zip(wanted, pool.map(fetch_item, wanted)):
                    if not item:
                        counts["unavailable_comment"] += 1
                    elif item.get("deleted") or item.get("dead"):
                        counts["deleted_or_dead"] += 1
                    elif item.get("type") != "comment":
                        counts["not_comment"] += 1
                    elif item.get("parent") != story_id or item.get("id") != item_id:
                        counts["unexpected_parent_or_id"] += 1
                    elif not isinstance(item.get("text"), str):
                        counts["empty_text"] += 1
                    else:
                        raw_html = item["text"]
                        text = decode_comment(raw_html)
                        key = normalized(text)
                        if not key:
                            counts["empty_text"] += 1
                        elif key in excluded_text:
                            counts["excluded_prior_text"] += 1
                        elif key in seen_text:
                            counts["duplicate_text"] += 1
                        elif thread_counts[story_id] < args.per_thread and len(rows) < args.limit:
                            seen_text.add(key)
                            thread_counts[story_id] += 1
                            rows.append({"text": text, "comment_id": item_id,
                                         "permalink": f"https://news.ycombinator.com/item?id={item_id}",
                                         "thread_id": story_id, "thread_title": title,
                                         "author": item.get("by"),
                                         "time_utc": datetime.fromtimestamp(item["time"], timezone.utc).isoformat(),
                                         "retrieved_at_utc": retrieved, "raw_html": raw_html,
                                         "text_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest()})
                        else:
                            counts["batch_surplus_after_cap"] += 1
            if len(rows) >= args.limit:
                break

    if len(rows) < 200:
        raise ValueError(f"Only {len(rows)} unique fresh comments available; no outputs written. Add source threads.")
    random.Random(args.seed).shuffle(rows)  # Annotation order only; never a train/test split.
    csv_buffer = io.StringIO(newline="")
    writer = csv.writer(csv_buffer)
    writer.writerow(["text", "label", "note"])
    writer.writerows((row["text"], "", "") for row in rows)
    provenance = []
    for index, row in enumerate(rows, 1):
        provenance.append(json.dumps({"csv_row": index, **{k: v for k, v in row.items() if k != "text"}}, ensure_ascii=False))
    manifest = {"started_at_utc": started, "finished_at_utc": utc_now(),
                "api": "https://hacker-news.firebaseio.com/v0/", "seed": args.seed,
                "requested_limit": args.limit, "per_thread_cap": args.per_thread,
                "count": len(rows), "requested_limit_met": len(rows) == args.limit,
                "sampling": "Shuffled top-level IDs per selected thread; no content-quality filtering. Final shuffle sets annotation order only.",
                "source_file": str(args.stories.resolve()), "discovery": source.get("discovery", {}),
                "selected_stories": source["stories"], "authoritative_threads": threads,
                "thread_counts": {str(k): v for k, v in thread_counts.items()},
                "excluded_comment_ids": sorted(excluded_ids), "excluded_normalized_texts": len(excluded_text),
                "exclusion_counts": dict(counts), "blank_label_count": len(rows), "blank_note_count": len(rows),
                "csv_row_convention": "1-based data row, excluding the header; multiline fields remain one row",
                "cold_annotation": {"status": "pending unaided student annotation", "reserved_data_rows": list(range(1, 21)),
                                    "reserved_comment_ids": [r["comment_id"] for r in rows[:20]], "notes_marked_cold": False},
                "outputs": [str(path) for path in outputs]}
    buffers = [csv_buffer.getvalue(), "\n".join(provenance) + "\n",
               json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"]
    # All fetching, validation and serialization finish before any output is created.
    outputs[1].parent.mkdir(parents=True, exist_ok=True)
    for path, content in zip(outputs, buffers):
        with path.open("x", encoding="utf-8", newline="") as handle:
            handle.write(content)
    print(json.dumps({"count": len(rows), "blank_labels": len(rows), "blank_notes": len(rows),
                      "excluded_prior_ids": len(excluded_ids), "thread_counts": manifest["thread_counts"],
                      "threads": threads, "outputs": manifest["outputs"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError, TypeError, RuntimeError) as exc:
        print(f"Collection stopped: {exc}", file=sys.stderr)
        sys.exit(1)
