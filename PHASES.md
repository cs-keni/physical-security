# PHASES.md — Building the Academy

Build plan for the repository itself. (For *studying* it, see
[`00_Roadmap/study_roadmap.md`](00_Roadmap/study_roadmap.md).)

Ordering principle: **build what unblocks the learner's next month first.** A perfect module
12 is worthless while module 1 has gaps.

---

## Phase 0 — Research and structure ✅ COMPLETE

- [x] Research current ASIS APP/PSP requirements (**blocked at source — documented, not
      guessed**)
- [x] Verify Bluebeam Revu 21 Complete feature availability against official documentation
- [x] Identify curriculum gaps and improve the structure (22 topics added)
- [x] Create the repository structure (39 directories)
- [x] `README.md` with repo map, ground rules, conventions
- [x] `31_References/source_index.md` with tag system and confidence disclosure

## Phase 1 — Roadmap and governance ✅ COMPLETE

- [x] `00_Roadmap/how_to_use_this_academy.md` — study method, cadence, software-background bridge
- [x] `00_Roadmap/study_roadmap.md` — 12 months, 8 checkpoints
- [x] `00_Roadmap/skills_matrix.md` — 8 competency areas × 4 levels
- [x] `00_Roadmap/progress_tracker.md`
- [x] `00_Roadmap/curriculum_gap_analysis.md`
- [x] `COURSE_PROGRESS.md`
- [x] `docs/` — AI_CONTEXT, HANDOFF, CURRENT_TASK, ENGINEERING_LOG

## Phase 2 — Foundations ✅ COMPLETE (solutions outstanding)

- [x] Module overview with objectives and certification mapping
- [x] 01 — What Physical Security Engineering Is
- [x] 02 — The Risk Vocabulary
- [x] 03 — The Functional Chain (D3ACR + timely detection)
- [x] 04 — Defense in Depth and Security Zones
- [x] 05 — CPTED
- [x] 06 — Requirements Engineering
- [x] 07 — Systems Thinking and Failure Thinking
- [x] Quiz 01 (30 questions) + full answer key with explanations
- [x] Flashcard deck (58 cards, validated)
- [ ] `_solutions/` for the 4 sets of embedded exercises
- [ ] `vocabulary.md`, `checklist_foundations.md`

## Phase 3 — Working tooling ✅ COMPLETE

- [x] `psec.optics` — FOV, lens selection, slant range, depression, PPF, DORI
- [x] `psec.video` — bitrate, storage, retention, ranges, RAID
- [x] `psec.power` — PoE budgets, voltage drop, conductor selection, battery
- [x] `psec.pps` — adversary paths, timely detection, intervention comparison
- [x] 68 tests, all passing, expected values hand-computed
- [x] `demo.py` — 8 worked examples with engineering interpretation
- [x] `28_Calculators/README.md` — assumptions and explicit non-goals
- [x] Security Device Data Model — schema, 6 projections, 11 validation rules
- [x] Synthetic flawed dataset for the design-review exercise
- [x] `16_Automation/README.md`

## Phase 4 — First lab and the capstone target ✅ COMPLETE

- [x] Project 1 brief — deliberate ambiguities, self-assessment checklist
- [x] Project 1 senior reference solution — full worked design
- [x] Data center campus capstone brief — fictional site, 25 deliverables, 12 ambiguities

---

## Phase 5 — Unblock month 1 ✅ COMPLETE

Module 35 shipped complete across Sessions 2 and 3. Roadmap months 1, 4, and 8 are unblocked and
Project 1 has its prerequisite. First module in the repo with no outstanding solution debt.

- [x] `35_Doors_and_Hardware/` module overview
- [x] 01 — Door anatomy and terminology
- [x] 02 — Handing, swing, secure side
- [x] 03 — Locking hardware families
- [x] 04 — Fail safe vs fail secure
- [x] 05 — Egress, delayed egress, controlled egress `[CODE][VERIFY]`
- [x] 06 — Electrified hardware and power transfer
- [x] 07 — Fire-rated openings `[CODE][VERIFY]`
- [x] 08 — Key management and mechanical security (gap-analysis addition)
- [x] `_solutions/` for all 8 lessons (written alongside the lessons, so this module does not
      repeat the Module 01 dangling-solutions debt)
- [x] Field exercise: survey and annotate 10 real doors, with a reference findings set
- [x] Quiz 35 (30 questions) + isolated answer key with full explanations
- [x] Flashcard deck (77 cards, validated)

## Phase 6 — Engineering math ✅ COMPLETE

Write the derivations for what Phase 3 already implements. Source the worked values from
`28_Calculators/tests/test_psec.py`.

- [x] `32_Engineering_Math/` module overview
- [x] 01 Camera FOV and focal length
- [x] 02 Pixel density and DORI
- [x] 03 Bandwidth
- [x] 04 Storage and retention
- [x] 05 PoE budgets **and port/capacity planning** (see deviation below)
- [x] 06 Voltage drop
- [x] 07 Battery and UPS sizing
- [x] 08 **Adversary path and timely detection** (see deviation below)
- [x] Problem sets + separated answer keys for each
- [x] Integrated sizing capstone + reference solution
- [x] Quiz 32 (30 questions) + isolated answer key with full explanations
- [x] Flashcard deck (80 cards, validated)

### Deviation from the original lesson list, and why

The planned item 08 was **"Rack, port, and capacity planning."** It was **folded into lesson 05**
instead, and **08 became "Adversary path and timely detection."** Two reasons:

1. Port count, oversubscription, and spare-port policy **are** the `PoESwitch` checks. Splitting
   them from the PoE power budget would have separated two constraints whose whole lesson is that
   they bind independently. Lesson 05 now teaches both and shows which one binds for a given mix.
2. `28_Calculators/psec/pps.py` had substantial tested math — `AdversaryPath`, the timeliness
   inequality, `required_detection_point_s`, `compare_interventions` — with **no derivation
   anywhere in the repo**. Since this module is the derivation record for `psec`, leaving `pps.py`
   underived would have left the module incomplete against its own stated purpose.

### Two defects found by working the units by hand

Both fixed in the same branch, both with new tests. **Test count 66 → 68.**

1. **`video.stream_gb_per_day(decimal_gb=False)` divided decimal megabytes by 1024.** A bitrate is
   decimal, so the intermediate megabytes are 10⁶ bytes; converting to GiB requires dividing by
   2³⁰/10⁶ = 1073.741824. The bug reported the decimal/binary gap at TB scale as 4.86% when the
   true figure is 9.95% — the exact "classic ~10% error" its own docstring warned about. No test
   caught it because the only test on that path asserted `binary < decimal`, true either way.
   Fixed with named constants plus `test_binary_units_are_true_gibibytes` and
   `test_decimal_binary_gap_at_tb_scale_is_about_ten_percent`.
2. **`pps.compare_interventions` docstring said "three levers" and returns four.** Fixed, with the
   module-32 cross-reference added.

## Phase 7 — Video surveillance ⬜

11 lessons through the imaging chain, plus the retail case study and Projects 2 and 4.

## Phase 8 — Access control ⬜

11 lessons, plus Project 3 and the SOO template library.

## Phase 9 — Risk assessment ⬜

7 lessons including adversary path analysis and security master planning.

## Phase 10 — Infrastructure ⬜

Networking (8), Electrical Power (6), plus Project 5 (warehouse).

## Phase 11 — Codes, documents, specifications ⬜

Codes & Standards (8), Construction Documents (8), Division 28 (6), Design Review QA flawed
packages, plus Project 6.

## Phase 12 — Tools ⬜

Bluebeam (8, Complete-plan only), Revit (6), AutoCAD (4), Excel (5) + templates.

## Phase 13 — Remaining systems ⬜

Intrusion (6), Perimeter incl. lighting (7), Intercom (3), plus Project 7.

## Phase 14 — Cyber, commissioning, operations ⬜

Cybersecurity (8), Commissioning (5) + forms, Operations (5).

## Phase 15 — Data center and capstone solution ⬜

Data Center module (8), capstone reference solution, capstone site geometry.

## Phase 16 — Breadth ⬜

Facility case studies (11), Human Factors/Privacy/Ethics, Project Management incl. cost
estimating, Products & Ratings.

## Phase 17 — Certification tracks ⬜

**Blocked** on verifying ASIS domains against the official Certification Handbook.
APP track, PSP track, CPP roadmap.

## Phase 18 — Continuous ⬜

- [ ] Cumulative quizzes and spaced-repetition review schedules
- [ ] Flashcard decks per module
- [ ] Templates library
- [ ] Automation tooling expansion
- [ ] Source index growth

---

## Quality gate — applies to every phase

Before checking any box:

- [ ] The file contains real instructional material, not headings
- [ ] Worked examples use real numbers and show the arithmetic
- [ ] Exercises exist, and solutions live in `_solutions/` or `_answer_keys/`
- [ ] Junior vs. Senior distinction is present
- [ ] Common mistakes section is present and specific
- [ ] Every code/standard claim is tagged and, where uncertain, marked `[VERIFY]`
- [ ] Sources logged in `31_References/source_index.md`
- [ ] Any code added is tested and the test passes
- [ ] `COURSE_PROGRESS.md` updated
