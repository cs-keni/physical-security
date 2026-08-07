# COURSE_PROGRESS

**Build status of the Physical Security Engineering Academy.**
This file is the source of truth for what has been *generated*. It is not a study tracker —
that is [`00_Roadmap/progress_tracker.md`](00_Roadmap/progress_tracker.md).

**Last updated:** 2026-08-06 (Session 1)

---

## For a coding agent resuming work

1. Read this file, then [`docs/HANDOFF.md`](docs/HANDOFF.md).
2. **Next work item is at the bottom of this file, under "Next logical work item."**
3. **Do not create placeholder files.** A file exists here only if it contains real
   instructional material. An unwritten module is an empty directory and a row in the table
   below — that is deliberate, so "does the file exist?" is a reliable completeness signal.
4. Follow the module template in [`docs/AI_CONTEXT.md`](docs/AI_CONTEXT.md).
5. Anything you assert about codes, ASIS, or product features must be tagged and logged in
   [`31_References/source_index.md`](31_References/source_index.md).
6. Run `python3 28_Calculators/tests/test_psec.py` before and after touching calculators.

---

## Legend

| Mark | Meaning |
|---|---|
| ✅ **Complete** | Full instructional content, exercises, and (where applicable) solutions |
| 🟡 **Partial** | Real content present, but named gaps remain |
| ⬜ **Not started** | Directory exists, no content |

---

## Governance and meta

| File | Status | Notes |
|---|---|---|
| `README.md` | ✅ | Repo map, ground rules, conventions |
| `COURSE_PROGRESS.md` | ✅ | This file |
| `PHASES.md` | ✅ | Build phases |
| `00_Roadmap/how_to_use_this_academy.md` | ✅ | Study method, cadence, software-background bridge |
| `00_Roadmap/study_roadmap.md` | ✅ | 12-month plan, 8 checkpoints |
| `00_Roadmap/skills_matrix.md` | ✅ | 8 competency areas, B→W→I→A |
| `00_Roadmap/progress_tracker.md` | ✅ | Study checkbox tracker |
| `00_Roadmap/curriculum_gap_analysis.md` | ✅ | 22 added topics, structural changes, honest limits |
| `31_References/source_index.md` | ✅ | Tag system, confidence disclosure, ASIS caveat, Bluebeam verification |
| `docs/AI_CONTEXT.md` | ✅ | Module template, authoring standards |
| `docs/HANDOFF.md` | ✅ | Architecture and conventions |
| `docs/CURRENT_TASK.md` | ✅ | Active work item |
| `docs/ENGINEERING_LOG.md` | ✅ | Change log |

---

## Modules

| # | Module | Status | What exists | What's missing |
|---|---|---|---|---|
| 01 | Foundations | ✅ | Overview + 7 full lessons (~28k words): what PSE is, risk vocabulary, D3ACR + timely detection, defense in depth/zones, CPTED, requirements engineering, systems & failure thinking. Exercises embedded in each lesson. | 4 `_solutions/` files for the embedded exercises; `vocabulary.md`; `checklist_foundations.md` |
| 02 | Risk Assessment | ⬜ | — | 7 lessons: methodology, asset characterization, threat/DBT, VA & site surveys, risk methods, adversary path analysis, master planning |
| 03 | Video Surveillance | ⬜ | — | 11 lessons. **Highest priority.** Optics math is already implemented in `psec.optics` — the lessons must derive it |
| 04 | Access Control | ⬜ | — | 11 lessons. SOO writing is partially demonstrated in the Project 1 reference solution |
| 05 | Intrusion Detection | ⬜ | — | 6 lessons |
| 06 | Perimeter Security | ⬜ | — | 7 lessons incl. lighting (promoted to major topic per gap analysis) |
| 07 | Intercom & Communications | ⬜ | — | 3 lessons |
| 08 | Networking | ⬜ | — | 8 lessons |
| 09 | Cybersecurity | ⬜ | — | 8 lessons incl. the evidence-integrity / synthetic-media question |
| 10 | Codes & Standards | ⬜ | — | 8 lessons. **Tag discipline is critical here** |
| 11 | Division 28 | ⬜ | — | 6 lessons + spec-reading exercises |
| 12 | Bluebeam | ⬜ | — | 8 lessons. **Complete-plan only; no Scripting (Max-only)** |
| 13 | Revit | ⬜ | — | 6 lessons + labs |
| 14 | AutoCAD | ⬜ | — | 4 lessons |
| 15 | Excel | ⬜ | — | 5 lessons + the calculator/schedule templates |
| 16 | Automation | 🟡 | `README.md`; `data_model/schema.py` (44-field model, 6 projections); `data_model/validate.py` (11 rules); `sample_data/devices_flawed.csv` (23 devices, deliberate errors). **All working and verified.** | Bluebeam export tools; Revit/AutoCAD tools; BOM/cost; drawing↔spec checker |
| 17 | Construction Documents | ⬜ | — | 8 lessons |
| 18 | Commissioning | ⬜ | — | 5 lessons + forms. Test-plan format demonstrated in Project 1 solution |
| 19 | Operations | ⬜ | — | 5 lessons |
| 20 | Data Center | ⬜ | — | 8 lessons. Capstone brief exists and depends on this |
| 21 | Facility Case Studies | ⬜ | — | 11 facility types |
| 22 | APP | ⬜ | — | **Verify domains against the official ASIS handbook first** |
| 23 | PSP | ⬜ | — | Same caveat |
| 24 | CPP Roadmap | ⬜ | — | Roadmap only |
| 25 | Quizzes | 🟡 | `quiz_01_foundations.md` (30 Q) + full answer key with explanations | Quizzes 02–20; cumulative reviews |
| 26 | Flashcards | 🟡 | `01_foundations.csv` — 58 cards, CSV-validated, Anki-ready | Decks for all other modules |
| 27 | Labs | 🟡 | Project 1 brief + full senior reference solution | Projects 2–7 |
| 28 | Calculators | ✅ | `psec` package: `optics`, `video`, `power`, `pps`. `demo.py` with 8 worked examples. **66 tests, all passing.** `README.md` documenting assumptions and non-goals | Rack/port planner; cost model |
| 29 | Templates | ⬜ | — | Schedules, trackers, BoD, SOO templates |
| 30 | Capstones | 🟡 | `data_center_campus/00_BRIEF.md` — full fictional site, 25 deliverables, 12 deliberate ambiguities | `_reference_solution/`; site plan geometry |
| 31 | References | ✅ | `source_index.md` | Grows continuously |
| 32 | Engineering Math | ⬜ | — | 8 lessons. **Must derive what `28_Calculators/` implements** — the tests are the derivation record |
| 33 | Design Review QA | ⬜ | — | Flawed packages. `16_Automation/sample_data/devices_flawed.csv` is a working prototype of the pattern |
| 34 | Electrical Power | ⬜ | — | 6 lessons |
| 35 | Doors & Hardware | ⬜ | — | 7 lessons. **High priority** — needed for month 1 and referenced by Project 1 |
| 36 | Human Factors, Privacy, Ethics | ⬜ | — | Per gap analysis |
| 37 | Project Management | ⬜ | — | Incl. cost estimating and delivery methods (added in gap analysis) |
| 38 | Products & Ratings | ⬜ | — | Incl. environmental conditions (added in gap analysis) |

---

## Verified working artifacts

| Artifact | Verification |
|---|---|
| `28_Calculators/psec/*` | `python3 28_Calculators/tests/test_psec.py` → **66 tests, OK** |
| `28_Calculators/demo.py` | Runs; 8 worked examples with interpretation |
| `16_Automation/data_model/validate.py` | Runs against the flawed sample; 25 errors / 5 warnings / 4 info, all genuine |
| `16_Automation/data_model/schema.py` | 6 projections verified (door schedule, camera schedule, IP plan, cable schedule, counts ×2) |
| `26_Flashcards/01_foundations.csv` | CSV-parsed: 58 cards, 3 fields, 0 malformed |

---

## Certification coverage

| Track | Status |
|---|---|
| APP | ⬜ Not started. **Blocked on verifying domains against the official ASIS Certification Handbook** (asisonline.org returns 403 to automated fetch). Provisional domain names recorded in `31_References/source_index.md` with confidence flags. |
| PSP | ⬜ Same. Domain *names* are moderately confident; **weightings are not asserted**. |
| CPP | ⬜ Roadmap only, by design. |
| **Indirect coverage** | Module 01 maps to APP D1/D3 and PSP D1/D2 — mapping table is in `01_Foundations/00_MODULE_OVERVIEW.md`. |

---

## Known issues and debts

1. **ASIS certification data is unverified.** Highest-priority correction. Requires a human to
   download the handbook.
2. **Module 01 exercise solutions are not written.** The lessons reference
   `01_Foundations/_solutions/*.md` (4 files). Retrieval checks and the quiz are covered; the
   embedded E-numbered exercises are not.
3. **`32_Engineering_Math/` lags `28_Calculators/`.** The code exists and is tested; the
   derivations that justify it are not yet written. The lessons should be written *from* the
   test file, since the tests encode the hand calculations.
4. **No site plan geometry for the capstone.** The brief describes the site in prose;
   dimensioned base geometry (even ASCII or SVG) would materially improve the exercise.
5. **`35_Doors_and_Hardware/` is referenced by Project 1 and the roadmap month 1 but not
   written.** This is the most disruptive current gap for a learner following the roadmap.

---

## Next logical work item

**In priority order** — each is sized to be completable and useful on its own:

1. **`35_Doors_and_Hardware/` lessons 01–07.** Unblocks roadmap month 1 and Project 1.
   The Project 1 reference solution already models the depth and vocabulary expected.
2. **`32_Engineering_Math/` lessons 01–07.** Derive what `28_Calculators/` implements. Write
   from `tests/test_psec.py` — every test's expected value is a hand calculation waiting to be
   shown. Include problem sets with separated answer keys.
3. **`01_Foundations/_solutions/`** — the 4 missing exercise solution files, plus
   `vocabulary.md` and `checklist_foundations.md`.
4. **`03_Video_Surveillance/` lessons 01–11.** The largest technical module; roadmap months
   3–4 depend on it.
5. **`04_Access_Control/` lessons 01–11.**
6. **`02_Risk_Assessment/` lessons 01–07.**
7. **Projects 2 and 3** (`27_Labs/`), following the Project 1 brief/solution pattern exactly.

**Authoring reminder:** before marking any module complete here, open it and confirm it
contains actual instructional material — worked examples, real numbers, exercises with
solutions — not headings.
