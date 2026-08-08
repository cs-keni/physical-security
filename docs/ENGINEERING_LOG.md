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
| `9aceadf` | Record commit hashes in the engineering log. A commit cannot contain its own hash; use `git log` for the exact value. |

---

## 2026-08-07 — Add repo-root CLAUDE.md

Session 2 opened with `/context-restore`. The saved checkpoint, `docs/HANDOFF.md`, and
`docs/CURRENT_TASK.md` all agree: foundation complete at `9aceadf`, working tree clean, next
work item is `35_Doors_and_Hardware/` lessons 01–07.

### Change
Added `CLAUDE.md` at the repo root. It did not exist — agent context lived only in `docs/`,
which meant an agent had to be told where to look before it knew where to look. The file
carries the read-first order, the conventions that must not drift, the verification commands,
and a gstack skill-routing section.

No content or code changed. Test suite untouched and still the authority on the calculators.

**Commit:** `6eddde9`

---

## 2026-08-07 — Session 2: Module 35 Doors and Hardware, lessons 01–05

Branch `module/35-doors-hardware`. Scope was deliberately set to lessons 01–05 at full depth
rather than all eight lessons thinned — detail prioritized over coverage, at Kenny's direction.

### What shipped

| File | Words | Content |
|---|---|---|
| `00_MODULE_OVERVIEW.md` | 923 | Objectives, study guidance, five load-bearing ideas, cross-references, provisional cert mapping |
| `01_door_anatomy.md` | 3,797 | The opening as the unit of design; frame, leaf, hinges, latching, closers, coordinators; reading a door schedule and hardware set |
| `02_handing_and_swing.md` | 2,935 | Four hands, the field procedure, handing vs. swing vs. secure side, device placement by side |
| `03_locking_hardware_families.md` | 4,346 | Five electrified families, selection framework, door position vs. latch position, worked power calculations |
| `04_fail_safe_vs_fail_secure.md` | 3,180 | Precise definitions, the five failure modes, hardwired FA release, decision tree |
| `05_egress.md` | 3,920 | Free egress, means of egress, five special locking arrangements, the "lock the exit" conversation |
| `_solutions/*.md` (5 files) | 10,444 | Worked senior-level answers for every E-numbered exercise |

**29,545 words total.** Comparable to Module 01's ~28k across 7 lessons, so the depth bar held.

### Decisions made

- **`_solutions/` written in the same commit as the lessons.** Module 01 shipped lessons whose
  exercise links dangle and that debt is still open (known issue #5). Repeating it would have
  been a smell. Recorded in `HANDOFF.md` as a convention for all future modules.
- **Key management placed in module 35 as lesson 08** rather than standing alone. A junior meets
  keying at the same door they meet the strike. Kenny's call.
- **Numeric examples computed with `psec.power`, not written by hand.** Lesson 03's power supply
  sizing, battery sizing, and voltage-drop tables — and E3.2's solution — were produced by
  running the calculator and transcribing the output. The numbers are reproducible, and a
  formula change will surface as a mismatch rather than silently stale prose. This is the
  inverse of the `32_Engineering_Math/` plan (derive *from* the tests) and the same principle.
- **Lesson 05 written as a map of a body of code, not a set of facts.** Every numeric and
  prescriptive claim carries `[CODE][VERIFY]`, the lesson opens with a standing warning, and the
  15/30-second delayed egress figures are presented as "commonly cited, confirm against the
  adopted text" rather than asserted. Hard rule 1 in `AI_CONTEXT.md` is doing real work here:
  the honest failure mode for this lesson is a learner quoting a number to a client.
- **Defensive depth only.** Attack classes are named (latch slipping, hinge pin removal, ceiling
  bypass) and immediately answered with the countermeasure (deadlatch, NRP hinges, deck-to-deck
  partition). No procedures.
- **No placeholder files for 06–08.** Empty positions in the module, rows in `COURSE_PROGRESS.md`,
  and explicit "not yet written" notes at the two places lessons forward-reference them.

### Teaching content worth flagging as load-bearing

Two corrections that change how a junior designs, both of which the lessons make explicit:

1. **Fail secure does not trap anyone.** Egress at an electrified lockset or exit device is a
   mechanical linkage. Juniors who believe otherwise specify fail safe everywhere and build a
   building that unlocks itself on power loss. Lesson 04 leads with this.
2. **Free egress is one-directional.** You may always secure the outside. Lesson 05 uses this to
   resolve most "lock the exit" client requests, which is the practical payoff of the whole
   lesson.

### Verification

```
python3 28_Calculators/tests/test_psec.py                → Ran 66 tests, OK
python3 28_Calculators/demo.py                           → clean
python3 16_Automation/data_model/validate.py <sample> CD → 25 errors / 5 warnings / 4 info
                                                           (unchanged baseline)
26_Flashcards/01_foundations.csv                         → 58 cards
```

No code changed this session, so the suite is a regression check rather than a validation of new
work. The `psec.power` outputs quoted in lesson 03 were captured from live runs of
`power_supply_sizing`, `battery_ah_required`, `voltage_drop_v`, `voltage_at_load_v`, and
`smallest_awg_for_run`.

### Docs updated

`COURSE_PROGRESS.md` (module 35 row → 🟡, known issues 5–7 rewritten, next work item),
`PHASES.md` (Phase 5 → 🟡, 01–05 checked, 08 added as an explicit item),
`docs/CURRENT_TASK.md`, `docs/HANDOFF.md` (state, two new architectural decisions, debts
renumbered, next work item).

### Follow-ups created

- Lessons 06–08 are the next binding constraint: lesson 03 forward-references power transfer to
  06 three times and lesson 05's "Next" link points at 06.
- Module 35 has no quiz and no flashcards. Module 01 has both.
- `00_MODULE_OVERVIEW.md` carries a provisional APP/PSP mapping that must be corrected when the
  ASIS handbook block is cleared.

### Commit record

| Commit | Scope |
|---|---|
| `6eddde9` | Add repo-root CLAUDE.md with conventions and skill routing |
| `2c39e88` | Module 35 lessons 01–05 + `_solutions/` + doc updates |
| `ff3170b` | Merge `module/35-doors-hardware` to `main` |

As in Session 1, the content commit cannot contain its own hash; it is recorded here in the
follow-up commit.

---

## 2026-08-07 — Session 3: Module 35 lessons 06–08 and assessment material

Branch `module/35-doors-hardware-part2`. Closes Phase 5. **Module 35 is the first complete
module in the repo.**

### What shipped

| File | Words | Content |
|---|---|---|
| `06_electrified_hardware_power_transfer.md` | 3,213 | Four transfer methods, conductor budgeting, voltage drop *through* the transfer, flex fatigue, factory prep |
| `07_fire_rated_openings.md` | 3,358 | The assembly concept, labels and what voids them, the four behaviors, what security scope gets wrong, the NFPA 80 obligation |
| `08_key_management.md` | 3,890 | Key hierarchy and its costs, rekey triggers, the three controls, construction keying, the no-override decision, attack classes and rated countermeasures |
| `_solutions/06–08` | 8,300 | Worked answers for every E-numbered exercise |
| `_exercises/10_door_survey.md` | 1,766 | Module capstone: 10-opening survey with a full recording template and a self-assessment rubric |
| `_solutions/10_door_survey_reference.md` | 2,824 | Reference findings set against a fictional building, with a worked findings memo |
| `25_Quizzes/quiz_35_doors_hardware.md` | 1,186 | 30 questions: 20 concept, 6 scenario, 4 calculation |
| `25_Quizzes/_answer_keys/quiz_35_answers.md` | 3,272 | Full explanations for all 30 |
| `26_Flashcards/35_doors_hardware.csv` | — | 77 cards, validated |

**Module 35 total across Sessions 2–3: ~58,000 words, 21 files.**

### Decisions made

- **Lesson 06's worked example deliberately continues lesson 03's.** Same opening, same 2.8 A ELR
  device, same 200 ft run — and the 12 AWG conductor that passed at 21.79 V in lesson 03 lands at
  **20.72 V** once six feet of 24 AWG transfer is added, back under the floor. Continuity teaches
  better than a fresh contrived example, and it makes the omission memorable rather than abstract.
  Recorded in `HANDOFF.md` as a convention.
- **E6.2 was built to produce an uncomfortable answer.** At 3.2 A running, 10 AWG barely passes;
  at the 8 A inrush, *no* home run gauge works and the only fixes are relocating the supply or
  changing the device. The exercise is designed so that iterating on conductor size fails, which
  is the actual engineering lesson — when the arithmetic gets ugly, question the device selection.
- **Lesson 07 is structured as a derivation, not a list.** Every rated-opening hardware
  restriction (no mag locks, no dogging, fail secure only, stair re-entry releases the trim) is
  derived from "a fire door must latch." E7.6 tests whether that compression happened. A learner
  who memorized four facts will list four facts; one who understood derives all four in one pass.
- **Lesson 08 leads with the framing that reduces our own scope** — key control is a policy
  project, not a procurement, and it bounds the value of the whole access control system.
  E8.4 makes the learner write that recommendation out. This is `AI_CONTEXT.md`'s "say the
  uncomfortable thing" applied where it costs something.
- **The 10-door survey is framed as a deliverable, not homework.** Junior engineers are handed
  door surveys in their first month; the exercise teaches the recording discipline (notably
  `UNKNOWN — [why]` over blanks) that makes a survey usable by someone who wasn't there.
- **The survey reference uses a fictional building**, labelled synthetic per `AI_CONTEXT.md` hard
  rule 4. Its three ranked findings are chosen so that the most common wrong answer — "add a card
  reader to the IDF closet" — is named explicitly as the failure to avoid.
- **Defensive depth held throughout lesson 08.** Attack classes are named and immediately paired
  with the rated countermeasure. No procedures, no technique. The table's real teaching point is
  that four of eight classes are answered by a rated cylinder and the biggest one is answered by
  a *policy*.

### Verification

```
python3 28_Calculators/tests/test_psec.py                → Ran 66 tests, OK
python3 28_Calculators/demo.py                           → clean
python3 16_Automation/data_model/validate.py <sample> CD → 25 errors / 5 warnings / 4 info
                                                           (unchanged baseline)
26_Flashcards/01_foundations.csv                         → 58 cards, 3 fields, 0 malformed
26_Flashcards/35_doors_hardware.csv                      → 77 cards, 3 fields, 0 malformed
Link check, 21 module-35 files                           → all relative targets resolve
```

No code changed this session. All numeric values in lesson 06, its solutions, and quiz questions
27–29 were captured from live runs of `psec.power` (`power_supply_sizing`,
`battery_ah_required`, `voltage_drop_v`, `voltage_at_load_v`).

A **link-check script** was added to `HANDOFF.md`'s verification block. Cross-module references
are easy to get wrong and nothing else in the repo catches them.

### Docs updated

`COURSE_PROGRESS.md` (module 35 → ✅, known issues collapsed from 7 to 6 and renumbered, next
work item, verified-artifacts rows, cert coverage), `PHASES.md` (Phase 5 → ✅ COMPLETE),
`docs/CURRENT_TASK.md`, `docs/HANDOFF.md` (state, three new architectural decisions, debts
renumbered, link-check procedure, next work item).

### Follow-ups

- **`32_Engineering_Math/` is now the most visible gap.** Module 35 leans on `psec.power` in
  three worked examples and forward-references module 32 for the derivations. Its voltage-drop
  lesson must cover **summing drops across segments of different gauge**, because lesson 06
  established that as the case that catches people.
- `01_Foundations/_solutions/` remains the oldest open debt — 4 files plus `vocabulary.md` and
  `checklist_foundations.md`. Small, and closing it makes "every lesson's solutions exist" true
  repo-wide.
- Two provisional APP/PSP mapping tables now need correcting when the ASIS block clears.

**Commit:** see `git log` — this entry ships in the same commit as the content it describes.
