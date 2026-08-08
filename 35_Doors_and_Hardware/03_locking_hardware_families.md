# 03 — Locking Hardware Families

## Learning objectives

- Name the five electrified locking families and state the mechanism by which each one
  provides free egress.
- Select the right locking device for an opening from its function, construction, rating, and
  egress requirement — rather than from habit or from what the last project used.
- Explain why a magnetic lock is a fundamentally different kind of device from every other
  option, and why "it's easier to install" is the reason it is over-specified.
- Distinguish **door position** from **latch/bolt position** and explain why only one of them
  tells you the opening is secure.
- 🧮 Size a power supply and select a conductor for a set of electrified openings, and explain
  why the most common electrified-hardware failure is an electrical problem misdiagnosed as a
  software problem.

---

## ELI5

There are five ways to lock a door with electricity:

1. **Electric strike** — the *hole* the latch goes into lets go.
2. **Magnetic lock** — a big electromagnet glues the door to the frame.
3. **Electrified lockset** — the normal lock, with a motor in it.
4. **Electrified exit device** — the push bar, with a motor in it.
5. **Electric bolt** — a bolt shoots out of the frame into the door.

The only question that matters for choosing among them: **when everything fails and it's dark
and full of smoke, how does a person get out?**

Four of the five answer that mechanically — you push, and you're out, no matter what the
electronics are doing. One of them (the magnet) has no mechanical answer at all, and everything
difficult about magnetic locks follows from that single fact.

---

## The organizing question

Before the product comparison, internalize the frame:

```
   Every electrified opening must answer THREE questions:

   1. How is it SECURED?          (which device, and how much attack resistance)
   2. How does a person GET OUT?  (mechanically, with no power, no network, no controller)
   3. How do you KNOW its state?  (door position, latch position, lock status)

   Question 2 is not negotiable and it is not yours to trade away.
   Answer it FIRST and the device choice usually collapses to one or two options.
```

> 🧠 **Juniors pick the device and then figure out egress. Seniors determine the egress
> mechanism and then pick from what's left.** That single reversal in order prevents most of
> the code exposure, most of the redesign, and all of the arguments with the fire marshal.
> Life safety outranks security, always (`../01_Foundations/`), and at an opening that
> abstract principle becomes a very concrete question about what a person's hand does.

---

## Family 1 — Electric strike

**What it is:** replaces the fixed strike in the frame. The keeper (the part the latch sits
against) pivots or releases on command, so the door can be pulled open without turning the
lever from the outside.

```
   FRAME (strike jamb)                Door
   ┌──────────┐
   │  ██████  │  ← solenoid
   │  ┌────┐  │
   │  │keep│◄─┼──────  latch bolt
   │  │ er │  │
   │  └────┘  │       keeper releases → door pulls open
   └──────────┘       lever ALWAYS works from inside → egress is mechanical
```

| Property | Value |
|---|---|
| **Mounts in** | The frame |
| **Power transfer to leaf?** | **No** — this is its biggest practical advantage |
| **Free egress** | Mechanical, via the existing lever/knob on the inside. The strike is not in the egress path at all. |
| **Fail state** | Fail secure (standard) or fail safe (ordered) — lesson 04 |
| **Typical current** | ~0.15–0.5 A at 12/24 VDC `[MFR][VERIFY per product]` |
| **Monitoring** | Latch monitoring and keeper monitoring available as options — **order them** |
| **Fire doors** | Only with a fire-rated strike, which must be **fail secure** and continuously latching `[CODE][VERIFY]` |

**When it's right:** retrofitting access control onto an opening that already has a good
mechanical lock and a decent frame. Enormously cost-effective, because the mechanical lock,
the leaf, and the hinges are all untouched.

**When it's wrong:**
- The frame is too shallow, or is a KD frame with no wire path.
- The mechanical lock has a **deadbolt that gets thrown**. A strike releases the *latch*. If
  someone throws the deadbolt at 5 p.m., the credential is now decorative and you will get a
  service call you can't fix.
- The door is badly aligned. Strikes are less tolerant of misalignment than magnets.

> ⚠️ **The deadbolt trap catches everyone once.** An electric strike plus an existing
> lockset-with-deadbolt is a very common retrofit condition and it produces an opening that
> works perfectly during commissioning (nobody throws the deadbolt during commissioning) and
> fails unpredictably in service. Verify the mechanical function of the existing lock before
> you specify a strike.

---

## Family 2 — Electromagnetic lock ("mag lock")

**What it is:** an electromagnet mounted to the frame head and a steel armature plate mounted
to the leaf. Energize the magnet and it holds. De-energize and it lets go. No moving parts.

| Property | Value |
|---|---|
| **Mounts on** | Frame head (and the leaf, for the armature) |
| **Power transfer to leaf?** | No — but you must get a solid mechanical mount on the leaf |
| **Free egress** | ⚠️ **NONE mechanically.** Egress requires *electrically releasing the lock.* |
| **Fail state** | **Fail safe only.** There is no fail-secure magnetic lock. Physics, not product line. |
| **Holding force** | Commonly 600 / 1200 / 1500 lbf `[MFR]` — a *shear/tension* rating that assumes correct alignment and a rigid mount |
| **Typical current** | ~0.25–0.5 A at 24 VDC, continuous `[MFR][VERIFY]` |
| **Monitoring** | Bond sensor / magnetic bond status available — **order it**; without it you know nothing |
| **Fire doors** | Generally incompatible with the requirement for a fire door to be self-latching `[CODE][VERIFY]` |

### Why the mag lock is a different kind of device

Every other family in this lesson provides egress **mechanically**: you push a bar or turn a
lever and a physical linkage retracts a bolt. The electronics can be dead, on fire, or
disconnected, and the person still gets out.

A magnetic lock has no such linkage. **The only way out is to cut power to the magnet.** So the
opening now needs an entire additional subsystem whose job is to guarantee that power gets cut:

- A **request-to-exit** device (motion sensor or push button) that drops power on approach.
- Very often a **push-to-exit button** hard-wired to break the power circuit, independent of
  the controller.
- An interface to the **fire alarm system** that drops power on alarm.
- Sometimes a **hardware-based release** in the egress path.

Every one of those is an additional component that must be specified, installed, wired,
commissioned, tested, and maintained — and every one of them is a single point of failure for
somebody's ability to leave a burning building. The specific arrangement that is *acceptable*
is a code and AHJ matter. `[CODE][VERIFY — the release requirements for electromagnetically
locked egress doors are prescriptive in the applicable building and life safety codes, they
differ by occupancy and by which code section you are designing under, and they are one of the
most-cited items in this field. Design this against the adopted code text and confirm with the
AHJ. Do not design it from a manufacturer's application sheet, and do not design it from
memory.]`

> ⚠️ **Mag locks are over-specified because they are easy to install.** They don't care much
> about alignment, they need no leaf prep, no power transfer, and no frame depth. A contractor
> can hang one on almost anything. That convenience is real — and it is paid for with permanent
> code exposure, a permanent additional-device count, and a permanent life-safety obligation.
>
> **The senior position:** a mag lock is the correct answer at a small number of openings —
> typically glass entrances and openings with no suitable lock or frame — and the wrong answer
> at most openings where it appears. If a mag lock is on your drawing, be able to say in one
> sentence why nothing else works there.

---

## Family 3 — Electrified lockset (cylindrical or mortise)

**What it is:** the mechanical lock itself, with a solenoid or motor inside that controls
whether the **outside** lever is engaged or free-spinning (or that retracts the latch directly).

| Property | Value |
|---|---|
| **Mounts in** | The leaf |
| **Power transfer to leaf?** | **Yes** — electric hinge or door loop required. Lesson 06. |
| **Free egress** | Mechanical, via the inside lever. **The inside lever is never controlled.** |
| **Fail state** | Fail safe or fail secure, ordered as such — lesson 04 |
| **Typical current** | ~0.15–0.35 A at 24 VDC `[MFR][VERIFY]` |
| **Monitoring** | Latch bolt monitoring, lever/request-to-exit switch, deadbolt monitoring — available integral. **This is its best feature.** |
| **Fire doors** | Compatible, when the lockset is fire-labeled and fail secure `[CODE][VERIFY]` |

**When it's right:** most access-controlled interior openings in new construction. It's the
default for a reason — one device, mechanical egress, integral monitoring, clean aesthetics,
good security.

**When it's wrong:** retrofit where you can't easily get power into the leaf, or where the
door isn't prepped for the lock case you need.

> 🧠 **The integral request-to-exit switch is the underappreciated feature.** An electrified
> lockset can report "somebody turned the inside lever" as a hardware event. That is a *far*
> better REX than a ceiling motion sensor: it can't be triggered from the wrong side, it can't
> be triggered by a passing cart, and it corresponds exactly to the act of leaving. Where you
> can get lever-based REX, take it. See lesson 02 for what goes wrong with motion-based REX.

---

## Family 4 — Electrified exit device

**What it is:** panic hardware or fire exit hardware — the horizontal bar — with electric
function added. Three distinct variants that juniors merge and shouldn't:

| Variant | What's electrified | Free egress | Note |
|---|---|---|---|
| **Electric latch retraction (ELR)** | The latch retracts electrically, so the door can be pulled open from outside | Push the bar — always mechanical | **High inrush current.** See the calculation below. |
| **Electric dogging** | Holds the latch retracted so the door is momentarily push/pull free | Push the bar | ⚠️ **Fire exit hardware may not be dogged at all** `[CODE][VERIFY]` |
| **Electrified trim / lever** | The outside lever is controlled; the latch is untouched | Push the bar | Lower current, simpler, usually the better choice |

| Property | Value |
|---|---|
| **Mounts on** | The leaf |
| **Power transfer to leaf?** | Yes |
| **Free egress** | Mechanical, by pushing the bar. This is the entire point of panic hardware. |
| **Fire doors** | Only with **fire exit hardware** (which is always latching and cannot be dogged) `[CODE][VERIFY]` |

**When it's right:** any opening that requires panic hardware — assembly occupancies, high
occupant loads, certain electrical rooms — and also needs credentialed entry. Stair doors and
main exterior entrances are the common cases.

> ⚠️ **"Panic hardware" and "fire exit hardware" are not synonyms.** Fire exit hardware is
> panic hardware that is fire-labeled: it always latches and it has no dogging feature, because
> a fire door must be self-latching to do its job. Specifying dogging on a fire-rated stair
> door is a classic error that gets caught at inspection, after installation. `[CODE][VERIFY]`

---

## Family 5 — Electric bolt / shear lock

Direct-throw bolts into the frame head or the floor, and shear locks that engage a recess.

**Use with strong reservation.** They put a bolt directly in the egress path, they are
alignment-sensitive, they can bind under load precisely when you least want them to, and their
egress story is weak. There are legitimate niches — some sliding doors, some frameless glass,
some interlocks — but if you're reaching for one at a normal swinging door, back up and ask
what constraint pushed you here.

---

## Comparison — the table to internalize

| | Electric strike | Mag lock | Electrified lockset | Electrified exit device |
|---|---|---|---|---|
| **Egress mechanism** | Mechanical (lever) | **Electrical only** | Mechanical (lever) | Mechanical (bar) |
| **Mounts in/on** | Frame | Frame + leaf | Leaf | Leaf |
| **Power transfer needed** | No | No | **Yes** | **Yes** |
| **Fail states available** | Safe or secure | **Safe only** | Safe or secure | Safe or secure |
| **Retrofit friendliness** | Best | Very good | Moderate | Moderate |
| **Alignment tolerance** | Low | **High** | Moderate | Moderate |
| **Attack resistance** | Good (rated) | Moderate — it's a pull force | Good | Good |
| **Latch/bolt monitoring** | Optional | Bond sensor only | **Integral, best-in-class** | Available |
| **Fire door compatible** | Rated versions `[VERIFY]` | Generally no `[VERIFY]` | Yes, fail secure `[VERIFY]` | Yes, fire exit hardware `[VERIFY]` |
| **Additional egress devices required** | None | **REX + push-to-exit + FA interface** | None | None |
| **Where it's the right answer** | Retrofit onto a sound lock and frame | Glass entrances; no suitable lock | Most new interior openings | Anywhere panic hardware is required |

---

## Door position is not latch position

Two different facts. Two different sensors. Juniors report one and believe they have the other.

```
   DOOR POSITION SWITCH (DPS)      →  "the leaf is in the frame"
   LATCH / BOLT MONITORING         →  "the bolt is actually thrown into the strike"

   A door held closed by a closer against the stop, with the latch riding on the
   strike face because the strike is 3 mm out of alignment:

        DPS says:      CLOSED     ✅   (magnet is next to the reed switch)
        Reality:       UNLOCKED   ❌   (a pull opens it)
        Your log says: SECURE
```

This condition is common, invisible, and survives commissioning because commissioning tests
"does the door say closed" rather than "is the door actually latched." **Latch monitoring is
the sensor that catches it.** It costs very little as an ordered option on an electrified
lockset and is essentially impossible to add later.

> 🧠 **Specify latch monitoring at every opening whose alarm actually matters** — data halls,
> evidence rooms, pharmacy, cash handling, MDF/IDF. On lower-consequence openings, DPS alone is
> a defensible economy. Making that distinction deliberately, and writing down why, is the
> difference between a design and a device list.

---

## 🧮 Worked example — power supply and conductor sizing

A floor with 12 electrified openings, all 24 VDC:

| Load | Qty | Standby A each | Peak A each |
|---|---|---|---|
| Electrified mortise lockset | 8 | 0.30 | 0.30 |
| Electric strike | 3 | 0.25 | 0.25 |
| Exit device, electric latch retraction | 1 | 0.30 | 3.00 |

`[MFR][VERIFY]` — always use the actual datasheet. These are plausible values for teaching.

**Step 1 — total the currents.**

```
   Standby:  8(0.30) + 3(0.25) + 1(0.30)  =  2.40 + 0.75 + 0.30  =  3.45 A
   Peak:     8(0.30) + 3(0.25) + 1(3.00)  =  2.40 + 0.75 + 3.00  =  6.15 A

   Design current = max(standby, peak) = 6.15 A
```

**Step 2 — add headroom.** At 25%:

```
   6.15 × 1.25 = 7.69 A   →  specify a supply with ≥ 7.69 A CONTINUOUS output
```

> ⚠️ **The rating trap.** A supply advertised as "10 A" is frequently 10 A *peak* with a lower
> continuous rating, and that rating often assumes it is **not** simultaneously charging a
> depleted battery. Battery charging current adds to load current. Read the datasheet, not the
> model number. `[MFR][VERIFY]`

**Step 3 — battery, for a 4-hour standby requirement.**

```
   Ah_raw   = 3.45 A × 4 h = 13.80 Ah
   Ah_sized = 13.80 × 1.25 (discharge derate) × 1.25 (aging) = 21.56 Ah
```

`[CODE][VERIFY]` — the *required* standby duration is not an engineering preference. It comes
from the applicable standard and the AHJ. The 4 hours above is an assumption for the example.

**Step 4 — the conductor, and the failure everyone misdiagnoses.**

The ELR exit device draws 3.0 A during retraction and sits 150 ft from the supply.

| Conductor | Voltage drop at 3.0 A, 150 ft | Voltage at the device |
|---|---|---|
| 18 AWG | 7.15 V | **16.85 V** ❌ |
| 14 AWG | 2.83 V | 21.17 V ✅ (verify against the device's minimum) |

At 16.85 V, a nominally 24 V latch retraction motor will behave... intermittently. It will work
when the building is cool and the battery is fresh, and fail when it isn't. The symptom
reported to you will be *"the door doesn't unlock sometimes"* and the first three people to
look at it will check the credential, the controller, and the software.

Compare a quiet 0.30 A lockset on the same 250 ft run:

| Conductor | Drop at 0.30 A, 250 ft | At the device |
|---|---|---|
| 18 AWG | 1.19 V | 22.81 V ✅ |

**Same wire, same building, completely different answer** — because current, not distance, is
what turns a wire into a problem.

> 🧠 **Say this out loud until it's reflex: the most common "access control software problem"
> is a voltage problem.** Intermittent, temperature-correlated, worse-when-busy, fine-on-the-
> bench: those are electrical signatures. When an integrator tells you a door is "flaky,"
> your first question is the conductor size and run length, not the firmware version.
>
> Real ELR devices often draw a much larger **inrush** for a few hundred milliseconds before
> settling to a low holding current, which makes this worse than the steady-state numbers
> above suggest. `[MFR][VERIFY inrush, duration, and minimum operating voltage per product.]`

Calculators: [`../28_Calculators/psec/power.py`](../28_Calculators/psec/power.py) —
`power_supply_sizing`, `battery_ah_required`, `voltage_drop_v`, `smallest_awg_for_run`.
**Do the arithmetic by hand first.** Derivations will live in `../32_Engineering_Math/`
(see `../COURSE_PROGRESS.md`).

---

## Selection framework

Work down this list. Stop at the first row that fits.

| If the opening... | Then |
|---|---|
| Requires panic or fire exit hardware | **Electrified exit device.** Prefer electrified trim over ELR unless you need pull-side entry with the latch retracted. |
| Is fire-rated | Fail secure, self-latching. **Electrified lockset** or fire-rated **electric strike** or **fire exit hardware**. Not a mag lock. `[CODE][VERIFY]` |
| Is new construction, interior, ordinary | **Electrified lockset**, fail secure, with latch monitoring |
| Is a retrofit with a sound existing lock and frame | **Electric strike**, after verifying no deadbolt is in play |
| Is glass, has no suitable lock or frame, or has no way to prep the leaf | **Magnetic lock** — and now design the full egress release subsystem `[CODE][VERIFY]` |
| Is anything else | Back up. You're probably solving the wrong problem. |

---

## Design tradeoffs

| Tradeoff | The tension | How to resolve |
|---|---|---|
| Mag lock vs. everything else | Easiest install; only device with no mechanical egress | Use only where nothing else fits, and document why |
| Electric strike vs. electrified lockset (retrofit) | Strike needs no power transfer; lockset gives better monitoring | Strike if the existing lock is sound and monitoring needs are modest |
| ELR vs. electrified trim | ELR allows pull-side entry with the latch out of the way; trim is simpler and far lower current | Trim unless a specific requirement demands ELR |
| Latch monitoring vs. cost | Real security signal; adds cost at every opening | Consequence-tier it. Specify it where the alarm matters. |
| Wired vs. wireless/offline locks | Wireless slashes install cost at scale; loses real-time control and adds battery maintenance | Wired at anything consequential; wireless for breadth at low-consequence interior openings |
| Bigger conductor vs. bigger supply | Both cost money; only one fixes voltage drop | Voltage drop is a conductor and distance problem. A bigger supply does not fix it. |

---

## Common mistakes

⚠️ **Defaulting to a mag lock.** Easiest to install, hardest to justify, permanent code exposure.

⚠️ **Electric strike on a lock with a deadbolt.** Works until someone throws the bolt.

⚠️ **Dogging specified on fire exit hardware.** `[CODE][VERIFY]`

⚠️ **Electrified hardware in the leaf with no power transfer.** Lesson 06. It happens every year.

⚠️ **Sizing a power supply on standby current.** The peak governs.

⚠️ **Undersized conductors on ELR devices.** Produces intermittent failures that get blamed on
software for months.

⚠️ **DPS without latch monitoring at a consequential opening**, then reporting "secure."

⚠️ **Not ordering the monitoring options.** They're order-time selections. Retrofitting them
means replacing the lock.

⚠️ **Trusting an application sheet over the code text** for the egress release arrangement on a
magnetically locked door.

---

## Junior vs. Senior

**Junior:** knows the five families, their mounting locations, their fail states, and which
need power transfer; can select a sensible device for a typical opening; sizes a power supply
using peak rather than standby current.

**Senior:** starts from the egress mechanism and lets it eliminate options before considering
security; can defend every mag lock on the drawing set in one sentence each; specifies latch
monitoring by consequence tier with a written rationale; diagnoses "flaky door" complaints as
voltage problems before touching the software; reads the actual adopted code text for
electrically locked egress rather than the manufacturer's application guide; and knows that the
monitoring options are order-time decisions that cannot be recovered later.

---

## 🔧 Field exercise

Find three access-controlled openings you can observe. For each:

1. Identify the locking family by sight. (Mag: box on the head. Strike: nothing visible in the
   leaf, a plate in the frame. Electrified lockset: normal-looking lock, look for the hinge.
   Exit device: the bar.)
2. Find the power transfer if there should be one — look at the hinges for a wire, or for a
   door loop.
3. Trace the egress story. Stand inside and ask: *if the power is off right now, what does my
   hand do?* Then check whether that actually works.
4. If it's a mag lock: find the REX sensor and the push-to-exit button. If you cannot find both,
   write that down — you have found something worth raising.

---

## Exercises

**E3.1** Select a locking device for each and justify in two sentences:
- (a) 90-minute rated stair door, occupant load requires panic hardware, credentialed re-entry.
- (b) Existing office suite entry, mortise lock with deadbolt, tenant wants badge access next
  month, minimal construction.
- (c) All-glass entrance to a lobby, aluminum frame, no place for a lock case.
- (d) New data hall door, highest consequence tier on the project.
- (e) 400 interior offices in a new building, low consequence, tight budget, owner wants
  audit trail.

**E3.2** 🧮 A wing has 14 electrified locksets at 0.28 A each, 4 electric strikes at 0.22 A
each, and 2 ELR exit devices at 0.25 A standby / 2.8 A peak each, all 24 VDC.
- (a) Compute standby current, peak current, and the recommended supply at 25% headroom.
- (b) Size the battery for a 4-hour standby using 1.25 discharge derate and 1.25 aging.
- (c) One ELR device is 200 ft from the supply. Compute the voltage at the device on 18 AWG
  and on 14 AWG. State which you'd specify and what else you'd verify first.
- (d) The owner asks whether a larger power supply would fix the voltage problem. Answer them.

**E3.3** An integrator reports that Door 214 "sometimes doesn't unlock, mostly in the
afternoon." The credential reads fine, the controller logs a valid grant, and the door is an
ELR exit device 180 ft from the panel. List, in order, the five things you check, and say what
each one would rule in or out.

**E3.4** A drawing set has magnetic locks at 22 of 61 access-controlled openings. Write the
review comment you would issue. Be specific about what you are asking for and why, and be fair
about the cases where a mag lock is legitimately correct.

**E3.5** Explain to an owner, in under 120 words, the difference between a door position switch
and latch monitoring, and why you are recommending the more expensive one at their vault
anteroom but not at their supply closet.

> Solutions: [`_solutions/03_locking_hardware_families_solutions.md`](_solutions/03_locking_hardware_families_solutions.md)

---

## Retrieval check

1. Name the five electrified locking families and the egress mechanism of each.
2. Which family has no mechanical egress, and what does that force you to add?
3. Which families require a power transfer to the leaf?
4. What is the deadbolt trap with an electric strike?
5. What is the difference between panic hardware and fire exit hardware?
6. Why do you size a power supply on peak rather than standby current?
7. What is the difference between door position and latch position, and why does it matter?
8. What is the most common root cause of an intermittent "software" unlock failure?

---

## References

- ANSI/BHMA A156 series — by product class: A156.5 auxiliary locks, A156.13 mortise locks,
  A156.3 exit devices, A156.31 electric strikes, A156.23 electromagnetic locks. `[STANDARD][VERIFY
  numbering against current editions]`
- UL 294 — Access Control System Units. `[STANDARD][VERIFY]`
- UL 10C / UL 10B — fire door assembly testing; relevant to what may be installed on a rated
  opening. `[STANDARD][VERIFY]`
- Applicable building code and life safety code — the sections governing door locking
  arrangements in the means of egress. **Read the adopted text.** `[CODE][VERIFY]`
- DHI — hardware application and specification practice. `[PRACTICE]`
- Manufacturer datasheets — the only authority on current draw, inrush, minimum operating
  voltage, and monitoring options. `[MFR]`

**Next:** [04 — Fail Safe vs. Fail Secure](04_fail_safe_vs_fail_secure.md)
