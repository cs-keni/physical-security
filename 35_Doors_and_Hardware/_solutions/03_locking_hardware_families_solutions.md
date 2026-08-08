# Solutions — 03 Locking Hardware Families

---

## E3.1 — Device selection

**(a) 90-minute rated stair door, panic hardware required, credentialed re-entry.**

**Fire exit hardware with electrified trim, fail secure.**

Panic hardware is required, and on a rated opening that means *fire exit hardware*
specifically — always latching, no dogging. `[CODE][VERIFY]` Electrified trim controls the
outside lever for credentialed re-entry while the latch itself stays mechanical, which keeps
current draw low and keeps the self-latching behavior the fire rating depends on. Egress is by
pushing the bar and is unaffected by anything electrical.

Add: **stairway re-entry release on fire alarm** (lesson 04), latch monitoring, DPS, power
transfer, and a reader on the stair side.

**(b) Existing office suite entry, mortise lock with deadbolt, badge access next month,
minimal construction.**

**Electric strike — but only after resolving the deadbolt.**

The strike is the obvious retrofit answer: no leaf prep, no power transfer, fast. But an
electric strike releases the *latch*. If the existing mortise lock has a deadbolt that gets
thrown, the badge stops working whenever someone throws it, intermittently, in a way nobody
will connect to the cause.

Two acceptable resolutions:
1. Replace the mortise cylinder/lock with a non-deadbolting function, or
2. Replace the lock with an **electrified mortise lockset** — better monitoring, but now you
   need power transfer and you have lost the "minimal construction" advantage.

Given the stated constraint, go with (1) plus the strike, and specify latch monitoring.

**(c) All-glass lobby entrance, aluminum frame, no place for a lock case.**

**Magnetic lock** — this is the case where it's genuinely correct.

There is nowhere to put a lock case and no leaf to prep. Accept the consequence and design the
whole arrangement: sensor release on the egress side, a manual release device in the egress
path that directly interrupts power, release on power loss, hardwired fire alarm release,
required signage, bond sensor for status, and the recurring test obligation in the O&M
handover. `[CODE][VERIFY]`

This is the answer to give when someone asks "when *is* a mag lock right?" — you should be able
to name this case immediately, because being able to name it is what makes your objection at
the other 21 openings credible.

**(d) New data hall door, highest consequence tier on the project.**

**Electrified mortise lockset, fail secure, with latch bolt monitoring, deadbolt monitoring if
the function includes one, and integral request-to-exit.**

Reasoning: highest consequence means you want the *state* of the opening, not just its
position. Integral latch monitoring tells you it is actually secured; the integral REX switch
is more trustworthy than a ceiling motion sensor because it corresponds to the physical act of
leaving and cannot be triggered from the wrong side.

Fail secure because a power event must not open the highest-consequence space, and because
egress is mechanical via the inside lever so nothing is traded away.

Add, beyond the lock: DPS as a second independent state signal, alarm-linked camera at the
opening, and — this is the senior part — check what happens to this door when the controller
loses the server (lesson 04, failure mode 4).

**(e) 400 interior offices, low consequence, tight budget, owner wants an audit trail.**

**Wireless or offline electronic locksets.**

At 400 low-consequence openings, wiring is the dominant cost and it dwarfs the hardware. Offline
or wireless locks slash install cost, provide the credential-level audit trail the owner asked
for, and are appropriate to the consequence tier.

State the tradeoffs honestly rather than selling it as free:
- **Battery maintenance** becomes a permanent operational program across 400 doors. Someone has
  to own it. If nobody owns it, the system degrades silently over three years.
- **Real-time control is weaker.** Offline locks may take hours or days to receive a credential
  revocation, depending on the update mechanism. Ask the owner directly: *"if you fire someone
  at 2 p.m., when does their badge stop working at these doors?"* If the honest answer is
  unacceptable, the tier is wrong and so is the technology.
- **No real-time alarms** at most of these openings.

That last question is the one that distinguishes a recommendation from a product pitch.

---

## E3.2 — 🧮 Power supply, battery, and conductor

Given, 24 VDC:

| Load | Qty | Standby A each | Peak A each |
|---|---|---|---|
| Electrified lockset | 14 | 0.28 | 0.28 |
| Electric strike | 4 | 0.22 | 0.22 |
| ELR exit device | 2 | 0.25 | 2.80 |

### (a) Currents and supply

```
   Standby:  14(0.28) + 4(0.22) + 2(0.25)
           =   3.92   +   0.88  +  0.50   =  5.30 A

   Peak:     14(0.28) + 4(0.22) + 2(2.80)
           =   3.92   +   0.88  +  5.60   = 10.40 A

   Design current = max(5.30, 10.40) = 10.40 A
   Supply at 25% headroom = 10.40 × 1.25 = 13.00 A CONTINUOUS
```

**Answer: specify a supply rated ≥ 13.0 A continuous.**

Two notes that belong in the submittal review:

- A supply advertised as "13 A" may be 13 A *peak*. Verify the **continuous** rating.
- Battery charging current is **additional** and is not in this number. Add it per the
  datasheet. `[MFR][VERIFY]`
- The peak assumes both ELR devices could retract simultaneously. If you can demonstrate they
  cannot, you may design to a lower peak — but "they probably won't" is not a demonstration.
  Simultaneous retraction happens at shift change and during a drill.

### (b) Battery for 4-hour standby

```
   Ah_raw   = 5.30 A × 4 h = 21.20 Ah
   Ah_sized = 21.20 × 1.25 (discharge derate) × 1.25 (aging) = 33.13 Ah
```

**Answer: 33.13 Ah minimum; specify the next standard size up.**

`[CODE][VERIFY]` The **4 hours** is the assumption in the problem, not a requirement. The
required standby duration comes from the applicable standard and the AHJ. Sizing a battery
correctly against the wrong duration is still wrong.

Note that standby current, not peak, drives the battery — the ELR devices draw their 2.8 A for
a fraction of a second at a time, so their contribution to amp-hours is negligible while their
contribution to the *supply rating* dominates. **Different question, different governing
number.** Getting these two backwards is the most common sizing error.

### (c) Conductor at 200 ft, 2.8 A

| Conductor | Drop | Voltage at device |
|---|---|---|
| 18 AWG | 8.90 V | **15.10 V** ❌ |
| 16 AWG | 5.59 V | **18.41 V** ❌ |
| 14 AWG | 3.52 V | **20.48 V** ❌ (below a 21 V floor) |
| 12 AWG | 2.21 V | **21.79 V** ✅ |

**Answer: 12 AWG**, assuming a 21 V minimum operating voltage.

**What I would verify first, before specifying anything:**

1. **The device's actual minimum operating voltage.** The 21 V floor used above is an
   assumption. If the device needs 22 V, 12 AWG is marginal too.
2. **The inrush current and its duration.** Many ELR devices draw far more than their rated
   retraction current for the first few hundred milliseconds. That transient is what actually
   determines whether the latch pulls. `[MFR][VERIFY]`
3. **The actual routed length**, not the plan distance. Conduit runs go up, over, and around.
   200 ft on a plan is often 260 ft of wire.
4. Whether a **local power supply** closer to the door is the better answer than a heavier
   conductor — frequently it is, and it also improves the failure domain.

### (d) "Would a larger power supply fix it?"

**No.** Say it plainly and then explain.

Voltage drop is `V = I × R`, where R is a property of the **conductor and its length**. The
supply sets the voltage at one end; the conductor decides how much of it survives to the other
end. A supply with more *current capacity* at the same output voltage delivers the same voltage
at the load, because the drop is unchanged.

Three things that actually fix it:

1. **A larger conductor** — reduces R. (Specified above.)
2. **A shorter run** — relocate the power supply closer to the load. Often cheapest, and it
   shrinks the blast radius of a supply failure.
3. **A higher supply voltage**, *if and only if* the device tolerates it and the supply is
   adjustable — you are then paying the same drop out of a bigger budget. Verify the device's
   maximum. `[MFR][VERIFY]`

> The one-sentence version for the meeting: *"The supply isn't running out of current, the wire
> is eating the volts. More amps on the shelf doesn't put volts back on the door."*

---

## E3.3 — "Door 214 sometimes doesn't unlock, mostly in the afternoon"

The clues, before you check anything: **intermittent**, **time-correlated**, **valid grant
logged**, **ELR device**, **180 ft run**. Three of those five point at electrical, and the
"valid grant logged" rules out most of the software stack immediately — the controller did its
job and told the door to open.

**Check, in order:**

**1. Conductor gauge and actual routed run length to the device.**
Rules in/out: the primary hypothesis. Compute the voltage at the device at the ELR's inrush
current, not its steady-state current. If it lands under the device's minimum, you're done
investigating and the fix is copper or a closer supply.

**2. Measured voltage at the device, at rest and during a retraction attempt.**
Rules in/out: confirms hypothesis 1 empirically. Measure *during* the event — a resting
measurement will look fine, which is exactly why this fault survives so long. This single
measurement resolves most of these calls.

**3. Power supply loading and battery condition.**
Rules in/out: whether the supply is sagging under aggregate load rather than the run being at
fault. If other loads on the same supply peak in the afternoon — more traffic, more retractions
— that explains the time correlation without the conductor being wrong. Also check whether the
supply is simultaneously charging a battery.

**4. Ambient temperature at the device and along the run.**
Rules in/out: the afternoon correlation. Conductor resistance rises with temperature, and an
afternoon-warm run in a plenum or an exterior wall drops more voltage than a morning-cool one.
This is frequently the piece that turns "sometimes" into "of course."

**5. Mechanical binding of the latch and the door alignment.**
Rules in/out: the non-electrical explanation. A door under compression from a misadjusted
closer, a settled frame, or thermal expansion in an exterior wall makes the latch harder to
retract, which raises the current required, which interacts with everything above. Afternoon
sun on an exterior door is a real mechanism.

**What I would not check first:** credentials, firmware, the reader, the controller
configuration, or the head-end software. The log already told us the controller granted access.
The failure is downstream of the decision.

> 🧠 The general diagnostic principle: **intermittent + temperature-correlated + load-correlated
> = physical layer.** Software fails deterministically. If the same input produces different
> outputs depending on the time of day, you are looking at physics, not logic.

---

## E3.4 — Review comment on 22 mag locks out of 61 openings

Model comment:

> **General comment — locking device selection.**
>
> The set shows magnetic locks at 22 of 61 access-controlled openings (36%). Magnetic locks are
> the only locking family with no mechanical egress: each one requires a sensor release on the
> egress side, a manual release device that directly interrupts power independent of the
> controller, automatic release on power loss and on fire alarm, and prescribed signage — plus
> a recurring test obligation that transfers to the owner at handover. `[CODE][VERIFY]`
>
> That arrangement is appropriate where the opening cannot accept a lock case — the all-glass
> lobby entrances at 1-01 and 1-02 are legitimate examples and I am not questioning those.
>
> **Request:** for each of the remaining 20 openings, either
> (a) provide a one-line justification for why an electrified lockset or electric strike is not
> feasible at that opening, or
> (b) revise to an electrified lockset (fail secure, latch monitoring) or an electric strike.
>
> Openings where the existing/specified door and frame appear capable of accepting a lock case
> should default to (b).
>
> **Also required at every opening that remains a magnetic lock:** manual release device,
> signage, hardwired fire alarm release (not an ACS software integration), bond status
> monitoring, and inclusion in the O&M testing schedule. None of these are currently shown.
>
> Happy to walk the openings together if that's faster than a written response.

**What makes it a good review comment:**

- It concedes the legitimate cases *first* and by name. This is not politeness; it is what makes
  the rest of the comment land as engineering rather than as a preference.
- It asks for a justification or a revision — the responder can choose, which makes compliance
  cheap.
- It states the specific missing components, so "we'll add what's needed" can't be a
  non-answer.
- It offers a walk-through. Most of these get resolved in twenty minutes in person.

---

## E3.5 — DPS vs. latch monitoring, for an owner

Model answer (118 words):

> Two different sensors that answer two different questions.
>
> A door position switch tells you the door is *shut*. Latch monitoring tells you the bolt
> actually went into the frame.
>
> Those come apart more often than you'd think. If a strike drifts a few millimetres out of
> alignment, the door rests closed against the frame with the latch riding on the outside of
> the strike. The position switch says "closed." The audit log says "secure." A light pull
> opens it, and nothing anywhere tells you.
>
> At the vault anteroom, "secure" needs to mean secure, so I'm specifying latch monitoring
> there. At the supply closet, knowing the door is shut is enough, and the extra cost isn't
> buying you anything you'd act on.

**What makes it work:** it names the failure concretely, it explains why the cheap sensor lies,
and it justifies *both* decisions — including the one where the answer is "don't spend the
money." Owners trust an engineer who tells them where not to spend.
