# 07 — Storage, Retention, and Redundancy

> **Prerequisite:** [`../32_Engineering_Math/04_storage.md`](../32_Engineering_Math/04_storage.md).
> That lesson derives the storage arithmetic, the decimal/binary distinction, the inverse problem,
> and how to present a range. **This lesson does not re-derive it.**
>
> Here we cover what the arithmetic sits inside: **who chooses the retention period, what RAID
> actually protects you against, what it does not, and what makes a recording usable as evidence.**
>
> Link **[7]** of [the imaging chain](01_imaging_chain.md), and the link where the most
> consequential number in the whole design is set by someone who is usually not an engineer.

## Learning objectives

- Interrogate a retention requirement rather than accepting it as an input.
- Convert a usable-capacity requirement into disks, through RAID and format overhead.
- State what each RAID level protects against, and why rebuild time is the real risk.
- Solve the inverse problem and deliver its answer to an owner who believes otherwise.
- Distinguish redundancy from backup, and both from archive.
- Specify the things that make video usable as evidence — time sync, export, integrity.

---

## Retention is not an engineering input

**It arrives as a number on an RFP and it is treated as a given. It should not be.**

Retention is a legal, regulatory, insurance, and operational decision with an engineering
consequence. The engineer's job is not to choose it — it is to **make sure someone chose it, on a
basis, and to record who and on what basis.**

The questions to ask, in order:

| Question | Why it matters |
|---|---|
| Who set this number? | If nobody can say, it was copied from a previous project |
| Against what obligation? | Regulation, insurance policy, licence condition, corporate policy, or habit |
| How long does this type of incident typically take to surface here? | The one question that actually predicts whether retention is adequate |
| Does any zone have a *different* obligation? | Retention often varies by area, and a single figure over-serves most of the site |
| What happens at day N+1? | Confirms everyone understands the data is gone, irreversibly |

⚠️ **The failure this prevents.** Internal theft, harassment complaints, discrimination claims, and
insurance disputes routinely surface **months** after the event, not days. A 30-day retention chosen
by habit will have destroyed the footage before anyone knew to ask for it, and the first time this
is discovered is during a dispute — where the absence of footage is sometimes worse than
unfavourable footage, because it invites an adverse inference. `[VERIFY — a legal question,
jurisdiction-dependent.]`

> 🧠 **Ask the "how long to surface" question of the people who handle incidents, not the people
> who commission buildings.** HR, the loss-prevention manager, and the duty security supervisor
> know the honest answer. Facilities and IT usually do not, and they are who you will be sitting
> with. Ten minutes with the right person can change the retention requirement by a factor of
> three, and it is far cheaper to discover before the storage is bought.

**Retention can and often should vary by zone.** A cash office, a controlled-substance store, or a
staff-only corridor may need 90 or 180 days while a general car park needs 14. A single site-wide
figure is either over-serving most of the site or under-serving the part that mattered. Varying it
is nearly free to design and is one of the clearest signals that a designer thought about the
problem.

---

## From a storage requirement to actual disks

The number from [lesson 06](06_compression_and_bandwidth.md) — **39.20 TB** for Meridian's 30 days,
**47.04 TB** with 20% headroom — is a **usable capacity** requirement. Between it and a purchase
order sit two layers of overhead.

### RAID overhead

| Level | Protects against | Usable fraction | Note |
|---|---|---|---|
| **RAID 5** | **One** disk failure | (n−1)/n | **Do not use on large disks** — see rebuild, below |
| **RAID 6** | **Two** simultaneous disk failures | (n−2)/n | The sensible default for video at scale |
| **RAID 10** | One per mirrored pair (sometimes more) | 1/2 | Fast rebuild, fast writes, expensive in capacity |

To deliver **47.04 TB usable**, allowing a further ~5% for filesystem and format overhead
`[PRACTICE]`:

| Disk size | RAID 6 configuration | Raw | Usable | After ~5% format |
|---|---|---|---|---|
| 8 TB | 7 data + 2 parity = **9 disks** | 72.0 TB | 56.0 TB | **53.2 TB** ✅ |
| 12 TB | 5 data + 2 parity = **7 disks** | 84.0 TB | 60.0 TB | **57.0 TB** ✅ |
| 16 TB | 4 data + 2 parity = **6 disks** | 96.0 TB | 64.0 TB | **60.8 TB** ✅ |
| 20 TB | 3 data + 2 parity = **5 disks** | 100.0 TB | 60.0 TB | **57.0 TB** ✅ |

⚠️ **Note what happens if you skip the format overhead.** An 8-disk RAID 6 of 8 TB disks gives
48.0 TB usable, which comfortably exceeds the 47.04 TB requirement — until ~5% format overhead
brings it to **45.6 TB, which does not.** A 3% margin evaporates into a shortfall. This is the same
class of error as [lesson 04](04_dori_and_pixel_density.md)'s E4.3: a requirement met by a hair is
a requirement not met.

### 🧮 Worked example 7.1 — the inverse problem

**The question you are actually asked on retrofits:** *"We already have a 48 TB array. How long
does that give us?"*

Using [`../28_Calculators/psec/video.py`](../28_Calculators/psec/video.py)'s
`retention_days_achievable` against Meridian's 31 cameras at nominal bitrates:

| Available | Retention achieved | With 20% reserved as headroom |
|---|---|---|
| 30.00 TB | 22.96 days | 19.13 days |
| 45.60 TB | 34.89 days | 29.08 days |
| **48.00 TB** | **36.73 days** | **30.61 days** |
| 58.32 TB | 44.63 days | 37.19 days |
| 92.00 TB | 70.40 days | 58.67 days |

So 48 TB buys **36.7 days raw**, or **30.6 days** once 20% is reserved — which just meets a 30-day
requirement, with almost nothing spare.

⚠️ **And note the units trap.** If that "48 TB" array is actually 48 **TiB** as reported by the
operating system, the same figures become 40.39 and 33.66 days. If it is 48 TB of disks *reported*
as 43.7 TiB, you have less than you think. The decimal/binary gap is about **10%** at TB scale and
is derived in [32/04](../32_Engineering_Math/04_storage.md) — the same distinction that produced a
real defect in `psec` (see that module's overview). **Always ask whether a stated capacity is the
manufacturer's decimal figure or the OS's binary one.**

> 🧠 **How to deliver the answer.** Clients asking this question have usually already decided the
> answer is "plenty." Do not lead with the shortfall. Lead with the **method**: "your cameras
> produce about 1.31 TB per day at current settings, so your 48 TB gives you about 37 days before
> reserving anything for headroom, and about 31 with a sensible reserve. Here is what would change
> that number." The arithmetic is inarguable and the conversation stays technical instead of
> becoming a negotiation about whether you are right.

---

## What RAID actually protects against — and the rebuild problem

**RAID protects against disk failure. That is all it protects against.**

It does not protect against: fire, flood, theft of the recorder, ransomware, accidental deletion,
a failed controller writing corruption across the array, or someone deleting the footage
deliberately. `[PRACTICE]`

**The rebuild is the dangerous window.** When a disk fails and is replaced, the array reconstructs
its contents by reading every remaining disk in full — the heaviest sustained load the array will
ever experience, applied to disks of the same age and batch as the one that just died, while it is
still recording 31 cameras.

Rebuild time scales with disk size:

| Disk | at 50 MB/s | at 100 MB/s | at 200 MB/s |
|---|---|---|---|
| 8 TB | 44.4 h (1.85 days) | 22.2 h | 11.1 h |
| 16 TB | 88.9 h (3.70 days) | 44.4 h (1.85 days) | 22.2 h |
| 20 TB | **111.1 h (4.63 days)** | 55.6 h (2.31 days) | 27.8 h |

Effective rebuild rates on a busy video array are at the low end of that range, because the array
is also servicing recording. `[PRACTICE][VERIFY per array]`

⚠️ **This is why RAID 5 is inadvisable on large modern disks.** During a rebuild, RAID 5 has **no
remaining redundancy** — a second failure, or a single unrecoverable read error anywhere across
several tens of terabytes of reads, loses the array. And the rebuild window is now measured in
**days**, on stressed, same-age disks. RAID 6 survives a second failure during rebuild, which is
precisely the scenario that has become likely rather than exotic.

**Specify, and check, these:**

- **RAID 6 or better** for any array of large disks.
- **A hot spare**, so the rebuild starts immediately rather than when someone notices and drives
  to site. On a 4-day rebuild, response time is a meaningful fraction of total exposure.
- **Monitoring that reaches a human.** An array in a degraded state that nobody was told about is
  the normal way arrays are lost. See [lesson 11](11_analytics_and_health.md).
- **Disks from mixed batches** where procurement allows, so correlated failures are less likely.

## Redundancy, backup, and archive are three different things

They get used interchangeably, and the confusion causes real losses.

| | Protects against | Does **not** protect against |
|---|---|---|
| **Redundancy** (RAID, failover recorder) | Component failure | Fire, theft, deletion, corruption propagated by the system itself |
| **Backup** (separate copy, ideally off-site) | Loss of the primary — including fire and ransomware | Nothing, if never tested |
| **Archive** (long-term retention of selected material) | Retention expiry destroying what mattered | Everything not selected |

**Most video systems have redundancy and no backup**, which is usually a defensible economic
decision — backing up a 47 TB rolling array is expensive and the data's value decays quickly. But
it should be a **decision**, stated, not an assumption:

> This system uses RAID 6 with a hot spare, which protects against disk failure. It is not backed
> up. A fire, flood, theft of the recorder, or a ransomware event affecting the recording server
> would result in total loss of recorded video. If particular footage needs to survive such an
> event, it must be **exported** to separate media promptly after the incident.

**Archive is where the real requirement usually lives.** What clients actually need is not a backup
of everything — it is that **footage relating to a known incident is preserved beyond the retention
period**. That is a workflow (someone exports and files it) more than a technology, and it is the
thing that most often fails: the incident is recorded, nobody exports it, and the retention clock
deletes it on schedule. **Specify the export workflow and name who owns it.**

## Edge and failover recording

- **Edge recording** — an SD card in the camera, recording locally, either continuously or when the
  network drops. Genuinely useful as a **gap filler** during network outages, with automatic
  backfill to the recorder on reconnection. `[MFR][VERIFY]` Not a primary storage strategy: cards
  have limited endurance, fail silently, and hold little.
- **Failover recorders** — a standby server that assumes recording if a primary fails. Real
  protection against recorder failure, at the cost of another server. The important question is the
  **failover time** and whether video is lost during the switch.
- **N+1 across a recorder pool** — one spare covering several primaries. Better economics at scale.

⚠️ **Failover that has never been tested is a diagram.** Test it at commissioning by pulling the
power on a primary and confirming the standby takes over, that the gap is what the vendor claims,
and — the part people skip — that footage from **before** the failover is still retrievable
afterwards. Then test it again annually. An untested failover has an unknown probability of working
and the client believes it is one.

## Evidence integrity: the part engineers forget

Storage that holds the footage is necessary. It is not sufficient for the footage to be *useful*.

**Time synchronisation.** Every recorder and camera must run NTP against a common source.
`[PRACTICE]` Without it clocks drift, and a video timestamp that cannot be reconciled with an
access-control record or a till transaction loses much of its value. Drifting clocks are also
attacked in cross-examination, and the argument is easy to make and hard to answer.

**Export.** The workflow matters more than its existence:

- Can an operator export a clip **without** re-encoding it?
- Does the export carry the **native timestamp and camera identity**?
- Is there a player, or is it a proprietary format the recipient cannot open?
- Is there a **hash or digital signature** proving the export was not altered? `[MFR][VERIFY]`
- How long does exporting an hour from six cameras take? If it is hours of an operator's time, it
  will be done badly under pressure.

⚠️ **The phone-video-of-a-monitor failure.** If the export workflow is awkward, the clip handed to
police will eventually be a phone recording of a screen. This is common, it destroys evidentiary
weight, and it is a **design** failure — the workflow was never specified or tested.

**Chain of custody** is procedural, not technical, but the system must support it: who exported
what, when, and can that be shown from the system's own audit log. Specify that the VMS logs
exports and that the log is retained. `[VERIFY]` The legal requirements are a legal question.

**Privacy and access control on the footage itself.** Who can view, export, and delete is a design
decision with legal weight — treated in
[`../36_Human_Factors_Privacy_Ethics/`](../36_Human_Factors_Privacy_Ethics/) *(not yet written)*
and [`../09_Cybersecurity/`](../09_Cybersecurity/) *(not yet written)*.

## Design tradeoffs

| Decision | Buys | Costs |
|---|---|---|
| Longer retention | Late-surfacing incidents recoverable | Storage, linearly |
| Per-zone retention | Right coverage where it matters | A little design effort; slightly more complex config |
| RAID 6 over RAID 5 | Survives a second failure during a multi-day rebuild | One disk of capacity |
| RAID 10 over RAID 6 | Fast rebuild, fast writes | **Half** of raw capacity |
| Hot spare | Rebuild starts immediately | One disk |
| Smaller disks | Much shorter rebuild windows | More disks, more slots, more power |
| Failover recorder | Survives recorder failure | A server, and a test regime |
| Edge recording | Covers network outages | Card endurance; silent failure; small capacity |
| Backup / off-site copy | Survives fire, theft, ransomware | Substantial cost |
| Archive workflow | Incident footage outlives retention | Process discipline — the hard part |

## Common mistakes

⚠️ **Accepting the retention number without asking who set it and why.**

⚠️ **Sizing on usable capacity and buying raw capacity.** RAID and format overhead sit between.

⚠️ **Forgetting format overhead**, turning a 2% margin into a shortfall.

⚠️ **Confusing TB and TiB.** ~10% at this scale; see [32/04](../32_Engineering_Math/04_storage.md).

⚠️ **RAID 5 on large disks.** Multi-day rebuild with no remaining redundancy.

⚠️ **Believing RAID is a backup.** It protects against exactly one failure mode.

⚠️ **Never testing failover.** Untested redundancy is a diagram.

⚠️ **No NTP.** Timestamps that cannot be reconciled, and cannot be defended.

⚠️ **No export workflow.** Ends in a phone video of a monitor.

⚠️ **Assuming the client will archive incident footage.** They will not, unless someone owns it.

## Junior vs. Senior

| | Junior | Senior |
|---|---|---|
| Treats retention as | An input | A decision to interrogate, attribute, and record |
| Asks about incident timing | Not at all | "How long do these typically take to surface?" — of HR and loss prevention |
| Sizes storage as | One figure, site-wide | Per zone, with different retentions where obligations differ |
| Converts to disks by | Dividing by disk size | Through RAID level **and** format overhead, then checking the margin |
| Specifies RAID by | The default in the quote | RAID 6 plus hot spare, justified by rebuild time on that disk size |
| Treats RAID as | Data protection | Protection against **disk failure only**, stated explicitly to the client |
| Handles failover by | Specifying it | Specifying it, testing it at commissioning, and re-testing annually |
| Thinks about export | If asked | As a designed workflow, timed and tested, with hashing and native timestamps |

## 🔧 Field exercise

1. On a live system, find the configured retention and the **actually achieved** retention. Look
   at the oldest recording available per camera. They frequently differ.
2. Ask three people at the site what the retention is. Compare their answers to each other and to
   reality.
3. Find out the RAID level, disk size, and whether a hot spare is fitted. Compute the rebuild time
   at 50 MB/s.
4. Ask when failover was last tested, and whether anyone has ever restored from the archive.
5. Export a 60-second clip and time yourself. Open it on a machine without the VMS installed.

## Exercises

Work these before opening
[`_solutions/07_storage_and_retention_solutions.md`](_solutions/07_storage_and_retention_solutions.md).

**E7.1** A client specifies 30 days for a 31-camera system consuming 1.31 TB/day.
 (a) How much usable storage is needed, with 20% headroom?
 (b) Configure it in RAID 6 with 16 TB disks, allowing 5% format overhead. How many disks?
 (c) How many for RAID 10 with the same disks? State the capacity penalty.
 (d) The client asks why not RAID 5 and one fewer disk. Answer with a number.

**E7.2** A retrofit client has a 60 TB array (manufacturer's figure) and 44 cameras averaging
4.2 Mbps, recording continuously.
 (a) Compute achievable retention, showing the daily consumption.
 (b) The client believes they have "about 60 days." Write the correction.
 (c) They ask for 90 days. Give two options with the storage each requires.

**E7.3** A design review finds: RAID 5, 20 TB disks, 8-disk array, no hot spare, monitoring by
email to an address belonging to a technician who left the company.
 (a) List the findings in order of severity.
 (b) For each, state the failure it enables.
 (c) Write the top recommendation as one sentence for an executive summary.

**E7.4** An incident occurs on day 3. It is reported on day 41. Retention is 30 days.
 (a) State what exists and what does not.
 (b) Name the process failure, which is not a storage failure.
 (c) Write the recommendation that prevents recurrence, naming who owns it.

**E7.5** 🧠 A client asks you to reduce storage cost. The system is 120 cameras, 30 days,
continuous, RAID 6, sized correctly. Give five distinct options, ordered by how much you would
recommend them, each with what it costs in capability. At least one must be an option that does
**not** reduce image quality or retention.

## Retrieval check

1. Who should choose the retention period, and what is the engineer's job?
2. What is the single best question for predicting whether retention is adequate?
3. What does RAID protect against, and name three things it does not.
4. Why is RAID 5 inadvisable on 16–20 TB disks?
5. What two overheads sit between usable capacity and disks purchased?
6. What is the decimal/binary gap at TB scale, approximately?
7. What distinguishes redundancy, backup, and archive?
8. Name three things that make exported video usable as evidence.

## References

- [`../32_Engineering_Math/04_storage.md`](../32_Engineering_Math/04_storage.md) — the derivation:
  storage arithmetic, decimal vs binary, the inverse problem, presenting a range. Prerequisite.
- [`../28_Calculators/psec/video.py`](../28_Calculators/psec/video.py) —
  `stream_tb_for_retention`, `retention_days_achievable`, `VideoSystem`.
- `[PRACTICE]` RAID rebuild rates, the ~5% format overhead, and the guidance to prefer RAID 6 are
  engineering practice and vary by array, controller, and load. Verify against the actual product.
- `[VERIFY]` Retention obligations, evidentiary requirements, chain-of-custody standards, and
  privacy constraints on stored video are **legal** questions that vary by jurisdiction and
  industry. Engineers implement them; they do not determine them. Get the requirement in writing
  from someone qualified to state it.
- `[MFR][VERIFY]` Export hashing, edge-recording backfill behaviour, and failover times are
  per-product claims. Test them at commissioning.

---

**Next:** [08 — VMS Architecture](08_vms_architecture.md) — the servers this storage hangs off,
where they fail, and what federation actually buys.
