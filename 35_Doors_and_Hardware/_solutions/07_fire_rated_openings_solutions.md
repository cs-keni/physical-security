# Solutions — 07 Fire-Rated Openings

> ⚠️ These are reasoning demonstrations, not compliance determinations. Every conclusion would
> require verification against the adopted code, the listing, and the AHJ on a real project.

---

## E7.1 — Acceptable at a 90-minute rated opening?

**(a) Magnetic lock with sensor release and hardwired FA release.**
**No.** Two independent reasons:

1. **Not positive latching.** A mag holds by magnetic force against a face; there is no bolt in
   a strike. A fire door must be held in the frame by a latch, because pressure differential
   across the barrier will push an unlatched leaf open.
2. **It releases on fire alarm by design** — which is exactly the moment the door must stay
   shut. The egress arrangement and the fire barrier function are in direct opposition here,
   and that opposition is why the device doesn't belong on this opening. `[CODE][VERIFY]`

The correct move is not to argue the arrangement; it is to change the device family.

**(b) Fire exit hardware with electric latch retraction and electrified trim.**
**Yes, with conditions.** Fire exit hardware is the right family: always latching, no dogging,
fire-labeled.

Conditions to verify:
- The specific ELR and trim options must be **listed for use on the rated assembly**. Not all
  are. `[VERIFY]`
- Prep must be factory-applied per the approved submittal.
- The power transfer must be factory-prepped and listed (lesson 06).
- ELR must not hold the latch retracted in any normal or failure state — the latch has to
  re-engage.

**Worth challenging:** does this opening need ELR at all, or does electrified trim alone do it?
Trim is simpler, lower current, and one fewer thing to be listed. Lesson 03's guidance applies.

**(c) Electric strike, fail secure, listed for fire doors.**
**Yes** — this is one of the two correct electrified answers at a rated opening.

Verify: the strike is specifically **fire-rated and continuously latching**, listed with the
assembly, fail secure, and the frame prep is factory-applied. A standard electric strike is not
acceptable; the qualifier "listed for fire doors" is doing all the work in this option.
`[CODE][VERIFY]`

**(d) Card reader through-bolted to the frame.**
**No.** A through-bolt is a hole that was not in the listed preparation, in a component of the
tested assembly. It voids the label.

**And it is completely unnecessary.** Mount the reader on the wall beside the opening. Nothing
about a reader's function requires it to be on the frame; that is a habit from drawing plans
where the frame is the obvious anchor. This is the mistake most likely to be made by a competent
person acting in good faith, which is why it's on the list.

**(e) Electrified mortise lockset, fail secure, with a factory-prepped transfer hinge.**
**Yes.** This is the other correct electrified answer, and generally the better one — it gives
latch monitoring and an integral REX that the strike doesn't.

Verify: the lockset is fire-labeled; it is fail secure; the latch is mechanical and always
engages; the hinge and its prep are listed for the assembly; all prep is factory-applied.

**(f) Magnetic hold-open releasing on fire alarm.**
**Yes**, when listed and correctly interfaced. This is the *permitted* way to hold a fire door
open, and it exists precisely because propping is otherwise inevitable when a door is in the way
of how people work.

Verify: the hold-open is listed; the release is on the fire alarm interface (hardwired, per
lesson 04); it is included in the periodic inspection scope; and the door fully closes **and
latches** on release, tested. `[CODE][VERIFY]`

**(g) Surface door loop installed in the field after the doors arrived.**
**No.** Attachment to the leaf and frame beyond the listed preparations voids the label. See
E6.4 for the full response. The options are factory prep, a device family change that keeps the
electrification in the frame, or — if and only if the listing permits it — modification by a
party authorized by the listing agency. `[VERIFY]`

---

## E7.2 — Determining the required opening rating

**The process, and who provides each input:**

| Step | Input | Who provides it |
|---|---|---|
| 1 | Occupancy classification of the spaces on both sides | Architect / code consultant, on the code analysis sheet |
| 2 | Adopted code and edition for the jurisdiction | Architect / code consultant; verify independently, do not assume |
| 3 | The **fire resistance rating of the wall** and its type (fire barrier, fire partition, fire wall, smoke barrier — these are not synonyms and they carry different opening requirements) | Architect's **life safety plan** |
| 4 | The required **opening protective rating** for that wall rating and type | A code table. Look it up against the adopted edition. `[CODE][VERIFY]` |
| 5 | Any additional requirements: temperature rise rating, smoke/S-label, glazing area limits | Code, driven by the wall type and the opening's location in the egress system `[CODE][VERIFY]` |
| 6 | Confirmation that the opening is where you think it is on the means of egress | Life safety plan |

**What I record in the design narrative:**

> The opening at Door 3-14 is located in a `[wall type]` with a `[  ]`-hour fire resistance
> rating, per the life safety plan, sheet `[  ]`, revision `[  ]`, dated `[  ]`. The required
> opening protective rating is `[  ]` minutes per `[code section]` of the `[code, edition]` as
> adopted by `[jurisdiction]`. Security hardware specified at this opening — `[list]` — is
> listed for use on a `[  ]`-minute assembly; listing references are in the submittal at `[  ]`.
> All preparation is factory-applied. No field modification is permitted.

**The two things that make this a real record rather than a note:**

1. **The sheet number and revision of the life safety plan.** Ratings change during design. A
   narrative that cites "the life safety plan" without a revision is citing a moving target,
   and when the rating changes at 90% CD nobody will connect it to your hardware.
2. **Explicitly stating that no field modification is permitted.** It reads as obvious and it is
   the sentence that gets quoted back during the pre-installation meeting.

**Why I don't state the rating in this answer:** the wall-rating-to-opening-rating mapping is a
code table, it varies by wall type and by edition, and reciting a pairing from memory is exactly
the failure mode this module warns about. The engineering skill is knowing that a table exists,
knowing which inputs it takes, and knowing whose document supplies each.

---

## E7.3 — Six rated stair doors drilled for door position switches

**The finding:**

> **Finding — unapproved field modification to rated openings.**
>
> During the site walk on `[date]`, recessed door position switches were observed installed in
> the frame heads of six 90-minute rated stair doors: `[opening numbers]`. The frames appear to
> have been field-drilled. No factory prep or listed field-modification documentation was
> presented.
>
> A field modification beyond the listed preparation voids the assembly's label. These six
> openings currently carry labels stating a 90-minute rating that the assemblies may no longer
> hold. This is a life-safety condition, not a cosmetic one: it is also the failure mode that
> is *least* likely to be caught downstream, because the label is still attached and the doors
> look correct. `[CODE][VERIFY]`

**The recommendation:**

1. **Stop work** on any further DPS installation at rated openings, today.
2. **Inventory** — confirm exactly which openings were modified and how. Six is the observed
   count, not necessarily the actual one.
3. **Determine whether the modification is recoverable.** Ask the listing agency or an
   authorized party whether this specific modification can be evaluated and re-labeled in the
   field. Some can. `[VERIFY]` This is the cheapest path if it exists, and it must be
   established by the listing agency, not by opinion.
4. **If not recoverable:** replace the frames, or replace the assemblies. This is the expensive
   answer and it is the correct one if step 3 comes back negative.
5. **Design alternative going forward:** at rated openings, specify frames with **factory DPS
   prep**, or use a **surface-mounted** switch if one is listed for the application, or take door
   position from the **integral latch/lock monitoring** in the electrified lockset — which, at
   an opening that already has one, means no separate DPS is needed at all. That last option is
   worth checking first at all six.
6. **Document** the resolution and put it in the O&M package, because the next fire door
   inspection will look at these openings.

**The conversation with the GC:**

> I need to raise something and I want to be straightforward that some of this is on us.
>
> Six of the 90-minute stair doors have field-drilled frames for the position switches. That
> voids the labels — the assemblies aren't rated anymore even though the labels are still on
> them. I don't think anyone did anything unreasonable here; the switches were on our drawings,
> the prep wasn't called out, and the electrician installed them the only way available.
>
> Two things I need. First, stop any further DPS installs at rated openings until we sort this
> out — I'll get you the opening list within the hour. Second, help me find out whether this
> modification can be field-evaluated and re-labeled by an authorized party. If it can, that's
> the cheap path and I want to know today.
>
> If it can't, we're looking at frame replacement at six openings, and I'd rather have that
> conversation now, with two weeks left, than at the fire door inspection after turnover.
>
> Going forward we'll call out factory DPS prep in the frame schedule. On four of these six
> the openings already have electrified locksets with latch monitoring, so we may not need a
> separate switch at all — let me check that before we replace anything.

**What makes the conversation work:**

- Opens by absorbing part of the blame, honestly, because the prep genuinely wasn't specified.
- Doesn't soften the technical finding at all.
- Two concrete asks, one of which is a stop-work.
- Raises the expensive outcome early and frames the timing as the reason to talk now.
- Ends with the possibility that four of the six need no switch, which turns a confrontation
  into a joint problem.

---

## E7.4 — The stair door propped with a fire extinguisher

Model answer (146 words):

> Take the extinguisher out today — if there's a fire on that stair, that door has to be shut,
> and that's also the one thing an inspector will write you up for on sight.
>
> But you're propping it for a reason, so let's fix the reason. Two possibilities:
>
> If it genuinely sticks, that's a mechanical problem I can get corrected — usually a closer
> that's out of adjustment or a frame that's moved. A door that's hard to open is also a door
> that's failing its accessibility requirement, so it needs fixing regardless.
>
> If it doesn't stick and people are propping it because the badge reader is slow or the route
> is awkward, tell me that instead. The fix there is a listed magnetic hold-open: it holds the
> door open all day and drops it automatically when the fire alarm goes off. That's the legal
> way to have the door open, and it's not expensive.
>
> Which one is it?

**What makes it work:** the prohibition is one sentence, delivered first, then the entire rest is
about solving their problem. It names the two possible causes and gives a real fix for each,
including a device the manager has probably never heard of that does exactly what they want. It
ends with a question, which is what turns it from a lecture into a conversation. A manager told
only "stop" starts again in six weeks.

---

## E7.5 — O&M handover paragraph

Model answer:

> **Fire door assemblies — recurring inspection and testing obligation**
>
> This project includes **48 fire-rated door assemblies**, of which **31 carry security hardware
> installed under this scope**. Rated door assemblies are subject to periodic inspection and
> testing under `[VERIFY — NFPA 80, § ____, as adopted; confirm the required frequency, which is
> commonly annual]`. **This obligation transfers to the building owner at substantial completion
> and recurs for the life of the building.**
>
> The inspection covers, at minimum `[VERIFY current checklist against the adopted edition]`:
> labels present and legible on leaf and frame; no unapproved holes or field modifications;
> clearances within tolerance; the door closes from any open position and **positively latches**;
> the closer operates; hold-open devices release on fire alarm and the door then closes and
> latches; gasketing intact; glazing intact and listed; no missing, broken, or substituted parts.
>
> **Components installed under the security scope that are within the inspection scope at the 31
> openings:**
> - Electrified locksets and fire exit hardware — must positively latch on every closure
> - Fire-rated electric strikes — must maintain continuous latching
> - Power transfer devices — no damage, no unapproved routing
> - Door position switches — factory-prepped; any field modification is a finding
> - Magnetic hold-opens at openings `[list]` — must release on fire alarm and the door must then
>   close and latch
> - Card readers — verify none has been relocated onto a rated frame
>
> **A schedule of the 48 openings, their ratings, their labels as transcribed at commissioning,
> and the security components at each, is at `[reference]`.** Commissioning test records
> demonstrating that each door closes and latches from a nearly-closed position are at
> `[reference]`.
>
> **Recommended owner:** `[role — typically Facilities Manager or Director of Engineering]`,
> coordinating with `[Security Manager]` for the components listed above. Inspection should be
> performed by a person qualified per `[VERIFY — qualification requirements per the adopted
> standard]`.
>
> **This obligation is frequently unassigned at handover.** Assigning it in writing now is the
> difference between a documented program and a finding at the first inspection.

**What makes it a real handover rather than a disclaimer:** it enumerates the affected openings
by count and provides the schedule; it lists *your* components specifically, so the inspector and
the owner both know what security scope is on the test list; it names a recommended owner by
role; it points at the commissioning records that establish the baseline; and it says the quiet
part — that nobody usually owns this — which is the sentence most likely to cause someone to
actually own it.

---

## E7.6 — The chain of reasoning from "a fire door must latch"

Model answer:

> A fire door must positively latch, because under fire conditions the pressure differential
> across the barrier is real and it will push an unlatched leaf open — a closed but unlatched
> door is not a barrier. Everything else follows from that single requirement. **Magnetic locks
> are out**, because a mag holds by magnetic force against a face rather than by a bolt in a
> strike, so it is not a latch at all; and because it releases on fire alarm by design, which is
> precisely when the door must stay shut. **Dogging on fire exit hardware is out**, because
> dogging works by holding the latch retracted, which is definitionally a non-latching door.
> **Fail safe is out** and rated openings are fail secure, because a fail-safe device unlocks on
> power loss and a fire is a plausible cause of power loss — the latch must be mechanical and
> must engage regardless of electrical state. And **stair re-entry releases the outside trim
> rather than the latch**, because the re-entry requirement is about a person in the stair being
> able to *operate* the lever without a credential, not about the door standing unlatched: the
> bolt stays engaged, the door stays a barrier, and only the credential control on the outside
> lever goes away. Four rules that look like four separate pieces of trivia are one requirement
> applied four times.

**What the exercise is testing:** whether the module's rules have compressed into a principle.
A learner who memorized four facts will list four facts. A learner who understood the module
will derive all four from the latching requirement in one pass, which is what makes them able to
handle the fifth case they haven't seen yet.
