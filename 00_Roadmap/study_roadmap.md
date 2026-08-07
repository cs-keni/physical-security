# Master Study Roadmap — 12 Months

Designed for **6–8 hours/week** alongside full-time work. 12 months of sustained study at
this pace ≈ 350 hours, which is roughly the deliberate-practice equivalent of 2–3 years of
passive on-the-job absorption — *if* you do the labs.

Five stages, four checkpoints. The stages overlap deliberately; you do not finish
"Foundation" and then start "Working Competency."

---

## Stage map

| Stage | Months | Theme | You can... |
|---|---|---|---|
| **I — Foundation** | 1–2 | Vocabulary, risk logic, how a project runs | Follow a design conversation without getting lost |
| **II — Working Competency** | 3–5 | The four core systems + drawings + math | Mark up a package and defend your device placement |
| **III — Independent Designer** | 6–8 | Full design lifecycle, codes, specs, networks | Produce a small-facility design package end to end |
| **IV — Advanced Designer** | 9–11 | Complex facilities, integration, cyber, commissioning | Lead the security scope on a mid-size project |
| **V — PSP-Level Development** | 12+ | Assessment methodology, master planning, judgment | Reason from mission → risk → design without a template |

---

## Month 1 — Foundations & Vocabulary

**Modules:** `01_Foundations/` (all), `35_Doors_and_Hardware/` (01–02), `17_Construction_Documents/` (01)

| Week | Focus | Deliverable |
|---|---|---|
| 1 | What physical security engineering is; asset/threat/vulnerability/risk vocabulary; risk equation | Vocabulary flashcards live in SRS; Quiz 01 ≥ 80% |
| 2 | Deter/Detect/Delay/Assess/Respond/Recover; defense in depth; security zones; CPTED | Written D3ACR analysis of a building you actually visit |
| 3 | Door anatomy and hardware; free egress; fail safe vs fail secure | Photograph and annotate 10 real doors |
| 4 | Drawing literacy: sheet sets, scales, symbols, keynotes, revisions | **Lab: Project 1 — Secure One Office Door** |

**Checkpoint 1 (end of month 1):**
- [ ] You can define, unprompted: asset, threat, hazard, vulnerability, likelihood, consequence, risk, residual risk, risk tolerance, countermeasure, mitigation.
- [ ] You can explain why *deter, detect, delay, assess, respond, recover* is an ordered functional chain and what happens when a link is missing.
- [ ] You can look at any door and state: swing, handing, hinge side, secure side, lock type, whether it has free egress, and whether it should be fail safe or fail secure — and why.
- [ ] You can read a sheet number, find a detail from its callout, and identify the scale of a plan.
- [ ] You have completed Project 1 with a written narrative.

---

## Month 2 — Risk Assessment & Design Process

**Modules:** `02_Risk_Assessment/`, `37_Project_Management/` (01–02), `01_Foundations/06` (requirements)

| Week | Focus | Deliverable |
|---|---|---|
| 5 | Asset characterization, threat assessment, adversary paths | Asset register for a fictional site |
| 6 | Vulnerability assessment, site survey methodology, survey checklist | Conduct a real site survey (your own office building, externally observable only) |
| 7 | Qualitative vs quantitative risk, risk matrices and their failure modes | Risk register with justified ratings |
| 8 | Design lifecycle: BoD → SD → DD → CD → bid → construction → closeout; who does what | Map a real project at your firm to the lifecycle stages |

**Checkpoint 2 (end of month 2):**
- [ ] You can run a structured site survey and produce findings that are *observations*, not opinions.
- [ ] You can turn "we need this building to be secure" into ≥ 15 testable requirements.
- [ ] You can name every design phase, its deliverables, and what a junior engineer contributes at each.
- [ ] You can explain why a 5×5 risk matrix is useful for communication and dangerous for decision-making.

---

## Month 3 — Video Surveillance I: Optics, Sensors, Coverage

**Modules:** `03_Video_Surveillance/` (01–05), `32_Engineering_Math/` (FOV, PPF)

| Week | Focus | Deliverable |
|---|---|---|
| 9 | Light → lens → sensor → ISP. Focal length, FOV, aperture, exposure triangle, DOF | Hand-calculate 10 FOV problems |
| 10 | DORI, pixel density (PPF/PPM), when each target class applies | Pixel density problem set, 100% |
| 11 | Camera form factors and the real tradeoffs; multisensor vs PTZ vs fisheye | Written comparison memo |
| 12 | Placement engineering: mounting height, angle, glare, backlight, choke points | **Lab: Project 2 — Small Office Camera Design** |

**Checkpoint 3a:** You can look at a floor plan and place cameras with a stated pixel-density
target per camera, and justify every lens choice numerically.

---

## Month 4 — Video Surveillance II: Encoding, Storage, VMS

**Modules:** `03_Video_Surveillance/` (06–10), `14_VMS`, `28_Calculators/`

| Week | Focus | Deliverable |
|---|---|---|
| 13 | H.264/H.265, GOP, CBR/VBR, smart codecs, artifacts, why vendor calculators disagree | Bandwidth estimates with stated assumptions |
| 14 | Storage math, retention, RAID concepts, failover, edge recording | Storage calculator built and validated |
| 15 | VMS architecture: recording/management/database servers, federation, redundancy | VMS architecture diagram for a 200-camera site |
| 16 | Retail camera case study — the "why are there four domes together?" module | **Lab: Project 4 — Retail Surveillance Design + senior critique** |

**Checkpoint 3b:** You can size storage and bandwidth for a 200-camera system, state every
assumption, and explain why the number is a *range*, not a value.

---

## Month 5 — Access Control & Doors

**Modules:** `04_Access_Control/`, `35_Doors_and_Hardware/` (03–06)

| Week | Focus | Deliverable |
|---|---|---|
| 17 | Credentials and card tech; why 125 kHz prox is obsolete; OSDP vs Wiegand | Credential technology comparison table |
| 18 | Controllers, readers, downstream boards, supervised inputs, EOL resistors | Wire a supervised input on paper; calculate EOL states |
| 19 | Locking hardware: strikes, mags, electrified locksets/panic; egress law | Door hardware decision tree |
| 20 | Sequences of operation; failure modes; fire alarm interface | **Lab: Project 3 — Office Suite Access Control + full SOO** |

**Checkpoint 4 (end of month 5 — the big one):**
- [ ] You can trace a credential presentation end-to-end through 11 components and name what fails at each.
- [ ] You can write a door sequence of operation that a contractor can build from and a commissioning agent can test.
- [ ] You can state, for any door, whether a mag lock is appropriate and what egress provisions it demands `[VERIFY with AHJ]`.
- [ ] You can size a 24 VDC power supply with battery backup for a 12-door system.

---

## Month 6 — Networking, Power, and Infrastructure

**Modules:** `08_Networking/`, `34_Electrical_Power/`, `32_Engineering_Math/` (PoE, Vdrop, battery)

| Week | Focus | Deliverable |
|---|---|---|
| 21 | Security network architecture, VLANs, segmentation, edge/core, MDF/IDF | Network diagram for a 3-story building |
| 22 | PoE standards and budgets, switch selection, uplinks, fiber | PoE budget calculator validated |
| 23 | Ohm's law applied; voltage drop; conductor sizing; power supplies; batteries | Voltage drop problem set |
| 24 | Cable types, distance limits, pathways, plenum, rack elevations | Cable schedule for Project 3 |

**Checkpoint 5 (6-month mark):**
- [ ] **You can independently produce a complete small-building security design package:** device plans, door schedule, camera schedule, sequences of operation, riser, cable schedule, and calculations.
- [ ] You can defend every device against "why is this here and what happens if it fails?"
- [ ] Begin the APP track in parallel (~2 hr/week) after confirming eligibility.

---

## Month 7 — Codes, Standards, and Life Safety

**Modules:** `10_Codes_Standards/`, `35_Doors_and_Hardware/` (07 fire-rated openings), Knox/fire access

| Week | Focus | Deliverable |
|---|---|---|
| 25 | The code landscape: model codes, adoption, amendments, AHJ authority | Determine what your own jurisdiction has adopted |
| 26 | Egress requirements and how they constrain security `[VERIFY]` | Egress conflict scenarios |
| 27 | NFPA 72 interfaces, fire alarm release, NEC basics for LV, UL 294 | Fire/security interface matrix |
| 28 | Knox boxes, first-responder access, life safety vs security tension | Written position memo |

---

## Month 8 — Documentation, Division 28, and Specifications

**Modules:** `11_Division_28/`, `17_Construction_Documents/` (full), `29_Templates/`

| Week | Focus | Deliverable |
|---|---|---|
| 29 | MasterFormat, spec anatomy (Parts 1/2/3), how to read a spec fast | Spec markup exercise |
| 30 | Drawing↔spec↔schedule↔detail coordination; finding contradictions | **Lab: `33_Design_Review_QA/` flawed package #1** |
| 31 | Basis of Design writing; assumptions and exclusions | BoD for Project 5 |
| 32 | Submittals, RFIs, shop drawings, substitution requests | Mock RFI responses |

**Checkpoint 6:** You can review a 30-sheet security package and produce a findings log a
senior engineer would sign.

---

## Month 9 — Tools: Bluebeam, Revit, AutoCAD, Excel

**Modules:** `12_Bluebeam/`, `13_Revit/`, `14_AutoCAD/`, `15_Excel/`

Tools are learned *after* the engineering, not before — otherwise you learn to produce
beautiful documentation of bad designs.

| Week | Focus | Deliverable |
|---|---|---|
| 33 | Bluebeam Revu 21 Complete: profiles, Tool Chest, custom tools, Markups List, custom columns | Security Tool Chest built |
| 34 | Sets, Batch Link, Batch Compare, Overlay, Spaces, measurement/calibration | Revision comparison report |
| 35 | Revit for security: families, shared parameters, schedules, views, sheets | Device family + schedule |
| 36 | AutoCAD + Excel schedules and calculators | Complete template set |

---

## Month 10 — Intrusion, Perimeter, Intercom, Integration

**Modules:** `05_Intrusion_Detection/`, `06_Perimeter_Security/`, `07_Intercom_Communications/`

| Week | Focus | Deliverable |
|---|---|---|
| 37 | Sensor physics and selection; nuisance vs false alarm; Pd/NAR/vulnerability to defeat | Sensor selection matrix |
| 38 | Perimeter systems, PIDS, fence/buried/beam, lighting design basics | Perimeter design for Project 7 |
| 39 | HVM, standoff, crash ratings, vehicle screening, sally ports | HVM concept study |
| 40 | Intercom/SIP, help points, mass notification | **Lab: Project 5 (Warehouse) + Project 7 (Water Facility)** |

---

## Month 11 — Cybersecurity, VMS/PACS Architecture, Commissioning

**Modules:** `09_Cybersecurity/`, `15_Access_Control_Software`, `18_Commissioning/`, `19_Operations/`

| Week | Focus | Deliverable |
|---|---|---|
| 41 | Threat modeling a VMS/PACS; segmentation, hardening, vendor access | System threat model |
| 42 | Evidence integrity, chain of custody, NTP, hashing, immutability, the deepfake question | Evidence integrity plan |
| 43 | Commissioning: point-to-point, functional, integrated systems testing | Commissioning forms completed for Project 3 |
| 44 | Operations: alarm handling, SOPs, maintenance, lifecycle | Ops narrative + PM plan |

**Checkpoint 7:** You can write a security systems cybersecurity plan and a full
commissioning plan with executable test scripts.

---

## Month 12 — Capstone: Data Center Campus

**Modules:** `20_Data_Center/`, `30_Capstones/`

Four weeks, full effort, on the capstone. Produce the entire package listed in
`30_Capstones/data_center_campus/00_BRIEF.md`. Do not open `_reference_solution/` until
you have submitted your own.

**Checkpoint 8 (12-month mark):**
- [ ] Complete data center campus security design package delivered.
- [ ] Self-review against the design review checklist, then compare to the reference solution.
- [ ] Gap list written; those gaps become months 13–18.
- [ ] APP sat or scheduled.

---

## Beyond month 12 — Stage V

- Second pass on `02_Risk_Assessment/` at PSP depth: adversary sequence diagrams, path
  analysis, EASI-style delay/response modeling, security master planning.
- Facility case studies you haven't done (`21_Facility_Case_Studies/`).
- Build the automation toolchain for real (`16_Automation/`) — this is your differentiator.
- Begin `23_PSP/` in earnest once eligible.
- Start teaching. Present a lunch-and-learn at your firm. Teaching is the final compression
  step; you will discover exactly which parts you only *think* you know.

---

## If you fall behind

You will. The failure mode is abandoning the whole plan after missing two weeks.

Recovery rule: **never skip the flashcards, never skip the Saturday block.** Everything else
can slip. A month at 3 hr/week that keeps both of those is worth more than a month at
10 hr/week followed by three months of nothing.

The roadmap is a guide to sequence, not a schedule to feel guilty about.
