# Source Index

The verification record for this curriculum. Two purposes:

1. **Accountability** — every substantive claim should be traceable to a source, and where it
   isn't, that should be visible rather than hidden.
2. **Your working bibliography** — as you verify things on real projects, log them here.

## How to read the tags

| Tag | Meaning | Your obligation |
|---|---|---|
| `[CODE]` | Adopted law in some jurisdiction | Confirm the **edition adopted locally**, local amendments, and the AHJ's interpretation |
| `[STANDARD]` | Consensus standard (UL, IEC, ANSI, ISO, NFPA) | Confirm current edition; note whether it's *referenced* by an adopted code (which makes it mandatory) or voluntary |
| `[GUIDELINE]` | Authoritative guidance, not mandatory | Use as a defensible basis; cite it |
| `[PRACTICE]` | Industry practice / respected text | Reasonable default; not authority |
| `[MFR]` | Manufacturer documentation | Product- and version-specific; goes stale |
| `[VERIFY]` | **I could not confirm this, or it changes over time** | Must be confirmed before it appears in a deliverable |

## Confidence disclosure for this repository

Written openly because a study guide that oversells its reliability is worse than useless.

| Area | Confidence | Why |
|---|---|---|
| Engineering physics and math (optics, bitrate, Ohm's law, voltage drop) | **High** | First-principles derivable; every formula in `28_Calculators/` is unit-tested against hand calculations |
| Methodology (D3ACR, timely detection, defense in depth, CPTED, requirements) | **High** | Long-established, well-documented, stable over decades |
| Product categories, form factors, tradeoffs | **High** | Stable at the category level |
| Specific product models, features, prices | **Low** | Goes stale within months — always pull the current datasheet |
| Code *concepts* (egress, fire interfaces, rated openings) | **Moderate** | The concepts are stable; the numbers are jurisdiction- and edition-specific and are all tagged `[VERIFY]` |
| Specific code numeric requirements | **Not asserted** | Deliberately. Get them from the adopted code text and the AHJ |
| ASIS certification domains and weightings | **Low — see below** | Could not be retrieved from the primary source |
| Bluebeam Revu 21 Complete feature availability | **Moderate-High** | Verified against Bluebeam's official support documentation, Aug 2026 |

---

## ⚠️ ASIS certification information — read this before building a study plan

**`www.asisonline.org` returns HTTP 403 to automated retrieval**, so the certification
details below could **not** be confirmed against the primary source. They come from
secondary sources and are recorded here with that caveat explicit.

**Action required from you:** download the current official **ASIS Certification Handbook**
from asisonline.org and verify domains, weightings, eligibility, exam length, passing score,
fees, and the reference reading list. Then correct the files in `22_APP/` and `23_PSP/` and
update this table. Certification bodies revise domains on multi-year cycles.

### APP — Associate Protection Professional `[VERIFY ALL]`

| Item | Value found | Confidence |
|---|---|---|
| Domain 1 | Security Fundamentals (~35%) | Low — secondary source |
| Domain 2 | Business Operations (~22%) | Low |
| Domain 3 | Risk Management (~25%) | Low |
| Domain 4 | Response Management (~18%) | Low |
| Exam format | 125 questions (100 scored + 25 pretest), 2 hours, Pearson VUE | Low |
| Eligibility | Experience + education combination — **not verified** | Not asserted |

### PSP — Physical Security Professional `[VERIFY ALL]`

| Item | Value found | Confidence |
|---|---|---|
| Domain 1 | Physical Security Assessment | Moderate — domain *names* appear consistently across sources |
| Domain 2 | Application, Design, and Integration of Physical Security Systems | Moderate |
| Domain 3 | Implementation of Physical Security Measures | Moderate |
| Weightings | **Conflicting/absent across sources — do not rely on any figure you see quoted** | Not asserted |
| Exam format | ~125 scored + 15 unscored questions; scaled passing score reported as 650 | Low |
| Eligibility | Reported as 3–5 years physical security experience depending on education | Low |

**Sources consulted (secondary, Aug 2026):** general web results referencing ASIS
certification pages. **Deliberately not cited individually**, because several were exam-dump
and test-prep marketing sites, which are not authoritative and should not be treated as such.

---

## Verified: Bluebeam Revu 21 subscription features

Verified against **Bluebeam official support documentation**, retrieved 2026-08-06:
`https://support.bluebeam.com/revu/subscription/subscription-features.html` `[MFR]`

**Your plan is Revu 21 Complete.** Confirmed availability:

| Feature | Complete? | Note |
|---|:---:|---|
| Sets | ✅ | |
| Compare Documents | ✅ | Also in lower tiers |
| Overlay Pages | ✅ | |
| Smart Overlay / Smart Review (view results) | ✅ | Complete and Max only |
| OCR | ✅ | |
| Tool Chest, custom tools | ✅ | |
| Markups List, custom columns | ✅ | |
| **Markups List export (CSV/XML)** | ✅ | Basics is PDF-only; Core and above export data — **this is the foundation of the `16_Automation/` Bluebeam track** |
| Formula custom columns | ✅ | Complete and Max only |
| **Batch Link** | ✅ | Complete and Max only |
| **Batch Compare** | ✅ | Complete and Max only |
| **Spaces** | ✅ | Complete and Max only |
| Quantity Link (Excel) | ✅ | |
| Dynamic fill markups | ✅ | Complete and Max only |
| Full measurement tools | ✅ | |
| Digital signatures, forms | ✅ | |
| Studio Sessions / Projects | ✅ | |
| **Scripting commands** | ❌ **MAX ONLY** | ⚠️ See below |
| Claude MCP integration | ❌ Max only | Not assumed anywhere in this curriculum |

> ⚠️ **Design consequence for this curriculum:** because **Bluebeam Scripting is Max-only**,
> the automation track in `16_Automation/` is built entirely on **offline processing of
> documented exports** (Markups List CSV/XML, sheet metadata) with Python — not on an
> in-application scripting API. Any tutorial you find online that automates Revu via its
> scripting engine does not apply to your plan. This constraint is also *better* practice
> for your environment: it keeps processing local and auditable.

> ⚠️ **Cloud/AI features are deliberately excluded**, per your stated privacy and security
> constraints. Nothing in this curriculum requires uploading project documents anywhere.

---

## Core references by module

### Foundational texts — buy these
| Source | Type | Why |
|---|---|---|
| Garcia, M.L., *The Design and Evaluation of Physical Protection Systems*, 2nd ed. | `[PRACTICE]` | **The** engineering text. Detect/delay/respond, timely detection, adversary sequence diagrams, EASI. If you buy one book, this one. |
| Garcia, M.L., *Vulnerability Assessment of Physical Protection Systems* | `[PRACTICE]` | The companion assessment methodology |
| ASIS International, *Protection of Assets* (POA) reference set | `[GUIDELINE]` | The professional reference set; check whether your firm has a subscription |
| Fennelly, L.J., *Effective Physical Security* | `[PRACTICE]` | Broad practitioner coverage |
| Crowe / Fennelly, *Crime Prevention Through Environmental Design* | `[PRACTICE]` | The standard CPTED reference |
| Leveson, N., *Engineering a Safer World* | `[PRACTICE]` | Systems-theoretic accident modeling — the best thing you can read on emergent failure, and well matched to your background |

### Codes and standards to know how to navigate `[VERIFY editions — all of them]`
| Source | Type | Relevance |
|---|---|---|
| IBC — International Building Code | `[CODE]` | Egress, occupancy, rated construction, opening protectives |
| IFC — International Fire Code | `[CODE]` | Fire safety, some security-affecting provisions |
| NFPA 101 — *Life Safety Code* | `[CODE]` | Egress, door hardware, delayed egress, access-controlled egress |
| NFPA 72 — *National Fire Alarm and Signaling Code* | `[CODE]` | Fire alarm interfaces, notification, secondary power |
| NFPA 70 (NEC) | `[CODE]` | Wiring methods, Class 2/3 circuits, plenum, pathways |
| NFPA 730 / 731 | `[GUIDELINE]` | Premises security guideline and installation standard — **note: guideline documents, distinct from mandatory codes** |
| ADA Standards for Accessible Design | `[CODE]` | Reach ranges, opening force, maneuvering clearances |
| UL 294 | `[STANDARD]` | Access control system units |
| UL 1076 | `[STANDARD]` | Proprietary burglar alarm units |
| UL 437 | `[STANDARD]` | Key locks |
| ANSI/BHMA A156 series | `[STANDARD]` | Door hardware grading |
| ASTM F2656 / F3016 | `[STANDARD]` | Vehicle barrier crash ratings |
| IEC 62676 series | `[STANDARD]` | Video surveillance systems; **Part 4 is the source of DORI** |
| IEC 60529 (IP), IEC 62262 (IK) | `[STANDARD]` | Ingress and impact protection ratings |
| NEMA 250 | `[STANDARD]` | Enclosure types (note: not interchangeable with IP) |
| SIA OSDP / SIA standards | `[STANDARD]` | Reader-to-controller protocol; the Wiegand replacement |
| ONVIF Profiles (S, G, T, M, A, C, D) | `[STANDARD]` | Video and access interoperability |
| BICSI TDMM and related | `[GUIDELINE]` | Telecom pathways, spaces, cabling practice |
| ISO 31000 / ISO Guide 73 | `[STANDARD]` | Risk vocabulary — for translating to enterprise risk functions |
| NIST SP 800-30, 800-53, 800-82, CSF | `[GUIDELINE]` | Risk assessment; controls; ICS/OT security; free and excellent |
| Interagency Security Committee (ISC) standards | `[STANDARD]` | Federal facility security levels and countermeasures |
| FEMA risk-management series (426/452 lineage) | `[GUIDELINE]` | Building blast/standoff and layered site security |
| IES lighting recommended practices | `[GUIDELINE]` | Illuminance, uniformity, glare for exterior and parking |
| ASIS standards and guidelines (Risk Assessment, PSC, etc.) | `[STANDARD]`/`[GUIDELINE]` | |

### Software documentation `[MFR]`
| Source | Note |
|---|---|
| Bluebeam Technical Support — subscription features | Verified Aug 2026; **your plan is Complete** |
| Bluebeam Revu 21 user guide and Tool Chest / Markups List documentation | Verify workflows against current docs before relying on them |
| Autodesk Revit help — families, shared parameters, schedules, sheets | |
| Autodesk AutoCAD help — layers, blocks, attributes, Xrefs, layouts | |
| Autodesk Dynamo / Revit API documentation | For the `16_Automation/` Revit track |
| Microsoft Excel documentation — dynamic arrays, Power Query | |

---

## Your verification log

Fill this in as you confirm things on real projects. This is the part that makes the
document yours.

| Date | Claim / topic | Source consulted | Edition / version | Outcome | Module to correct |
|---|---|---|---|---|---|
| 2026-08-06 | Bluebeam Complete feature set; Scripting is Max-only | support.bluebeam.com | Revu 21 | Confirmed | `12_`, `16_` |
| 2026-08-06 | ASIS APP/PSP domains | asisonline.org | — | **Blocked (403)** — unverified | `22_`, `23_` |
| | | | | | |
| | | | | | |
| | | | | | |

---

## Sources retrieved during authoring (2026-08-06)

- [Bluebeam Technical Support — Subscription features](https://support.bluebeam.com/revu/subscription/subscription-features.html) — `[MFR]` **verified, primary**
- [ASIS International — APP certification page](https://www.asisonline.org/certification/associate-protection-professional-app/) — **403, not retrievable**
- [ASIS International — PSP certification page](https://www.asisonline.org/certification/physical-security-professional/) — **403, not retrievable**

Secondary web results referencing ASIS domain structures were consulted but are **not cited
as authority** — several were exam-dump vendors. Treat all ASIS specifics in this repo as
provisional until you check the official handbook.
