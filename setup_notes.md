# TakeMeter setup and progress

Setup completed October 17, 2026.

- Fork: https://github.com/sawantamar05/ai201-project3-takemeter-starter-v2026
- Upstream: https://github.com/codepath/ai201-project3-takemeter-starter-v2026
- Python: 3.11.0, with an isolated `.venv` in this repository.
- Installed the starter requirements and `ipykernel` for notebook support.
- `python test.py`: **9 passed, 0 failed, 1 warning**.
- PyTorch: 2.14.1; detected device: **mps (Apple Silicon GPU)**.
- RAM: 16 GB; free disk after package installation: 23.7 GB.
- Initial setup warning: the baseline model had not been downloaded. The
  download and first baseline run were completed in Part 2.

The sandbox initially reported CPU; the same check outside the sandbox
confirmed MPS availability. The actual seed-42 training run used `mps`
(Apple Silicon GPU), recorded in the executed notebook, README, and results.

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
`.venv/bin/python` as the notebook kernel, and inspect the saved outputs.
Sections 1–5 are complete. Do not use Run All: sections 6–7 belong to unit 6.

## Milestones 1–3: recorded materials

**Community:** Hacker News commenters discussing AI news and tools, treating
each complete public comment as one post.

| Milestone | Recorded material |
|---|---|
| 1 | I reviewed the [reading notes](milestone1_reading_notes.md): 36 unique comment links, collection details, paraphrased notes, and three distinctions I adopted. |
| 2 | I reviewed and adopted the README taxonomy: three definitions, two real examples each, boundary rules, and [eight synthetic exercises](milestone2_taxonomy_check.md), with matching baseline definitions and notebook labels. |
| 3 | I reviewed five numeric targets and explanations in `criteria.md`, covering accuracy, per-label performance, and balance, and manually committed them before training as `7aa786e`. |

## Criteria review and commit

I reviewed the five AI-assisted targets and explanations, adopted the updated
accuracy explanation, and retained the other targets and reasons. I manually
committed the reviewed file as `7aa786e` before training.

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

I manually committed and pushed the collection checkpoint as `5df3d88`.
The manifest is a collection-time snapshot: it records the original blank
labels and first-20 reservation, rather than the completed annotation review.

I requested AI draft labels for records 1–20 in `cold20_worksheet.md`, reviewed
all 20, and accepted the labels saved in `labels.csv` with
`AI-prelabelled; reviewed by student` notes. At that checkpoint there were
9 `analysis`, 4 `request`, and 7 `commentary` labels, with 220 records blank.
I manually committed and pushed the reviewed annotations as `3cd207e`.

I requested and reviewed the second batch of 20 AI draft labels in
`unaided20_worksheet.md`. The accepted labels were imported with the same
review notes, preserving the complete text, source links, and order.
At that checkpoint there were 40 reviewed records (14 `analysis`, 9 `request`,
17 `commentary`) and 200 blank records. I manually committed and pushed the
second worksheet, reviewed annotations, and documentation as `0b9af49`.

I reviewed the remaining 200 labels in `remaining200_worksheet.md` and accepted
the final labels saved in `labels.csv`. `data/remaining_draft_labels.json`
preserves the initial AI proposals and completed review/import confirmation.
The README documents the annotation method. No record is marked `cold`.
Comments can contain line breaks, so CSV records differ from physical lines.

The final unsplit dataset has 240 reviewed labels: 87 `analysis` (36.25%),
58 `request` (24.17%), and 95 `commentary` (39.58%). It has zero blank labels,
zero duplicate comments, and zero `cold` notes. All original comment text and
row order are preserved. The largest class meets both the assignment's 70%
cap and acceptance criterion 5's 60% cap.

I manually committed and pushed the complete annotation checkpoint as
`443e00c`. Three hard-case explanations are recorded in
the README for records 120 (`request`), 205 (`analysis`), and 107
(`commentary`). Their links and explanations match the saved labels and
taxonomy. I reviewed and adopted all three explanations, then manually
committed and pushed the reviewed documentation as `5e80f8d`.

## Milestone 5: training run

The notebook now uses the Git author identity and the adopted labels
`analysis`, `request`, and `commentary`. The base model is
`distilbert-base-uncased`; settings are 3 epochs, learning rate `2e-5`, batch
size 16, maximum input length 256 tokens, and seed 42.

The input limit increased from the starter's 128 tokens because 26 comments
exceed 128 whitespace words, including 22 analysis comments. This is a length
proxy used before training. A subsequent check with the cached tokenizer
found 42 comments over 128 tokens and 12 over 256 tokens, including special
tokens. The latter comprise 10 analysis and 2 request comments and are
truncated by the model. Full text stays in the CSV.

The seed-42 run matched the preflight: 168 train, 36 validation, and 36 test
records. Test counts are 13 analysis, 9 request, and 14 commentary. Source
rows and texts are disjoint across splits, with all three labels represented.

The notebook's validation now stops execution on invalid data. The complete
dataset passes without warnings. Nine regression cases correctly stop:
missing, empty, whitespace-only, noncanonical, unknown, or entirely missing
labels; a missing note column; an empty dataset; and empty text. All code cells
compile. Installed dependencies have no reported conflicts, and the notebook's
training arguments match the installed Transformers 4.57.6 API.

No model or tokenizer was downloaded during the preflight. I manually
committed and pushed the prepared notebook and documentation as `e83e834`
before execution.

Notebook sections 1–5 completed on October 18, 2026 (PDT), using `mps`
(Apple Silicon GPU), PyTorch 2.14.1, and the committed settings above. The run
downloaded the public DistilBERT files and generated `results.json` and
`test_split.csv`; the notebook contains all eight executed Unit 5 code cells.
Sections 6–7 remain unexecuted for unit 6.

Artifact verification passed: the held-out CSV exactly matches the
deterministic seed-42 test split; the confusion counts, accuracy, per-label
metrics, and macro F1 agree; the dataset, criteria, and notebook source are
unchanged by execution.

Held-out accuracy is 0.5278 (19/36), and macro F1 is 0.3996. Per-label F1:
analysis 0.6471, request 0.0000, commentary 0.5517. The model made no request
predictions. The accuracy and request-F1 targets are missed on this run;
analysis F1, commentary F1, and dataset balance meet their targets for this
checkpoint. Criteria remain unchanged. The three-seed test belongs to unit 6.

## Part 1 repository checkpoint

The executed notebook, training results, held-out split, and reviewed
documentation were manually committed and pushed as `2a9b37d`. The required
files and five README sections are present. Course Portal submission has
not been confirmed in this conversation.

## Part 2: testing progress

I predicted that my trained model would score higher overall than the
baseline and manually committed and pushed that prediction as `9c5f3a9`
before baseline execution.

The baseline ran with `python baseline.py --trained results.json`, using
`facebook/bart-large-mnli`, the unchanged definitions, and all 36 original
held-out comments. It used `mps:0` (Apple Silicon GPU) and took 49.87 seconds
including model loading and the first download. It generated
`baseline_results.json`; the README contains the comparison table.

Baseline accuracy is 17/36 (0.4722), compared with 19/36 (0.5278) for the
trained model. Macro F1 is 0.3580 versus 0.3996. Neither model predicted
`request`. The prediction is supported on this split, with a margin of two
comments. Saved predictions exactly match the held-out row order, and
independently calculated metrics match the saved scores. Part 1 data,
criteria, definitions, model configuration, and outputs remain unchanged.

### Remaining testing milestones

1. Review and manually commit and push the baseline results and write-up.
2. Run the unchanged model across seeds 42, 7, and 2024, preserving
   `results_three_seeds_before.json`, and record the typed confusion matrix.
3. Independently label all 30 staff posts under `data/staff_taxonomy.md` and
   save `my_staff_labels.csv` before obtaining or opening the TF's answer key.
   Then run the agreement check and adjudicate every disagreement.
4. Judge all five original criteria and diagnose each miss using evidence.
5. Make one diagnosed improvement and rerun the same three seeds, preserving
   `results_three_seeds_after.json`, then compare the before and after logs.
6. Finish the write-up, verify at least four new Part 2 commits, push manually,
   and submit the same repository URL through the Course Portal.

## Git checkpoint before every new step

I run Git commands manually. Before each new project step, check `git status`
and flag changes that need review. Do not stage, commit, or push automatically.
When a commit is appropriate, explain what is ready and provide commands
limited to the relevant files. Report uncommitted changes and local commits
that have not been pushed.
