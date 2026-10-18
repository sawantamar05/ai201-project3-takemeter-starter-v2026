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

## Community reading progress

Selected scope: **Hacker News commenters discussing AI news and tools**,
treating each complete public comment as one post. At the student's request,
Codex retrieved and reviewed 12 complete comments from each of three threads.
The 36 source links, paraphrased reading notes, and three candidate distinctions
are in [milestone1_reading_notes.md](milestone1_reading_notes.md).

Collection can later use the official public API:
https://github.com/HackerNews/API. Keep full comment text and source links;
prefer comments that can be understood on their own.

Student review of the AI-assisted reading notes and sources is pending.
The taxonomy, acceptance criteria, and labeled dataset have not been completed.
No training has been run.

Next, review the observations against the linked comments, then proceed in order:

1. Design 2–4 labels, with two real examples each and a boundary rule.
2. Write and commit five personal acceptance criteria with numeric targets
   and reasons, covering at least three required areas, before training.
3. Collect at least 200 real posts into one unsplit `labels.csv`.
4. Personally label the first 20 without AI help and mark them `cold`.
5. Label the rest; review every AI pre-label and disclose its use. Record
   three hard cases and verify no label exceeds 70% of the dataset.
6. Commit the dataset, run notebook sections 1–5, and commit `results.json`
   and `test_split.csv`.
7. Complete the five unit 5 README sections, ensure at least four new commits,
   push, and submit the fork URL in the Course Portal.

AI helped with repository setup, dependency installation, environment
verification, the community recommendation, and the 36-comment source review.
Continue updating the final README's AI disclosure with the specific
interactions actually used during the work.
