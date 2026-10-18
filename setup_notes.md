# TakeMeter setup and progress

Setup completed October 17, 2026.

- Fork: https://github.com/sawantamar05/ai201-project3-takemeter-starter-v2026
- Upstream: https://github.com/codepath/ai201-project3-takemeter-starter-v2026
- Python: 3.11.0, with an isolated `.venv` in this repository.
- Installed the starter requirements and `ipykernel` for notebook support.
- `python test.py`: **9 passed, 0 failed, 1 warning**.
- PyTorch: 2.14.1; detected device: **mps (Apple Silicon GPU)**.
- RAM: 16 GB; free disk after package installation: 23.7 GB.
- Expected warning: the unit 6 baseline model has not been downloaded yet.

The sandbox initially reported CPU; the same check outside the sandbox
confirmed MPS availability. Record the device used by the actual training
run in the final README and results.

## Resume in Terminal

```bash
cd "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project3-takemeter-starter-v2026"
source .venv/bin/activate
python test.py
```

To recreate the environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt ipykernel
```

Open `takemeter.ipynb` in VS Code, select this repository's
`.venv/bin/python` as the notebook kernel, and run section 1's first cell.
Do not use Run All: the later sections require the finished dataset and
criteria, and sections 6–7 belong to the next unit.

## Milestones 1–3: recorded materials

**Community:** Hacker News commenters discussing AI news and tools, treating
each complete public comment as one post.

| Milestone | Recorded material |
|---|---|
| 1 | [Reading notes](milestone1_reading_notes.md): 36 unique comment links, collection details, paraphrased notes, and three candidate distinctions; personal review confirmed by the user |
| 2 | README taxonomy: three definitions, two real examples each, and boundary rules; [eight synthetic exercises](milestone2_taxonomy_check.md); matching baseline definitions and notebook labels; taxonomy review confirmed by the user |
| 3 | `criteria.md`: five numeric targets with explanations, covering accuracy, per-label performance, and balance; reviewed and manually committed before training as `7aa786e` |

## Criteria review and commit

The five targets and draft explanations were reviewed in the conversation.
The accuracy explanation was updated, and the remaining targets and reasons
were retained. The reviewed file was manually committed as `7aa786e` before
training. This records review and adoption of the AI-assisted draft.

The README's **How I Used AI** section records the assistance used.

## Milestone 4: collection checkpoint

Collected 240 complete public Hacker News comments on October 17, 2026 (PDT):
12 comments from each of 20 AI-related discussions across four weekly windows.
At collection time all labels and notes were blank. The dataset is unsplit,
with no duplicate comment IDs or normalized texts and no overlap with the
36 reading examples.

- `collect_comments.py`: collection script with overwrite protection.
- `data/collection_stories.json`: title-based source selection and discovery details.
- `data/comment_sources.jsonl`: source metadata and original HTML aligned to CSV records.
- `data/collection_manifest.json`: collection settings, exclusions, and first-20 reservation.
- `labels.csv`: 240 records with exactly `text,label,note` columns.

The collection checkpoint was manually committed as `5df3d88` and pushed.
The manifest records the original reservation of the first
20 **data records** for unaided annotation. At the user's later request,
those records received AI draft labels in `cold20_worksheet.md`. The user
confirmed review of all 20, and the saved labels were transferred into
`labels.csv` with `AI-prelabelled; reviewed by student` notes. The reviewed
counts at that checkpoint were 9 `analysis`, 4 `request`, and 7 `commentary`,
with 220 records blank. These 20 reviewed records are not eligible for `cold` notes. The
reviewed annotations were manually committed as `3cd207e` and pushed.

The README records this departure from the required cold-first sequence.
Unaided annotations must use fresh comments without classification help.
Comments can contain line breaks, so CSV data records are not the same as
physical file lines. No records are marked `cold` yet.

At the user's request, AI proposed labels for CSV records 21–40 in
`unaided20_worksheet.md`. The user confirmed review of this second batch,
and its saved labels were imported with `AI-prelabelled; reviewed by student`
notes. The complete comment text, source links, and order are preserved.
At that checkpoint the totals were 40 reviewed records (14 `analysis`,
9 `request`, 17 `commentary`), 200 records with blank labels and notes, and
zero `cold` records. The second worksheet, reviewed annotations, and documentation were
manually committed as `0b9af49` and pushed. Git was clean and synced before
preparing the bulk drafts below.

The user chose AI drafts for all remaining 200 comments, acknowledging that
the unaided requirement would remain unmet. `remaining200_worksheet.md`
contains the reviewed labels for records 41–240, with complete text and source
links. The user confirmed review of all 200, and the saved labels were imported
with `AI-prelabelled; reviewed by student` notes.
`data/remaining_draft_labels.json` records the initial draft labels, brief
reasons, uncertainty flags, IDs, and hashes, plus the review/import confirmation.
All 240 comments have now received classification help and are ineligible for
the required unaided annotations.

The final unsplit dataset has 240 reviewed labels: 87 `analysis` (36.25%),
58 `request` (24.17%), and 95 `commentary` (39.58%). It has zero blank labels,
zero duplicate comments, and zero `cold` notes. All original comment text and
row order are preserved. The largest class meets both the assignment's 70%
cap and acceptance criterion 5's 60% cap. Training has not started.

## Remaining build milestones

1. Manually commit the completed 240 annotations, bulk worksheet, draft
   snapshot with review confirmation, and updated documentation.
2. Record and review three hard cases. Retain the disclosure of the unmet
   unaided requirement and earlier cold-first sequence deviation.
3. Commit the completed annotations manually, run notebook sections 1–5, and manually commit
   the resulting `results.json` and `test_split.csv`.
4. Complete the five unit 5 README sections, verify at least four new commits,
   push manually, and submit the fork URL in the Course Portal.

## Git checkpoint before every new step

Check `git status` before moving to another project step and flag any changes
that need review. Do not stage, commit, or push automatically: the user runs
Git commands manually. When a commit is appropriate, explain what is ready
and provide commands limited to the relevant files. Report uncommitted changes
and local commits that have not been pushed.
