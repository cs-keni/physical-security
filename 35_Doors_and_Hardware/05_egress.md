# 05 — Egress, Delayed Egress, and Controlled Egress

> ⚠️ **Read this before the lesson.** Everything in this lesson is governed by adopted codes
> that vary by jurisdiction, by adopted edition, and by occupancy, and that are interpreted by
> a local Authority Having Jurisdiction. **No number in this lesson is a compliance
> determination.** Every numeric or prescriptive claim is tagged `[CODE][VERIFY]` and your job
> is to read the adopted text and confirm with the AHJ. This lesson teaches you the *shape* of
> the requirements, the vocabulary, the questions to ask, and the engineering judgment — so
> that when you open the code you know what you're looking at.
>
> Getting this wrong kills people. Not metaphorically. The history of this body of code is a
> list of fires where the exits were locked.

## Learning objectives

- State the free egress principle and explain what "a single motion, without special knowledge
  or effort" is protecting against.
- Name the three components of a means of egress and locate an opening within it.
- Describe the special locking arrangements that exist — delayed egress, controlled egress,
  sensor-release / electromagnetically locked egress, stairway re-entry, elevator lobby locking
  — and the *class* of conditions each one attaches.
- Explain why occupancy classification and occupant load determine the answer before any
  security consideration enters.
- Respond correctly and usefully when a client asks you to lock an exit.
- Write a design narrative that documents the code path for a locking arrangement.

---

## ELI5

The rule that everything else hangs off:

> **A person inside a building must be able to get out, without a key, without knowing a
> secret, without needing a tool, and in one motion — always.**

"One motion" means you push the bar or turn the lever *once* and you are moving. Not: unlock
the deadbolt, then turn the knob. Not: find the button. Not: know that you have to lift and
pull.

Security wants doors locked. Life safety wants people out. **Life safety wins.** Not as a
value statement — as a matter of law and of what an engineer is allowed to sign.

There are a few narrow, heavily-conditioned arrangements that let a door in the egress path be
locked in some way. They exist, they are legitimate, and they are conditioned on things like
occupancy type, sprinklers, fire alarm interconnection, signage, timers, and AHJ approval. They
are not a general-purpose escape hatch from the rule.

---

## The means of egress

Egress is a **path**, not a door. Codes describe it in three parts:

```
   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
   │ EXIT ACCESS  │ →  │     EXIT     │ →  │ EXIT DISCHARGE│
   └──────────────┘    └──────────────┘    └──────────────┘
   From wherever you    The protected      From the exit to
   are, to the exit.    portion — the      the public way.
   Corridors, aisles,   enclosed stair,    Lobby run-out,
   the office you're    the exterior door. yard, sidewalk.
   standing in.

   Every door you touch is somewhere on this path — or it isn't on it at all,
   which is the first thing to determine.
```

The whole path is regulated: width, travel distance, number of exits, separation between
exits, illumination, signage, and — your part — **what may be done to the doors.**
`[CODE][VERIFY]`

**Your first question at any opening is therefore not "how do we lock it" but "where is this
door on the means of egress, and what is the occupancy?"** Everything downstream depends on
those two answers, and they are determined by the architect and the code, not by you.

---

## The free egress principle

Common formulations you will encounter in code text `[CODE][VERIFY exact language in the
adopted edition]`:

- Egress doors shall be **readily openable from the egress side without the use of a key, tool,
  special knowledge, or effort**.
- Releasing the latch shall require **not more than one releasing operation** (with narrowly
  defined exceptions).
- Operable hardware shall not require **tight grasping, tight pinching, or twisting of the
  wrist** — an accessibility requirement that converges with the egress requirement and rules
  out, among other things, ordinary round knobs in many applications.
- Hardware shall be mounted within a defined height range above the floor.

**What each of these is protecting against, concretely:**

| Requirement | The failure it prevents |
|---|---|
| No key | People die at locked doors holding no key. This is the entire origin of the body of code. |
| No special knowledge | In smoke, at night, in panic, a visitor cannot be expected to know the trick. |
| One motion | Under stress, fine motor sequences fail. Two-step operations become zero-step failures. |
| No tight grasping / twisting | People with limited hand function, people carrying someone, people with burns |
| Mounting height | Reachable by a person crawling under smoke, and by a wheelchair user |

> 🧠 **Note that every one of those is about a human being under conditions where they are not
> at their best.** The code is not written for the calm, informed, able-bodied adult who read
> the sign. That is the design posture to carry into every egress decision you make: *does this
> work for someone who is panicking, unfamiliar, injured, or being carried?*

### Panic hardware

Where occupant load or occupancy requires it, egress doors must have **panic hardware** (or
**fire exit hardware** on rated openings): a bar spanning most of the door width that releases
the latch when pushed in the direction of travel. `[CODE][VERIFY — the thresholds that trigger
this requirement are occupancy- and occupant-load-based; look them up.]`

The reason for the bar shape rather than a lever: a crowd pressed against the door releases it
by the act of being pressed against it. It works when nobody is operating it deliberately.

---

## The special locking arrangements

These are the legitimate exceptions. Each attaches to a defined set of conditions. **Learn what
each one is for and what class of conditions it carries; look up every parameter.**

### 1. Delayed egress

**What it does:** pushing the device initiates an irreversible timer. An alarm sounds locally.
When the timer expires, the door unlocks and stays unlocked until manually reset.

**The security value:** it converts "someone walked out the back with the merchandise" from an
undetected event into a loud, delayed, recorded one. It is the *only* arrangement that gives
you meaningful adversary delay on an egress door, and even then it's a short delay whose real
function is detection and deterrence, not barrier.

**The shape of the conditions** `[CODE][VERIFY every one of these]`:

- Permitted only in **certain occupancies**, and typically excluded from assembly, educational,
  and high-hazard occupancies.
- The building generally must be **sprinklered or have an automatic fire detection system**.
- The delay period is commonly cited as **15 seconds**, with **30 seconds where specifically
  approved by the AHJ**. `[CODE][VERIFY — these are the figures usually discussed; confirm
  against the adopted text, and never state them to a client as settled without the citation.]`
- The lock must release on **fire alarm activation**, on **sprinkler activation**, and on **loss
  of power** to the locking device.
- **Signage** is required at the door, with prescribed wording and placement, telling the
  occupant to push and hold.
- There is usually a limit on the **number of delayed egress doors** in a single egress path.
- **Periodic testing** is required and it is an ongoing owner obligation, not a one-time
  commissioning item.

```
   DELAYED EGRESS — the occupant experience

   push bar ──► local alarm sounds immediately
                │
                ├─ signage says PUSH UNTIL ALARM SOUNDS, DOOR CAN BE OPENED IN 15 SECONDS
                │  [CODE][VERIFY exact required wording]
                │
                └─ timer runs (irreversible — releasing the bar does not reset it)
                       │
                       ▼
                   door unlocks, stays unlocked until manual reset

   Bypassed immediately and completely by:  fire alarm │ sprinkler flow │ power loss
```

> ⚠️ **Delayed egress is not "a locked exit you're allowed to have."** It is a 15-second,
> loudly-announced, code-conditioned, self-defeating-on-alarm arrangement with an ongoing
> testing obligation. Clients hear "delayed egress" and think "locked." Correct that in the
> first meeting.

### 2. Controlled egress

**What it does:** permits doors in the egress path to be locked in specific care settings where
the occupants' own safety depends on them not leaving unsupervised — secure psychiatric units,
memory care, nurseries.

**The shape of the conditions** `[CODE][VERIFY]`: restricted to defined occupancies and defined
uses within them; staff must carry the means of release; release on fire alarm and sprinkler
activation; a clinical-needs justification; and AHJ acceptance.

**Your posture:** this is a *clinical* determination wearing an engineering costume. You
implement it; you do not propose it. If a client outside those occupancies asks for controlled
egress, the answer is no, and the conversation moves to what they're actually worried about.

### 3. Sensor-release of electrically locked egress doors

The arrangement that makes a magnetic lock on an egress door legitimate.

**The shape** `[CODE][VERIFY]`: a sensor on the egress side detects an approaching occupant and
unlocks the door; a **manual release device** in the egress path (a button, typically marked
and adjacent to the door) that on operation directly interrupts power to the lock, independent
of any controller, and keeps it interrupted until reset; automatic release on **power loss** and
on **fire alarm / sprinkler activation**; required **signage**.

This is the "entire additional subsystem" referenced in lesson 03. Now you can see its shape:
**sensor + manual release + power-loss release + fire-alarm release + signage**, all of which
exist solely to replace the mechanical linkage that a lever would have given you for free.

> 🧠 That framing is the argument to make when someone wants a mag lock for convenience:
> *"We're adding five components and a permanent testing obligation to replace one lever. What
> is it about this opening that makes a lever impossible?"* Sometimes the answer is good — an
> all-glass door genuinely has nowhere to put a lock. Often it isn't.

### 4. Stairway re-entry

Stair doors locked against re-entry from the stair side create the failure where an occupant
enters the stair, finds smoke below, and cannot get back onto a floor. Codes address this with
requirements for automatic unlocking on fire alarm, for a minimum number of re-entry floors, or
for two-way communication — the specifics vary. `[CODE][VERIFY]`

**For you this is a fail-state and a fire-alarm-interface question** (lesson 04) attached to
every stair door in the project, and it is one of the most commonly missed items on a security
drawing set.

### 5. Elevator lobby locking

Where elevator lobbies are enclosed, doors from the lobby to the exit access can be subject to
their own locking provisions, including release on fire alarm. `[CODE][VERIFY]`

---

## When the client asks you to lock an exit

They will. Usually for a real reason: theft through a back door, tailgating at a service exit,
an unmonitored stair discharge. **Do not lead with "you can't."** Lead with the problem.

**The conversation, in order:**

1. **Name the actual risk.** "You're losing inventory through the east exit." Not "you want to
   lock a door."
2. **State the constraint plainly, once.** "That door is in the means of egress, so it has to
   open from the inside in one motion. That's not a preference and I can't design around it."
3. **Offer the alternatives you already prepared.** This is the part that makes you useful:

| What they want | What you can actually do |
|---|---|
| Stop people leaving through it | **Alarm it.** Local sounder + monitored contact + alarm-linked camera. Detection instead of a barrier — see `../01_Foundations/03_functional_chain.md`. |
| Stop people leaving *with something* | Delayed egress, **if** the occupancy and conditions permit `[CODE][VERIFY]` |
| Stop people entering through it | Lock it from the **outside**. Free egress is one-directional; nothing prevents you from securing entry. This is the answer far more often than people realize. |
| Stop the door being propped | Prop alarm (door-held-open timer), closer adjustment, camera, and a conversation with operations |
| Protect the asset | **Move the asset.** Delay and detection at the asset rather than at the exit. Frequently cheapest and always legal. |
| Know who left and when | REX event logging, camera at the door, reader on the outside for re-entry |

4. **Write it down.** The recommendation, the constraint, and the alternative selected, in the
design narrative.

> 🧠 **The senior insight is that "free egress" is a *one-directional* constraint and most
> clients don't know that.** The door must open from the inside. It does not have to open from
> the outside. An enormous fraction of "we need to lock the exit" requests are satisfied
> completely by securing the exterior side and alarming the interior side, and the client walks
> away happy having gotten what they actually needed.

---

## The engineer's process

```
   1. Determine the OCCUPANCY CLASSIFICATION.        (architect / code consultant)
   2. Determine the ADOPTED CODES and EDITIONS.      (jurisdiction — verify, don't assume)
   3. Determine the MEANS OF EGRESS.                 (architect's life safety plan)
   4. Locate your opening on that path.
   5. NOW consider security. Choose an arrangement that the code text permits
      for that occupancy on that path.
   6. Confirm with the AHJ, early, and DOCUMENT the conversation.
   7. Write the design narrative with the citation.
   8. Commission it by TEST — actually pull the alarm and watch the doors.
```

Steps 1–3 are not yours, but you must have them **in writing** before step 5. Designing
locking arrangements against an assumed occupancy is how projects get expensive at inspection.

### On the AHJ

The Authority Having Jurisdiction interprets and enforces the code, and their interpretation
governs on their project. Two adjacent jurisdictions with the same adopted code can reach
different conclusions on the same arrangement.

**Practices worth adopting from day one:**

- Engage them **early**, before the design is locked, when a change is still cheap.
- Bring a **specific proposal** with the code sections you're designing to, not an open
  question. "We're proposing delayed egress at these three doors under section X; here's the
  fire alarm interface and the signage" gets a decision. "What can we do here?" gets a shrug.
- **Write down what they said**, send it back to them in an email, and keep the reply. A verbal
  approval from a person who has since changed jobs is worth nothing at inspection.
- Never quote an AHJ decision from another project as precedent on this one.

---

## Commissioning: this is where egress designs actually fail

A correct design that was installed wrong is a wrong design. Every egress locking arrangement
needs a **physical test**, and the tests are simple:

| Test | Method | Pass criterion |
|---|---|---|
| Free egress | Walk up from the egress side with no credential and no knowledge; operate the hardware once | Door opens |
| Fire alarm release | Activate the fire alarm system | Every affected door releases, and stays released |
| Power loss release | Interrupt power to the locking device | Fail-safe doors release |
| Manual release (sensor-release arrangement) | Press the release button | Power interrupted; door releases; stays released until reset |
| Delayed egress timing | Push and hold; time it | Alarm immediate, release at the specified interval, irreversible |
| Sensor coverage | Approach from every realistic direction, at every realistic speed, including slowly | Unlocks every time |
| Signage | Look at it | Present, correct wording, correct location `[CODE][VERIFY]` |

> ⚠️ **Sensor coverage is the one that fails in service.** A REX or release sensor aimed for a
> person walking briskly at chest height will miss a person in a wheelchair, a person crawling
> under smoke, and a person approaching from an oblique angle. Test it from the awkward
> directions and at the awkward speeds, because that is who the arrangement exists to protect.
> See `../18_Commissioning/`.

---

## Design tradeoffs

| Tradeoff | The tension | How to resolve |
|---|---|---|
| Lock the exit vs. alarm the exit | Locking is what's asked for; alarming is what's permitted | Alarm + monitor + camera. Detection replaces the barrier. |
| Delayed egress vs. plain alarm | Delayed egress adds real (short) delay and a strong deterrent; adds code conditions, signage, and an ongoing testing obligation | Use it where the loss is real and the occupancy permits; otherwise alarm alone |
| Mag lock + sensor release vs. mechanical-egress hardware | Mag is easier to install; adds five components and a permanent life-safety obligation | Mechanical egress unless the opening genuinely cannot take a lock |
| Securing entry vs. securing egress | Securing entry is unconstrained; securing egress is heavily constrained | Ask which one the client actually needs — usually entry |
| Early AHJ engagement vs. schedule | Engagement costs weeks now | It costs months later. Engage early. |

---

## Common mistakes

⚠️ **Chained, padlocked, or deadbolted exits.** This is the failure mode that generated the
code. It still happens, usually added by an operator after handover because of a theft problem.
**If you see it on a site walk, report it in writing the same day.**

⚠️ **A second releasing operation.** A deadbolt above the lever, or a thumbturn plus a lever, is
two motions. `[CODE][VERIFY]`

⚠️ **Assuming delayed egress is permitted** without checking occupancy, sprinkler status, and
the count of such doors on the path.

⚠️ **No signage**, or signage with the wrong wording or in the wrong place.

⚠️ **No fire alarm interface**, or one implemented in software (lesson 04).

⚠️ **Designing against an assumed occupancy classification.**

⚠️ **Treating an AHJ conversation as done because it went well.** Get it in writing.

⚠️ **Commissioning by inspection instead of by test.** "It looks right" is not a test.

⚠️ **Forgetting the ongoing obligation.** Delayed egress and sensor-release arrangements have
recurring testing requirements that outlive your involvement. Put them in the O&M handover
(`../19_Operations/`).

⚠️ **Quoting a number from memory.** Including any number in this lesson.

---

## Junior vs. Senior

**Junior:** knows free egress is non-negotiable; can name the special locking arrangements and
knows they're conditioned; knows to look up the code rather than recall it; knows the fire alarm
release must be hardwired.

**Senior:** determines occupancy and the means of egress before considering any security option;
knows free egress is one-directional and reframes most "lock the exit" requests into securing
entry plus alarming egress; walks into the client meeting with the alternatives already priced;
engages the AHJ early with a specific proposal and documents the answer; commissions by test
including the awkward approaches; writes a design narrative that lets the next engineer see the
reasoning and the citation; and reports a chained exit the day they see it, regardless of whose
scope it is.

---

## 🔧 Field exercise

In your building, find the nearest exit to where you sit and follow the full means of egress to
the public way. At every door on that path, record:

1. Can you open it from the egress side in one motion, with no key and no knowledge? (Try it.)
2. What hardware is on it — lever, panic bar, fire exit hardware?
3. Is there any electrified locking? If so, can you find the release button and the signage?
4. Is anything propped, chained, blocked, or obstructed?

Then write one paragraph: if the alarm sounded right now and the lights were out, would this
path work for a person who had never been in the building?

**If you find a chained or blocked exit, report it to your facilities team in writing today.**
That is not an exercise.

---

## Exercises

**E5.1** For each, state whether the arrangement is plausibly permitted, what conditions you
would need to verify, and what you would propose if it isn't:
- (a) Delayed egress on the two rear exits of a sprinklered retail store.
- (b) Delayed egress on the exit doors of a high school gymnasium.
- (c) A magnetic lock with sensor release on the main lobby exit of an office building.
- (d) A deadbolt added above the lever on a stockroom door that discharges to the exterior.
- (e) Locked doors on a memory care unit in a nursing facility.

**E5.2** A retail client is losing $60k/year to theft through a rear exit that discharges to an
alley. They want it locked. Write the recommendation: name the risk, state the constraint,
present three options with what each does and does not solve, and make a recommendation with a
reason. Under 400 words.

**E5.3** You are reviewing a drawing set for a sprinklered warehouse. It shows magnetic locks
on four exterior egress doors with card readers on the outside and REX motion sensors on the
inside. No release buttons, no signage, and the fire alarm interface is shown as "by ACS
integration." List every deficiency and write the review comment for each.

**E5.4** Explain, in under 150 words to a store manager who has just told you they lock the back
door during the evening shift "because it's just us," why they need to stop today. Be direct
and do not lecture.

**E5.5** Write the design narrative paragraph documenting a delayed egress installation at three
doors: what the arrangement is, what conditions make it permissible, what it interfaces with,
what signage is provided, and what the ongoing obligation is. Leave the code citations as
explicit `[VERIFY]` placeholders showing what would need to be filled in.

**E5.6** A door is on the means of egress from a data hall. The client wants the highest
possible security on it. Describe what you can and cannot do, and where you would put the
security that the door cannot provide.

> Solutions: [`_solutions/05_egress_solutions.md`](_solutions/05_egress_solutions.md)

---

## Retrieval check

1. State the free egress principle. What does "one motion" protect against?
2. Name the three components of a means of egress.
3. Name five special locking arrangements and the class of conditions each carries.
4. Why is free egress a one-directional constraint, and what does that let you do?
5. What three events must release a delayed egress lock?
6. What components make up a compliant sensor-release arrangement for an electrically locked
   egress door?
7. What are the two things you must have in writing before choosing a locking arrangement?
8. Why must sensor coverage be tested from awkward directions and at slow speeds?

---

## References

- Applicable **building code** and **life safety code**, means of egress chapters — door
  operation, locking and latching, panic and fire exit hardware, delayed egress, controlled
  egress, sensor release, stairway re-entry, elevator lobby locking. **This lesson is a map of
  what to read; the code text is the authority.** `[CODE][VERIFY adopted edition per
  jurisdiction]`
- Accessibility standards — operable hardware requirements, mounting heights, opening force,
  maneuvering clearances. `[CODE][VERIFY]`
- NFPA 72 — fire alarm interface and releasing arrangements. `[STANDARD][VERIFY]`
- NFPA 80 — fire door assemblies and their inspection/testing obligations. `[STANDARD][VERIFY]`
- The local AHJ — the actual authority on your project. Engage early, in writing.
- `../10_Codes_Standards/` — how to determine the adopted edition for a jurisdiction and how to
  cite it.
- `../18_Commissioning/` — test procedures.

**Next:** 06 — Electrified Hardware and Power Transfer *(not yet written — see
[`../COURSE_PROGRESS.md`](../COURSE_PROGRESS.md))*
