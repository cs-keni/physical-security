# CURRENT_TASK

**Status:** Session 2 complete. No task in progress.

## Just completed (2026-08-07)

**`35_Doors_and_Hardware/` lessons 01–05 at full depth** (~18k words of lessons, ~10.4k words
of solutions), on branch `module/35-doors-hardware`:

- Module overview with objectives, study guidance, cross-references, provisional cert mapping
- **01 — Door Anatomy:** the opening as the unit of design; frame, leaf, hinges, latching,
  closers; reading a door schedule and a hardware set
- **02 — Handing, Swing, Secure Side:** the four hands, the field procedure, where each
  security device goes, why handing errors are always schedule impacts
- **03 — Locking Hardware Families:** the five electrified families, selection framework,
  door position vs. latch position, worked power-supply / battery / voltage-drop calculations
- **04 — Fail Safe vs. Fail Secure:** the five failure modes, why fail secure does not trap
  anyone, why the fire alarm release must be hardwired
- **05 — Egress:** free egress, means of egress, the special locking arrangements, how to
  respond when a client asks you to lock an exit. Every code claim `[CODE][VERIFY]`.
- `_solutions/` for all five lessons, written alongside — deliberately **not** repeating the
  Module 01 dangling-solutions debt

Numeric examples in lesson 03 and its solutions were computed with `psec.power` and are
reproducible: see the verification block in `HANDOFF.md`.

## Next task

**`35_Doors_and_Hardware/` lessons 06–08**, then the module's assessment material.

Why this next: lesson 03 forward-references power transfer to lesson 06 in three places, and
lesson 05's "Next" link points at 06. Roadmap month 4 pairs `04_Access_Control/` with
`35/03–06`, so 06 is the first binding constraint. Month 8 needs 07.

Scope:
6. Electrified hardware and power transfer — electric hinges, door loops, EPTs, voltage drop
   across the leaf, coordination with `34_Electrical_Power/` and `psec.power`
7. Fire-rated openings — label requirements, what may not be modified, positive latching,
   hold-opens, the inspection/testing obligation `[CODE][VERIFY]`
8. Key management and mechanical security — keying schedules, master key hierarchy, why
   mechanical security is still the real perimeter
Plus: the 10-door field exercise, `25_Quizzes/quiz_35_doors.md` + isolated answer key,
`26_Flashcards/35_doors_hardware.csv`, and `_solutions/` for 06–08 alongside the lessons.

**Quality bar:** match `35_Doors_and_Hardware/03_locking_hardware_families.md` and
`01_Foundations/03_functional_chain.md`. ~3–4k words per lesson.

**Before starting:** read `docs/AI_CONTEXT.md` and `docs/HANDOFF.md`.
Branch: `module/35-doors-hardware-part2` off `main`.

**Before finishing:**
1. Run the verification commands in `HANDOFF.md`
2. Update `COURSE_PROGRESS.md`, `PHASES.md`, `ENGINEERING_LOG.md`
3. Commit content + docs together, push, merge to `main`

---

## The one item blocked on a human

**Verify ASIS APP/PSP domains, weightings, and eligibility** against the official ASIS
Certification Handbook (asisonline.org returns 403 to automated fetch, so an agent cannot do
this). Until then, `22_APP/` and `23_PSP/` must not be built — the provisional figures in
`31_References/source_index.md` are from exam-dump vendors and are flagged low-confidence.

This is not urgent: the roadmap doesn't start the APP track until month 6.

Note: `35_Doors_and_Hardware/00_MODULE_OVERVIEW.md` carries a provisional APP/PSP mapping table
with the same `[VERIFY]` caveat. It will need correcting at the same time.
