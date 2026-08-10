# COURSE_PROGRESS

**Build status of the Physical Security Engineering Academy.**
This file is the source of truth for what has been *generated*. It is not a study tracker —
that is [`00_Roadmap/progress_tracker.md`](00_Roadmap/progress_tracker.md).

**Last updated:** 2026-08-09 (Session 6)

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
| 01 | Foundations | ✅ | Overview + 7 full lessons (~28k words): what PSE is, risk vocabulary, D3ACR + timely detection, defense in depth/zones, CPTED, requirements engineering, systems & failure thinking. Exercises embedded in each lesson, with `_solutions/` for all 6 sets. Plus `vocabulary.md` (full glossary + disambiguation drill), `checklist_foundations.md` (the reasoning checklist), and `exercises.md` — index plus the **Ashford Public Library capstone**, one site through all 7 lessons, with a reference solution. ~37k words added in Session 5. | — |
| 02 | Risk Assessment | ⬜ | — | 7 lessons: methodology, asset characterization, threat/DBT, VA & site surveys, risk methods, adversary path analysis, master planning |
| 03 | Video Surveillance | ✅ | Overview + 11 full lessons (~76k words) with `_solutions/` for every one: the imaging chain, optics/aperture/DOF, sensors & low light, DORI in practice, form factors, compression & bandwidth, storage & retention, VMS architecture, camera placement, the retail case study, analytics & health monitoring. Plus the **Cedar Junction park-and-ride capstone** with a full reference solution, Quiz 03 + isolated key, and 114 flashcards. **The largest module in the academy.** It deliberately does *not* re-derive module 32's math — see the division-of-labour table in its overview | — |
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
| 25 | Quizzes | 🟡 | `quiz_01_foundations.md`, `quiz_35_doors_hardware.md`, `quiz_32_engineering_math.md`, `quiz_03_video_surveillance.md` (30 Q each) + full answer keys with explanations | Quizzes for the remaining modules; cumulative reviews |
| 26 | Flashcards | 🟡 | `01_foundations.csv` (58), `35_doors_hardware.csv` (77), `32_engineering_math.csv` (80), `03_video_surveillance.csv` (114) — 329 cards, CSV-validated, Anki-ready | Decks for all other modules |
| 27 | Labs | 🟡 | Project 1 brief + full senior reference solution | Projects 2–7 |
| 28 | Calculators | ✅ | `psec` package: `optics`, `video`, `power`, `pps`. `demo.py` with 8 worked examples. **68 tests, all passing.** `README.md` documenting assumptions and non-goals | Rack/port planner; cost model |
| 29 | Templates | ⬜ | — | Schedules, trackers, BoD, SOO templates |
| 30 | Capstones | 🟡 | `data_center_campus/00_BRIEF.md` — full fictional site, 25 deliverables, 12 deliberate ambiguities | `_reference_solution/`; site plan geometry |
| 31 | References | ✅ | `source_index.md` | Grows continuously |
| 32 | Engineering Math | ✅ | Overview + 8 full lessons (~42.6k words) with `_solutions/` for every one: camera FOV, pixel density & DORI, bandwidth, storage & retention, PoE & switch capacity, voltage drop, battery & supply sizing, adversary path & timely detection. Plus the integrated sizing capstone (one site, all 8 lessons) with a full reference solution, Quiz 32 + isolated key, and 80 flashcards. **This module is the derivation record for `28_Calculators/`** — every value transcribed from a `psec` run. Writing it found **2 real defects in `psec`** (see known issues 7) | — |
| 33 | Design Review QA | ⬜ | — | Flawed packages. `16_Automation/sample_data/devices_flawed.csv` is a working prototype of the pattern |
| 34 | Electrical Power | ⬜ | — | 6 lessons |
| 35 | Doors & Hardware | ✅ | Overview + 8 full lessons (~28k words) with `_solutions/` for every one: door anatomy, handing & secure side, locking hardware families, fail safe vs fail secure, egress, power transfer, fire-rated openings, key management. Plus the 10-door survey capstone with a reference findings set, Quiz 35 + isolated key, and 77 flashcards. All power calculations computed with `psec.power`. **Roadmap months 1, 4, and 8 unblocked; Project 1 has its prerequisite.** | — |
| 36 | Human Factors, Privacy, Ethics | ⬜ | — | Per gap analysis |
| 37 | Project Management | ⬜ | — | Incl. cost estimating and delivery methods (added in gap analysis) |
| 38 | Products & Ratings | ⬜ | — | Incl. environmental conditions (added in gap analysis) |

---

## Verified working artifacts

| Artifact | Verification |
|---|---|
| `28_Calculators/psec/*` | `python3 28_Calculators/tests/test_psec.py` → **68 tests, OK** |
| `28_Calculators/demo.py` | Runs; 8 worked examples with interpretation |
| `16_Automation/data_model/validate.py` | Runs against the flawed sample; 25 errors / 5 warnings / 4 info, all genuine |
| `16_Automation/data_model/schema.py` | 6 projections verified (door schedule, camera schedule, IP plan, cable schedule, counts ×2) |
| `26_Flashcards/01_foundations.csv` | CSV-parsed: 58 cards, 3 fields, 0 malformed |
| `26_Flashcards/35_doors_hardware.csv` | CSV-parsed: 77 cards, 3 fields, 0 malformed |
| `26_Flashcards/32_engineering_math.csv` | CSV-parsed: 80 cards, 3 fields, 0 malformed |
| `26_Flashcards/03_video_surveillance.csv` | CSV-parsed: **114 cards**, 3 fields, 0 malformed |
| `03_Video_Surveillance/` internal links | 25 files link-checked; all relative targets resolve |
| `03_Video_Surveillance/` worked values | Every number reproduced by running `psec.optics`, `psec.video`, and `psec.pps`; DOF and exposure-budget arithmetic shown in full in-lesson (not in `psec` — see known issue 8) |
| `35_Doors_and_Hardware/` internal links | 21 files link-checked; all relative targets resolve |
| `32_Engineering_Math/` internal links | 19 files link-checked; all relative targets resolve |
| `32_Engineering_Math/` worked values | Every number reproduced by running `psec` directly; capstone model in the reference solution |
| `01_Foundations/` internal links | 13 files link-checked; all relative targets resolve |
| `01_Foundations/` capstone values | Adversary-path arithmetic reproduced with `psec.pps` (6 variants) |

---

## Certification coverage

| Track | Status |
|---|---|
| APP | ⬜ Not started. **Blocked on verifying domains against the official ASIS Certification Handbook** (asisonline.org returns 403 to automated fetch). Provisional domain names recorded in `31_References/source_index.md` with confidence flags. |
| PSP | ⬜ Same. Domain *names* are moderately confident; **weightings are not asserted**. |
| CPP | ⬜ Roadmap only, by design. |
| **Indirect coverage** | Module 01 maps to APP D1/D3 and PSP D1/D2 (`01_Foundations/00_MODULE_OVERVIEW.md`). Module 35 maps to APP D1/D2/D4 and PSP D2/D3 (`35_Doors_and_Hardware/00_MODULE_OVERVIEW.md`). Module 32 maps to APP D1/D4 and PSP D1/D2/D3 (`32_Engineering_Math/00_MODULE_OVERVIEW.md`). **Both mapping tables are provisional and must be corrected when the ASIS block clears.** |

---

## Known issues and debts

1. **ASIS certification data is unverified.** Highest-priority correction. Requires a human to
   download the handbook.
2. ~~**Module 01 exercise solutions are not written.**~~ **Resolved (Session 5).** All 6
   solution files written, plus `vocabulary.md`, `checklist_foundations.md`, and `exercises.md`
   with a module capstone. **The repo now has zero dangling solution links.** Note the original
   count of 4 was wrong — lessons 02–07 each carry an exercise set, so there were 6.
3. ~~**`32_Engineering_Math/` lags `28_Calculators/`.**~~ **Resolved (Session 4).** Module 32 is
   complete: 8 lessons, all solutions, the integrated sizing capstone, quiz, and flashcards.
   `28_Calculators/` now has a full derivation record.
4. **No site plan geometry for the capstone.** The brief describes the site in prose;
   dimensioned base geometry (even ASCII or SVG) would materially improve the exercise.
5. ~~**`35_Doors_and_Hardware/` is referenced by Project 1 and the roadmap month 1 but not
   written.**~~ **Resolved (Sessions 2–3).** Module 35 is complete: 8 lessons, all solutions,
   capstone survey, quiz, and flashcards. Roadmap months 1, 4, and 8 are unblocked.
6. ~~**Modules 32 and 35 are the only modules with no solution debt.**~~ **Resolved (Session 5).**
   Modules 01, 32, and 35 are all clean. The stale
   `01_Foundations/03_functional_chain.md` → `28_Calculators/timely_detection.py` link was also
   fixed; it now points at `psec/pps.py` and the module 32 derivation. **The only remaining
   broken link repo-wide is `30_Capstones/data_center_campus/` → `_reference_solution/`**, which
   is issue 4. The convention — write solutions in the same commit as the lessons that link to
   them — now holds for every written module and must hold for every module from here.
8. **`psec` has no depth-of-field or motion-blur functions, and Module 03 needs both.** Writing
   module 03 required DOF (hyperfocal, near/far limits) in lesson 02 and motion blur
   (`smear_px = speed × exposure × PPF`) in lessons 01 and 03. Both are geometric, both are
   testable against hand calculations, and both belong in `psec.optics`. **They were deliberately
   not added**, because this repo's architecture is that `32_Engineering_Math/` derives what
   `28_Calculators/` implements — so adding them properly means writing the derivations in module
   32 first, which would reopen a module marked complete. Until then the arithmetic is shown in
   full in the module 03 lessons so it can be checked by hand. Logged as a follow-on work item.

7. **Two defects in `psec` were found by hand-checking units while writing Module 32, and both
   are fixed.** (a) `video.stream_gb_per_day(decimal_gb=False)` divided decimal megabytes by
   1024 instead of 2³⁰/10⁶, halving the reported decimal/binary gap — the exact error its own
   docstring warned about, missed because the only test on that path asserted `binary < decimal`,
   true either way. (b) `pps.compare_interventions` documented three levers and returns four.
   **Test count 66 → 68.** The lesson generalises: a passing test suite is not evidence that the
   units are right, and the cheapest defect detector available is dimensional analysis done by
   hand.

---

## Next logical work item

**In priority order** — each is sized to be completable and useful on its own:

1. **`04_Access_Control/` lessons 01–11.** Now the highest priority. Module 35 lessons 03, 04, and
   06 hand off to this one directly — offline controller behavior, REX strategy, and
   reader-in/reader-out are all raised there and resolved here. Module 03 lesson 08 also
   forward-references it for PACS/video integration.
2. **`02_Risk_Assessment/` lessons 01–07.** Module 32 lesson 08 derives the path
   arithmetic; this module supplies the method for finding the paths worth analysing. Module 03's
   capstone leans on it too — the timeliness analysis there is the technique this module teaches
   generally.
3. **Projects 2 and 4** (`27_Labs/`) — small office camera design and retail surveillance design.
   **Both are now fully unblocked** by module 03 and follow the Project 1 brief/solution pattern.
   Project 3 (access control) follows module 04.
4. **`psec.optics` additions: depth of field and motion blur.** Module 03 needed both routinely and
   neither exists. See known issue 8 — the derivations belong in module 32 first.
5. **`30_Capstones/data_center_campus/_reference_solution/`** — the last dangling link in the
   repo, and the only remaining solution debt.

**Authoring reminder:** before marking any module complete here, open it and confirm it
contains actual instructional material — worked examples, real numbers, exercises with
solutions — not headings.

**Modules 01, 03, 32, and 35 are the current quality bar for a complete module:** overview, lessons,
solutions for every lesson, a capstone exercise with a reference solution, a quiz with an
isolated key, and a validated flashcard deck. Match that shape.

**Module 03 adds one convention worth keeping:** where a module *applies* math another module
derives, it says so explicitly in a **division-of-labour table** in its overview, links to the
derivation for every formula, and does not restate it. This is what kept a 76k-word module from
duplicating module 32, and it is the pattern for module 04 against module 35.

**Module 32 adds one convention worth keeping:** where a module has code behind it, every
numeric value in the prose is produced by *running* that code and transcribing the result — never
hand-written. It keeps the lessons and the tests from drifting, and it is what surfaced the two
`psec` defects in known issue 7.
