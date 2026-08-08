# Solutions — 05 Egress, Delayed Egress, and Controlled Egress

> ⚠️ These solutions demonstrate **reasoning**, not compliance determinations. Every conclusion
> below would require verification against the adopted code text and the AHJ on a real project.
> Where a solution says "plausibly permitted," that means *worth pursuing*, not *approved*.

---

## E5.1 — Permitted or not

**(a) Delayed egress on the two rear exits of a sprinklered retail store.**

**Plausibly permitted.** This is close to the canonical delayed egress application: mercantile
occupancy, sprinklered building, back-of-house exits with a real loss problem.

**Verify before proposing it:**
- Is the occupancy classification one the adopted code permits delayed egress in?
  `[CODE][VERIFY]`
- Sprinkler coverage or automatic fire detection throughout, as required.
- Occupant load — some thresholds change the answer.
- How many delayed egress doors are on any single egress path? There is usually a limit.
- The delay period permitted, and whether the longer period requires specific AHJ approval.
- Signage wording and location.
- Release on fire alarm, sprinkler flow, and power loss — all three, hardwired.
- Who will perform the recurring testing after handover, and does the owner know they own it?

**(b) Delayed egress on the exit doors of a high school gymnasium.**

**Almost certainly not permitted.** Two independent reasons, either of which is disqualifying:

1. **Assembly occupancy.** A gymnasium is an assembly space, and delayed egress is typically
   excluded from assembly occupancies. `[CODE][VERIFY]`
2. **Educational occupancy.** Also typically excluded.

Beyond the code text, apply the design posture from the lesson: a 15-second delay on an exit
serving a packed gymnasium is exactly the arrangement the body of code exists to prevent.
Don't propose it, don't price it, and don't let it into a drawing set.

**What to propose instead:** alarm the doors (local sounder, monitored contact, alarm-linked
camera), and if the problem is people entering rather than leaving, secure the exterior side —
which is unconstrained.

**(c) Magnetic lock with sensor release on the main lobby exit of an office building.**

**Plausibly permitted**, as a sensor-release arrangement — this is a common and legitimate
application. But it is *conditioned*, and the conditions are the whole answer:

- Sensor on the egress side that unlocks on approach, with coverage tested from oblique angles,
  at slow speeds, and at wheelchair height.
- A **manual release device** in the egress path that directly interrupts power to the lock,
  independent of the controller, and holds it interrupted until reset.
- Release on loss of power.
- Release on fire alarm and sprinkler activation, **hardwired**.
- Signage, with the prescribed wording and location.
- `[CODE][VERIFY]` all of the above against the adopted text, and confirm with the AHJ.

**The question worth asking anyway:** is this an all-glass entrance? If the lobby door can take
an electrified lockset or exit device, the mechanical-egress option removes this entire
subsystem. Check before accepting the mag as given.

**(d) A deadbolt added above the lever on a stockroom door that discharges to the exterior.**

**Not permitted, and this one is urgent.**

A deadbolt above a lever is a **second releasing operation** — the occupant must retract the
deadbolt *and then* turn the lever. That fails the one-motion requirement, and it fails the
"without special knowledge" requirement for anyone who doesn't know the deadbolt is there.
`[CODE][VERIFY]`

Note the framing of the question: the deadbolt was **added**. This is the single most common
egress violation in existing buildings, and it is almost always added after handover by an
operator with a real theft problem and no one to ask.

**Response:** report it in writing the day you see it. Then solve the actual problem — alarm the
door, secure the exterior side, add a camera, or move the stock. The operator is not the enemy
here; they had a problem and reached for the only tool they had.

**(e) Locked doors on a memory care unit in a nursing facility.**

**Plausibly permitted as controlled egress** — this is precisely the case controlled egress
exists for, where an occupant's own safety depends on not leaving unsupervised.

**But this is not your call to originate.** The conditions:
- The occupancy and the specific use must be among those the adopted code permits.
  `[CODE][VERIFY]`
- A **clinical needs** justification, from the clinical staff.
- Staff must carry the means of release, and there must be enough staff, always.
- Release on fire alarm and sprinkler activation.
- AHJ acceptance.

**Your role:** implement what the clinical determination and the code permit. You do not
propose controlled egress, and if someone outside a permitted occupancy asks for it, the answer
is no and the conversation moves to what they are actually worried about.

---

## E5.2 — The retail theft recommendation

Model answer (368 words):

> **Rear exit at [store] — loss through the alley door**
>
> **The problem.** The store is losing roughly $60,000 a year to merchandise leaving through the
> rear exit into the alley. The door is currently unmonitored: it opens freely from the inside,
> there is no alarm, and nothing records who used it or when.
>
> **The constraint.** That door is part of the store's means of egress. It has to open from the
> inside, in one motion, with no key and no special knowledge, whenever anyone is in the
> building. That is not a preference I can design around and it is not something I can get
> waived. Locking it is off the table.
>
> What is *not* constrained: the outside. Free egress runs one direction only. We can secure
> that door completely against entry from the alley, today, with no code implications at all.
>
> **Three options.**
>
> **1. Alarm and monitor it.** Local sounder at the door, monitored contact to the alarm system,
> and a camera covering the door and the alley approach with the alarm linked to the video.
> Anyone leaving through it announces themselves, on camera, with a timestamp.
> *Solves:* undetected departures, and most of the loss, because most of this is opportunistic
> and stops the first time it's loud. *Doesn't solve:* a determined person who accepts the
> noise. Lowest cost, fastest to install, no ongoing obligations.
>
> **2. Add delayed egress.** Pushing the bar sounds an alarm immediately and holds the door for
> 15 seconds before releasing. *Solves:* the same as option 1, plus it puts a real interval
> between the decision and the exit, which is usually enough for staff to arrive.
> *Doesn't solve:* anything option 1 doesn't, if nobody responds to the alarm.
> *Requires verification:* the occupancy, sprinkler coverage, and the number of such doors on
> the path — I need to confirm this is permitted here before pricing it. It also creates a
> recurring testing obligation the store will own.
>
> **3. Move the exposure.** Relocate high-value stock away from the rear of the store and put
> the security at the stock instead of at the exit. *Solves:* the actual loss, permanently, and
> it costs nothing but layout. *Doesn't solve:* the door being an uncontrolled opening.
>
> **Recommendation: option 1 now, and option 3 as a merchandising conversation.** Option 1
> captures most of the benefit at the lowest cost and installs in a day. Option 2 is worth
> pursuing only if option 1 doesn't move the number after a quarter, and I'd want the code
> verification done before we discuss it seriously. Option 3 is the one nobody proposes and it
> is frequently the cheapest thing on the list.

**What makes it work:** names the risk before the constraint, states the constraint once
without lecturing, immediately gives away the good news (you can secure the outside), presents
options with what each does *and doesn't* solve, and recommends the cheap thing first. Note
also that it does not pretend option 2 is available — it flags the verification.

---

## E5.3 — Warehouse drawing set review

Given: sprinklered warehouse, magnetic locks on four exterior egress doors, card readers
outside, REX motion sensors inside, no release buttons, no signage, FA interface "by ACS
integration."

**Deficiency 1 — No manual release device in the egress path.**
> **Review comment:** A magnetically locked door in the means of egress requires a manual
> release device on the egress side that directly interrupts power to the lock, independent of
> the access control system, and maintains the interruption until manually reset. None is shown
> at Doors [x, y, z, w]. Provide the device, its location, and its wiring on the point-to-point
> details. `[CODE][VERIFY]`

**Deficiency 2 — No signage.**
> **Review comment:** Required signage is not shown at any of the four magnetically locked
> openings. Provide the sign, the prescribed wording, and the mounting location on the door
> details. `[CODE][VERIFY]`

**Deficiency 3 — Fire alarm release shown as an ACS software integration.**
> **Review comment:** The release on fire alarm is shown as "by ACS integration." A life-safety
> release must be a hardwired path — a dry contact from the fire alarm system that physically
> interrupts power to the locking devices, independent of both head-end systems and of the
> network. A software integration fails silently and in the wrong direction. Revise to show the
> hardwired interface, the contact arrangement, and the interposing relay if used. The software
> integration may be retained *in addition*, for logging. `[CODE][VERIFY]`

**Deficiency 4 — No release on loss of power indicated.**
> **Review comment:** Confirm and show that the locking devices release on loss of power to the
> lock, and that this is not dependent on controller state.

**Deficiency 5 — REX motion sensors as the sole sensor release; coverage not documented.**
> **Review comment:** Where a sensor release is used, provide the sensor coverage pattern for
> each opening, and include in the commissioning plan a test of approach from oblique angles,
> at walking-slow speed, and at seated (wheelchair) height. A sensor aimed for a briskly walking
> adult at chest height will miss the occupants this arrangement exists to protect.

**Deficiency 6 — Device selection not justified.**
> **Review comment:** These are four exterior openings on a warehouse. Confirm whether the doors
> and frames can accept an electrified lockset or exit device. Mechanical egress would eliminate
> the entire release subsystem above (five components plus a recurring test obligation) and
> would improve attack resistance at an exterior opening. If a magnetic lock is required at
> these openings, provide the reason.

**Deficiency 7 — No bond/status monitoring shown.**
> **Review comment:** Provide magnetic bond status monitoring at each lock. Without it the
> system cannot distinguish "locked" from "energized but not holding."

**Deficiency 8 — Ongoing testing obligation not addressed.**
> **Review comment:** Include the recurring test requirement for these arrangements in the O&M
> documentation and the owner training scope.

**The comment I would put first, above all of them:** deficiency 6. Everything else is a
consequence of a device choice that may not have been necessary.

---

## E5.4 — "We lock the back door during the evening shift"

Model answer (137 words):

> I need you to stop doing that tonight.
>
> If there's a fire in the stockroom during evening shift, that door is the exit closest to
> where your people are standing. Locked, they have to turn around and cross the store through
> the smoke to reach the front. That's the situation that gets people killed, and it's the
> reason locking an exit is illegal rather than just inadvisable — it's not paperwork, it's
> because it has happened, repeatedly.
>
> It's also on you personally if it happens, not on the company.
>
> Here's the thing though: I can solve the problem you're actually solving. You're worried
> about someone coming in off the alley. We can lock that door from the *outside* completely —
> there's no rule against that. Nobody gets in, your people still get out, and I can have it
> done this week.

**What makes it work:** direct, gives the reason in physical terms rather than citing a code
section, mentions personal liability once without dwelling on it, and — critically — spends the
last third solving their problem. A manager who is only told "stop" will start again in six
weeks. A manager who is given a better answer won't.

---

## E5.5 — Delayed egress design narrative paragraph

Model answer:

> **Delayed egress locking — Doors 118, 119, 142**
>
> Doors 118, 119, and 142 are rear exit doors from the stockroom and receiving areas,
> discharging to the service yard. Each is provided with delayed egress hardware. On operation
> of the exit device, a local audible alarm sounds immediately and the door remains locked for
> `[VERIFY — delay period permitted by §____ of the adopted ____ Code, ____ edition; longer
> period, if used, requires AHJ approval per §____]`, after which the door unlocks and remains
> unlocked until manually reset at the door. The initiation sequence is irreversible; releasing
> the device does not reset the timer.
>
> This arrangement is applied under `[VERIFY — cite the permitting section]`, which permits
> delayed egress in this occupancy classification `[VERIFY — occupancy: ____, per the life
> safety plan, sheet ____]` subject to the building being protected throughout by an automatic
> sprinkler system `[VERIFY — confirmed, see sheet ____]`. The number of delayed egress doors
> in any single means of egress path does not exceed `[VERIFY — limit per §____]`; the egress
> path analysis is shown on sheet ____.
>
> Each device releases automatically and immediately on: activation of the building fire alarm
> system; waterflow in the automatic sprinkler system; and loss of power to the locking device.
> All three releases are hardwired. The fire alarm interface is a dry contact from the FACP
> interrupting power to the locking devices, shown on sheet ____, detail ____. No release
> function is dependent on the access control system, its servers, or the network.
>
> Signage is provided at each door in accordance with `[VERIFY — §____ ; confirm required
> wording verbatim and mounting location]`, mounted `[VERIFY — required location relative to
> the release device]`.
>
> These arrangements were reviewed with `[AHJ name and title]` on `[date]`; written
> confirmation is in the project record at `[reference]`.
>
> **Ongoing obligation transferring to the owner at substantial completion:** each delayed
> egress device requires periodic testing per `[VERIFY — §____ ]`. This requirement, the test
> procedure, and the record-keeping form are included in the O&M documentation, section ____.

**What makes it a real narrative rather than a description:** it names the doors, states the
arrangement, cites the permitting path *as placeholders that visibly demand filling*, records
the AHJ conversation with a date and a document reference, and — the part almost everyone omits
— explicitly hands the recurring obligation to the owner in writing.

> 🧠 The `[VERIFY]` placeholders are not laziness; they are the correct output at this stage.
> A narrative with confident-looking citations that nobody checked is far more dangerous than
> one with visible holes, because the holes get filled and the wrong citations don't get
> caught.

---

## E5.6 — Data hall door on the means of egress

**What you cannot do:**

- You cannot prevent egress. The door must open from the inside, in one motion, no key, no
  special knowledge, whenever the building is occupied.
- You cannot add a second releasing operation — no deadbolt above the lever, no thumbturn plus
  lever.
- You cannot rely on a delayed egress arrangement unless the occupancy and conditions permit it,
  and a data center's occupancy classification and the position of this door on the path both
  need checking. `[CODE][VERIFY]`

**What you can do — and it's more than people expect:**

| Direction | What's available |
|---|---|
| **Entry (unconstrained)** | Everything. Credential + PIN or biometric, mantrap or interlocked vestibule ahead of it, anti-passback, two-person rule, video verification. Free egress says nothing about entry. |
| **Egress detection** | Door position switch, latch monitoring, REX event logging, alarm-linked camera on both sides. You can know precisely who left, when, and what the door did. |
| **Egress deterrence** | Local sounder on unexpected use, visible camera, signage. All permitted. |
| **Egress delay** | Only delayed egress, only if permitted. Assume it isn't until verified. |

**Where to put the security the door cannot provide:**

This is the actual answer, and it comes straight from the functional chain
(`../../01_Foundations/03_functional_chain.md`): if this opening cannot carry delay, move the
delay somewhere it can.

1. **Layer outward.** Put the hard control at the *entry* to the data hall suite — a vestibule
   or mantrap with a credential on both sides — so that reaching this egress door already
   required passing a strong control. The egress door then only has to be *monitored*, not
   *hardened*.
2. **Layer inward.** Put delay at the cabinet and cage level. Locking cabinets, caged suites,
   and cabinet-level access logging mean the asset is protected even by someone standing in the
   hall.
3. **Detect at the door, respond from the layer.** Alarm-linked video at the egress door with a
   verified response, so an unauthorized departure is detected and assessed in seconds, not
   discovered later.
4. **Reduce the consequence.** Ask what could actually leave through that door. If the answer
   is "a drive," the control is at the drive — media handling procedure, encryption at rest,
   and cabinet locks — not at the door.

> 🧠 The reframe worth carrying: *an egress door is a detection point, not a barrier.* Once you
> stop trying to make it a barrier, the design gets both more compliant and more effective,
> because you put the delay where delay is allowed to live.
