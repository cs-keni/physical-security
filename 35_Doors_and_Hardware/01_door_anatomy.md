# 01 — Door Anatomy: Reading an Opening

## Learning objectives

- Name every component of a commercial opening and state what it does.
- Explain why the unit of design is the **opening**, not the door, and why that distinction
  changes what you specify and who you have to talk to.
- Read a door schedule and a hardware set well enough to find the error in one.
- Identify which components carry security load, which carry life-safety load, and which
  carry both — and why confusing the three is the most common junior failure at an opening.
- Walk up to any commercial door and describe it accurately in under a minute.

---

## ELI5

A door isn't a door. It's five things pretending to be one thing:

1. The **frame** — the metal or wood surround that's fixed to the wall.
2. The **leaf** — the slab that actually moves. (This is what you call "the door.")
3. The **hardware** — hinges, lock, closer, handle. The parts that make it swing, latch, and
   stay shut.
4. The **wall** it sits in.
5. The **gap** between all of them.

Every one of those five can be the weak point, and it usually isn't the one you're looking at.
People spend $4,000 on a high-security lock and hang it on a door in a stud wall with a
suspended ceiling that anyone can climb over in eleven seconds.

---

## The professional framing: the opening is the unit of design

In the construction industry the word for "a hole in a wall with a door in it" is an
**opening**. It is the unit that gets numbered, scheduled, specified, priced, ordered,
delivered, installed, inspected, and warrantied. It is *not* the door.

An opening consists of:

```
   OPENING = DOOR(S) + FRAME + HARDWARE SET + WALL CONDITION + CLEARANCES
```

Each of those is specified by a different party, often from a different discipline, and they
are reconciled — if you are lucky — in the **door schedule** and the **hardware sets** in
specification section 08 71 00, Door Hardware. `[PRACTICE]`

> **Software bridge:** the opening is an interface, the door schedule is its schema, and the
> hardware set is the config bundle that implements it. The parties are different teams
> committing to a shared contract without a compiler to catch the mismatch.
>
> **Where the analogy breaks, and it breaks expensively:** there is no type system, no CI, and
> no rollback. If the hardware set specifies a mortise lock and the door is prepped for a
> cylindrical lock, nobody finds out until a $900 door leaf is standing in a hallway with the
> wrong hole in it, eight weeks after the order went in. The reconciliation is done by humans
> reading tables. **Your review of that table is the CI.** This is why lesson `../33_Design_Review_QA/`
> exists and why the Bluebeam work in `../12_Bluebeam/` matters more than it sounds like it
> should.

### Why you, a security engineer, care

You will rarely own the door. The architect owns it. A specialty consultant — an
**AHC (Architectural Hardware Consultant)**, credentialed through DHI — usually writes the
hardware sets. `[PRACTICE]`

You own a narrow, high-consequence slice: the electrified hardware, the reader, the position
switch, the request-to-exit device, the power supply, and the *interaction* between all of
that and the rest of the opening. That slice cannot be designed without understanding the
whole opening, because:

- An electric strike must match the **lock** it releases and the **frame** it mounts in.
- A magnetic lock must land on a door and frame that can carry its **pull force in shear**,
  and must be released by things that live in the life-safety system.
- A card reader's mounting height and side are determined by the **handing** (lesson 02).
- A door position switch's reliability depends on the **gap** and the **closer** adjustment.

> 🧠 **The single most useful relationship you can build in your first year is with a good
> hardware consultant.** They know things about openings that are not written down anywhere
> you can find them. Bring them the security intent and let them tell you which hardware
> actually exists. Do not send them a device list.

---

## The frame

The frame transfers every load at the opening into the wall. Attack the opening and you are
usually attacking the frame, not the leaf.

```
   FRAME, HEAD-ON (elevation)                    FRAME, PLAN SECTION (looking down)

        ┌──────── head ────────┐                      wall
        │                      │                 ╔════════════╗
        │                      │                 ║            ║  throat
   hinge│                      │strike           ║  ┌─────────╨────┐
   jamb │       (opening)      │jamb             ║  │   backbend   │
        │                      │                 ║  │  ┌────┐      │  ← face / trim
        │                      │                 ║  │  │stop│      │
        │                      │                 ║  └──┤    ├──────┘
        └──┬────────────────┬──┘                 ║     │    │  rabbet (door sits here)
           │  floor / sill  │                    ╚═════╧════╧═══════
```

| Part | What it does | Why it matters to you |
|---|---|---|
| **Head** | Horizontal top member | Where a mag lock or overhead stop usually mounts |
| **Jambs** | Vertical sides — *hinge jamb* and *strike jamb* | The strike jamb is prepped for the strike or electric strike |
| **Stop** | The raised ridge the door closes against | Its side determines swing direction; defines the *rabbet* |
| **Rabbet** | The recess the door sits into | Rabbet depth and door thickness must agree |
| **Throat** | Depth of the frame, matched to wall thickness | Get this wrong and the frame doesn't fit the wall |
| **Backbend / return** | The leg that grips the wall | Part of the anchorage load path |
| **Anchors** | Attach the frame to the wall (masonry T-anchors, stud anchors, existing-wall/EWA) | **This is the security-critical item and nobody looks at it** |
| **Floor anchor** | Ties jamb bottoms to the slab | Resists spreading the frame |

**Two construction types you must be able to tell apart on sight:**

- **Welded frame** — mitred, welded, ground, delivered as one rigid unit, set *before* the wall
  is finished. Stronger, and the only sensible choice at a security-relevant opening.
- **KD (knock-down) / drywall slip-on frame** — ships flat in three pieces and snaps onto a
  finished stud wall. Fast, cheap, common in tenant fit-out. Materially weaker, and it can
  often be *removed* without tools you'd need a permit for.

> ⚠️ **The mistake:** specifying a high-security lock at an opening with a KD frame in a
> single-layer drywall partition. The lock is now the strongest part of a chain whose weakest
> element is 5/8" gypsum board. You have bought delay that the adversary simply walks around.
> Balanced protection (`../01_Foundations/04_defense_in_depth_and_zones.md`) applies at the
> scale of a single opening exactly as it does at the scale of a site.

---

## The leaf

```
   HOLLOW METAL DOOR — cutaway of the lock edge

     ┌───────────────────────────┬──┐
     │                           │  │ ← face sheet (typ. 18 or 16 gauge)
     │        core               │  │
     │  (honeycomb / polystyrene │  │   lock edge, beveled
     │   / polyurethane /        │  │   (typ. 1/8" in 2")
     │   mineral, if fire-rated) │  │
     │                           │██│ ← lock reinforcement (welded-in channel)
     │                           │  │
     └───────────────────────────┴──┘
       hinge edge ↑                    ↑ strike edge
       (hinge reinforcements here)
```

| Material | Where you see it | Security character |
|---|---|---|
| **Hollow metal (HM)** | Exterior, stairs, mechanical, back-of-house | The workhorse. Gauge and reinforcement are what matter, not "it's steel." |
| **Wood, solid core** | Offices, interior suites | Fine for privacy and fire; modest delay |
| **Wood, hollow core** | Residential; should not appear in a secured commercial opening | Effectively decorative |
| **Aluminum storefront** | Main entrances, glass-heavy façades | Delay is governed by the **glazing**, not the aluminum. See below. |
| **FRP** | Wet, corrosive, or wash-down areas | Chosen for environment, not security |

**Parts of a leaf you must name correctly:**

- **Stiles** (vertical members) and **rails** (horizontal, top and bottom) — literal on a wood
  or aluminum door, conceptual on hollow metal.
- **Lock edge / strike edge** — the free edge. Usually **beveled** so it clears the frame.
- **Hinge edge** — the pivoting edge.
- **Lock block** — the solid material in a wood door where the lock is bored. Mislocate it and
  the lock cannot be installed.
- **Reinforcements** — welded channels inside a hollow metal door at hinges, lock, and closer.
  **This is what "prepped for" means.** A door not prepped for a closer cannot take a closer
  without field surgery that voids its fire label.
- **Core** — honeycomb (cheap), polystyrene/polyurethane (thermal), **mineral** (required for
  most fire ratings). `[VERIFY]`
- **Vision lite / lite kit** — a window in the leaf, with a rated frame if the door is rated.
- **Louver** — a vent. Generally incompatible with fire ratings and always incompatible with
  a secure opening. `[VERIFY]`

**Typical commercial dimensions** — memorize these so you can spot an anomaly:

| Dimension | Typical commercial value |
|---|---|
| Leaf width | 3'-0" (single); 6'-0" pair |
| Leaf height | 7'-0" |
| Leaf thickness | 1-3/4" |
| Lock backset (cylindrical) | 2-3/4" |
| Bevel | 1/8" in 2" |

`[PRACTICE]` — these are conventions, not code. Clear-width and maneuvering-clearance
*requirements* are accessibility and life-safety code, and are covered in lesson 05 and
`../10_Codes_Standards/`. `[CODE][VERIFY]`

> ⚠️ **Aluminum storefront is where junior designs die.** The opening is 80% glass. You can
> specify any lock you want; the delay value of the opening is the delay value of the glazing,
> which for standard tempered glass is *a few seconds*. If the design intent is delay, the
> conversation is about laminated glazing or security film — an architectural and cost
> conversation — not about the lock. Say this early. Saying it late looks like you missed it.

---

## Hinges and pivots

| Type | Use | Note |
|---|---|---|
| **Full-mortise butt hinge** | The default | Standard vs. heavy weight; plain vs. **ball bearing** (required with a closer) |
| **Continuous / geared hinge** | High-frequency, heavy, or abused doors | Distributes load along the full edge; excellent for doors that get slammed |
| **Pivot (offset or center-hung)** | Very heavy or full-glass doors | Load goes to floor and head, not the jamb |

**The one security detail:** on an **out-swinging exterior door**, the hinge barrels are on the
unsecured side. The countermeasures are **NRP (non-removable pin)** hinges or **security studs**
(interlocking pins that hold the leaf in the frame even with the hinge pin gone). Specify one
of them, every time, on any out-swinging exterior or out-swinging secure-area door.
`[PRACTICE]`

> 🧠 This is a one-line spec change with a near-zero cost delta that closes an entire attack
> class. Almost nobody catches it in review. Catching it in your first year is how you build
> the reputation that gets you the interesting work.

---

## Latching, locking, and the strike

Full treatment is in lesson 03. For now, the vocabulary:

- **Latch bolt** — the spring-loaded, beveled bolt that holds the door closed. Retracts when
  you turn the lever.
- **Deadlatch / auxiliary latch** — the small secondary plunger beside the latch bolt. When the
  door is closed, it rides on the strike and *blocks* the main latch from being pushed back.
  **It exists specifically to defeat the "slip a card past the latch" class of attack.** If it
  isn't seated — because the door is misaligned or the strike is in the wrong place — the
  opening is far weaker than the schedule says, and nothing visible tells you that.
- **Deadbolt** — a bolt with no bevel and no spring, thrown deliberately. Real delay. Frequently
  prohibited on egress doors unless it retracts with the same single motion that opens the
  door. `[CODE][VERIFY]`
- **Strike** — the plate and pocket in the frame that receives the bolt. The industry-standard
  face is called an **ANSI strike**. Lip length matters: too short and the latch drags on the
  frame; too long and it's a snag hazard in the corridor.
- **Dust box** — the cup behind the strike. Skipped constantly. Without it the bolt lands in
  raw stud cavity and the "throw" the datasheet promises is fiction.

---

## Closers, coordinators, and the rest of the set

| Component | Function | Failure you will actually see |
|---|---|---|
| **Closer** (surface: regular arm / parallel arm / top jamb; concealed; floor) | Returns the door to closed and latched | Adjusted too weak → door doesn't latch → the whole electronic access control layer is bypassed by physics |
| **Coordinator** | On a pair with an overlapping astragal, forces the inactive leaf to close first | Omitted → leaves close out of order → neither latches |
| **Astragal** | Seals the meeting edge of a pair | Overlapping astragals *require* a coordinator |
| **Mullion** (fixed or **removable**) | Vertical post between a pair | Removable mullions give a wide clear opening when needed and a solid strike point when not |
| **Flush bolts** (manual or automatic) | Secure the inactive leaf into head and sill | Manual flush bolts on an egress pair are usually a code problem `[CODE][VERIFY]` |
| **Threshold / sweep / weatherstrip / gasketing** | Seal against weather, smoke, sound, light | Smoke gasketing is a fire-rating item, not a comfort item |
| **Overhead stop / wall stop** | Limits swing | Without one, the lever punches the wall and eventually the closer arm fails |
| **Kick / armor / mop plate** | Protects the leaf | Cosmetic to you, structural to the door's life |
| **Silencers** | Rubber bumpers in the frame stop | Absent on gasketed and rated doors |

> ⚠️ **The closer is the most under-respected component at an access-controlled opening.** An
> electrified lock only secures a door that is *fully closed and latched*. A closer that's been
> backed off because someone complained it was too heavy will leave the door resting against
> the stop, unlatched, all day. Your card reader, your controller, your audit log, and your
> $3,000 of head-end equipment are all perfectly functional and the door is open. Check closers
> on every site walk.

---

## Reading a door schedule

A door schedule is a table with one row per opening. Minimum useful columns:

| Door # | Size | Type | Matl | Frame matl | Rating | Hdwe set | Remarks |
|---|---|---|---|---|---|---|---|
| 105A | 3070 | F | HM | HM | 90 min | 08 | Card reader, DPS |
| 210 | 3070 | N | WD | HM | — | 03 | Office |
| 001 | 6070 | F | HM | HM | 90 min | 12 | Pair, removable mullion, stair |

`3070` is the trade shorthand for 3'-0" × 7'-0". `F` is flush, `N` is narrow-lite. The
**hardware set** number points into the hardware sets in the spec, each of which lists every
piece of hardware for that opening — hinges, lock, closer, stop, seals, and any electrified
components.

**What you are looking for when you review one, in order:**

1. Does every opening that needs access control **have** it, and does every opening that has it
   **need** it? (Both errors are expensive; the second is more common and nobody flags it.)
2. Do the security devices in the hardware set match the ones on your drawings? Reader, strike
   or mag, position switch, REX, power transfer.
3. Is the **fail state** stated, and does it match the opening's function? (Lesson 04.)
4. Is the opening **rated**, and does every specified component carry the matching label?
   (Lesson 07, not yet written — see `../COURSE_PROGRESS.md`.)
5. Does the **frame** support what you hung on it? A mag needs a head that can take the shear;
   an electric strike needs a frame deep enough for the body and a path for the wire.
6. Is there a **power transfer** — an electric hinge or door loop — for anything electrified in
   the *leaf*? Every year, somewhere, an electrified lockset is specified with no way to get
   power across the hinge gap. (Lesson 06.)

> 🧠 **The senior move is to review the door schedule against the security drawings as two
> independent sources and diff them, rather than reading either one on its own.** They are
> produced by different people and they disagree more often than they agree. This is exactly
> the kind of repetitive comparison the Bluebeam and data-model work in `../16_Automation/`
> is built to support: the device data model is the single source of truth and the schedule
> is one of its projections. Automate the comparison; never automate the judgment.

---

## Design tradeoffs

| Tradeoff | The tension | How to resolve |
|---|---|---|
| Welded vs. KD frame | Welded is stronger and must be set before the wall closes; KD is cheap and retrofit-friendly | Welded at every opening with a security or fire function; KD only where neither applies |
| Solid core vs. glazed leaf | Vision improves safety and supervision; glass destroys delay | Glaze for visibility where delay isn't the objective; laminated where you need both |
| Heavy closer vs. usability | A strong closer guarantees latching; users fight it | Correct closer size and correct hinge type, not brute force. Opening-force limits are code. `[CODE][VERIFY]` |
| Pair with removable mullion vs. pair with vertical rods | Mullion gives a solid strike and better security; rods give an unobstructed opening | Mullion unless move-in/move-out width genuinely requires otherwise |
| Surface hardware vs. concealed | Concealed looks better and resists tampering; it's costly and hard to service | Concealed at lobbies and high-visibility openings only |

---

## Common mistakes

⚠️ **Designing the door and ignoring the wall.** The suspended ceiling above the partition, the
adjacent glazing, and the gypsum board are all part of the opening's delay value.

⚠️ **Ignoring the frame.** The best lock in the world is bolted to a frame that may be 18-gauge
steel snapped onto drywall.

⚠️ **Specifying electrified hardware in the leaf with no power transfer.** Lesson 06.

⚠️ **Assuming "prepped for."** A door not factory-prepped for a component cannot take it
without modification that may void its label.

⚠️ **Treating the closer as somebody else's problem.** It is the component that determines
whether your access control system is connected to reality.

⚠️ **Using "door" when you mean "opening" in writing.** It reads as inexperience to everyone on
the distribution list, and it creates real ambiguity about scope in an RFI.

⚠️ **Not visiting the opening.** Everything above can be checked in twenty seconds in person
and not at all from a PDF.

---

## Junior vs. Senior

**Junior:** names the components correctly; reads a door schedule; knows a hardware set exists
and where to find it; can identify the frame type and leaf material on sight.

**Senior:** looks at an opening and immediately identifies the *governing* weakness — which is
usually the wall, the frame anchorage, the glazing, or the closer, and almost never the lock;
knows which decisions belong to the architect and which to them, and raises the architectural
ones early enough to be cheap; reviews the door schedule against the security drawings as a
diff rather than a read; and treats the hardware consultant as a design partner rather than a
downstream recipient of a device list.

---

## 🔧 Field exercise

Walk your own building. Find **five** openings: one exterior, one stairwell, one office suite
entry, one mechanical or electrical room, one glass entrance.

For each, without touching anything, record:

1. Frame type (welded or KD) and material.
2. Leaf material, and solid or glazed.
3. Hinge type, and whether hinge barrels are on the secure or unsecure side.
4. Whether a closer is present and whether the door actually latches when released.
5. Any electrified hardware, reader, or position switch you can see.
6. **Your one-sentence assessment of the governing weakness of the opening.**

Number six is the exercise. The rest is data collection.

---

## Exercises

**E1.1** For each opening, name the component most likely to govern its delay value, and say why:
- (a) A 90-minute rated hollow metal stair door in a masonry shaft wall.
- (b) A tenant suite entry: aluminum storefront, tempered glass sidelite, mortise lock.
- (c) An IT closet: solid-core wood door, KD frame, single-layer drywall partition, suspended
  ceiling continuous over the wall.
- (d) An out-swinging exterior HM door with standard butt hinges and a deadbolt.

**E1.2** A hardware set for an access-controlled office suite entry lists: 3 ball-bearing butt
hinges, cylindrical lockset, surface closer, wall stop, silencers, card reader, electric strike.
Name **three** items that are missing or wrong and explain the consequence of each.

**E1.3** Explain, in under 120 words and with no jargon, to a facilities manager who wants to
"just put a better lock on it," why their IT closet's problem is not the lock.

**E1.4** You are handed a door schedule with 240 openings and a security drawing set showing 61
card readers. Describe the procedure you would use to verify the two agree, and identify which
parts of that procedure you would automate and which you would not. Justify the boundary.

> Solutions: [`_solutions/01_door_anatomy_solutions.md`](_solutions/01_door_anatomy_solutions.md)

---

## Retrieval check

1. What is an "opening," and why is it the unit of design rather than the door?
2. Name the parts of a frame and say which one carries the security load into the wall.
3. What does a deadlatch do, and what tells you it isn't working?
4. Why does a coordinator exist, and on what kind of opening?
5. Why is a closer an access control component?
6. What is the countermeasure for exposed hinges on an out-swinging exterior door?
7. What governs the delay value of an aluminum storefront entrance?

---

## References

- DHI (Door and Hardware Institute) — *Basic Architectural Hardware* and the AHC body of
  knowledge. `[PRACTICE]` The authoritative trade source for everything in this lesson.
- ANSI/BHMA A156 series — hardware product standards, by component type. `[STANDARD][VERIFY]`
- SDI (Steel Door Institute) publications — hollow metal door and frame construction.
  `[STANDARD][VERIFY]`
- CSI MasterFormat 08 71 00 — Door Hardware; 08 11 00 — Metal Doors and Frames. `[PRACTICE]`
- Manufacturer catalogs (Allegion, ASSA ABLOY, dormakaba) — useful for *what exists*; treat
  capability claims as `[MFR]`, never as principle.

**Next:** [02 — Handing, Swing, and the Secure Side](02_handing_and_swing.md)
