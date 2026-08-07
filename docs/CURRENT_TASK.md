# CURRENT_TASK

**Status:** Session 1 complete. No task in progress.

## Just completed (2026-08-06)

Initial build of the Physical Security Engineering Academy:
- Research: Bluebeam Revu 21 Complete feature set verified; ASIS certification data
  **blocked at source and documented as unverified rather than guessed**
- 39-directory structure, governance docs, 12-month roadmap, skills matrix, gap analysis
  (22 topics added to the requested curriculum)
- **Module 01 Foundations** — 7 full lessons, ~28,000 words
- **Working calculators** — `psec` package, 66 passing tests, demo with 8 worked examples
- **Security Device Data Model** — 44-field schema, 6 projections, 11 validation rules,
  synthetic flawed dataset
- Quiz 01 + answer key, 58-card flashcard deck
- Project 1 brief + senior reference solution
- Data center capstone brief

## Next task

**`35_Doors_and_Hardware/` lessons 01–07.**

Why this next: roadmap month 1 week 3 depends on it, and Project 1 (the learner's first lab)
references it directly. It is currently the most disruptive gap.

Scope:
1. Door anatomy and terminology
2. Handing, swing, secure side
3. Locking hardware families (strikes, mags, electrified locksets, electrified exit devices)
4. Fail safe vs fail secure — the decision framework
5. Egress, delayed egress, controlled egress `[CODE][VERIFY throughout]`
6. Electrified hardware and power transfer
7. Fire-rated openings
Plus: key management and mechanical security (gap-analysis addition), the 10-door field
exercise, quiz, and flashcards.

**Quality bar:** match `01_Foundations/03_functional_chain.md` and
`27_Labs/_solutions/project_01_reference.md`.

**Before starting:** read `docs/AI_CONTEXT.md` and `docs/HANDOFF.md`.
Branch: `module/35-doors-hardware` off `main`.

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
