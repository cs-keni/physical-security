# 06 — Compression, Bitrate, and Bandwidth

> **Prerequisite:** [`../32_Engineering_Math/03_bandwidth.md`](../32_Engineering_Math/03_bandwidth.md).
> That lesson derives the bitrate arithmetic, frame-rate and codec scaling, and the peak-versus-average
> distinction. **This lesson does not re-derive it.**
>
> This lesson answers the question the arithmetic cannot: **where does the input number come from,
> why do two vendors give you two of them, and what do you put in the specification?**
>
> Link **[5]** and **[6]** of [the imaging chain](01_imaging_chain.md).

## Learning objectives

- Explain what a video codec actually does, at the level needed to predict its behaviour.
- State why scene content drives bitrate more than resolution does.
- Choose between CBR, VBR, and capped VBR, and say what each protects.
- Describe what smart codecs do and name the case where they destroy the evidence.
- Present a bandwidth figure as a **defensible range** with the assumptions attached.
- Size an uplink on **peak**, and explain why averaging is the wrong tool.

---

## What a codec does, briefly

Video compression exploits two redundancies:

- **Spatial** (within one frame) — neighbouring pixels are similar, and the eye is less sensitive
  to fine colour detail than to brightness. This is roughly what JPEG does.
- **Temporal** (between frames) — most of frame `n+1` looks like frame `n`. Rather than resending
  it, encode the *difference*.

Temporal redundancy is where nearly all the compression comes from, and it is the entire reason
scene content dominates bitrate.

**Frame types:**

```
I P P P P P P P P P P P I P P P P P P P P P P P I
└─────── one GOP ───────┘

I-frame  complete, standalone image. Large. The only frame decodable alone.
P-frame  "predicted" — encodes only the change from the previous frame. Small.
B-frame  "bi-directional" — references frames before AND after. Smallest.
         Adds latency, so it is often avoided in live surveillance.
```

**GOP length** (Group of Pictures) is the spacing between I-frames. Long GOP means fewer big
frames and lower bitrate; it also means **more damage from a lost packet** (errors propagate until
the next I-frame) and coarser seeking in playback.

> ⚠️ **The GOP trap in evidence.** With a 4-second GOP, exporting a 2-second clip actually requires
> the surrounding GOP, and some systems will export more than you asked for or re-encode to trim —
> which is an evidentiary problem, not just an inconvenience. Very long GOPs also mean that a
> corrupted stream stays corrupted for seconds at a time. Keep GOPs modest on
> evidence-critical cameras. `[PRACTICE]`

**Codec generations** `[PRACTICE]` — treat the figures as rough:

| Codec | Relative bitrate for similar quality | Notes |
|---|---|---|
| MJPEG | ~10× H.264 | No temporal compression at all. Every frame is a full JPEG. Still found on legacy and on some analytics feeds |
| H.264 | 1.0× (baseline) | Universal. The safe default for compatibility |
| H.265 (HEVC) | ~0.5–0.6× | Roughly half the bitrate for similar quality. **Licensing and decode load are the constraints** |
| H.266 / AV1 | lower again | Limited surveillance support as of writing `[VERIFY]` |

⚠️ **H.265 is not free.** It costs substantially more CPU/GPU to decode, so a workstation that
displayed 32 H.264 streams may manage far fewer in H.265 without hardware acceleration. And VMS,
analytics, and export-to-third-party support vary. `[MFR][VERIFY]` Halving the bandwidth and
halving the number of cameras an operator can watch is not a win.

---

## Why scene content beats resolution

Temporal compression encodes *change*. So bitrate is driven by **how much the scene changes
between frames**, which is a property of the scene, not the camera.

| Scene | Why its bitrate lands where it does |
|---|---|
| Server room, no windows, nobody present | Almost nothing changes. Very low, very stable |
| Interior corridor, artificial light | Empty most of the time; predictable when occupied. Low, narrow band |
| Office lobby with glass | Sunlight moves, reflections shift, people cross. Moderate, wide band |
| Car park with trees | **Every leaf moves.** Rain, snow, headlights, sun/shade transitions. High and wildly variable |
| Loading dock | Vehicles, doors, weather, high-contrast transitions. High |

**A 2 MP camera on a windy car park can out-consume a 4 MP camera in a corridor.** This is why a
"Mbps per megapixel" rule of thumb is wrong in a way that matters, and why vendor calculators —
which mostly key off resolution, frame rate, and a coarse "scene activity" dropdown — disagree
with each other by 2× or more.

> 🧠 **The professional consequence.** When two calculators disagree, neither is lying; they are
> assuming different scenes. The correct response is not to pick one, and definitely not to
> average them. It is to **state your own assumption explicitly and present a range** — which is
> what the rest of this lesson builds.

Other real drivers: **noise** (a noisy night image looks like change to the encoder, so bitrate can
*rise* at night — the opposite of the intuition that dark scenes are cheap), **IR illumination**
(monochrome helps, but IR noise hurts), and **rain or snow** (each drop is motion).

---

## Rate control: CBR, VBR, and capped VBR

| Mode | Behaviour | Protects | Costs |
|---|---|---|---|
| **CBR** | Fixed bitrate, quality varies | **Predictable network and storage** | Quality collapses exactly when the scene gets busy — i.e. during the incident |
| **VBR** | Fixed quality, bitrate varies | **Consistent image quality** | Unpredictable peaks; storage and network planning become guesswork |
| **Capped VBR (MBR)** | VBR with a ceiling | Quality most of the time, bounded worst case | Quality still degrades at the cap, but only there |

⚠️ **CBR's failure mode deserves emphasis** because it is counter-intuitive and it bites during
exactly the moment the system exists for. Under CBR, a quiet corridor wastes bits on nothing; then
six people run through and the encoder must hold the same bitrate, so it degrades quality —
blocking, smearing — **at the instant the footage matters.** A system that looks fine on every
routine day is at its worst during the incident.

> 🧠 **Capped VBR is the right default for most surveillance.** It gives VBR's quality behaviour
> with a bound you can plan against. Set the cap from your peak calculation, not from a guess, and
> record what the cap is — a camera silently sitting at its cap during every busy period is a
> finding, and nobody checks for it unless the cap is documented.

## Smart codecs

Every major manufacturer ships a "smart" codec under its own name `[MFR]`. They work by some
combination of: dynamic GOP length, lowering quality in static regions, lowering quality in regions
judged uninteresting, and dropping frame rate when nothing moves. Savings are real — commonly
30–70% `[PRACTICE][VERIFY]` — and they are highly scene-dependent, which is exactly the problem
when you are trying to produce a defensible number.

⚠️ **The failure that matters.** Some implementations preserve bits in *static* regions and reduce
quality on *moving* regions — precisely inverting what evidence requires. Others aggressively
degrade anything the algorithm scores as background, which can include a person standing still. A
system saving 60% and delivering a blocky, smeared face on the one subject you needed has made a
bad trade on your behalf, invisibly.

**How to handle them professionally:**

1. **Test before you trust.** Record a walking subject with the smart codec on and off, export
   both, and compare the face. This is a one-hour test that settles it.
2. **Do not bank the saving in the design.** Size storage and bandwidth without the smart codec, or
   with a conservative fraction of the claimed saving. If it delivers more, you have headroom. If
   you sized on 60% and get 20% on a windy car park, you are short and it is your number that was
   wrong.
3. **Turn them down on evidence-critical cameras.** The vestibule identify camera is not where you
   economise.

---

## 🧮 Worked example 6.1 — Meridian Building 2, the honest range

**The system** (fictional; carried forward into
[lesson 07](07_storage_and_retention.md), [08](08_vms_architecture.md), and
[09](09_camera_placement.md)): 31 cameras, 30-day retention, continuous recording.

The **low / nominal / high** bands below are set **per scene type**, not as a uniform multiplier.
That is the entire point — a server room has a narrow band and a car park an enormous one.
`[PRACTICE]`

| Group | Count | Low | Nominal | High | Why the band is that wide |
|---|---|---|---|---|---|
| Vestibule identify | 2 | 3.5 | 6.0 | 11.0 | Busy, detailed, glass behind |
| Lobby / atrium overview | 3 | 2.5 | 5.0 | 11.0 | Moving sunlight, reflections |
| Corridors (4 floors) | 16 | 2.0 | 3.0 | 4.5 | **Narrow** — empty and predictable |
| Loading dock | 2 | 3.0 | 6.0 | 13.0 | Vehicles, doors, weather |
| Car park | 6 | 2.5 | 5.0 | 12.5 | **Widest** — trees, rain, headlights |
| Server room | 2 | 0.8 | 2.0 | 3.0 | **Narrowest** — nothing changes |

Aggregated with [`../28_Calculators/psec/video.py`](../28_Calculators/psec/video.py):

| Case | Peak bandwidth | 30-day storage (decimal) | (binary) |
|---|---|---|---|
| Low | 69.1 Mbps | 22.39 TB | 20.36 TiB |
| **Nominal** | **121.0 Mbps** | **39.20 TB** | **35.66 TiB** |
| High | 234.0 Mbps | 75.82 TB | 68.95 TiB |

**The spread is 3.39×, in both bandwidth and storage.** They move together because storage is
bitrate integrated over time — one input, two outputs.

**Note peak equals average here**, because every group records continuously (duty cycle 1.0). That
is a design decision, not a fact of nature; see the duty-cycle section below.

### What actually goes in the specification

Not the nominal figure alone. This:

> **Video bandwidth and storage — basis of estimate.**
> Estimated aggregate peak bandwidth: **121 Mbps nominal**, within a range of **69 to 234 Mbps**
> depending on scene complexity, weather, and night-time noise. Estimated 30-day storage:
> **39.2 TB nominal**, range **22.4 to 75.8 TB**.
> **Assumptions:** H.264, continuous recording, 30-day retention, per-camera bitrates as
> scheduled, **no smart-codec saving assumed**. Car park and loading dock figures carry the widest
> uncertainty (weather and vegetation).
> **Design provision:** storage and switching provisioned at **nominal + 20% headroom**
> (**47.0 TB**, **145.2 Mbps**), with the storage architecture able to expand to the high case
> without replacing the chassis.
> **Verification:** bitrates to be measured per camera group during the first 30 days and the
> provision reviewed against measurement.

Four things that paragraph does, all of which matter:

1. **Gives a number to build to.** Owners cannot act on "it depends."
2. **States the range**, so nobody is surprised later and the eventual outcome is inside what you
   said.
3. **Names the assumptions**, so a reviewer can challenge the input rather than the output — and so
   *you* can point to the assumption when the car park turns out to be worse.
4. **Commits to measuring**, which converts an estimate into a number within a month and is the
   single most professional element of the whole statement.

> 🧠 **This is the deliverable that most distinguishes an engineer from a quoter.** A quoter gives
> one number. An engineer gives a number, its range, its assumptions, and the plan to replace the
> estimate with a measurement.

---

## Peak versus average, and why averaging is dangerous

Size network links on **peak**, always.

The tempting argument is that not every camera peaks at once, so the aggregate should smooth out
statistically. **It does not, because motion events correlate.** A vehicle entering the car park
triggers six cameras. A shift change fills every corridor simultaneously. A storm makes every
exterior camera busy at the same instant. The moment of maximum load is the moment of maximum
interest, and it is the moment your averaged link saturates.

For Meridian at nominal + 20% headroom (**145.2 Mbps**):

| Link | Utilisation by video |
|---|---|
| 1 GbE | **14.5%** |
| 10 GbE | 1.5% |

14.5% of a gigabit sounds comfortable, and for this building it is. Note what the figure does *not*
account for: other traffic on shared links, live viewing (each viewed stream is an **additional**
copy from the recorder or camera), export traffic, and analytics streams. **Recording bandwidth is
not total bandwidth.**

⚠️ **Live viewing is the load people forget.** Sixteen operators each watching sixteen streams is a
very different link requirement from recording alone — and it is concentrated on the recorder's
network port, not spread across the camera VLAN.

**Multicast** can help where many clients watch the same stream, by sending one copy the network
replicates. It requires switch and network configuration (IGMP snooping, a querier) that must be
designed and is frequently misconfigured. `[VERIFY]` Treated properly in
[`../08_Networking/`](../08_Networking/) *(not yet written)*.

## The motion duty cycle: the tempting saving

Recording only on motion is the most common way to make a storage number smaller. `psec` models it
as `motion_duty_cycle`. For Meridian:

| Duty cycle | 30-day storage | Peak bandwidth | Average bandwidth |
|---|---|---|---|
| 100% (continuous) | 39.20 TB | 121.0 Mbps | 121.0 Mbps |
| 50% | 19.60 TB | **121.0 Mbps** | 60.5 Mbps |
| 30% | 11.76 TB | **121.0 Mbps** | 36.3 Mbps |

Two things to read from this table:

1. **Storage scales linearly with duty cycle.** Halve the recording, halve the disk. Genuinely
   attractive.
2. **Peak bandwidth does not change at all.** When motion triggers, the camera streams at full
   rate. Sizing a network on the *average* of a motion-recorded system is exactly the error the
   previous section warns about, and motion recording makes it more tempting because the average
   looks so much better.

⚠️ **The real risk is not bandwidth, it is missed evidence.** Motion detection that misses the
event produces a recording of an empty corridor before and after, and nothing during — which is
worse than no system, because everyone believed it was recording. Pre- and post-event buffers help
and do not eliminate it. Poorly tuned motion detection misses events routinely: a subject moving
slowly, a subject at the frame edge, a scene where the detector was desensitised to stop rain
triggering it.

> 🧠 **Where motion recording is defensible:** low-risk zones, as a *supplement* to continuous
> recording on critical cameras, or where retention requirements cannot otherwise be met and the
> alternative is a shorter retention period. **Name the risk explicitly to the client and get it
> acknowledged** — `psec`'s own docstring says the same thing, which is not an accident. Never
> apply it to an identification camera at a chokepoint.

## Design tradeoffs

| Decision | Buys | Costs |
|---|---|---|
| H.265 over H.264 | ~40–50% bitrate | Decode load, compatibility, licensing |
| Longer GOP | Lower bitrate | Error propagation; coarse export; evidentiary awkwardness |
| CBR | Predictable planning | **Quality collapse during the incident** |
| VBR | Consistent quality | Unpredictable peaks |
| Capped VBR | Both, bounded | Needs a considered cap, and monitoring against it |
| Smart codec | 30–70% claimed | Scene-dependent; may degrade moving subjects; unverifiable in design |
| Lower frame rate | Bitrate, linearly-ish | Motion continuity; harder to follow fast events |
| Motion recording | Storage, linearly | **Missed events**; no peak-bandwidth saving |
| More headroom | Survives being wrong | Capital cost |

**On frame rate:** 15 fps is adequate for most surveillance and halves the data against 30 fps
`[PRACTICE]`. It is a legitimate and underused saving. But it is **not** a substitute for shutter
speed — a 15 fps stream with a 1/125 s shutter has sharp frames spaced further apart, while
30 fps at 1/30 s has smeared frames close together. [Lesson 03](03_sensors_and_low_light.md)
governs sharpness; frame rate governs continuity. **They are independent settings and confusing
them is common.**

## Common mistakes

⚠️ **Quoting a single bitrate figure with no assumptions.** It will be wrong, and there will be
nothing to point at.

⚠️ **Averaging two vendor calculators.** They assume different scenes; the mean of two guesses is a
third guess.

⚠️ **Sizing links on average bandwidth.** Motion correlates. Size on peak.

⚠️ **Banking the smart-codec saving in the design.** Test it, then decide; never assume it.

⚠️ **Using CBR on evidence-critical cameras.** Quality degrades exactly when the scene gets busy.

⚠️ **Assuming night is cheap.** Sensor noise looks like change, so bitrate often *rises* at night.

⚠️ **Forgetting live viewing and export in the network budget.** Recording bandwidth is not total
bandwidth.

⚠️ **Applying motion recording to identification cameras.** The event you miss is the one that
mattered.

⚠️ **Confusing frame rate with shutter speed.** Independent settings; only one of them fixes blur.

## Junior vs. Senior

| | Junior | Senior |
|---|---|---|
| Produces a bandwidth figure by | Running a vendor calculator | Estimating per scene type, then stating a range and its assumptions |
| Handles two disagreeing calculators by | Picking the lower one | Explaining that they assume different scenes, and stating their own |
| Sizes uplinks on | Average | **Peak**, plus live viewing and export |
| Treats smart codecs as | A saving to design around | A saving to verify, and to disable on evidence cameras |
| Chooses rate control by | The default | Capped VBR, with the cap derived and documented |
| Presents storage as | A number | A number, a range, the assumptions, and a commitment to measure |
| Assumes night bitrate | Falls | May **rise**, because noise looks like motion |

## 🔧 Field exercise

1. On a live system, find the configured bitrate, codec, GOP, and rate-control mode for three
   cameras in genuinely different scenes (a corridor, an exterior, a busy entrance).
2. Record the **actual** bitrate each is achieving over a full day, including overnight. Compare
   the exterior camera's day and night figures — note whether night is higher.
3. Compute the aggregate peak for the system and compare it to the uplink capacity.
4. If a smart codec is enabled, record a walking subject with it on and off. Export both and
   compare the face at full zoom.

## Exercises

Work these before opening
[`_solutions/06_compression_and_bandwidth_solutions.md`](_solutions/06_compression_and_bandwidth_solutions.md).

**E6.1** A vendor calculator returns 4.2 Mbps for a 4 MP camera at 15 fps. A second returns
9.1 Mbps for the same specification.
 (a) Give two specific assumptions that could account for the difference.
 (b) State what you would write in the basis of design.
 (c) The client asks "so which is right?" Answer in three sentences.

**E6.2** Meridian's car park group (6 cameras) is re-estimated after a site visit reveals mature
deciduous trees along two sides and no lighting control — the lot is lit by street lighting that
casts moving shadows.
 (a) Which of the low / nominal / high figures should now be treated as the working estimate, and
     why?
 (b) Recompute the system peak and 30-day storage using the high figure for the car park group
     only, all other groups nominal.
 (c) State the effect on the +20% headroom provision.

**E6.3** A design uses CBR at 4 Mbps on all cameras "so the numbers are predictable."
 (a) State the one scenario where this decision causes the most harm.
 (b) Give the recommendation and the reason.
 (c) The client's IT department insists on predictable bandwidth for capacity planning. Propose a
     resolution that satisfies both.

**E6.4** A 200-camera system is proposed with motion recording at a 30% duty cycle to fit a
retention requirement into existing storage.
 (a) By what factor does storage fall?
 (b) By what factor does peak bandwidth fall?
 (c) Name the risk in one sentence and write the two-sentence disclosure you would send.
 (d) Name two cameras in such a system where you would refuse to apply it, and why.

**E6.5** 🧠 A client's existing 60-camera system was sized at a flat 3 Mbps per camera. Measured
over a month, the **40** interior corridor cameras average **2.2 Mbps** and the **20** exterior
cameras average **9.8 Mbps**. Retention was specified at 30 days and the array is full at day 19.
 (a) Work out roughly why, showing your reasoning.
 (b) Give three options to reach 30 days, with what each costs.
 (c) Which do you recommend, and what do you tell the client about how the original number was
     produced?

## Retrieval check

1. Which redundancy provides most of the compression, and what follows from that?
2. Why can a 2 MP car park camera use more bandwidth than a 4 MP corridor camera?
3. What does CBR protect, and when does it fail?
4. What is the default rate-control recommendation and why?
5. Why should links be sized on peak rather than average?
6. Does motion recording reduce peak bandwidth?
7. Why might bitrate rise at night?
8. What four things belong in a bandwidth statement?

## References

- [`../32_Engineering_Math/03_bandwidth.md`](../32_Engineering_Math/03_bandwidth.md) — the
  derivation: bitrate arithmetic, frame-rate and codec scaling, peak vs average. Prerequisite.
- [`../28_Calculators/psec/video.py`](../28_Calculators/psec/video.py) — `CameraGroup`,
  `VideoSystem`, `scale_bitrate_mbps`, and `SMART_CODEC_FACTOR` (whose own comment flags it as
  highly scene-dependent).
- `[STANDARD][VERIFY]` H.264 is ITU-T H.264 / ISO-IEC 14496-10; H.265 is ITU-T H.265 / ISO-IEC
  23008-2. Verify current editions and, importantly, **licensing terms**, which are a commercial
  question with engineering consequences.
- `[MFR][VERIFY]` Smart-codec savings, H.265 decode support, and multicast behaviour are
  per-product. The 30–70% smart-codec range quoted here is practice, not a specification.
- `[PRACTICE]` All per-scene bitrate bands in worked example 6.1 are engineering estimates for a
  fictional site. Substitute measurements from your own sites as you accumulate them — that
  library is one of the more valuable things you will build in your first five years.

---

**Next:** [07 — Storage, Retention, and Redundancy](07_storage_and_retention.md) — where this
lesson's bitrate becomes disk, and where the most consequential number in the design gets decided
by someone who is not an engineer.
