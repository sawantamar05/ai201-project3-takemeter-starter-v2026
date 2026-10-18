# Acceptance criteria — TakeMeter

Five criteria that say what "working" means for this classifier, written in
unit 5 **before** anything was trained.

**All five are yours this time.** None are given. You've had two projects of
practice.

An acceptance criterion names a number. *"The model is accurate"* is an
opinion. *"Every label has an F1 of at least 0.60 on the held-out set"* is a
criterion.

Under each, write a sentence or two on **why that number**. A reason that says
something about your data or your taxonomy earns credit — *"I picked 0.60 F1
for `reaction` because it's my smallest label and I only have about 50
examples of it"*. A reason that could be attached to any project does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

Not numbers that sound impressive. Uniformly guessing among three labels has
an expected accuracy of about 33%; always guessing the largest class has a
different baseline determined by its share. Your target should sit somewhere
you'd honestly call useful.

**Cover at least three of these five areas.** They're here as prompts, not as a
form to fill in — a criterion that fits none of them is fine if it names a
number.

| Area | A question it could answer |
|---|---|
| Overall accuracy | How often does it need to be right to be worth using? |
| Per-label performance | Is one label allowed to be much worse than the others? |
| Balance | How lopsided can your label counts get before it's a problem? |
| Consistency | If someone else labelled the same posts, how often should you agree? |
| Confidence | Should a confident prediction be right more often than an unsure one? |

Two things worth knowing before you pick numbers, because both will affect
whether you hit them:

- **Your smallest label will have the jumpiest score.** If a label has 50
  examples, about 8 land in the test split. An F1 computed on 8 examples moves
  a lot between seeds. A target for that label should be looser than one for
  your biggest label, and saying so is a good reason.
- **Unit 6 tests across three seeds, and the target has to hold across all
  three.** A target of 0.65 against results of 0.71, 0.62, 0.68 is a **miss**.
  Pick with that in mind — it is stricter than it first sounds.

---

## 1. Overall accuracy

Overall accuracy must be at least 0.65 on held-out data.

**Why this target:**

I would consider TakeMeter useful if it correctly classified at least
65 out of 100 unseen AI discussion comments. Distinguishing supported
analysis from commentary can be subtle, so this target allows some
boundary mistakes while requiring most predictions to be correct.

---

## 2. Analysis performance

The `analysis` label must achieve an F1 score of at least 0.60
on held-out data.

**Why this target:**

The boundary between supported analysis and commentary is difficult.
This target requires reasonable performance in both finding analysis
and avoiding incorrect analysis predictions.

---

## 3. Request performance

The `request` label must achieve an F1 score of at least 0.60
on held-out data.

**Why this target:**

Requests can contain detailed technical background that resembles
analysis. The classifier should recognize genuine requests for
information or action despite that background.

---

## 4. Commentary performance

The `commentary` label must achieve an F1 score of at least 0.55
on held-out data.

**Why this target:**

Commentary includes varied reactions, unsupported opinions, and
resource shares. The slightly lower target reflects this variety
while still requiring meaningful classification performance.

---

## 5. Dataset balance

No label may account for more than 60% of the final, unsplit
`labels.csv` dataset.

**Why this target:**

This is stricter than the assignment's 70% limit and reduces the
advantage of always predicting the largest class.

---

For criteria 1–4, each target must be met independently for every
evaluation seed: 42, 7, and 2024. These three-seed checks occur in
Unit 6; a passing average alone does not satisfy a criterion.



---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 6 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Every label performs acceptably

         The model performs well on all labels.

         **Why this target:** ...

         > **Revised in unit 6:** Every label has an F1 of at least 0.60 on
         > the held-out set.
         >
         > **Why revised:** "performs well" gave me nothing to check. I
         > couldn't produce a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "Overall accuracy of at least 0.65" → "at least 0.55", because
            0.65 turned out to be optimistic for 200 examples.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
