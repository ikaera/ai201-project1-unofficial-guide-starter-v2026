# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**

Four questions have very specific facts in single sentences:
- "Wait times at Kestrel Commons?" → "20 to 25 minutes"
- "Laundry cost at Aldridge Hall?" → "$1.75"
- "Distance to science quad?" → "four minutes"
- "Drop after week two?" → "shows as W on transcript"

One question is harder because the answer is buried in a paragraph with other information about deadlines, so retrieval might get the document but not the exact sentence with "second week".

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**

Naming a source is all-or-nothing. When the system generates an answer, it either always includes the document name or never does. There's no middle ground — it's built into how the system works, not something that sometimes works and sometimes doesn't. If sourcing is working, all 5 answers will have sources. If it's broken, none will.

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

<!-- The five questions are the ones in `OUT_OF_SCOPE` at the bottom of
     `questions.py`, and `run_eval.py` puts them through the gate and writes
     what happened into your run log. Swap them for your own if you'd rather —
     just keep five of them, or the "4 of 5" above has nothing to be 4 of. -->

**Why this target:**

Most out-of-scope questions are completely unrelated to campus life (Mongolia, oil changes, World Cup, ibuprofen). But one question — "How do I write a for loop in Rust?" — might accidentally match CS course documents, even though it's not about campus. The other four should definitely get refused. That's why I expect 4 of 5 to be stopped, with one possibly slipping through.

---

## 4. Something about your chunks

At least 4 of 5 sampled chunks contain between 100 and 400 characters, with no chunk ending mid-sentence.

<!-- YOU WRITE THIS ONE.

     How would you know if your chunks were the right size? Name something
     countable or observable.

     Examples of the right shape — don't copy these, they should come from
     what you actually saw in Milestone 3:
       - "At least 4 of 5 sampled chunks read as a complete thought, with no
          sentence cut in half at either end."
       - "No chunk is shorter than 200 characters, since anything below that
          in my corpus turned out to be a heading with no content under it." -->



**Why this target:**

- Documents in my corpus average 317 characters
- Chunks between 100-400 characters fit whole ideas without splitting sentences
- 100 characters minimum prevents tiny "junk" chunks (just headings)
- 400 characters maximum prevents mixing unrelated topics
- 4 of 5 accounts for rare edge cases where formatting is unusual

---

## 5. Your choice

At least 4 of 5 answers include a direct quote of at least 8 words from the source document.

<!-- YOU WRITE THIS ONE TOO.

     Pick something you actually care about getting right. It could be about
     speed, about refusals, about a particular kind of question your corpus
     handles badly, about source attribution being correct rather than merely
     present — anything, as long as it names a number or an observable
     outcome. -->



**Why this target:**

- Direct quotes prove answers come from the source, not made up
- 8 words is the minimum to be meaningful (longer than just 1-2 word fragments)
- 8 words is short enough to fit naturally into an answer
- 4 of 5 allows one answer to be paraphrased when a quote doesn't fit smoothly

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
