# CURRENT_TASK

**Status:** Session 5 complete. No task in progress.

## Just completed (2026-08-08)

**Module 01's solution debt is closed — the repo's oldest open item.** ~37k words across 10 files
on branch `module/01-foundations-solutions`. Module 01 shipped in Session 1 with 9 dangling
links, before the write-solutions-in-the-same-commit convention existed. **The repo now has zero
dangling solution links** except one, noted below.

- **`_solutions/` for all 6 exercise sets** — lessons 02 through 07. Every doc had recorded this
  as "4 missing files"; there were 6. See the caution in `docs/HANDOFF.md`.
- **`vocabulary.md`** — the full module glossary: risk terms, the six functions, the timely
  detection symbols, zones, CPTED, requirements, the nine failure categories, plus a
  routinely-confused disambiguation table.
- **`checklist_foundations.md`** — the reasoning checklist. Eight sections of questions, not
  facts, ending with the five questions that catch the most.
- **`exercises.md`** — a per-lesson exercise index **plus the module capstone**: Ashford Public
  Library, one site through all 7 lessons, Parts A–G, with a full reference solution in
  `_solutions/exercises_solutions.md`. This gives module 01 the capstone it lacked and matches
  modules 32 and 35.

**Every calculation was computed by running `psec` and transcribing** — E3.2 and the capstone's
Part B with `psec.pps`, E6.4 with `psec.optics`, E7.2 with `psec.power`. Per the module 32
convention.

**Stale link fixed:** `01_Foundations/03_functional_chain.md` pointed at
`28_Calculators/timely_detection.py`, superseded by `psec/pps.py` in Phase 3. It now points at
`psec/pps.py` and at `32_Engineering_Math/08_adversary_path.md`.

**The capstone is a library on purpose.** Every other worked example in the module is a
warehouse, an office, or a server room. A library inverts the assumptions — the mission is
unrestricted public access and the primary asset is staff — so most of the module's instincts
produce the wrong answer, which is what the exercise tests.

## Next task

**`03_Video_Surveillance/` lessons 01–11.**

Why this next: it is the largest technical module, roadmap months 3–4 depend on it, and it is now
fully unblocked. **Module 32 lessons 01–04 supply all of its math** — FOV, pixel density and
DORI, bandwidth, storage and retention — so these lessons can cover the imaging chain, camera
selection, and design judgment without re-deriving anything. Cross-reference module 32 rather
than repeating it.

Scope (from PHASES.md Phase 7): 11 lessons through the imaging chain, plus the retail case study
and Projects 2 and 4.

**Method:** `psec.optics` and `psec.video` already implement the math and module 32 already
derives it. **Do not hand-write a number into any lesson** — run `psec` and transcribe, as
modules 01, 32, and 35 all now do.

**Quality bar:** `32_Engineering_Math/06_voltage_drop.md`,
`35_Doors_and_Hardware/03_locking_hardware_families.md`, and
`01_Foundations/03_functional_chain.md`.

**Module shape to match** (01, 32, and 35 are the reference): overview, lessons, `_solutions/`
for every lesson written in the same commit, a capstone exercise with a reference solution, a
quiz with an isolated key, and a validated flashcard deck.

**Before starting:** read `docs/AI_CONTEXT.md` and `docs/HANDOFF.md`.

**Before finishing:**
1. Run the verification commands in `HANDOFF.md`, plus the link check
2. Update `COURSE_PROGRESS.md`, `PHASES.md`, `ENGINEERING_LOG.md`
3. Commit content + docs together, push, merge to `main`

## The last remaining solution debt

`30_Capstones/data_center_campus/00_BRIEF.md` links to `_reference_solution/`, which does not
exist. It is `COURSE_PROGRESS.md` known issue 4 and is the **only broken link left in the repo**.
It is a large piece of work (25 deliverables) and depends on `20_Data_Center/`, so it is
sequenced after that module rather than treated as a quick fix.

---

## The one item blocked on a human

**Verify ASIS APP/PSP domains, weightings, and eligibility** against the official ASIS
Certification Handbook (asisonline.org returns 403 to automated fetch, so an agent cannot do
this). Until then, `22_APP/` and `23_PSP/` must not be built — the provisional figures in
`31_References/source_index.md` are from exam-dump vendors and are flagged low-confidence.

This is not urgent: the roadmap doesn't start the APP track until month 6.

**Three** provisional mapping tables need correcting when this clears:
`01_Foundations/00_MODULE_OVERVIEW.md`, `35_Doors_and_Hardware/00_MODULE_OVERVIEW.md`, and
`32_Engineering_Math/00_MODULE_OVERVIEW.md`.
