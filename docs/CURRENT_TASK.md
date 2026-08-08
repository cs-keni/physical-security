# CURRENT_TASK

**Status:** Session 4 complete. No task in progress.

## Just completed (2026-08-08)

**Module 32 Engineering Math is finished.** ~55k words across 19 files on branch
`module/32-engineering-math`. It is the second complete module in the repo, and the first whose
entire purpose is to be the **derivation record for working code** — `test_psec.py`'s own
docstring says its expected values are hand-computed in these lessons, so all 68 tests now trace
to a derivation written out in prose.

- **01–08 lessons** with `_solutions/` for every one, written in the same commit: camera FOV and
  focal length, pixel density and DORI, bandwidth, storage and retention, PoE budgets and switch
  capacity, voltage drop and conductor selection, battery and supply sizing, adversary path and
  timely detection.
- **`_exercises/integrated_sizing.md`** — the module capstone. One fictional 3PL distribution
  centre sized end to end through all eight lessons: cameras → FOV → PPF → bitrate → storage →
  PoE → voltage drop → battery → adversary path. **The design fails four times before it works**,
  which is the point: the exercise tests noticing that an answer is unacceptable, not computing
  it. Full reference solution in `_solutions/integrated_sizing_reference.md`, including a worked
  basis-of-design memo.
- **`25_Quizzes/quiz_32_engineering_math.md`** + isolated answer key (30 questions, 52 points,
  weighted toward calculation).
- **`26_Flashcards/32_engineering_math.csv`** — 80 cards, validated.

**Two real `psec` defects were found by working the units by hand**, both fixed with new tests
(**66 → 68**). Details in `docs/HANDOFF.md` under "Session 4 carry-overs" and in
`COURSE_PROGRESS.md` known issue 7. The one worth remembering: `stream_gb_per_day(decimal_gb=
False)` divided decimal megabytes by 1024, halving the reported decimal/binary gap — the exact
error its own docstring warned about, invisible to a test asserting only `binary < decimal`.

**Deliberate deviation from PHASES.md's lesson list**, recorded with rationale in Phase 6:
rack/port/capacity planning folded into `05_poe.md`, and lesson 08 became the adversary path
derivation because `psec/pps.py` had substantial tested math and no derivation anywhere.

## Next task

**`01_Foundations/_solutions/`** — the 4 missing exercise solution files, plus `vocabulary.md`
and `checklist_foundations.md`.

Why this next: it is the repo's oldest open debt, it is small, and closing it makes "every
lesson's solutions exist" true repo-wide for the first time. Modules 32 and 35 both adopted the
write-solutions-in-the-same-commit convention; module 01 predates it and is the only remaining
violation.

Scope:
1. `_solutions/02_risk_vocabulary_solutions.md`
2. `_solutions/03_functional_chain_solutions.md`
3. `_solutions/04_zones_solutions.md`
4. `_solutions/05_cpted_solutions.md`
5. `_solutions/06_requirements_solutions.md`
6. `_solutions/07_systems_failure_solutions.md`
7. `vocabulary.md` and `checklist_foundations.md` (linked from the module overview)

Also fix while in there: `01_Foundations/03_functional_chain.md` links to
`28_Calculators/timely_detection.py`, which no longer exists — it was superseded by `psec/pps.py`.
Point it at `psec/pps.py` and at `32_Engineering_Math/08_adversary_path.md`, which now derives it.

**After that:** `03_Video_Surveillance/` lessons 01–11. Module 32 lessons 01–04 now supply all of
its math, so those lessons can cover the imaging chain, camera selection, and design judgment
without re-deriving anything.

**Quality bar:** `32_Engineering_Math/06_voltage_drop.md`,
`35_Doors_and_Hardware/03_locking_hardware_families.md`, and
`01_Foundations/03_functional_chain.md`.

**Module shape to match** (32 and 35 are the reference): overview, lessons, `_solutions/` for
every lesson written in the same commit, a capstone exercise with a reference solution, a quiz
with an isolated key, and a validated flashcard deck.

**Before starting:** read `docs/AI_CONTEXT.md` and `docs/HANDOFF.md`.

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

**Three** provisional mapping tables now need correcting when this clears:
`01_Foundations/00_MODULE_OVERVIEW.md`, `35_Doors_and_Hardware/00_MODULE_OVERVIEW.md`, and
`32_Engineering_Math/00_MODULE_OVERVIEW.md`.
