# Solutions — 04 Storage and Retention

---

## P4.1 — Units, 8 Mbps continuous

**(a) Decimal GB/day**
```
   8 × 3600 × 24 = 691,200 Mb
   / 8           =  86,400 MB
   / 1000        =    86.4 GB/day
```
(Or straight from the shortcut: `8 × 10.8 = 86.4`.)

**(b) True GiB/day**
```
   86,400 MB × 10⁶ bytes = 8.64 × 10¹⁰ bytes
   / 2³⁰                 = 80.466 GiB/day
```
Equivalently `86,400 / 1073.741824 = 80.4663`.

**(c) The wrong route**
```
   86,400 / 1024 = 84.375        ← neither GB nor GiB
   error vs. true GiB: 84.375 / 80.4663 = 1.04858  →  +4.86%
```

**(d) 45-day retention**

| | Value |
|---|---|
| Decimal | **3.8880 TB** |
| Binary | **3.5361 TiB** |
| Ratio | **1.099511628** |
| 2⁴⁰/10¹² | **1.099511627776** ✅ |

The ratio matches the definition to nine decimal places, which is the check that says your unit
chain is right. **Note that the error in (c) is 4.86% while the true decimal/binary gap is 9.95%
— the wrong route recovers slightly less than half the real difference**, which is exactly why it
looks plausible and survives review.

---

## P4.2 — 80-camera system, 60-day retention

**(a) Raw storage**

```
   Per camera @ 6 Mbps:   6 × 10.8 = 64.8 GB/day × 60 = 3,888 GB = 3.888 TB
     × 60 cameras                                                = 233.28 TB

   Per camera @ 18 Mbps: 18 × 10.8 = 194.4 GB/day × 60 = 11,664 GB = 11.664 TB
     × 20 cameras                                                  = 233.28 TB

   Raw total                                                       = 466.56 TB
```

(Both groups land on 233.28 TB again — 60 × 6 = 360 Mbps and 20 × 18 = 360 Mbps. Storage tracks
aggregate bitrate, not camera count.)

**(b) With 20% headroom**
```
   466.56 × 1.20 = 559.87 TB
```

**(c) Honest range**
```
   low  = 559.87 × 0.7 = 391.9 TB
   high = 559.87 × 1.6 = 895.8 TB
```

**Range: roughly 390 to 900 TB, point estimate 560 TB.**

**(d) The two sentences**

> Our point estimate is **560 TB** for 60 days across these 80 cameras, and realistically it lands
> somewhere between **390 and 900** depending on how busy the outdoor scenes turn out to be — the
> twenty 4K cameras are most of the variance.
>
> I'd like to pilot two of those 4K cameras for 24 hours in their actual locations before we buy;
> that would collapse most of that range and it costs us about a week.

**Why the second sentence matters:** a range without a plan to narrow it is an engineer hedging.
A range *with* a cheap, specific action to resolve it is an engineer managing uncertainty. The
client hears the difference.

---

## P4.3 — The retrofit conversation

**(a) Daily consumption**
```
   72 × 6 Mbps  = 432 Mbps
   24 × 10 Mbps = 240 Mbps
   Total        = 672 Mbps

   672 × 10.8 GB/day = 7,257.6 GB/day = 7.2576 TB/day
```

**(b) Actual retention on 120 TB**
```
   120 / 7.2576 = 16.5 days
```

**They believe they have 30 days. They have 16.5** — and that is the raw figure with no headroom,
so in practice the array will start overwriting sooner than that.

**(c) Three options to reach 30 days**

Storage required: `7.2576 × 30 = 217.7 TB` raw, or **261.3 TB with 20% headroom.** They have 120.
**They are short by roughly 140 TB.**

| Option | What it does | Cost driver |
|---|---|---|
| **1. Buy storage** | Add ~140 TB. Nothing else changes; retention and image quality are untouched. | **Capital cost of disk, plus chassis/shelf capacity.** Check whether the existing array can even take another 140 TB, or whether this is a new chassis — that is often the real number. |
| **2. Reduce the streams** | H.265 if they're on H.264 (roughly halves it — could get to ~33 days on existing disk). Or drop frame rate to 15 fps (~38% reduction per lesson 03, giving ~27 days). | **Verification effort, plus quality.** H.265 needs camera and VMS support confirmed — on a retrofit, some cameras won't have it. Frame rate reduction costs motion smoothness in every clip ever reviewed. |
| **3. Tier the retention** | Keep 30 days on the cameras that matter and 7–14 on the rest. 96 cameras almost certainly do not all warrant identical retention. | **A policy decision, not a purchase.** Costs a conversation about which cameras are evidentially important, and VMS support for per-camera retention. |

**Recommendation order: 3, then 2, then 1.** Option 3 is free and frequently sufficient, and it
forces a question the client should answer anyway. Option 2 is cheap but needs verification.
Option 1 always works and is the only one that costs real money.

> 🧠 **Lead with the finding, not the options.** *"Before we talk about anything else — you have
> 16 days of retention, not 30."* That sentence reframes the entire project, and it is thirty
> seconds of arithmetic.

---

## P4.4 — RAID for 250 TB usable

| Configuration | Efficiency | Raw required |
|---|---|---|
| RAID 5, 8 disks | 0.875 | **285.7 TB** |
| RAID 5, 12 disks | 0.917 | **272.7 TB** |
| RAID 6, 8 disks | 0.750 | **333.3 TB** |
| RAID 6, 12 disks | 0.833 | **300.0 TB** |
| RAID 6, 16 disks | 0.875 | **285.7 TB** |

**Recommendation, three sentences:**

> **RAID 6 across 16-disk groups.** It costs exactly the same raw capacity as RAID 5 across 8
> disks — 285.7 TB either way — because the wider group amortizes the second parity drive, so the
> redundancy is genuinely free here.
>
> That matters because at these capacities the rebuild window is the real risk: a RAID 5 array
> rebuilding a large drive is slower and fully exposed, and a second failure during that window
> loses the array along with all the video on it.
>
> RAID 6 survives a second failure during the rebuild, which is precisely the scenario that
> destroys surveillance arrays — and since nobody backs up 250 TB of video, this array *is* the
> only copy.

**The reasoning being tested:** the naive read is "RAID 6 costs more than RAID 5." The table shows
that's only true at a fixed group width. **Group width is a free variable**, and once you treat it
as one, RAID 6 at 16 disks dominates RAID 5 at 8 disks outright — same cost, strictly better
failure tolerance.

---

## P4.5 — 61 TB vs. 88 TB, same cameras and retention

Ratio: 88/61 = **1.44**. Check in this order — cheapest to check first, and most likely first
within that:

**1. Bitrate assumption.** By far the most likely. A 1.44× ratio is entirely explicable by one of
you using 6 Mbps where the other used 8.6, or by one using a datasheet figure and the other a rule
of thumb. **Ask "what bitrate did you use and where did it come from?" first**, because it
resolves most of these in one question.

**2. Codec.** If one of you applied H.265 (×0.5) and the other didn't, the ratio would be nearer
2×, so this is probably not the whole story — but a partial application (H.265 on some groups)
could produce 1.44. Rules in or out quickly.

**3. Headroom.** 1.20 vs. 1.00 is a 1.2× factor. Combined with a modest bitrate difference this
easily reaches 1.44. Check whether one figure is "raw" and the other "sized" — **these two numbers
are frequently not the same quantity**, and that alone explains a lot of disagreements.

**4. Duty cycle / effective hours.** If one of you applied a motion duty cycle or reduced
recording hours to a group and the other assumed continuous, that scales directly.

**5. Decimal vs. binary.** Only a 1.0995× factor at TB scale, so it cannot be the whole
difference — but it can be a component, and it is worth checking because it is a *correctness*
problem rather than an assumption difference. If one of you is dividing by 1024 somewhere, the
error is 1.0486× and it will follow you into every future calculation.

> 🧠 **The general procedure: don't diff the answers, diff the assumptions.** Put both calculations
> side by side as a list of inputs — bitrate, source of bitrate, codec, fps, duty cycle, hours,
> retention, headroom, units — and the discrepancy usually identifies itself in under a minute.
> Two engineers arguing about 61 vs. 88 without doing that can burn an afternoon.

---

## P4.6 — Explaining the range

Model answer (144 words):

> The honest answer is that storage depends on how much is happening in front of each camera, and
> nobody knows that until the cameras are up.
>
> A camera watching a still corridor compresses down to almost nothing. The same camera watching a
> car park with moving trees, rain, and headlights at night can produce three or four times the
> data. It's the same hardware and the same settings — the scene is doing it.
>
> So a single number would be a guess dressed up as a calculation. Our best estimate is 560
> terabytes, and the realistic band is 390 to 900.
>
> Here's how we narrow it: put two of the outdoor cameras up for 24 hours and measure what they
> actually produce. That collapses most of the uncertainty, costs about a week, and it's a lot
> cheaper than buying 900 terabytes or running out at 390.

**What makes it work:** it explains the *mechanism* for the uncertainty, so the range reads as
knowledge rather than as hedging. Then it immediately offers a concrete, cheap way to reduce it —
which is what separates "I don't know" from "here is what we do about not knowing."

---

## P4.7 — 🧮 Deriving the shortcuts

**GB/day per Mbps:**
```
   1 Mbps × 3600 s/h × 24 h  =  86,400 Mb/day
   / 8                       =  10,800 MB/day
   / 1000                    =      10.8 GB/day

   ┌───────────────────────────────┐
   │   1 Mbps  =  10.8 GB/day      │
   └───────────────────────────────┘
```

**TB per 30 days per Mbps:**
```
   10.8 GB/day × 30 days  =  324 GB  =  0.324 TB

   ┌────────────────────────────────────────┐
   │   1 Mbps  =  0.324 TB per 30 days      │
   └────────────────────────────────────────┘
```

**Checking worked example 4.3 in one line:**
```
   Total bitrate = 50 × 6 + 30 × 10 = 300 + 300 = 600 Mbps
   Storage       = 600 × 0.324      = 194.4 TB       ✅
```

Matches the long-form calculation exactly.

> 🧠 **Why this shortcut is worth carrying:** it reduces a whole-system storage estimate to
> *aggregate bitrate × 0.324*, which you can do in your head in a meeting. It also makes the
> structure obvious — **storage is linear in aggregate bitrate and linear in retention days**, so
> you can answer "what if we go to 45 days?" instantly rather than re-running a spreadsheet.

---

## P4.8 — Three tests that pin definitions rather than implementation

The defect survived because `test_gb_per_day_binary_is_smaller_number` asserted only
`binary < decimal` — true for an infinite family of wrong divisors. Good tests here anchor to
something *outside* the code.

**Test 1 — Round-trip the full unit chain from bytes.**
Assert that `stream_gb_per_day(b, h, decimal_gb=True) × 10⁹` equals `b × 3600 × h / 8 × 10⁶`
bytes, computed independently in the test. Then assert the binary variant equals the same byte
count divided by 2³⁰.
*Catches:* any wrong divisor, any dropped or duplicated factor of 8, and any confusion between
bits and bytes — the whole class of unit-chain errors, by construction, because the test computes
bytes from the definition rather than from the function.

**Test 2 — Assert dimensionless ratios against their definitions.**
`decimal / binary` must equal `2³⁰/10⁹` at the GB scale and `2⁴⁰/10¹²` at the TB scale — values
written in the test as powers, not as decimals copied from a run.
*Catches:* the specific defect here, plus any future change that alters one conversion step
without the other. This is the strongest form: the expected value cannot be produced by running
the code, so a wrong implementation cannot "bless" it.

**Test 3 — Assert scaling invariants rather than values.**
Doubling the bitrate must exactly double GB/day; doubling retention must exactly double TB;
halving `hours_per_day` must exactly halve consumption. Assert to floating-point equality.
*Catches:* any accidental non-linearity — a stray rounding, a clamp, a lookup table quietly
introduced, or an off-by-one in a loop. These are cheap to write and they pin the *shape* of the
function, which survives refactoring better than any single value does.

**Honourable mentions worth adding:**
- A test that `stream_tb_for_retention(b, d)` equals `stream_gb_per_day(b) × d / 1000` — pinning
  the composition of the two functions, so they can't drift apart.
- A test that the class ratios in `DORI_PPF` hold (from lesson 02's P2.1), for the same reason:
  it is the property designers actually reason with, and nothing currently protects it.

> 🧠 **The general principle:** a test whose expected value was produced by running the code can
> only detect *changes*, not *errors*. A test whose expected value comes from a definition,
> a standard, or an independent hand calculation can detect the code being wrong on day one.
> The repo's convention — "expected values are hand-computed in the corresponding
> `32_Engineering_Math` lesson" — exists precisely to force the second kind, and this defect is
> what happens on the one path where it wasn't followed.
