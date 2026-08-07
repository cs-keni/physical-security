# How to Use This Academy

Read this once. It will save you months.

---

## 1. The core problem this curriculum solves

Most physical security engineers learn by osmosis: they mark up drawings for two years,
absorb their firm's house style, and eventually develop instincts they cannot explain.
That works, slowly, and it produces engineers who are excellent inside their firm's habits
and lost outside them.

This academy inverts that. You will learn **the reasoning first**, then the artifacts.
Every device you place will be traceable to an asset, a threat, a consequence, and a
required function. When a client asks "why is there a camera there?", the answer is never
"that's how we always do it."

---

## 2. Why passive reading fails, and what to do instead

You have a CS degree. You already know that reading a book about compilers does not let
you write one. Same here.

The evidence-backed learning techniques this curriculum is built on:

| Technique | What it means here | Where you'll see it |
|---|---|---|
| **Retrieval practice** | Answer before you look | Every module ends with quiz-before-solution |
| **Spaced repetition** | Re-meet facts at increasing intervals | `26_Flashcards/` + the review schedule below |
| **Interleaving** | Mix camera math with door hardware, don't block | The roadmap deliberately alternates topics |
| **Elaboration** | Explain *why*, out loud, in your own words | The "explain it to an architect" prompts |
| **Worked example → faded example → solo** | Scaffolded problem solving | `32_Engineering_Math/` problem sets |
| **Generation effect** | Attempt before instruction | Labs give you the site *before* the lesson |

**Rule: never read a solution file before producing your own answer.** The solutions live
in `_solutions/` and `_answer_keys/` folders precisely so you can't skim them by accident.
If you look first, you will feel like you understood it and you will not have.

---

## 3. The weekly cadence (designed around a full-time job)

Target **6–8 hours/week**. Sustainable beats heroic. A realistic week:

| Slot | Duration | Activity |
|---|---|---|
| Mon evening | 45 min | New lesson — read + take notes in your own words |
| Tue evening | 45 min | New lesson continued, or calculations |
| Wed | 20 min | Flashcard review only (spaced repetition) |
| Thu evening | 45 min | Lab / design exercise — produce something |
| Sat morning | 2–3 hr | Deep work: project, drawing review, or capstone increment |
| Sun | 30 min | Quiz + review misses + update `progress_tracker.md` |

**Protect the Saturday block.** Design skill is built by designing, and designing needs
uninterrupted time. Everything else is negotiable.

### The flashcard schedule

Import `26_Flashcards/*.csv` into Anki (free) or any SRS. Do them **daily, 10–20 minutes**,
even on days you do nothing else. The default Anki settings are fine. Do not build your own
scheduler — that is procrastination disguised as engineering.

---

## 4. The three notebooks you must keep

This curriculum assumes you maintain three artifacts *outside* this repo:

1. **A field notebook.** Every time you're on a site walk, in a coordination meeting, or
   reviewing a package, write down: one term you didn't know, one decision someone made and
   why, and one thing that surprised you. Review monthly. This is where the real curriculum
   lives; this repo just gives you the scaffolding to hang it on.

2. **A question log.** Whenever you don't understand something a senior engineer said,
   write it down verbatim rather than nodding. Batch the questions and ask them weekly.
   Asking five good questions once a week reads as engaged; asking one vague question a day
   reads as needy.

3. **A decision journal.** For every design decision you make, record: what you chose, what
   you rejected, what you assumed, and what would change your mind. In six months, read it.
   This is the single fastest way to build calibrated engineering judgment, because it
   forces you to confront the decisions where you were confident and wrong.

---

## 5. How to study a module

Every module follows the same 20-part structure (objectives → beginner → engineering depth
→ vocabulary → diagrams → calcs → examples → tradeoffs → mistakes → junior/senior → checklist
→ exercises → scenarios → quiz → explanations → flashcards → references → lab → cert mapping).

The efficient path through it:

```
1. Read the LEARNING OBJECTIVES.
2. Take the QUIZ cold. You will do badly. That is the point —
   failed retrieval primes learning better than successful reading.
3. Read the BEGINNER + ENGINEERING sections.
4. Do the CALCULATIONS by hand before running the Python calculator.
5. Do the LAB. Produce an artifact.
6. Retake the quiz. Read the answer explanations even for the ones you got right.
7. Add the flashcards to your SRS deck.
8. Write three sentences in your decision journal about the biggest tradeoff in the module.
```

Steps 2 and 8 are the ones everyone skips. They are the ones that work.

---

## 6. Using your software background as leverage (and where it will mislead you)

**Where it helps enormously:**

- Systems thinking, signal tracing, and failure-mode analysis are the same skills as
  debugging a distributed system.
- A PACS is a distributed system with a database, an API, edge nodes, and a message bus.
  A VMS is a media pipeline with ingest, transcode, storage tiering, and a query layer.
  You already understand these shapes.
- Structured data. Most security engineers manage device data in ad-hoc spreadsheets.
  You can build a real data model (`16_Automation/data_model/`) and it will be a genuine
  differentiator within a year.
- Automation of QA. Drawing/schedule/spec coordination is a graph-consistency problem.

**Where it will actively mislead you:**

| Software instinct | Why it fails in physical security |
|---|---|
| "Just deploy a fix" | A wrong device location costs a truck roll, a lift, a ceiling patch, and a change order. There is no hot reload. |
| "Fail closed for security" | Fail *secure* on an egress door can kill people. Life safety outranks security, always. |
| "Redundancy is cheap" | A redundant camera is a real capital cost, a real port, a real license, and real maintenance forever. |
| "The spec is the source of truth" | Drawings, specs, schedules, and submittals all disagree, and resolving that disagreement *is the job*. |
| "Move fast" | Your errors get poured into concrete. Construction documents are effectively immutable after bid. |
| "The user will figure it out" | The user is a fatigued guard at 3 a.m. If your design requires attention, your design has failed. |
| "Latest version is best" | Firmware on a life-safety-adjacent system is updated deliberately, on change control, after regression testing. |

Write that table down. The second column is 80% of what separates a software engineer
playing at security design from a security engineer.

---

## 7. Verification discipline (non-negotiable)

This material was authored with care, but **you are the engineer of record for your own
knowledge**. Two rules:

1. **Anything tagged `[VERIFY]` must be confirmed** against a primary source (the adopted
   code edition, the manufacturer's current datasheet, the AHJ) before it appears in a
   deliverable with your name on it.
2. **Codes are jurisdiction- and edition-specific.** "The IBC says…" is not a sentence a
   competent engineer finishes without knowing which edition the jurisdiction adopted and
   what local amendments apply. This curriculum teaches you the *shape* of the requirements
   and how to find the current text. It is not a substitute for the code books.

Log every source you verify in `31_References/source_index.md`. Future-you will need it.

---

## 8. Certification timing

Do not chase certifications early. The order that works:

- **Months 1–6:** learn the engineering. Certification material will feel obvious later.
- **Month ~6:** confirm APP eligibility against the current ASIS Certification Handbook,
  then begin `22_APP/` as a *parallel* track, ~2 hr/week.
- **Months 9–12:** sit the APP.
- **PSP:** requires more years of experience than you have. `23_PSP/` runs as slow
  background study; by the time you're eligible, the exam should be a formality rather than
  a cram.
- **CPP:** a management credential for later in your career. `24_CPP_Roadmap/` exists so you
  can see how today's work feeds it, not so you can study for it now.

**Always verify current eligibility, domains, and fees against the official ASIS
Certification Handbook.** Third-party summaries — including the ones cited in this
repo — go stale.

---

## 9. What "done" looks like at 12 months

You can be handed an architectural background for a facility you have never seen, and
produce: a defensible risk-informed security concept, a device layout with justified
coverage, a door schedule with sequences of operation, storage/bandwidth/PoE/power
calculations, a Division 28 outline spec, a riser, a commissioning plan, and a written
Basis of Design that explains every major decision — and defend all of it in a design
review against a skeptical senior engineer.

That is the target. Now go to `study_roadmap.md`.
