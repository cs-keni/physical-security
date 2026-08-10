# Solutions — 01 The Imaging Chain

> Work the exercises in [`../01_imaging_chain.md`](../01_imaging_chain.md) before reading this.
> Numeric values here were produced by running
> [`../../28_Calculators/psec/optics.py`](../../28_Calculators/psec/optics.py) and transcribed.

---

## E1.1 — Diagnose the link

The skill being tested is not naming the link. It is naming the link people **wrongly** blame,
because that is the argument you will actually have to win.

**(a) Faces in the doorway are silhouettes against a bright atrium at midday.**

- **Cause: link [1], scene and light** — the light is behind the subject, and the scene's dynamic
  range exceeds what the sensor can hold. Link [4] (ISP) delivers the damage by metering for the
  bright background.
- **Commonly blamed: link [3], the sensor** — "we need a better camera / more megapixels."
- **Why that is wrong:** no sensor resolution recovers a subject that was exposed as a
  silhouette. A camera with genuinely better WDR helps somewhat, and is a legitimate link [3]/[4]
  intervention. But the cheap, reliable fix is at link [1]: put light on the subject side, or
  re-aim so the atrium is not directly behind the subject. Re-aiming is free.

**(b) The recording shows a subject in three positions with nothing between them.**

- **Cause: link [6], the network** — dropped frames from congestion or packet loss. Possibly
  link [7] if the recorder was writing faster than the storage could accept.
- **Commonly blamed: link [3] or the camera generally** — "the camera is glitching."
- **Why that is wrong:** the camera almost certainly captured and encoded those frames. They did
  not arrive or were not written. Diagnose with the camera's own frame counters versus the
  recorder's, not by looking at the video. **This failure is dangerous because the recording looks
  normal on casual review** — the gap is only visible when you need the missing seconds.

**(c) Number plates are legible but drivers' faces are soft in the same frame.**

- **Cause: link [2], the lens** — insufficient depth of field. The plate plane and the face plane
  are at different distances, and only one is inside the acceptable focus zone. A wide aperture
  chosen for low light narrows DOF, so this frequently appears only at night.
- **Commonly blamed: link [3]** — "resolution isn't high enough for faces."
- **Why that is wrong:** the plate proves resolution is sufficient at that distance. The face is
  not under-resolved, it is **out of focus**, and sharpening will not fix it. Fix at link [2]
  (smaller aperture, if light allows) or by accepting the real answer: **plate capture and facial
  capture are different tasks and normally need different cameras.** Lesson 09 returns to this;
  the capstone is built on it.

**(d) The subject's jacket is blue on Tuesday and grey on Wednesday, same camera.**

- **Cause: link [4], the ISP** — auto white balance responding differently to mixed or changing
  illumination (daylight plus sodium or LED, or a different mix at a different hour).
- **Commonly blamed: link [8] / the operator, or "the video is bad."**
- **Why it matters more than it looks:** colour is frequently the identifying descriptor in a
  witness statement and a BOLO. A system that reports colour unreliably is producing **confidently
  wrong evidence**, which is worse than producing none. Fix by locking white balance to the actual
  installed lighting, and by knowing that any IR-illuminated night image is monochrome and carries
  **no** colour information at all.

**(e) Footage of the incident exists but the incident was reported 45 days later.**

- **Cause: link [7], retention** — assuming retention was under 45 days, the footage is gone.
- **Commonly blamed: nobody, until it becomes a dispute** — and then, usually, the engineer who
  sized the storage.
- **The real failure is upstream of engineering:** somebody chose a retention period without
  reference to how long this type of incident historically takes to surface. Internal theft,
  harassment complaints, and insurance claims routinely surface in months, not days. **Ask who
  set the number and against what obligation, and get the answer in writing.** See lesson 07.

---

## E1.2 — The 2 MP → 8 MP proposal

A model answer, at the length and tone of a real email:

> Thanks — before we price this I want to flag that I don't think it will fix the problem.
>
> The night images in the yard are poor because of light, not resolution. Our geometry already
> puts enough pixels on target at the distances that matter; what's destroying the image is that
> at the current light level the cameras are holding the shutter open long enough to smear anyone
> who's moving, and running enough gain that noise reduction is smoothing away what's left.
>
> Moving from 2 MP to 8 MP on the same sensor size makes that worse, not better, in two ways.
> The pixels get smaller, so each one collects less light and the night image gets noisier. And
> the smear scales with pixel density: at four times the pixels, a walking person smears across
> four times as many pixels. **The ratio of blur to facial detail doesn't change at all** — we'd
> pay for the resolution, pay again in bandwidth and storage, and get an image that is just as
> unusable.
>
> What I'd propose instead: a night lighting assessment of the yard, then adding illumination
> where the faces actually need to be legible, and constraining the camera's maximum exposure time
> so it can't choose a shutter slow enough to smear. That's a fraction of the cost of re-heading
> 14 cameras, and it's the change that actually moves the image. If after that the geometry is
> short at specific distances, we upgrade those specific cameras — with numbers behind each one.

**What is being graded:** naming light as the binding link; the smaller-photosite argument; the
scale-invariance of the blur-to-detail ratio (see E1.3(d)); proposing the cheap intervention at the
binding link; and offering a path to the expensive fix *if the evidence supports it*. Refusing the
upgrade outright is the wrong answer — you do not yet know the geometry is adequate everywhere.

---

## E1.3 — Moving the vestibule camera from 12 ft to 22 ft

**(a) Slant range, scene width, PPF.**

Camera unchanged: 2688 px horizontal, 1/2.8" sensor (**w = 5.37 mm**), **f = 4 mm**, mount
**8.5 ft**, face plane **5.0 ft**. Floor distance now **22 ft**.

Slant range — [32/01](../../32_Engineering_Math/01_camera_fov.md):

```
D_slant = √(22.0² + (8.5 − 5.0)²) = √(484 + 12.25) = √496.25 = 22.28 ft
```

Scene width, `W = D·w/f`:

```
W = 22.28 ft × 5.37 mm / 4 mm = 29.91 ft
```

Pixel density, `PPF = px / W`:

```
PPF = 2688 / 29.91 = 89.88 ppf   (295 ppm)
```

| | 12 ft (original) | 22 ft (moved) |
|---|---|---|
| Slant range | 12.50 ft | 22.28 ft |
| Scene width | 16.78 ft | 29.91 ft |
| PPF | 160.18 | 89.88 |
| Class | identify | identify |
| Margin over identify | 2.11× | **1.18×** |

**(b) Does it still meet identify?**

**Yes — but only just.** 89.88 ppf against a 76 ppf threshold is a **1.18× margin**, down from
2.11×. The maximum range at which this camera holds identify is **26.35 ft**, so at 22 ft you are
inside the limit with about 4 ft of room.

The engineering point is that "meets identify" is now a *fragile* claim. Any of the following
pushes it under: the subject standing a foot further back than assumed, a lens focal length that
is 3.8 mm rather than the nominal 4 mm (manufacturing tolerance is real `[MFR][VERIFY]`), or the
face plane being lower than 5.0 ft for a shorter person. At 2.11× none of those matter. At 1.18×
all of them do. **Design margin is not padding; it is the tolerance budget for the things you did
not model.**

**(c) Depression angle.**

```
θ = arctan((8.5 − 5.0) / 22.0) = arctan(0.1591) = 9.04°
```

Down from **16.26°** at 12 ft. **This change helps.** A shallower depression angle gives a more
frontal view of the face, and facial capture degrades as the angle steepens — the practice limit
is around 30° `[PRACTICE]`.

So the move trades pixel density (worse, 160 → 90) for viewing angle (better, 16.3° → 9.0°). Both
matter to identification and they move in opposite directions as you pull back. **This is the
central geometric tension in identification-camera placement**, and it is why identification
cameras are mounted low and far rather than high and near. Lesson 09 makes it a placement rule.

**(d) Motion smear at the new PPF, and the ratio.**

Smear in feet is a property of the subject and the shutter — it does not depend on where the
camera is:

```
smear = 4.4 ft/s × (1/30) s = 0.1467 ft = 1.76 in
```

In pixels at the new density:

```
0.1467 ft × 89.88 ppf = 13.18 px      (was 23.5 px at 12 ft)
```

Eye-to-eye distance (2.5 in = 0.2083 ft) at the new density:

```
0.2083 ft × 89.88 ppf = 18.73 px      (was 33.4 px at 12 ft)
```

Ratios:

```
at 22 ft:  13.18 / 18.73 = 0.704
at 12 ft:  23.50 / 33.40 = 0.704
```

**The ratio has not changed — it is identical to three decimal places.**

**Why, in one sentence:** the smear and the facial feature are both physical lengths in the scene,
so multiplying by pixel density scales both by the same factor and the ratio cancels —
`(s × PPF) / (e × PPF) = s / e = 0.1467 / 0.2083 = 0.704`, a property of the shutter speed and the
subject's walking pace alone.

> 🧠 **This is the generalisation of worked example 1.2, and the most transferable idea in the
> lesson.** Motion blur expressed *relative to facial detail* is invariant under every change of
> pixel density — resolution, lens, distance, sensor. It can therefore be fixed **only** by
> changing the shutter (which requires light) or the subject's speed (which requires a
> chokepoint, a door, or a turnstile). No amount of resolution, and no camera placement, touches
> it. When a night image is blur-limited, the geometry conversation is over before it starts.

---

## E1.4 — The self-storage "prevents vs. documents" paragraph

A model answer at the required length:

> To set expectations clearly: with no staff on site after 6 p.m. and no one watching the cameras
> live, this system documents what happens — it does not stop it. If someone forces a unit at
> 2 a.m., we will very likely have usable footage of it, which is what supports a police report
> and an insurance claim, but nobody will be alerted while it is happening. If you want events
> interrupted rather than recorded, the options are monitored alarms with a response service, or a
> monitoring contract for the cameras themselves, and I am glad to price either — they are a
> different scope and a recurring cost rather than a one-time one.

**What is being graded:**

- It states the limitation **first and plainly**, without hedging.
- It is specific about *why* (no staff, no live monitoring), so it does not read as a disclaimer.
- It says what the system genuinely **does** deliver, with real value attached — this is what
  keeps it from being insulting.
- It offers the path to the thing they may actually want, and is honest that it costs money on an
  ongoing basis.
- It does not use the word "just," does not blame the client's budget, and does not oversell the
  deterrent effect (which is real but unquantifiable, and claiming it is where honest engineers
  drift into sales).

**A common wrong answer** is technically accurate and reads as contempt: *"Cameras don't prevent
crime. They only record it. You'd need guards for that."* Every clause is true. It tells the
client they were foolish, offers nothing, and is the reason some engineers are never asked back.

---

## E1.5 — 🧠 Should link [8] be in the chain?

**The strongest version of the colleague's argument:**

Engineering scope should end at the boundary of what the engineer controls and can specify. The
designer selects cameras, lenses, illumination, network, and storage; they do **not** hire
guards, write post orders, set staffing levels, or control whether anyone looks at a monitor at
3 a.m. Including an uncontrollable factor inside the engineering model muddies accountability:
it invites the engineer to be blamed for an operational failure, and — worse in practice — it
lets a client argue that a technically correct system was "badly engineered" when what actually
happened is that they cut the guard post. There is also a discipline argument: models are useful
because they are bounded. A chain that ends at "and then a human decides" ends at something with
no specification, no failure rate you can compute, and no acceptance test.

**The response, and where I land:**

The argument is right about accountability and wrong about scope. Two reasons.

First, **the chain describes information, not contract boundaries.** The claim being made is that
information only degrades, and that is simply true through the operator: a decision not made is
information lost as surely as a dropped frame. Excluding link [8] does not make the loss stop
happening; it makes it stop being visible in your model. Models that end where responsibility
ends are how systems get built that are individually correct and collectively useless.

Second, and decisively: **link [8] changes upstream engineering decisions.** If nobody watches
live, then the design should shift budget from live-view infrastructure toward retention, export
workflow, and image quality on recorded playback, because investigation is the actual use case. If
there *is* a monitored console, then latency, live stream quality, alarm presentation, and camera
handoff between views become real requirements. **You cannot correctly engineer links [1] through
[7] without knowing what link [8] is** — so it is inside the engineering problem whether or not
it is inside your contract.

The right resolution takes the colleague's concern seriously without dropping the link: **model
it, state the assumption in writing, and put it in the basis of design.** "This design assumes no
live monitoring; video is for post-incident investigation. If monitoring is added, cameras
X, Y, Z should be revisited." That records the dependency, prices the alternative, and protects
you if staffing changes — which addresses the accountability worry directly, and better than
silence would.

**Grading:** full credit for a defensible position on either side that engages the accountability
concern honestly and recognises that link [8] constrains upstream choices. The position taken
matters much less than whether the reasoning survives contact with the other side.

---

## Retrieval check — answers

1. Scene/light → lens → sensor → ISP → encoder → network → recorder → display/operator.
2. **Binding:** link [1], light. **Bought:** link [3], sensor resolution.
3. Link [1]: photons that never arrived. Link [3]: motion blur, clipped highlights, and noise.
   Link [5]: detail discarded by compression. None is recoverable downstream.
4. **Nothing.** An unmonitored camera is not a slow detector; it is not a detector.
5. Because the blur and the facial features scale together with pixel density, so their ratio is
   invariant — see E1.3(d).
6. A **night walk with a light meter** on a retrofit survey.
