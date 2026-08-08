# Quiz 35 — Answer Key and Explanations

> **Stop.** If you have not written your answers down, go back. Reading these first will make you
> feel like you understood the material and will not teach you anything.

Read the explanation for **every** question, including the ones you got right. The explanations
carry material the questions don't.

---

## Part A

**1. The opening.** Door(s) + frame + hardware set + wall condition + clearances.

The reason this matters and isn't pedantry: the opening is the unit that gets numbered,
scheduled, specified, priced, ordered, delivered, installed, and inspected. Saying "door" when
you mean "opening" creates real ambiguity about scope in an RFI, and it reads as inexperience to
everyone on the distribution list.

**2. A KD (knock-down) or drywall slip-on frame.**
Materially weaker than a welded frame, and it can often be worked loose from the wall. The
security consequence is the balanced-protection failure: a high-security lock on a KD frame in a
single-layer drywall partition is the strongest element in a chain whose weakest element is 5/8"
gypsum board.

**3.** The deadlatch (auxiliary latch) is the small plunger beside the main latch bolt. When the
door is closed it rides on the strike and **blocks the main latch from being pushed back**. It
exists specifically to defeat the "slip something past the latch" class of attack.

**It stops working when it isn't seated** — because the door is misaligned or the strike is in
the wrong place, so the plunger drops into the strike pocket alongside the latch instead of
riding on the strike face. The opening is then far weaker than the schedule says and **nothing
visible tells you.** Check it in the field, visually, against the strike.

**4. A coordinator.** Without it the leaves close out of order, the astragal fouls, and
frequently **neither leaf latches.** An unlatched door is not a barrier and, on a rated opening,
is not a fire door.

**5.** Stand on the **outside** of the door; the hinge side (left or right) plus the swing
direction (away from you, or toward you = "reverse") gives the hand.

Full credit requires "stand on the outside." Half the handing errors in practice are not
left/right confusion — they are two people disagreeing about which side is outside.

**6.** The door swings **toward** the person standing on the outside. That is the entire meaning.
It does not mean anything is backwards.

**7. LH (Left Hand).** Outside = the corridor (you are secured *from* the corridor; the key goes
in from the corridor). Hinges on your left, swinging away from you → LH.

**8. Unsecured (approach) side, on the strike jamb side.**

The jamb answer: a reader on the hinge side forces the user to badge, then cross the door swing
to reach the lever. It is not a code issue, so nothing catches it, so it gets built — and then
every user does an awkward two-step at that door forever.

**9.** The REX shunts the door alarm on detection. On the unsecured side, it shunts for anyone
*approaching from outside* — so the door can be opened from the unsecured side with no credential
and **the system logs nothing abnormal.**

This is the failure mode that survives commissioning, because nothing looks wrong. The opening
is functionally uncontrolled and the audit trail says it is fine.

**10.**

| Family | Free egress mechanism |
|---|---|
| Electric strike | Mechanical — the inside lever, which the strike is not in the path of |
| Magnetic lock | **None mechanically.** Electrical release only. |
| Electrified lockset | Mechanical — the inside lever, which is never controlled |
| Electrified exit device | Mechanical — pushing the bar |
| Electric bolt / shear lock | Weak; bolt is in the egress path. Use with reservation. |

**11. The magnetic lock.** It requires (any three): a request-to-exit sensor on the egress side; a
manual release device that directly interrupts power independent of the controller; automatic
release on power loss; a hardwired fire alarm release; required signage; and a recurring testing
obligation.

The framing worth remembering: **five components and a permanent life-safety obligation to
replace one lever.**

**12. Electrified locksets and electrified exit devices** (including electrified trim) — anything
electrified that lives **in the leaf**. Electric strikes and magnetic locks mount in or on the
frame and need no transfer.

**13.** An electric strike releases the **latch**. If the existing mechanical lock has a
**deadbolt** that someone throws, the credential is decorative.

The reason it catches everyone once: nobody throws the deadbolt during commissioning. It works
perfectly at handover and fails unpredictably in service.

**14. Fail safe = unlocked with no power. Fail secure = locked with no power.**
"Safe" refers to **people**; "secure" refers to **property**. Both terms describe only the lock's
behavior in the absence of power.

Also worth stating: never say "fail open" or "fail closed." Open could mean the door or the
circuit, and two engineers can use it to mean opposite things in the same meeting without
noticing.

**15.** Because **the inside lever is a mechanical linkage** and is never electrified. It works
with the power off, the controller dead, the network gone, and the building on fire. Fail secure
stops granting *entry*; egress was never electrical.

This is the single most consequential correction in the module. Juniors who believe fail secure
is dangerous specify fail safe everywhere "to be safe," and build a building that unlocks itself
whenever the power drops — trading a real security property for a life-safety benefit they
already had mechanically.

**16.** Any two of:

- **The failure direction is wrong.** A hardwired normally-closed contact fails to *released* — a
  cut wire is indistinguishable from an alarm. A message-based path fails to *locked*: a network
  outage, an expired certificate, or a service that didn't restart produces silence, and nothing
  happens.
- **The dependency chain is wrong.** A relay depends on a relay. A software path depends on two
  servers, a network, and two vendors' software versions staying compatible for the twenty-year
  life of the building.
- **It isn't testable by the people who will own it.** A facilities tech can pull a station and
  watch a door release, forever. Nobody will meaningfully test an API integration.

**17.** A person inside must be able to get out **without a key, without special knowledge,
without a tool, and in one motion — always.**

"One motion" protects against the fact that **under stress, fine motor sequences fail.** In smoke,
in the dark, in panic, a two-step operation (retract the deadbolt, then turn the lever) becomes a
zero-step failure. The code is not written for the calm, informed, able-bodied adult who read the
sign.

**18.** It lets you **secure the outside completely.** The door must open from the inside; nothing
requires it to open from the outside.

It resolves most "lock the exit" requests because the client's actual worry is usually people
coming *in* off the alley or the loading dock — and that is entirely unconstrained. You can give
them what they need without touching the egress function, and they walk away satisfied.

**19.** Any three:

- **Magnetic locks are out** — a magnet holds by friction against a face, not by a bolt in a
  strike, so it is not positive latching; and it releases on fire alarm by design, exactly when
  the door must stay shut.
- **Dogging on fire exit hardware is out** — dogging holds the latch retracted.
- **Fail secure only** — the latch must be mechanical and must engage regardless of electrical
  state.
- **Stair re-entry releases the outside trim, not the latch** — the bolt stays engaged; only
  credential control on the outside lever goes away.
- **Electric strikes must be fire-rated and continuously latching.**

Full credit for three. **The thing being tested is whether four rules have compressed into one
principle.** A learner who memorized facts will list facts; one who understood will derive all of
them from "it must latch."

**20.** The control key **removes and replaces interchangeable cores** without disassembling the
lock. It opens no door on its own.

**Rekey scope when lost: every core in the system.** Whoever holds it can pull any core in the
building and substitute one keyed to a key you don't know about, silently, leaving a lock that
looks identical.

The trap: because it isn't a door key, it gets treated casually. It is the most sensitive
credential in an SFIC system.

---

## Part B

**21. Governing weakness: the wall** — specifically the suspended ceiling running continuously
over the partition into the corridor. Second: the KD frame in a single-layer drywall partition.
The door is third and the lock is fourth.

**Why the lock is not the answer:** you would be buying delay at the strongest path while the
weakest stays open. Anyone can go over the partition in about a minute, with no tools and no
noise. This is balanced protection (`01_Foundations/04`) at the scale of a single room.

**Cheapest material intervention:** a door position switch **and an interior motion sensor** on
the intrusion system, so entry by *either* path is detected. Detection is the affordable
substitute when delay is not available — see the functional chain. The real fix is extending the
partition to the structural deck, which is architectural, capital, and correct.

Full credit requires naming the ceiling. Half credit for naming the frame. **No credit for
recommending access control**, which is the most common wrong answer and the one the exercise is
built to catch.

**22.**

*Concede first, by name:* the two all-glass lobby entrances are legitimate — there is nowhere to
put a lock case and no leaf to prep. Naming them specifically is what makes the rest of the
comment land as engineering rather than as preference.

*Ask for:* at each of the other 20, either a one-line justification for why an electrified
lockset or electric strike is not feasible, or a revision to one of those. Openings whose door and
frame can accept a lock case should default to the revision.

*Require at any opening that remains a mag lock:* manual release device, signage, hardwired fire
alarm release (not an ACS integration), bond status monitoring, release on power loss, and
inclusion in the O&M testing schedule. `[CODE][VERIFY]`

*Bonus point:* offer to walk the openings together. Most of these get resolved in twenty minutes
in person.

**23.** The clues before checking anything: **intermittent**, **time-correlated**, **valid grant
logged**, **ELR device**, **long run**. Four of five point at the physical layer.

*Check first, in order:*

1. **Conductor gauge and actual routed run length** — computed at the device's *inrush* current,
   not its running current. Rules in or out the primary hypothesis.
2. **Measured voltage at the device during a retraction attempt** — confirms it empirically. A
   resting measurement looks fine, which is exactly why this fault survives.
3. **Ambient temperature along the run** — explains the afternoon correlation. Conductor
   resistance rises with temperature.

(Also acceptable: power supply loading and battery condition; mechanical binding of the latch.)

*Deliberately not first:* the credential, the firmware, the reader, the controller config, or the
head-end software. **The log already told you the controller granted access.** The failure is
downstream of the decision.

*The principle:* software fails deterministically. Same input, different output depending on time
of day, is physics.

**24.**

*The constraint, one sentence:* that door is on the means of egress, so it must open from the
inside in one motion with no key, and that is not something I can design around or get waived.

*Three options:*

| Option | Solves | Doesn't solve |
|---|---|---|
| **Alarm and monitor it** — local sounder, monitored contact, alarm-linked camera | Undetected departures; most of the loss, because most of it is opportunistic and stops the first time it's loud | A determined person who accepts the noise |
| **Delayed egress**, if the occupancy and conditions permit `[CODE][VERIFY]` | The above, plus a real interval for staff to arrive | Nothing more, if nobody responds. Adds code conditions, signage, and a recurring test obligation. |
| **Move the exposure** — relocate high-value stock away from the rear | The actual loss, permanently, at near-zero cost | The door remains an uncontrolled opening |

*Bonus:* mention that you can lock it from the **outside** completely. Free egress is
one-directional. If the client's real worry is people coming in off the alley, that solves it
today with no code implications.

**25.**

*The finding:* six 90-minute rated frames field-drilled beyond their listed preparation. A field
modification beyond the listing **voids the label**, so those six assemblies carry labels stating
a rating they may no longer hold. `[CODE][VERIFY]`

*Why it is worse than a visible violation:* the label is still attached and the doors look
correct. Nothing downstream catches it — not the next engineer, not the facilities team, not a
casual inspection. A chained exit gets noticed. This does not.

*First two actions:*

1. **Stop work** on any further DPS installation at rated openings, today, and inventory exactly
   which openings were modified. Six is the observed count, not necessarily the actual one.
2. **Ask the listing agency** whether this modification can be field-evaluated and re-labeled by
   an authorized party. That is the cheap path if it exists and it must be established by the
   agency, not by opinion. `[VERIFY]`

*Bonus:* check whether the openings already have electrified locksets with integral latch
monitoring — if so, a separate DPS may not have been needed at all, and some of the six may not
need remediation beyond removing the switch.

**26.** **Key control.** Not hardware.

*The mechanism, which is what the question is really asking for:* every electrified lock has a
**mechanical key override** by design, because "what happens when the battery is dead" has to have
an answer. So a person with the right key walks past the entire $400,000 system, and at most
openings a mechanical key operation **generates no event at all.** Not a suspicious event —
nothing.

*What to recommend:* a written key control policy; **one named owner by role**; an issuance
register; key return integrated with HR offboarding; an annual physical audit of masters; and, as
the one purchase worth making, a **restricted or patented keyway**, because that is what makes the
number of existing keys knowable.

*The point of the question:* the best answer costs the client almost nothing and reduces your own
scope. Say it anyway.

---

## Part C

**27.**

**(a)**
```
   Standby:  10(0.32) + 5(0.20) + 1(0.30) = 3.20 + 1.00 + 0.30 = 4.50 A
   Peak:     10(0.32) + 5(0.20) + 1(3.50) = 3.20 + 1.00 + 3.50 = 7.70 A
```

**(b) Peak governs**, at 7.70 A. The supply must be able to deliver current at the moment of
maximum demand; a supply sized to standby will sag or current-limit exactly when the latch is
trying to retract.

**(c)** `7.70 × 1.25 = 9.625` → **specify a supply rated ≥ 9.63 A continuous.**

**(d)** Any one of:
- **Battery charging current**, which is additional and comes from the datasheet.
- The distinction between a supply's **peak** and **continuous** ratings — a unit advertised as
  "10 A" is often 10 A peak with a lower continuous figure.
- Any **future load** at the openings.
- The assumption that only one ELR device retracts at a time — here there is only one, but with
  multiple ELR devices you must justify any assumption that they cannot fire simultaneously.
  "They probably won't" is not a justification; shift change and fire drills exist.

**28.**

**(a)**
```
   Ah_raw   = 4.50 A × 4 h = 18.00 Ah
   Ah_sized = 18.00 × 1.25 (discharge derate) × 1.25 (aging) = 28.13 Ah
```
**28.13 Ah minimum; specify the next standard size up.**

**(b) Standby current drives it**, which is the opposite of question 27, because **the battery
question is about energy over time and the supply question is about instantaneous current.**

The ELR device draws 3.50 A for a fraction of a second at a time, so its contribution to
amp-hours is negligible while its contribution to the supply rating dominates. **Different
question, different governing number.** Getting these two backwards is the most common sizing
error in this whole subject.

**(c)** The required standby duration is **not an engineering choice.** It comes from the
applicable standard and the AHJ. `[CODE][VERIFY]` Sizing a battery correctly against the wrong
duration is still wrong, and it is wrong in a way that passes review.

**29.**

**(a)** Transfer, 6 ft of 24 AWG at 2.0 A: **0.766 V.**

**(b)**

| Home run | Home run drop | + transfer | Total | At the device |
|---|---|---|---|---|
| 18 AWG | 4.766 V | 0.766 | 5.532 | **18.47 V** ❌ |
| 16 AWG | 2.997 V | 0.766 | 3.763 | **20.24 V** ❌ |
| 14 AWG | 1.885 V | 0.766 | 2.651 | **21.35 V** ✅ |

**(c) 14 AWG.**

**(d) No — and this is the entire point of the question.**

Stopping at the frame:
```
   16 AWG:  24.00 − 2.997 = 21.00 V   → exactly at the floor, "passes"
```
You would have specified 16 AWG. Add the six feet of transfer and the device sees **20.24 V** and
the opening does not work.

**Six feet of small wire moved the answer by a full conductor size.** Everyone computes the home
run. The failure lives in the last segment.

**30.**

**(a)**
```
   Lock power                 2
   Latch bolt monitoring      2
   REX (lever switch)         2
   Deadbolt monitoring        2
                          ─────
   Subtotal                   8
```

**(b) Specify a 10-conductor transfer** — the budget plus a **minimum of two spares.**

Why: the cost delta is small and one-time; the cost of needing a ninth conductor after
installation is a door removal, and on a rated opening potentially a voided label. Things that
consume the spares are all normal — a conductor damaged during installation (the most common),
a lock function that changes during submittal review, a conductor that fails from flex fatigue
in year seven.

**The rule: count the functions, add two, round up to the next available device.** If you are on
the fence between 8 and 10, take the 10.

**(c) No — a reader on the secure side mounts on the *wall*, not in the leaf**, so it consumes no
transfer conductors.

*The better answer also says:* what *would* consume them is a change to the lock function during
submittal review, which is a real risk. And it flags the more important issue hiding in the
colleague's question — **a second reader is a controlled-egress or occupancy-tracking decision,
not a hardware convenience.** It changes the request-to-exit strategy, it may enable anti-passback
or a two-person rule, and it belongs in requirements (`01_Foundations/06`) before it belongs in a
hardware set. Ask what requirement it serves.

---

## Scoring yourself honestly

| Score band | What it means |
|---|---|
| Cold, < 50% | Expected. Doing its job. |
| Retake, < 65% | Reread lessons 03 and 04. Those two carry most of Part A. |
| Retake, 65–80% | Solid grasp; check whether your losses cluster in Part C. If so, the problem is arithmetic discipline, not comprehension. |
| Retake, ≥ 80% with ≥ 90% on Part C | You can be handed an opening. |

**The three questions most worth getting right, regardless of total:** 15 (fail secure doesn't
trap anyone), 18 (free egress is one-directional), and 29(d) (the transfer changes the answer).
Those three are the ones that change what you build.
