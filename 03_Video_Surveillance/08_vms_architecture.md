# 08 — VMS Architecture

> The lesson that decides whether the system still works on a bad day.
>
> Everything so far produced a good image and stored it. This lesson is about the software and
> servers that sit between the camera and the operator, **where they fail, and what the system does
> when they do.** It is also where a software engineer's instincts are most useful and most
> dangerous — useful because this is a distributed system with a database and a client tier;
> dangerous because the failure modes that matter here are not the ones you are used to.
>
> Links **[6]**, **[7]**, and **[8]** of [the imaging chain](01_imaging_chain.md).

## Learning objectives

- Name the VMS components and what each one is responsible for.
- State, for each, what stops working when it fails — the question that defines the architecture.
- Size recorders on **throughput and licensing**, not on a camera-count rule of thumb.
- Account for live viewing and export as loads **additional** to recording.
- Choose between centralised and federated multi-site architectures on WAN reality.
- Produce an architecture deliverable that states its own failure behaviour.

---

## The components

```
        ┌──────────────┐
        │   CAMERAS    │  edge devices, own storage optional
        └──────┬───────┘
               │ camera VLAN
        ┌──────▼───────────────────────────────────────────┐
        │  RECORDING SERVER(S)                             │
        │  receives streams, writes to storage,            │
        │  serves live + playback to clients               │
        └──────┬────────────────────────┬──────────────────┘
               │                        │
        ┌──────▼──────┐          ┌──────▼──────────────────┐
        │  STORAGE    │          │  MANAGEMENT SERVER      │
        │  RAID array │          │  config, users, rules,  │
        └─────────────┘          │  licensing, directory   │
                                 └──────┬──────────────────┘
                                        │
                                 ┌──────▼──────┐
                                 │  DATABASE   │  config + event/metadata
                                 └─────────────┘
                                        │
        ┌───────────────────────────────▼──────────────────┐
        │  CLIENTS: workstations, video wall, mobile,      │
        │  web gateway, integrations (PACS, alarms)        │
        └──────────────────────────────────────────────────┘
```

| Component | Responsible for | Typically fails as |
|---|---|---|
| **Recording server** | Receiving streams, writing to disk, serving live and playback | Hardware failure, disk full, NIC saturation, service crash |
| **Storage** | Holding the recordings | Disk failure, array degradation, capacity exhaustion |
| **Management server** | Configuration, users, permissions, rules, licensing, directory of recorders | Service failure, licence expiry, certificate expiry |
| **Database** | Configuration and event/metadata index | Corruption, disk exhaustion, unmaintained growth |
| **Clients** | Display, search, export | Decode capacity, network, user error |
| **Gateway / mobile** | Remote and browser access | The security exposure of the whole system |

---

## The architectural question: what breaks when each piece fails?

**This is the question that separates an architecture from a bill of materials, and it is the one
to ask a VMS vendor in the first meeting.** The answers vary by product and by version, so they
must be verified rather than assumed. `[MFR][VERIFY]`

| If this fails... | Does recording continue? | Does live view work? | Does playback work? |
|---|---|---|---|
| **Management server** | Usually **yes** for a period — recorders keep recording on their last config | Often degraded; client login may fail | Often unavailable via the client |
| **Database** | Usually yes | Often | **Search and event lookup typically fail** |
| **One recording server** | **No — for its cameras** | No, for its cameras | No, for its cameras |
| **Storage array** | No | Live may still pass through | No |
| **Client workstation** | Yes | On that workstation, no | No, there |
| **Network core** | Depends where the break is | No | No |

> ⚠️ **The management-server dependency is the one that surprises people.** On many platforms,
> recorders continue recording without the management server — which sounds reassuring — but
> **operators cannot log in**, because authentication and permissions live there. So the system is
> faithfully recording video that nobody can watch. Whether that is acceptable depends entirely on
> whether the site has a live-monitoring function, which is a
> [lesson 01](01_imaging_chain.md) link-[8] question resurfacing as an architecture decision.

> 🧠 **For a software engineer:** the instinct to treat this like any distributed system is right,
> with one correction. In most systems, degraded availability means users are inconvenienced. Here,
> **a recorder that stops recording destroys information that never existed anywhere else and
> cannot be regenerated.** There is no replay, no retry, no eventual consistency. The write path is
> the only path, it is real-time, and a gap in it is permanent. Design accordingly: the recording
> tier gets the redundancy budget, and the management tier can usually tolerate a slower recovery.

---

## Sizing recorders

The common rule of thumb — "N cameras per recorder" — is wrong because it ignores what actually
binds. Size on four independent limits and take the smallest.

**1. Sustained write throughput.**

| Site | Cameras × bitrate | Aggregate | Sustained write |
|---|---|---|---|
| Meridian | 31 × 4.0 Mbps | 124.0 Mbps | **15.5 MB/s** |
| Mid-size | 200 × 5.0 Mbps | 1000.0 Mbps | **125.0 MB/s** |
| Campus | 600 × 5.0 Mbps | 3000.0 Mbps | **375.0 MB/s** |

For scale, a single 7.2k SATA disk sustains roughly 150–200 MB/s sequential, and a RAID 6 array of
six aggregates well beyond that. `[PRACTICE][VERIFY per product]` **Write throughput is rarely the
binding limit** on a modern server — which is precisely why sizing on it alone produces recorders
that fail for other reasons.

**2. Network interface.** A 1 GbE NIC on the recorder carries 1000 Mbps *total* — recording **plus**
every live and playback stream it serves. See the next section; this is very often the real limit.

**3. Licensing.** Most platforms license per camera or per channel, and many bind licences to a
recorder. `[MFR][VERIFY]` This frequently sets the practical camera-per-recorder number, and it is
a commercial constraint that behaves like a technical one.

**4. Failure domain.** The most important limit and the least technical: **how many cameras are you
willing to lose at once?** A single recorder holding 200 cameras is a single failure that removes
200 cameras. Two recorders holding 100 each halve that exposure for the cost of a second chassis.

> 🧠 **Size the failure domain first, then check the other three.** On most projects the honest
> constraint is "no more than X cameras may go dark together," and it produces a better answer than
> any throughput calculation. Ask the client what X is; they will never have been asked, and the
> conversation is worth more than the number.

## Live viewing is additional load — and it lands on the recorder

Recording bandwidth is not total bandwidth. **Every live stream a client watches is another copy
sent from the recorder** (or from the camera, depending on architecture), and it concentrates on
the recorder's network interface rather than spreading across the camera VLAN.

| Operators × streams | Additional load |
|---|---|
| 1 × 16 streams @ 4 Mbps | 64.0 Mbps |
| 4 × 16 | 256.0 Mbps |
| 8 × 25 | 800.0 Mbps |
| 16 × 16 | **1024.0 Mbps — exceeds 1 GbE on its own** |

Applied to Meridian's 121 Mbps of recording:

| Scenario | Total on the recorder NIC | % of 1 GbE |
|---|---|---|
| Recording only | 121.0 Mbps | 12.1% |
| + 2 operators × 16 | 249.0 Mbps | 24.9% |
| + 4 operators × 16 | 377.0 Mbps | 37.7% |
| + 8 operators × 16 | 633.0 Mbps | 63.3% |

**Substreams are the standard fix, and they are underused.** Cameras can publish a second,
low-resolution stream. Clients display the substream in multi-view tiles — where a 4 MP image is
being shown at postage-stamp size anyway — and switch to the main stream only when an operator
maximises a view or reviews recorded footage. Recording always uses the main stream.

| Scenario | Main-stream viewing | Substream viewing | Reduction |
|---|---|---|---|
| 4 operators × 16 | 377.0 Mbps | 153.0 Mbps | **59%** |
| 8 operators × 16 | 633.0 Mbps | 185.0 Mbps | **71%** |

⚠️ **Substreams also solve a client-side problem**: decoding sixteen 4 MP H.265 streams will defeat
a workstation without hardware acceleration long before the network notices. The tile is 320 px
wide; decoding 2688 px into it is waste at both ends.

## Centralised vs. federated multi-site

| Model | Recording happens | Good for | Breaks when |
|---|---|---|---|
| **Centralised** | All video crosses the WAN to one data centre | Small remote sites; consistent central control | **The WAN.** Video is continuous and unforgiving of bandwidth |
| **Distributed / local recording** | At each site, managed centrally | Almost every real multi-site estate | Central management link — but recording survives |
| **Federated** | Locally, with independent systems joined at the management layer | Large estates, mergers, differing ownership | Cross-site search and consistency are weaker |

⚠️ **Centralised recording across a WAN is the recurring multi-site mistake.** A 40-camera remote
site at 4 Mbps is 160 Mbps, sustained, permanently. That is not a spike — it is the steady state,
24 hours a day, and it will not fit alongside the site's ordinary business traffic on a typical
branch circuit.

**Record locally, manage centrally.** Then only the streams someone is actually watching cross the
WAN, which is intermittent and small, and a WAN outage degrades visibility rather than destroying
the recording. This is the right default and it should be the starting position in any multi-site
discussion.

**What federation genuinely buys:** one operator interface across sites with differing ownership,
differing VMS versions, or differing administrative control — common after mergers or in
landlord/tenant estates. **What it costs:** cross-site search is usually slower and less complete,
permissions become complicated, and version compatibility between federated systems is a
maintenance obligation forever. `[MFR][VERIFY]`

## Integration, and the interfaces that matter

- **Access control** — the highest-value integration. Correlating a badge event with video at that
  door turns two records into one investigation. Needs **time sync** ([lesson 07](07_storage_and_retention.md))
  and an agreed device-naming convention. Covered in
  [`../04_Access_Control/`](../04_Access_Control/) *(not yet written)*.
- **Alarms and intrusion** — an alarm that pulls up the relevant camera is the difference between
  a monitored system and an ignored one.
- **Analytics** — server-side, edge, or a third-party engine. See
  [lesson 11](11_analytics_and_health.md).
- **The device data model** — camera names, locations, and IDs must match the drawings, the
  schedules, and the access-control system. This is exactly the problem
  [`../16_Automation/data_model/`](../16_Automation/data_model/) exists to solve: one register,
  many projections. A VMS where camera 47 is called "CAM47" in the software, "C-2-14" on the
  drawing, and "North Dock" by the guards is a system nobody can operate under pressure.

**Cybersecurity is not optional here.** A VMS is a set of servers with cameras that are, in
practice, small unpatched Linux computers on your network. Camera VLAN separation, changed default
credentials, certificate management, patching, and restricted remote access are minimum
expectations. Treated in [`../09_Cybersecurity/`](../09_Cybersecurity/) *(not yet written)*; the
architecture must leave room for it.

## 🧮 Worked example 8.1 — Meridian's architecture, stated with its failure behaviour

Thirty-one cameras, 121 Mbps recording, 47 TB storage
([lesson 07](07_storage_and_retention.md)), a single building, no dedicated monitoring station —
footage is reviewed by the facilities manager and, occasionally, live-viewed by reception.

**The design:**

- **One recording server**, 31 cameras, RAID 6 with hot spare, dual NIC (camera VLAN + client VLAN).
- **Management server** virtualised on the client's existing VM infrastructure, with their standard
  backup applying to it.
- **Substreams enabled**, clients configured to use them in multi-view.
- **No failover recorder.**

**And the part that makes it an architecture — the stated failure behaviour:**

> **Failure behaviour.**
> **Recording server fails:** all 31 cameras stop recording until it is repaired or replaced.
> Recorded video already written remains on the array and is retrievable once the server is
> restored. Estimated outage 4–24 hours depending on spares. **This is the accepted single point of
> failure for this system.**
> **Storage array degrades (one disk):** recording continues; the hot spare rebuilds automatically;
> alerts are sent to [monitored address]. **Two disks:** recording continues, no further redundancy
> until rebuild completes.
> **Management server fails:** recording continues on the last known configuration. Operators
> cannot log in to the client until it is restored; it is covered by the client's existing VM
> backup, with an estimated 2-hour restore.
> **Network core fails:** cameras cannot reach the recorder; recording stops for the duration.
> Cameras with edge storage fitted [list] will backfill on restoration.
>
> **If a 4–24 hour total recording outage is not acceptable**, the options are a failover recorder
> (adds one server) or splitting the cameras across two recorders (adds one server, halves the
> exposure to ~15 cameras). Neither is included in the current scope.

**Why this paragraph is the deliverable.** It converts an architecture from a diagram of boxes into
a set of statements the client can evaluate and accept or reject. It surfaces the single point of
failure **before** it fails, prices the remedy, and puts the decision where it belongs. A client who
reads that and says "4 to 24 hours is fine" has made an informed decision. A client who was never
told has a grievance.

## Design tradeoffs

| Decision | Buys | Costs |
|---|---|---|
| More, smaller recorders | Smaller failure domain | More servers, more licences, more to maintain |
| Failover recorder | Survives recorder failure | A server; a test regime |
| Substreams | Large reduction in client-side network and CPU | Configuration; slight complexity |
| Centralised recording | Single location, simple control | **WAN bandwidth, permanently** |
| Local recording, central management | Survives WAN loss; sane bandwidth | Equipment at every site |
| Federation | One interface across independent systems | Weaker cross-site search; version-compatibility burden |
| Virtualised management server | Uses existing infrastructure and backup | Depends on that infrastructure's availability |
| Mobile / web gateway | Genuine operational value | **The main security exposure of the system** |

## Common mistakes

⚠️ **Sizing recorders by camera count.** Size by throughput, NIC, licensing, and failure domain —
and take the smallest.

⚠️ **Forgetting live view and export in the recorder's network budget.** They land on one NIC.

⚠️ **Not enabling substreams.** A large, free improvement, left on the table by default.

⚠️ **Centralising recording across a WAN.** Continuous load that does not fit.

⚠️ **Not asking what happens when the management server fails.** Frequently: recording continues
and nobody can log in.

⚠️ **One recorder for the whole site with no failover and no discussion.** The problem is not the
single point of failure; it is the *undisclosed* single point of failure.

⚠️ **Inconsistent naming across VMS, drawings, and access control.** Guarantees confusion during
the one incident that matters.

⚠️ **Treating cameras as appliances rather than as networked computers.** They are the softest
targets on the network.

## Junior vs. Senior

| | Junior | Senior |
|---|---|---|
| Sizes recorders by | Cameras per box | Throughput, NIC, licensing, and failure domain |
| Asks the vendor | What it costs | **What still works when each component fails** |
| Plans multi-site by | Centralising to one data centre | Recording locally, managing centrally |
| Treats live viewing as | Free | An additional load on the recorder's NIC, mitigated with substreams |
| Delivers an architecture as | A diagram | A diagram **plus stated failure behaviour and outage estimates** |
| Handles a single point of failure by | Not mentioning it | Naming it, pricing the remedy, and getting an explicit decision |
| Names devices | However the installer did | Consistently across VMS, drawings, schedules, and PACS |

## 🔧 Field exercise

1. On a live system, draw the actual architecture — recorders, management server, database,
   storage, clients. Most sites do not have this drawing.
2. For each component, ask the administrator what happens when it fails. Compare their answers to
   the vendor documentation.
3. Find out whether substreams are enabled, and what a client actually pulls in a 16-tile view.
4. Compare a camera's name in the VMS, on the drawing, and as the guards refer to it.
5. Ask when the system was last patched, and whether the cameras are on a separate VLAN.

## Exercises

Work these before opening
[`_solutions/08_vms_architecture_solutions.md`](_solutions/08_vms_architecture_solutions.md).

**E8.1** A 200-camera site at 5 Mbps average is proposed on a single recording server with a 1 GbE
NIC. The site has 6 operator workstations, each displaying 16 streams.
 (a) Compute the recording load and the live-view load.
 (b) Does it fit? Show the arithmetic.
 (c) Give two distinct fixes and state what each costs.

**E8.2** A retail chain with 30 stores, 24 cameras each at 3 Mbps, proposes centralised recording
to head office.
 (a) Compute the per-store and total WAN load.
 (b) State why this fails, beyond the raw number.
 (c) Give the recommended architecture and what is lost by adopting it.

**E8.3** For a VMS you are evaluating, write the five questions you would ask the vendor about
failure behaviour. For each, state what answer would concern you.

**E8.4** A client has one recorder holding all 140 cameras, no failover, and asks whether they need
redundancy.
 (a) What do you need to know before answering?
 (b) Present the options with what each changes.
 (c) Write the two-sentence framing that puts the decision to them properly.

**E8.5** 🧠 A VMS vendor states their platform is "fully redundant." Write the six questions that
establish what that actually means, and for each explain what a weak answer reveals.

## Retrieval check

1. Name the VMS components and one failure mode each.
2. On many platforms, what happens to recording when the management server fails — and to operator
   login?
3. What are the four limits that size a recorder, and which is usually the real one?
4. Where does live-view load land, and what mitigates it?
5. Why is centralised recording across a WAN usually wrong?
6. What does federation buy, and what does it cost?
7. What makes an architecture deliverable more than a diagram?

## References

- [`../28_Calculators/psec/video.py`](../28_Calculators/psec/video.py) — aggregate bandwidth used
  in the sizing figures here.
- [`../16_Automation/data_model/`](../16_Automation/data_model/) — the single device register that
  makes naming consistent across VMS, drawings, schedules, and access control.
- [`../08_Networking/`](../08_Networking/) — VLANs, uplinks, multicast, QoS *(not yet written)*.
- [`../09_Cybersecurity/`](../09_Cybersecurity/) — camera and VMS hardening, remote access
  exposure, patching *(not yet written)*.
- `[MFR][VERIFY]` **Every failure-behaviour claim in this lesson varies by product and version.**
  The table above describes common patterns, not guarantees. Get the answers for the actual product
  and version, in writing, and test the important ones at commissioning.
- `[PRACTICE]` Disk throughput figures, streams-per-workstation limits, and the substream guidance
  are engineering practice and depend heavily on hardware.

---

**Next:** [09 — Camera Placement Engineering](09_camera_placement.md) — the floor plan, and the
rule that every camera must answer a written question.
