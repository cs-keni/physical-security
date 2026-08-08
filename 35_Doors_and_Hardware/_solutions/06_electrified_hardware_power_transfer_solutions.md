# Solutions — 06 Electrified Hardware and Power Transfer

---

## E6.1 — Transfer method and conductor budget

**(a) Electrified mortise lockset with latch monitoring and integral REX, interior office suite.**

```
   Lock power                 2
   Latch monitoring           2
   REX (lever switch)         2
                          ─────
   Subtotal                   6
   Spares                     2
                          ─────
   SPECIFY                    8-conductor
```

**Method: electrified transfer hinge, 8-conductor, 24 AWG.** Interior, low current
(~0.30 A), concealed, no reason to reach for anything heavier. This is the default case and
the hinge is the default answer.

**(b) Fire exit hardware with electric latch retraction on a 90-minute stair door.**

```
   ELR power                  2
   Latch monitoring           2
   REX (touchbar switch)      2
   Electrified trim, if the
     re-entry function is
     separate from the ELR    2
                          ─────
   Subtotal                   8
   Spares                     2
                          ─────
   SPECIFY                   10-conductor
```

**Method: EPT, not a hinge.** Two reasons, and the second is the one that decides it:

1. Conductor count is at the top of what a hinge carries.
2. **Current.** ELR draws multiple amps and the transfer's own gauge becomes a governing term
   in the voltage-drop calculation — E6.2 works this through. An EPT is available with heavier
   conductors; a 24 AWG hinge is not the right device for an ELR load.

**Additionally, because it's a 90-minute opening:** the prep must be factory-applied per the
approved submittal, on both the frame and the leaf. Field-machining this opening voids the label
(lesson 07). Get the transfer into the door order.

**Worth challenging before you spec it:** does this opening actually need ELR, or does
**electrified trim** do the job? Lesson 03's guidance is trim unless a specific requirement
demands latch retraction. Trim drops the current by an order of magnitude and this entire
problem with it.

**(c) Retrofit onto an existing solid-core wood door, unrated, back-of-house corridor, door
cannot be removed for machining.**

**Method: surface-mounted armored door loop** — or, better, **don't put the lock in the leaf at
all.**

The constraint says no machining, which rules out a concealed transfer. That leaves the door
loop, which is acceptable here on its merits: back-of-house (appearance doesn't matter),
interior (no water), unrated (no label to void).

**But the better answer is to re-examine the device choice.** If the existing lock is sound and
has no deadbolt, an **electric strike** puts the electrified component in the *frame* and the
transfer problem disappears entirely. Lesson 03 named this as the strike's biggest practical
advantage; this is the case where it pays.

Full credit for either answer; the strong answer names both and recommends the strike.

**(d) Data hall door: electrified lockset with latch monitoring, REX, deadbolt monitoring, plus
provision for a second reader later.**

```
   Lock power                 2
   Latch monitoring           2
   REX (lever switch)         2
   Deadbolt monitoring        2
                          ─────
   Subtotal                   8
   Future second reader       ← see below
   Spares                     2
                          ─────
   SPECIFY                   10-conductor minimum, 12 if available
```

**The second-reader trap:** a reader on the secure side is mounted on the *wall*, not in the
leaf, so it does not consume transfer conductors. Do not budget for it in the transfer.

What *would* consume them is a change in the lock function during submittal review — and at the
highest-consequence opening on the project, that is likely. **Take the largest conductor count
the product line offers.** The cost delta is trivial against the consequence tier, and this is
the opening where you least want to be pulling a door in year two.

**Method: EPT or a high-count hinge**, factory-prepped. Current is low so gauge isn't governing;
conductor count and future-proofing are.

---

## E6.2 — 🧮 ELR at 175 ft with a 5 ft transfer

Given: 3.2 A running, 175 ft home run, 5 ft of 24 AWG transfer, 24.0 V supply, 21.0 V minimum
at the device.

### (a) Drops

**Transfer, 5 ft of 24 AWG at 3.2 A: 1.022 V.**

| Home run conductor | Home run drop | + transfer | Total | At the device |
|---|---|---|---|---|
| 18 AWG | 8.897 V | 1.022 | 9.918 | 14.08 V |
| 16 AWG | 5.593 V | 1.022 | 6.615 | 17.39 V |
| 14 AWG | 3.518 V | 1.022 | 4.540 | 19.46 V |
| 12 AWG | 2.213 V | 1.022 | 3.234 | 20.77 V |
| 10 AWG | 1.392 V | 1.022 | 2.414 | 21.59 V |

### (b) Which conductor works?

**10 AWG** — and only just, at 21.59 V against a 21.0 V floor.

**Note what happened to 12 AWG.** On the home run alone it delivers 21.79 V and passes. Add five
feet of hinge wire and it delivers 20.77 V and fails. **The transfer moved the answer by a full
conductor size.** An engineer who stopped at the frame would have specified 12 AWG and built an
opening that doesn't work.

Also flag the margin: 0.59 V of headroom on a 24 V system is roughly 2.5%. That is not a design;
that is a coin flip against conductor temperature, supply tolerance, and connection resistance.
Even before part (c), 10 AWG is not a comfortable answer.

### (c) Recompute at 8.0 A inrush

**Transfer, 5 ft of 24 AWG at 8.0 A: 2.554 V.**

| Home run conductor | Home run drop | + transfer | At the device |
|---|---|---|---|
| 12 AWG | 5.531 V | 2.554 | **15.91 V** ❌ |
| 10 AWG | 3.480 V | 2.554 | **17.97 V** ❌ |

**What changes: everything.** At inrush there is no home run conductor size that solves this
problem. 10 AWG — already an awkward, expensive, hard-to-terminate conductor for a lock circuit
— delivers 17.97 V, three volts under the floor.

**This is the real lesson of the exercise.** The running-current calculation in part (a) produced
a plausible-looking answer that is wrong, because the moment that actually matters is the
250 ms when the latch has to pull. Running the numbers at steady state is how a design passes
review and fails in the building.

Note also that the transfer's contribution grew from 1.02 V to 2.55 V while the home run's grew
proportionally too — but the transfer is only 5 feet. **Five feet of 24 AWG is costing you more
than a hundred feet of 12 AWG.**

### (d) Two fixes that don't increase the home run gauge

**Fix 1 — Relocate the power supply.** Put a local supply 25 ft from the opening instead of
175 ft. With 12 AWG home run and an EPT carrying 18 AWG:

```
   Home run  25 ft, 12 AWG, 8.0 A  →  0.790 V
   Transfer   5 ft, 18 AWG, 8.0 A  →  0.635 V
                                      ───────
                                       1.425 V   →  22.57 V at the device  ✅
```

Comfortable margin, smaller conductors, and a bonus: a local supply shrinks the failure domain,
so one supply failure takes out a few openings instead of a floor.

**Fix 2 — Change the transfer device.** Swap the 24 AWG hinge for an **EPT with 18 AWG
conductors**. At 8 A that alone takes the transfer drop from 2.554 V to 0.635 V — a 1.9 V
recovery from a component change with no additional wire. It does not solve this opening on its
own (10 AWG home run + 18 AWG transfer still lands at 19.89 V), but combined with fix 1 it is
decisive, and on a shorter home run it would be sufficient by itself.

**Fix 3, and the one to raise first — change the device.** Per lesson 03: use **electrified trim**
instead of electric latch retraction unless a requirement specifically demands pull-side entry
with the latch retracted. Trim draws a fraction of the current, and the entire problem evaporates.

> 🧠 The general principle, and it's worth stating explicitly because it recurs: **when the
> arithmetic gets ugly, question the device selection before you question the conductor.** Three
> iterations of wire sizing to make a marginal ELR work is a signal that the ELR was the wrong
> choice.

---

## E6.3 — Missing transfers across 61 openings

**The count:** 34 electrified locksets + 6 electrified exit devices = **40 openings with
leaf-mounted electrified hardware**. The hardware sets list transfer hinges at 22.

**18 openings have a device in the leaf and no way to power it.**

**The review comment:**

> **General comment — power transfer.**
>
> The set specifies leaf-mounted electrified hardware at 40 openings (34 electrified locksets,
> 6 electrified exit devices) and lists a power transfer device at 22. **18 openings have no
> means of getting power into the leaf.** Exception list attached.
>
> For each of the 18, provide a transfer device in the hardware set, with:
> - conductor count meeting the function budget plus a minimum of 2 spares (for a lockset with
>   latch monitoring and REX, that is 8; with deadbolt monitoring, 10);
> - conductor gauge adequate at the device's **inrush** current, not its running current —
>   particularly at the 6 exit devices if any use electric latch retraction;
> - factory prep called out on the door and frame schedules.
>
> Please confirm the transfer decision is reflected in the door order. Any opening whose doors
> have already been released without transfer prep needs to be identified now, not at
> installation.
>
> **At the 22 openings that do list a transfer**, confirm the conductor count against the
> function list — several sets appear to budget lock power only.

**The check against the device register:**

```
   RULE:  leaf_mounted_electrified_device(opening) AND NOT has_transfer_record(opening)
          → ERROR "Leaf-mounted electrified hardware with no power transfer"

   RULE:  has_transfer_record(opening)
          AND transfer_conductor_count < function_conductor_budget(opening) + 2
          → ERROR "Transfer conductor count below function budget plus spares"

   RULE:  has_transfer_record(opening)
          AND device_peak_current(opening) > threshold
          AND transfer_awg > 20
          → WARNING "Small-gauge transfer on a high-current device — verify voltage at inrush"
```

Where `leaf_mounted_electrified_device` is derived from the device type field: electrified
lockset, electrified exit device, and electrified trim are leaf-mounted; electric strike,
magnetic lock, and door position switch are not.

**This is a presence-and-consistency check, so it belongs in the validator**
(`../../16_Automation/data_model/`). The rules above produce an exception list. **What stays
manual:** whether the specified transfer is the *right* one, whether the current figures used
were inrush or running, and whether the 22 existing entries were budgeted from the function list
or copied from another project. The validator finds the 18; a person decides what to do about
each.

---

## E6.4 — Nine surface door loops as a field fix

**The response:**

> Thanks for flagging it before installing.
>
> **The five unrated openings:** a surface armored loop is acceptable there. It isn't what I'd
> have specified — it's exposed to abuse and it looks like a field fix, which it is — but it
> works, it's reversible, and at back-of-house openings I'm not going to hold the schedule over
> appearance. Please use an armored loop rated for the cycle count, route it so it isn't a snag
> hazard, and note the deviation in the as-builts.
>
> **The four 90-minute rated openings: no.** Installing a surface transfer requires attaching to
> the leaf and the frame, and any attachment beyond the listed preparations voids the label. The
> opening would stop being a rated assembly while continuing to carry a label that says it is —
> which is worse than a visible violation, because nothing downstream catches it.
> `[CODE][VERIFY]`
>
> Three options for those four, in order of preference:
>
> 1. **Return them for factory prep**, or order replacement leaves and frames with the transfer
>    prep. Schedule impact, but it is the only option that ends with a rated opening and a valid
>    label.
> 2. **Change the device family.** If the existing lock at any of the four could be served by a
>    **fire-rated electric strike** instead, the electrified component moves into the frame and
>    the transfer problem goes away. This is worth twenty minutes of checking before we accept
>    option 1's schedule hit.
> 3. **Have the modification performed by a party authorized by the listing agency**, if the
>    listing permits a field modification of this type and such a party is available. Verify
>    before assuming — most transfers are not a permitted field modification, and "a locksmith
>    said it was fine" is not the standard. `[VERIFY]`
>
> I'd like to look at option 2 today. Can you send me the lock types at those four openings?
>
> **For the record on how we got here:** the transfer decision has to be fixed before the door
> order. I'll take my share of that — let's put it on the checklist for the next package.

**What makes it work:**

- Splits the problem. Five of the nine are fine and saying so immediately buys credibility for
  the refusal on the other four.
- Explains *why* the rated four are different, in one sentence, mechanically.
- Offers three options ranked, including one that might avoid the schedule hit entirely.
- Asks for a specific piece of information so the next step happens today.
- Takes partial ownership of the root cause without making a performance of it.

---

## E6.5 — Why the transfer decision precedes the door order

Model answer (114 words):

> Doors get machined at the factory, not on site. If a lock goes in the leaf, the leaf needs a
> wire path and a hinge or transfer prep, and that has to be on the door order.
>
> If we miss it, the doors arrive solid and we have three options: send them back, cut them in
> the field, or surface-mount an armored loop. The first is a lead-time hit. The second voids
> the label on anything rated. The third looks like what it is.
>
> The good news is that the decision is stable early. I don't need the final device model to
> fix the conductor count — that comes from the function list, and the function list barely
> moves. Give me the door order date and I'll have it before then.

**What makes it work:** frames the constraint as a fact about manufacturing rather than a
process demand, names the three bad outcomes concretely, and then removes the PM's real
objection — that the security design isn't finished — by explaining why this particular decision
doesn't need it to be.
