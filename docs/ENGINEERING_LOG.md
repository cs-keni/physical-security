# ENGINEERING_LOG

Reverse-chronological record of changes to this repository.

---

## 2026-08-06 — Session 1: initial build

### Research performed
- **Bluebeam Revu 21 subscription features** — retrieved from official Bluebeam support
  documentation. **Key finding: Scripting commands are Max-only.** The user's plan is
  Complete. This changed the architecture of the `16_Automation/` Bluebeam track from an
  in-application scripting approach to offline processing of documented CSV/XML exports.
  Confirmed available on Complete: Sets, Batch Link, Batch Compare, Spaces, Smart Overlay,
  formula custom columns, Markups List data export, OCR, Quantity Link.
- **ASIS APP/PSP certification requirements** — `asisonline.org` returns HTTP 403 to
  automated retrieval. Secondary sources consulted were largely exam-dump vendors.
  **Decision: record the provisional figures with explicit low-confidence flags rather than
  present them as verified, and block the APP/PSP tracks on human verification against the
  official Certification Handbook.** Recorded in `31_References/source_index.md`.

### Structure
- Created 39 module directories plus `docs/`.
- Deviated from the user's proposed structure by adding `32_Engineering_Math`,
  `33_Design_Review_QA`, `34_Electrical_Power`, `35_Doors_and_Hardware`,
  `36_Human_Factors_Privacy_Ethics`, `37_Project_Management`, `38_Products_and_Ratings`.
  Rationale documented in `00_Roadmap/curriculum_gap_analysis.md`.

### Content authored
- `README.md`, `PHASES.md`, `COURSE_PROGRESS.md`
- `00_Roadmap/` — `how_to_use_this_academy.md`, `study_roadmap.md` (12 months, 8 checkpoints),
  `skills_matrix.md` (8 competency areas × 4 levels), `progress_tracker.md`,
  `curriculum_gap_analysis.md` (22 added topics, structural changes, and an honest statement
  of where this curriculum's authority ends)
- `01_Foundations/` — module overview + 7 lessons: what PSE is; risk vocabulary; the
  functional chain with the timely-detection calculation; defense in depth and zones; CPTED;
  requirements engineering; systems and failure thinking. ~28,000 words.
- `25_Quizzes/quiz_01_foundations.md` (30 questions) + isolated answer key with full
  explanations
- `26_Flashcards/01_foundations.csv` — 58 cards
- `27_Labs/project_01_secure_one_door/BRIEF.md` + senior reference solution
- `30_Capstones/data_center_campus/00_BRIEF.md` — fictional site, 25 deliverables,
  12 deliberate ambiguities
- `31_References/source_index.md` — tag system, per-area confidence disclosure, ASIS caveat,
  verified Bluebeam matrix
- `docs/AI_CONTEXT.md`, `docs/HANDOFF.md`, `docs/CURRENT_TASK.md`

### Code authored
- **`28_Calculators/psec/`** — stdlib-only package:
  - `optics.py` — angle of view, FOV width, lens selection (the inverse problem), slant range,
    depression angle, PPF/PPM, DORI classification, max range for a target class, `CameraSpec`
    with coverage reports
  - `video.py` — bitrate scaling (sub-linear in frame rate, documented as a modelling choice),
    GB/day, storage for retention, camera groups, peak vs. average bandwidth, honest storage
    *ranges*, RAID raw capacity, inverse retention
  - `power.py` — PoE class budgets and switch checks, voltage drop (K at 75 °C), max run
    length, conductor selection, battery Ah with derate and aging factors, supply sizing
  - `pps.py` — adversary path timelines, timely detection, required detection point,
    intervention comparison across four levers
  - `tests/test_psec.py` — **66 tests, all passing**, expected values hand-computed
  - `demo.py` — 8 worked examples with engineering interpretation
  - `README.md` — documents embedded judgments and explicit non-goals
- **`16_Automation/data_model/`**:
  - `schema.py` — `SecurityDevice` (44 fields), `DeviceRegister`, device-type catalogue,
    phase-based field requirements, 6 projections (camera schedule, door schedule, IP plan,
    cable schedule, counts by type and by drawing)
  - `validate.py` — 11 rules producing severity-tagged findings; reports, never mutates
  - `sample_data/devices_flawed.csv` — 23 synthetic devices with deliberate realistic errors
  - `README.md`

### Defects found and fixed during the session
1. **`compare_interventions` emitted a negative detection target** when the response deficit
   exceeded the whole adversary path — arithmetically true, operationally meaningless. Now
   detects infeasibility and says so explicitly. Two tests added (66 total).
2. **`ID_PATTERN` required a numeric room designator**, which wrongly rejected every
   controller, switch, and power supply in head-end rooms (MDF, IDF-2). Relaxed to
   alphanumeric.
3. **Required-field validation flagged cable fields on rack-mounted head-end equipment** and
   network fields on non-IP devices, producing noise. Added type-aware exemptions — a
   validator that cries wolf gets ignored.
4. **Four rows of the sample CSV had a surplus field**, shifting columns and producing false
   findings. Normalised.
5. **`demo.py` interpretation text stated a max identification range inconsistent with its
   own computed output.** Corrected to match the calculation.

### Verification
```
python3 28_Calculators/tests/test_psec.py                → Ran 66 tests, OK
python3 28_Calculators/demo.py                            → clean
python3 16_Automation/data_model/validate.py <sample> CD  → 25 errors / 5 warnings / 4 info,
                                                            all genuine intentional defects
26_Flashcards/01_foundations.csv                          → 58 cards, 3 fields, 0 malformed
```

### Version control
Repository initialised, branch renamed `master` → `main`, remote added:
`git@github.com:cs-keni/physical-security.git`. Initial import committed and pushed.
`.gitignore` excludes `__pycache__/`, `*.pyc`, and `*_CONFIDENTIAL*` / `*_CLIENT*` patterns —
the latter as a guard against ever committing real project data.

**Commit:** see the follow-up entry below.

---

## 2026-08-06 — Session 1 commit record

| Commit | Scope |
|---|---|
| `667c2d1` | Initial import: structure, governance, Module 01, calculators, data model, Project 1, capstone brief |
| _(this commit)_ | Record commit hashes in the engineering log. A commit cannot contain its own hash; use `git log` for the exact value. |
