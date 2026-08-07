# Project 1 — Senior Engineer Reference Solution

> Read only after submitting your own. This is *a* defensible solution, not *the* solution.
> Where your reasoning differs and you can defend it, you may well be right — engineering
> judgment admits more than one good answer. Where your reasoning is *absent*, that's the gap.

---

## The one-paragraph version

A card reader on Room 412 is the *fourth* most valuable thing you can do to this room, and
the first three cost less. The wall stops at 10'-0" below a 13'-6" deck, so the room's actual
boundary is a ceiling tile — roughly **40 seconds of delay** against someone standing on a
chair. Fourteen-plus people hold a key, including three who no longer work there. Nobody
would know about an after-hours entry until Monday. **Fix the boundary, fix the key system,
and add detection — then the reader you were asked for becomes meaningful instead of
ceremonial.**

---

## 1. Risk basis

### Asset register

| Asset | Owner | Life safety | Financial | Operational | Regulatory/legal | Reputational |
|---|---|---|---|---|---|---|
| Servers + NAS (primary file storage, client archive) | IT manager | — | ~$25k replace | **Severe — this is the business** | Depends on data | High |
| Client contracts (signed originals) | Office manager | — | Low | Moderate | **Contractual/evidentiary** | Moderate |
| Personnel files (PII) | Office manager | — | Low | Low | **High — breach notification obligations `[VERIFY jurisdiction]`** | **High** |
| Backup tapes (in safe) | IT manager | — | Low | **Severe if lost with primary** | Depends on data | High |
| Corporate original documents | Principals | — | Low | Moderate | Moderate | Low |
| **Continuity of operations** | Principals | — | **Severe** | **Severe** | — | **Severe** |
| **The client relationship that triggered this** | Principals | — | **Contract value** | — | **The questionnaire answer** | **Severe** |

> ⚠️ **The consequence that justifies the budget is not the $25k of hardware.** It's the
> combination of (a) a business-ending continuity event if primary and backup are taken
> together, and (b) the fact that they have already answered a client questionnaire saying
> access is controlled, monitored, and auditable. Right now that answer is not true. That is
> a contractual and reputational exposure, and it is what you lead with when you present.
>
> Most candidates list the assets and never identify which consequence pays for the project.
> That reframing is the single highest-value thing an engineer contributes at this stage.

### Threats

| ID | Threat | Motivation | Capability | Knowledge | Access | Risk aversion |
|---|---|---|---|---|---|---|
| T1 | **Opportunistic after-hours intruder** (building-wide) | Financial — resaleable equipment | Low; hand tools at most | None of this suite | Must defeat building entry first | High — leaves if challenged |
| T2 | **Insider / former employee** | Grievance, data theft, curiosity | Low tools, **high knowledge** | Complete | **Holds a key** | Moderate — expects not to be detected at all |
| T3 | **Unescorted service personnel** (janitorial, building engineering) | Opportunity | Low | Partial | **Holds a building master, present nightly, unobserved** | High |
| T4 | **Targeted actor after client data** | Financial/competitive | Moderate | Would surveil | Would use T2/T3 paths | Moderate |

**T2 and T3 are the dominant threats and neither is addressed by a card reader alone.** T3 in
particular has *authorized, routine, unobserved* presence — the exact profile that barrier
controls do not touch.

### Vulnerability findings

Written as exploitable weaknesses, not missing devices:

- **V1 — The room's boundary is a ceiling tile.** Partitions terminate at 10'-0" with the
  deck at 13'-6". An intruder in the corridor can stand on furniture, displace a tile, and
  enter over the wall in approximately 30–60 seconds with no tools. *Every other control on
  this door is subordinate to this finding.* Balanced protection is violated: a $3,000 door
  assembly on a $0 wall.
- **V2 — Key control has failed.** At least 14 office master keys are in circulation, three
  of them held by former employees. The building master is held by an unknown number of
  janitorial and engineering staff. **The number of people who can currently open this door
  is unknown to the client**, which is itself the finding.
- **V3 — No detection.** An entry at 0200 Saturday would be discovered Monday morning at the
  earliest, and only if something was visibly missing. Data copied rather than removed would
  never be discovered.
- **V4 — The transfer grille** (24"×24" at 8'-6") is a direct acoustic and visual penetration
  and a bypass path for a reach-through attack on the interior lever `[VERIFY door hardware —
  see §3]`. At 576 in² it is also large enough to warrant a look at whether it is
  person-passable `[VERIFY — commonly cited threshold is 96 in², confirm against your
  applicable requirement]`.
- **V5 — Unescorted service access is unmanaged.** Nightly, unobserved, unlogged presence
  inside the suite by personnel Meridian does not employ, background-check, or supervise.
- **V6 — No audit trail.** The client questionnaire answer ("controlled, monitored, auditable")
  is currently false on all three counts.

---

## 2. Requirements

| ID | Type | Requirement | Traces to |
|---|---|---|---|
| R-01 | C | Free egress from Room 412 shall be maintained at all times without a key, credential, or special knowledge. `[CODE][VERIFY with AHJ]` | Life safety — **non-negotiable, constrains all others** |
| R-02 | F | The Room 412 boundary shall be continuous from floor slab to structural deck on all sides, or shall provide equivalent penetration resistance above the ceiling line. | V1 |
| R-03 | F | Entry to Room 412 shall require an authenticated individual credential; entry events shall be logged with cardholder identity and timestamp. | V2, V6, questionnaire |
| R-04 | F | Room 412 shall be monitored for door position, and shall annunciate forced-open and held-open conditions. | V3 |
| R-05 | P | Held-open annunciation shall occur within 30 s of shunt expiry; forced-open within 3 s. | V3 |
| R-06 | F | Room 412 shall be equipped with volumetric intrusion detection, armed continuously outside 0700–1900 weekdays, reporting to a monitored central station. | V3, V5 |
| R-07 | F | Any access to Room 412 outside published hours shall generate a notification to the IT manager and office manager within 5 minutes. | V3, V5 |
| R-08 | F | The mechanical key system for Room 412 shall be separated from the office master and building master systems, with keys issued individually and recorded. | **V2 — highest value per dollar in this project** |
| R-09 | O | Service personnel (janitorial, building engineering) shall not have unescorted access to Room 412. | V5 |
| R-10 | F | The door controller shall make access decisions from a locally cached credential database and buffer not fewer than 5,000 transactions during loss of communication. | Graceful degradation |
| R-11 | P | Access control and intrusion equipment shall operate for not less than 4 hours on secondary power. `[VERIFY required duration — UL 294 / AHJ]` | Power failure |
| R-12 | F | Access control events for Room 412 shall be retained for not less than 12 months and be exportable for audit. | V6, questionnaire |
| R-13 | C | Work shall not modify the base building fire alarm system, sprinkler system, or demising construction without landlord approval. | Lease |
| R-14 | O | The design shall be maintainable by the existing IT manager without specialist training, and shall self-report device faults. | Ops reality — no SOC, no dedicated staff |

---

## 3. Design narrative

Ordered **by value per dollar**, which is deliberately *not* the order the client asked for.

### 3.1 Close the boundary — $1,200–2,200 (R-02)
Extend the partitions from 10'-0" to the deck at 13'-6" on all four sides, or install
expanded-metal security mesh from the top of wall to deck, fastened to the studs and deck.

Mesh is usually the pragmatic choice: cheaper, faster, does not disturb the ceiling grid as
much, and preserves the plenum return airflow the mechanical system relies on. Extending
gypsum board to the deck may require mechanical coordination and a transfer path, so **ask
the building engineer before you specify it.**

> **This is the single most important item in the project** and it was not in the client's
> request. Without it nothing else matters. Present it first, with the 40-second number.

**Transfer grille (V4):** it exists for return air and cannot simply be removed. Specify a
**security bar set or expanded metal barrier** behind the grille. Also verify the interior
lever is not reachable through it — if the grille is within reach of the lever, that is a
direct bypass and must be addressed regardless.
**Coordinate with the building's mechanical engineer** — you are adding pressure drop to a
return path, and doing so unilaterally is how you get a call about a room that won't cool.

### 3.2 Fix the key system — $400–900 (R-08)
Re-key Room 412 to a **separate keyway, outside the office and building master systems**, on
a restricted/patented keyway so keys cannot be duplicated at a hardware store `[VERIFY
availability with the local locksmith]`. Issue individually. Maintain a key record.

Consequence: **the building master no longer opens this room**, which means janitorial and
building engineering lose unescorted access — which is R-09, achieved as a side effect at
essentially zero marginal cost.

> ⚠️ **Coordinate this with the landlord and the fire department.** Some leases require the
> building master to work everywhere, and some jurisdictions require first-responder access
> `[VERIFY]`. The usual resolution is a **Knox-style box** or a documented escort procedure —
> see `10_Codes_Standards/`. Raise it; do not just re-key and hope.
>
> This item is second only to the wall in value, and it costs less than the reader. Almost no
> candidate proposes it, because it isn't a device.

### 3.3 Detection — $900–1,600 (R-04, R-05, R-06, R-07)
- **Door position switch:** recessed, on the *secure* side, at the top of the door leaf
  opposite the hinge, with a wide-gap magnet if the frame is steel. **Supervised circuit with
  end-of-line resistor** so a cut or shorted wire is distinguishable from an open/closed
  state.
- **Interior motion detector:** PIR, ceiling or corner mount, positioned to cover the door
  approach *and* the volume beneath the ceiling boundary — i.e. it should catch someone
  coming over the wall. This is the control that covers V1 even if the mesh is value-
  engineered out. Arm outside business hours.
- **Report to a monitored central station** plus a push/email notification to the IT and
  office managers (R-07). Given the 45-minute keyholder response, the *notification* is worth
  more than the dispatch.

### 3.4 Access control — $1,400–2,400 (R-03, R-10, R-12)
- **Reader:** the technology depends on the existing suite system. If it is legacy 125 kHz
  proximity, say so plainly: **prox credentials are trivially cloneable and provide no
  meaningful authentication.** Recommend a smart-card or mobile credential migration and note
  that this is a suite-wide decision with its own budget. If migration isn't feasible now,
  install a multi-technology reader so the migration doesn't mean replacing hardware later.
  Specify **OSDP with secure channel** for the reader-to-controller link, not Wiegand.
- **Controller:** use spare capacity on the existing suite panel in the IDF 90 ft away.
  Verify it supports local decision-making and buffering (R-10) — **do not assume it.**
- **Lock:** **electric strike, FAIL SECURE**, with the existing mechanical lockset retained.
  See §3.5.
- **REX:** the door swings **into the room**. On the egress path *out* of the room, occupants
  use the interior lever, which mechanically retracts the latch and provides free egress
  regardless of the electric strike's state — so **R-01 is satisfied by the mechanical
  hardware, not by electronics.** A REX device is therefore **not required for egress**. It
  *is* required to **shunt the DPS** so that a normal exit doesn't generate a forced-door
  alarm. Specify a REX (request-to-exit sensor or a switch in the lockset) **for alarm
  shunting only**, and say so explicitly in the SOO — because this distinction is exactly
  where junior designs go wrong in both directions.

### 3.5 Fail safe vs. fail secure — the decision and the reasoning
**Fail secure.** On loss of power the strike remains locked.

Justification:
- **Egress is unaffected** because free egress is provided mechanically by the interior lever.
  This is what makes fail secure permissible here.
- Room 412 is **not on a required egress path** — it is a terminal room, not a passage.
- Fail safe would unlock the room on any power loss, which is exactly the condition under
  which you least want it unlocked.
- **A magnetic lock would be the wrong choice here** and is worth saying so in writing: it
  fails *unlocked*, it requires code-mandated egress provisions (a listed REX device, and
  typically a labeled emergency release `[CODE][VERIFY — NFPA 101 / IBC access-controlled
  egress provisions, edition and AHJ dependent]`), and it draws power continuously forever.
  None of that is warranted for an interior records room with a functioning mechanical lock.

**Fire alarm interface:** none. This door is not on the egress path and there is no mag lock
to release. `[VERIFY with AHJ]` — but the correct engineering answer is that **you should not
tie this door to the fire alarm**, because doing so would unlock the records room during
every false alarm, and there is no life-safety benefit to offset it. This is a case where the
naive "connect it to fire alarm to be safe" instinct produces a worse outcome.

### 3.6 Video — recommend, with a caveat
One camera in the **corridor** covering the approach to 412 (not inside the room).

- Target: **recognition (≥38 PPF)** at the door plane, not identification. Rationale: the
  population is 62 known employees plus a small set of service personnel. You need to know
  *which known person*, not to identify a stranger to an unfamiliar viewer. Specifying
  identification here would cost more and buy nothing.
- If there is an existing corridor camera (ambiguity #4), **verify its actual coverage and
  pixel density before assuming it's adequate** — "there's a camera there" is not a finding.
- **Caveat to state plainly:** with no monitoring and a 45-minute response, this camera is a
  *recovery* control, not detection or assessment. It documents. Say that.

### 3.7 Procedural controls — ~$0 (R-09, R-12)
- Escort requirement for service personnel entering Room 412.
- **Quarterly access review** — who holds credentials and keys, reconciled against HR.
- Key issuance record with signature.
- Termination checklist including key and credential return.
- Annual test of the intrusion system and the notification path. *Untested notification paths
  silently fail; ask anyone who has discovered their central station account was cancelled.*

These cost nothing and address V2 and V5 more directly than any hardware. **Propose
procedural controls before hardware** — it demonstrates you're solving their problem rather
than selling yours.

---

## 4. Sequence of operation

**Normal access (granted)**
1. Cardholder presents credential to reader R-412.
2. Reader transmits credential data to controller ACP-4 via OSDP (secure channel).
3. ACP-4 evaluates: credential enrolled, not expired, access level includes Door 412, current
   time within assigned schedule. *Decision is made locally by ACP-4 and does not require the
   head-end.*
4. On grant: ACP-4 energizes the strike output for the programmed unlock time (**8 s**), and
   simultaneously shunts the DPS input for the programmed shunt time (**30 s**).
5. Reader annunciates grant (green LED, single tone).
6. Cardholder opens the door. DPS transitions to open. No alarm — input is shunted.
7. Strike de-energizes at end of unlock time and relocks mechanically when the door closes.
8. DPS transitions to closed within the shunt period. Shunt clears. Door secure.
9. ACP-4 generates a "Access Granted" transaction with cardholder ID, door ID, and timestamp,
   and transmits to the head-end (or buffers if offline).

**Access denied**
10. On any failed condition in step 3, ACP-4 withholds the strike output, reader annunciates
    denial (red LED, triple tone), and a "Access Denied — [reason]" transaction is generated.
    Three denials within 60 s generate a notification per R-07.

**Egress**
11. Occupant operates the interior lever. Latch retracts mechanically; door opens **regardless
    of electric strike state or system power**. Free egress is preserved at all times.
12. REX device detects the egress and shunts the DPS for **15 s** to prevent a forced-door
    alarm. *REX shunts the alarm; it does not unlock anything.*
13. A "Request to Exit" transaction is logged.

**Door forced open**
14. DPS transitions to open with no valid grant and no REX active → **"Door Forced Open"**
    alarm within 3 s. Alarm to central station, notification per R-07, event logged.

**Door held open**
15. DPS remains open beyond the 30 s shunt → local reader sounder annunciates as a courtesy
    warning; at shunt + 30 s → **"Door Held Open"** alarm, central station, notification,
    logged.

**Intrusion detection (armed period)**
16. Outside 0700–1900 M–F, the interior PIR is armed. Any activation → **"Intrusion Alarm"**
    to central station within 3 s, notification per R-07, logged.
17. A valid credential presentation at R-412 **disarms** the zone for the duration of the
    authorized entry and re-arms on door close + 60 s of no motion. *This prevents authorized
    after-hours access from generating an intrusion alarm — the omission of which is the most
    common cause of a disabled intrusion system.*

**Loss of communication to the head-end**
18. ACP-4 continues to make access decisions from its local credential database.
19. Transactions buffer locally (≥5,000 per R-10).
20. Forced/held/intrusion alarms annunciate locally and via the central station path, which
    is independent of the head-end.
21. Head-end annunciates "Controller Communication Loss."
22. On restoration, buffered transactions upload with original timestamps.

**Loss of AC power**
23. Power supply transfers to battery. "AC Fail" signal to ACP-4 → event and notification.
24. All functions maintained for ≥4 hours (R-11).
25. **The strike remains locked** (fail secure). Free egress via the mechanical lever is
    unaffected.
26. On battery depletion: door remains **mechanically locked**; electronic access ceases;
    egress remains free. Entry then requires the mechanical key.

**Fire alarm activation**
27. **No interface.** Door 412 is not on a required egress path and has no fail-safe locking
    device. The door remains locked; free egress via the mechanical lever is unaffected and
    is the code-compliant egress means. `[VERIFY with AHJ]`

**Controller failure**
28. Door remains **mechanically locked**. No electronic access; no logging. Egress unaffected.
29. Head-end annunciates comm loss (indistinguishable from network loss until investigated —
    note this as a diagnostic limitation).
30. Recovery: mechanical key access, controller replacement, database re-sync.

---

## 5. Calculations

### 5.1 Power and battery

| Device | Qty | Standby (A ea) | Alarm (A ea) | Standby total | Alarm total |
|---|---|---|---|---|---|
| Reader (OSDP) | 1 | 0.100 | 0.100 | 0.100 | 0.100 |
| Electric strike (fail secure) | 1 | 0.000 | 0.350 | 0.000 | 0.350 |
| DPS | 1 | 0.000 | 0.000 | 0.000 | 0.000 |
| REX (PIR type) | 1 | 0.030 | 0.030 | 0.030 | 0.030 |
| Interior PIR | 1 | 0.030 | 0.030 | 0.030 | 0.030 |
| Controller share | — | 0.150 | 0.150 | 0.150 | 0.150 |
| **Total** | | | | **0.310 A** | **0.660 A** |

Note the fail-secure strike draws **zero** in standby — it's only energized during the 8 s
unlock. That's a real operating-cost advantage over a mag lock, which would draw ~0.5 A
continuously, forever.

**Battery (4 h standby, 5 min alarm):**
```
Ah_standby = 0.310 A × 4 h                = 1.24 Ah
Ah_alarm   = 0.660 A × (5/60) h           = 0.055 Ah
Ah_raw                                     = 1.295 Ah
× derate 1.25 (discharge rate/temp)        = 1.62 Ah
× aging 1.25                               = 2.02 Ah
```
**Specify 7 Ah** — the smallest standard sealed lead-acid size commonly stocked. Massive
headroom, negligible cost difference, and it accommodates future devices. *Don't
over-optimize a $25 component.*

**Power supply:** design current 0.660 A × 1.25 headroom = **0.83 A**, plus battery charging
current per the supply's datasheet. A standard 12/24 VDC 2.5 A supply is appropriate.
`[VERIFY standby duration requirement — UL 294 / AHJ]`

### 5.2 Voltage drop

**The routed length is not 90 ft.** Cable does not travel in straight lines: allow for the
vertical drop from the IDF ceiling, horizontal routing in the cable tray or J-hooks, the
drop at the door, and slack at both terminations. **Use 90 ft × 1.5 + 20 ft of terminations
and slack ≈ 155 ft.** Round to **175 ft** for the cable schedule. *Under-estimating routed
length is one of the most common junior errors and it shows up as an installer standing in a
ceiling 6 ft short of the panel.*

Strike at 0.350 A, 24 VDC supply, 18 AWG:
```
Vdrop = 2 × K × I × L / CM = 2 × 12.9 × 0.350 × 175 / 1624
      = 1580.25 / 1624 = 0.97 V
V at strike = 24.0 − 0.97 = 23.03 V  ✅
```
Comfortably within a typical 24 VDC strike's operating range. **But calculate against the
low end of the supply's output** (a battery-backed supply on standby may sit near 22 V):
`22.0 − 0.97 = 21.03 V` — still acceptable for a strike specified 21.6–26.4 V, though
marginal. **18 AWG is acceptable; 16 AWG is cheap insurance** and is what a careful engineer
specifies here.

### 5.3 Camera (corridor)

2 MP (1920 px H), 1/2.8" sensor (5.37 mm), corridor camera at 12 ft from the door plane,
mounted 9'-0" AFF.

```
Slant range to face plane (5 ft): √(12² + 4²) = 12.65 ft
Choose 6 mm lens:  W = 12.65 × 5.37 / 6 = 11.32 ft
PPF = 1920 / 11.32 = 169.6 PPF  →  IDENTIFY class
Max range for RECOGNISE (38 PPF) = (1920 × 6)/(38 × 5.37) = 56.5 ft
```
Well above the recognition target at the door. A wider lens (2.8 mm) would give
`W = 24.3 ft, PPF = 79` — still identify-class at the door and covering much more corridor.
**Specify a varifocal or the 2.8 mm**, and note that the corridor is narrow so the wide lens's
edge distortion is acceptable here.

### 5.4 Timely detection — and the honest conclusion

Adversary path to the safe (T2/T3 profile, after hours, hand tools):

| Task | Delay (s) | Cumulative |
|---|---|---|
| Enter building (has credential or master) | 30 | 30 |
| Reach 4th floor suite door | 60 | 90 |
| Enter suite (has key/credential) | 15 | 105 |
| Reach Room 412 | 30 | 135 |
| **Enter 412** — *with mesh + re-key: 180 s; without: 40 s* | 180 | 315 |
| Locate and attack safe | 120 | 435 |
| Open safe (basic wall safe, hand tools) | 600 | 1035 |

`T_T = 1035 s`. Detection at entry to 412 (DPS + PIR) = 315 s; assessment (notification read
and acted on) — **realistically 300 s at 0200**, not 20.
`T_D = 615 s`. `T_A = 1035 − 615 = 420 s`. `T_R = 2700 s` (45 min keyholder).

```
Margin = 420 − 2700 = −2280 s  ❌  NOT TIMELY, by 38 minutes.
```

**And that is fine — provided everyone understands it.** State it explicitly in the residual
risk section:

> *This system does not interrupt an after-hours intrusion. With a 45-minute keyholder
> response, no achievable amount of hardware in this budget would. What it does do is
> guarantee that an intrusion is **known within minutes rather than days**, produce a
> reliable record of who accessed the room and when, and remove the ability of 14+ unknown
> keyholders to enter undetected. Those are the objectives this design achieves, and they are
> the ones the client's questionnaire actually asked about.*

Note also what the analysis reveals: **the delay term that moved most was entering 412**
(40 s → 180 s from the mesh), and **the assessment term is the weakest link at 300 s.** If
the client wanted to improve timeliness, the cheapest lever is not more hardware — it's a
faster, more reliable notification path and a nearer keyholder. That's an operations
recommendation, and it belongs in your report.

---

## 6. Residual risk statement (as written for the principals)

> After this work, Room 412 will be a genuinely separate secure space: the walls will go to
> the structure instead of stopping above the ceiling, only the people you choose will have a
> key, every entry will be recorded with a name and a time, and you will be notified within
> minutes if the room is opened outside business hours or if the door is forced.
>
> Three things this does **not** do, which we want you to decide about knowingly:
>
> **1. It will not stop someone who is determined and has time.** With a 45-minute response
> at night, an intruder who gets into the room will have finished before anyone arrives. What
> changes is that you will know it happened immediately, and you will have a record — rather
> than finding out on Monday, as would happen today.
>
> **2. It does not protect against someone you have authorized.** Anyone you give a
> credential to can enter, and the system will record it correctly. Detecting misuse by an
> authorized person requires reviewing the access records periodically — which is why we
> recommend the quarterly access review. It costs nothing and it is the only control that
> addresses this.
>
> **3. Your data is still in one building.** If the servers and the backup tapes are both in
> Room 412, then fire, flood, or a successful theft takes both. **This is the largest
> remaining risk to the business and it is not a security problem — it's a backup problem.**
> An off-site or cloud backup copy would reduce it more than anything in this proposal, and
> would likely cost less. We raise it because it would be wrong not to.
>
> We also recommend you revisit the client questionnaire answer once this work is complete,
> since it will then be accurate.

> 🧠 **Note what point 3 does.** It tells the client that the most valuable thing they could
> do is outside your scope and would reduce your fee. Say it anyway. It is the correct
> engineering answer, and it is the single fastest way to become the consultant they call
> first. This is what "engineering judgment" actually looks like in practice.

---

## 7. Test plan (extract)

| Test ID | Verifies | Procedure | Expected result |
|---|---|---|---|
| CX-01 | R-03 | Present enrolled credential during authorized schedule | Grant; strike releases; event logged with correct name and timestamp |
| CX-02 | R-03 | Present credential outside its schedule | Deny; event logged with reason |
| CX-03 | R-03 | Present a de-activated credential | Deny; event logged |
| CX-04 | R-01 | With system powered **and** with power removed, operate interior lever | Door opens freely in both cases, no key, no special knowledge |
| CX-05 | R-04/05 | Force door open without a grant | Forced-open alarm ≤ 3 s at central station; notification received |
| CX-06 | R-04/05 | Hold door open past shunt | Held-open alarm within 30 s of shunt expiry; notification received |
| CX-07 | R-04 | Exit via REX | DPS shunted; **no** forced-door alarm; REX event logged |
| CX-08 | R-06 | Trip PIR during armed period | Intrusion alarm ≤ 3 s; notification received |
| CX-09 | R-06/SOO 17 | Valid credential during armed period, then enter | Zone disarms; **no** intrusion alarm; re-arms 60 s after door close |
| CX-10 | R-10 | Disconnect controller uplink; present valid credential | Grant still occurs; event buffers; head-end shows comm loss; on restore, event appears with original timestamp |
| CX-11 | R-11 | Remove AC; monitor for 4 h | All functions maintained; AC-fail event generated; door remains locked; egress remains free |
| CX-12 | R-02 | Physical inspection above ceiling, all four sides | Mesh/wall continuous to deck; no gaps > [specified]; fastened per detail |
| CX-13 | V4 | Physical inspection of transfer grille | Barrier installed; interior lever not reachable through grille |
| CX-14 | R-08 | Attempt entry with office master and building master keys | **Both fail.** Room key operates |
| CX-15 | R-07 | Generate an after-hours access event | Notification received by both IT and office manager within 5 min |
| CX-16 | R-12 | Export 30 days of events | Export succeeds in a readable format with identity and timestamp |

> **CX-14 is the test nobody writes and everybody should.** "We re-keyed it" is a claim.
> Trying the old keys is a verification. The number of re-keying jobs that quietly miss a
> cylinder is not small.

---

## What most people miss on this project

Ranked by how often, and how much it costs:

1. **The ceiling plenum.** The most common miss and the most consequential. If you only found
   one thing you missed, this should be it.
2. **The key system.** Second-highest value, lowest cost, almost never proposed — because it
   isn't a device, and the brief said "card reader."
3. **Coordinating the re-key with the landlord and fire access.** Doing the right thing in a
   way that creates a lease violation or a code problem is not the right thing.
4. **REX purpose.** Either specifying it "for egress" (wrong — the lever provides egress) or
   omitting it entirely (wrong — the DPS will alarm on every exit). It is for **alarm
   shunting**.
5. **Arguing for fail secure explicitly**, rather than defaulting to it silently. And
   recognizing that a mag lock would be actively wrong here.
6. **Not tying the door to the fire alarm.** The reflex is to connect everything to fire
   alarm "to be safe." Here it would unlock the records room on every false alarm for no
   life-safety benefit.
7. **Realistic assessment time.** Using 20 s for assessment at 0200 when the "operator" is an
   IT manager asleep at home. The honest number is minutes, and it changes the conclusion.
8. **Routed cable length.** 90 ft on a plan is ~175 ft of cable.
9. **The backup problem.** The largest residual risk is outside the scope you were given, and
   raising it is the job.
10. **Saying plainly what the system is for.** A design that documents rather than prevents
    is a legitimate design — but only if the client knows that's what they bought.

---

## Carry forward to Project 2

- The zone-integrity check (nine elements) — you will run it on every secure space forever.
- Fail safe/fail secure reasoning — this recurs on every door for the rest of your career.
- The habit of ordering recommendations by **value per dollar** rather than by what was asked.
- Writing residual risk for the actual decision-maker.
- Computing timely detection and then saying honestly what the system achieves.
