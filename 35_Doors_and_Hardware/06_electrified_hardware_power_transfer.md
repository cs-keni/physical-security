# 06 — Electrified Hardware and Power Transfer

## Learning objectives

- Explain why getting power into a moving door leaf is a distinct engineering problem, and name
  the four methods of doing it.
- Budget the **conductor count** for an opening before selecting a transfer device, and specify
  spares as a matter of routine.
- 🧮 Account for the transfer device's conductor gauge in a voltage-drop calculation, and
  recognize that a correct home run can still fail at the last six feet.
- Identify the failure modes specific to a transfer — flex fatigue, pinch, water ingress — and
  design against them.
- Explain why door prep is a submittal-stage decision made at the factory, not a field decision,
  and what happens when that is ignored on a rated opening.
- Catch a missing power transfer in a drawing review, which is the single most common omission
  in a security drawing set.

---

## ELI5

If the lock is *in the door*, the electricity has to get *into the door*.

The door moves. The wall doesn't. So somewhere there has to be a wire that bends, thousands of
times a year, forever, without breaking.

There are four ways to do that. Pick one, count how many wires you need through it, and add
spares — because adding a wire later means taking the door apart.

---

## Why this is its own problem

Lesson 03 sorted the locking families by whether they need power in the leaf:

| Device | Lives in | Needs a transfer? |
|---|---|---|
| Electric strike | Frame | **No** |
| Magnetic lock | Frame (armature on leaf, unpowered) | **No** |
| Electrified lockset | **Leaf** | **Yes** |
| Electrified exit device | **Leaf** | **Yes** |
| Door position switch | Frame (magnet in leaf, unpowered) | No |

So the moment you choose an electrified lockset or exit device — which lesson 03 recommends for
most openings — you have committed to a transfer. It is not an accessory to that decision; it
*is* part of that decision, and it belongs in the same sentence.

> **Software bridge:** this is the physical-layer version of forgetting that your service needs
> a network route. The application is written, the config is correct, the credentials are
> valid — and there is no path.
>
> **Where the analogy breaks:** you can add a route in thirty seconds. Adding a conductor to an
> installed opening means pulling the door, machining it, and possibly voiding its fire label.
> The cost asymmetry between deciding this correctly at submittal and discovering it at
> installation is roughly three orders of magnitude.

---

## The four methods

### 1. Electrified transfer hinge (ETH)

A butt hinge with conductors run through the barrel, concealed. Replaces one hinge in the set —
conventionally the **top** hinge (or the middle one on a 3-hinge door, depending on the
manufacturer's guidance).

| | |
|---|---|
| **Conductor count** | Commonly 4, 8, or 10 `[MFR][VERIFY]` |
| **Gauge** | Small — commonly 24 AWG `[MFR][VERIFY]`. **This matters. See the calculation.** |
| **Concealment** | Fully concealed when the door is closed |
| **Prep required** | Hinge prep already exists; a wire raceway must be routed in the leaf and frame |
| **Best for** | Most new-construction electrified openings |

### 2. Electric power transfer (EPT)

A dedicated device mortised into the frame and the leaf edge, with a short armored flexible loop
that lives in the gap and is hidden when the door is closed.

| | |
|---|---|
| **Conductor count** | Higher than a hinge — often 8–12+, and heavier gauge available `[MFR][VERIFY]` |
| **Gauge** | Larger conductors available — **this is why you choose it for ELR devices** |
| **Concealment** | Concealed when closed; the loop is visible when the door is open |
| **Prep required** | Mortise prep in **both** the frame and the leaf edge |
| **Best for** | High conductor count, high current, exit devices with electric latch retraction |

### 3. Door loop / door cord

A surface-mounted armored flexible loop running from the frame to the leaf.

| | |
|---|---|
| **Conductor count** | Whatever you route through it |
| **Concealment** | **None.** It is visible, always. |
| **Prep required** | Surface mounting only |
| **Best for** | Retrofit where no prep is possible, and back-of-house openings |
| **Against it** | Ugly; exposed to abuse and vandalism; a snag hazard; collects damage on high-traffic doors; unacceptable on an exterior opening (water) or a public-facing one (appearance) |

### 4. Continuous hinge with an integrated raceway

A geared continuous hinge with a wire channel. Combines the durability advantage of a continuous
hinge (lesson 01) with the transfer function.

Good choice on high-cycle, heavy, or abused doors — which is often exactly where you also want
the continuous hinge for its own sake.

### The fifth option: don't transfer at all

**Wireless or offline battery-powered locks** move the power source into the leaf and eliminate
the problem. That is a real answer, with the real costs lesson 03 named: battery maintenance
across the whole population, weaker real-time control, and no live alarms.

At a handful of openings this is a dodge. Across four hundred low-consequence interior openings
it is the correct engineering answer, and the transfer problem is one of the reasons why.

---

## Budget the conductors first

**The governing constraint is conductor count, and you must know it before you pick a device.**
Count the functions, then count the conductors each one needs.

```
   TYPICAL ELECTRIFIED MORTISE LOCKSET, FULLY MONITORED

   Function                            Conductors
   ─────────────────────────────────   ──────────
   Lock power (solenoid/motor)              2
   Latch bolt monitoring                    2
   Request-to-exit (lever switch)           2
   Deadbolt monitoring (if the function
     includes one)                          2
                                       ──────────
   Subtotal                                 8
   Spares (minimum)                         2
                                       ──────────
   SPECIFY                                 10-conductor transfer
```

**Always specify spares. Minimum two.** The cost delta between an 8-conductor and a
10-conductor hinge is small and one-time. The cost of needing a ninth conductor after
installation is a door removal.

Things that consume the spares later, all of which are normal:

- Someone adds a second reader for controlled egress
- The lock function changes during submittal review and now includes deadbolt monitoring
- A conductor is damaged during installation — **this happens, and it is the single most
  common reason a spare gets used**
- A conductor fails from flex fatigue in year seven

> 🧠 **The rule: count the functions, add two, round up to the next available device.** If
> you're on the fence between the 8-conductor and the 10-conductor hinge, take the 10. Nobody
> has ever regretted the spare conductors.

---

## 🧮 The calculation everyone skips: drop *through the transfer*

Lesson 03 ended with an ELR exit device drawing 2.8 A at 200 ft, where 12 AWG was the smallest
conductor that kept the device above a 21 V floor:

```
   200 ft, 12 AWG, 2.8 A  →  drop 2.21 V  →  21.79 V at the leaf   ✅
```

That calculation stopped at the frame. **The circuit doesn't.** It continues through the
transfer device's own conductors — which are small — and then through the leaf to the lock.

Call it 6 feet of 24 AWG through the hinge and along the raceway:

```
   Transfer: 6 ft, 24 AWG, 2.8 A  →  drop 1.07 V
```

Now add them:

| Segment | Conductor | Drop |
|---|---|---|
| Home run, panel → frame | 200 ft, 12 AWG | 2.21 V |
| Transfer + leaf run | 6 ft, 24 AWG | 1.07 V |
| **Total** | | **3.28 V** |
| **At the device** | | **20.72 V** ❌ |

**Six feet of small wire ate more than a third of what two hundred feet of properly-sized wire
cost you, and it pushed the opening back under the floor it had just cleared.**

Compare the same transfer with a quiet lockset:

| Load | Transfer drop, 6 ft 24 AWG |
|---|---|
| Lockset, 0.30 A | **0.115 V** — irrelevant |
| ELR exit device, 2.8 A | **1.073 V** — decisive |

**The lesson:** the transfer's gauge is negligible for low-current devices and governing for
high-current ones. This is why an **EPT with heavier conductors** is the right transfer for an
electric-latch-retraction exit device and a 24 AWG hinge is fine for a lockset. It is not a
preference; it falls out of the arithmetic.

**And remember lesson 03's warning:** real ELR devices often draw a much larger *inrush* for a
few hundred milliseconds than their steady-state retraction current. Run this calculation at the
inrush figure, not the running figure. `[MFR][VERIFY inrush, duration, and minimum operating
voltage.]`

```
   The complete circuit — draw it this way every time

   [Power supply] ──── home run ────►[frame]──transfer──►[leaf]──raceway──►[lock]
        24.0 V          200 ft            6 ft, 24 AWG        (included above)
                        12 AWG
                      −2.21 V           −1.07 V
                                                            = 20.72 V at the lock

   Everyone computes the first arrow. The failure lives in the second one.
```

Calculators: [`../28_Calculators/psec/power.py`](../28_Calculators/psec/power.py) —
`voltage_drop_v`, `voltage_at_load_v`, `smallest_awg_for_run`. **Sum the segments by hand
first.**

---

## Failure modes specific to a transfer

**1. Flex fatigue — the dominant one.**
A conductor that bends every cycle work-hardens and eventually fractures, usually inside the
insulation where nothing is visible. A moderately busy office door sees tens of thousands of
cycles a year; a lobby or stair door can see far more.

Design against it:
- Use a transfer product rated for the cycle count, and get the number from the datasheet rather
  than assuming. `[MFR][VERIFY]`
- Specify **stranded** conductors, never solid, in any flexing segment.
- Specify **spares**, so a fractured conductor is a re-termination rather than a door removal.
- On genuinely high-cycle openings, prefer a continuous hinge with a raceway or an EPT over a
  small hinge.

**2. Pinch and crush at installation.**
The raceway routing gets closed up with a conductor sitting where it shouldn't be. The symptom
is an intermittent fault that appears weeks later as the insulation abrades through. This is
what the pre-installation meeting and the installer's mockup are for.

**3. Water ingress on exterior openings.**
A door loop on an exterior door is a wick. Even concealed transfers on exterior openings need
the manufacturer's exterior-rated variant and attention to the drainage path. `[MFR][VERIFY]`

**4. The transfer that was never installed.**
Covered below, because it deserves its own section.

---

## Prep is a submittal decision, not a field decision

**Who machines the door:** the door manufacturer, at the factory, per the approved submittal.

**Why this is non-negotiable on a rated opening:** field-modifying a fire door beyond its listed
preparations voids its label (lesson 07). An installer with a hole saw and good intentions can
destroy a 90-minute rating in four minutes, and the label will still be sitting there on the
hinge edge saying otherwise. `[CODE][VERIFY]`

**What this means for your calendar:** the transfer decision has to be made *before the door
order goes in*, which is early — often earlier than the security design feels finished. The
practical consequence:

```
   The sequence that works                  The sequence that fails
   ───────────────────────                  ───────────────────────
   Security intent defined                  Doors ordered
   Hardware sets written                    Security design "finalized"
   Transfer + conductor count fixed         Transfer discovered missing
   Submittal reviewed and approved          Surface door loop installed as a
   Doors ordered WITH prep                    field fix, on a rated opening
   Doors arrive ready                       Label voided; inspector catches it
                                              or, worse, doesn't
```

> ⚠️ **The surface door loop as a field fix is the tell.** When you walk a finished building and
> see armored loops on doors that clearly should have had concealed transfers, you are looking
> at a design omission that was patched in the field. On a rated opening, you are also probably
> looking at a voided label.

---

## Catching it in review

**A missing power transfer is the single most common omission in a security drawing set.** It
happens because the transfer is invisible in the way people review drawings: the reader is on
the plan, the lock is in the hardware set, the panel is on the riser, and the transfer belongs
to none of those views.

**The review check, and it takes one pass:**

> For every opening with an electrified device **in the leaf** (electrified lockset, electrified
> exit device, electrified trim), confirm: (a) a transfer device is specified, (b) its conductor
> count meets or exceeds the function budget plus spares, and (c) its conductor gauge is
> adequate at the device's peak current.

This is exactly the kind of check the device data model supports
(`../16_Automation/data_model/`): the device register knows which openings have leaf-mounted
electrified hardware, so "leaf-mounted device with no transfer record" is a validation rule, not
a manual sweep. **Automate the flag; keep the judgment.**

---

## Design tradeoffs

| Tradeoff | The tension | How to resolve |
|---|---|---|
| Concealed transfer vs. door loop | Concealed looks right and survives; the loop needs no prep | Concealed everywhere it's feasible; loop only in retrofit back-of-house |
| Hinge vs. EPT | The hinge is simpler and needs less prep; the EPT carries more conductors and heavier gauge | Hinge for locksets; EPT for ELR exit devices and high conductor counts |
| More conductors vs. cost | Spares cost pennies now and a door removal later | Always add two. This is not a real tradeoff. |
| Wired transfer vs. wireless lock | Wireless removes the problem and the wiring cost | Consequence-tier it. Wireless at breadth, wired at anything that matters. |
| Early transfer decision vs. design maturity | The door order forces the decision before the design feels done | Fix the conductor budget early even if the device model is still moving; conductor count is stable across most product changes |

---

## Common mistakes

⚠️ **No transfer specified at all.** The perennial. Costs weeks when caught at installation.

⚠️ **Too few conductors.** Counted lock power and forgot latch monitoring and REX.

⚠️ **No spares.** One conductor damaged during installation and the door comes back off.

⚠️ **Ignoring the transfer's gauge on a high-current device.** The home run calculation was
right and the opening still fails.

⚠️ **Running the voltage-drop calculation at running current instead of inrush.**

⚠️ **Door loop on an exterior opening.** Water.

⚠️ **Field-prepping a rated door.** Voids the label; see lesson 07.

⚠️ **Solid conductors in a flexing segment.**

⚠️ **Making the transfer decision after the doors are ordered.**

---

## Junior vs. Senior

**Junior:** knows which devices need a transfer and which don't; specifies a transfer with an
adequate conductor count including spares; knows the prep happens at the factory.

**Senior:** budgets conductors from the function list before choosing a product; carries the
voltage-drop calculation through the transfer segment and catches the openings where a correct
home run still fails; chooses EPT over hinge on current grounds rather than by habit; drives the
transfer decision to happen before the door order and says so in the schedule conversation; and
reviews for missing transfers as a deliberate pass, because nobody else's review will catch it.

---

## 🔧 Field exercise

Find three openings with electrified hardware in the leaf. For each:

1. **Find the transfer.** Open the door and look at the hinge edge and the hinges. A concealed
   transfer is nearly invisible; look for a hinge that differs from the others in the set, or a
   small armored loop in the gap near the hinge edge.
2. If it's a **surface door loop**, note it — and note whether the opening has a fire label.
3. Look for **wear**: abrasion on the loop, a hinge that binds, a raceway cover that doesn't
   sit flush.
4. Estimate the daily cycle count by watching it for five minutes at a busy time and
   extrapolating. Then ask whether the transfer product you'd have specified is rated for it.

---

## Exercises

**E6.1** For each opening, state the transfer method you would specify and the conductor count,
showing your budget:
- (a) Electrified mortise lockset with latch monitoring and integral REX, interior office suite.
- (b) Fire exit hardware with electric latch retraction on a 90-minute stair door.
- (c) Retrofit onto an existing solid-core wood door, unrated, back-of-house corridor, where
  the door cannot be removed for machining.
- (d) Electrified lockset with latch monitoring, REX, and deadbolt monitoring at a data hall
  door, plus provision for a second reader to be added later.

**E6.2** 🧮 An ELR exit device draws 3.2 A during retraction and sits 175 ft from the power
supply. The transfer path is 5 ft of 24 AWG. Supply is 24.0 VDC; assume a 21.0 V minimum at the
device.
- (a) Compute the drop on the home run for 18, 14, and 12 AWG, and the drop through the transfer.
- (b) Which home run conductor works, accounting for the transfer?
- (c) The manufacturer's data says inrush is 8 A for 250 ms. Recompute. What changes?
- (d) State two design changes that fix the problem without increasing the home run gauge.

**E6.3** You are reviewing a 61-opening security drawing set. 34 openings have electrified
locksets and 6 have electrified exit devices. The hardware sets list transfer hinges at 22
openings and nothing at the rest. Write the review comment, and describe the check you would run
against the device register to produce the exception list.

**E6.4** A contractor proposes surface-mounted armored door loops at nine openings, noting the
doors are already on site and were ordered without transfer prep. Four of the nine openings are
90-minute rated. Write your response.

**E6.5** Explain to a project manager, in under 120 words, why the power transfer decision has
to be made before the door order and cannot wait for the security design to be finalized.

> Solutions: [`_solutions/06_electrified_hardware_power_transfer_solutions.md`](_solutions/06_electrified_hardware_power_transfer_solutions.md)

---

## Retrieval check

1. Which locking families need a power transfer and which don't?
2. Name the four transfer methods and the case each one is best for.
3. Budget the conductors for a fully monitored electrified mortise lockset.
4. Why do you specify spare conductors, and how many?
5. Why does the transfer's gauge matter for an ELR device and not for a lockset?
6. What is the dominant failure mode of a transfer, and what three things design against it?
7. Why is door prep a submittal decision rather than a field decision?
8. What does a surface door loop on a rated opening usually tell you?

---

## References

- ANSI/BHMA A156.1 (butt hinges), A156.26 (continuous hinges) — hinge product standards.
  `[STANDARD][VERIFY numbering against current editions]`
- UL 294 — Access Control System Units. `[STANDARD][VERIFY]`
- NFPA 80 — fire door assemblies; governs what may be done to a rated opening and by whom.
  `[STANDARD][VERIFY]`
- Manufacturer catalogs and templates — the authority on conductor count, gauge, cycle rating,
  and required prep for a specific transfer product. `[MFR]`
- DHI — hardware application practice, including transfer selection. `[PRACTICE]`
- `../34_Electrical_Power/` — power supplies, batteries, and voltage drop in depth.
- `../28_Calculators/psec/power.py` — the calculations in this lesson.

**Next:** [07 — Fire-Rated Openings](07_fire_rated_openings.md)
