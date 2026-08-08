# 16 — Automation

> **Automate repetitive engineering work. Never automate engineering judgment.**

This is your differentiator. Most security engineers manage device data by hand across five
drifting spreadsheets. You can build the pipeline. Within a year it will be the thing people
know you for.

---

## ⚠️ The constraint that shapes this entire track

**Bluebeam Scripting is a Max-plan feature. Your plan is Complete, so you do not have it.**
(Verified against Bluebeam's official support documentation, Aug 2026 — see
`../31_References/source_index.md`.)

Any tutorial you find that automates Revu via its scripting engine **does not apply to you.**

So this track is built on **offline processing of documented exports** — Markups List CSV/XML,
sheet metadata, Revit schedule exports, AutoCAD attribute extracts — using Python, entirely
locally. This is not a workaround; for your environment it is the better architecture:

- Nothing leaves your machine. No cloud, no AI service, no upload of project documents.
- Everything is auditable, diffable, and version-controllable.
- It works identically regardless of what license the next firm buys.

**No tool in this repository fabricates an API that doesn't exist.** If something isn't
documented and available in Revu 21 Complete, it isn't used here.

---

## What's built

### `data_model/` — the Security Device Data Model ✅

The single source of truth. Every other artifact is a *projection* of it.

```
                    ┌──────────────────────┐
                    │   DEVICE REGISTER    │   one CSV, one schema
                    │   (schema.py)        │
                    └──────────┬───────────┘
       ┌──────────────┬────────┼────────┬──────────────┬────────────┐
       ▼              ▼        ▼        ▼              ▼            ▼
  camera_schedule  door_    ip_plan  cable_      counts_by_    counts_by_
                   schedule           schedule    type          drawing
       │              │        │        │              │            │
       ▼              ▼        ▼        ▼              ▼            ▼
   Div 28 sheet   Door sched  IT      Cable      BOM / cost   Sheet QA
   + Bluebeam     + SOO       handoff schedule   estimate     check
```

| File | What it does |
|---|---|
| `schema.py` | `SecurityDevice` dataclass (44 fields), `DeviceRegister`, device-type catalogue, phase-based field requirements, and the projections above |
| `validate.py` | 11 validation rules producing severity-tagged findings. **Reports; never mutates.** |
| `../sample_data/devices_flawed.csv` | 23 synthetic devices containing deliberate, realistic errors |

**Run it:**
```bash
python3 16_Automation/data_model/validate.py \
        16_Automation/sample_data/devices_flawed.csv CD
```

**What it catches** (the tedious-for-humans, trivial-for-computers category):
duplicate device IDs · ID/type prefix mismatches · ID level vs. level-column disagreement ·
unknown device types · fields missing for the current design phase · orphaned controller /
power supply / switch references · malformed and **duplicate IP addresses** · malformed MACs ·
double-assigned switch ports · doors missing a DPS, a lock, a fail state, or a controller ·
**maglocks declared fail secure** · cameras with no resolution, lens, or pixel-density target ·
calculated PPF below the stated target · PoE class contradicting power source · locally
powered devices with no supply · devices traced to no requirement.

**What it deliberately does NOT catch:** whether a camera is in the right place, whether the
pixel-density target is appropriate, whether a door should be fail safe. That is judgment and
it stays with you. A tool that silently "fixes" your data will eventually silently break it,
and you won't notice until it's in a construction document.

**Phase awareness:** pass `SD`, `DD`, `CD`, or `CX`. An SD-phase device isn't flagged for a
missing IP address it cannot possibly have yet. This matters — a validator that cries wolf
gets ignored, which is worse than no validator.

### `28_Calculators/psec/` — engineering calculators ✅
Optics, video bandwidth/storage, PoE, voltage drop, battery, timely detection. 68 tests.
See [`../28_Calculators/README.md`](../28_Calculators/README.md).

---

## 🔧 Lab: use the flawed register as a design review exercise

Before running the validator:

1. Open `sample_data/devices_flawed.csv` in Excel.
2. Find as many problems as you can **by hand**. Time yourself.
3. Then run the validator and compare.
4. **The interesting question is not what you missed — it's which class of error you're bad
   at.** Most people are good at spotting a wrong value in a cell and bad at spotting a
   reference that points nowhere, because the latter requires holding two sheets in your head
   at once. That is precisely the class a computer should own.

Then: fix the register, re-run until clean, and **write a one-paragraph note on the two
errors you'd rank as most dangerous if they reached construction.** (Suggested answer: the
duplicate IP, because it produces intermittent field failures that are miserable to diagnose;
and the maglock/fail-secure contradiction, because it's a life-safety issue that a validator
caught and a reviewer might not.)

---

## Roadmap — not yet built

Tracked in `../COURSE_PROGRESS.md`. Planned, in priority order:

**Bluebeam (export-based only, Complete-compatible)**
- Markups List CSV analyzer → device counts by type, sheet, and status
- Markup-to-device-schedule converter (feeds the register above)
- Device naming validator against the Tool Chest convention
- Duplicate/missing-parameter detection across sheets
- Sheet inventory and revision comparison reporting (pairs with Batch Compare output)

**Revit**
- Schedule export QA and round-trip validation against the register
- Shared-parameter and family-naming validation
- Model-vs-schedule reconciliation
- Dynamo concepts; Revit API overview

**AutoCAD**
- Block attribute extraction (ATTOUT / DXF parsing) → device counts
- Layer standard validation

**Cross-cutting**
- BOM and parametric cost estimate generation
- Drawing↔specification coordination checker
- Commissioning tracker generation from the register
- Automated report generation

---

## Engineering standards for anything you add here

1. **Standard library only** unless there's a compelling reason. It has to run on a
   locked-down laptop without a software request.
2. **Synthetic data only.** Never commit real project data, real IP schemes, real device
   locations, or anything from a client. See the constraint in the root `README.md`.
3. **Report, don't mutate.** Findings, with severity and a device ID. A human decides.
4. **Test with hand-computed expected values.** The test file is the record of the
   derivation.
5. **Traceability.** Every output should be explainable back to an input. If you can't say
   why a tool produced a number, you can't put that number in a document.
6. **Fail loudly on bad input.** A validator that swallows a malformed row is worse than no
   validator, because it produces false confidence.
