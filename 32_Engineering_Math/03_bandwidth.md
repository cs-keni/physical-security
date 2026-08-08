# 03 — Video Bandwidth

> Derives the bitrate half of [`../28_Calculators/psec/video.py`](../28_Calculators/psec/video.py).
> Lesson 04 takes these numbers and turns them into storage.

> ⚠️ **Read this before the derivations.** Every number in this lesson and the next is an
> **estimate built on an assumed bitrate**, and real bitrate depends on scene content, motion,
> noise, lighting, codec implementation, and encoder tuning — none of which you know at design
> time. **Two vendors' calculators will disagree by 2× on the same camera.** That is not a bug in
> either one; it reflects genuine uncertainty. The engineering skill this lesson teaches is not
> computing a number. It is computing a number *and communicating how much you trust it.*

## Learning objectives

- State where a bitrate figure legitimately comes from, in order of preference.
- Derive the frame-rate scaling model, explain why it is deliberately sub-linear, and explain why
  a documented modelling choice beats an undocumented one.
- Apply codec factors and compose them correctly with frame-rate scaling.
- Distinguish peak from average bandwidth, and explain why network links are sized on peak even
  though storage is sized on average.
- Explain what a motion duty cycle actually assumes, and why it is a risk to be named rather than
  a saving to be booked.

---

## Where a bitrate comes from

Everything downstream is built on one number per camera. Get it from the best available source:

| Rank | Source | When to use it |
|---|---|---|
| **1** | **A measured stream from a pilot camera**, in the actual scene, at the actual settings, over 24 hours | Any project where storage is a material cost. This is the only source that accounts for *your* scene. |
| **2** | **The camera datasheet's bitrate table** for the specific model, resolution, and frame rate | Normal practice at design stage |
| **3** | **A reference table** like `TYPICAL_H264_MBPS` | Early estimating, feasibility, order-of-magnitude sanity checks |
| **4** | A vendor's online calculator | Cross-check only. Never as the primary source, and never without knowing its assumptions. |

`[PRACTICE]` The reference table in the calculator, for H.264, moderate motion, good lighting,
VBR with a quality target:

| Camera | Mbps |
|---|---|
| 1 MP @ 30 fps | 4.0 |
| 2 MP @ 30 fps (1080p) | 6.0 |
| 4 MP @ 30 fps | 10.0 |
| 5 MP @ 30 fps | 12.0 |
| 8 MP @ 30 fps (4K) | 18.0 |
| 12 MP @ 30 fps | 25.0 |

**Note that bitrate is sub-linear in resolution too.** 8 MP is four times the pixels of 2 MP and
three times the bitrate, because compression finds more redundancy in a denser image. Don't scale
bitrate by pixel count.

> 🧠 **Always write down which rank you used**, in the design narrative. "Storage sized from
> datasheet bitrates at 2 MP/30 fps H.265" and "storage sized from a rule of thumb" are different
> claims, and only one of them survives a client asking why they ran out of disk in month seven.

---

## Derivation 1 — Frame rate scaling

You have a bitrate at one frame rate and need it at another.

**The naive model is linear:** halve the frame rate, halve the bitrate. It is wrong, and it is
wrong in the dangerous direction — it **under**-estimates.

### Why linear is wrong

Two mechanisms:

**1. Inter-frame prediction gets less efficient.** Modern codecs encode most frames as differences
from previous frames. At 30 fps, consecutive frames are nearly identical and the difference is
tiny. At 5 fps, 200 ms have passed, everything has moved further, and the difference is large. So
each frame you keep is *more expensive* than it was at the higher rate.

**2. I-frames and overhead don't scale.** A full keyframe is sent on a fixed interval regardless
of frame rate, and stream overhead is roughly constant. Those bits are there at 5 fps just as they
were at 30.

### The model

```
   ┌─────────────────────────────────────────────────┐
   │   rate  =  base × ( to_fps / from_fps ) ^ 0.7   │
   └─────────────────────────────────────────────────┘
```

**The exponent 0.7 is a modelling choice**, not a physical constant. `[PRACTICE]` A square-root-ish
relationship matches observed encoder behaviour better than a linear one. It is documented in the
source **so you can challenge it rather than inherit it silently** — which is the point.

### 🧮 Worked example 3.1 — the shape of the model

Base 10 Mbps at 30 fps:

| Target fps | ratio | ratio^0.7 | Model | Linear model would say | Under-estimate if you used linear |
|---|---|---|---|---|---|
| 30 | 1.000 | 1.000 | **10.00** | 10.00 | — |
| 25 | 0.833 | 0.880 | **8.80** | 8.33 | 5% |
| 20 | 0.667 | 0.753 | **7.53** | 6.67 | 11% |
| 15 | 0.500 | 0.616 | **6.16** | 5.00 | **19%** |
| 10 | 0.333 | 0.463 | **4.63** | 3.33 | **28%** |
| 5 | 0.167 | 0.285 | **2.85** | 1.67 | **41%** |
| 1 | 0.033 | 0.092 | **0.92** | 0.33 | **64%** |

`test_frame_rate_scaling_is_sublinear` pins the essential property at 15 fps: the result must be
**less than** the full-rate figure and **more than half** of it. Both bounds matter — the first
says frame rate reduction does something, the second says it does less than you hoped.

> ⚠️ **The practical failure this prevents:** someone proposes halving frame rate to fit the
> storage budget and books a 50% saving. The real saving is about 38%. On a 200 TB system that is
> a 24 TB shortfall, discovered when retention quietly drops from 30 days to 26 and nobody
> notices until they need day 28.

### The honest caveat

This model is a curve fit to observed behaviour, not a derivation from codec internals. Real
encoders vary. **If frame rate reduction is load-bearing in your storage budget — if the design
only fits because you dropped to 15 fps — measure it on the actual camera rather than trusting
0.7.** A modelling choice is fine for estimating and not fine for a decision that has no margin.

---

## Derivation 2 — Codec scaling

```
   H.265 / HEVC:   × 0.5      [PRACTICE] — vendors claim 0.4–0.6
   Smart codec:    × 0.5      [PRACTICE] — 0.2–0.8 in reality, highly scene-dependent
```

Both are multiplicative and compose with frame-rate scaling:

```
   rate = base × (to_fps/from_fps)^0.7 × codec_factor × smart_factor
```

### 🧮 Worked example 3.2 — composing the factors

10 Mbps H.264 at 30 fps, moved to H.265 at 15 fps:

```
   fps factor    = (15/30)^0.7  =  0.61557
   codec factor  = 0.5

   rate = 10.0 × 0.61557 × 0.5  =  3.078 Mbps
```

**From 10.0 to 3.08 Mbps** — a 69% reduction. Add a smart codec and the model says 1.54 Mbps.

`test_h265_halves_bitrate` pins the codec factor exactly: `h265 == h264 × H265_FACTOR`.

> ⚠️ **The smart-codec range is the widest uncertainty in this whole module — 0.2 to 0.8 is a
> factor of four.** Smart/zipstream-type codecs work by spending very few bits on static scene
> regions. On an empty corridor at 3 a.m. they are spectacular. On a windy car park with moving
> foliage, rain, and headlights they can perform *worse* than plain H.265 because the analysis
> overhead buys nothing.
>
> **Never size storage on a smart-codec assumption without a pilot measurement in the actual
> scene.** If you must estimate, use 0.8 and say so. Booking 0.2 in a design and getting 0.8 in
> the building is how a system loses three quarters of its retention.

**Unsupported codecs raise.** `test_unsupported_codec_raises` checks that `mjpeg` is rejected
rather than silently treated as H.264. This is the right behaviour: MJPEG has an entirely
different bitrate profile (no inter-frame prediction at all, so it scales *linearly* with frame
rate), and silently applying an H.264 model to it would be wrong by a large factor with no
warning.

---

## Derivation 3 — Peak and average

```
   ┌────────────────────────────────────────────────┐
   │   peak     =  count × bitrate                  │
   │   average  =  count × bitrate × duty_cycle     │
   └────────────────────────────────────────────────┘
```

### 🧮 Worked example 3.3 — the test case

A car park group: 10 cameras, 6 Mbps each, motion duty cycle 0.25.

```
   peak    = 10 × 6.0        =  60.0 Mbps
   average = 10 × 6.0 × 0.25 =  15.0 Mbps
```

This is `test_camera_group_peak_vs_average`.

### Which one do you use?

**This is the load-bearing distinction in the lesson.**

| Sizing... | Use | Why |
|---|---|---|
| **Network links, switch uplinks, WAN circuits** | **PEAK** | See below |
| **Storage** | **average** (via effective hours) | Storage integrates over time; the average *is* the consumption |

**Why links are sized on peak, and why the statistics don't save you:**

The tempting argument is that with 80 cameras, motion events will be spread out, so the aggregate
will hover near the average with occasional excursions — size for average plus a margin and let
statistics do the rest.

**That argument fails because motion events are correlated, not independent.** A car driving
through a lot triggers six cameras in sequence. A fire alarm sends everyone into the corridors at
once. A crowd leaving at 5 p.m. lights up every camera on the egress path. **The moments when many
cameras go to full bitrate simultaneously are exactly the moments something is happening** — which
is exactly when you need the video to arrive.

A link sized on average bandwidth works beautifully at 3 a.m. and drops frames during the
incident. The video you lose is the video the entire system exists to capture.

> 🧠 **State it to clients this way:** *"The network has to carry the worst minute of the year, not
> the average minute. The average minute is when nothing is happening."*

---

## The motion duty cycle is a risk, not a saving

`motion_duty_cycle` models motion-triggered or motion-boosted recording: the fraction of the day a
camera records at full bitrate. `1.0` is continuous recording.

**Anything below 1.0 is an assumption about the future that you should name explicitly to the
client**, because:

- **Motion recording that misses the event is worthless.** All the storage saved is saved on
  footage nobody wanted, and the one clip that mattered isn't there.
- **Poorly tuned motion detection misses events routinely.** A subject moving slowly, entering at
  the frame edge, or wearing low-contrast clothing against the background can fail to trigger.
- **Duty cycle is not measurable at design time.** You are predicting how much motion a scene will
  have over the next five years. A quiet corridor becomes a construction route; a car park gets a
  new footpath through it.
- **It degrades silently.** If real duty turns out to be 0.6 instead of 0.25, storage runs out
  early and retention drops. Nobody gets an alert.

The calculator validates `0 < duty ≤ 1` and rejects both endpoints of nonsense
(`test_motion_duty_cycle_validated`): a duty of 0 means the camera never records, which is not a
configuration, it's an error.

> **The recommendation:** use continuous recording as the default and treat motion-based reduction
> as a deliberate, documented trade with the client's acceptance — the same posture lesson 04 takes
> toward retention. If the budget only closes with a duty cycle assumption, that is a finding to
> report, not a lever to pull quietly.

---

## Aggregation

A `VideoSystem` sums its groups:

```
   system peak    = Σ group peak
   system average = Σ group average
```

### 🧮 Worked example 3.4 — the test case

50 indoor cameras at 6 Mbps, 30 outdoor at 10 Mbps, all continuous:

```
   indoor peak  = 50 × 6.0  = 300 Mbps
   outdoor peak = 30 × 10.0 = 300 Mbps
   system peak  =             600 Mbps
   camera count =              80
```

This is `test_system_totals`.

**Now do the engineering that the number is for:**

- **600 Mbps aggregate** on a 1 Gbps uplink is 60% utilization at peak. That is workable but has
  no room for growth, and it shares the link with everything else on it.
- **If those 80 cameras are spread across four access switches**, each switch's uplink carries
  roughly 150 Mbps — comfortable on 1 Gbps.
- **If the recording server is on the far side of one uplink**, that uplink carries the whole
  600 Mbps and 1 Gbps is too tight. This is where the design either gets a 10 Gbps link to the
  recorder, or the recorders get distributed.
- **Add client viewing traffic**, which is *additional* — every operator workstation pulling live
  views re-streams from the recorder. Ten operators watching a 16-up wall is not free.

> ⚠️ **The mistake this catches:** computing 600 Mbps, noting it's under 1 Gbps, and stopping.
> Aggregate bandwidth is not a single number the network has to satisfy — it is a load with a
> *topology*. Where the cameras are relative to where the recorder is determines which links carry
> what. See [`../08_Networking/`](../08_Networking/).

---

## Assumptions and limits

| Assumption | Reality |
|---|---|
| A single bitrate per camera | Real VBR streams vary continuously with scene content |
| Frame rate scales as `ratio^0.7` | A curve fit, `[PRACTICE]`, not a codec property |
| H.265 is exactly 0.5× H.264 | 0.4–0.6 in practice, model-dependent |
| Smart codec is 0.5× | **0.2–0.8**, the widest uncertainty here |
| Duty cycle is knowable | It is a prediction about future scene activity |
| Motion events are what triggers recording | Tuning quality varies enormously |
| Peak = everything at once | Correct for sizing; conservative by design |

**Everything here compounds.** Three factors each uncertain by ±30% do not give you a result
uncertain by ±30%. This is why lesson 04 presents storage as a **range** rather than a value, and
why that is an honesty requirement rather than a stylistic preference.

---

## Common mistakes

⚠️ **Scaling bitrate linearly with frame rate.** Under-estimates by 19% at half rate.

⚠️ **Scaling bitrate linearly with resolution.** 4× the pixels is roughly 3× the bitrate.

⚠️ **Sizing network links on average bandwidth.** Works at 3 a.m., fails during the incident.

⚠️ **Booking a smart-codec saving without a pilot measurement.**

⚠️ **Treating a duty cycle as a saving rather than an assumption.**

⚠️ **Quoting a vendor calculator's output without knowing its assumptions.**

⚠️ **Reporting a single bandwidth number without saying where the bitrate came from.**

⚠️ **Forgetting client viewing traffic**, which is additional to camera-to-recorder traffic.

---

## Junior vs. Senior

**Junior:** applies the frame-rate and codec models correctly; distinguishes peak from average and
uses peak for links; knows the bitrate table is a starting point.

**Senior:** states the provenance of every bitrate figure in the design narrative; refuses to book
a smart-codec saving without a pilot; treats duty cycle as a client-facing risk rather than a
budget lever; reasons about aggregate bandwidth as a topology problem rather than a single number;
and knows that when a design only closes because of a frame-rate reduction, the right move is to
measure rather than to trust the exponent.

---

## Problem set

**P3.1** A 4 MP camera streams 10 Mbps H.264 at 30 fps.
- (a) Compute the bitrate at 20 fps, at 15 fps, and at 10 fps using the model.
- (b) Compute what a linear model would give for each.
- (c) A colleague proposes going to 15 fps to "halve the storage." Correct them with a number.

**P3.2** Compute the bitrate for a 4 MP camera at 15 fps using H.265. Then compute it again
assuming the smart codec delivers 0.8 rather than 0.5. State the ratio between your two answers
and say what that implies for how you present the figure.

**P3.3** A system has three groups:
- 40 indoor 2 MP cameras, 6 Mbps, continuous
- 24 outdoor 4 MP cameras, 10 Mbps, continuous
- 16 car park 4 MP cameras, 10 Mbps, motion duty cycle 0.30

Compute the system peak and average bandwidth, and the camera count.

**P3.4** Using P3.3's system: the 40 indoor cameras are on two access switches, the 24 outdoor on
one, and the 16 car park on one. All four switches uplink to a core switch, and the recording
server hangs off the core. Compute the load on each access uplink and on the server's link. State
which links you would specify at 1 Gbps and which at 10 Gbps, and why.

**P3.5** Explain, in under 150 words to a network manager who wants to size the camera VLAN on
average bandwidth, why that will work perfectly until it matters.

**P3.6** The frame-rate exponent is 0.7. Suppose you measured a real camera and found the true
figure was closer to 0.85. For a 200-camera system at 15 fps whose storage was sized with 0.7, by
what percentage would the storage estimate be wrong, and in which direction? Show the reasoning.

**P3.7** `test_unsupported_codec_raises` rejects MJPEG rather than defaulting to H.264. Explain why
silently defaulting would be a worse bug than raising, and describe what would go wrong in a real
design. What would you need to add to the module to support MJPEG properly?

> Answers: [`_solutions/03_bandwidth_solutions.md`](_solutions/03_bandwidth_solutions.md)

---

## Retrieval check

1. Rank the four sources of a bitrate figure.
2. Write the frame-rate scaling model and give the two mechanisms that make it sub-linear.
3. By how much does a linear model under-estimate at half frame rate?
4. Write the composed formula for frame rate + codec + smart codec.
5. Why are network links sized on peak while storage is sized on average?
6. Why doesn't statistical smoothing save an under-sized link?
7. What is a motion duty cycle actually assuming, and why is it a risk rather than a saving?
8. Why does the module reject MJPEG instead of defaulting?

---

## References

- [`../28_Calculators/psec/video.py`](../28_Calculators/psec/video.py) — the implementation.
- [`../28_Calculators/tests/test_psec.py`](../28_Calculators/tests/test_psec.py) — `TestVideo`.
- Camera manufacturer datasheets and bitrate tables. `[MFR]`
- [`../08_Networking/`](../08_Networking/) — topology, VLANs, QoS, and multicast *(not yet
  written)*.
- [`../03_Video_Surveillance/`](../03_Video_Surveillance/) — application *(not yet written)*.

**Next:** [04 — Storage and Retention](04_storage.md)
