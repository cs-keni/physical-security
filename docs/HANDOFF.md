# HANDOFF

**Last session:** 2026-08-06 (Session 1 — initial build)
**State:** Foundation complete and verified. Ready for Phase 5.

---

## Repository

- **Remote:** `git@github.com:cs-keni/physical-security.git`
- **Default branch:** `main`
- **Workflow:** feature branch per work item (e.g. `module/35-doors-hardware`), then merge to
  `main`. Never commit real project data — `.gitignore` guards `*_CONFIDENTIAL*` / `*_CLIENT*`
  but the real control is discipline.
- **Commit convention:** imperative subject ≤72 chars stating *what* and *why*. Update
  `COURSE_PROGRESS.md`, `PHASES.md`, and `docs/ENGINEERING_LOG.md` **in the same commit** as
  the content they describe.

---

## Architecture

```
physical-security/
├── README.md                  entry point, repo map, ground rules
├── COURSE_PROGRESS.md         ← BUILD STATUS. Read first when resuming.
├── PHASES.md                  build plan
├── docs/                      agent context (this dir)
├── 00_Roadmap/                how to study, 12-month plan, skills matrix, gap analysis
├── 01–38_<Module>/            instructional content; solutions in _solutions/
├── 25_Quizzes/_answer_keys/   isolated
├── 27_Labs/_solutions/        isolated
├── 28_Calculators/psec/       ← WORKING CODE. 66 tests.
├── 16_Automation/data_model/  ← WORKING CODE. Device schema + validator.
└── 31_References/             source_index.md — the verification record
```

**Two kinds of artifact, different rules:**
- **Content** (Markdown) — follows the 20-part module template in `AI_CONTEXT.md`
- **Code** (Python) — standard library only, tested, documented assumptions

---

## Key architectural decisions

| Decision | Rationale |
|---|---|
| **Solutions isolated in `_solutions/` / `_answer_keys/`** | The learner explicitly asked not to be able to spoil exercises by scrolling. Never inline an answer. |
| **No placeholder files** | "Does the file exist?" must be a reliable completeness signal. Unwritten = empty dir + a `COURSE_PROGRESS.md` row. |
| **Calculators are stdlib-only** | Must run on a locked-down work laptop with no software request. |
| **Tests encode the hand calculations** | `32_Engineering_Math/` lessons will be written *from* the test file. If a test fails after a formula change, redo the hand calc — don't change the test. |
| **Device data model is the single source of truth** | Drawings, schedules, IP plan, cable schedule, commissioning tracker are all projections. This is the learner's differentiator. |
| **Validator reports, never mutates** | "Automate the repetitive work, never the engineering judgment." A tool that silently fixes data will silently break it. |
| **Phase-aware validation** | A validator that cries wolf gets ignored, which is worse than none. |
| **Bluebeam automation via exports, not scripting** | Scripting is Max-only; the user has Complete. Verified against official docs. |
| **Doors/hardware and electrical split into their own modules (35, 34)** | They're the top two junior knowledge gaps and deserve dedicated depth. |
| **Engineering math (32) separate from calculators (28)** | Derivations are pedagogically distinct from tools; separation prevents using a calculator you don't understand. |

---

## Content conventions that must not drift

- Tag system: `[CODE]` `[STANDARD]` `[GUIDELINE]` `[PRACTICE]` `[MFR]` `[VERIFY]`
- Icons: 🧮 calculation · 🔧 lab · ⚠️ mistake · 🧠 senior insight
- Every module: Junior vs. Senior sections, Common Mistakes, Retrieval Check, References
- Every code/standard numeric claim: tagged `[VERIFY]`
- ASCII diagrams only (must render in a plain text editor)

---

## Outstanding risks and debts

1. **ASIS certification data unverified** — asisonline.org 403s automated fetch. Domain names
   and weightings in `31_References/source_index.md` are flagged low-confidence. **A human
   must download the official Certification Handbook.** Do not build the APP/PSP tracks on the
   provisional figures.
2. **`35_Doors_and_Hardware/` is referenced by roadmap month 1 and Project 1 but unwritten** —
   the most disruptive gap for a learner starting today.
3. **`32_Engineering_Math/` lags the calculators** — code is tested, derivations unwritten.
4. **Module 01 embedded exercises lack solution files** (4 files). Quiz and retrieval checks
   are covered; the E-numbered exercises are not.
5. **Capstone has no dimensioned site geometry** — prose description only.

---

## Verification commands

```bash
python3 28_Calculators/tests/test_psec.py     # 66 tests → OK
python3 28_Calculators/demo.py                 # 8 worked examples
python3 16_Automation/data_model/validate.py \
        16_Automation/sample_data/devices_flawed.csv CD   # 25 errors, all genuine
python3 -c "import csv; print(len(list(csv.DictReader(open('26_Flashcards/01_foundations.csv')))))"
```

---

## Next work item

See the bottom of [`../COURSE_PROGRESS.md`](../COURSE_PROGRESS.md).
Short version: **`35_Doors_and_Hardware/` lessons 01–07**, then `32_Engineering_Math/`.

Match the depth and voice of `01_Foundations/03_functional_chain.md` and
`27_Labs/_solutions/project_01_reference.md` — those are the quality bar.
