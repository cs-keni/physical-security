# 02 — Handing, Swing, and the Secure Side

## Learning objectives

- Determine the handing of any door in the field, correctly, in under fifteen seconds.
- State the four hands (LH, RH, LHR, RHR) and the convention that produces them.
- Distinguish **handing** (a hardware-ordering property) from **secure side** (a design
  decision) and from **egress direction** (a code constraint), and explain why conflating them
  produces expensive errors.
- Place a reader, a request-to-exit device, a door position switch, and a locking device
  correctly given a door's handing and secure side.
- Explain why a handing error cannot be corrected in software, in configuration, or after
  delivery.

---

## ELI5

Doors come in left-handed and right-handed versions, like scissors. A left-handed lock will
not work on a right-handed door.

There are four versions, not two, because a door can also swing toward you or away from you.

Get it wrong and a truck delivers the wrong thing eight weeks late and it is not returnable.

---

## Why handing exists at all

Most hardware is **chiral** — it has a handedness that cannot be corrected by rotating it.

- A **latch bolt** is beveled. The bevel must face the direction the door closes.
- A **lever handle** droops toward the hinge side on some designs and away on others.
- A **closer arm** mounts on the pull side (regular arm) or the push side (parallel arm), which
  depends on swing direction.
- An **exit device** has a defined strike side and dogging orientation.
- An **electric strike** keeper faces one way.
- A **mortise lock** case has its functions arranged for one hand; some are field-reversible,
  many are not.

> **Software bridge:** handing is chirality, and the closest analogue you have is endianness.
> It's a property with exactly two states, invisible from inside the component, silently
> corrupting everything downstream if you assume the wrong one.
>
> **Where the analogy breaks:** you can byte-swap at runtime. You cannot byte-swap a
> $1,400 mortise exit device with a 10-week lead time. There is no reversibility and no
> deploy. **Handing errors are always schedule impacts.** That asymmetry — cheap to get right
> at design, ruinous to get wrong at delivery — is why the trade built a rigid convention and
> insists on it.

Modern cylindrical locksets are commonly field-reversible and this makes juniors complacent.
The things that are *not* reversible are exactly the things at security-relevant openings:
mortise locks, exit devices, electric strikes, closers, and every electrified variant of all
of them. `[MFR][VERIFY per product]`

---

## The convention

**Stand on the OUTSIDE of the door. Look at it.**

```
        hinge on your LEFT   +   swings AWAY from you   →   LH    Left Hand
        hinge on your RIGHT  +   swings AWAY from you   →   RH    Right Hand
        hinge on your LEFT   +   swings TOWARD you      →   LHR   Left Hand Reverse
        hinge on your RIGHT  +   swings TOWARD you      →   RHR   Right Hand Reverse
```

"Reverse" means the door swings toward the person standing outside. That is the whole meaning
of the word. It does not mean anything is backwards.

### Plan view of all four

```
   LH — hinge left, swings away              RH — hinge right, swings away

          I N S I D E                              I N S I D E
              ↖ swing                                  swing ↗
    ●━━━━━━━━━━┐                                    ┌━━━━━━━━━━●
   ═════════════════════                     ═════════════════════
          O U T S I D E                             O U T S I D E
             ( you )                                   ( you )


   LHR — hinge left, swings toward           RHR — hinge right, swings toward

          I N S I D E                              I N S I D E
    ●━━━━━━━━━━┐                                    ┌━━━━━━━━━━●
   ═════════════════════                     ═════════════════════
              ↙ swing                                  swing ↘
          O U T S I D E                             O U T S I D E
             ( you )                                   ( you )

   ● = hinge jamb        ━ = door leaf        ═ = wall
```

### The hard part: what is "outside"?

For an exterior door, it is obvious. For everything else, the convention is:

**Outside is the side you are secured *from* — the side the key goes in, the corridor side,
the public side, the side you approach from.**

| Opening | "Outside" is |
|---|---|
| Exterior door | The exterior |
| Office suite entry off a corridor | The corridor |
| IT closet | The corridor, not the closet |
| Stair door, floor-to-stair | The floor side `[VERIFY per project; stairwell re-entry conventions vary]` |
| Restroom | The corridor |
| Door between two secured zones | **A decision, not a fact. See below.** |

> ⚠️ **The most common handing error is not misreading left and right. It is standing on the
> wrong side.** Two competent people will produce opposite answers for the same door if they
> disagree about which side is "outside." Write the side you stood on into the field note.
> Every time.

---

## Handing is not the secure side, and neither is the swing

Three separate properties get conflated constantly. Keep them apart:

| Property | What it is | Who decides | Changeable later? |
|---|---|---|---|
| **Handing** (LH/RH/LHR/RHR) | Physical chirality of the assembly | Determined by the architecture | No — it's the built condition |
| **Swing direction** | In or out relative to a space | Architect, constrained by **code** | No, not after framing |
| **Secure side** | Which side is protected | **You** | Yes — it's a design decision |

**Swing direction is frequently a code constraint, not a preference.** Doors serving a
sufficient occupant load, and doors in certain occupancies and equipment rooms, are required to
swing in the direction of egress travel. `[CODE][VERIFY — this is an occupant-load and
occupancy-driven requirement in the applicable building and life safety codes; confirm the
adopted edition and the threshold for your project. Do not quote a number from memory.]`

**The consequence for you:** exterior and stair doors are very often **out-swinging**, which
means:

1. The hinges are exposed on the unsecured side → **NRP hinges or security studs**, always.
2. A direct-pull magnetic lock cannot mount in the head the simple way → it needs an L- or
   Z-bracket, or you choose different hardware.
3. The door leaf's face on the unsecure side is exposed to attack on the *pull* direction, and
   the stop is doing less work for you than it would on an in-swinging door.

None of that is a reason to argue for an in-swinging door. Life safety wins. It's a reason to
design the hardware to the swing you were given.

### The door between two secured zones

A door from a general office area into a data hall is secured *from* the office. A door from a
loading dock into a warehouse is secured *from* the dock. Easy.

Now: a door between two data halls of equal classification. Or a stair door where the stair is
secure from the floor *and* the floor is secure from the stair.

**These need a decision, in writing, and the decision drives everything else:**

- Which side gets the reader? (Or do both? See below.)
- Which side gets the REX?
- Which face gets the mag armature?
- Which side gets the position switch wiring?

> 🧠 **When both sides need control, you specify readers on both sides — and that is not just
> two readers.** Reader-in/reader-out changes the system's behavior: it enables occupancy
> tracking, anti-passback, and two-person-rule enforcement, and it changes what your
> request-to-exit strategy is (because there may no longer be a free-egress-by-motion side).
> It also roughly doubles the device count at that opening and adds a second wire path. That
> is an access control design decision (`../04_Access_Control/`), and this lesson is where you
> learn it starts as a *handing and sides* question, not a feature question.

---

## Where each security device goes

This is the payoff of the lesson. Given handing and secure side:

```
   PLAN VIEW — in-swinging door, secure side INSIDE

                     I N S I D E   (secure)
                     
       REX motion sensor ┐        ┌ door position switch
       (ceiling, secure  │        │ (frame head, hinge or
        side, covering   │        │  center; magnet in leaf)
        the approach)    ▼        ▼
    ●━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┐
   ═══════════════════════════════════════════
                          ▲
                   card reader
                   (unsecure side, strike-jamb
                    side, ~40-48" AFF `[CODE][VERIFY
                    per accessibility requirements]`)
   
                    O U T S I D E   (unsecure)
```

| Device | Side | Position | Why |
|---|---|---|---|
| **Card reader** | Unsecure / approach | On the **strike jamb side**, so the user can reach the lever after presenting | A reader on the hinge side forces the user to cross the door swing. Users hate it and it slows throughput. |
| **Second reader** (if in/out control) | Secure | Mirrored | Only if the design calls for controlled egress or occupancy tracking |
| **REX device** (motion sensor, or the lock's own request-to-exit switch) | Secure | Ceiling covering the approach, or integral to the hardware | It exists to tell the system "this exit was authorized" so a legitimate departure isn't logged as a forced door |
| **Door position switch (DPS)** | Either — wire it on the secure side | Frame head, magnet in the leaf top | Recessed at the head is standard; surface-mount only where you must |
| **Electric strike** | Frame, strike jamb | In the frame | Frame must have the depth and a wire path |
| **Magnetic lock** | **The side the door closes against** | Head, secure side for in-swing; bracket for out-swing | Governed by geometry, not preference |
| **Power transfer** (electric hinge / door loop) | Hinge jamb | At the hinge | Needed for anything electrified *in the leaf*. Lesson 06. |

> ⚠️ **The reader-on-the-hinge-side error.** It happens when the reader is placed on a plan
> from the drawing's geometry without checking handing. It is not a code violation and nothing
> stops it, so it gets built. Then every user at that door does an awkward two-step every
> single time, forever. Small error, permanent consequence, entirely avoidable at review.

> ⚠️ **REX on the wrong side is worse.** A REX sensor on the unsecure side shunts the alarm
> for anyone approaching from outside, which quietly converts a controlled opening into an
> uncontrolled one — and the system logs everything as normal. This is a real failure mode that
> survives commissioning because *nothing looks wrong.* Test it deliberately.

---

## The field procedure

Do this every time. It takes fifteen seconds and it never fails.

1. **Decide which side is "outside"** using the rule above, and say it out loud. If the door
   is between two secured spaces, use the side you defined as unsecure in the design and
   *write down that you did*.
2. **Stand there.**
3. **Find the hinges.** Left or right?
4. **Push the door.** Away from you = LH/RH. Toward you = LHR/RHR.
5. **Record it with the side you stood on**, e.g. `Door 210 — RHR (outside = corridor)`.

Photograph the opening from the outside with the swing visible. Do it as part of the same
motion. A photo settles every argument that follows and costs you two seconds.

> 🧠 **Never determine handing from a floor plan alone in an existing building.** The plan
> shows the design intent; the field shows what got built, plus twenty years of renovations
> that nobody redlined. On a retrofit, field-verify 100% of the openings you're touching. On
> new construction, the plan is the authority — but confirm the swing arc is actually drawn,
> because plans with doors shown as a plain rectangle and no arc are common and tell you
> nothing.

---

## Design tradeoffs

| Tradeoff | The tension | How to resolve |
|---|---|---|
| Out-swing (code-driven) vs. hinge exposure | Egress requires out-swing at many openings; out-swing exposes hinges | NRP hinges or security studs. This is not a tradeoff you get to make — it's a mitigation you owe. |
| Reader on strike side vs. wiring convenience | Strike side is right for the user; the wire path may be easier on the hinge side | User experience wins. Route the wire. |
| Single reader vs. reader in/out | In/out gives occupancy data, anti-passback, and controlled egress; costs ~2× device and wire | Drive it from the requirement (`../01_Foundations/06_requirements_engineering.md`), never from "while we're here" |
| Field-reversible hardware vs. handed hardware | Reversible reduces ordering risk; handed products are often better and cheaper | Reversible where the field condition is uncertain; handed where you've verified |
| Verifying handing in the field vs. trusting the schedule | Field verification costs hours; a wrong order costs weeks | Verify on retrofits, always. On new construction, verify the schedule against the plan. |

---

## Common mistakes

⚠️ **Standing on the wrong side.** The number one cause of handing errors and the easiest to
prevent — write down which side you stood on.

⚠️ **Assuming "reverse" means something is backwards.** It means the door swings toward the
outside. That's all.

⚠️ **Mirroring a detail drawing to "make it fit the other side."** Mirroring flips the hand.
The detail is now wrong and it looks right, which is the worst combination.

⚠️ **Ordering handed electrified hardware before field verification on a retrofit.**

⚠️ **Placing the reader from the plan geometry without checking the hand.**

⚠️ **Putting the REX on the unsecure side.** Silently disables the control.

⚠️ **Treating swing direction as an architectural preference.** It's frequently code.
`[CODE][VERIFY]`

---

## Junior vs. Senior

**Junior:** determines handing correctly in the field; knows the four hands; places readers,
REX devices, and position switches on the correct sides; knows out-swinging doors need NRP
hinges.

**Senior:** treats "which side is secure" as an explicit design decision with a written
rationale rather than an assumption; recognizes when a two-sided-control requirement is really
an occupancy-tracking or anti-passback requirement in disguise and pushes it back to
requirements; knows which hardware is field-reversible and which is a 10-week lead item, and
sequences field verification accordingly; and catches mirrored details in review, because
they're invisible to everyone else.

---

## 🔧 Field exercise

Extend the five-opening survey from lesson 01. For each opening, add:

1. Handing (LH / RH / LHR / RHR) **and the side you stood on**.
2. Swing direction relative to egress travel — does it swing the way people would run?
3. If it has a reader: is the reader on the strike side or the hinge side?
4. If it's out-swinging and exterior: are the hinges NRP or security-stud equipped? (Look at
   the pin — an NRP hinge has a set screw in the barrel that is only accessible when the door
   is open.)
5. One sentence: if you had to add access control to this opening tomorrow, what would the
   handing force you to choose?

---

## Exercises

**E2.1** For each, state the handing and justify the side you chose as "outside":
- (a) An exterior door on the north façade. Standing on the sidewalk, hinges are on your right
  and the door swings toward you.
- (b) An IT closet off a corridor. Standing in the corridor, hinges on the left, door swings
  into the closet.
- (c) A stair door. Standing on the floor side, hinges on the right, door swings into the stair.
- (d) A door between two equally-classified data halls, hinges on the east side, swinging west.

**E2.2** A design shows an in-swinging office suite entry, LH, with a card reader on the hinge
jamb, a REX motion sensor on the corridor ceiling, and a mag lock in the head on the corridor
side. Identify **every** error and state the consequence of each.

**E2.3** You are retrofitting access control onto 34 existing openings in a 1988 building. The
record drawings show all door swings; the building has been renovated three times. Write the
field-verification procedure you would hand to a technician, including exactly what they record
per opening and what they photograph. Then state which items you would *not* trust a technician
to determine and why.

**E2.4** An out-swinging exterior door must be electrically locked. Explain why a standard
direct-pull magnetic lock in the frame head does not work here, and describe two alternatives
with their tradeoffs.

**E2.5** Explain to a project manager, in under 100 words, why "we'll just flip it in the field"
is not an available answer for a mortise exit device.

> Solutions: [`_solutions/02_handing_and_swing_solutions.md`](_solutions/02_handing_and_swing_solutions.md)

---

## Retrieval check

1. State the handing convention in one sentence.
2. What does "reverse" mean?
3. What is the difference between handing, swing direction, and secure side, and who decides
   each?
4. Which side does a card reader go on, and on which jamb?
5. What goes wrong if a REX sensor is on the unsecure side?
6. Why do out-swinging doors need NRP hinges or security studs?
7. Why can't a handing error be fixed the way a configuration error can?

---

## References

- DHI — handing conventions and hardware application. `[PRACTICE]` The trade authority.
- ANSI/BHMA A156 series — product standards; individual standards state handing and
  reversibility for their product class. `[STANDARD][VERIFY]`
- Applicable building code and life safety code, egress chapters — for door swing direction
  requirements and their occupant-load thresholds. `[CODE][VERIFY — confirm the adopted
  edition for your jurisdiction; see `../10_Codes_Standards/`]`
- Manufacturer templates and installation instructions — the authority on whether a specific
  product is field-reversible. `[MFR]`

**Next:** [03 — Locking Hardware Families](03_locking_hardware_families.md)
