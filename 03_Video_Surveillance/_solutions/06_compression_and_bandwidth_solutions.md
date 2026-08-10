# Solutions — 06 Compression, Bitrate, and Bandwidth

> Work the exercises in
> [`../06_compression_and_bandwidth.md`](../06_compression_and_bandwidth.md) before reading this.
> All aggregate figures were produced by running
> [`../../28_Calculators/psec/video.py`](../../28_Calculators/psec/video.py) and transcribed.

---

## E6.1 — Two calculators, 4.2 Mbps and 9.1 Mbps

**(a) Two assumptions that account for the difference.**

Any two of these earn credit; the first two are the most likely:

1. **Scene complexity setting.** One calculator assumed "low activity" (an office corridor), the
   other "high activity" (a busy exterior). This alone routinely produces a 2× difference, and it
   is usually a dropdown the user never touched.
2. **Codec.** One assumed H.265, the other H.264. That is roughly a 2× difference on its own —
   4.2 and 9.1 are almost exactly the H.265/H.264 relationship.
3. **Smart codec.** One included the manufacturer's smart-codec saving (commonly 30–70%) and the
   other did not.
4. **Rate control.** One quoted an average VBR figure, the other a CBR or capped-VBR ceiling.
   Average and cap are different quantities.
5. **Compression quality level.** Vendors' "high/medium/low" quality presets are not comparable
   between vendors.

**(b) What goes in the basis of design.**

> Per-camera bitrate for this group is estimated at **6 Mbps nominal, range 4 to 9 Mbps**,
> assuming H.264, capped VBR, 15 fps, and **no smart-codec saving**. Vendor calculators returned
> 4.2 and 9.1 Mbps for this specification; the difference is attributable to differing scene-activity
> and codec assumptions rather than to a disagreement about the camera. Provision is made at
> nominal + 20%. Actual bitrates will be measured per camera group within the first 30 days of
> operation and this provision reviewed.

The important moves: **state your own number**, put the range around it, name the assumptions that
generate the range, explain the vendor discrepancy rather than hiding it, and commit to measuring.

**(c) "So which is right?" — three sentences.**

> Neither is wrong; they are answering slightly different questions, because each one assumes a
> scene and they assumed different ones. The bitrate this camera actually produces depends far
> more on what is in front of it — how much moves, how much the light changes, whether there is
> weather or vegetation — than on the camera model, so any figure before installation is an
> estimate with a range around it. I have designed to 6 Mbps with provision to 9, and we will
> measure the real figure in the first month and adjust before it becomes a problem.

---

## E6.2 — Re-estimating the car park after the site visit

**(a) Which figure becomes the working estimate, and why.**

**The high figure, 12.5 Mbps.** The site visit found precisely the conditions the high end of the
band was reserved for: **mature deciduous trees** on two sides (constant leaf motion, and a seasonal
change as they fill out and drop), and **uncontrolled street lighting casting moving shadows**
(the encoder sees shadow movement as scene change, at night, when sensor noise is already
elevated). This is no longer an uncertainty band — it is a known condition, and continuing to
carry the nominal figure would be carrying an estimate you have evidence against.

> 🧠 **The professional point:** the range exists to be *collapsed by information*. A site visit
> that tells you which end of the band you are on has done its job, and the estimate should move
> immediately. An engineer who leaves the nominal figure in place after seeing the trees is
> holding an average rather than an estimate.

**(b) Recomputed system peak and 30-day storage.**

Car park group at 12.5 Mbps, all other groups at nominal:

| | Nominal throughout | Car park at high |
|---|---|---|
| Peak bandwidth | 121.0 Mbps | **166.0 Mbps** |
| 30-day storage | 39.20 TB | **53.78 TB** |

The car park's six cameras alone move from 30.0 to 75.0 Mbps, so the group goes from 25% of the
system's bandwidth to 45% of it — **six cameras out of thirty-one driving nearly half the load.**

**(c) Effect on the +20% headroom provision.**

| | Nominal | Car park at high |
|---|---|---|
| Peak + 20% | 145.2 Mbps | **199.2 Mbps** |
| Storage + 20% | 47.04 TB | **64.54 TB** |

The storage provision rises by **17.5 TB**, a 37% increase over the original provision. On a 1 GbE
uplink the video load moves from 14.5% to 19.9% — still comfortable, so **the network is
unaffected in practice while the storage decision changes materially.** Worth saying explicitly in
the report, because it directs the client's attention to the decision that actually moved.

---

## E6.3 — CBR at 4 Mbps everywhere

**(a) The scenario where it causes most harm.**

**During a busy incident on an evidence-critical camera.** Under CBR the encoder must hold 4 Mbps
regardless of scene content. When six people move through the vestibule at once — a scuffle, an
evacuation, a theft in progress — the quantity of change in the scene rises sharply, and the only
way to hold the bitrate constant is to **reduce quality**. Blocking and smearing appear on the
moving subjects, at the exact moment the footage is being created for.

The system passes every routine inspection, because on a quiet day 4 Mbps is generous for that
scene. It fails only under load, which is the only condition anyone will ever review it under.

**(b) Recommendation and reason.**

**Capped VBR**, with the cap set from the peak calculation. Quality stays consistent as scene
complexity varies, and the cap bounds the worst case so network and storage remain plannable. The
reasoning to give: CBR does not actually make the system predictable, it makes the *bitrate*
predictable while making the **image quality unpredictable in the specific direction that matters**
— worst exactly when busiest.

**(c) Satisfying IT's capacity-planning requirement.**

IT's requirement is legitimate and is about the **ceiling**, not the average. Capped VBR gives them
exactly that:

> Capped VBR gives your capacity planning a hard per-camera ceiling — the same guarantee CBR
> offers — because no camera can exceed its cap. The difference is that on a quiet corridor the
> camera will use well under the cap instead of padding to it, so your *average* utilisation drops
> while your *worst case* stays exactly as bounded as it is today. Size the links and the storage
> on the sum of the caps, precisely as you would with CBR, and you will find real utilisation runs
> comfortably below it.

**This resolves the disagreement rather than splitting it**, because CBR's only genuine advantage —
a known ceiling — is fully preserved by a cap. Point out the bonus: they also gain headroom they
did not have, since CBR consumed the full rate at all times.

---

## E6.4 — 200 cameras at a 30% motion duty cycle

**(a) Storage.** Falls to **30%** of continuous — a **3.33× reduction**. Storage scales linearly
with recorded time.

**(b) Peak bandwidth.** **Unchanged — a factor of 1.00.** When motion triggers, the camera streams
at its full rate. Only the *average* falls (also to 30%).

**(c) The risk, and the disclosure.**

*Risk in one sentence:* motion detection that fails to trigger produces no recording of the event
at all, so a missed detection is indistinguishable from nothing having happened.

*Two-sentence disclosure:*

> To fit the 30-day retention requirement within the existing storage, cameras in [zones] will
> record on motion rather than continuously, which reduces stored video to about 30% of continuous
> recording; the trade is that if the motion detector fails to trigger — a subject moving slowly,
> at the frame edge, or in heavy rain where sensitivity has been reduced to prevent false
> triggers — that event will not be recorded at all, and the gap will not be obvious on review.
> We recommend continuous recording on the cameras listed in [schedule] regardless, and pre- and
> post-event buffers of 10 seconds on all motion-recorded cameras; please confirm you accept this
> trade for the remaining zones.

**(d) Two cameras where you would refuse, and why.**

1. **Any identification camera at a chokepoint** — the vestibule, the main entrance, the gate. The
   entire design intent of a chokepoint camera is that everyone passing is captured; a detector
   that misses one person destroys the guarantee that makes the camera worth its cost. These
   cameras also have the *most* motion, so the storage saving is smallest exactly where the risk
   is highest.
2. **Any camera covering a high-value or regulated asset** — the server room, a cash office, a
   controlled-substance store. The incidents there are low-frequency and high-consequence, often
   involving someone moving deliberately and slowly, which is the motion profile detectors handle
   worst. A near-empty room also produces almost no footage under continuous recording, so the
   saving is negligible and the risk is total.

The general rule: **the storage saving from motion recording is largest where activity is lowest,
and the risk is largest where the consequence is highest — and those are frequently the same
camera.** Check that the camera you are economising on is not the one you cannot afford to miss.

---

## E6.5 — 🧠 Full at day 19

**(a) Why, with reasoning.**

Compare what was sized against what is actually produced:

```
sized:   60 cameras × 3.0 Mbps                 = 180.0 Mbps
actual:  40 × 2.2 Mbps  +  20 × 9.8 Mbps
       =  88.0          +  196.0               = 284.0 Mbps

ratio = 284.0 / 180.0 = 1.578×
```

Retention scales inversely with bitrate, so:

```
achieved retention = 30 days / 1.578 = 19.0 days
```

**That matches the observed 19 days exactly, so bitrate alone explains it** — there is no need to
look for a second cause such as RAID overhead or a decimal/binary units error (though both are
worth ruling out; see [32/04](../../32_Engineering_Math/04_storage.md)).

In storage terms:

```
installed (30 d at 180 Mbps): 58.32 TB
required  (30 d at 284 Mbps): 92.02 TB
shortfall:                    33.70 TB
```

**The root cause is a flat per-camera bitrate applied to a mixed system.** The corridors were
over-estimated (2.2 against 3.0) and the exteriors were under-estimated by more than 3× (9.8
against 3.0). The interior over-estimate partially masked the exterior under-estimate, which is why
the error was not obvious at design time — the *average* across 60 cameras is 4.73 Mbps, only 1.6×
the assumption, while the exterior group alone is 3.3× out.

**(b) Three options to reach 30 days.**

| Option | What it takes | What it costs |
|---|---|---|
| **A. Add storage** | **+33.70 TB** to reach 92.02 TB total | Capital, and rack/chassis capacity — check the array can expand before promising it |
| **B. Cap the exterior bitrate** | Exterior cameras capped to average **4.60 Mbps** (from 9.8 — a 53% reduction) | **Image quality on the exterior cameras**, which are the ones facing the highest-risk scenes. Likely unacceptable at that depth of cut |
| **C. Motion recording on the exterior group** | At **50% duty**, effective load 186.0 Mbps → **29.0 days**; at 40%, 32.5 days | Missed-event risk (E6.4), concentrated on exterior cameras where weather causes both false triggers and desensitisation |

*(A fourth, legitimate: reduce retention to 19 days and re-baseline the requirement — only if the
30 days was a preference rather than an obligation. Ask.)*

**(c) Recommendation, and what to say about the original number.**

**Recommend option A**, adding storage, unless the 30-day figure turns out to be a preference
rather than an obligation.

The reasoning: 30 days was specified for a reason, and both alternatives pay for the shortfall in
**evidentiary quality on the exterior cameras** — the cameras covering the perimeter, the car
park, and the approaches, which is where the incidents that need 30 days of retention actually
originate. Option B degrades those images permanently; option C introduces a chance of not
recording at all. Option A costs money once and costs nothing operationally. **Before committing,
confirm the array can physically expand** — if it cannot, the conversation changes to a chassis
replacement and options B and C get another look.

**What to tell the client about the original number:**

> The original sizing used a single 3 Mbps figure for every camera. That is a reasonable average
> for interior corridors — yours actually measure 2.2 — but exterior cameras produce far more
> data, because trees, weather, headlights, and changing light are constant scene change and that
> is what video compression is sensitive to. Yours measure 9.8 Mbps, more than three times the
> assumption. The interior over-estimate partly hid the exterior under-estimate, so the total was
> only about 60% short rather than obviously wrong, which is why it was not caught at design
> review. The fix is straightforward and we now have a month of real measurements rather than an
> estimate, so the new figure is solid: 92 TB for a true 30 days, against the 58 TB installed.

**What is being graded:** getting to 19.0 days from the arithmetic rather than hand-waving;
identifying the flat-rate assumption as the root cause; **noticing that the interior over-estimate
masked the exterior under-estimate**, which is why this class of error survives review; giving
options with honest costs rather than only the expensive one; and explaining the original error
without either concealing it or theatrically apologising for it. Note the closing move — the new
number is *better* than the original, because it comes from measurement. That is the argument that
makes the extra spend easy to approve.

---

## Retrieval check — answers

1. **Temporal** redundancy (between frames). It follows that bitrate is driven by **how much the
   scene changes**, which is a property of the scene, not the camera.
2. Because temporal compression encodes change: a car park has constantly moving trees, weather,
   headlights, and shifting light, while a corridor is empty and static most of the time.
3. CBR protects **predictable network and storage planning**. It fails by **degrading image quality
   when the scene gets busy** — during the incident.
4. **Capped VBR**, because it gives VBR's consistent quality with a hard ceiling you can plan
   against — preserving CBR's only real advantage.
5. Because **motion events correlate**: one vehicle triggers six cameras, a shift change fills every
   corridor, a storm activates every exterior camera. The peak is the moment of interest.
6. **No.** It reduces storage and average bandwidth; peak is unchanged, because a triggered camera
   streams at full rate.
7. **Sensor noise looks like scene change** to the encoder, so a noisy night image can compress
   worse than a clean daytime one.
8. A **nominal figure**, a **range**, the **assumptions** behind them, and a **commitment to
   measure** and revise.
