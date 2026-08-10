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

### Commit record

| Commit | Scope |
|---|---|
| `fe34d21` | Record Session 2 commit hashes in engineering log |
| `e3c2aca` | Module 35 lessons 06–08, capstone survey, quiz + key, flashcards, doc updates |
| `f422074` | Merge `module/35-doors-hardware-part2` to `main` |

---

## 2026-08-08 — Session 4: Module 32 Engineering Math (complete)

Branch `module/32-engineering-math` off `main` at `b609dda`. ~55k words across 19 files. Second
complete module in the repo, and the first written as a **derivation record for working code**.

### Code changed — two real defects in `psec`, both found by hand

This is the headline of the session. `28_Calculators/` had a green suite of 66 tests. Working the
units by hand to write lesson 04 found a defect the suite could not see.

**1. `video.stream_gb_per_day(decimal_gb=False)` divided decimal megabytes by 1024.**

A bitrate is decimal — 5.0 Mbps is 5 × 10⁶ bits per second — so the intermediate megabytes are
10⁶ bytes. Converting those to gibibytes requires dividing by **2³⁰/10⁶ = 1073.741824**, not by
1024. The consequence: the function reported the decimal/binary gap at TB scale as **4.86%** when
the true figure is **9.95%** — the *exact* "classic ~10% error at the TB scale" its own docstring
warned about. **The code contradicted its own comment.**

Why no test caught it: the only test on that path asserted `binary < decimal`, which is true
whichever divisor you use. An assertion of the form `a < b` passes for the wrong reason far more
often than it fails for the right one.

Fixed in `28_Calculators/psec/video.py` with named constants (`MB_TO_GB_DECIMAL`,
`MB_TO_GIB_BINARY`, `GB_TO_TB_DECIMAL`, `GIB_TO_TIB_BINARY`) so the two conversion systems cannot
be silently mixed again, plus two tests:

- `test_binary_units_are_true_gibibytes`
- `test_decimal_binary_gap_at_tb_scale_is_about_ten_percent` — asserts the ratio against
  `2**40/1e12`, **a value derived from the definition rather than captured from a run**. A test
  that records what the code did cannot detect that the code was wrong.

**2. `pps.compare_interventions` docstring said "three levers" and returns four.** Fixed, and the
module-32 cross-reference added.

**Test count 66 → 68.** Every doc quoting 66 was updated except the historical session entries in
this log, which record what was true at the time and should not be rewritten.

### Content written

- **`32_Engineering_Math/00_MODULE_OVERVIEW.md`** — lesson table with what each derives, how to
  study, eight load-bearing ideas, cross-references, provisional APP/PSP mapping with the
  `[VERIFY]` caveat, and a section documenting the `video.py` defect as the module's own argument
  for existing.
- **Lessons 01–08 with `_solutions/` for every one**, written in the same commit:
  camera FOV and focal length, pixel density and DORI, bandwidth, storage and retention, PoE
  budgets and switch capacity, voltage drop and conductor selection, battery and supply sizing,
  adversary path and timely detection.
- **`_exercises/integrated_sizing.md`** + `_solutions/integrated_sizing_reference.md` — the
  capstone. One fictional 3PL distribution centre sized end to end through all eight lessons.
- **`25_Quizzes/quiz_32_engineering_math.md`** + isolated answer key — 30 questions, 52 points,
  16 concept / 6 scenario / 8 calculation.
- **`26_Flashcards/32_engineering_math.csv`** — 80 cards, validated.

### Design decisions worth recording

- **Deviated from PHASES.md's lesson list, deliberately.** Planned item 08 was "Rack, port, and
  capacity planning"; it was folded into `05_poe.md` because port count, oversubscription, and
  spare-port policy **are** the `PoESwitch` checks, and separating them from the power budget
  would have split two constraints whose entire lesson is that they bind independently. Lesson 08
  became the adversary path derivation, because `psec/pps.py` had substantial tested math with no
  derivation anywhere in the repo — leaving it underived would have left the module incomplete
  against its own stated purpose. Rationale recorded in `PHASES.md` Phase 6.
- **Every numeric value was produced by running `psec` and transcribing it.** Module 35 established
  this; module 32 makes it a hard rule, since a hand-written number in a lesson about code is a
  future drift bug. It is also what surfaced both defects above.
- **Problem sets are built around traps, deliberately.** Lesson 02 P2.6 has a row where the
  arithmetic passes and a 48° depression angle has thrown the face away. Lesson 06 P6.4 **reverses
  module 35's conclusion** — there the transfer dominated, here the home run does — so "always
  check the transfer" is shown to be a habit rather than a rule. Lesson 08 P8.2 asks for a
  detection point that comes out negative.
- **Lesson 06 carries module 35's multi-segment case forward**, as `HANDOFF.md` required: summing
  `L/CM` across segments of different gauge, opening with the same worked example (200 ft 12 AWG +
  6 ft 24 AWG at 2.8 A → 20.72 V, fails).
- **The capstone fails four times before it works, by construction.** The gate camera misses
  identify by two DORI classes; the warehouse cameras miss observe by 10.5%; a single switch is
  over its PoE budget by 99.4 W *and* short on spare ports; and the cage conductor delivers
  10.068 V against a 10.2 V minimum. The adversary path is then not timely, and — the sharpest
  result in the module — **adding the obvious fence detection layer still fails**, because the
  60 s assessment delay consumes more than half the 135 s detection budget. The fix that works
  costs no hardware at all. The exercise tests noticing that an answer is unacceptable, not
  computing it.
- **The capstone reference includes a worked basis-of-design memo**, because the deliverable a
  junior engineer is actually judged on is the memo, not the spreadsheet.
- **A correction made mid-session:** lesson 07 originally stated that adding the derate factors
  instead of multiplying under-sizes a battery by ~6%. It is **4.167%** (1.5625 vs 1.5). Fixed in
  the body and in the common-mistakes list, and the capstone now asks the learner to compute it
  and then say honestly that at that site it changes nothing.

### Verification

```
python3 28_Calculators/tests/test_psec.py                → Ran 68 tests, OK
python3 28_Calculators/demo.py                           → clean
python3 16_Automation/data_model/validate.py <sample> CD → 25 errors / 5 warnings / 4 info
                                                           (unchanged baseline)
26_Flashcards/01_foundations.csv                         → 58 cards, 3 fields, 0 malformed
26_Flashcards/35_doors_hardware.csv                      → 77 cards, 3 fields, 0 malformed
26_Flashcards/32_engineering_math.csv                    → 80 cards, 3 fields, 0 malformed
Repo-wide link check                                     → 11 broken, all pre-existing in
                                                           01_Foundations and 30_Capstones
```

The link check found one new break introduced last session —
`32_Engineering_Math/_solutions/08_adversary_path_solutions.md` linked to `../01_Foundations/`
from inside `_solutions/`, one level too shallow. Fixed. The remaining 11 are the known
`01_Foundations/_solutions/` debt plus `30_Capstones/.../_reference_solution/`, both tracked in
`COURSE_PROGRESS.md`.

### Docs updated

`COURSE_PROGRESS.md` (module 32 → ✅, quiz and flashcard rows, verified-artifacts rows, cert
coverage, known issue 3 resolved and issue 7 added for the `psec` defects, next work item
renumbered), `PHASES.md` (Phase 6 → ✅ COMPLETE with the lesson-list deviation and both defects
recorded), `docs/CURRENT_TASK.md`, `docs/HANDOFF.md` (two architectural decisions amended, one
added, Session 4 carry-overs section, next work item), `CLAUDE.md`, `28_Calculators/README.md`,
`16_Automation/README.md` (all test counts 66 → 68).

### Follow-ups

- **`01_Foundations/_solutions/` is now the oldest and only remaining solution debt** — 4 files
  plus `vocabulary.md` and `checklist_foundations.md`. It is the next work item.
- **`01_Foundations/03_functional_chain.md` links to `28_Calculators/timely_detection.py`**, which
  no longer exists; it was superseded by `psec/pps.py`. Fix it when closing the module 01 debt,
  and point it at `32_Engineering_Math/08_adversary_path.md`, which now derives it.
- **`03_Video_Surveillance/` is mathematically unblocked.** Module 32 lessons 01–04 supply the
  optics, bandwidth, and storage derivations, so that module can cover the imaging chain, camera
  selection, and design judgment without re-deriving anything.
- **Three** provisional APP/PSP mapping tables now need correcting when the ASIS block clears.
- **A testing convention worth adopting repo-wide:** where a figure has a known correct value
  derivable from a definition, assert against the definition, not against a captured run. The
  `video.py` defect survived 66 passing tests precisely because no test did this.

### Commit record

| Commit | Scope |
|---|---|
| `8db0da4` | Module 32 lessons 01–08 with solutions; fix `video.py` binary units |
| `0e12f21` | Module 32 overview and integrated sizing capstone |
| `2c2f9ca` | Quiz 32 + key, flashcards, doc updates, link fix |
| `0c1884c` | Merge `module/32-engineering-math` to `main` |

---

## 2026-08-08 — Session 5: close Module 01's solution debt

Branch `module/01-foundations-solutions` off `main`. ~37k words across 10 files. **The repo's
oldest open debt**, carried since Session 1.

### What was missing, and the count that was wrong

Module 01 shipped in Session 1 with **9 dangling links** — before the
write-solutions-in-the-same-commit convention existed. Every doc since has recorded this as
*"4 missing solution files."*

**There were 6.** Lessons 02 through 07 each carry an exercise set. The number was recorded once,
early, and copied forward across four sessions without ever being re-counted against the files.
Worth logging as a general caution: **re-derive a tracked number before acting on it.** The
link-check script would have caught this at any point; nobody ran it against module 01 until now.

### Content written

- **`_solutions/02_risk_vocabulary_solutions.md`** — 8 practice problems plus the full risk chain
  for two of them. Marked on the *second* half of each question (what you would need to know),
  because that is where the engineering is.
- **`_solutions/03_functional_chain_solutions.md`** — E3.1's five missing-function cases,
  **E3.2's timely-detection arithmetic**, the function-mapping table, and the 100-word plain-English
  explanation with a breakdown of what makes it work.
- **`_solutions/04_zones_solutions.md`** — zone diagram and integrity checklist against a synthetic
  building, the 12-item SPOF enumeration ranked by cost-effectiveness, and the $50k-door
  conversation.
- **`_solutions/05_cpted_solutions.md`** — the six-condition table, the glass-lobby problem solved
  without losing the architect's design, and the $15,000 allocation with its ordering rule
  (restore before you add; buy signals before hardware).
- **`_solutions/06_requirements_solutions.md`** — vague-to-testable conversions, the four
  pathologies, **E6.4's submittal review**, and E6.5's budget cut against a constructed
  SEC-001..014 set.
- **`_solutions/07_systems_failure_solutions.md`** — the intrusion chain and its failure table,
  the PoE switch FMEA, five emergent failures, and **E7.5's analytics workload arithmetic**.
- **`vocabulary.md`** — full module glossary plus a routinely-confused disambiguation table.
- **`checklist_foundations.md`** — the reasoning checklist: 8 sections of *questions*, closing with
  the five that catch the most.
- **`exercises.md`** + **`_solutions/exercises_solutions.md`** — see below.

### Design decisions worth recording

- **`exercises.md` was ambiguous scope and became the module capstone.** The overview promised
  "practice + scenarios," but every lesson already carries its own exercises, so a separate file
  risked duplication or a second dangling link. It is now an index of the per-lesson sets **plus
  the Ashford Public Library capstone** — one site through all 7 lessons, Parts A–G, with a full
  reference solution. That also gives module 01 the capstone it lacked, matching modules 32 and 35.
- **The capstone is a library on purpose.** Every worked example in module 01 is a warehouse, an
  office, or a server room — buildings where hardening is culturally acceptable and the assets are
  property. A library inverts both: the mission is unrestricted public access, and the most
  valuable asset is staff, not the collection. Most of the module's instincts produce the wrong
  answer there, which is what the exercise tests. **The tell for a weak submission is a proposal
  that controls the entrance.**
- **The capstone's Part B produces a result none of the module's other examples do.** Worked
  through six variants with `psec.pps`: moving detection to the point of entry gains only 40 s
  against a 215 s deficit, because the **90 s assessment delay** is the binding term, not the
  sensor placement. Detection works only when the sensor moves outside the building *and*
  assessment drops to 20 s — and at the realistic unverified-alarm response of 15 minutes the
  required detection point goes **negative**, so detection is not achievable at all. The delay
  lever (a safe, +325 s of margin) is decisively correct, which is the **opposite** of the
  warehouse conclusion in E3.2 and in module 32's capstone. The solution states why the answers
  differ: asset size, who controls response, and what the institution is for.
- **Exercises done against the learner's own building get marking criteria plus a synthetic
  worked reference**, not a single "answer" — the pattern module 35's survey reference
  established. All fictional buildings labelled synthetic per `AI_CONTEXT.md` hard rule 4.
- **E6.5's SEC-001..014 table is constructed and flagged as such.** The lesson refers to it but
  shows only four RTM rows; the solution says so rather than pretending the set exists.
- **Every calculation was computed by running `psec` and transcribing**, per the module 32
  convention — E3.2 and capstone Part B with `psec.pps`, E6.4 with `psec.optics`, E7.2 with
  `psec.power`. Two results worth noting because they make the exercises sharper than intended:
  E6.4's submitted lens crosses a **DORI class boundary** (81.8 PPF identify → 62.8 recognise),
  and E7.2's 24 802.3af cameras on a 370 W switch land at **99.9% utilisation with 0 free ports**,
  so "PoE budget exceeded" is the as-designed state rather than a hypothetical failure mode.

### Code and link fixes

**`01_Foundations/03_functional_chain.md` linked to `28_Calculators/timely_detection.py`**, which
was superseded by `psec/pps.py` in Phase 3 and never updated — a stale link that survived four
sessions. It now points at `psec/pps.py` and at `32_Engineering_Math/08_adversary_path.md`.

No Python changed this session.

### Verification

```
python3 28_Calculators/tests/test_psec.py                → Ran 68 tests, OK
python3 28_Calculators/demo.py                           → clean
python3 16_Automation/data_model/validate.py <sample> CD → 25 errors / 5 warnings / 4 info
                                                           (unchanged baseline)
Repo-wide link check                                     → 1 broken, down from 11
```

**The one remaining broken link repo-wide** is
`30_Capstones/data_center_campus/00_BRIEF.md` → `_reference_solution/`, which is
`COURSE_PROGRESS.md` known issue 4. Every other relative target in every written module resolves.

### Docs updated

`COURSE_PROGRESS.md` (module 01 row, quality-bar line, verified-artifacts rows, known issues 2 and
6 resolved, next work item renumbered), `PHASES.md` (Phase 2 → ✅ COMPLETE with the wrong-count
correction and the capstone rationale), `docs/CURRENT_TASK.md`, `docs/HANDOFF.md` (solutions
decision amended, Session 5 carry-overs, next work item).

### Follow-ups

- **`03_Video_Surveillance/` is the next work item and is fully unblocked.** Module 32 lessons
  01–04 supply all of its math; those lessons should be cross-referenced, not repeated.
- **`30_Capstones/data_center_campus/_reference_solution/` is now the only solution debt in the
  repo.** It is 25 deliverables and depends on `20_Data_Center/`, so it is sequenced after that
  module rather than treated as a quick fix.
- **A process note worth keeping:** run the link check against a module *before* declaring its
  debts, not just after writing it. A four-session-old count was wrong by 50% and nothing caught
  it because the check was only ever run on new work.
- Three provisional APP/PSP mapping tables still need correcting when the ASIS block clears.

### Commit record

| Commit | Scope |
|---|---|
| `a653978` | Module 01 solutions for lessons 02–03; fix stale calculator link |
| `7f0112c` | Module 01 solutions for lessons 04–05 |
| `3954145` | Module 01 solutions for lessons 06–07 |
| `3faed54` | vocabulary.md, checklist_foundations.md, exercises.md + capstone, doc updates |
| `426f5fc` | Merge `module/01-foundations-solutions` to `main` |

---

## 2026-08-09 — Session 6: Module 03 Video Surveillance (complete)

Branch `module/03-video-surveillance`. **~76k words across 25 files** — the largest module in the
academy — plus Quiz 03 and a 114-card deck. Phase 7 complete; roadmap months 3 and 4 unblocked.

### What was written

`03_Video_Surveillance/`: overview + 11 lessons, each with a `_solutions/` file written in the
**same commit** as the lesson linking to it. Plus the Cedar Junction park-and-ride capstone with a
full reference solution, `25_Quizzes/quiz_03_video_surveillance.md` (30 Q / 54 pts) with an
isolated key, and `26_Flashcards/03_video_surveillance.csv` (114 cards, 0 malformed).

Lessons: 01 imaging chain · 02 optics and lenses · 03 sensors and low light ·
04 DORI and pixel density · 05 camera form factors · 06 compression and bandwidth ·
07 storage and retention · 08 VMS architecture · 09 camera placement · 10 retail case study ·
11 analytics and health monitoring.

### The governing decision

**Module 32 derives the math; module 03 applies it and re-derives nothing.** The overview opens
with a **division-of-labour table** — *"why is `W = D·w/f` true?"* → module 32; *"should this
camera be looking there at all?"* → module 03. Every lesson needing a formula links out and states
only the result. Without this the module would have duplicated roughly 40% of module 32.

This is now a repo convention, recorded in `HANDOFF.md`, and **module 04 should apply it against
module 35.**

### Three results that inverted the expected answer

Each was planned as one thing, computed as another, and the computed version became the lesson.

1. **The vestibule camera passes the geometry at 2.11× the identify threshold and is still
   unusable at night.** A 1/30 s shutter smears a walking subject across **23.5 px** against a
   **33.4 px** eye-to-eye distance. Generalised in the solutions: **the smear-to-detail ratio is
   invariant under pixel density** — 0.704 at both 12 ft and 22 ft, because both scale with PPF and
   the ratio cancels. Resolution cannot fix blur; only a faster shutter (light) or a slower subject
   (a chokepoint) can. This is the module's most transferable result.
2. **Camera count is a ceiling function.** An 8 MP upgrade needs the *same* count as 4 MP on a
   90 ft elevation at both recognise and identify — the extra pixels never cross an integer
   boundary, so they are wasted while still costing 1.03 stops of light and double the storage.
   Vendors quote coverage width (continuous); you buy cameras (integers).
3. **A 99% false-alarm reduction still leaves 0.905% precision** at 2 true events/year. The base
   rate, not the detector, is the constraint — so analytics belong in retrospective search, where a
   false positive costs one second to dismiss, not in low-base-rate live alarms.

### A correction made mid-module

Lesson 01's exercise E1.1(c) attributed a soft face beside a sharp plate to depth of field.
Checking it with real numbers showed the claim holds **only for long lenses**: at 12 mm both planes
are in focus (22.1–46.5 ft at f/1.4); at 50 mm focused on a plate at 40 ft the DOF is **2.2 ft**.
The condition is now stated explicitly in the solution. **Compute before asserting, even when the
claim is textbook** — this is the same class of error as the module 01 "4 missing files" count.

### Two gaps in `psec`, deliberately not filled

Module 03 needed **depth of field** (hyperfocal, near/far limits) and **motion blur**
(`smear_px = speed × exposure × PPF`) routinely. Neither exists in `psec`. Both are geometric,
testable against hand calculations, and belong in `psec.optics`.

**They were not added.** This repo's architecture is that `32_Engineering_Math/` derives what
`28_Calculators/` implements, so adding them properly means writing derivations in module 32 first
— reopening a module marked complete. Instead the arithmetic is shown in full in module 03 lessons
01, 02, and 03 so it can be hand-checked, with an explicit note in lesson 02 explaining why it is
not in the calculator. Logged as `COURSE_PROGRESS.md` known issue 8 and `HANDOFF.md` debt 6.

### The capstone

**Cedar Junction park-and-ride** — chosen, per the module 01 and 32 pattern, to break its own
module's instincts. Three traps: identify-at-the-incident (128 cameras, still fails on occlusion
and pose); light-is-always-binding (**29 of 34 incidents happened in daylight**, so the lighting
argument survives only in its precise form — levels 1–3 are enclosed and measure 2.5 lux *at
noon*); and where the chokepoint is (the **pedestrian cores**, not the vehicle portal, because
offenders arrive on foot).

The timeliness analysis governs the design: even with **instant detection and zero assessment**, a
720 s response exceeds the 130 s task time by **590 s**, so no detection point on the site can be
timely. The answer is 42 cameras with identify at the cores — and a top recommendation (access
control on the uncontrolled pedestrian street gate) that **shrinks the video scope**, which is the
professional act `AI_CONTEXT.md` names.

Its conclusion is deliberately distinct from module 01's Ashford Library capstone, which also finds
detection cannot be timely but lands on **delay**; the garage lands on **deterrence and access
control**, because delay is not available at a parked car.

### Verification

```
python3 28_Calculators/tests/test_psec.py                    # 68 tests → OK (unchanged)
python3 28_Calculators/demo.py                               # clean
python3 16_Automation/data_model/validate.py ... CD          # 25 err / 5 warn / 4 info
repo-wide link check                                         # 1 broken (module 30, known)
26_Flashcards/03_video_surveillance.csv                      # 114 cards, 0 malformed
```

**No code was changed this session**, so the test count remains 68.

The link check caught **three relative-depth errors** in new files before merge — the recurring
authoring bug flagged in the Session 5 handoff. Two were `_solutions/` files linking to a sibling
lesson without `../`; one was an answer key in `25_Quizzes/_answer_keys/` needing `../../`. Running
the check before committing remains non-negotiable.

### Commit record

| Commit | Content |
|---|---|
| `3de3221` | Module 03 overview and lesson 01 (imaging chain) |
| `9b6d691` | Lessons 02–03 (optics, sensors and low light) |
| `7ff9177` | Lessons 04–05 (DORI in practice, form factors) |
| `b6e27c5` | Lessons 06–08 (bandwidth, storage, VMS architecture) |
| `6048774` | Lessons 09–11 (placement, retail case study, analytics) |
| `1de601c` | Capstone, Quiz 03 + key, flashcard deck |
| `f24945d` | Doc updates, link fixes, Phase 7 closed |
| `c3ac8b1` | Merge `module/03-video-surveillance` to `main` |
