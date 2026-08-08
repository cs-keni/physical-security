# Module 35 — Doors and Hardware

> **Time:** ~8–12 hours over 2–3 weeks for lessons 01–05.
> **Prerequisite:** [`../01_Foundations/`](../01_Foundations/) — specifically the functional
> chain (`03`) and defense in depth (`04`).
> **Why this module is early:** the opening is where a security design becomes physical. It is
> the single highest-density knowledge gap for a junior physical security engineer, and it is
> the one place where a mistake can hurt somebody. Roadmap month 1 week 3 depends on lessons
> 01–02; Project 1 depends on 01–04.

## Lessons

| # | Lesson | Core question it answers |
|---|---|---|
| 01 | [Door Anatomy: Reading an Opening](01_door_anatomy.md) | What are all the parts, and which one is actually the weak point? |
| 02 | [Handing, Swing, and the Secure Side](02_handing_and_swing.md) | Which way does it face, and why does that determine everything I specify? |
| 03 | [Locking Hardware Families](03_locking_hardware_families.md) | What are my options for locking it electrically, and how do I choose? |
| 04 | [Fail Safe vs. Fail Secure](04_fail_safe_vs_fail_secure.md) | What should this door do when the power dies? |
| 05 | [Egress, Delayed Egress, and Controlled Egress](05_egress.md) | How does a person get out, and what am I actually allowed to do? |

**Not yet written** — see [`../COURSE_PROGRESS.md`](../COURSE_PROGRESS.md) for status:
06 Electrified Hardware and Power Transfer · 07 Fire-Rated Openings · 08 Key Management and
Mechanical Security · the 10-door field exercise · quiz and flashcards.

## Learning objectives for the module

By the end of lessons 01–05 you can:

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
8. Review a door schedule against a security drawing set and find the disagreements.

## How to study this module

Read 01 and 02 with a building around you. These two lessons are almost worthless read at a
desk and almost self-teaching read while standing in a corridor. Do the field exercises as you
go, not afterward.

Lessons 03 and 04 are the engineering core. Do the arithmetic in 03 by hand before touching
[`../28_Calculators/`](../28_Calculators/).

Lesson 05 is different in kind. It is a map of a body of code, not a set of facts to memorize.
The skill it teaches is knowing what to look up, what to ask the AHJ, and what to refuse. Read
it, then read the actual adopted code text for one jurisdiction alongside it.

## The load-bearing ideas

If you retain five things from this module:

1. **The unit of design is the opening, not the door** — and the weak point is usually the wall,
   the frame anchorage, the glazing, or the closer.
2. **Determine the egress mechanism first.** It eliminates most locking options before security
   enters the conversation.
3. **Fail secure does not trap anyone.** It is the correct default, and specifying fail safe
   everywhere "to be safe" builds a building that unlocks itself.
4. **Free egress is one-directional.** You may always secure the outside. This resolves most
   client requests that sound impossible.
5. **The most common access control "software problem" is a voltage problem.**

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
| [`../27_Labs/project_01_secure_one_door/BRIEF.md`](../27_Labs/project_01_secure_one_door/BRIEF.md) | The lab this module unblocks |

## Certification mapping

| Content | APP domain | PSP domain |
|---|---|---|
| Opening anatomy, hardware families | D2 Business Principles / D4 Security Operations | D2 Application, Design & Integration |
| Locking device selection, fail states | D4 Security Operations | D2 |
| Egress, codes, life safety | D1 Security Fundamentals | D2, D3 Implementation |
| Power and conductor sizing | — | D2, D3 |

> `[VERIFY]` Domain names and numbering per the current official ASIS Certification Handbook.
> These mappings are **provisional** — see [`../31_References/source_index.md`](../31_References/source_index.md)
> for the confidence note. The APP/PSP tracks are blocked on human verification.

---

> ⚠️ **A standing warning for this module.** Every code claim here is tagged `[CODE][VERIFY]`
> and every numeric threshold must be read out of the adopted text for your jurisdiction. This
> module teaches you the shape of the requirements and the questions to ask. It is not a
> compliance reference and must never be used as one.
