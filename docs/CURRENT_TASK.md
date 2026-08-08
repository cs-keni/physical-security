# CURRENT_TASK

**Status:** Session 3 complete. No task in progress.

## Just completed (2026-08-07)

**Module 35 Doors and Hardware is finished.** Sessions 2 and 3 together produced ~58k words
across 21 files. It is the first complete module in the repo — 8 lessons, solutions for every
lesson, a capstone field exercise, a quiz with an isolated key, and a validated flashcard deck.

Session 3 added, on branch `module/35-doors-hardware-part2`:

- **06 — Electrified Hardware and Power Transfer:** the four transfer methods, conductor
  budgeting, and the voltage-drop calculation carried *through* the transfer. Deliberately
  continues lesson 03's worked example — the same opening, and 12 AWG stops being the answer
  once the last six feet are counted.
- **07 — Fire-Rated Openings:** the assembly concept, labels and what voids them, the four
  behaviors, and the derivation of every rated-opening hardware restriction from "a fire door
  must latch."
- **08 — Key Management and Mechanical Security:** the key hierarchy, rekey triggers, the three
  controls that do the work, construction key turnover, and the no-override decision.
- `_solutions/` for 06–08 plus a reference findings set for the survey.
- **`_exercises/10_door_survey.md`** — the module capstone: survey ten real openings against a
  full recording template and write a ranked findings memo.
- **`25_Quizzes/quiz_35_doors_hardware.md`** + isolated answer key (30 questions).
- **`26_Flashcards/35_doors_hardware.csv`** — 77 cards, validated.

## Next task

**`32_Engineering_Math/` lessons 01–07.**

Why this next: `28_Calculators/` is tested and working but the derivations that justify it are
unwritten, so a learner can use a calculator they don't understand — which the repo's own
architecture explicitly separated modules 28 and 32 to prevent. Module 35 lessons 03 and 06 now
lean on `psec.power` in three worked examples and forward-reference `32_Engineering_Math/` for
the derivations, so the gap is visible to a learner following the roadmap.

Scope (from PHASES.md Phase 6):
1. Camera FOV and focal length
2. Pixel density and DORI
3. Bandwidth
4. Storage and retention
5. PoE budgets
6. Voltage drop and conductor selection — **this one now has to reconcile with module 35 lesson
   06's multi-segment example.** The derivation should cover summing drops across segments of
   different gauge, because that is the case that actually catches people.
7. Adversary path and timely detection

**Method:** write each lesson *from* `28_Calculators/tests/test_psec.py`. Every test's expected
value is a hand calculation waiting to be shown. Include problem sets with answer keys in
`_answer_keys/` or `_solutions/`.

**Quality bar:** `35_Doors_and_Hardware/03_locking_hardware_families.md` and
`01_Foundations/03_functional_chain.md`.

**Module shape to match** (module 35 is the reference): overview, lessons, `_solutions/` for
every lesson written in the same commit, a capstone exercise, a quiz with an isolated key, and a
validated flashcard deck.

**Before starting:** read `docs/AI_CONTEXT.md` and `docs/HANDOFF.md`.
Branch: `module/32-engineering-math` off `main`.

**Before finishing:**
1. Run the verification commands in `HANDOFF.md`, plus the link check
2. Update `COURSE_PROGRESS.md`, `PHASES.md`, `ENGINEERING_LOG.md`
3. Commit content + docs together, push, merge to `main`

---

## The one item blocked on a human

**Verify ASIS APP/PSP domains, weightings, and eligibility** against the official ASIS
Certification Handbook (asisonline.org returns 403 to automated fetch, so an agent cannot do
this). Until then, `22_APP/` and `23_PSP/` must not be built — the provisional figures in
`31_References/source_index.md` are from exam-dump vendors and are flagged low-confidence.

This is not urgent: the roadmap doesn't start the APP track until month 6.

**Two** provisional mapping tables now need correcting when this clears:
`01_Foundations/00_MODULE_OVERVIEW.md` and `35_Doors_and_Hardware/00_MODULE_OVERVIEW.md`.
