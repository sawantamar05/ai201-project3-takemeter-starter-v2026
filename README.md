# TakeMeter

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, the
> notebook, the baseline, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> head -5 data/practice_labels.csv     # the shape your labels.csv needs
> ```
>
> Then open `takemeter.ipynb` **in this folder** — in VS Code, or with
> `jupyter notebook` if you prefer. Pick the kernel: the `.venv` inside this
> project. Run section 1, which reports the hardware you'll be training on.
> Everything else waits until you have data.
>
> Nothing to upload, nothing to connect, no accounts and no keys. The notebook
> runs on your machine and writes next to your code.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     Unit 5 asks for the first five sections. Unit 6 adds the five below them.

     Everything is pasted as TEXT. No screenshots, no images.

     ⚠️ The confusion matrix especially. The notebook prints one as a markdown
     table, ready to copy. A screenshot of a matrix earns nothing. Paste the
     table.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 5 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- Your community, and what your classifier sorts posts into. Three or four
     sentences. -->

TakeMeter will classify complete public Hacker News comments from discussions
about AI model releases, AI explanations, and local-model tools. Its proposed
labels distinguish supported claims (`analysis`), requests for answers or
actions (`request`), and remaining opinions, reactions, or resource shares
(`commentary`). Each comment receives one label using the decision rules below.
The [Milestone 1 reading notes](milestone1_reading_notes.md) contain 36 linked
examples and three candidate distinctions from the community review.


---

## Label Taxonomy

<!-- Each label: a one-sentence definition and two real examples from your
     reading. Then your decision rule for the hardest boundary.

     The decision rule is worth a point on its own and it's the thing most
     people leave out. Every taxonomy has a hardest boundary. Name yours. -->

The taxonomy describes a comment's purpose and the support offered in its text.
Support is evaluated as presented, rather than independently fact-checked.
The [Milestone 2 boundary exercises](milestone2_taxonomy_check.md) record the
stress test. Real examples below use short excerpts; each source link opens
the complete comment.

### `analysis`

**Definition:** A comment that, without primarily seeking an answer or action,
explicitly states a substantive claim about a concrete result, behavior,
limitation, accessibility problem, or implication and connects it to a specific
reported observation, measurement, comparison, explanatory mechanism, or
relevant source passage.

**Example 1 — [apecjic's benchmark comparison](https://news.ycombinator.com/item?id=50130421), excerpt:**
> Overall 20% less tokens at each reasoning effort.

The complete comment describes a benchmark against earlier weights and links
the author's longer comparison; the measurements support the update assessment.

**Example 2 — [kgeist's throughput comparison](https://news.ycombinator.com/item?id=50134730), excerpt:**
> It says 46 tok/sec for Qwen3.6-27b 4 bit on RTX5090, but I get 60-70 tok/sec on a small context like that

The complete comment compares an estimate with reported results and identifies
quantization, cache settings, and speculation as variables the estimate misses.

### `request`

**Definition:** A comment whose main purpose is to seek information,
clarification, validation, advice, or a concrete change, even when it includes
detailed background or a hypothetical explanation, excluding rhetorical
questions and questions merely emphasizing a conclusion the comment has
already demonstrated.

**Example 1 — [dullcrisp's key/value question](https://news.ycombinator.com/item?id=50126359), excerpt:**
> For an LLM, the keys are the tokens in your context, and the values are … what exactly?

The author asks readers to explain a missing part of their understanding.

**Example 2 — [hizlikovboy27's workplace-use question](https://news.ycombinator.com/item?id=50128820), excerpt:**
> to what extent could your setup handle this kind of workflow and how accurate are the results?

The complete comment describes a database workflow as background for asking
whether the tool's estimates apply; that background does not answer the question.

### `commentary`

**Definition:** A comment that neither primarily seeks an answer or action nor
explicitly develops a supported substantive claim, instead expressing an
unsupported assertion, opinion, or reaction or simply sharing a resource,
including quoted wording used only to convey amusement, praise, or dislike.

**Example 1 — [hum3hum3's appreciation](https://news.ycombinator.com/item?id=50126371), complete comment:**
> The animated bird, the kea is absolutely fabulous.  I appreciate the effort and detail that went into this.

This expresses appreciation without developing a supported assessment.

**Example 2 — [jmward01's regulatory-motive claim](https://news.ycombinator.com/item?id=50132405), excerpt:**
> This model is why OpenAI and Anthropic want regulatory hurdles.

The complete comment advocates diversity, but offers no concrete example,
observation, or source that supports the claimed regulatory motive.

### How to choose exactly one label

Apply these steps to the complete comment, including its own explanation
around any quotation or link:

1. If the main purpose is to obtain an actual answer or action, choose
   `request`. Detailed background, a hypothetical worked example, or a
   proposed interpretation for readers to validate does not override this.
2. Otherwise, identify the main claim and the specific support offered for
   it. If both are present and connected, choose `analysis`.
3. Otherwise, choose `commentary`.

A rhetorical question, or a question pointing out an inconsistency the
comment has already demonstrated, does not by itself make the post a request.
An explicit request for a feature belongs to `request`; a bare announcement
or resource link belongs to `commentary` unless it develops a supported point.

Concrete support can be a described task outcome or failure without an
external citation. A model name, GPU name, number, link, or long quotation
alone does not qualify: it must support the writer's main point. A mechanism
must explain how or why the conclusion follows rather than simply repeat
the judgment. Length, confidence, sentiment, and agreement with the author
do not determine the label.

Do not infer an unstated analytical conclusion from a joke or expression of
feeling. If the writer only registers amusement, praise, or dislike about
wording or presentation, choose `commentary`, even when the trigger is quoted.
For `analysis`, the writer must also state a claim about a concrete result,
behavior, limitation, accessibility problem, or implication and connect
specific support to it. A quotation can support that claim; merely pointing
at amusing wording cannot substitute for it.

### The hardest boundary

**Which two labels:** `analysis` and `commentary`.

**Decision rule to apply consistently:** After ruling out a primary request,
choose `analysis` only when both the writer's main claim and a specific
observation, measurement, comparison, explanatory mechanism, or source passage
supporting it can be identified in the comment; otherwise choose `commentary`.

**Real borderline post:** [gitowiec's notation complaint](https://news.ycombinator.com/item?id=50132341)
combines a feeling of exclusion with a quoted passage of mathematical notation
and an unsuccessful attempt to fix the apparent rendering problem. It could
look like `commentary` because of the emotional response, or `analysis` because
of the specific example and reported troubleshooting. Under the written rule,
the proposed choice is **`analysis`**: those details support the accessibility
complaint. The emotional tone does not remove that support.

**Other difficult boundary:** A question with detailed background remains
`request` when it seeks an unresolved answer, such as
[the state-capital worked example](https://news.ycombinator.com/item?id=50131683).
In [tom_alexander's memory-fit report](https://news.ycombinator.com/item?id=50130918),
the comment demonstrates a specific contradiction and offers its own explanation
about CPU/GPU offloading; its concluding question highlights that contradiction,
so the proposed choice is `analysis`.

---

## The Dataset

<!-- Where you collected from, how you labelled, your counts, and three hard
     cases. -->

**Where the posts came from:** 240 complete public top-level comments from
20 Hacker News AI discussions, collected on October 17, 2026 (PDT) using the
[official Hacker News API](https://github.com/HackerNews/API). Story discovery
used AI-related title searches across four weekly windows in the preceding
28 days. The collector shuffled comment IDs with seed `20261017` and took
12 eligible comments per thread, without filtering by likely label or opinion.
Deleted, dead, empty, duplicate, and previously reviewed comments were excluded.
The final shuffle sets annotation order only; `labels.csv` remains unsplit.

[Source records](data/comment_sources.jsonl) retain each comment's permalink,
thread, author, timestamps, original HTML, and text hash. The
[collection manifest](data/collection_manifest.json) records sampling settings
and exclusions. The 36 Milestone 1 examples and synthetic boundary posts are
excluded from this dataset.

**How I labelled them:** <!-- Cold first? Pre-labelled with AI and corrected?
Say so plainly — the disclosure is required, not penalised. -->

All 240 records were pre-labelled with AI and then reviewed by me in three
batches, using [the first worksheet](cold20_worksheet.md),
[the second worksheet](unaided20_worksheet.md), and
[the bulk worksheet](remaining200_worksheet.md). Their reviewed labels are
now in `labels.csv`, with `AI-prelabelled; reviewed by student` in every note.
There are no blank labels or duplicate comments. The required unaided
annotations remain unmet. The three hard-case explanations below have been
reviewed. Training has not started.

The [draft snapshot](data/remaining_draft_labels.json) retains the initial
proposals for records 41–240, brief reasons, source IDs, and text hashes,
alongside a record of the completed review and import.

**Counts per label:**

These are the final counts in the unsplit, reviewed dataset.

| Label | Count | Share |
|---|---|---|
| `analysis` | 87 | 36.25% |
| `request` | 58 | 24.17% |
| `commentary` | 95 | 39.58% |
| **Reviewed total** | **240** | 100% |

The largest label is 39.58% of the dataset, meeting the assignment's 70% cap
and acceptance criterion 5's stricter 60% cap.

**Three hard cases**

<!-- Any post that made you pause: what it was, which two labels it could have
     been, and what you chose. These are worth more than the easy 190. -->

**1.**
> *The post:* [CSV record 120 — questions about confirmation dialogs and focus](https://news.ycombinator.com/item?id=50018945).
> The writer asks which agent workflows use the described dialogs and whether
> changing their focus behavior would solve the visibility problem.
>
> *Could have been:* `request` or `analysis`, because the questions include
> a technical explanation and a possible alternative fix.
>
> *I chose, because:* `request`. The writer still seeks workflow details and
> validation of the focus assumptions. The proposed explanation is conditional
> rather than a demonstrated result, so the unresolved questions determine
> the comment's primary purpose.

**2.**
> *The post:* [CSV record 205 — unfamiliar AI innovation](https://news.ycombinator.com/item?id=50037316).
> The writer predicts that AI innovation could become difficult to recognize,
> citing an unnamed mathematician's reported description of recent AI-generated
> mathematics as "alien-like."
>
> *Could have been:* `analysis` or `commentary`, because the prediction is
> speculative and its quoted support is second-hand.
>
> *I chose, because:* `analysis`. The writer states an explicit implication
> and connects the reported mathematics description to it as an illustration.
> That support is weak and unverified, but the taxonomy evaluates whether
> support is presented and connected, rather than whether the prediction
> has been proven.

**3.**
> *The post:* [CSV record 107 — the "technical dept" typo](https://news.ycombinator.com/item?id=49864195).
> The writer quotes advice about AI-assisted work, notices "dept" instead of
> "debt," and reacts to the wording as funny.
>
> *Could have been:* `commentary` or `analysis`, because the comment quotes
> a technical passage and interprets its wording.
>
> *I chose, because:* `commentary`. The quotation primarily supplies the
> trigger for amusement. Calling it true on a profound level does not explain
> a substantive conclusion or mechanism. The humor rule applies; a quotation
> alone does not make the comment analysis.

---

## The Training Run

<!-- Your starting model, your settings, and anything you changed and why. -->

**Base model:**

**Settings:** <!-- epochs, learning rate, batch size, seed -->

**Anything I changed from the defaults, and why:**

**Split sizes:** <!-- train / val / test, and per-label counts in the test
split. If a label had fewer than about 8 in test, say so — it explains a lot
of next unit's variance. -->



---

## How I Used AI

<!-- Two specific moments — what you asked, what came back, what you changed.

     ⚠️ Plus disclosure of any pre-labelling. If you had a model pre-label a
     batch and then read and corrected every one, say that. It's an allowed
     workflow and disclosing it costs you nothing. Not disclosing it is the
     problem. -->

**Moment 1**

- *What I asked for:* Help completing the project step by step, starting with setup.
- *What came back:* A working fork and local checkout, installed project dependencies and notebook kernel, and environment-check results.
- *What I changed:* The repository now has a local virtual environment and setup notes; the environment check confirmed Apple Silicon GPU (`mps`) access.

**Moment 2**

- *What I asked for:* An AI-news community recommendation, followed by reading 12 complete comments from each of three discussions, saving links, and identifying three differences in how opinions are expressed.
- *What came back:* A set of 36 linked comment summaries and three candidate distinctions for the taxonomy.
- *What I changed:* The project scope is Hacker News AI-news and tools discussions. The reading observations informed the proposed labels and boundary rules.

**Taxonomy assistance:** The label-definition draft, real-example selection,
borderline-case analysis, and eight synthetic boundary posts were prepared with
AI assistance. The synthetic examples are used only to stress-test the rules.

**Hard-case assistance:** AI helped select three boundary examples from the
reviewed dataset and draft explanations using their saved labels. I reviewed
all three explanations.

**Criteria assistance:** I used AI to propose initial numeric targets and draft
explanations before saving them in `criteria.md`. I reviewed the five targets
and explanations before manually committing the file as `7aa786e`.

**Collection assistance:** AI helped select AI-related discussion titles and
write and run `collect_comments.py`. The script collected complete comments,
recorded sources, and checked for duplicates. At collection time, it left every
label and note blank and generated no classification suggestions.

**Pre-labelling disclosure:**

At my request, AI proposed labels for the first 20 collected comments before
the required unaided batch was completed. I reviewed all 20 proposals, and
the saved labels were transferred into `labels.csv` with AI-prelabelling and
review notes. These records are not marked `cold`. This differs from the
assignment's required cold-first sequence, and Milestone 4 remains incomplete.
Any later unaided annotations must use fresh examples that have not received
AI classification help.

At my request, AI also proposed labels for records 21–40 in a second review
worksheet. I reviewed all 20, and their saved labels were imported into
`labels.csv` with the same AI-prelabelling and review notes. They do not
qualify as unaided annotations.

I then chose AI drafts for all remaining 200 comments, understanding that
the required 20 unaided annotations would remain unmet. I reviewed all 200
in `remaining200_worksheet.md`, and their saved labels were imported into
`labels.csv` with AI-prelabelling and student-review notes. All 240 collected
comments received AI classification help; none qualifies as an unaided
annotation. All 240 reviewed labels are now in `labels.csv`.

Milestone 1 reading notes and the Milestone 2 taxonomy examples and boundary
decisions were also prepared with AI assistance. Synthetic stress-test posts
are excluded from the real dataset.

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy |  |  |  |
| Macro F1 |  |  |  |
| F1 — `label_one` |  |  |  |
| F1 — `label_two` |  |  |  |

**What I predicted before I looked:**
<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A
     prediction made afterwards isn't one. -->

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->



---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

| true \ predicted |  |  |  |
|---|---|---|---|
| **** |  |  |  |
| **** |  |  |  |
| **** |  |  |  |

**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->



---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->



---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** ___ / 30 = ___%

<!-- Nobody grades this number. A 60% who argues every disagreement from the
     stated rules beats a 95% who wrote "staff was right" nine times. Several
     of the 30 were chosen because they're genuinely ambiguous — you should be
     winning some of these. -->

**Disagreements**

<!-- Three lines each: the post, both labels, and who you think is right and
     why — grounded in the staff definitions you were both applying.

     Then sort each into one of three piles:
       (a) the rule covered it and I applied it loosely → a consistency problem
       (b) the rule genuinely doesn't say               → a gap in the definitions
       (c) the rule is ambiguous here and my reading is defensible → argue it.
           This is a legitimate win.

     Pile (a) is the one that matters most for your diagnosis: if you applied a
     written rule two different ways on 30 posts, that is direct evidence about
     what you did across your own 200. -->

**1.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**2.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**What the pattern in my disagreements tells me:**



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Did it help, and how do I know:**

<!-- If it didn't, say so. Relabelling that didn't help is a genuinely
     interesting result and earns full credit. -->



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->



**The gap between what I meant my labels to capture and what the model
learned:**
<!-- Two sentences. Your confusion matrix is the evidence. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 5

       [ ] criteria.md has five numbered criteria, each naming a NUMBER
       [ ] Each has a reason underneath tied to your data or taxonomy
       [ ] labels.csv: at least 200 rows, text/label/note, ONE file not split
           (150–199 only under the assignment's documented time-limit exception)
       [ ] No label above 70%
       [ ] All five unit 5 sections have real content
       [ ] Label Taxonomy includes the decision rule for your hardest boundary
       [ ] The Dataset includes three hard cases
       [ ] results.json and test_split.csv written by the notebook and committed manually
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 6

       [ ] Baseline vs. Trained table, with your prediction written beforehand
       [ ] Run Log — Before, five criteria across three seeds
       [ ] Confusion matrix TYPED AS A MARKDOWN TABLE
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, using the agreement report as evidence
       [ ] Agreement Report with every disagreement adjudicated
       [ ] One improvement, with Run Log — After
       [ ] What's Still Broken
       [ ] results_three_seeds_before.json, results_three_seeds_after.json,
           baseline_results.json and
           agreement_results.json committed
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
