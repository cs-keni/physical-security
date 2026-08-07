# 04 — Defense in Depth, Layers, and Security Zones

## Learning objectives

- Explain defense in depth and why it is a *time* strategy, not a *strength* strategy.
- Lay out concentric security zones for a facility and define the transition control at each boundary.
- Apply balanced protection and identify the weakest penetration path through a boundary.
- Distinguish redundancy, diversity, and graceful degradation, and know when each is warranted.
- Identify single points of failure in a security system architecture.

---

## ELI5

A castle doesn't have one enormous wall. It has a moat, then a wall, then a courtyard, then
an inner wall, then a keep. Not because any one of them is unbeatable — but because getting
through all of them takes a long time, and during that long time, guards are watching, horns
are blowing, and soldiers are arriving.

Each layer buys minutes. The minutes are the point.

---

## Defense in depth, defined properly

**Defense in depth** is the deliberate arrangement of protection measures in successive
layers along an adversary's likely path, such that the adversary must defeat multiple
independent measures in sequence, and such that each defeat produces detection and consumes
time.

Three words carry the meaning:

- **Successive** — arranged along the path, in sequence. Layers side by side are not depth.
- **Independent** — defeating one must not defeat the others. A master key that opens the
  perimeter door, the suite door, and the server room collapses three layers into one. So
  does a single access control server whose failure unlocks everything, or a single VLAN
  where compromising any camera reaches the VMS.
- **Detection at each** — a layer that is defeated silently only contributes delay, and
  (from lesson 03) delay before detection is nearly worthless.

> **Defense in depth is not "more security." It is "security arranged in series."** You can
> spend twice as much and have *less* depth if you spend it all on one boundary.

### The software analogy (and where it breaks)

You know this pattern: WAF → authentication → authorization → input validation → least
privilege → encryption at rest → monitoring. Same idea: no single control is trusted, an
attacker must chain multiple failures, and every layer logs.

**Where it breaks:** in software, layers are nearly free to add and defeating one takes an
attacker seconds. In physical security, layers cost real money and physically defeating one
takes *minutes you can compute*. That computability is a gift — you can actually calculate
whether your depth is sufficient (lesson 03). Software security has no equivalent of a
delay time in seconds.

---

## Security zones — the organizing framework

A **security zone** is a contiguous area with a uniform protection requirement and a defined,
controlled boundary. The classic model is concentric:

```
 ┌───────────────────────────────────────────────────────────────────┐
 │  ZONE 0 — PUBLIC / UNCONTROLLED                                   │
 │  Street, public sidewalk, approach. No control. CPTED + observation │
 │                                                                     │
 │  ┌─────────────────────────────────────────────────────────────┐  │
 │  │  ZONE 1 — CONTROLLED / SITE PERIMETER                        │  │
 │  │  Owned property, parking, yard.                              │  │
 │  │  Boundary: fence/landscape/bollards. Control: vehicle gate,  │  │
 │  │  visible cameras, lighting, signage.                         │  │
 │  │                                                               │  │
 │  │  ┌───────────────────────────────────────────────────────┐  │  │
 │  │  │  ZONE 2 — RECEPTION / SEMI-PUBLIC INTERIOR             │  │  │
 │  │  │  Lobby, visitor waiting, public counters.              │  │  │
 │  │  │  Boundary: building envelope. Control: staffed         │  │  │
 │  │  │  reception, visitor processing, cameras.               │  │  │
 │  │  │                                                         │  │  │
 │  │  │  ┌─────────────────────────────────────────────────┐  │  │  │
 │  │  │  │  ZONE 3 — EMPLOYEE / RESTRICTED                  │  │  │  │
 │  │  │  │  General work areas.                             │  │  │  │
 │  │  │  │  Boundary: access-controlled doors/speedgates.    │  │  │  │
 │  │  │  │  Control: badge, DPS, REX, escort rules.          │  │  │  │
 │  │  │  │                                                   │  │  │  │
 │  │  │  │  ┌───────────────────────────────────────────┐  │  │  │  │
 │  │  │  │  │  ZONE 4 — SENSITIVE / HIGH SECURITY        │  │  │  │  │
 │  │  │  │  │  MDF, server room, cash room, lab, records │  │  │  │  │
 │  │  │  │  │  Boundary: slab-to-slab, rated door.       │  │  │  │  │
 │  │  │  │  │  Control: MFA, IDS when unoccupied,        │  │  │  │  │
 │  │  │  │  │  camera at door, logged, audited.          │  │  │  │  │
 │  │  │  │  │                                             │  │  │  │  │
 │  │  │  │  │      ┌───────────────────────────┐         │  │  │  │  │
 │  │  │  │  │      │ ZONE 5 — CRITICAL          │         │  │  │  │  │
 │  │  │  │  │      │ Cage, vault, HSM, safe.    │         │  │  │  │  │
 │  │  │  │  │      │ Two-person rule, biometric,│         │  │  │  │  │
 │  │  │  │  │      │ continuous video, escort.  │         │  │  │  │  │
 │  │  │  │  │      └───────────────────────────┘         │  │  │  │  │
 │  │  │  │  └───────────────────────────────────────────┘  │  │  │  │
 │  │  │  └─────────────────────────────────────────────────┘  │  │  │
 │  │  └───────────────────────────────────────────────────────┘  │  │
 │  └─────────────────────────────────────────────────────────────┘  │
 └───────────────────────────────────────────────────────────────────┘
```

Most facilities use 3–5 zones. Naming varies by client and sector (Public / Reception /
Restricted / Secure / Critical is common; government and DoD have their own formal
terminology `[VERIFY per applicable directive]`). **Adopt the client's naming, don't impose
yours.**

### The four questions for every zone boundary

For each boundary, you must be able to answer:

1. **Who may cross, in which direction?** (Often asymmetric — free egress, controlled ingress.)
2. **How is authorization verified?** (Nothing / visual / badge / badge+PIN / badge+biometric / escort)
3. **How is a crossing recorded, and how is an unauthorized crossing detected?**
4. **What happens at this boundary during fire alarm, power loss, and network loss?**

If you can answer all four for every boundary in a facility, you have a security concept.
That's genuinely most of schematic design.

### Zone integrity — the rule people break constantly

**A zone boundary must be continuous in three dimensions.** The boundary of a zone is not
the door; it is the entire enclosing surface: walls, doors, windows, floor, ceiling, and
every penetration through them.

The canonical failure: a "secure" server room with a card reader, a rated door, and
partition walls that stop at the suspended ceiling grid, with a continuous plenum to the
corridor. Someone stands on a chair. Total delay: 40 seconds. You have specified a $3,000
door on a $0 wall.

**The checklist for zone boundary integrity:**

| Element | Question |
|---|---|
| Walls | Slab to slab? Construction type? Can they be cut quickly? |
| Ceiling | Is there a plenum path over the wall from a lesser zone? |
| Floor | Raised floor with a path underneath? Slab penetrations? Floor below? |
| Doors | Rating, frame, hinges, strike/lock, gap, glazing, undercut |
| Windows | Glazing type, operable?, ground floor?, adjacent roof access? |
| Penetrations | Ducts (>96 in² is a person-passable concern `[VERIFY]`), conduits, cable trays, chases, pipe sleeves |
| Roof | Hatches, skylights, mechanical wells, adjacent structures that enable access |
| Adjacencies | What's on the other side of every wall? Who has access to *that* space? |
| Egress hardware | Does the required egress path from within create an entry path from without? |

> 🧠 That last row is subtle and important: a stairwell that must be free-egress in the exit
> direction can be an *entry* path from a less-secure floor. Stair door hardware and floor
> re-entry strategy is one of the most-argued topics in multistory security design (module
> `35_Doors_and_Hardware/05`).

---

## Balanced protection

**Balanced protection:** all penetration paths through a boundary should present approximately
equal delay to an adversary.

You do not achieve this by making everything maximum-strength; you achieve it by finding the
weakest path and either strengthening it or accepting that it defines the boundary's real
delay — and then not overspending on the other paths.

**The engineering discipline:**

1. Enumerate every penetration path through the boundary.
2. Estimate delay for each, against your stated adversary and toolset.
3. The boundary's delay = **minimum** of those.
4. If the minimum is unacceptable, fix the minimum. Repeat.
5. Stop when the boundary's delay meets the requirement from your timely-detection
   calculation. **Do not keep strengthening past that point** — the money belongs elsewhere.

> ⚠️ Step 5 is the one that separates engineers from salespeople. Once the boundary meets the
> requirement, further hardening buys nothing measurable. If a client wants more anyway,
> that's their prerogative — but you should tell them what it does and doesn't buy.

**Where balance is *deliberately* violated:** you may accept a weaker path if it is
compensated by *detection* rather than delay. A large window that could be defeated in
15 seconds is acceptable if glass-break plus interior motion detects it immediately and the
response is fast enough. That's a legitimate trade of delay for detection — just make it
consciously, and write it down.

---

## Redundancy, diversity, and graceful degradation

Three different concepts, constantly conflated.

### Redundancy — a second identical thing
Two recording servers. Two power supplies. Dual uplinks.
**Protects against:** random component failure.
**Does not protect against:** a design flaw or an attack that affects both identically. Two
identical cameras with the same firmware vulnerability are not redundant against that
vulnerability. Two servers on the same UPS are not redundant against a UPS failure.

### Diversity — a second *different* thing achieving the same function
A PIR sensor *and* a microwave sensor. A door contact *and* a camera analytic. Access logs
*and* video. Network path over fiber *and* over a separate carrier.
**Protects against:** common-mode failure and environmental conditions that defeat one
technology. Also against *defeat* — an adversary who knows how to mask a PIR may not defeat
the microwave simultaneously.
**Costs:** more complexity, more integration, more to maintain, more to commission.

> **The rule:** use **redundancy** against *failure*; use **diversity** against *defeat and
> environment*. Against a thinking adversary, diversity is worth more than redundancy.

### Graceful degradation — the system loses capability progressively, not totally
When the network to a building is lost:
- **Brittle design:** all doors free-exit and free-*entry*, no logging, no alarms. Total loss.
- **Graceful design:** controllers continue making access decisions from their local cached
  database, buffer transactions to memory, maintain locking, alarm locally on forced/held
  doors, and upload the buffer when the link restores. Degraded (no real-time monitoring, no
  credential changes) but *functional*.

**Graceful degradation is a design requirement you must write down**, because it is a
purchasing decision (does the controller have local decision-making and adequate buffer?) and
a configuration decision (offline mode behavior). It is one of the highest-value things a
junior engineer can learn to specify, because it's cheap at design time and impossible to
retrofit.

**The degradation questions to answer for every system:**

| Loss | Cameras | Access control | Intrusion |
|---|---|---|---|
| Network to head-end | Recording? Edge storage? For how long? | Local decisions? Buffer depth? | Local siren? Dialer backup? |
| Power (utility) | UPS runtime? Generator? Which cameras are on standby power? | Battery runtime? Which doors fail how? | Battery runtime (code-referenced minimums `[VERIFY]`) |
| Head-end server | Failover? Manual? How long? | Controllers autonomous? For how long? | Monitoring path? |
| A single switch | How many cameras dark? Is that acceptable? | How many doors offline? | — |

---

## Single points of failure

A **single point of failure (SPOF)** is any element whose failure disables a function across
a large scope. Finding them is a review skill you'll use constantly.

**Common SPOFs in security systems — check every design for these:**

| SPOF | Consequence | Typical mitigation |
|---|---|---|
| One head-end room | Fire/flood there kills everything | Distributed or secondary head-end; at minimum, don't co-locate with high-hazard equipment |
| One network switch serving a floor | All devices on that floor dark | Split critical devices across switches; dual-home key devices |
| One uplink / one fiber path | Building isolated | Diverse physical routing (not just two strands in one conduit — that's not diversity) |
| One power supply serving many doors | Many doors fail simultaneously | Distribute; size for zones; battery backup |
| One UPS | Everything drops together | Separate UPS per critical function; generator |
| One access control server, no failover | No credential changes, no monitoring | Redundant/hot-standby server; **and** controllers with local decision-making |
| One recording server for many cameras | Loss of all evidence for that group | Failover recording; N+1 |
| One administrator account | Compromise or departure = total loss | Role-based access, MFA, break-glass procedure, documented |
| One person who knows the system | Bus factor of 1 | Documentation, as-builts, training, credential escrow |
| Shared conduit for all cabling | One cut, everything | Diverse pathways for critical circuits |
| Single vendor / single product line | EOL or business failure strands you | Open standards (ONVIF, OSDP), documented migration path |

> 🧠 **The last two rows are the ones people forget.** "One person who knows the system" is
> the most common real-world SPOF in security operations, and it is an *engineering*
> responsibility — the as-builts, the O&M manuals, and the device schedules you produce are
> the mitigation.

**A useful review habit:** on any riser or block diagram, put your finger on each box and
line in turn and ask "if I delete this, what stops working?" Anything whose deletion kills
more than you're comfortable with is a finding.

---

## Zones in practice — worked example

**Facility:** three-story professional office, 40,000 sq ft, single tenant, ~180 employees,
a small data room, an HR records room, and a lobby with a receptionist 0800–1700.

| Zone | Areas | Boundary | Ingress control | Egress | Detection | After hours |
|---|---|---|---|---|---|---|
| 0 Public | Street, sidewalk | — | none | — | — | — |
| 1 Site | Parking, walkways | Landscape, lighting | none | — | Cameras (lot, approaches) | Lighting on |
| 2 Reception | L1 lobby, restrooms | Building envelope | Unlocked 0700–1800, staffed | free | Cameras at entries + lobby, DPS on all exterior doors | Locked; badge only; intrusion armed on non-lobby areas |
| 3 Employee | Office floors, break, conf | Lobby speedgate/door + stair/elevator control | Badge | free (REX + free mech egress) | Reader logs, DPS, forced/held alarms; cameras at each floor lobby | Badge only, all events logged |
| 4 Sensitive | Data room, HR records, IDF closets | Slab-to-slab walls, rated door | Badge (+PIN for data room) | free | Camera at door, DPS, motion inside when unoccupied | Intrusion armed; any access alerts |

**Zone integrity findings you'd expect to have to fight for:**
- The IDF closets are usually drawn with partition walls to grid. Push for slab-to-slab or
  accept and compensate with interior detection. Write down which.
- The stairwell doors: if stair re-entry is required by code on certain floors `[CODE][VERIFY]`,
  your zone 3 boundary has a hole you must control with hardware and logic, not wishes.
- The loading/service entrance is almost always the weakest real boundary and almost always
  gets less attention than the front door in the client's mind. It should get *more*.
- The roof. Who can reach it? From where? What's on it, and does it penetrate zone 4?

---

## Common mistakes

⚠️ **Layers side by side rather than in series.** Three cameras on the same wall is not depth.

⚠️ **Layers that share a defeat.** One credential, one key, one server, one VLAN, one vendor
account — collapse multiple layers into one.

⚠️ **Zone boundaries that exist only on the floor plan.** Draw the boundary in section, not
just in plan. Ceilings and floors are boundaries too.

⚠️ **Over-hardening one boundary.** A vault door on a drywall room. Spend it on the weak path.

⚠️ **Ignoring the adjacency question.** What's on the other side of the secure room's wall?
If it's an unleased tenant space or a public corridor, that changes everything.

⚠️ **Redundancy that isn't.** Two fiber strands in one conduit. Two servers on one UPS. Two
identical devices with an identical vulnerability.

⚠️ **No documented degraded-mode behavior.** Discovered during commissioning, or worse, during
the first outage.

---

## Junior vs. Senior

**Junior:** can produce a zone diagram; knows to check ceilings; can list SPOFs from a
checklist; specifies controllers with local decision-making because the standard says to.

**Senior:** designs the zone structure to match how the organization *actually operates*
(including the fact that everyone props the side door for smoke breaks); knows which zone
boundaries the client will fail to enforce and designs accordingly; negotiates slab-to-slab
walls with the architect early, when it's free, rather than late, when it's a change order;
and can explain to a CFO why the second recording server is not optional in terms of
consequence rather than technology.

---

## Exercises

**E4.1** Draw the zone diagram for the building you work in. Include zone numbers, boundary
descriptions, and the control at each boundary. Then identify the *three* boundaries you
believe are least intact and explain why.

**E4.2** For a room you designate as Zone 4, complete the full zone-integrity checklist
(all 9 rows). Note every item you cannot answer from observation — those are survey questions.

**E4.3** A design has: 120 cameras, one recording server, one 48-port PoE switch per floor
(3 floors), one core switch, one access control server, 6 door controllers, one 24 VDC power
supply per floor for locks, one UPS in the MDF.
List every SPOF. For each, state what stops working and propose a proportionate mitigation.
Rank your mitigations by cost-effectiveness.

**E4.4** A client wants to spend $50k hardening the door to a records room that currently has
a hollow-core door in a stud wall with a suspended ceiling. Write the three-sentence response
you'd give.

> Solutions: [`_solutions/04_zones_solutions.md`](_solutions/04_zones_solutions.md)

---

## Retrieval check

1. What three properties must layers have to constitute defense in depth?
2. What is balanced protection, and what is the correct stopping rule when applying it?
3. Distinguish redundancy from diversity. Which is better against a thinking adversary, and why?
4. What is graceful degradation, and why must it be specified at design time?
5. List the nine elements of a zone-integrity check.
6. Name five common SPOFs in a security system.

---

## References

- Garcia, M.L., *The Design and Evaluation of Physical Protection Systems*, 2nd ed. `[PRACTICE]`
- ASIS International — *Protection of Assets*, Physical Security volume. `[GUIDELINE]`
- FEMA risk-management series for buildings (e.g., FEMA 426/452 lineage) — layered site
  security concepts. `[GUIDELINE]` `[VERIFY current publication numbers and editions]`
- Interagency Security Committee (ISC) — *The Risk Management Process for Federal Facilities*.
  `[STANDARD]` Federal-specific but the zone/level structure is instructive. `[VERIFY edition]`

**Next:** [05 — CPTED](05_cpted.md)
