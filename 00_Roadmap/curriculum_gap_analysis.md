# Curriculum Gap Analysis

You asked me to identify what was missing from your requested curriculum and improve it.
This document records what I added, what I restructured, and why. It is also the honest
record of where this curriculum's authority ends.

---

## Part 1 — Significant topics missing from the original request

These are added to the curriculum. Ordered by how much their absence would hurt you.

### 1.1 Lighting design as a first-class engineering discipline ⭐ highest impact
Your outline mentions lighting three times, always as a bullet inside another topic. In
practice, **lighting is the single largest determinant of whether a camera system works at
night**, and it is the most commonly under-engineered element in security design. A $2,000
camera in a badly lit dock is worse than a $600 camera in a well-lit one.

Added to `06_Perimeter_Security/` and `03_Video_Surveillance/`: illuminance (lux) vs
luminance, uniformity ratios (avg:min, max:min), glare and veiling luminance, color
rendering index and its effect on suspect description, IES-style recommended illuminance
concepts `[GUIDELINE]`, light trespass, dark-sky considerations, IR vs white light vs
thermal decision logic, and the interaction between lighting uniformity and WDR performance.

### 1.2 Environmental and site conditions engineering
Beyond the IP/IK/NEMA ratings you listed: sun angle and solar loading on camera views
(east/west-facing cameras are blinded twice a day, predictably, and you can calculate it),
precipitation and fog attenuation, wind loading on pole-mounted devices, thermal cycling and
condensation inside enclosures, salt fog in coastal sites, dust in industrial sites, and
vibration from rail/HVAC. Added to `38_Products_and_Ratings/`.

### 1.3 Cost estimating and value engineering
Your outline mentions cost estimation once. It is a large part of a consulting engineer's
actual value. Added to `37_Project_Management/`: order-of-magnitude vs parametric vs
detailed estimates, device-count-driven parametric models, the labor/material split in
low-voltage work, contingency by design phase, the difference between capital cost and
total cost of ownership, and how to run a value-engineering exercise without destroying the
design intent. Includes what to do when the owner cuts 30% of the budget after DD.

### 1.4 Existing-conditions and retrofit engineering
Your outline assumes new construction throughout. Most real work is retrofit, and retrofit
is *harder*. Added to `17_Construction_Documents/`: existing-conditions surveys, working
without accurate as-builts, asbestos/lead awareness and why you don't drill first, pathway
constraints in occupied buildings, phasing and maintaining security during construction
(the "temporary security measures" plan nobody remembers until the doors come off), cutover
planning, legacy system integration and head-end replacement strategy, and how to write a
scope when you genuinely don't know what's in the ceiling.

### 1.5 Key management and mechanical security
Electronic access control gets all the attention; **the mechanical key system is usually the
actual weakest link**, and it is frequently nobody's scope. Added to `35_Doors_and_Hardware/`:
master key system hierarchy (GGM/GM/M/change keys), keyway control and patented keyways,
key records and audits, restricted vs unrestricted, core types (SFIC/LFIC), rekeying strategy,
construction cores, and the classic finding that the electronic system is perfect and there
are 400 unaccounted grand-master keys.

### 1.6 Safes, vaults, secure rooms, and physical hardening
Not mentioned at all. Added to `06_Perimeter_Security/` and a new section in
`20_Data_Center/`: UL-rated safes and their meaning `[STANDARD]`, vault construction,
wall/ceiling/floor penetration resistance (the classic "the walls stop at the ceiling grid"
vulnerability), slab-to-slab construction, ballistic and forced-entry ratings, secure mesh,
cage construction in colocation, and how to specify a secure room without specifying a bank
vault.

### 1.7 Screening technology
Not mentioned. Added to `06_Perimeter_Security/`: walk-through and hand-held metal detection,
X-ray screening, package screening, mail handling, and — importantly — the operational and
throughput math that determines whether a screening design is actually usable at shift change.

### 1.8 Weapons detection and emerging sensing
Brief treatment added: the current generation of "AI weapons detection" portals, what they
actually claim, how to evaluate vendor claims skeptically, and the false-positive throughput
problem. Framed as *how to evaluate*, not *what to buy*.

### 1.9 Drone / UAS awareness
Increasingly asked about for data centers and critical infrastructure. Added as an awareness
topic in `20_Data_Center/`: what the threat actually is (mostly surveillance and disruption,
not payload), why most "counter-drone" measures are legally restricted in the US, detection
vs mitigation, and — the practical engineering answer — designing for overhead observation
(roof markings, equipment shielding, sensitive-area siting). Explicitly flagged as an area
requiring legal counsel, not engineering judgment alone.

### 1.10 Insider threat and its physical design implications
Your outline is heavily oriented toward external adversaries. The insider is the higher-
probability threat for most facilities, and the countermeasures are different: two-person
integrity, separation of duties, audit-driven detection rather than barrier-driven
prevention, escort requirements, and material control. Added to `02_Risk_Assessment/` and
`19_Operations/`.

### 1.11 Workplace violence and active assailant design considerations
A significant driver of security spending that your outline omits. Added to
`21_Facility_Case_Studies/` (schools, hospitals, offices): the tension between lockdown
capability and egress law, run/hide/fight design implications, secure-in-place areas, mass
notification integration, ballistic-resistant reception glazing, and the fact that most
requests for "active shooter security" are best answered with better egress, better
notification, and better operations than with hardware.

### 1.12 Emergency and business continuity integration
Added to `19_Operations/`: how security systems support (and are supported by) emergency
operations plans, evacuation and accountability (mustering via access control), continuity
of operations, and the security system's role during and after an incident.

### 1.13 Coordination with mechanical, plumbing, and structural
Your outline covers architects and EEs. Security fails constantly at the mechanical
interface: ductwork blocking camera views (a *classic*), rooftop equipment as a climbing
aid, ceiling plenum access above secure walls, structural capacity for barrier foundations,
sprinkler and conduit conflicts in corridors, and the loading-dock leveler that makes your
door contact impossible. Added to `17_Construction_Documents/`.

### 1.14 Signage, wayfinding, and the legal function of signs
Small topic, real consequences: notice requirements for surveillance in some jurisdictions
`[VERIFY]`, trespass notice, restricted area marking, emergency exit signage interaction with
delayed egress (specific signage text is code-prescribed `[CODE][VERIFY]`), and signage as a
deterrent instrument. Added to `36_Human_Factors_Privacy_Ethics/`.

### 1.15 Sustainability, energy, and the mag-lock power question
Increasingly a client requirement. Added to `34_Electrical_Power/`: standby power draw of
security systems (a mag lock holds 24/7 forever; an electric strike doesn't), LEED/energy
code implications of continuous loads, and heat load in head-end rooms as an input to the
mechanical design.

### 1.16 Procurement models and delivery methods
You listed "bid/procurement" as one step. The *delivery method* changes your job completely.
Added to `37_Project_Management/`: design-bid-build vs design-build vs CM-at-risk vs IPD,
basis-of-design vs performance vs proprietary specification strategy, sole-source
justification, owner-furnished/contractor-installed (OFCI) vs contractor-furnished, and how
each affects what you must draw and specify.

### 1.17 Standards bodies and reference frameworks you didn't list
Added to `10_Codes_Standards/` as navigation targets `[VERIFY current editions]`: FEMA
risk-management series for buildings, DHS/CISA infrastructure security resources, the
Interagency Security Committee (ISC) standard for federal facilities, ASTM vehicle barrier
crash-rating standards, UL standards beyond 294 (including UL 1076, UL 2050 concepts, UL 437),
IEC/ISO 27001-adjacent physical controls, ANSI/BHMA hardware grading, NFPA 730/731
(security guideline documents, distinct from mandatory codes), ONVIF profiles specifically,
and SIA standards including OSDP.

### 1.18 Testing and measurement instruments
An engineer who can't measure can't verify. Added to `18_Commissioning/`: light meters,
multimeters, cable certifiers vs qualifiers vs verifiers, network test sets, PoE testers,
door force gauges (there are code-referenced maximum opening forces `[CODE][VERIFY]`), and
what a commissioning agent actually carries.

### 1.19 Warranty, service contracts, and lifecycle economics
Added to `19_Operations/`: warranty scope and duration, what "one-year warranty" excludes,
service-level agreements, spare parts strategy, firmware/software maintenance agreements,
end-of-life and end-of-support planning, and the refresh-cycle math that determines whether
your design is affordable to *own*.

### 1.20 Accessibility beyond the checkbox
You listed ADA once. It has real design consequences: reader mounting heights and reach
ranges `[CODE][VERIFY]`, door opening force limits, automatic operator interaction with
access control, turnstile accessible lanes, intercom accessibility for hearing/vision/mobility
impairment, and the fact that the accessible route is also an adversary's easiest route.
Expanded in `35_Doors_and_Hardware/` and `36_Human_Factors_Privacy_Ethics/`.

### 1.21 Audio: capability, legality, and utility
You mention audio recording only under privacy. Also worth engineering treatment: audio
detection (gunshot, aggression, glass break as an analytic), talk-down and its operational
effectiveness, intercom audio quality in noisy environments, and the sharply
jurisdiction-dependent legality of audio recording `[VERIFY — this is a legal question,
escalate it]`.

### 1.22 How to actually learn from manufacturers without becoming a vendor mouthpiece
Added to `38_Products_and_Ratings/`: how to read an A&E spec critically (they are marketing
documents shaped like engineering documents), how to detect a proprietary spec written to
exclude competitors, how to run a fair product evaluation with weighted criteria, how to
handle vendor lunch-and-learns, and the ethics of manufacturer relationships in a consulting
firm.

---

## Part 2 — Structural changes I made

| Change | Reason |
|---|---|
| Split **doors/hardware** into its own module (`35_`) rather than a subsection of access control | Door hardware is the #1 knowledge gap in junior security engineers and the #1 source of construction-phase conflict. It needs its own depth and its own field exercises. |
| Split **electrical/power** into its own module (`34_`) | Same reason. Power supply and battery sizing errors are extremely common and extremely visible. |
| Added **`32_Engineering_Math/`** as a separate module from `28_Calculators/` | The *lessons* (derivation, units, assumptions, problem sets) are pedagogically different from the *tools*. Separating them prevents you from using a calculator you don't understand. |
| Added **`33_Design_Review_QA/`** as a module, not an exercise type | Reviewing others' work is a distinct, teachable, career-critical skill. It gets its own flawed-package library. |
| Added **`36_`, `37_`, `38_`** for human factors/privacy, project management, and products/ratings | These were sections in your prompt with no home in your folder structure. |
| Moved the **Security Device Data Model** into `16_Automation/data_model/` | It's the schema that everything else in the automation track imports; it belongs with the code that uses it. |
| **Solutions live in `_solutions/` and `_answer_keys/` subfolders** | So you cannot spoil an exercise by scrolling. |
| **Lighting** promoted from a bullet to a substantial topic | See 1.1. |

---

## Part 3 — Where this curriculum's authority ends (read this)

I want to be explicit about the limits, because a study guide that oversells its own
reliability is worse than useless.

**1. Codes and standards.** I can teach you the *structure* of code requirements, the
reasoning behind them, and how to find and read the current text. I cannot be your code
reference. Every specific numeric requirement in this repo is tagged `[VERIFY]` and must be
confirmed against the edition your jurisdiction has adopted, plus local amendments, plus the
AHJ's interpretation. Code text is also copyrighted; this curriculum summarizes concepts and
does not reproduce it.

**2. ASIS certification specifics.** The ASIS website blocks automated retrieval, so the
domain weightings recorded in `22_APP/` and `23_PSP/` come from secondary sources and are
flagged accordingly. **Verify domains, weightings, eligibility, fees, and the reference
list against the official ASIS Certification Handbook before you build a study plan around
them.** Certification bodies revise domains on multi-year cycles.

**3. Products.** Any specific product mentioned is an example of a *category*, current as of
authoring, and will go end-of-life. Always pull the current datasheet.

**4. Legal questions.** Privacy law, recording law, biometric law, employee monitoring law,
and counter-drone law are jurisdiction-specific and change. This curriculum teaches you to
*recognize* when you've hit a legal question and escalate it. It does not answer it.

**5. Judgment cannot be transferred in text.** The reasoning frameworks here are real, and
the exercises are designed to build calibration. But calibration ultimately comes from
making decisions, seeing outcomes, and being corrected by people with more scars than you.
The decision journal in `how_to_use_this_academy.md` is the mechanism that turns your real
work into learning. Use it.

---

## Part 4 — What I deliberately did *not* add

- **Offensive techniques.** No lock picking beyond conceptual vulnerability awareness, no
  bypass methodology, no credential cloning procedure, no detection evasion. You will
  encounter these concepts professionally; when you do, the appropriate depth is "this class
  of attack exists, here is the countermeasure," which is what this curriculum provides.
- **Deep electrical engineering.** No semiconductor physics, no power systems analysis, no
  motor control. You asked me not to, and you're right not to need it.
- **Architectural design.** You need to *read* architecture fluently and coordinate with
  architects credibly. You do not need to design buildings.
- **Vendor certification content.** Manufacturer certifications (VMS/PACS platform certs)
  are valuable and employer-driven. They're noted in the roadmap but not taught here, because
  they go stale fast and are best learned on the vendor's current courseware.
