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

TakeMeter classifies complete public Hacker News comments from discussions
about AI model releases, AI explanations, and local-model tools. Its adopted
labels distinguish supported claims (`analysis`), requests for answers or
actions (`request`), and remaining opinions, reactions, or resource shares
(`commentary`). Each comment receives one label using the decision rules below.
The [Milestone 1 reading notes](milestone1_reading_notes.md) contain 36 linked
examples and three distinctions I adopted after reviewing the reading notes.


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
my adopted choice is **`analysis`**: those details support the accessibility
complaint. The emotional tone does not remove that support.

**Other difficult boundary:** A question with detailed background remains
`request` when it seeks an unresolved answer, such as
[the state-capital worked example](https://news.ycombinator.com/item?id=50131683).
In [tom_alexander's memory-fit report](https://news.ycombinator.com/item?id=50130918),
the comment demonstrates a specific contradiction and offers its own explanation
about CPU/GPU offloading; its concluding question highlights that contradiction,
so my adopted choice is `analysis`.

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

I reviewed all 240 AI-prelabelled records against my adopted taxonomy in
batches of 20, 20, and 200, using [the first worksheet](cold20_worksheet.md),
[the second worksheet](unaided20_worksheet.md), and
[the bulk worksheet](remaining200_worksheet.md). I accepted the final labels
saved in `labels.csv`, with `AI-prelabelled; reviewed by student` in every note.

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

**Status:** Notebook sections 1–5 completed on October 18, 2026 (PDT).
The executed notebook, `results.json`, and `test_split.csv` record the run.

**Base model:** `distilbert-base-uncased`.

**Settings:** 3 epochs, learning rate `2e-5`, batch size 16, maximum input
length 256 tokens, and seed 42. The run used `mps` (Apple Silicon GPU), with
PyTorch 2.14.1, as recorded in the notebook and `results.json`.

**Anything I changed from the defaults, and why:** I adopted the AI-assisted
recommendation to increase `MAX_LENGTH` from 128 to 256 before training.
Of the 240 comments, 26 exceed 128 whitespace
words, including 22 labelled `analysis`. Keeping more input should help retain
the observations and reasoning that distinguish analysis from commentary.
Word counts were a proxy used before training. A subsequent check with the
cached tokenizer found 42 comments longer than 128 tokens and 12 longer than
256 tokens (10 `analysis`, 2 `request`, including special tokens). Those 12
inputs are truncated at 256 tokens; the complete comments remain in `labels.csv`.

The dataset check now rejects missing or blank labels, unknown label names,
surrounding spaces, missing required columns, and empty datasets. It raises
an error on invalid input. All 240 project records pass without warnings.

**Split sizes:** The seed-42 run used the following stratified 70/15/15
split. No held-out label has fewer than eight examples.

| Label | Train | Validation | Test |
|---|---:|---:|---:|
| `analysis` | 61 | 13 | 13 |
| `request` | 40 | 9 | 9 |
| `commentary` | 67 | 14 | 14 |
| **Total** | **168** | **36** | **36** |

**Held-out results:** Accuracy was 0.5278 (19 of 36 correct), and macro F1
was 0.3996.

| Label | F1 | Test examples |
|---|---:|---:|
| `analysis` | 0.6471 | 13 |
| `request` | 0.0000 | 9 |
| `commentary` | 0.5517 | 14 |

The model made no `request` predictions: four of the nine requests were
predicted as `analysis` and five as `commentary`. This first run misses the
accuracy and request-F1 targets. The analysis and commentary F1 targets are
met for seed 42, and the dataset balance target is met. The targets are
unchanged. The Part 2 sections below record the three-seed evaluation.

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
- *What I changed:* I used the project virtual environment and manually committed the setup checkpoints. The environment check confirmed Apple Silicon GPU (`mps`) access.

**Moment 2**

- *What I asked for:* An AI-news community recommendation, followed by reading 12 complete comments from each of three discussions, saving links, and identifying three differences in how opinions are expressed.
- *What came back:* A set of 36 linked comment summaries and three candidate distinctions for the taxonomy.
- *What I changed:* I adopted Hacker News AI-news and tools discussions as the project scope. I reviewed the reading notes and adopted the labels and boundary rules they informed.

**Taxonomy assistance:** I reviewed and adopted the AI-assisted label
definitions, real examples, boundary rules, and eight synthetic boundary
exercises. I kept the synthetic examples out of the real dataset.

**Hard-case assistance:** I reviewed and adopted all three hard-case
explanations drafted with AI assistance, using the saved labels and taxonomy.

**Training assistance:** I used AI assistance to prepare the notebook's
dataset validation and 256-token input limit. I manually committed the
configuration before the AI-assisted execution of sections 1–5 and verification
of the generated results and held-out split.

**Criteria assistance:** I used AI to propose initial numeric targets and draft
explanations before saving them in `criteria.md`. I reviewed the five targets
and explanations before manually committing the file as `7aa786e`.

**Part 2 testing assistance:** I supplied my prediction and manually committed
it before the baseline run. I used AI assistance to execute the baseline,
verify its saved predictions and scores, and prepare the comparison below.
I also used AI assistance to execute the three unchanged before trials,
verify the saved metrics, and prepare the run log and typed confusion matrix.
AI also checked the saved split counts and training logs and drafted the
criterion verdicts and diagnoses below, distinguishing observed failures
from possible causes.
For Milestone 5, AI helped implement and execute the declared six-epoch
experiment, verify the three after results, and prepare the comparison.
AI also helped draft the final limitations and two-sentence explanation
of the gap between the intended labels and the observed model behavior.

**Staff annotation assistance:** At my request, AI drafted labels and short
rule-based reasons for all 30 staff posts before the staff answer key was
available. I reviewed all 30 labels and reasons on October 22, 2026, and
retained them without changes in `staff_labeling_worksheet.md` and
`my_staff_labels.csv`. This departs from the instruction to label these posts
independently, so the comparison measures AI-assisted annotation agreement
rather than my unaided rule application. After committing these labels as
`91691d1`, I supplied the staff key. AI helped run and verify the comparison
and lay out both interpretations of the one disagreement. I chose to accept
staff's `hot_take` label and classify the disagreement as pile (a).

**Collection assistance:** I used AI assistance to select AI-related discussion
titles and create and run `collect_comments.py`. The script collected complete
comments, recorded sources, and checked for duplicates. At collection time,
it left every label and note blank and generated no classification suggestions.

**Pre-labelling disclosure:**

I requested AI draft labels and reviewed all three batches: records 1–20,
21–40, and 41–240. I accepted the final labels saved in `labels.csv` and
manually committed the reviewed annotation checkpoints. Every record retains
its AI-prelabelling and student-review note. I did not complete the required
20 unaided annotations before AI prelabelling, and none of these 240 records
is marked `cold` or qualifies as unaided.

I also reviewed the AI-assisted Milestone 1 reading notes and adopted the
Milestone 2 taxonomy examples and boundary decisions. The synthetic stress-test
posts remain separate from the real dataset.

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

The baseline is `facebook/bart-large-mnli`, using the unchanged definitions
in `label_definitions.txt`. It classified all 36 comments in the committed
`test_split.csv`, matching the Part 1 trained model's held-out test set.
The trained scores below are the existing Part 1 results. The baseline ran
with `python baseline.py --trained results.json` on `mps:0` (Apple Silicon
GPU); total wall time was 49.87 seconds, including model loading and the
first download. This is not an inference-only timing measurement.

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy | 0.472 | 0.528 | +0.056 |
| Macro F1 | 0.358 | 0.400 | +0.042 |
| F1 — `analysis` | 0.519 | 0.647 | +0.129 |
| F1 — `request` | 0.000 | 0.000 | +0.000 |
| F1 — `commentary` | 0.556 | 0.552 | -0.004 |

Difference means trained minus baseline, calculated before rounding.

**What I predicted before I looked:**
<!-- Record the prediction BEFORE running or seeing the baseline results.
     The Part 1 trained-model results are already known. -->

I predict that my trained model will score higher overall than the baseline.

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->

The trained model got 19 of 36 comments right, compared with 17 for the
baseline: an advantage of two comments, or 5.6 percentage points. This
supports my prediction on this test set. The trained model had higher
`analysis` F1, slightly lower `commentary` F1, and the same zero `request`
F1. Neither model predicted any comments as `request`. This comparison applies
to the original test set. The three-seed run below measures the trained
model's scores across different splits; the baseline has only been scored
on the original test set.



---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

These are the **before** trials, with no improvement applied. Each trial
uses the unchanged 240-row dataset, taxonomy, criteria, and Part 1 settings:
`distilbert-base-uncased`, 3 epochs, learning rate `2e-5`, batch size 16, and
256 tokens. The device was `mps` (Apple Silicon GPU), with PyTorch 2.14.1.
Every split has 168 training, 36 validation, and 36 test comments. The seed
changes both the split and training randomness.

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1. Overall accuracy | ≥ 0.65 | 0.528 | 0.500 | 0.750 | MISSED |
| 2. `analysis` F1 | ≥ 0.60 | 0.647 | 0.585 | 0.867 | MISSED |
| 3. `request` F1 | ≥ 0.60 | 0.000 | 0.000 | 0.000 | MISSED |
| 4. `commentary` F1 | ≥ 0.55 | 0.552 | 0.545 | 0.848 | MISSED |
| 5. Largest unsplit class share | ≤ 60% | 39.58% | 39.58% | 39.58% | MET |

Criteria 1–4 must pass on every seed, using unrounded scores. The 75% result
on seed 2024 does not offset the lower accuracy on seeds 42 and 7. Analysis
and commentary F1 miss their targets on seed 7. Criterion 5 is a property of
the same unsplit dataset in every trial: 95/240 = 39.5833%; the repeated value
is not three independent measurements.

Macro F1, an additional measure rather than an adopted criterion, was 0.400,
0.377, and 0.572 for seeds 42, 7, and 2024, respectively.

**Stability:** Accuracy ranges from 50.0% to 75.0%, a spread of **25 percentage
points**, exceeding the assignment's ten-point concern threshold. These
results are sensitive to the seed. Each test split contains only 36 comments,
so one changed answer moves accuracy by about 2.8 percentage points. The
spread alone does not identify whether label application, sample size, or
training randomness is responsible. The completed staff comparison below
provides a limited check on applying an evidence rule, rather than isolating
the cause of this spread.

All three runs made zero `request` predictions and missed all nine requests
in their test splits. Seed 2024 correctly classified every non-request
comment, so its higher accuracy still hides the complete failure on requests.

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

**Before, seed 42 — 36 held-out comments.** This is one trial's matrix,
not an aggregate across all three seeds. Rows are true labels; columns are
predictions.

| true \ predicted | analysis | request | commentary |
|---|---|---|---|
| **analysis** | 11 | 0 | 2 |
| **request** | 4 | 0 | 5 |
| **commentary** | 6 | 0 | 8 |

**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->

Six true `commentary` comments were predicted as `analysis`, compared with
two true `analysis` comments predicted as `commentary`. This run leans toward
`analysis` on that pair. The matrix also shows all nine requests going to
the other labels: four to `analysis` and five to `commentary`. These are
observed error patterns; the diagnoses below use the completed agreement
report with its limits made explicit.



---

## Verdicts and Diagnoses

These verdicts and diagnoses refer to the **before** trials. The after
verdicts and measured changes appear under **The Improvement** below.

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 | Overall accuracy | ≥ 0.65 on every seed | MISSED | Seeds 42 and 7 scored 0.5278 and 0.5000; seed 2024's 0.7500 does not cancel either miss. |
| 2 | `analysis` F1 | ≥ 0.60 on every seed | MISSED | Seed 7 scored 0.5854; seeds 42 and 2024 passed at 0.6471 and 0.8667. |
| 3 | `request` F1 | ≥ 0.60 on every seed | MISSED | All three scores were 0.0000; no run predicted this label. |
| 4 | `commentary` F1 | ≥ 0.55 on every seed | MISSED | Seed 7 scored 0.54545, below 0.55; seeds 42 and 2024 passed at 0.5517 and 0.8485. |
| 5 | Largest unsplit class share | ≤ 60% | MET | `commentary` is the largest class: 95 of 240 comments, or 39.58%. This is one measurement of the fixed dataset. |

The verdicts use unrounded scores. All five criteria are measurable; none
has been revised or lowered.

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->

**1. Overall accuracy: missed requests plus unstable analysis/commentary separation.**
Every trial missed all nine test requests. That alone limits accuracy to
27/36 = 75%, which seed 2024 reached by getting every non-request right.
Seeds 42 and 7 also misclassified eight and nine non-requests, respectively,
leaving accuracy at 19/36 and 18/36. The persistent request failure and the
varying analysis/commentary errors explain the accuracy misses. The
25-percentage-point spread shows sensitivity to the seed; the seed changes
both the split and training randomness, so it does not isolate either cause.

**2. Analysis F1: too many other comments are called analysis.**
On seed 7, the model predicted `analysis` for 28 of 36 comments, but only
12 were correct. Eight requests and eight commentary comments became false
analysis predictions. Recall was high at 12/13 = 0.9231, while precision
was only 12/28 = 0.4286, producing F1 of 0.5854. The miss comes from
overpredicting analysis, rather than failing to find most actual analysis.
The working diagnosis is weak separation of technical subject matter from
the comment's purpose and supporting evidence. The staff disagreement below
makes loose evidence-rule application a plausible labeling risk, but does
not establish that my Hacker News annotations caused these errors.

**3. Request F1: the smaller intent class has not been learned under this setup.**
Requests are present in every training split: 40 examples, compared with
61 analysis and 67 commentary examples. All nine test requests were missed
in each run. These include seed-42 test record 2, which asks whether an
accepted cybersecurity practitioner must apply again, and record 21, which
shares benchmark links and then asks for more projects. Their main purpose
is seeking an answer, even though they contain background or resources.
The failure therefore extends beyond difficult analysis/commentary cases.
Limited examples and training are plausible contributors: the model received
only 33 updates over three epochs, and validation loss was still falling
at the final epoch on every seed. For example, seed 7's validation loss fell
from 1.0696 to 1.0437 to 1.0338. This supports incomplete learning as a
working hypothesis; it does not prove that more training will fix requests.
The staff taxonomy has no request label, so its agreement score cannot
validate this boundary or rule out annotation problems here.

**4. Commentary F1: low recall on seed 7 exposes the analysis boundary.**
Seed 7 correctly recognized only six of fourteen commentary comments;
the other eight went to analysis. Precision was 6/8 = 0.7500, but recall
was 6/14 = 0.4286, giving F1 of 0.54545 and missing 0.55. Commentary is
the largest class, so being the smallest label is not an explanation for
this miss. The working diagnosis is a difficult, unstable boundary between
supported claims and varied unsupported opinions or reactions. Seed 42
also sent six commentary comments to analysis, while seed 2024 sent none.
The staff evidence-rule disagreement is relevant to this distinction,
but does not identify which Hacker News comments, if any, were mislabeled.

**What the agreement report adds, and what remains uncertain.**
The 29/30 agreement includes one pile-(a) disagreement: I accepted that I
treated a decorative statistic as sufficient support. That gives a specific
rule-application risk to investigate, rather than permission to assume every
technical comment is analysis. However, these were AI-assisted annotations
on another topic under different definitions. The high rate neither proves
nor rules out inconsistent Hacker News labeling, and cannot explain the
request failure by itself. The saved trained-model results contain aggregate
confusion counts, not individual predictions, so I cannot name particular
analysis/commentary errors from them. The request errors above are known
because the model predicted zero requests. The next single improvement
should prioritize that persistent failure and test a stated hypothesis.
At this diagnostic checkpoint, no data, labels, taxonomy, criteria, or model
settings had been changed. The one selected improvement is documented below.



---

## Agreement Report

**Status:** Comparison and adjudication complete. I reviewed all 30 staff
labels and reasons on October 22, 2026, retained them without changes, and
committed them as `91691d1` before supplying or opening the staff key. The
[labeling worksheet](staff_labeling_worksheet.md) still matches
`my_staff_labels.csv`: 11 `analysis`, 9 `hot_take`, and 10 `reaction`.
The staff key contains 10 of each label. All 30 posts matched, with no missing,
extra, or duplicate entries. There is one disagreement, adjudicated below.

This exercise uses the [staff taxonomy](data/staff_taxonomy.md) for a
fictional running forum: `analysis`, `hot_take`, and `reaction`. The Hacker
News training taxonomy remains unchanged. The supplied key is saved unchanged
as `data/staff_labels.csv`; `python agreement.py` produced
[agreement_results.json](agreement_results.json). The AI-assisted annotation
workflow is disclosed in **How I Used AI** above.

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** 29 / 30 = 96.7%. The script displays 97% after rounding.
This measures agreement with staff under the staff rules, not classifier accuracy.

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

**1. Post 14 (`sp_014`): evidence versus a decorative statistic**
> *The post:* Times are down about 3% since the shoe rules changed, so obviously the shoes are the whole story and the sport has a problem.
>
> *Staff said / I said:* `hot_take` / `analysis`.
>
> *My call, and why:* I accept `hot_take`. I originally read the statistic and
> "so" as a premise supporting a conclusion, which resembles the analysis
> example in rule 1. After considering both readings, I read "obviously,"
> "the whole story," and "the sport has a problem" as the central unsupported
> judgment. The 3% change does not establish that shoes explain everything;
> here it decorates that sweeping judgment. Rule 1 already distinguishes a
> fact that carries an argument from a statistic used as a flourish. I applied
> that distinction too loosely.
>
> *Which pile:* (a) The written rule covered the boundary, but I applied it loosely.

Pile counts: (a) 1, (b) 0, (c) 0. I preserved the original `analysis` label
in `my_staff_labels.csv` and the worksheet so the comparison continues to
measure the annotations saved before seeing the key.

**What the pattern in my disagreements tells me:**

My one disagreement concerns whether a statistic actually supports a claim.
That suggests checking the supported-analysis versus unsupported-commentary
boundary in my Hacker News data, where the seed-42 model called six commentary
posts analysis. The staff taxonomy and topic differ from that dataset, however,
and these annotations were AI-assisted. One disagreement does not prove that
my Hacker News labels are inconsistent or explain why the trained model never
predicts `request`. Those causes still need separate evidence.


---

## The Improvement

**What I changed:**

Declared before the after runs: increase `EPOCHS` from 3 to 6. Six epochs
double the training passes and updates, from 33 to 66 per run, to test whether
the original budget stopped learning too early. Each seed starts a fresh
DistilBERT model. The dataset, labels, taxonomy, criteria, seeds 42/7/2024,
initial learning rate `2e-5`, batch size 16, and maximum length of 256 tokens
stay the same. The existing learning-rate decay schedule now spans the
longer run. `RUN_LABEL = "after"` only directs the new results to
`results_three_seeds_after.json`, preserving the before artifact.

**Which diagnosis pointed at it:**

The request label was never predicted, and the final validation loss was
still decreasing on all three before trials. That makes incomplete learning
a plausible contributor. Doubling the epoch count is one bounded test of
that hypothesis; it might improve request recognition, leave it unchanged,
or overfit. Six epochs were selected before seeing any after results, and
there will be no further tuning in this improvement experiment.

**Execution status:** All three six-epoch runs completed on October 22, 2026,
using `mps` (Apple Silicon GPU), PyTorch 2.14.1, and the same seed-matched
168/36/36 train/validation/test splits. Results are saved in
[results_three_seeds_after.json](results_three_seeds_after.json), and the
notebook contains the actual after outputs. Training took about 57 seconds
per seed; the complete execution took 181.4 seconds. The original
three-epoch results, before artifact, baseline, and test split are preserved.

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1. Overall accuracy | ≥ 0.65 | 0.556 | 0.583 | 0.750 | MISSED |
| 2. `analysis` F1 | ≥ 0.60 | 0.667 | 0.667 | 0.929 | MET |
| 3. `request` F1 | ≥ 0.60 | 0.200 | 0.000 | 0.000 | MISSED |
| 4. `commentary` F1 | ≥ 0.55 | 0.552 | 0.667 | 0.800 | MET |
| 5. Largest unsplit class share | ≤ 60% | 39.58% | 39.58% | 39.58% | MET |

Verdicts use unrounded scores and require every seed to pass. The balance
row repeats the unchanged 95/240 dataset measurement, not three independent
measurements. Macro F1 was 0.473, 0.444, and 0.576, respectively.

**Matched before and after results** (before → after):

| Measure | Seed 42 | Seed 7 | Seed 2024 |
|---|---|---|---|
| Accuracy | 0.528 → 0.556 | 0.500 → 0.583 | 0.750 → 0.750 |
| `analysis` F1 | 0.647 → 0.667 | 0.585 → 0.667 | 0.867 → 0.929 |
| `request` F1 | 0.000 → 0.200 | 0.000 → 0.000 | 0.000 → 0.000 |
| `commentary` F1 | 0.552 → 0.552 | 0.545 → 0.667 | 0.848 → 0.800 |

**After, seed 42 — 36 held-out comments:**

| true \ predicted | analysis | request | commentary |
|---|---|---|---|
| **analysis** | 11 | 0 | 2 |
| **request** | 3 | 1 | 5 |
| **commentary** | 6 | 0 | 8 |

The largest off-diagonal count is still six commentary comments predicted
as analysis, versus two analysis comments predicted as commentary. This
boundary's seed-42 counts did not improve. One request is now correct;
eight of nine are still missed.

**Did it help, and how do I know:**

<!-- If it didn't, say so. Relabelling that didn't help is a genuinely
     interesting result and earns full credit. -->

The improvement helped partially. Three criteria now pass, compared with
one before: analysis F1 and commentary F1 newly pass on every seed, while
balance remains met. Accuracy improved by one correct comment on seed 42
(+2.8 percentage points) and three on seed 7 (+8.3 points), and stayed
unchanged on seed 2024. Its spread narrowed from 25.0 to 19.4 percentage
points, which still exceeds the assignment's ten-point concern threshold.

The intended request fix is mostly unsuccessful: seed 42 predicts one
request and gets it right, giving recall 1/9 and F1 0.20; the other seeds
still predict zero requests. Longer training therefore did not resolve
the main intent boundary. There is also a regression: seed 2024's commentary
F1 fell from 0.8485 to 0.8000 because seven requests were called commentary,
up from five before. Its overall accuracy stayed at 27/36; the errors
shifted between the other labels.

These matched trials support a limited benefit from the declared change,
with the remaining accuracy and request criteria still missed. They do
not establish incomplete training as the sole cause, or show that more
epochs would keep helping. The experiment stops at the predeclared six
epochs; no second improvement or further tuning was performed.



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->

**Criterion 1 — overall accuracy ≥ 0.65: still missed.**
After the change, accuracy is 0.5556, 0.5833, and 0.7500. The first two
seeds remain below the target, and the 19.4-percentage-point spread shows
that the result is still sensitive to the split and training randomness.
In a future experiment, I would audit the analysis/commentary training
examples against the written rules with a second reviewer. Any boundary
correction would then be tested on a larger, newly labeled set from additional
Hacker News threads, so its benefit is measured beyond the small 36-comment
test sets. I stopped this experiment after its one declared change; a
boundary correction and fresh evaluation require a separate experiment.

**Criterion 3 — request F1 ≥ 0.60: still missed.**
After F1 is 0.2000, 0.0000, and 0.0000. Seed 42 recognizes one of nine
requests, while the other seeds recognize none. A separate future experiment
would add 30 new, carefully reviewed request examples to the training
data, including questions with technical background, resource lists, and
requests for action. I would keep the definitions fixed and have another
annotator check the labels to investigate inconsistent rule application.
That would test whether more varied examples help the model learn intent.
I stopped after the predeclared six-epoch comparison because another data
change would require its own recorded experiment and evaluation; these
additional examples were not collected or used in the reported runs.

The analysis F1, commentary F1, and balance criteria are met, but the model
is not yet reliable at distinguishing genuine requests. The original targets
remain in place, and no second improvement was performed.


**The gap between what I meant my labels to capture and what the model
learned:**
<!-- Two sentences. Your confusion matrix is the evidence. -->

I intended the labels to capture whether a comment offers supported analysis,
genuinely asks for an answer or action, or gives commentary. In the after run
for seed 42, the model still misclassified eight of nine requests and called
six commentary comments analysis, showing that it learned those distinctions
incompletely.

**Submission repository:**
[sawantamar05/ai201-project3-takemeter-starter-v2026](https://github.com/sawantamar05/ai201-project3-takemeter-starter-v2026)


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
