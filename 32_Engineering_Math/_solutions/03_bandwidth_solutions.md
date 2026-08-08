# Solutions — 03 Video Bandwidth

---

## P3.1 — Frame rate scaling, 10 Mbps at 30 fps

**(a) and (b)**

| Target | ratio^0.7 | **Model** | Linear model | Model ÷ Linear |
|---|---|---|---|---|
| 20 fps | 0.75290 | **7.529 Mbps** | 6.667 Mbps | 1.129 |
| 15 fps | 0.61557 | **6.156 Mbps** | 5.000 Mbps | 1.231 |
| 10 fps | 0.46346 | **4.635 Mbps** | 3.333 Mbps | 1.390 |

**(c) Correcting the colleague**

> Going from 30 to 15 fps cuts the bitrate by about **38%**, not 50%. The model gives 6.16 Mbps,
> not 5.0.
>
> The reason it isn't half: at 15 fps consecutive frames are twice as far apart in time, so
> they're less similar, so the inter-frame compression that does most of the work gets less
> efficient. And the keyframes and stream overhead don't scale at all.
>
> So if we're 50% over on storage, halving the frame rate doesn't close the gap — it gets us
> about three quarters of the way, and it costs us motion smoothness in every clip we ever review.

**Why this correction matters in dollars:** on a system sized at 200 TB, booking a 50% saving when
the real saving is 38% leaves you **24 TB short**. That doesn't manifest as an error. It manifests
as retention silently dropping from 30 days to about 26, discovered the first time someone asks
for day-28 video.

---

## P3.2 — Smart codec uncertainty

**H.265 at 15 fps, from a 10 Mbps H.264/30 fps base:**

```
   fps factor    = (15/30)^0.7 = 0.61557
   codec factor  = 0.5
   rate          = 10.0 × 0.61557 × 0.5 = 3.078 Mbps
```

**With the smart codec:**

| Smart factor | Bitrate |
|---|---|
| 0.5 (the module default) | **1.539 Mbps** |
| 0.8 (pessimistic end of the documented range) | **2.462 Mbps** |

**Ratio: 1.60.**

**What that implies for presentation:**

A 60% spread between two defensible values of a single assumption means **the figure cannot be
presented as a number.** Presenting "1.54 Mbps per camera" implies three significant figures of
confidence in a parameter whose documented range is 0.2–0.8 — a factor of four.

Present it as a **range with the assumption stated**:

> Per-camera bitrate: **1.5–2.5 Mbps** (H.265, 15 fps, smart codec). The lower figure assumes the
> smart codec achieves a 50% reduction; the upper assumes 80%. Actual performance is highly
> scene-dependent — static interior scenes trend toward the lower figure, and scenes with moving
> foliage, weather, or headlights toward the upper. **Recommend a 24-hour pilot measurement on two
> representative cameras before committing storage.**

That paragraph costs nothing and it is the difference between an estimate and a promise.

---

## P3.3 — System totals

| Group | Count | Mbps each | Duty | Peak | Average |
|---|---|---|---|---|---|
| Indoor 2 MP | 40 | 6.0 | 1.0 | 240.0 | 240.0 |
| Outdoor 4 MP | 24 | 10.0 | 1.0 | 240.0 | 240.0 |
| Car park 4 MP | 16 | 10.0 | 0.30 | 160.0 | 48.0 |
| **System** | **80** | | | **640.0 Mbps** | **528.0 Mbps** |

Note the car park group: peak 160 Mbps, average 48 Mbps. **The duty cycle changes the average by
112 Mbps and changes the peak by nothing** — which is the whole reason the two numbers exist
separately.

---

## P3.4 — Link sizing by topology

```
                            ┌──────────────┐
                            │ RECORDING    │  ← 640 Mbps peak
                            │ SERVER       │
                            └──────┬───────┘
                                   │  server link
                            ┌──────┴───────┐
                            │  CORE SWITCH │
                            └──┬──┬──┬──┬──┘
                   ┌───────────┘  │  │  └───────────┐
              ┌────┴────┐  ┌──────┴┐ ┌┴──────┐ ┌────┴────┐
              │ SW-A    │  │ SW-B  │ │ SW-C  │ │ SW-D    │
              │ indoor  │  │indoor │ │outdoor│ │ car park│
              │ 20 cams │  │20 cams│ │24 cams│ │ 16 cams │
              └─────────┘  └───────┘ └───────┘ └─────────┘
                120 Mbps    120 Mbps  240 Mbps    160 Mbps
```

| Link | Peak load | Specify | Reasoning |
|---|---|---|---|
| SW-A uplink | 20 × 6 = **120 Mbps** | **1 Gbps** | 12% utilization. Ample. |
| SW-B uplink | 20 × 6 = **120 Mbps** | **1 Gbps** | Same. |
| SW-C uplink | 24 × 10 = **240 Mbps** | **1 Gbps** | 24% utilization. Comfortable. |
| SW-D uplink | 16 × 10 = **160 Mbps** | **1 Gbps** | Peak, not the 48 Mbps average. 16% utilization. |
| **Server link** | **640 Mbps** | **10 Gbps** | See below |

**Why the server link is 10 Gbps and not 1 Gbps:**

640 Mbps on a 1 Gbps link is **64% utilization at peak, before anything else.** Three problems:

1. **No growth headroom.** Adding eight more 4 MP cameras puts it at 72%. The system is one small
   expansion from a redesign.
2. **Client viewing traffic is additional.** Every operator workstation pulling live views
   re-streams from the server. Ten operators on a 16-up wall is easily another 300–500 Mbps
   depending on whether sub-streams are used — which would put the link over.
3. **A single congested link loses frames from every camera at once**, and it does so precisely
   during correlated-motion events, which is when the video matters. See P3.5.

**The car park uplink is the one worth calling out**, because it's the trap in the problem: its
*average* is 48 Mbps and its *peak* is 160 Mbps. Sized on average with a generous 2× margin
(96 Mbps) it still fails during a correlated event. Size links on peak.

---

## P3.5 — To a network manager who wants to size on average

Model answer (142 words):

> The average is real, but it's the wrong statistic for a link.
>
> Camera motion isn't independent — it's correlated. A car crossing the lot triggers six cameras
> in sequence. A fire alarm puts everyone in the corridors at once. Shift change lights up every
> camera on the egress path. The moments when most cameras jump to full bitrate simultaneously are
> exactly the moments something is happening.
>
> So a link sized on average works perfectly at three in the morning and drops frames during the
> incident. And the frames it drops are the ones the whole system exists to capture. There's no
> alarm for it — you find out weeks later when the clip has gaps.
>
> Our peak is 640 Mbps. On a 1 Gig link that's 64% before any operator opens a viewing client.
> I'd like 10 Gig to the recorder, and 1 Gig is genuinely fine everywhere else.

**What makes it work:** it concedes the manager's point is statistically reasonable and then
supplies the missing fact (correlation), rather than asserting a rule. It names the failure mode
in operational terms — silent, discovered late — and it closes by *agreeing* with them about four
of the five links, which makes the one disagreement easy to accept.

---

## P3.6 — If the true exponent were 0.85

```
   At 15 fps, ratio = 0.5

   Model in use (0.7):   0.5^0.70  =  0.61557
   True behaviour (0.85): 0.5^0.85 =  0.55478

   Ratio (true / model) = 0.55478 / 0.61557 = 0.90125
```

**The storage estimate would be too LARGE by about 11%.**

```
   model / true = 1 / 0.90125 = 1.1096  →  +11.0%
```

**The direction matters more than the magnitude, and it is the safe one.**

A *higher* exponent means the curve is *closer to linear* — less sub-linear, so frame rate
reduction saves more than the 0.7 model predicts. Sizing with 0.7 therefore over-provisions.

| If the true exponent is... | The 0.7 model... | Consequence |
|---|---|---|
| **> 0.7** (e.g. 0.85) | over-estimates bitrate | Storage is over-provisioned. Costs money; nothing breaks. |
| **< 0.7** (e.g. 0.55) | **under**-estimates bitrate | Storage runs short; retention silently drops. |

> 🧠 **The habit worth taking from this problem: when you inherit a modelling constant, work out
> which direction its error runs and whether that direction is safe.** A parameter whose error
> costs money is a different risk from one whose error costs evidence. Here, 0.7 sits on the
> conservative side of the plausible range for most encoders, which is a defensible place for a
> default to sit — and that is worth knowing rather than assuming.
>
> On a 200-camera system, 11% of over-provisioning is real money, so if frame-rate reduction is
> load-bearing in the budget, **measure it**. The model is for estimating, not for a decision with
> no margin.

---

## P3.7 — Why rejecting MJPEG beats defaulting to H.264

**Why silently defaulting is the worse bug:**

MJPEG has **no inter-frame prediction at all.** Every frame is an independent JPEG. That single
difference breaks both models in the module:

1. **Frame rate scaling is LINEAR for MJPEG**, not `ratio^0.7`. Half the frames is exactly half
   the bits, because there is no inter-frame efficiency to lose. Applying `^0.7` over-estimates
   MJPEG bitrate at reduced frame rates — by 23% at 15 fps.
2. **The base bitrate is far higher** — MJPEG typically runs several times the bitrate of H.264
   for comparable quality, because it discards all temporal redundancy.

So a silent default would produce a number that is **badly wrong in both terms, with no warning
anywhere in the output.** The user gets a plausible-looking figure, sizes storage from it, and
discovers the error when the array fills in a fraction of the expected time.

**What goes wrong in a real design:** MJPEG still appears on older cameras, on some intercom and
elevator systems, and wherever a client has legacy equipment being integrated. Somebody enters
`codec="mjpeg"` because that is what the device does, gets a number, and sizes a retrofit storage
expansion from it. The failure surfaces months later as a retention shortfall on exactly the
legacy cameras nobody wanted to touch.

**Raising is right** because the caller has expressed an intent the module cannot honour. The two
honest responses to that are "here is the answer" and "I can't answer that" — and quietly
answering a different question is neither.

**What supporting MJPEG properly would require:**

1. A **codec model flag** distinguishing inter-frame codecs (H.264, H.265) from intra-frame ones
   (MJPEG), because the frame-rate exponent depends on it: `1.0` for intra-frame, `0.7` for
   inter-frame.
2. A **separate reference bitrate table** for MJPEG. The `TYPICAL_H264_MBPS` figures are
   meaningless as a base.
3. A **test** pinning linear frame-rate scaling for MJPEG — the mirror of
   `test_frame_rate_scaling_is_sublinear`, asserting that half the frame rate gives half the
   bitrate to within floating point.
4. A note in the docstring that MJPEG's storage profile makes it unsuitable for anything but short
   retention, so nobody discovers that from the arithmetic alone.

That is a small change and it is not currently worth making, because MJPEG should be designed out
rather than designed around. **The raise is the correct behaviour precisely because it forces that
conversation** instead of hiding it inside a plausible number.
