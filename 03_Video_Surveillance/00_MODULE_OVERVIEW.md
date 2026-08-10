# Module 03 — Video Surveillance

> **Time:** ~30–40 hours over 8–10 weeks for the full module, including the exercises and the
> capstone. This is the largest technical module in the academy.
> **Prerequisites:** [`../01_Foundations/`](../01_Foundations/) — you need the functional chain
> (`03`) and the zone model (`04`) before lesson 09 will make sense.
> [`../32_Engineering_Math/`](../32_Engineering_Math/) lessons **01–04** are a hard prerequisite
> for lessons 02, 04, 06, and 07 of this module.
> **What this module is not:** it is **not** the math. Module 32 derives the optics, the pixel
> density, the bitrate, and the storage arithmetic, and this module does not re-derive any of it.
> Read the division of labour below before you start.

---

## The division of labour with Module 32

This is the single most important thing to understand about this module, so it goes first.

| Question | Where it is answered |
|---|---|
| *Why* is `W = D·w/f` true? | [`../32_Engineering_Math/01_camera_fov.md`](../32_Engineering_Math/01_camera_fov.md) |
| Given a 32 ft storefront at 55 ft, what lens? | Module 32, lesson 01 |
| **Should this camera be looking at the storefront at all?** | **Here, lesson 09** |
| *Why* is PPF `px / W`, and why does it fall as `1/D`? | [`../32_Engineering_Math/02_pixel_density.md`](../32_Engineering_Math/02_pixel_density.md) |
| **Which DORI class does this door actually need, and who decides?** | **Here, lesson 04** |
| How do I compute the bitrate and the storage? | Module 32, lessons 03–04 |
| **Why did the number the vendor gave me differ by 2×, and which one goes in the spec?** | **Here, lessons 06–07** |

Module 32 answers *how do I compute it*. This module answers *what am I computing, and why that
and not something else*. A designer who has only module 32 will size a system beautifully against
a requirement nobody checked. A designer who has only this module will hand-wave numbers that a
reviewer will take apart.

**When a lesson here needs a formula, it links to module 32 and states the result.** It does not
reproduce the derivation. If you find yourself unable to follow a worked example here, that is a
signal to go back, not to push forward.

## Lessons

| # | Lesson | Core question it answers | Leans on |
|---|---|---|---|
| 01 | [The Imaging Chain](01_imaging_chain.md) | What happens between a photon and an operator's eye, and which link is actually limiting? | — |
| 02 | [Optics: Focal Length, FOV, Aperture, Depth of Field](02_optics_and_lenses.md) | What does the lens control that the sensor cannot fix? | 32/01 |
| 03 | [Sensors, Exposure, WDR, and Low Light](03_sensors_and_low_light.md) | Why does the image fail at 3 a.m. when the geometry says it should be fine? | — |
| 04 | [DORI and Pixel Density in Practice](04_dori_and_pixel_density.md) | Which target class does this scene need, and what does choosing wrong cost? | 32/02 |
| 05 | [Camera Form Factors and Tradeoffs](05_camera_form_factors.md) | Multisensor, PTZ, fisheye, or four fixed domes — and what is the real basis for deciding? | 32/03, 32/05 |
| 06 | [Compression, Bitrate, and Bandwidth](06_compression_and_bandwidth.md) | Where does a bitrate number come from, and why do two vendors disagree by 2×? | 32/03 |
| 07 | [Storage, Retention, and Redundancy](07_storage_and_retention.md) | How much disk, how much of it survives a failure, and who signs off on the retention? | 32/04 |
| 08 | [VMS Architecture](08_vms_architecture.md) | What are the servers, where do they fail, and what does federation actually buy? | 08, 09 |
| 09 | [Camera Placement Engineering](09_camera_placement.md) | Given a floor plan, where do cameras go and how is each one justified? | 01/03, 01/04, 32/01–02 |
| 10 | [Retail Case Study](10_retail_case_study.md) | Why *are* there four domes clustered over that till? | all prior |
| 11 | [Analytics and Health Monitoring](11_analytics_and_health.md) | What do analytics reliably do, what do they not, and how do you know a camera is still working? | 09 |

## Assessment and practice

- 🧮 [**The park-and-ride garage capstone**](_exercises/garage_design.md) — the module capstone.
  One fictional site designed end to end: imaging chain → optics → low light → DORI → form factor
  → bandwidth → storage → VMS → placement → analytics. Reference solution in
  [`_solutions/garage_design_reference.md`](_solutions/garage_design_reference.md).
  **It is chosen to make this module's instincts fail** — see the warning in the brief.
- Every lesson ends with **exercises**, answered in [`_solutions/`](_solutions/). Work them before
  opening the solutions; several contain deliberate traps.
- [`../25_Quizzes/quiz_03_video_surveillance.md`](../25_Quizzes/quiz_03_video_surveillance.md) —
  30 questions, isolated answer key.
- [`../26_Flashcards/03_video_surveillance.csv`](../26_Flashcards/03_video_surveillance.csv) —
  Anki-importable.

## Learning objectives for the module

By the end of this module you can:

1. Trace an image problem to the link in the imaging chain that caused it, from a still frame,
   and say which of the other links cannot fix it.
2. Select a lens from scene geometry **and** from the light available, and explain why the second
   constraint is the one that gets forgotten.
3. Predict how a scene will fail at night before it is built, and specify lighting and camera as
   one system rather than as two purchases.
4. Set a pixel-density target per zone from the **operational decision** the video must support,
   defend it in a room, and defend a lower one where budget demands, with the consequence
   documented in writing.
5. Choose between multisensor, PTZ, fisheye, and multiple fixed cameras on ports, licences,
   maintenance, and failure behaviour — not on pixel count.
6. Produce a bandwidth and storage figure with every assumption stated, present it as a range,
   and explain to an owner why the range is the honest answer.
7. Design a VMS topology that states where it fails and what happens when it does.
8. Place cameras on a floor plan so that every camera answers a written question, and identify
   which cameras in an existing design answer none.
9. Say plainly which analytics are dependable, which are marketing, and how a 200-camera system
   tells you that camera 147 has been showing a wall for six weeks.
10. For all of the above: distinguish what the system **prevents** from what it **documents**, and
    never let a client believe the second is the first.

## How to study this module

**Lesson 01 is the spine.** Every later lesson is one link in the chain it lays out. If you read
only one lesson properly, read that one properly.

**Lessons 02, 04, 06, and 07 each open with a pointer into module 32.** Follow it. These lessons
are deliberately thin on derivation and thick on judgment, and the judgment is unintelligible
without the derivation underneath it. The intended order is: read module 32's lesson, do its
problem set, then read the corresponding lesson here.

**Lessons 03 and 09 are where most real designs are lost.** Not the math — the math is easy and
`psec` already does it. Designs fail because nobody walked the site at night and because cameras
were placed to cover area instead of to answer questions. Both lessons are longer than their
subjects appear to justify, on purpose.

**Lesson 10 is a case study, not a lecture.** Read it after 01–09, with the floor plan in front of
you, and try to answer each question before reading on.

Finish with the [garage capstone](_exercises/garage_design.md). Budget four to six hours for it and
do not open the reference solution early. Its conclusion contradicts what lessons 04 and 09 will
have trained you to reach for, which is the point of it.

## The load-bearing ideas

If you retain eight things from this module:

1. **Most camera systems document; they do not prevent.** Say this to the client in the first
   meeting, in writing, in those words. A system sold as prevention and delivered as documentation
   is the single most common failure in this discipline, and it is a failure of the conversation,
   not of the equipment.
2. **The chain is only as good as its worst link, and the worst link is usually light.** A 4K
   sensor behind a dirty dome bubble in a scene lit to 2 lux produces a worse image than a 2 MP
   camera in a scene lit properly. Resolution is the link people buy; illumination is the link
   that binds.
3. **Every camera must answer a written question.** "Cover the lobby" is not a question. "Who
   passed through the north vestibule between 2 and 3 a.m., to a standard a stranger could
   identify" is a question, and it determines the lens, the mounting height, the pixel target, the
   lighting, and the retention. A camera with no question behind it is a camera nobody will look
   at.
4. **Pixel density is necessary, never sufficient.** Geometric PPF says nothing about motion blur,
   focus, compression artefacts, glare, or a 30° depression angle flattening a face. Meeting the
   number and failing the task is routine.
5. **A bitrate is a range, not a value.** Scene content drives it by more than 2×. Any single
   figure — yours or a vendor's — is a point estimate inside a wide distribution, and the
   professional act is to say so while still giving a number to build to.
6. **Retention is a legal and operational decision that engineers get handed as a number.** Ask
   who set it and against what obligation. Sizing 90 days perfectly when the actual obligation was
   180 is a failure that surfaces years later, in a deposition.
7. **Redundancy that has never been tested is a diagram, not a capability.** The failover that was
   never exercised, the RAID that was never rebuilt under load, the archive nobody has restored
   from — all of these are documented as working.
8. **A camera that has been misaimed for six weeks is worse than no camera**, because the client
   believed they were covered. Health monitoring is not an upsell; it is the thing that makes the
   rest of the design true a year later.

## Cross-references

| Module | Relationship |
|---|---|
| [`../32_Engineering_Math/`](../32_Engineering_Math/) | **The math.** Lessons 01–04 there are prerequisites here. See the division-of-labour table above. |
| [`../28_Calculators/`](../28_Calculators/) | `psec.optics` and `psec.video` implement the arithmetic. Every number in this module was produced by running it. |
| [`../01_Foundations/03_functional_chain.md`](../01_Foundations/03_functional_chain.md) | Detect / delay / respond. Lesson 09 places cameras against it; lesson 01's "document vs. prevent" is its direct consequence. |
| [`../01_Foundations/04_defense_in_depth_and_zones.md`](../01_Foundations/04_defense_in_depth_and_zones.md) | The zone model that lesson 09's per-zone pixel targets are set against. |
| [`../06_Perimeter_Security/`](../06_Perimeter_Security/) | Lighting design in depth. Lesson 03 covers only what a camera designer must know. *(not yet written)* |
| [`../08_Networking/`](../08_Networking/) | Where lesson 06's aggregate bitrate becomes a switch uplink, a VLAN, and a multicast decision. *(not yet written)* |
| [`../09_Cybersecurity/`](../09_Cybersecurity/) | Camera hardening, and the evidence-integrity question lesson 11 raises. *(not yet written)* |
| [`../16_Automation/data_model/`](../16_Automation/data_model/) | The camera schedule this module's output becomes. `schema.py` already projects one. |
| [`../27_Labs/`](../27_Labs/) | Project 2 (small office camera design) and Project 4 (retail) are the applied labs for this module. *(not yet written)* |
| [`../33_Design_Review_QA/`](../33_Design_Review_QA/) | Reviewing someone else's camera design against lesson 09's questions. *(not yet written)* |

## Certification mapping

| Content | APP domain | PSP domain |
|---|---|---|
| Imaging chain, optics, sensors | — | D2 Application, Design & Integration |
| DORI, pixel density targets | — | D1 Physical Security Assessment, D2 |
| Camera selection, form factors | — | D2 |
| Bandwidth, storage, retention | — | D2, D3 Implementation |
| VMS architecture, redundancy | — | D2, D3 |
| Placement engineering | D1 Security Fundamentals | D1, D2 |
| Analytics, health monitoring | D4 Security Operations | D3 |

> `[VERIFY]` Domain names and numbering per the current official ASIS Certification Handbook.
> These mappings are **provisional** — see
> [`../31_References/source_index.md`](../31_References/source_index.md) for the confidence note.
> The APP/PSP tracks are blocked on human verification.

---

> ⚠️ **Standing warnings for this module.**
>
> **Privacy is a design constraint, not a footnote.** Camera placement decisions carry legal and
> ethical weight that varies enormously by jurisdiction and by space type. Restrooms, changing
> areas, and medical treatment spaces are categorically off limits; break rooms, union
> workplaces, and residential sightlines are jurisdiction-dependent and frequently litigated.
> `[VERIFY]` This module teaches you to raise the question and document the answer, not to
> answer it yourself. Where a design decision has a privacy dimension, the lessons say so.
>
> **Every site, floor plan, and figure in this module is fictional**, including the three running
> case studies. Any resemblance to a real facility is coincidental and unintended.
>
> **Nothing here is a bypass technique.** Where an attack class matters to the design — glare
> blinding, IR retroreflection, camera tampering — the lessons name the class and give the
> countermeasure, and stop there.
