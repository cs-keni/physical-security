# Capstone — Meridian Point Data Center Campus

> **The final examination of this academy.** Four weeks, full effort. Everything in the
> curriculum converges here.
>
> **All information in this brief is fictional.** No real facility's security design is
> represented. Do not substitute real project information at any point.

**Prerequisites:** Projects 1–7 complete; `20_Data_Center/` studied.
**Do not open [`_reference_solution/`](_reference_solution/) until you submit.**

---

## 1. The site

**Meridian Point** — a build-to-suit colocation data center campus for **Northvale
Infrastructure Partners**, an operator leasing space to enterprise and financial-services
tenants.

### Property
- 38-acre rectangular parcel, roughly 1,300 ft (E–W) × 1,270 ft (N–S).
- **North:** county arterial road, 4 lanes, 45 mph posted. Primary site access.
- **East:** a 60-ft municipal drainage easement, then a light-industrial park (occupied,
  24 hr operations, unfenced).
- **South:** undeveloped agricultural land, privately held, no structures. A farm track runs
  parallel ~200 ft from the property line.
- **West:** a rail spur (2 trains/day) on a 40-ft embankment approximately 12 ft above site
  grade, then a two-lane county road.
- Site grade falls approximately 8 ft from the northwest corner to the southeast.
- A 230 kV utility transmission corridor crosses the **southwest corner** diagonally, with a
  60-ft easement. **No permanent structures or fencing permitted within the easement**
  without utility approval.

### Buildings
| Building | Size | Contents | Phase |
|---|---|---|---|
| **DH-1** Data Hall 1 | 120,000 sf | 4 data halls (24,000 sf ea), 8 tenant cage zones, MDF/MMR, staging, loading dock | Phase 1 |
| **DH-2** Data Hall 2 | 120,000 sf | Identical program | **Phase 2 — shell only in Phase 1** |
| **ADM** Administration | 28,000 sf | Main lobby, SOC, offices, conference, tenant work areas, break room, NOC | Phase 1 |
| **UB-1 / UB-2** Utility | 18,000 sf ea | Generators (8 ea), fuel (2× 30,000 gal above-ground), switchgear, chillers, UPS | Phase 1 / Phase 2 |
| **GH** Gate House | 900 sf | Guard post, visitor processing, screening, restrooms | Phase 1 |
| **WY** Warehouse/Yard | 12,000 sf + 2-acre laydown | Spares, decommissioned equipment, contractor staging | Phase 1 |

- DH-1 and ADM are connected by a **single-story enclosed link** at the north end.
- All data halls are **slab-on-grade, 22-ft clear**, tilt-up concrete panel construction with
  a structural steel roof.
- ADM is two stories, steel frame, curtain wall on the north and east elevations.
- The DH-1 roof carries substantial mechanical equipment and is accessed by an exterior
  caged ladder on the west elevation plus an interior stair.

### Circulation
- **One vehicle entrance** from the north arterial, with a 220-ft stacking lane inside the
  property line before the gate house.
- A **secondary emergency-only gate** at the southwest, off a gravel access drive to the
  county road. Fire department has required this `[VERIFY with AHJ]`.
- Employee parking (80 spaces) north of ADM.
- Visitor parking (24 spaces) north of the gate house, **outside** the secure perimeter.
- Truck court and loading dock on the **east** side of DH-1: 4 dock positions, 1 grade-level
  roll-up, 140-ft truck maneuvering apron.
- A **separate fuel delivery route** to UB-1 along the south side.

### Operations
- **24/7/365.** Staffing: 3 security officers per shift (1 gate house, 1 SOC, 1 roving) plus
  a supervisor on days.
- 45 operations/facilities staff, day shift heavy.
- **Tenant access:** ~180 authorized tenant personnel across 14 tenants. Tenants access only
  their own cages, escorted or unescorted depending on their contract tier.
- **Contractors:** 20–60 on site daily during Phase 1 construction; 5–15 steady state.
- **Deliveries:** 8–15/day. Fuel delivery weekly.
- **Tours:** prospective-customer tours 2–4× per month, including through data hall
  perimeters.

---

## 2. The mission and the drivers

**Business mission:** provide contracted uptime and contracted physical security to
colocation tenants. Northvale's product *is* trust.

**What is actually driving this project:**
1. **Tenant contractual obligations.** Three anchor tenants are financial-services firms whose
   contracts specify physical access controls, audit trails, and third-party audit rights.
   Two require **SOC 2** reporting; one requires **PCI DSS**-relevant physical controls
   `[VERIFY current requirements — these are audit frameworks, not codes]`.
2. **An incident at a competitor's facility** 14 months ago (unauthorized person reached a
   customer cage via an unescorted contractor badge) that made the trade press. Northvale's
   sales team is asked about it in every deal.
3. **Insurance.** The carrier has asked for a physical security assessment.
4. A prospective anchor tenant's security team will **audit the design** before signing.

**Risk tolerance:** near zero for unauthorized access to a tenant cage. Moderate for property
crime in the laydown yard. The tolerance is set by *contract*, not by internal appetite —
identify what follows from that.

---

## 3. Assets, and what the operator will and won't tell you

**Stated by the client:**
- Tenant IT equipment (they don't know what's in the cages, by design and by contract)
- Continuity of operations — an outage is a contractual penalty event
- The MMR/MDF and carrier entrance facilities
- Generators, fuel, switchgear, chillers (an attack here causes an outage without entering a
  data hall)
- Staff safety

**Not stated, which you must surface:**
- The **reputational asset** — the ability to pass a tenant audit is itself the product
- Access control and video **data**, which is itself sensitive (a log of who entered whose
  cage when is competitively meaningful)
- The **fiber entrance paths and their physical routing** — a single-point-of-failure
  question nobody frames as security
- **Personnel information** in the badging system
- The **construction documents for this facility**, which the client will hand to a dozen
  contractors

---

## 4. Threat context (develop your own DBT from this)

Do **not** treat the following as your design basis threat. It is raw input. **Your first
deliverable is to develop and justify a DBT from it.**

- Regional property crime; copper theft from utility and construction sites is common in the
  county. Two incidents at nearby construction sites in the past year.
- The industrial park to the east has an **unfenced, occupied** yard. Its employees regularly
  walk the drainage easement at lunch.
- The rail embankment to the west **overlooks the site by ~12 ft**. Trains stop occasionally
  due to a signal 400 ft north.
- Activist interest in data center **water and power consumption** is documented regionally;
  one protest at a similar facility involved gate blockage and banner-hanging on fencing. No
  violence.
- Financial-services tenants raise **insider and social-engineering** threats specifically.
- The competitor incident: **unescorted contractor badge**, no forced entry, discovered on
  audit review 11 days later.
- No credible history of vehicle-borne attack in the region; the client's parent company
  standard nonetheless requires **"anti-ram protection at vehicle approaches"** with no
  further specification. `[This is deliberately vague. Resolve it.]`
- The county sheriff's average response to a verified alarm is **11 minutes**; to an
  unverified alarm, **40+ minutes or no response** depending on the false-alarm ordinance
  `[VERIFY locally]`.

---

## 5. Deliverables

Aim for a package a senior engineer would take to a client. **20–40 pages** plus schedules
and calculations. Quality over volume.

### A. Risk and concept
1. **Risk assessment** — asset register with consequence across all six categories; threat
   characterization; **a justified Design Basis Threat**; vulnerability assessment by adversary
   path; risk register with treatment decisions.
2. **Security zone plan** — zones 0–5 defined for the campus and each building, with the
   transition control and the four boundary questions answered at every boundary.
3. **Site security concept narrative** — 2–3 pages, written for the client's executive team.
4. **Basis of Design** — assumptions, exclusions, standards applied, and every place you made
   a judgment call.

### B. Design
5. **Perimeter design** — fencing, HVM/anti-ram, standoff, gates, vehicle screening,
   pedestrian screening, PIDS, lighting, clear zones. Address the utility easement, the rail
   embankment, and the drainage easement explicitly.
6. **Video design** — camera locations, types, lenses, mounting, with a **coverage analysis**
   and per-camera pixel-density target tied to the operational task.
7. **Access control design** — reader locations, credential strategy, controller topology,
   anti-passback and vestibule strategy, tenant cage access model, elevator/turnstile strategy.
8. **Door narratives / sequences of operation** — full SOOs for at least **six representative
   door types**, each covering normal, denied, forced, held, egress, network loss, power loss,
   fire alarm, and controller failure.
9. **Intrusion detection design** — sensor selection with stated Pd/nuisance reasoning, zoning,
   arming logic, supervision.
10. **Intercom / communications** — call stations, masters, SIP integration, dispatch workflow.
11. **Network architecture** — VLANs, segmentation, switch topology, uplinks, fiber, MDF/IDF
    locations, redundancy, and the **IT/security interface agreement**.
12. **Cybersecurity plan** — threat model for the VMS/PACS, hardening baseline, segmentation,
    vendor/remote access, credential and certificate lifecycle, logging, **evidence integrity
    and chain of custody**, backup and DR.

### C. Engineering
13. **Calculations** — bandwidth, storage, retention (with ranges and stated assumptions),
    PoE budgets per switch, voltage drop for representative runs, battery/UPS sizing, rack
    units, port counts, spare capacity, growth factor.
14. **Device schedule** — using the data model in `16_Automation/data_model/`. It must pass
    `validate.py` at CD phase.
15. **Cable schedule**, **switch-port schedule**, **IP plan**.
16. **Rack elevations** and head-end room requirements including power, cooling, and weight.
17. **Riser diagram** and system block diagrams.

### D. Documentation and delivery
18. **Division 28 outline specification** — section list with scope statements; one section
    developed in full (Part 1 / 2 / 3).
19. **Drawings or markups** — at minimum a site security plan and one building device plan.
    Hand sketches on the provided plan geometry are acceptable; the reasoning is what's graded.
20. **Equipment selection methodology** — your weighted-criteria process, not a product list.
21. **Commissioning plan + test sheets** — executable procedures traced to requirements.
22. **Operations considerations** — SOC design, alarm volume analysis vs. staffing, SOPs,
    tenant escort model, badge lifecycle.
23. **Lifecycle and maintenance plan** — PM schedule, spares, firmware policy, refresh cycle.
24. **Requirements Traceability Matrix** — every requirement → design element → drawing →
    spec → test.
25. **Design review checklist** — self-applied, with your findings on your own package.

---

## 6. The deliberate ambiguities

Real projects are ambiguous. **These are not oversights — they are the exam.** For each:
state your assumption, justify it, note what would change your answer, and where appropriate
write the RFI you would send.

1. **"Anti-ram protection at vehicle approaches."** Which threat vehicle? What speed? What
   penetration rating? Where does the standoff requirement come from? The parent-company
   standard doesn't say. What do you do?
2. **The utility easement crosses the southwest corner** and you cannot fence or build in it.
   How do you secure a perimeter with a 60-ft hole in it?
3. **The rail embankment overlooks the site by 12 ft** and trains sometimes stop. Is this a
   threat? To what? What, if anything, do you do — and what would be an overreaction?
4. **Tenant cage access tiers.** Some tenants get unescorted access, some escorted. The
   client hasn't defined the tiers. Propose a model, and identify the *contractual* question
   you can't answer as an engineer.
5. **Phase 2 is shell-only.** How much infrastructure do you build in Phase 1? What does it
   cost to defer versus to strand? Where do you put the head-end so Phase 2 doesn't require
   rework?
6. **The fire department required the southwest emergency gate.** It is a hole in your
   perimeter. How do you secure it without impeding emergency access? What do you propose,
   and who do you have to talk to?
7. **The client wants tours through data hall perimeters.** This conflicts with tenant
   contractual obligations. Surface the conflict; propose a design that accommodates both.
8. **Retention period is unstated.** Different tenants will want different things. What do
   you assume, what does it cost, and how do you frame the decision?
9. **Nobody has told you who owns the security network** — the client's IT, a managed
   provider, or the security integrator. Ask the question, and design so the answer can change.
10. **The roof.** DH-1's roof has an exterior caged ladder, substantial mechanical equipment,
    and penetrations into the data halls. Nobody mentioned it. It is one of the most
    significant vulnerabilities on the site.
11. **The badging system will hold tenant personnel data across 14 competing companies.**
    Who can see what? This is a design requirement disguised as an administrative detail.
12. **Alarm volume.** Compute what your design will generate. Compare it to three officers
    per shift. If it doesn't fit, your design is wrong — fix it before you submit.

---

## 7. What separates a good submission from a great one

A **good** submission covers all 25 deliverables competently.

A **great** submission additionally:

- **Develops a DBT and designs to it**, rather than designing to a device checklist.
- **Runs timely-detection analysis on the weakest paths**, not the designed ones — and states
  honestly which paths the system interrupts and which it only documents.
- Identifies that **the highest-consequence attack doesn't require entering a data hall** —
  it requires reaching the utility building, the fuel, or the fiber entrance.
- Notices the **insider/contractor path** is the one that actually happened to the competitor,
  and designs specifically against it (escort enforcement, contractor badge lifecycle, audit
  cadence) rather than adding perimeter hardware.
- Treats the **roof** as a zone boundary.
- Checks **alarm volume against operator capacity** and adjusts the design accordingly.
- Handles the **tour vs. tenant-contract conflict** without pretending it isn't one.
- States what it would cost to be wrong about each major assumption.
- Contains a **residual risk statement an executive could actually act on.**
- Is honest about what the design does *not* do.

---

## 8. Suggested schedule (4 weeks)

| Week | Focus | Output |
|---|---|---|
| 1 | Risk, DBT, zones, concept, BoD | Deliverables 1–4 |
| 2 | Perimeter, video, access control, doors, intrusion, intercom | 5–10 |
| 3 | Network, cyber, all calculations, schedules, racks, riser | 11–17 |
| 4 | Spec, drawings, commissioning, operations, lifecycle, RTM, self-review | 18–25 |

---

## 9. Before you open the reference solution

1. **Submit your own package.** Date it.
2. Apply your own design review checklist to it and log your findings.
3. **Then** read the reference solution.
4. Write a gap analysis: what it caught that you didn't, and — more importantly — **why you
   missed it**. Pattern-match your misses against the ones from Projects 1–7. The repeated
   ones are your real weaknesses.
5. Those become your months 13–18.
