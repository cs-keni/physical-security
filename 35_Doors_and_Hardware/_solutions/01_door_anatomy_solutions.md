# Solutions — 01 Door Anatomy

> Work the exercises before reading. The value is in being wrong first.

---

## E1.1 — Governing component

The habit this exercise builds: **look past the lock.** In every one of these, the lock is not
the answer.

**(a) 90-minute rated hollow metal stair door in a masonry shaft wall.**

Governing component: **the door assembly itself, and specifically its latching.** This is the
one case in the set where the opening genuinely is the strong point — masonry shaft wall, rated
HM leaf and frame, welded frame set in masonry. The delay value is real.

What governs in practice is whether the door is **latched**. A rated door that isn't latching —
because the closer is misadjusted or the strike is out of alignment — is a leaf resting in a
frame. Check the latch, not the label.

**(b) Tenant suite entry: aluminum storefront, tempered glass sidelite, mortise lock.**

Governing component: **the tempered glass sidelite.** Delay measured in seconds regardless of
the lock. The mortise lock is irrelevant to the delay value of this opening; it controls
*authorized* access only.

If delay is actually a requirement here, the conversation is about laminated glazing or
security film, and it is an architectural and budget conversation you need to start early. If
delay is *not* a requirement — and for most tenant suite entries it honestly isn't — then say
so plainly and stop specifying as though it were.

**(c) IT closet: solid-core wood door, KD frame, single-layer drywall partition, suspended
ceiling continuous over the wall.**

Governing component: **the suspended ceiling.** The wall stops at the ceiling grid. Anyone can
go over it, from an adjacent unsecured space, in under a minute, with no tools and no noise.

Second-worst: the KD frame in a single-layer drywall partition. The frame can be worked loose
from the wall.

The door is the third-best attack path and the lock is the fourth. **This is the classic IT
closet and you will find it in every building you ever walk.** The fix is deck-to-deck
partition (or a hardened ceiling barrier), then the frame, then the lock — in that order, and
the first item is architectural and expensive, which is exactly why it doesn't get done.

**(d) Out-swinging exterior HM door with standard butt hinges and a deadbolt.**

Governing component: **the exposed hinges.** Out-swinging puts the barrels on the unsecured
side. The deadbolt is doing real work on the strike side and nothing at all on the hinge side.

Fix: NRP hinges or security studs, or a continuous geared hinge. Near-zero cost delta at
design time, disproportionate cost to correct after installation.

---

## E1.2 — Three defects in the hardware set

Given set: 3 ball-bearing butt hinges, cylindrical lockset, surface closer, wall stop,
silencers, card reader, electric strike.

**Defect 1 — no door position switch.**
Consequence: the system can grant and deny access but cannot tell whether the door ever opened,
whether it closed, or whether it is standing open right now. No forced-door alarm, no
door-held-open alarm, and the audit log records intentions rather than events. At an
access-controlled opening this is not an accessory; it is the thing that makes the opening
monitored rather than merely controlled.

**Defect 2 — no request-to-exit device.**
Consequence: every legitimate departure trips a forced-door alarm. Within two weeks operations
asks for the alarm to be disabled at that door, and it is, forever. This is the mechanism by
which a correctly-specified system becomes an incorrectly-operated one, and it is caused at
design time.

**Defect 3 — silencers specified with a closer and a latching opening, and no seals.**
Silencers are the rubber bumpers in the frame stop. They are omitted on gasketed openings, and
on an access-controlled suite entry you would normally expect at minimum a smoke/sound gasket
depending on the wall rating. More importantly, the set has **no power supply, no power
transfer consideration, and no fail state stated for the electric strike.**

**Accept any three of the following as correct answers**, and note that a strong answer names
the fail state:

- No door position switch
- No request-to-exit device
- **No fail state specified for the electric strike** — the contractor orders the default
- No power supply or wiring device listed
- No verification that the existing/specified cylindrical lockset has no deadbolt function
- Wall stop specified where an overhead stop may be needed depending on adjacent wall condition
- No latch monitoring option on the strike

> The general lesson: a hardware set with a reader and a strike and nothing else is the
> signature of a device list rather than a design. The monitoring and the fail state are the
> engineering content.

---

## E1.3 — Explaining it to a facilities manager

Model answer (117 words):

> The lock isn't the way in. Your closet wall is drywall that stops at the ceiling tiles —
> there's an open gap above it running into the corridor. Someone can stand on a chair, lift a
> tile, and be inside in about a minute without touching the door. The frame is also a
> snap-on type that can be worked loose from the wall.
>
> A better lock protects the one path that's already the hardest. To actually secure the room,
> the wall needs to run up to the structural deck, and the frame needs to be the welded type.
> That's construction work, not hardware.
>
> If that's not in the budget this year, the cheapest real improvement is a door contact and a
> motion sensor inside, so you'd at least know.

**What makes it work:** no jargon, names the actual path, gives the real fix, gives a cheap
partial fix, and doesn't make the manager feel stupid for asking.

---

## E1.4 — Verifying 240 openings against 61 readers

**The procedure:**

1. **Extract** the door schedule to structured data (CSV) — door number, size, type, rating,
   hardware set, remarks. Bluebeam markup export or a table extraction from the PDF; see
   `../../12_Bluebeam/` and `../../16_Automation/`.
2. **Extract** the security drawing device list to structured data — device ID, door number,
   device type, floor, room.
3. **Normalize the door numbers.** This is where it actually breaks: `105A`, `105-A`, `105 A`,
   and `0105A` are the same opening to a human and four different keys to a script.
4. **Join on door number** and produce three reports:
   - Readers with no matching schedule row (device on a door that doesn't exist)
   - Schedule rows flagged as access-controlled with no reader
   - Rows present in both where the hardware set does not include the electrified components
     the security drawing implies
5. **Extract the hardware sets** from the spec and check each access-controlled opening's set
   for the required components: locking device, fail state, DPS, REX, power transfer where the
   device is in the leaf.
6. **Review the exception list by hand.**

**What I would automate:** steps 1–4, and the presence checks in step 5. These are mechanical,
repetitive, high-volume, and objectively decidable. A human doing 240 rows will miss things by
row 80.

**What I would not automate:** step 6, and every judgment inside it. Specifically:

- Whether an opening *should* be access-controlled. That is a risk decision.
- Whether the specified fail state is *correct* for that opening. Requires occupancy, egress
  path, and rating.
- Whether the locking device is appropriate to the construction.
- Whether a discrepancy is an error or an intentional deviation someone documented elsewhere.

**The boundary, stated as a principle:** automate the *comparison*, never the *conclusion*. A
tool that tells me "these 14 rows disagree" makes me faster. A tool that tells me "these 14
rows are fine" makes me worse, because I will believe it. This is the same rule the device
model validator follows — it reports, it never mutates (`../../16_Automation/`).

> 🧠 The senior addition: run the comparison at **every** drawing revision, not once. The
> disagreements are introduced by revisions, and the whole value of having built the tooling is
> that the second run costs nothing.
