# Solutions — 07 Storage, Retention, and Redundancy

> Work the exercises in [`../07_storage_and_retention.md`](../07_storage_and_retention.md) before
> reading this. Storage figures were produced by running
> [`../../28_Calculators/psec/video.py`](../../28_Calculators/psec/video.py) and transcribed.

---

## E7.1 — 31 cameras, 1.31 TB/day, 30 days

**(a) Usable storage required.**

```
raw need   = 1.31 TB/day × 30 days = 39.30 TB
+20% headroom                      = 47.16 TB usable
```

**(b) RAID 6 with 16 TB disks, 5% format overhead.**

Work backwards through the format overhead first, then add parity:

```
capacity needed before format loss = 47.16 / 0.95 = 49.64 TB
data disks = ceil(49.64 / 16) = 4
plus 2 parity                = 6 disks total
```

**Six 16 TB disks.** Delivering 64.0 TB usable, **60.8 TB after format overhead** — comfortably
above the 47.16 TB requirement, with genuine room to extend retention later. Raw purchase 96 TB.

**(c) RAID 10, same disks.**

```
data disks = 4 (as above), mirrored → 8 disks total
usable = 64.0 TB → 60.8 TB after format
raw    = 128 TB
```

**Eight disks.** The capacity penalty is **50% of raw** against RAID 6's 33% here — two extra disks
for the same usable capacity. What that buys is much faster rebuild (a mirror copies one disk
rather than reconstructing from parity across the set) and better write performance. For a video
array, which is write-heavy and rebuild-sensitive, RAID 10 is a defensible choice at a real price;
at larger scale the capacity cost usually decides against it.

**(d) "Why not RAID 5 and one fewer disk?"**

Answer with the rebuild number:

> RAID 5 would save one disk — 16 TB of raw capacity. What it costs is the rebuild window: if a
> disk fails, reconstructing a 16 TB disk at a realistic 50 MB/s while the array is still recording
> takes about **89 hours — nearly four days.** Throughout those four days RAID 5 has **no remaining
> redundancy at all**, so a second disk failure, or a single unrecoverable read error anywhere
> across the tens of terabytes the rebuild has to read, loses the entire array and all recorded
> video. The disks are the same age and the same batch, and they are being worked harder than at
> any other time. RAID 6 survives that second failure. One disk is a cheap price for not gambling
> the array on a four-day window.

---

## E7.2 — 60 TB array, 44 cameras at 4.2 Mbps

**(a) Achievable retention.**

Daily consumption:

```
per camera:  4.2 Mbps × 24 h → 45.36 GB/day
system:      45.36 GB × 44   = 1.996 TB/day
```

Retention:

```
60 TB / 1.996 TB per day = 30.06 days
```

**About 30 days** — or **25.05 days** if 20% is reserved as headroom, which it should be.

*(If that "60 TB" is actually 60 TiB as reported by the OS, the figure is 33.05 days. Ask which it
is.)*

**(b) The correction, for a client expecting 60 days.**

> Your 44 cameras produce about 45 GB each per day at their current settings, which is very close
> to 2 TB per day for the system. Against a 60 TB array that works out at just over **30 days**, and
> realistically closer to **25** once you keep a sensible reserve so the array is never running
> completely full. I suspect the 60-day figure came from an assumption of about 2 Mbps per camera;
> yours are running at 4.2, which is entirely normal for these scenes but is double what that
> estimate assumed. The good news is this is measured rather than estimated, so we can plan against
> it confidently — and if 60 days is a real requirement rather than an expectation, there are a
> few ways to get there.

Note the moves: give the daily figure (checkable), give both numbers (raw and with reserve), offer
a **specific explanation** for where their belief came from rather than leaving them feeling
misled, and end with a path forward.

**(c) Two options to reach 90 days.**

```
90 days at current rate: 1.996 TB/day × 90 = 179.63 TB raw
                                   +20%    = 215.55 TB usable required
```

| Option | What it requires | What it costs |
|---|---|---|
| **A. Add storage** | Expand from 60 TB to **~216 TB usable** — a 3.6× increase. In RAID 6 with 16 TB disks that is roughly 16 data + 2 parity disks | Capital, chassis capacity, power, and rack space. Check the array can physically expand before offering this |
| **B. Motion recording at 50% duty on suitable cameras** | Halves consumption to ~1.0 TB/day → **~90 TB usable** with headroom | **Missed-event risk** ([lesson 06](../06_compression_and_bandwidth.md) E6.4). Must exclude identification and high-value-asset cameras, which reduces the saving |

*(A third, often the best: **per-zone retention** — 90 days only where the obligation actually
applies, 30 days elsewhere. If only 10 of the 44 cameras need 90 days, the total is far below
either option above. Ask which zones drive the 90-day requirement before pricing a site-wide
increase — this is the answer that most often turns out to be right.)*

---

## E7.3 — The design review findings

**(a) Findings in order of severity.**

1. **Monitoring goes to a departed employee's address.** Nobody will learn that a disk has failed.
2. **RAID 5 with 20 TB disks.** A rebuild takes ~111 hours (4.63 days) at 50 MB/s with zero
   remaining redundancy.
3. **No hot spare.** The rebuild cannot even begin until a human notices and attends with a disk.

**(b) The failure each enables.**

1. **Dead monitoring address** → a failed disk is never reported. The array runs degraded
   indefinitely. The *second* failure — which is now the one that destroys the array — arrives with
   no warning at all, and the first anyone knows is that the video system is gone. **This is the
   most severe finding because it silently disables the protection the other two depend on.**
2. **RAID 5 on 20 TB disks** → during the 4.63-day rebuild the array has no redundancy. A second
   disk failure or a single unrecoverable read error across the ~140 TB of reads the rebuild
   performs destroys the array and every recording on it. On same-age, same-batch disks under the
   heaviest load they ever see, this is a realistic scenario rather than a theoretical one.
3. **No hot spare** → the rebuild window is extended by the entire human response time: noticing,
   sourcing a disk, scheduling a visit. Realistically days added to an already multi-day window,
   and here it is unbounded because of finding 1.

**Note how they compound:** with no monitoring, nobody knows to fit a disk; with no hot spare,
nothing happens automatically; and with RAID 5, the state they are sitting in has no margin. The
system is one disk failure away from being one disk failure away from total loss, and no one will
be told about either.

**(c) Executive-summary recommendation, one sentence.**

> The recording array is configured so that a single disk failure will go unreported and leave the
> system with no protection against a second failure for roughly four days — we recommend
> reconfiguring to RAID 6 with a hot spare and redirecting failure alerts to a monitored address,
> as a priority item.

*(It leads with the consequence, not the technology; it is specific about the exposure; and it
gives the remedy in the same sentence. An executive summary that says "RAID 5 is not best practice"
communicates nothing to the person who has to approve the spend.)*

---

## E7.4 — Incident on day 3, reported on day 41, retention 30 days

**(a) What exists and what does not.**

**The footage does not exist.** The incident occurred on day 3; retention is 30 days; by day 33 it
was overwritten. When the report arrives on day 41 the recording has been gone for eight days, and
nothing can recover it — this is not a case where deleted data might be retrievable, because the
storage has been continuously overwritten by 38 days of subsequent recording.

What **does** exist: the system's own logs (if retained longer), access-control records, and any
footage from day 11 onward. And, critically, **any export that was made at the time** — which is
where the actual failure lives.

**(b) The process failure.**

**It is not a storage failure.** The system did exactly what it was specified to do, and 30-day
retention was met precisely.

The failure is that **nothing in the process converted "an incident occurred" into "footage was
preserved."** Either the incident was not recognised as one on day 3, or it was recognised and
nobody exported the video. This is an **archive and workflow** failure — the gap the lesson
identifies as the one that most often fails: the incident is recorded, nobody exports it, and the
retention clock deletes it on schedule.

A secondary contributor: the 30-day retention itself was likely never tested against **how long
this type of incident takes to surface**. A 38-day reporting delay is entirely ordinary for
harassment, internal theft, and insurance matters.

**(c) The recommendation, with an owner.**

> **Recommendation.** Establish an incident-preservation procedure with a named owner. Whenever any
> incident, complaint, or claim is logged — by security, HR, or facilities — the duty security
> supervisor exports the relevant video within **72 hours** and files it to the incident record,
> before retention can expire. This is a standing instruction, not a request that has to be raised
> each time.
>
> **Owner:** Security Operations Manager, with HR and Facilities required to notify Security when
> any complaint that might involve a physical location is opened.
>
> **Supporting changes:** (i) review the 30-day retention against how long incidents at this site
> historically take to surface — a sample of the last two years of incident records will answer it,
> and if the median delay exceeds 30 days the retention is simply wrong; (ii) extend retention in
> the specific zones where late-surfacing incidents cluster; (iii) verify the export workflow is
> quick enough that a supervisor will actually do it under time pressure.

**What is being graded:** recognising this is a **process** failure and saying so without blaming
the storage design; naming a specific owner and a specific time limit (a recommendation without
both is a wish); connecting HR and Facilities to Security, since the reporting delay comes from
those functions not notifying; and challenging the retention period with evidence rather than
simply proposing to increase it.

---

## E7.5 — 🧠 Five ways to reduce storage cost on 120 cameras

Ordered by how strongly I would recommend them.

**1. Per-zone retention. (No loss of image quality or retention where it matters.)**

Almost every 120-camera system carries one retention figure across all zones. Interrogate it: if
the 30 days derives from an obligation covering only the cash office and the loading dock, then 90
cameras are being retained for 30 days out of habit. Dropping general areas to 14 days while
*raising* the obligated zones to 60 can reduce total storage substantially **and improve
compliance at the same time**. This is the option that most often wins and it costs only the
conversation required to establish which obligation applies where.

**2. Measure actual bitrates and re-size against them. (No capability loss whatsoever.)**

Most systems are sized on estimates. As [lesson 06](../06_compression_and_bandwidth.md) E6.5 shows,
those estimates are frequently wrong in **both** directions — interiors over-estimated, exteriors
under. Measuring for 30 days and re-provisioning against real figures often frees capacity with no
change to the design at all. If it turns out the system is under-provisioned, that is worth knowing
urgently and is not a cost the client avoided by not looking.

**3. Frame rate reduction on non-critical cameras.**

15 fps rather than 30 halves the data for those cameras `[PRACTICE]`. For corridors, car parks, and
general area coverage, 15 fps is entirely adequate for establishing what happened and who was
present. **Cost:** some loss of motion continuity, and it becomes harder to follow very fast events
frame by frame. **Do not apply it** to cameras covering fast motion where sequence matters — a
gate, a till, a vehicle lane. Note this is independent of shutter speed and does **not** worsen
motion blur ([lesson 03](../03_sensors_and_low_light.md)).

**4. H.265 on cameras and clients that support it well.**

Roughly 40–50% bitrate reduction for similar quality. **Cost:** decode load on workstations, which
can reduce how many streams an operator can watch simultaneously, plus compatibility risk on
export and analytics. Verify the workstation can handle the intended stream count before
committing — trading storage cost for an operator who cannot open their video wall is not a saving.

**5. Motion recording on genuinely low-risk zones only.**

Storage scales linearly with duty cycle, so the arithmetic is attractive. **Cost:** the
missed-event risk, which is why this is last. Apply only to zones where the consequence of a missed
event is low, never to identification cameras or high-value assets, and always with pre- and
post-event buffers and a written, acknowledged disclosure
([lesson 06](../06_compression_and_bandwidth.md) E6.4). Note the saving is smallest exactly where
activity is lowest — which is where it is safest to apply — so it often delivers less than hoped.

**Explicitly not recommended:** reducing resolution below the per-zone DORI target, or shortening
retention in an obligated zone. Both trade a capability the system was bought for against a cost
that options 1–3 can usually cover without any loss at all.

> 🧠 **The framing for the client:** *"Before we reduce anything the system does, let me check two
> things that might cost nothing — whether every zone actually needs the same retention, and
> whether our bitrate assumptions match what your cameras are really producing. Those two have
> covered the whole gap on most systems I have looked at. If they don't, here is the order I'd
> trade capability in, and why."*

---

## Retrieval check — answers

1. **The client should choose it**, on a legal, regulatory, insurance, or operational basis. The
   engineer's job is to ensure someone chose it deliberately, to record **who** and **on what
   basis**, and to state the consequence.
2. **"How long does this type of incident typically take to surface here?"** — asked of HR, loss
   prevention, and the duty supervisor, not of facilities or IT.
3. RAID protects against **disk failure**. It does not protect against fire, flood, theft,
   ransomware, accidental or deliberate deletion, or controller-propagated corruption.
4. Because the **rebuild takes days** (≈3.7 days for 16 TB, ≈4.6 days for 20 TB at 50 MB/s) and
   RAID 5 has **no remaining redundancy** during it, while reading tens of terabytes off same-age
   disks under maximum load.
5. **RAID parity overhead** and **filesystem/format overhead** (~5%).
6. Approximately **10%** — see [32/04](../../32_Engineering_Math/04_storage.md).
7. **Redundancy** survives component failure; **backup** survives loss of the primary including
   fire and ransomware; **archive** preserves selected material beyond the retention period. Most
   systems have only the first.
8. Any three of: **NTP time synchronisation**, export **without re-encoding**, native **timestamp
   and camera identity** carried in the export, a **hash or signature**, a **playable format**, and
   an **audit log** of who exported what and when.
