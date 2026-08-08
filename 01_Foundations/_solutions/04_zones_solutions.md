# Solutions — 04, Defense in Depth and Security Zones

> For the exercises in
> [`../04_defense_in_depth_and_zones.md`](../04_defense_in_depth_and_zones.md).
> **Write your answers first.**

E4.1 and E4.2 are done against *your* building, so what follows is a worked reference against a
fictional one plus the marking criteria. E4.3 and E4.4 have determinate answers.

> The building used in E4.1 and E4.2 is **synthetic**. It is a composite written to exercise the
> checklist, not a description of a real facility.

---

## E4.1 — Zone diagram and the three weakest boundaries

### Worked reference: "Kestrel Building" — 4-storey office with a 2nd-floor R&D suite

```
   ZONE 0  Public street, sidewalk, unrestricted parking apron
     │  boundary: property line.  control: signage, landscaping, grade change
     ▼
   ZONE 1  Site — gated staff lot, loading apron, building envelope approach
     │  boundary: fence + vehicle gate + building exterior wall
     │  control: credentialed vehicle gate; exterior doors locked, badge on 2
     ▼
   ZONE 2  Public interior — lobby, reception, ground-floor conference, restrooms
     │  boundary: lobby speedlanes + elevator dispatch + stair doors
     │  control: credential required; reception staffed 0700–1800
     ▼
   ZONE 3  Employee interior — open office floors 1, 3, 4; break rooms; copy areas
     │  boundary: R&D suite entry door, MDF door, records room door
     │  control: credential + access group
     ▼
   ZONE 4  Restricted — 2nd-floor R&D suite, MDF, records room
            boundary: suite envelope.  control: credential + PIN, DPS, video
```

**The three weakest boundaries, and why.** The point of the exercise is that the weakest
boundaries are almost never the ones with the most hardware on them.

**1. Zone 3 → Zone 4 at the MDF, via the ceiling.** The MDF has a card reader, a rated door,
and partition walls terminating at the suspended ceiling grid, with a continuous plenum to the
corridor. Every control is on the door and **the boundary does not exist above 9 feet**. This
is the canonical failure and it is invisible on a floor plan, on a device schedule, and in a
photograph of the door.

**2. Zone 2 → Zone 3 at the stairs, after 1800.** The speedlanes control the elevator lobby.
The stair doors are free-egress in the exit direction and locked on the floor side — but the
**ground-floor stair door opens into Zone 2**, so anyone in the public lobby can enter the
stair and try every floor door. The doors hold; the *attempts* are undetected because there is
no position monitoring on stairs. And the boundary is only as good as reception, which goes
home at 1800 while the lobby stays open until 2100 for the conference rooms.

> This is the lesson's egress-hardware row doing its work: *does the required egress path from
> within create an entry path from without?* Here, yes — and the fix is a floor re-entry
> strategy and stair door monitoring, not a stronger lock (module `35_Doors_and_Hardware/05`).

**3. Zone 0 → Zone 1 at the loading apron.** The vehicle gate is credentialed and the pedestrian
route beside it is a 3-foot gap between the gate post and the landscape wall, left for
maintenance access. It is a **designed hole in the boundary** that appears on no drawing as a
boundary crossing. Nothing detects it. It exists because a real constraint was solved locally
and nobody re-ran the zone diagram afterwards.

### Marking criteria for your own answer

| Criterion | What good looks like |
|---|---|
| Zones are **spaces**, not devices | If your diagram is a device layout, redo it. Zones are volumes with boundaries. |
| Every boundary names its **control** | A boundary with no stated control is either not a boundary or an undocumented gap. |
| Boundaries are **enclosing surfaces**, not doors | If every boundary in your diagram is a door, you have not applied the lesson. |
| The three weakest are justified **by mechanism** | "The back door is weak" is not a finding. "The back door's frame is KD in a stud wall with the strike into 20-gauge" is. |
| At least one weakness is **not a hardware weakness** | Staffing hours, procedure, adjacency, and time-of-day are boundary properties too. |

Most first attempts pick three doors. **If all three of your weakest boundaries are doors, you
have almost certainly missed the real one**, because the wall, the ceiling, the schedule, and
the maintenance gap are where boundaries actually fail.

---

## E4.2 — Full zone-integrity checklist for a Zone 4 room

Worked against the **Kestrel Building MDF**, a 14 × 18 ft room on floor 3.

| Element | Finding | Confidence |
|---|---|---|
| **Walls** | Metal stud with single-layer gypsum each side, terminating at ceiling grid. Cuttable with a utility knife in well under a minute. | **Observed** |
| **Ceiling** | Suspended grid; plenum appears continuous to the corridor and to the adjacent break room. | **Observed from the corridor side; not verified above the MDF tile** |
| **Floor** | Slab on the floor below. No raised floor. **Space below is a Zone 3 open office** — a ceiling penetration from below is not addressed by anything. | Observed |
| **Doors** | Single leaf, hollow metal in a welded frame, card reader, electric strike, closer. **Gap at the strike edge measured by eye at roughly ¼ in.** Undercut ~¾ in. | Observed |
| **Windows** | None. | Observed |
| **Penetrations** | Two 4-in conduit sleeves (fire-stopped, adequate), one cable tray entering through a wall opening roughly 12 × 18 in that is **not** sealed, and a return air path above the ceiling. | Observed |
| **Roof** | N/A — interior room on an intermediate floor. | N/A |
| **Adjacencies** | North: Zone 3 corridor. East: break room (**Zone 3, unstaffed, unobserved, and the most likely attack position**). South: exterior wall. West: janitor closet — **who has keys to the janitor closet?** | Partially observed |
| **Egress hardware** | Lever trim, no panic device required at this occupancy `[CODE][VERIFY occupant load and adopted code]`. Door is not part of any egress path *from* other spaces. No entry path created. | Observed; code determination **not** made |

### The items I could not answer from observation — these are the survey questions

This list is the actual deliverable. **Every "unknown" is a question for the site survey, and
writing `UNKNOWN — [why]` is data; a blank is indistinguishable from an oversight.**

1. Does the partition actually stop at the grid, or is there a fire-rated extension above the
   tile? *Requires lifting a ceiling tile with permission.*
2. Is the plenum continuous to the break room, or is there a full-height wall on that side?
   *Same access required — and it is the single highest-value unknown on this list.*
3. What is above the cable tray opening, and can a person pass through it? `[VERIFY]` The
   lesson's >96 in² person-passable threshold is a starting point, not a determination — 12 × 18
   is 216 in², so this needs a real look.
4. What is the actual door gap at the strike, measured rather than eyeballed? Governs whether
   the latch is attackable.
5. Is the electric strike fail-secure, and has anyone verified it rather than assuming?
6. Who holds keys to the janitor closet, and does that closet share the plenum?
7. Is there any detection *inside* the room, or is every control on the door? (Observed answer:
   every control is on the door.)
8. What is the adopted code edition, and what does it require for this occupancy? `[CODE][VERIFY]`

**The finding that comes out of this table:** the MDF has three independent bypasses — the
ceiling plenum, the unsealed cable tray opening, and the floor slab from a Zone 3 space below —
and all of the money is on the door. Extending the partition slab to slab and sealing the tray
opening costs a small fraction of the access control already installed and is the only work that
makes any of it matter.

---

## E4.3 — Single points of failure

### The design

120 cameras · 1 recording server · 1 × 48-port PoE switch per floor (3 floors) · 1 core switch ·
1 access control server · 6 door controllers · 1 × 24 VDC supply per floor for locks · 1 UPS in
the MDF.

### Every SPOF

| # | SPOF | What stops working | Detection |
|---|---|---|---|
| 1 | **Recording server** | **All 120 cameras stop recording.** Live view may survive if direct-to-camera; recorded evidence does not. | Should be alarmed. Frequently is not. |
| 2 | **Core switch** | Everything on the network: all video, all access control head-end communication, all monitoring. **The single largest SPOF in the design.** | Immediate and obvious |
| 3 | **UPS in the MDF** | On failure or depletion: core switch, recording server, access control server, and anything else in that room. **It is a SPOF that guarantees several other SPOFs fail simultaneously.** | Only if UPS supervision is configured *and monitored* |
| 4 | **Access control server** | Real-time monitoring, credential changes, new events at the head-end. Controllers should keep making local decisions — **verify that, do not assume it.** | Comm-loss alarm |
| 5 | **Floor PoE switch** (×3) | 40 cameras per floor go dark. Not site-wide, but a whole floor of a whole zone. | Immediate |
| 6 | **24 VDC lock supply** (×3) | Every electrified lock on that floor reverts to its fail state simultaneously. **If any of them are fail-safe, a floor unlocks itself.** | Only with power-fail supervision |
| 7 | **Door controller** (×6) | All doors on that controller. Whether this matters depends entirely on **which doors share a controller** — see below. | Comm loss |
| 8 | **The MDF room itself** | Fire, water, or a locked door with a lost key takes out items 1–4 at once. A room is a SPOF and it never appears on a riser diagram. | None |
| 9 | **One utility feed / one generator path** | Everything, after the UPS depletes. | Power-fail alarm, if configured |
| 10 | **One WAN / monitoring path** | Offsite monitoring and remote response. Local recording may continue with nobody watching. | Should be supervised; often is not |
| 11 | **One VMS software instance and one database** | Corruption or license expiry takes down all recording with no hardware failure at all (lesson 07, category 4). | Variable, often slow |
| 12 | **One administrator / one set of credentials** | Nobody can change anything. The bus-factor SPOF. **Never on a riser diagram, routinely the real one.** | None until needed |

### Mitigations, ranked by cost-effectiveness

**Tier 1 — configuration and design decisions. Near-zero cost, done at design time.**

1. **Distribute door controller assignments so that no two doors on the same adversary path
   share a controller.** Costs nothing at design time and is unfixable later without rewiring.
   This is the lesson-07 FMEA row that is invisible on a device schedule.
2. **Verify offline controller behaviour and buffer depth in commissioning**, rather than
   trusting the datasheet. Costs an hour. Converts assumption 4 into a fact.
3. **Configure and *test* supervision on the UPS, the lock supplies, and the WAN path.** Most of
   these have supervision available and unconfigured. A SPOF you detect in seconds is a
   different risk from one you detect in months.
4. **Document the fail state of every door and check that a floor supply failure does not unlock
   a boundary.** Free, and it is the difference between graceful degradation and a building
   that opens itself.
5. **Second administrator, documented credentials in escrow.** Free. Closes #12.

**Tier 2 — modest capital, high value.**

6. **Camera-edge recording (SD card) as failover for the highest-value cameras.** This is
   *diversity*, not redundancy: it fails for different reasons than the server does, so it
   survives a server crash, a database corruption, and a core switch outage. A second identical
   server would not survive the switch outage.
7. **Dual uplinks from each floor switch to the core**, and ideally to two core switches. Halves
   the blast radius of #2 and #5.
8. **A second recording server covering the highest-value cameras**, sized so no single server
   failure loses more than a defined number of cameras. Note this is the exact form of the
   lesson-06 example requirement — "failure of any single recording server results in loss of
   recording for no more than 16 cameras."

**Tier 3 — significant capital, justified only by the risk assessment.**

9. Redundant core switching with a resilient topology.
10. A second head-end location in a different fire compartment. Closes #8, which nothing else
    does.
11. Generator with automatic transfer, if the required availability warrants it.

**The ranking argument to make in a report:** items 1–5 cost essentially nothing and remove or
expose five of the twelve SPOFs. **They are all decisions, not purchases**, and every one of
them gets harder and more expensive after the design is issued. Spend the design effort there
before spending the owner's money on tier 3.

> **Diversity beats redundancy against a thinking adversary and against common-cause failure
> alike.** Two identical servers in the same rack on the same UPS fail together for most of the
> reasons they will actually fail. Edge recording plus a server is worth more than two servers.

---

## E4.4 — The $50k records room door

> **Three sentences:**
>
> "Before we spend anything on the door, I need to point out that the wall it sits in is a stud
> partition that stops at the ceiling grid, so anyone can be in that room in about forty seconds
> without touching the door at all. For roughly a tenth of that budget we can extend the wall
> slab to slab, seal the ceiling path, and put a monitored contact and a camera on the room —
> which would actually change how hard it is to get in and would tell you when someone did.
> If you'd still like to upgrade the door after that, we should, but it should be the last thing
> we do rather than the first."

**What that answer is doing:**

- **It leads with the mechanism and the number.** "Forty seconds" is the whole argument, and it
  is checkable. Without it, this is just an engineer disagreeing with a client.
- **It does not say no.** The lesson's balanced-protection point is not "don't buy the door" —
  it is "the stopping rule is when the weakest path is no longer the one you're spending on."
  The door upgrade becomes correct *after* the wall is fixed.
- **It recommends spending roughly a tenth of the budget** — against the interest of anyone
  paid by the value of the installed work. Lesson 01 argued you must sometimes do this; this is
  what it looks like in three sentences.
- **It adds detection**, because a hardened room with no monitoring is still a room where you
  find out later.
- **It ends with "yes, and here's the order."** A client who is told their idea is wrong
  defends it. A client who is told their idea is *premature* reorders it.

**The failure mode to avoid:** answering "a $50k door is a waste of money on that wall." True,
faster, and it loses the room. The finding is identical; the sentence that gets it funded is
not.

---

## The thread through all four

E4.1 and E4.2 find boundaries that are not continuous. E4.3 finds dependencies that are not
visible. E4.4 is the conversation where you spend a client's money in the right order.

All three failure classes share a property: **none of them appears on a device schedule.** A
schedule tells you what is installed. It cannot tell you that a wall stops at the grid, that two
doors on the same path share a controller, or that the strongest component is protecting the
weakest path. That is why the checklist, the SPOF enumeration, and the balanced-protection
stopping rule are separate deliberate activities rather than things you notice while drawing.

> Next: [`05_cpted.md`](../05_cpted.md) — where the cheapest boundary control turns out to be
> the position of a reception desk.
