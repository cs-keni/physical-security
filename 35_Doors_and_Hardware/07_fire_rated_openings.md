# 07 — Fire-Rated Openings

> ⚠️ **Same warning as lesson 05.** Ratings, durations, clearances, and permitted modifications
> are governed by adopted codes and listing standards that vary by jurisdiction and edition, and
> are enforced by an AHJ. Every numeric or prescriptive claim here is tagged `[CODE][VERIFY]`.
> This lesson teaches the *shape* of the requirements and the questions to ask. It is not a
> compliance reference.

## Learning objectives

- Explain what a fire door is actually for, in terms of the barrier it restores.
- Describe a rated opening as a **tested assembly** and explain why components cannot be mixed
  freely.
- Locate and read a fire label, and state what voids one.
- Name the four behaviors a rated opening must always exhibit, and connect each to a security
  design decision you have already learned.
- Identify the ways security scope routinely damages a rated opening, and specify around them.
- Explain the recurring inspection obligation your design creates and who ends up owning it.

---

## ELI5

A fire-rated wall is there to hold fire and smoke on one side for a stated number of minutes so
people can get out and firefighters can get in.

A door is a hole in that wall.

A fire-rated door assembly is what makes the hole behave like the wall did — for a while. Not
forever: 20, 45, 60, 90, or 180 minutes, depending. `[VERIFY]`

For that to work, four things have to be true, always:

1. It has to be **closed**.
2. It has to be **latched**.
3. It has to be the **tested combination** of parts.
4. Nobody may have **cut a new hole in it**.

Almost everything a security engineer does at a door threatens number 3 or number 4, and
magnetic locks threaten number 2.

---

## The assembly is the product

This is the concept that makes the rest of the lesson make sense.

**A fire door rating belongs to an *assembly*, not to a door.** The leaf, the frame, the hinges,
the closer, the latching hardware, the glazing, the gasketing, and the anchoring were tested
*together* to a standard such as UL 10C or UL 10B, and the rating applies to that combination.
`[STANDARD][VERIFY]`

```
   NOT A RATED DOOR                    A RATED OPENING ASSEMBLY

   ┌─────────────┐                     leaf (labeled)
   │             │                       + frame (labeled)
   │  "the door" │                       + hinges (listed)
   │             │                       + closer (listed)
   │             │                       + latching hardware (listed, positive latch)
   └─────────────┘                       + glazing (listed, area-limited)
                                         + gasketing (listed)
                                         + anchoring per the listing
                                         + NOTHING ELSE ADDED
                                       ────────────────────────────
                                         = 90-minute rated opening
```

**The engineering consequence:** you cannot substitute a component because it looks equivalent.
A closer that is not listed for the assembly, a hinge that isn't, a piece of glass that isn't —
each one takes the assembly outside what was tested, and outside what was tested is not rated.

> **Software bridge:** this is a version-pinned dependency set that was tested as a whole. You
> know what happens when someone swaps one library for a "compatible" one because the API
> matched.
>
> **Where the analogy breaks:** your test suite tells you. Here nothing tells you. The assembly
> looks identical, works identically, and carries a label that still says 90 minutes. The
> divergence between the label and the reality is silent and can persist for the life of the
> building.

---

## Ratings and where they come from

Openings are rated in minutes. Commonly encountered durations: **20, 45, 60, 90, 180**.
`[VERIFY]`

**The opening rating is generally less than the rating of the wall it sits in**, on the
reasoning that the opening is a small part of the barrier and is not exposed to the same load
for the same duration. A 2-hour wall commonly takes a 90-minute opening; a 1-hour wall commonly
takes a 45-minute opening. `[CODE][VERIFY — the required opening protective rating for a given
wall rating is a code table. Look it up; do not carry these pairings in your head as fact.]`

**Where the requirement comes from, and who owns it:** the architect's life safety plan and code
analysis establish which walls are rated and therefore which openings are rated. **You do not
determine this and you must not infer it from the drawings.** Get the life safety plan, and note
the sheet number in your design narrative.

Related ratings you will see and should not confuse:

| Term | What it addresses |
|---|---|
| **Fire protection rating** | The opening protective — resisting fire spread through the opening |
| **Fire resistance rating** | The wall/barrier itself |
| **Temperature rise rating** | Limits heat transmitted through the door — matters where the door serves an exit enclosure people will be standing next to `[VERIFY]` |
| **Smoke rating / S-label** | Smoke leakage performance; drives gasketing `[VERIFY]` |

---

## The label

The evidence that an assembly is what it claims to be.

**Where to look:**
- **Leaf:** on the **hinge edge**, near the top. Open the door and look at the edge.
- **Frame:** in the rabbet on the hinge jamb, or on the frame face near the hinge.
- Glazing, closers, and hardware carry their own listing marks.

**What it tells you:** the listing agency, the assembly's rating in minutes, and often the
temperature rise rating and whether the assembly is rated for a particular use.

**What voids it — the practical list:**

- **A hole that wasn't in the listed preparation.** Drilling for a card reader through-bolt, a
  door position switch, a transfer raceway, a viewer, or a pull.
- **Field modification of the leaf or frame** — cutting, trimming, welding, or plugging.
- **An unlisted component substituted in.** Wrong closer, wrong hinge, unlisted glazing.
- **Removing a required component.** Taking the closer off because users complained.
- **Painting over the label** so it can no longer be read. A label that cannot be read cannot be
  relied on, and an inspector will treat the assembly accordingly.

`[CODE][VERIFY — what constitutes a permitted field modification, and who is permitted to make
one, is governed by the listing and by NFPA 80. Some modifications are permitted when performed
by a party authorized by the listing agency. "Some" is not "the ones you were about to make."]`

> 🧠 **The uncomfortable operational truth:** you can specify a rated opening perfectly and have
> its label voided in the field by an installer with a hole saw who is genuinely trying to
> complete your scope. The label will still be attached. Nothing will look wrong. The control is
> not vigilance after the fact — it is the **submittal** (prep specified and factory-applied),
> the **pre-installation meeting** (say this out loud to the people holding the tools), and the
> **inspection**.

---

## The four behaviors

Every rated opening must, always:

### 1. Be closed

A fire door propped open is not a fire door. The most common permanent violation in any
building, and it is almost always a workflow problem rather than a discipline problem — the door
is in the way of how people actually work.

**Your design relevance:** a door-held-open alarm on the access control system is a genuinely
useful control here, and it costs almost nothing when you already have a door position switch.
It also creates a nuisance-alarm risk if the workflow problem isn't solved, so solve the
workflow problem too. See `../19_Operations/`.

### 2. Be self-closing

The closer is not an accessory. On a rated opening it is a required component of the tested
assembly, and it must be listed for that assembly.

**Hold-opens are permitted only when they release on fire alarm.** An electromagnetic hold-open,
or a closer-holder-release unit, holds the door open in normal use and drops it on alarm.
`[CODE][VERIFY]` A wooden wedge, a hook, a fire extinguisher, or a chair is not a hold-open; it
is a violation.

**Your design relevance:** magnetic hold-opens are on the fire alarm interface, alongside the
egress releases from lesson 04, and they are frequently in the security scope by accident
because they are the same kind of device on the same kind of circuit. Know whose scope they are
on your project. Find out in writing.

### 3. Be self-latching (positive latching)

**This is the requirement that determines your locking hardware.**

A closed but unlatched door does not stay closed under fire conditions. Pressure differential
across a barrier during a fire is real and it will push an unlatched leaf open. The door has to
be *held* in the frame by a bolt.

**Consequences you already know, now with their reason:**

| From lesson | Consequence | Why |
|---|---|---|
| 03 | **Magnetic locks are generally incompatible with rated openings** `[CODE][VERIFY]` | A mag holds by friction against a face, not by a bolt in a strike. It is not positive latching, and it releases on fire alarm by design — exactly when the door must stay shut. |
| 03 | **Fire exit hardware cannot be dogged** | Dogging holds the latch retracted. A non-latching fire door is not a fire door. |
| 04 | **Rated openings are fail secure and self-latching** | The latch must be mechanical and must always engage. |
| 04 | **Stair re-entry releases the *trim*, not the latch** | The door stays latched; only credential control on the outside lever goes away. |
| 03 | **Electric strikes on rated openings must be fire-rated and continuously latching** `[CODE][VERIFY]` | A standard strike's keeper can be released, which un-latches the door. A fire-rated strike holds the latch under fire conditions. |

If you retain one sentence from this lesson: **a fire door must latch, so anything that
interferes with latching is off the table at a rated opening.**

### 4. Be unmodified

Covered above. Everything in the assembly is what was tested, and there are no additional holes.

---

## What security scope does wrong at a rated opening

The pattern: every one of these is a reasonable thing to want, done in a way that destroys the
rating.

| What we want | The wrong way | The right way |
|---|---|---|
| A card reader on the frame | Through-bolt or drill the frame in the field | Reader on the wall beside the opening, or a factory-prepped frame per the approved submittal |
| A door position switch | Drill the frame head on site | Specify the DPS prep with the frame order; use a listed assembly and prep `[VERIFY]` |
| Power into the leaf | Field-route a raceway; surface door loop | Factory prep, listed transfer, specified at submittal (lesson 06) |
| Electric locking | Magnetic lock | Electrified lockset or fire exit hardware, fail secure, self-latching |
| Hold the door open for a workflow | A wedge | Listed magnetic hold-open on the fire alarm interface |
| A vision panel added later | Cut a lite into the leaf | Not available. Order the door with listed glazing, or don't have one. |
| Reduce closing force because users complain | Back the closer off, or remove it | Correct closer sizing, correct hinges, and an accessibility review. Never removal. |

> ⚠️ **The card reader on a rated frame is the one that catches people**, because it feels
> harmless. The reader is 3 inches across and the frame is steel. But a through-bolt is a hole
> that was not in the listing, in a component of the assembly. Mount the reader on the wall.
> Nothing about the reader's function requires it to be on the frame — that is purely a habit
> from drawing plans where the frame is the obvious anchor.

---

## The obligation your design creates

Rated openings are subject to **periodic inspection and testing** — commonly annual — under
NFPA 80. `[STANDARD][VERIFY frequency, scope, and documentation requirements against the
adopted edition.]`

The inspection checks, roughly: label present and legible; no unapproved holes or field
modifications; clearances within tolerance; door closes and latches from any position; closer
functioning; hold-opens releasing; gasketing intact; no missing or broken parts; glazing intact
and listed. `[VERIFY the current checklist.]`

**Why this is your problem even though you don't perform it:**

- Every rated opening you put electrified hardware on is an opening whose inspection now
  includes your components.
- If you specified a magnetic hold-open, its release is on the test list.
- If your commissioning didn't verify that the door closes and latches from any position, you
  handed over an opening that will fail its first inspection.
- **Somebody has to own this at the owner's organization, and typically nobody has been told.**

**Put it in the O&M handover.** One paragraph naming the obligation, the frequency, the openings
affected, and the components of yours that are on the test list. See `../19_Operations/`.

> 🧠 This is a recurring theme across lessons 04, 05, and 07: **your design creates ongoing
> obligations that transfer to the owner at substantial completion, and they are invisible
> unless you write them down.** Delayed egress testing, sensor-release testing, fire door
> inspection, battery replacement, key control. An engineer who hands over the obligations
> along with the system is doing the job; one who hands over only the system is leaving a
> building that degrades on a schedule.

---

## Design tradeoffs

| Tradeoff | The tension | How to resolve |
|---|---|---|
| Reader on the frame vs. on the wall | The frame is the obvious anchor on a plan | Wall, at every rated opening. It costs nothing and removes the risk. |
| Electrified lockset vs. fire-rated electric strike | The lockset gives better monitoring; the strike needs no transfer | Either works if listed. Choose on monitoring and retrofit constraints, not on the rating. |
| Hold-open convenience vs. component count | A listed hold-open solves a real workflow problem; it adds a device on the FA interface | Use it where the workflow genuinely requires it; fix the workflow where it doesn't |
| Vision panel vs. rating | Visibility improves safety and supervision; glazing is area-limited and must be listed | Decide at door order. It is not a later decision. |
| Closing force vs. latching reliability | A weak closer is pleasant and doesn't latch | Correct sizing and correct hinges. Never trade away latching. |

---

## Common mistakes

⚠️ **Treating the rating as a property of the leaf.** It's the assembly.

⚠️ **Magnetic lock on a rated opening.** Not positive latching. `[CODE][VERIFY]`

⚠️ **Field drilling a rated frame or leaf** for a reader, DPS, or raceway.

⚠️ **Dogging specified on fire exit hardware.**

⚠️ **Substituting a "compatible" closer or hinge.**

⚠️ **Painting over the label.**

⚠️ **Removing or defeating the closer** in response to a complaint.

⚠️ **Inferring which openings are rated from the drawings** instead of getting the life safety
plan.

⚠️ **Commissioning by inspection.** Test that the door closes and latches from a 5-degree
opening, not just from wide open.

⚠️ **Not handing over the inspection obligation.**

---

## Junior vs. Senior

**Junior:** knows a rating belongs to an assembly; can find and read a label; knows the four
behaviors; knows a mag lock doesn't belong on a rated opening; specifies factory prep.

**Senior:** gets the life safety plan in writing before designing any rated opening and cites
the sheet; anticipates the field-modification risk and addresses it at the pre-installation
meeting rather than discovering it at inspection; moves readers off frames as a standing
practice; knows which hold-opens are on whose scope and settles it in writing early; commissions
latching from a nearly-closed position; and hands the recurring inspection obligation to the
owner in the O&M documentation with the affected openings enumerated.

---

## 🔧 Field exercise

Find three rated openings — stair doors and mechanical/electrical room doors are the usual
candidates.

1. **Find the label** on the hinge edge of the leaf. Photograph it. Record the rating.
2. Find the frame label.
3. **Test the latching from nearly closed.** Open the door about five degrees and release it.
   Does it close *and latch*? This is the test that fails.
4. Look for unapproved holes: readers or switches bolted through the frame, added viewers,
   drilled raceways.
5. Check for a wedge, hook, or other prop. If you find one, note where and why — there is
   always a workflow reason.
6. If the door has electrified hardware, note whether it is a mag lock. If it is, you have found
   something worth raising.

---

## Exercises

**E7.1** For each, state whether it is acceptable at a 90-minute rated opening and why:
- (a) Magnetic lock with sensor release and hardwired FA release.
- (b) Fire exit hardware with electric latch retraction and electrified trim.
- (c) Electric strike, fail secure, listed for fire doors.
- (d) Card reader through-bolted to the frame.
- (e) Electrified mortise lockset, fail secure, with a factory-prepped transfer hinge.
- (f) A magnetic hold-open releasing on fire alarm.
- (g) Surface door loop installed in the field after the doors arrived.

**E7.2** A 2-hour rated wall separates a data hall from a corridor. Describe the process by
which you determine the required opening rating, who provides each input, and what you record in
your design narrative. Do not state the rating.

**E7.3** During a site walk two weeks before turnover you find that the electrical contractor
has drilled the frame head of six 90-minute stair doors to install recessed door position
switches. The switches are in and working. Write your finding, your recommendation, and the
conversation you would have with the GC.

**E7.4** A facilities manager tells you the stair door on level 3 "sticks" and they've been
propping it with a fire extinguisher. Write a response of under 150 words that solves their
problem rather than just prohibiting theirs.

**E7.5** Write the O&M handover paragraph for a project with 48 rated openings, of which 31 carry
security hardware. Name the obligation, the frequency, what is tested, which of your components
are on the test list, and who you are recommending owns it. Use `[VERIFY]` placeholders for the
regulated specifics.

**E7.6** Trace the reasoning: explain, in a single paragraph starting from "a fire door must
latch," why each of these follows — no magnetic locks, no dogging on fire exit hardware, fail
secure only, and stair re-entry releasing the trim rather than the latch.

> Solutions: [`_solutions/07_fire_rated_openings_solutions.md`](_solutions/07_fire_rated_openings_solutions.md)

---

## Retrieval check

1. What is a fire door assembly for, and why is the rating a property of the assembly?
2. Where are the labels, and name five things that void one.
3. State the four behaviors a rated opening must always exhibit.
4. Why must a fire door positively latch, and what does that rule out?
5. Why is a magnetic lock generally unacceptable at a rated opening — give both reasons.
6. Where should a card reader be mounted at a rated opening, and why?
7. What recurring obligation does a rated opening carry, and who ends up owning it?
8. Why is "the door closes when I let it go from wide open" an inadequate test?

---

## References

- NFPA 80 — *Standard for Fire Doors and Other Opening Protectives*. The governing document for
  what a rated assembly is, what may be done to it, and the inspection and testing obligation.
  `[STANDARD][VERIFY edition]`
- NFPA 105 — smoke door assemblies. `[STANDARD][VERIFY]`
- UL 10C / UL 10B — fire door assembly test standards. `[STANDARD][VERIFY]`
- Applicable building code — opening protective ratings required for each wall rating, and the
  occupancy-driven requirements. `[CODE][VERIFY adopted edition]`
- Listing agency directories — the authority on whether a specific component is listed for a
  specific assembly. `[VERIFY]`
- DHI — application practice at rated openings. `[PRACTICE]`
- `../10_Codes_Standards/` — determining and citing the adopted edition.
- `../18_Commissioning/` — test procedures.
- `../19_Operations/` — O&M handover and recurring obligations.

**Next:** [08 — Key Management and Mechanical Security](08_key_management.md)
