# Solutions — 02 Handing, Swing, and the Secure Side

---

## E2.1 — Determine the handing

Recall the convention: stand on the **outside**; hinge side + swing direction gives the hand.
"Reverse" = swings toward you.

**(a) Exterior door, north façade. On the sidewalk: hinges right, swings toward you.**

Outside = the exterior. That's unambiguous for an exterior door.
Hinges right + swings toward you → **RHR (Right Hand Reverse)**.

Note what else this tells you: the door is **out-swinging**, which is common and often required
at exterior egress doors, and which means the **hinge barrels are on the unsecured side**.
Specify NRP hinges or security studs.

**(b) IT closet off a corridor. In the corridor: hinges left, swings into the closet.**

Outside = the corridor. You are secured *from* the corridor; the key goes in from the corridor.
Hinges left + swings away from you → **LH (Left Hand)**.

**(c) Stair door, floor side: hinges right, swings into the stair.**

Outside = the floor side, under the usual convention for a door leading into the stair.
Hinges right + swings away from you → **RH (Right Hand)**.

⚠️ The real answer includes a caveat: stair doors frequently swing **into** the stair at the
level of exit discharge and **out of** the stair elsewhere, and the direction is driven by
egress travel, not by preference. Verify the swing per floor rather than assuming it's uniform
through the stack. `[CODE][VERIFY]`

**(d) Door between two equally-classified data halls, hinges east, swinging west.**

**This question cannot be answered as asked, and recognizing that is the point.**

There is no "outside" until you decide which hall is the unsecure side. Both are equally
classified, so the convention gives you nothing.

The correct response is:

1. Make the decision explicitly — pick a side as the approach side, based on operational flow
   (which direction do people normally travel?), and record it.
2. Write it into the door schedule remarks and the design narrative: *"Door 3-14: outside =
   Hall A. Handing determined from Hall A."*
3. Then the hand follows: standing in Hall A (assume Hall A is east of the door), hinges are on
   your... and here you need the geometry, which is why step 1 has to come first.

If both directions genuinely need control, you are specifying **readers on both sides**, and
that is an access control design decision with consequences for anti-passback, occupancy
tracking, and the request-to-exit strategy. Raise it as a requirements question rather than
answering it as a hardware question.

> 🧠 The general skill: notice when a question is underdetermined and say so, rather than
> producing a confident answer built on an assumption you didn't state. In practice this is
> how you avoid building the wrong thing correctly.

---

## E2.2 — Errors in the design

Given: in-swinging office suite entry, **LH**, card reader on the **hinge jamb**, REX motion
sensor on the **corridor** ceiling, mag lock in the head on the **corridor** side.

**Error 1 — card reader on the hinge jamb.**
Consequence: the user badges on the hinge side, then has to move across the door swing to reach
the lever and pull. Every user, every time, forever. Not a code issue, so nothing catches it;
it just makes the building slightly worse permanently. Move it to the strike jamb side.

**Error 2 — REX motion sensor on the corridor (unsecure) side.**
Consequence: **this is the serious one.** The REX exists to shunt the door alarm for authorized
departures from the secure side. Mounted on the corridor side it shunts the alarm for anyone
*approaching from outside* — which means the door can be opened from the corridor with no
credential and the system logs nothing abnormal. The opening is functionally uncontrolled and
the logs say it is fine. Move it to the secure side, covering the interior approach.

**Error 3 — mag lock mounted in the head on the corridor side, on an in-swinging door.**
Consequence: geometry failure. On an in-swinging door (swinging into the suite), the door
closes against the stop on the **corridor** side... which means the leaf face presented at the
closed position is toward the corridor, and a head-mounted magnet on the corridor side is on
the correct side geometrically — **but it is now mounted on the unsecured side**, where the
magnet body, its wiring, and its mounting screws are accessible to anyone in the corridor.

The mag and its wiring belong on the secure side. On an in-swinging door with the secure side
inside, that means the door must close against a stop such that the armature and magnet meet on
the secure face — which for this handing means reconsidering the device entirely, not just
relocating it.

**Error 4 (the one behind the other three) — a mag lock was chosen at all.**
This is an office suite entry with a frame and a normal door. It can take an electrified
lockset or an electric strike, both of which provide mechanical egress via the inside lever and
neither of which requires the sensor-release subsystem this design now needs. The mag lock adds
a REX, a manual release button, a hardwired fire alarm interface, signage, and a permanent
testing obligation, in exchange for easier installation. `[CODE][VERIFY]`

**Error 5 — no manual release device, no signage, no fire alarm interface shown.**
A magnetically locked door in the egress path needs all of them. Their absence is not an
oversight in draftsmanship; it means the arrangement as drawn is not one that can be built.

**Full credit answer names errors 2 and 4.** Error 2 because it silently defeats the control;
error 4 because it is the root cause of 3, 5, and most of the project's code exposure.

---

## E2.3 — Field verification procedure for 34 retrofit openings

**What the technician records, per opening:**

| Field | Notes |
|---|---|
| Opening ID | Match to the record drawing number; flag if the number is absent or ambiguous |
| Handing | LH / RH / LHR / RHR — **plus the side they stood on**, in words |
| Swing | In or out, relative to the named space |
| Leaf material and construction | HM / wood / aluminum / glass; solid or glazed |
| Leaf dimensions | Width × height × thickness, measured, not estimated |
| Frame type | Welded / KD; material; approximate throat depth |
| Frame depth at the strike jamb | Measured — determines whether a strike will fit |
| Hinge type and count | Butt / continuous / pivot; NRP present? |
| Existing lock type | Cylindrical / mortise / exit device / other; **deadbolt present?** |
| Existing hardware condition | Does the door latch when released from 30°? |
| Closer | Present? Type? Functioning? |
| Rating label | Present on the leaf edge and frame? Transcribe it verbatim. Photograph it. |
| Existing electrification | Any wire, any device, any abandoned conduit |
| Path for wire | Accessible ceiling? Conduit? Slab-on-grade? |
| Obstructions | Adjacent glazing, sidelites, transoms, wall condition |

**Photographs, per opening (mandatory, not optional):**

1. Full opening from the outside, swing visible, with the opening number legible in frame
2. Full opening from the inside
3. Hinge edge, close
4. Strike jamb and existing strike, close
5. Rating label, if any, legible
6. Head of the frame

**What I would not trust a technician to determine, and why:**

- **The rating.** Transcribe and photograph the label; do not interpret it. Whether a label is
  still valid depends on modifications made since, which is an engineering and code judgment.
- **Whether the opening is in the means of egress.** That comes from the life safety plan, not
  from looking at it.
- **Which side is "secure."** That's my design decision; the technician records the side they
  stood on so I can convert.
- **Whether the frame will take an electric strike.** They measure depth; I decide.
- **Whether the existing lock is "fine."** They report deadbolt present/absent and whether it
  latches; the suitability call is mine.
- **Anything about code compliance.** Not their scope, not their liability, not their training.

**The instruction that saves the project:** *"If anything doesn't match the record drawing,
photograph it and move on. Do not resolve the discrepancy in the field."* A technician who
"corrects" a field note to match the drawing has destroyed the only reason the survey existed.

---

## E2.4 — Out-swinging exterior door, electrically locked

**Why a standard direct-pull magnetic lock in the frame head doesn't work:**

A direct-pull mag holds by clamping the armature on the leaf face flat against the magnet on
the frame head. That geometry requires the leaf to close *against* the plane the magnet is
mounted in. On an in-swinging door, the leaf closes into the frame toward the outside and the
magnet mounts on the inside face of the head — clean, flat, direct.

On an **out-swinging** door, the leaf closes toward the *outside*, so there is no interior head
surface for the leaf face to meet. Mounting a magnet flat in the head puts it in a plane the
door never contacts. The mag has nothing to grab.

**Alternative 1 — L-bracket / Z-bracket mounting.**
A fabricated bracket carries the armature out from the leaf so it meets a magnet mounted on the
frame face or soffit in the correct plane.

| Pro | Con |
|---|---|
| Keeps the mag lock solution, familiar to installers | The bracket is now the weakest element and it's exposed on the unsecured side |
| Available as a manufactured kit `[MFR]` | Adds an alignment-sensitive assembly to a door that sees weather and abuse |
| | Does not remove any of the sensor-release, signage, or FA obligations |

**Alternative 2 — electrified exit device or electrified lockset.**
Change the device family rather than fight the geometry.

| Pro | Con |
|---|---|
| **Mechanical egress** via the bar or lever — removes the entire sensor-release subsystem | Requires power transfer into the leaf (electric hinge or door loop) |
| Better attack resistance than a mag on an exterior opening | Higher hardware cost, longer lead time |
| Latch monitoring available | Requires the leaf to be prepped, or replaced |
| Compatible with a rated opening if fire exit hardware | |

**Recommendation, and say it plainly:** alternative 2. An out-swinging exterior door is exposed
weather, exposed hinges, and exposed hardware. Putting a bracket-mounted magnet on it — a
device with no mechanical egress, mounted on an assembly that must stay in alignment through
temperature cycling and slamming — is choosing the harder problem twice. The reason people do
it anyway is that alternative 1 avoids running power into the leaf, and that is not a good
enough reason.

---

## E2.5 — "We'll just flip it in the field"

Model answer (94 words):

> Cylindrical locks are usually field-reversible. Mortise exit devices are not. The chassis is
> machined for one hand — the latch, the dogging mechanism, and the strike interface are all
> built into a case that can't be turned around. It isn't a setting.
>
> If the wrong hand shows up on site, it goes back and we wait for the correct one. On this
> product that's roughly a ten-week lead time, and it's a non-returnable special order because
> it was made to our submittal.
>
> That's why I'm field-verifying handing before the submittal goes out, not after.

**What makes it work:** it doesn't say "no," it explains the mechanism in one sentence, it
converts the answer into a schedule number the PM actually cares about, and it closes by
telling them what you're already doing about it.
