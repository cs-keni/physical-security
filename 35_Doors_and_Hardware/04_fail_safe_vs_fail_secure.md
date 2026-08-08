# 04 — Fail Safe vs. Fail Secure

## Learning objectives

- Define fail safe and fail secure precisely, and explain what each word refers to.
- Explain why **fail secure does not trap anyone**, and why believing otherwise leads to
  systematically worse designs.
- Distinguish the **fail state of a lock** from the **degraded behavior of a system**, and
  design each deliberately.
- Enumerate the five distinct failure modes an opening can experience and specify the desired
  behavior for each.
- Explain why the fire alarm release must be a hardwired path and not a software integration.
- Choose and document a fail state for any opening, and get it onto the drawing where the
  contractor will actually read it.

---

## ELI5

An electric lock has to do *something* when the power goes out. There are only two choices:

- **Fail safe** — it **unlocks**. ("Safe" = safe for *people*.)
- **Fail secure** — it stays **locked**. ("Secure" = secure for *property*.)

That's the whole definition. The words tell you what the lock protects when it dies.

The part everyone gets wrong: **fail secure does not lock people in.** On almost every kind of
lock, the inside handle is purely mechanical and always works. Fail secure locks the *outside*.

---

## The precise definitions

| Term | State with **no power** | What it protects on failure |
|---|---|---|
| **Fail safe** | **Unlocked** | People — the barrier disappears |
| **Fail secure** | **Locked** | Property — the barrier persists |

Both terms describe **the lock's behavior in the absence of power**. Nothing else.

### Banish "fail open" and "fail closed"

You will hear these constantly. Refuse to use them, and gently push back when others do,
because they are genuinely ambiguous:

- "Open" could mean the *door* is open, or the *electrical circuit* is open (which
  de-energizes the lock, which for a fail-secure device means **locked**).
- Two engineers using "fail open" in the same meeting can mean exactly opposite things and
  neither will notice.

When there is any doubt, use the unambiguous long form on the drawing:

> **"Locked on loss of power"** / **"Unlocked on loss of power"**

That phrasing has never been misread by anyone.

---

## The correction that changes how you design

**Fail secure does not trap people.**

Look at the egress mechanism from lesson 03 again:

```
   ELECTRIFIED LOCKSET, FAIL SECURE, POWER COMPLETELY DEAD

        OUTSIDE                              INSIDE
        ───────                              ──────
     lever is rigid,                    lever is MECHANICAL,
     will not retract latch             always retracts the latch
     (this is the "secure" part)        (this is never controlled,
                                         never electrified, never
        ✋ no entry                        dependent on power)

                                        🚪 person turns lever, walks out
```

The inside lever on an electrified lockset, and the push bar on an exit device, are
**mechanical linkages**. They are not part of the electrified function. They work with the
power off, the controller dead, the network gone, and the building on fire.

So the honest reading of "fail secure" is: **"on power loss, stop granting entry; egress is
unaffected because egress was never electrical."**

> 🧠 **Why this matters more than it sounds:** juniors who believe fail secure is dangerous
> specify fail safe everywhere "to be safe." The result is a building that **unlocks itself
> when the power goes out** — which is (a) a security failure the owner never agreed to, and
> (b) an attack surface, because interrupting power is often easy. They have traded a real
> security property for a life-safety benefit that they were already getting mechanically.
>
> **Fail secure is the correct default for most openings**, precisely because it is safe.

---

## When fail safe is actually required

Fail safe is not a preference you sprinkle on. It's a requirement that comes from one of these:

1. **The device has no mechanical egress.** A magnetic lock is fail safe because there is no
   other option. This is physics.
2. **Code requires the lock to release** on power loss, on fire alarm, or on both, for that
   opening in that occupancy. This is the big one and it is prescriptive.
   `[CODE][VERIFY — the arrangements permitted for electrically locked doors in the means of
   egress differ by code, by adopted edition, and by occupancy. Design from the adopted text
   and confirm with the AHJ.]`
3. **Stairwell re-entry.** Where stair doors are locked against re-entry from the stair, code
   commonly requires them to unlock automatically on fire alarm so occupants are not trapped in
   the stair. `[CODE][VERIFY]`
4. **A specific operational requirement**, documented — for example, an opening whose function
   is to release a controlled area on evacuation.

If a fail-safe device is on your drawing and it isn't for one of those four reasons, ask why.

---

## The five failure modes

This is the part that separates a real design from a checkbox. "Fail state" is usually
discussed as if there were one failure. There are at least five, they are independent, and the
correct behavior differs across them.

| # | Failure | Fail-secure lockset | Mag lock | What the owner probably expects |
|---|---|---|---|---|
| 1 | **AC power lost, battery holding** | Normal operation | Normal operation | Everything keeps working — and it does, for the battery's duration |
| 2 | **Total power loss (battery exhausted)** | **Locked.** Egress fine. No entry. | **Unlocked.** Building is open. | Almost never thought about. Ask. |
| 3 | **Fire alarm activation** | Stays locked unless specifically released; **egress is mechanical so this is fine** | **Must release** — hardwired | People get out; responders get in |
| 4 | **Access control head-end / server failure** | Depends on **controller** design, not the lock | Depends on controller | "The doors still work," which is only true if controllers hold their own database |
| 5 | **Network loss between controller and server** | Controller runs offline with cached credentials, *if it was specified to* | Same | Same |

Three things fall out of this table:

**(a) Failure modes 4 and 5 are not lock questions at all.** They are access control system
architecture questions — does the door controller retain its credential database and its
schedule locally, and for how long? A "fail secure" lock on a controller that goes brain-dead
without the server means nobody enters. That may be correct for a data hall and unacceptable
for a hospital medication room. This is where the lesson hands off to
`../04_Access_Control/` — but the *question* originates here.

**(b) Mode 2 is the one nobody asks about, and it's where mag locks are worst.** A building
full of mag locks, after the batteries run out, is a building with no locks. Whether that is
acceptable is the owner's call — but it has to be an actual call, made out loud, and almost
nobody makes it.

**(c) Mode 3 is a code question with a *wiring* answer.** See below.

> 🧠 **The senior habit: for every failure mode, write the sentence "when X happens, this door
> is ___ and people ___." Five sentences per opening type, not per opening.** It takes fifteen
> minutes for a whole project and it catches things that no review checklist catches, because
> it forces you to say the consequence out loud rather than tick a column.

---

## The fire alarm interface

For any opening where fire alarm activation must release the lock, the release path must be a
**hardwired, fail-safe electrical path**, typically a dry contact from the fire alarm system
that physically breaks the power to the lock (or to a relay that does).

**It must not be a software integration between the fire alarm system and the access control
system.** `[CODE][VERIFY — confirm the required arrangement against the adopted code and with
the AHJ.]`

Reasons, and you should be able to give all three:

1. **The failure mode is wrong.** A software integration fails silently. A message doesn't
   arrive, a service is down, a firewall rule changed, a certificate expired — and nothing
   happens, and nobody knows until the fire. A hardwired normally-closed contact fails to the
   *released* state, because a cut wire is indistinguishable from an alarm.
2. **The dependency chain is wrong.** A software path depends on two servers, a network, and
   two vendors' software versions staying compatible for the twenty-year life of the building.
   A relay depends on a relay.
3. **It isn't testable the same way.** The commissioning test for a hardwired release is
   "activate the alarm, watch the door release." That test can be repeated by a facilities tech
   forever. Testing a software integration meaningfully requires people who won't be there.

```
   RIGHT                                    WRONG

   FA panel                                 FA panel
      │ dry contact (N.C.)                     │ network
      ▼                                        ▼
   breaks power to lock                     FA head-end software
      │                                        │ integration / API
      ▼                                        ▼
   lock releases                            ACS head-end software
                                               │ command
   Cut wire = released ✅                       ▼
   Server down = released ✅                 controller → lock
   Nobody home = released ✅
                                            Any link down = NOTHING HAPPENS ❌
```

> ⚠️ **This gets proposed regularly**, usually by someone enthusiastic about integration, and it
> sounds modern and elegant. It is the wrong architecture for a life-safety function, for the
> same reason you don't implement a hardware interlock in application code. Be ready to say so
> clearly and without condescension, because the person proposing it is usually smart and
> genuinely trying to help.

---

## The decision framework

```
   START: this opening will be electrically locked.

   ├─ Is it a magnetic lock?
   │     └─ YES → FAIL SAFE (no choice) + full egress release subsystem
   │              + hardwired FA release   [CODE][VERIFY]
   │
   ├─ Does the adopted code require release on power loss or on fire alarm
   │  for this opening, in this occupancy, in this means of egress?
   │     └─ YES → FAIL SAFE, hardwired release, documented code citation
   │              [CODE][VERIFY]
   │
   ├─ Is it a stair door subject to re-entry requirements?
   │     └─ YES → FAIL SAFE on fire alarm  [CODE][VERIFY]
   │
   ├─ Is it a fire-rated opening?
   │     └─ YES → FAIL SECURE and self-latching. A fire door must latch.
   │              [CODE][VERIFY]
   │
   └─ Otherwise → FAIL SECURE.
         Egress is mechanical. Entry stops on power loss. This is the default
         and it is the safe choice, not the risky one.

   THEN, for every branch, answer separately:
     • What happens when the controller loses the server?      (ACS architecture)
     • What happens when the battery is exhausted?             (ask the owner)
     • What is the mechanical key override, and who holds it?  (lesson 08)
```

---

## Worked decisions

| Opening | Fail state | Why |
|---|---|---|
| Data hall door, electrified mortise lockset | **Fail secure** | Egress mechanical via inside lever. Power loss must not open the highest-consequence space. |
| 90-min rated stair door, fire exit hardware, credentialed re-entry | **Fail secure** latch, **fail safe release of the re-entry function on FA** | The door must self-latch (fire), and re-entry must be available on alarm. Two requirements, one opening. `[CODE][VERIFY]` |
| Glass lobby entrance, magnetic lock | **Fail safe** | No mechanical egress exists. Plus REX, push-to-exit, and hardwired FA release. |
| Tenant suite entry, electric strike retrofit | **Fail secure** | Egress mechanical via inside lever. Default. |
| Electrical room, panic hardware required | **Fail secure** | Egress by bar. The room must stay secured on power loss — arguably more so, since a power event is exactly when someone might go in there. |
| Pharmacy / controlled substances | **Fail secure** | Regulatory and consequence-driven. Confirm any AHJ-specific requirement. `[VERIFY]` |
| Area of refuge / evacuation-path door under a specific code provision | **Per code text** | Do not reason from analogy here. Read the section. `[CODE][VERIFY]` |

Notice that the answer is **fail secure** most of the time. That's the point of the lesson.

---

## Getting it onto the drawing

A fail state that lives only in your head is not a design decision; it's a preference.

**It must appear in at least two places:**

1. The **hardware set** in the specification — "Electric strike, fail secure, 24 VDC, latch
   monitoring."
2. The **security drawings / door schedule** — as an explicit column or note, not as an
   inference from the device type.

**Why it matters:** most electrified devices are order-time configurable and many manufacturers
ship a **default** fail state that varies by product line. If the submittal says "electric
strike" and nothing else, the contractor orders the default, the default is whatever it is, and
you find out at commissioning — or in year three, during a power outage, when the wrong doors
open.

> ⚠️ **Some devices are field-convertible between fail safe and fail secure (a jumper or a
> mechanical reversal) and some are not.** Do not assume you can correct this later.
> `[MFR][VERIFY per product]`

**In the device data model** (`../16_Automation/data_model/`), fail state is a field, and it
should be one of the values the validator checks for presence and for consistency with the
opening's rating and function. That is exactly the class of repetitive check worth automating —
and exactly the class of *judgment* (is fail safe correct here?) that must not be.

---

## Design tradeoffs

| Tradeoff | The tension | How to resolve |
|---|---|---|
| Fail safe vs. fail secure | Safe releases on power loss; secure preserves the barrier | Fail secure unless code, device physics, or a documented requirement says otherwise |
| Battery duration vs. cost | Longer standby delays the mode-2 failure | Size to the required standby, then ask the owner what should be true after it |
| Hardwired FA release vs. integrated release | Integration is elegant and cheaper to wire | Hardwired. Life-safety functions do not run on application software. |
| Controller offline capability vs. cost | Local credential caching keeps doors working when the server dies | Specify offline behavior explicitly per door group; don't inherit the vendor default |
| Mechanical key override vs. key control burden | Override guarantees access when everything is dead; every key is a risk | Always have the override; manage it properly (lesson 08) |

---

## Common mistakes

⚠️ **Saying "fail open" or "fail closed."** Ambiguous. Two people, opposite meanings, same word.

⚠️ **Believing fail secure traps people.** It doesn't. Egress is mechanical.

⚠️ **Specifying fail safe everywhere "to be safe."** Produces a building that unlocks itself.

⚠️ **Not specifying the fail state at all.** The contractor orders the default.

⚠️ **Implementing the fire alarm release as a software integration.**

⚠️ **Confusing lock fail state with system degraded mode.** Different questions, different
subsystems, both need answers.

⚠️ **Never asking what happens after the battery dies.**

⚠️ **Assuming the device is field-convertible.**

⚠️ **Reasoning about egress code requirements by analogy to the last project.** Occupancy,
code, and adopted edition all change the answer. `[CODE][VERIFY]`

---

## Junior vs. Senior

**Junior:** defines both terms correctly, knows fail secure is the usual default, knows a mag
lock is fail safe by necessity, and gets the fail state onto the hardware set.

**Senior:** treats the five failure modes as five separate design questions and writes the
consequence sentence for each; recognizes that failure modes 4 and 5 are access control
architecture rather than hardware, and raises them at the right time with the right team;
insists on a hardwired fire alarm release and can explain why in terms a smart integrator will
accept; asks the owner the mode-2 question out loud; and treats the code determination as
something to be read and cited rather than remembered.

---

## 🔧 Field exercise

Pick one access-controlled opening you can safely observe. Without touching anything, write the
five sentences:

1. "When AC power is lost but the battery is holding, this door is ______ and people ______."
2. "When the battery is exhausted, this door is ______ and people ______."
3. "When the fire alarm activates, this door is ______ and people ______."
4. "When the access control server fails, this door is ______ and people ______."
5. "When the network to this controller drops, this door is ______ and people ______."

You will not be able to answer 4 and 5 by looking. **That is the finding.** Note who you'd have
to ask, and what document should have told you.

---

## Exercises

**E4.1** State the fail state and justify in one sentence each:
- (a) Server room, electrified mortise lockset, no panic hardware required.
- (b) Stair door, floor-to-stair, 90-min rated, re-entry required on alarm.
- (c) All-glass lobby entrance with a magnetic lock.
- (d) Loading dock personnel door, out-swinging, electric strike retrofit.
- (e) Cash counting room in a retail back-of-house.

**E4.2** A colleague argues that all doors on the egress path should be fail safe "because life
safety comes first." Write a response of no more than 150 words that agrees with their
principle, corrects their conclusion, and does not condescend.

**E4.3** An integrator proposes releasing the mag locks at the lobby via an API call from the
fire alarm head-end to the access control head-end, noting it gives better logging and avoids
running new conduit. List every failure mode this introduces and state your position.

**E4.4** For a 12-story office building with fail-secure electrified locksets throughout and a
4-hour battery: write the memo paragraph that tells the owner what is true at hour 5 of a
regional power outage, and the two options they have. Do not recommend one — present the
decision.

**E4.5** You inherit a drawing set. The door schedule lists device types but has no fail-state
column. Describe the correction you would make and every document it must propagate to.

> Solutions: [`_solutions/04_fail_safe_vs_fail_secure_solutions.md`](_solutions/04_fail_safe_vs_fail_secure_solutions.md)

---

## Retrieval check

1. Define fail safe and fail secure. What does each word refer to?
2. Why should you never say "fail open"?
3. Why does fail secure not trap anyone at an electrified lockset?
4. Name the four situations that genuinely require fail safe.
5. List the five failure modes and say which two are not lock questions.
6. Why must the fire alarm release be hardwired?
7. Where must the fail state appear so that the right device gets ordered?

---

## References

- Applicable building code and life safety code — the sections on door locking arrangements in
  the means of egress, stairway re-entry, and electrically locked egress doors. **Read the
  adopted text; cite the section in your design.** `[CODE][VERIFY]`
- NFPA 72 — fire alarm system interfaces and the required arrangement of releasing devices.
  `[STANDARD][VERIFY]`
- UL 294 — Access Control System Units; addresses endurance, standby, and destructive attack
  levels. `[STANDARD][VERIFY]`
- ANSI/BHMA A156.31 (electric strikes), A156.23 (electromagnetic locks) — fail state options by
  product class. `[STANDARD][VERIFY]`
- Manufacturer datasheets — for whether a specific device is field-convertible. `[MFR]`
- `../10_Codes_Standards/` — how to find and cite the adopted edition for a jurisdiction.

**Next:** [05 — Egress, Delayed Egress, and Controlled Egress](05_egress.md)
