# Physical Security Engineering Academy

A self-directed, university-grade curriculum for becoming an independent physical security
design engineer — from placing a single door contact through designing, documenting,
commissioning, and operating the security systems for a data center campus.

**Built for:** an entry-level Physical Security Engineer at a large engineering/consulting
firm, with a CS degree and strong software background, and beginner-level physical
security knowledge.

**Success criterion** (not "I passed a cert"):

> Give me a facility, its mission, its assets, its threats, its drawings, and its
> operational requirements, and I can systematically reason through how its physical
> security should be designed, documented, integrated, tested, commissioned, maintained,
> and improved — and clearly explain why I made every major decision.

---

## Start here

1. **[`00_Roadmap/how_to_use_this_academy.md`](00_Roadmap/how_to_use_this_academy.md)** — read this first. 10 minutes.
2. **[`00_Roadmap/study_roadmap.md`](00_Roadmap/study_roadmap.md)** — the 12-month plan with monthly checkpoints.
3. **[`00_Roadmap/skills_matrix.md`](00_Roadmap/skills_matrix.md)** — Beginner → Working → Independent → Advanced, per competency.
4. **[`00_Roadmap/progress_tracker.md`](00_Roadmap/progress_tracker.md)** — your live checkbox tracker.
5. **[`01_Foundations/`](01_Foundations/)** — begin studying.

If you are a **coding agent** resuming work on this repository, read
[`COURSE_PROGRESS.md`](COURSE_PROGRESS.md) and [`docs/HANDOFF.md`](docs/HANDOFF.md) first.

---

## Repository map

| Dir | Contents |
|---|---|
| `00_Roadmap/` | Roadmap, skills matrix, progress tracker, curriculum design rationale |
| `01_Foundations/` | Security engineering first principles, risk vocabulary, D3ACR, defense in depth, CPTED, requirements engineering |
| `02_Risk_Assessment/` | Threat/vulnerability/risk assessment methodology, site surveys, security master planning |
| `03_Video_Surveillance/` | Optics → sensor → codec → network → VMS → storage → operator. Camera types, placement, DORI/PPF |
| `04_Access_Control/` | Credentials, readers, controllers, PACS architecture, door sequences of operation |
| `05_Intrusion_Detection/` | Sensor physics, selection, placement, nuisance-alarm engineering, supervision |
| `06_Perimeter_Security/` | Fencing, HVM, barriers, gates, PIDS, lighting, vehicle/pedestrian screening |
| `07_Intercom_Communications/` | Intercom, SIP, help points, emergency phones, mass notification |
| `08_Networking/` | Security-system networks: VLANs, PoE, fiber, multicast, QoS, MDF/IDF |
| `09_Cybersecurity/` | Hardening, segmentation, evidence integrity, chain of custody, threat modeling of PACS/VMS |
| `10_Codes_Standards/` | IBC/IFC, NFPA 72/101, NEC, UL 294, ADA, ASIS, ONVIF, OSDP, BICSI, NIST — how to navigate, not memorize |
| `11_Division_28/` | CSI MasterFormat Div 28, spec anatomy, spec↔drawing↔schedule coordination |
| `12_Bluebeam/` | Revu 21 **Complete** workflows (no Max/cloud-AI features assumed) |
| `13_Revit/` | BIM for security engineers: families, parameters, schedules, sheets, coordination |
| `14_AutoCAD/` | Layers, blocks, attributes, Xrefs, layouts, security device plans and risers |
| `15_Excel/` | Tables, dynamic arrays, Power Query, and the engineering calculators/schedules |
| `16_Automation/` | Python tooling, the **Security Device Data Model**, QA automation, synthetic data |
| `17_Construction_Documents/` | Drawing literacy: plans, RCPs, risers, schedules, details, revisions |
| `18_Commissioning/` | Test procedures, forms, point-to-point, functional testing, acceptance |
| `19_Operations/` | SOC ops, alarm handling, SOPs, maintenance, badge lifecycle |
| `20_Data_Center/` | Data center physical security — the deepest applied module |
| `21_Facility_Case_Studies/` | Office, campus, retail, warehouse, hospital, school, water, industrial, lab, garage, government |
| `22_APP/` | ASIS APP certification track |
| `23_PSP/` | ASIS PSP certification track |
| `24_CPP_Roadmap/` | Long-horizon CPP roadmap |
| `25_Quizzes/` | Cumulative quizzes; answer keys isolated in `_answer_keys/` |
| `26_Flashcards/` | Spaced-repetition decks (CSV, Anki-importable) |
| `27_Labs/` | Progressive Projects 1–8 and skill labs; solutions in `_solutions/` |
| `28_Calculators/` | Working, tested Python calculators (FOV, PPF, storage, bandwidth, PoE, Vdrop, battery) |
| `29_Templates/` | Schedules, trackers, checklists, BoD and SOO templates |
| `30_Capstones/` | Data center campus capstone; reference solution isolated |
| `31_References/` | `source_index.md` — every claim's source, by module |
| `32_Engineering_Math/` | Formula workbook: derivation, units, assumptions, worked examples, problem sets |
| `33_Design_Review_QA/` | Intentionally flawed drawing packages to review; findings hidden |
| `34_Electrical_Power/` | Practical LV electrical for security: Ohm's law → Vdrop → PoE → battery → UPS |
| `35_Doors_and_Hardware/` | Door anatomy, hardware, fail safe/secure, egress, fire-rated openings |
| `36_Human_Factors_Privacy_Ethics/` | Operator performance, alarm fatigue, deterrence psychology, privacy/legal escalation |
| `37_Project_Management/` | Scope, deliverables, RFIs, submittals, client communication, technical writing |
| `38_Products_and_Ratings/` | Reading datasheets objectively; IP/IK/NEMA/UL ratings, environmental selection |

---

## Ground rules baked into this curriculum

1. **No confidential material, ever.** Every exercise uses fictional or public data. Never
   upload client drawings, real facility layouts, credential databases, or proprietary
   specs into any tool — including AI tools. See `36_Human_Factors_Privacy_Ethics/`.
2. **Never invent a code requirement.** Every code/standard reference states its edition
   and is labeled *code / standard / guideline / best practice / manufacturer recommendation*,
   plus whether it is jurisdiction-dependent and must be confirmed with the AHJ.
3. **Defensive security only.** The cybersecurity track teaches protection, detection,
   integrity, and forensics — not intrusion technique.
4. **Automate the repetitive; never automate the judgment.**
5. **Solutions are separated** from exercises so you cannot spoil yourself by scrolling.

---

## Conventions

- `[CODE]` `[STANDARD]` `[GUIDELINE]` `[PRACTICE]` `[MFR]` — tags used inline to classify any requirement.
- `[VERIFY]` — a claim you must confirm against a primary source or the AHJ before using on a real project.
- **ELI5** blocks precede the professional explanation for hard concepts.
- **Junior / Senior** blocks appear in every module: what each level is expected to know.
- 🧮 marks a worked calculation. 🔧 marks a hands-on lab. ⚠️ marks a common mistake.

---

## License / status

Personal study material. Not professional engineering advice. Nothing here substitutes for
a licensed engineer's judgment, the applicable adopted codes in your jurisdiction, or the AHJ.
