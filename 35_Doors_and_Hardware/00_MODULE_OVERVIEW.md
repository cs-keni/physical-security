# Module 35 — Doors and Hardware

> **Time:** ~16–22 hours over 4–6 weeks for the full module.
> **Prerequisite:** [`../01_Foundations/`](../01_Foundations/) — specifically the functional
> chain (`03`) and defense in depth (`04`).
> **Why this module is early:** the opening is where a security design becomes physical. It is
> the single highest-density knowledge gap for a junior physical security engineer, and it is
> the one place where a mistake can hurt somebody. Roadmap month 1 week 3 depends on lessons
> 01–02; Project 1 depends on 01–04; roadmap month 4 depends on 03–06.

## Lessons

| # | Lesson | Core question it answers |
|---|---|---|
| 01 | [Door Anatomy: Reading an Opening](01_door_anatomy.md) | What are all the parts, and which one is actually the weak point? |
| 02 | [Handing, Swing, and the Secure Side](02_handing_and_swing.md) | Which way does it face, and why does that determine everything I specify? |
| 03 | [Locking Hardware Families](03_locking_hardware_families.md) | What are my options for locking it electrically, and how do I choose? |
| 04 | [Fail Safe vs. Fail Secure](04_fail_safe_vs_fail_secure.md) | What should this door do when the power dies? |
| 05 | [Egress, Delayed Egress, and Controlled Egress](05_egress.md) | How does a person get out, and what am I actually allowed to do? |
| 06 | [Electrified Hardware and Power Transfer](06_electrified_hardware_power_transfer.md) | How does electricity get into a door that moves? |
| 07 | [Fire-Rated Openings](07_fire_rated_openings.md) | What may I not do to this door, and why is the damage invisible? |
| 08 | [Key Management and Mechanical Security](08_key_management.md) | Who can open all of this with a piece of metal? |

## Assessment and practice

- 🔧 [**The 10-door survey**](_exercises/10_door_survey.md) — the module capstone. Survey ten real
  openings and write a findings memo. Reference set in
  [`_solutions/10_door_survey_reference.md`](_solutions/10_door_survey_reference.md).
- [`../25_Quizzes/quiz_35_doors_hardware.md`](../25_Quizzes/quiz_35_doors_hardware.md) — 30
  questions. Take it cold, before reading, then again after.
- [`../26_Flashcards/35_doors_hardware.csv`](../26_Flashcards/35_doors_hardware.csv) — 77 cards,
  Anki-importable.
- `_solutions/` — worked answers for every lesson's exercises. Written alongside the lessons, so
  nothing dangles.

## Learning objectives for the module

By the end of this module you can:

1. Walk up to any commercial opening and describe it accurately — frame type, leaf, hinges,
   hardware, handing — in under a minute.
2. Identify the component that actually governs an opening's delay value, which is usually not
   the lock.
3. Determine handing correctly in the field and place a reader, REX, and position switch on the
   correct sides.
4. Select an electrified locking device from the opening's function, construction, rating, and
   egress requirement, and defend the choice.
5. Size a power supply and select a conductor for a set of electrified openings, and recognize
   the electrical signature of a "software" fault.
6. Specify a fail state for any opening, justify it, and get it onto the drawing where the
   contractor will read it.
7. Explain why free egress is non-negotiable and one-directional, and reframe a "lock the exit"
   request into something you can actually deliver.
8. Budget conductors for a power transfer and carry a voltage-drop calculation through it.
9. Specify around a fire-rated opening without voiding its label, and explain why the damage is
   invisible when you do.
10. Raise key control on a project, and explain why it bounds the value of the access control
    system.
11. Review a door schedule against a security drawing set and find the disagreements.

## How to study this module

Read 01 and 02 with a building around you. These two lessons are almost worthless read at a
desk and almost self-teaching read while standing in a corridor. Do the field exercises as you
go, not afterward.

Lessons 03, 04, and 06 are the engineering core. Do the arithmetic by hand before touching
[`../28_Calculators/`](../28_Calculators/). Lesson 06's worked example deliberately continues
lesson 03's — the same opening, and the answer changes once you account for the last six feet.

Lessons 05 and 07 are different in kind. They are maps of a body of code, not sets of facts to
memorize. The skill they teach is knowing what to look up, what to ask the AHJ, and what to
refuse. Read them, then read the actual adopted code text for one jurisdiction alongside them.

Lesson 08 is the one that will change how you talk to clients. Read it last, and notice that its
central recommendation costs the client almost nothing and reduces your own scope.

Finish with the [10-door survey](_exercises/10_door_survey.md). It is where the module becomes a
skill rather than a body of knowledge.

## The load-bearing ideas

If you retain seven things from this module:

1. **The unit of design is the opening, not the door** — and the weak point is usually the wall,
   the frame anchorage, the glazing, or the closer.
2. **Determine the egress mechanism first.** It eliminates most locking options before security
   enters the conversation.
3. **Fail secure does not trap anyone.** It is the correct default, and specifying fail safe
   everywhere "to be safe" builds a building that unlocks itself.
4. **Free egress is one-directional.** You may always secure the outside. This resolves most
   client requests that sound impossible.
5. **The most common access control "software problem" is a voltage problem** — and the circuit
   doesn't stop at the frame.
6. **A fire door must latch.** Every hardware restriction at a rated opening derives from that
   one requirement.
7. **The mechanical key is the real perimeter.** Every electrified lock has an override, and it
   generates no event.

## Cross-references

| Module | Relationship |
|---|---|
| [`../01_Foundations/`](../01_Foundations/) | Delay, detection, and balanced protection — the reasoning this module makes physical |
| [`../04_Access_Control/`](../04_Access_Control/) | Readers, controllers, credentials, offline behavior. Lesson 03 and 04 hand off directly. |
| [`../34_Electrical_Power/`](../34_Electrical_Power/) | Power supplies, batteries, voltage drop in depth |
| [`../28_Calculators/`](../28_Calculators/) | `psec.power` — supply sizing, battery, voltage drop |
| [`../10_Codes_Standards/`](../10_Codes_Standards/) | Determining and citing the adopted edition |
| [`../17_Construction_Documents/`](../17_Construction_Documents/) | Door schedules, hardware sets, spec section 08 71 00 |
| [`../18_Commissioning/`](../18_Commissioning/) | Testing egress arrangements by test, not by inspection |
| [`../19_Operations/`](../19_Operations/) | The recurring obligations lessons 05, 07, and 08 hand to the owner |
| [`../16_Automation/data_model/`](../16_Automation/data_model/) | The device register; lesson 06's missing-transfer check is a validation rule |
| [`../38_Products_and_Ratings/`](../38_Products_and_Ratings/) | Padlocks, hasps, cabinets, safes, vaults — where lesson 08 hands off |
| [`../27_Labs/project_01_secure_one_door/BRIEF.md`](../27_Labs/project_01_secure_one_door/BRIEF.md) | The lab this module unblocks |

## Certification mapping

| Content | APP domain | PSP domain |
|---|---|---|
| Opening anatomy, hardware families | D2 Business Principles / D4 Security Operations | D2 Application, Design & Integration |
| Locking device selection, fail states | D4 Security Operations | D2 |
| Egress, codes, life safety | D1 Security Fundamentals | D2, D3 Implementation |
| Power, conductor sizing, power transfer | — | D2, D3 |
| Fire-rated openings | D1 Security Fundamentals | D2, D3 |
| Key management and key control | D4 Security Operations | D2 |

> `[VERIFY]` Domain names and numbering per the current official ASIS Certification Handbook.
> These mappings are **provisional** — see [`../31_References/source_index.md`](../31_References/source_index.md)
> for the confidence note. The APP/PSP tracks are blocked on human verification.

---

> ⚠️ **A standing warning for this module.** Every code claim here is tagged `[CODE][VERIFY]`
> and every numeric threshold must be read out of the adopted text for your jurisdiction. This
> module teaches you the shape of the requirements and the questions to ask. It is not a
> compliance reference and must never be used as one.
