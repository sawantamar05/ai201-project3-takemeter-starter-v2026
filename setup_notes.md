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

## Remaining build milestones

1. Collect at least 200 complete real comments into one unsplit `labels.csv`,
   retaining source links. Collection can use the
   [official public API](https://github.com/HackerNews/API).
2. Label the first 20 unaided and mark them `cold`; use fresh examples that
   have not received AI classification help.
3. Label the remaining examples, personally reviewing every AI pre-label.
   Record three hard cases. Check the assignment's 70% maximum class share
   and the chosen acceptance criterion's stricter 60% maximum.
4. Commit the dataset manually, run notebook sections 1–5, and manually commit
   the resulting `results.json` and `test_split.csv`.
5. Complete the five unit 5 README sections, verify at least four new commits,
   push manually, and submit the fork URL in the Course Portal.

## Git checkpoint before every new step

Check `git status` before moving to another project step and flag any changes
that need review. Do not stage, commit, or push automatically: the user runs
Git commands manually. When a commit is appropriate, explain what is ready
and provide commands limited to the relevant files. Report uncommitted changes
and local commits that have not been pushed.
