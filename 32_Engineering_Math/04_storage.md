# 04 — Storage and Retention

> Derives the storage half of
> [`../28_Calculators/psec/video.py`](../28_Calculators/psec/video.py). Takes the bitrate figures
> from [lesson 03](03_bandwidth.md) and turns them into disk.

> ⚠️ **Lesson 03's warning still applies, and harder.** Every figure here inherits the bitrate
> uncertainty *and multiplies it by a retention period*. **A design that is 30% short on storage
> silently shortens retention, and nobody finds out until they need day-28 video and it is gone.**
> This lesson's most important content is not the arithmetic. It is the two sections on presenting
> a range and on the inverse problem.

## Learning objectives

- Derive GB/day from a bitrate, tracking every unit conversion explicitly.
- Explain the decimal/binary distinction, compute it correctly, and recognize the common error
  that halves it.
- Compute storage for a retention period, apply headroom, and present an honest range.
- Solve the inverse problem — how many days does the storage they already own actually buy? —
  and explain why the answer is usually much worse than the client believes.
- Compute RAID raw capacity and state precisely what RAID does and does not protect against.

---

## Derivation 1 — GB per day

A bitrate is bits per second. Storage is bytes. The conversion is four steps and people drop one.

```
   Mbps  ──×3600──►  megabits per hour
         ──×hours──►  megabits per day
         ──÷8──────►  megaBYTES per day
         ──÷1000───►  gigabytes per day

   ┌─────────────────────────────────────────────────┐
   │   GB/day  =  Mbps × 3600 × hours / 8 / 1000     │
   └─────────────────────────────────────────────────┘
```

### 🧮 Worked example 4.1 — the test case

4 Mbps, continuous (24 h):

```
   megabits/day  =  4.0 × 3600 × 24   =  345,600 Mb
   megabytes/day =  345,600 / 8       =   43,200 MB
   gigabytes/day =  43,200 / 1000     =     43.2 GB
```

**43.2 GB/day.** This is `test_gb_per_day_decimal`.

> 🧠 **The shortcut worth memorizing:** `1 Mbps ≈ 10.8 GB/day` continuous. Then 4 Mbps is 43.2,
> 6 Mbps is 64.8, 10 Mbps is 108. This lets you sanity-check any vendor's storage figure in your
> head, in the meeting, which is when it is useful.
>
> Derivation of the constant: `1 × 3600 × 24 / 8 / 1000 = 10.8`.

---

## Derivation 2 — Decimal vs binary, and the error that hides in it

**Disk vendors sell decimal. Operating systems report binary.**

| | Decimal (SI) | Binary (IEC) |
|---|---|---|
| kilo | 10³ = 1,000 | Ki = 2¹⁰ = 1,024 |
| mega | 10⁶ | Mi = 2²⁰ |
| giga | 10⁹ | Gi = 2³⁰ = 1,073,741,824 |
| tera | 10¹² | Ti = 2⁴⁰ = 1,099,511,627,776 |

```
   1 TB  =  10¹²  bytes
   1 TiB =  2⁴⁰   bytes  =  1.099511627776 × 10¹²

   Ratio: 2⁴⁰ / 10¹²  =  1.0995      ← the classic ~10% at the TB scale
```

**A 10 TB disk shows up as 9.09 TiB in the OS.** Nothing is missing; the units differ.

### ⚠️ The error this module used to contain

**A bitrate is decimal.** `Mbps` means 10⁶ bits per second. So the "megabytes" that fall out of
the derivation above are **decimal megabytes — 10⁶ bytes each.**

To convert those to **gibibytes**, you divide by:

```
   2³⁰ bytes/GiB  ÷  10⁶ bytes/MB   =   1,073.741824
```

**Not by 1024.** Dividing decimal megabytes by 1024 produces a number that is neither GB nor GiB.

Worked, for the same 4 Mbps stream:

| Route | Calculation | Result |
|---|---|---|
| Decimal GB | 43,200 / 1000 | **43.200 GB** ✅ |
| **True GiB** | 43,200 / 1073.741824 | **40.233 GiB** ✅ |
| The error | 43,200 / 1024 | **42.188** ❌ — 4.86% high, and dimensionally meaningless |

**How the error compounds at the TB scale**, over 30 days:

| Route | 30-day figure | Ratio to decimal |
|---|---|---|
| Decimal | **1.296 TB** | — |
| True binary | **1.1787 TiB** | **1.0995** ✅ matches 2⁴⁰/10¹² |
| The error | 1.2360 | 1.0486 ❌ |

**The buggy version reported the decimal/binary gap as 4.9% — less than half the true 9.95% —
which is precisely the "classic ~10% error at the TB scale" that the module's own docstring warns
about.** The code contradicted its own documentation and no test caught it, because the only test
covering that path asserted `binary < decimal`, which was true either way.

> 🧠 **This is why the derivation lessons exist.** The code was written first, was tested, ran
> clean, and produced a plausible number. Working the units by hand is what surfaced it. Two
> lessons generalize:
>
> 1. **A test that only checks the direction of an inequality is barely a test.** It passes for an
>    infinite family of wrong implementations. `test_binary_units_are_true_gibibytes` now pins the
>    value, and `test_decimal_binary_gap_at_tb_scale_is_about_ten_percent` pins the ratio against
>    `2⁴⁰/10¹²` — a value derived from the definition rather than from the code.
> 2. **When code and its comments disagree, one of them is a bug, and it is not always the
>    comment.** The docstring was right and the implementation was wrong.

Both are now in the test file with the hand calculation in the comment. See
[`../28_Calculators/tests/test_psec.py`](../28_Calculators/tests/test_psec.py).

### Which one do you quote?

**Quote decimal TB when purchasing, and tell the client what the OS will show them.** Otherwise
you get the phone call: *"We bought 100 TB and the server says 91."*

---

## Derivation 3 — Storage for a retention period

```
   ┌────────────────────────────────────────────────────────────┐
   │   TB per stream  =  (GB/day) × retention_days / 1000        │
   │   System TB      =  Σ over groups of (per-stream × count)   │
   └────────────────────────────────────────────────────────────┘
```

### 🧮 Worked example 4.2 — the test case

4 Mbps, 30-day retention:

```
   43.2 GB/day × 30 = 1,296 GB = 1.296 TB
```

This is `test_tb_for_retention`.

### 🧮 Worked example 4.3 — a system

50 indoor cameras at 6 Mbps, 30 outdoor at 10 Mbps, all continuous, 30-day retention:

```
   Indoor,  per camera:  6 × 10.8 = 64.8 GB/day × 30 = 1,944 GB = 1.944 TB
                         × 50 cameras                = 97.2 TB

   Outdoor, per camera: 10 × 10.8 = 108 GB/day × 30 = 3,240 GB = 3.240 TB
                         × 30 cameras                = 97.2 TB

   Raw total                                          = 194.4 TB
```

This is `test_system_totals`. Note the coincidence that both groups land on 97.2 TB — 50 cameras
at 6 Mbps and 30 at 10 Mbps are the same total bitrate. Useful sanity check: **storage is driven
by aggregate bitrate, not camera count.**

### Effective hours

If a group has a motion duty cycle (lesson 03), the storage calculation uses
`effective_hours = hours_per_day × duty_cycle`. A 24-hour camera at 0.25 duty consumes as much as
a 6-hour continuous camera.

**Note the asymmetry with lesson 03 again:** duty cycle reduces storage and does *not* reduce
peak bandwidth.

---

## Derivation 4 — Headroom and the honest range

### Headroom

```
   sized = raw × (1 + headroom)          DEFAULT_HEADROOM = 0.20
```

20% covers estimate error, growth, and filesystem overhead. `test_headroom_applied` pins it.

```
   194.4 TB × 1.20 = 233.3 TB
```

### The range

Headroom alone is not honesty. It is a single number with a safety factor, and it still *looks*
like a prediction.

```
   ┌─────────────────────────────────────────────────┐
   │   low   =  sized × 0.7                          │
   │   high  =  sized × 1.6                          │
   └─────────────────────────────────────────────────┘
```

The multipliers reflect the real spread between an optimistic smart-codec estimate and a busy,
noisy, low-light scene. For the 194.4 TB system:

```
   sized = 233.3 TB
   range = 163.3 TB  to  373.2 TB
```

**Present the range, with the point estimate inside it.** `test_storage_range_brackets_point_estimate`
asserts exactly that: `low < point < high`.

> ⚠️ **A 163–373 TB range looks unprofessional to a junior and reads as competence to anyone who
> has built one of these.** The alternative — "233 TB" — is a number that will be wrong, presented
> with a confidence nobody can justify. When the array fills in month seven, the engineer who gave
> a range has a conversation about which end of it the scene landed on. The engineer who gave a
> point estimate has a different conversation.
>
> **How to present it:** *"233 TB is our best estimate. Realistically it's 165 to 375 depending on
> how busy these scenes turn out to be. I'd like to pilot two cameras for 24 hours before we buy —
> that would collapse most of this range and it costs us a week."* That paragraph is the whole
> skill.

---

## Derivation 5 — The inverse problem

**The question you actually get asked**, especially on retrofits: *"We have 100 TB. How long does
that last?"*

```
   ┌────────────────────────────────────────────────┐
   │   days  =  available_TB / (TB consumed per day) │
   └────────────────────────────────────────────────┘
```

### 🧮 Worked example 4.4 — the conversation that goes badly

The same 80-camera system. Consumption per day:

```
   Indoor:  50 × 1.944 TB / 30 days  =  3.24 TB/day
   Outdoor: 30 × 3.240 TB / 30 days  =  3.24 TB/day
   Total                              =  6.48 TB/day
```

**On 100 TB:**
```
   days = 100 / 6.48 = 15.4 days
```

**They believe they have 30 days. They have 15.** And that is before headroom — with the 20%
headroom the system needs, the honest figure is lower still, and if the scenes are busy it could
be under 10.

`test_retention_inverse_round_trips` verifies the inverse is a true inverse: take a system's raw
storage requirement, feed it back in, get the original retention days.

> 🧠 **Run this calculation unprompted on every retrofit.** It is thirty seconds of arithmetic and
> it is frequently the single most valuable thing you tell a client all week. It is also how you
> discover that a "we just need more cameras" project is actually a storage project.

---

## Derivation 6 — RAID

RAID trades raw capacity for redundancy. To get `usable` capacity you must buy `raw`:

```
   ┌──────────────────────────────────────┐
   │   raw  =  usable / efficiency        │
   └──────────────────────────────────────┘
```

| Level | Efficiency | Constraint | Survives |
|---|---|---|---|
| RAID 0 | 1.0 | — | nothing |
| RAID 1 | 0.5 | even disk count | 1 disk per mirror |
| RAID 5 | (n−1)/n | n ≥ 3 | 1 disk |
| RAID 6 | (n−2)/n | n ≥ 4 | 2 disks |
| RAID 10 | 0.5 | even, n ≥ 4 | 1 disk per mirror |

### 🧮 Worked example 4.5 — the test cases

For **100 TB usable, 8 disks per group:**

```
   RAID 5:   efficiency = 7/8 = 0.875   →  raw = 100 / 0.875 = 114.29 TB
   RAID 6:   efficiency = 6/8 = 0.750   →  raw = 100 / 0.750 = 133.33 TB
   RAID 10:  efficiency = 0.5           →  raw = 100 / 0.5   = 200.00 TB
```

These are `test_raid_efficiencies`.

**Note that RAID 5 and 6 efficiency depends on group size**, which is a lever people forget:

| Configuration | Efficiency | Raw for 100 TB usable |
|---|---|---|
| RAID 5, 8 disks | 0.875 | 114.3 TB |
| RAID 5, 12 disks | 0.917 | 109.1 TB |
| RAID 6, 8 disks | 0.750 | 133.3 TB |
| RAID 6, 16 disks | 0.875 | 114.3 TB |

**RAID 6 across 16 disks costs exactly what RAID 5 across 8 does, and survives two failures
instead of one.** Wider groups amortize the parity. That is a real design lever and it is usually
free.

**Invalid configurations raise** (`test_raid_disk_count_validation`): RAID 5 with 2 disks, RAID 6
with 3, RAID 10 with 5. Each is arithmetically expressible and physically meaningless, and
silently returning a number for them would be worse than failing.

### What RAID does not do

`[PRACTICE]` **RAID protects against disk failure. That is the entire list.** It does not protect
against:

- Controller failure
- Chassis loss, fire, flood, theft
- Ransomware or malicious deletion
- Accidental deletion or a misconfigured retention policy
- Filesystem corruption
- **The rebuild itself** — during a rebuild the array is slower *and* more vulnerable, and
  large-capacity drives take a long time to rebuild. A second failure during a RAID 5 rebuild
  loses the array. This is the main argument for RAID 6 at modern drive sizes.

> ⚠️ **"It's on RAID" is not a backup answer, and video is the case where people most often think
> it is** — because nobody backs up 200 TB of surveillance video, so RAID ends up being the only
> protection there is. That may be an acceptable decision. It has to be a *decision*, stated to
> the owner, not an assumption.

---

## Assumptions and limits

| Assumption | Reality |
|---|---|
| One bitrate per camera | Inherited from lesson 03; the dominant uncertainty |
| Constant consumption per day | Scenes vary by season, daylight hours, and occupancy |
| Retention is uniform | Real systems often keep alarm clips longer than continuous footage |
| No audio, metadata, or analytics streams | All add, typically 5–10% `[VERIFY per system]` |
| Filesystem overhead is inside the headroom | Usually true at 20%; verify for the specific platform |
| Storage is one pool | Distributed and edge recording change the arithmetic entirely |

---

## Common mistakes

⚠️ **Dividing decimal megabytes by 1024.** The error this module contained.

⚠️ **Quoting binary figures when purchasing**, or decimal figures when explaining what the OS will
show.

⚠️ **Presenting storage as a point estimate.**

⚠️ **Forgetting the inverse question on retrofits.**

⚠️ **Sizing RAID group width by habit.** RAID 6 across 16 disks is often free relative to RAID 5
across 8.

⚠️ **Treating RAID as backup.**

⚠️ **Applying headroom and then treating the result as a ceiling.** Headroom covers *estimate
error*, not growth you already know about.

⚠️ **Forgetting that duty cycle reduces storage but not peak bandwidth.**

---

## Junior vs. Senior

**Junior:** computes GB/day and system storage correctly; knows the decimal/binary distinction;
applies headroom; computes RAID raw capacity.

**Senior:** presents storage as a range with the assumptions stated and offers a pilot to collapse
it; runs the inverse retention calculation unprompted on every retrofit and leads with the answer;
chooses RAID group width deliberately; states plainly that RAID is not a backup and gets a
decision rather than an assumption; and, when the units look wrong, works them by hand rather than
trusting the tool — because the tool was written by someone making the same assumptions.

---

## Problem set

**P4.1** A camera streams 8 Mbps continuously.
- (a) Compute GB/day, decimal.
- (b) Compute true GiB/day.
- (c) Compute what you would get by incorrectly dividing megabytes by 1024, and the percentage
  error.
- (d) Compute 45-day retention in TB and in TiB, and verify the ratio equals 2⁴⁰/10¹².

**P4.2** A system: 60 cameras at 6 Mbps and 20 cameras at 18 Mbps, all continuous, 60-day
retention.
- (a) Compute raw storage.
- (b) Apply 20% headroom.
- (c) Give the honest range.
- (d) Write the two sentences you would say to the client presenting this.

**P4.3** A client has an existing 120 TB array and 96 cameras: 72 at 6 Mbps and 24 at 10 Mbps, all
continuous. They believe they have 30 days of retention.
- (a) Compute daily consumption.
- (b) Compute actual retention.
- (c) They want 30 days. Give three options with the cost driver of each.

**P4.4** For 250 TB usable, compute raw capacity for RAID 5 at 8 and 12 disks, and RAID 6 at 8, 12,
and 16 disks. Then recommend a configuration and justify it in three sentences, addressing rebuild
risk.

**P4.5** A colleague's storage calculation for a 40-camera system comes out at 61 TB. Yours comes
out at 88 TB. Both of you used the same camera count and retention. List the five most likely
places the difference lives, in the order you would check them.

**P4.6** Explain to a client, in under 150 words, why you are giving them a storage range instead
of a number, without sounding like you don't know the answer.

**P4.7** 🧮 Derive the `1 Mbps ≈ 10.8 GB/day` shortcut from first principles. Then derive the
equivalent shortcut for TB per 30 days per Mbps, and use it to check worked example 4.3 in one
line.

**P4.8** The module's binary-units defect went undetected because the only test on that path
asserted `binary < decimal`. Write, in words, three other tests you would add to this module that
pin *values or invariants derived from definitions* rather than from the implementation. For each,
say what class of bug it would catch.

> Answers: [`_solutions/04_storage_solutions.md`](_solutions/04_storage_solutions.md)

---

## Retrieval check

1. Write the GB/day derivation with every unit step.
2. What is `1 Mbps` in GB/day, continuous?
3. Why do you divide decimal megabytes by 1073.741824 and not 1024 to get GiB?
4. What is the true ratio of TB to TiB, and where does it come from?
5. Why present storage as a range rather than a value?
6. Write the inverse retention formula and say when you use it.
7. Why is RAID 6 across 16 disks often free relative to RAID 5 across 8?
8. Name five things RAID does not protect against.

---

## References

- [`../28_Calculators/psec/video.py`](../28_Calculators/psec/video.py) — the implementation,
  including the corrected binary conversion.
- [`../28_Calculators/tests/test_psec.py`](../28_Calculators/tests/test_psec.py) — `TestVideo`.
- IEC 80000-13 — binary prefixes (Ki, Mi, Gi, Ti). `[STANDARD][VERIFY]`
- [`03_bandwidth.md`](03_bandwidth.md) — where the bitrate figures come from.
- [`../20_Data_Center/`](../20_Data_Center/) and [`../08_Networking/`](../08_Networking/) —
  storage architecture and topology *(not yet written)*.

**Next:** [05 — PoE Budgets and Switch Capacity](05_poe.md)
