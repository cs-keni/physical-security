# 05 — PoE Budgets and Switch Capacity

> Derives the PoE half of [`../28_Calculators/psec/power.py`](../28_Calculators/psec/power.py).
> Also covers port and capacity planning, which is the same arithmetic looked at from the other
> side.

> **Scope note.** This module covers **low-voltage DC and PoE for security devices**. It is a
> design aid, not a substitute for an electrical engineer, the NEC as adopted in your
> jurisdiction, or the AHJ. Anything touching line voltage, branch circuits, grounding and
> bonding, or standby power systems belongs to a licensed EE. `[CODE][VERIFY]`

## Learning objectives

- Distinguish **PSE power** from **PD power** and explain what the difference physically is.
- Explain why you budget a switch against the **class allocation** rather than the datasheet
  draw, and what it costs you when you don't.
- Compute switch power utilization and identify the four independent ways a switch design fails.
- Recognize that **port count and power budget are separate constraints**, and determine which one
  binds for a given device mix.
- Explain why PoE does not need the voltage-drop calculation from lesson 06.

---

## The two numbers everyone conflates

`[STANDARD]` IEEE 802.3af / at / bt. `[VERIFY current edition]`

```
   PSE power  =  what the switch port must SOURCE     ← budget against THIS
   PD power   =  what the device may DRAW             ← datasheets quote THIS
```

**The difference is the worst-case cable loss the standard allows.** Power is sourced at the
switch, travels up to 100 m of twisted pair, and some of it becomes heat in the copper. The
standard guarantees the device gets its PD figure by requiring the switch to source the larger PSE
figure.

| Class | Standard | PSE (source) | PD (draw) | Loss allowance |
|---|---|---|---|---|
| `af` | 802.3af (Type 1) | **15.4 W** | 12.95 W | 2.45 W — 15.9% |
| `at` | 802.3at (Type 2, PoE+) | **30.0 W** | 25.50 W | 4.50 W — 15.0% |
| `bt_t3` | 802.3bt Type 3 (PoE++) | **60.0 W** | 51.00 W | 9.00 W — 15.0% |
| `bt_t4` | 802.3bt Type 4 (PoE++) | **90.0 W** | 71.30 W | 18.70 W — 20.8% |

> ⚠️ **The classic error:** a designer reads "camera: 12 W" off a datasheet, multiplies by 24
> cameras, gets 288 W, and specifies a switch with a 370 W budget. The datasheet figure is **PD**.
> The switch must source **PSE**, and if the camera classifies as Type 1 that is 15.4 W each —
> 369.6 W — which is 99.9% of the budget. The design that looked like it had 22% of headroom has
> 0.1%.

---

## Why budget by class, not by measured draw

The calculator uses the **class PSE allocation** by default, and only uses a measured or datasheet
draw if you explicitly supply one.

**The reason is how switches actually allocate.** Many switches reserve power by **class**, not by
consumption. A 6 W camera that negotiates as Type 2 can reserve **30 W** of the switch's budget
whether or not it ever draws it. Whether a given switch does **static** (by class) or **dynamic**
(by actual draw) allocation is a per-model question. `[VERIFY per switch datasheet]`

**Budgeting by class is the conservative answer and it is what keeps you out of trouble.**

### 🧮 Worked example 5.1 — what the override costs and buys

10 cameras that classify as Type 2 (`at`) but actually draw 8.5 W each:

```
   By class:          10 × 30.0 W  =  300.0 W reserved
   By actual draw:    10 × 8.5 W   =   85.0 W consumed

   Phantom reservation:              215.0 W
```

These are `test_poe_budget_uses_class_allocation_by_default` and
`test_poe_actual_draw_overrides_class`.

**215 W is not a rounding error — it is more than half of a typical 370 W switch budget.** On a
switch with static allocation, those ten cameras consume 300 W of budget and there is nothing you
can do about it except choose a switch with dynamic allocation or force a lower class.

**When to use the override:** only when you have **confirmed in writing** that the switch performs
dynamic allocation, *and* you have a measured or datasheet draw you trust. Then say so in the
design narrative, because the next engineer will not know why your budget is a third of what the
classes imply.

> 🧠 **The asymmetry that decides the default:** budgeting by class and being wrong means you
> bought a bigger switch than you needed. Budgeting by draw and being wrong means cameras stop
> powering up at 4 p.m. on a Friday when someone adds the last device. **Default to the failure
> mode that costs money rather than the one that costs availability.**

---

## Switch checks: four independent failure modes

`check()` returns a list of findings; an empty list means it passes. There are four, and they are
genuinely independent — a design can fail any subset.

### 1. Oversubscribed ports

```
   ports_used > port_count
```

### 🧮 Worked example 5.2 — the test case

12 cameras on an 8-port switch:

```
   ports_used = 12,  port_count = 8   →  OVERSUBSCRIBED PORTS
   ports_free = 8 − 12 = −4           →  also triggers the spare-port finding
```

This is `test_switch_detects_port_oversubscription`. Note it produces **two** findings, and that
the free-port count goes negative rather than clamping at zero. **Letting it go negative is
correct** — it tells you *how badly* you're over, which a clamp would hide.

### 2. PoE budget exceeded

```
   power_used > poe_budget
```

### 🧮 Worked example 5.3 — the test case

8 PTZ cameras at Type 3 on a 24-port switch with a 370 W budget:

```
   power_used = 8 × 60.0 W = 480.0 W
   budget     =              370.0 W
   over by                   110.0 W
   utilization = 480/370 = 130%
```

This is `test_switch_detects_budget_exceeded`, and it also trips the "tight" finding at 130%.

**Ports were never the problem** — 8 devices on 24 ports is fine. **Power bound first**, which is
the normal situation once PTZs or heaters enter the design.

### 3. Insufficient spare ports

```
   required_spare = ceil(port_count × spare_port_pct)      spare_port_pct = 0.20  [PRACTICE]
   finding if ports_free < required_spare
```

### 🧮 Worked example 5.4 — the test case

22 cameras on a 24-port switch at 20% spare:

```
   ports_free     = 24 − 22        =  2
   required_spare = ceil(24 × 0.20) = ceil(4.8) = 5

   2 < 5  →  INSUFFICIENT SPARE PORTS
```

This is `test_switch_detects_insufficient_spare_ports`.

**Why `ceil` and not `round`:** 4.8 rounds to 5 either way, but `ceil(24 × 0.10) = ceil(2.4) = 3`
while `round(2.4) = 2`. **The spare-port rule is a minimum, and rounding a minimum downward
defeats it.** `ceil` is the semantically correct operation for "at least this many."

**Why 20%:** `[PRACTICE]`, not a standard. It covers the device you forgot, the device added in
year two, the port that fails, and the technician who needs to plug a laptop in. On a 24-port
switch that is 5 ports, which sounds generous until the first change order.

### 4. PoE budget tight

```
   finding if utilization > 80%
```

A warning rather than an error. At 83% utilization the design works today and one more camera may
not power up. The finding exists to make you look at the growth plan before you ship.

### 🧮 Worked example 5.5 — the clean case

24 Type 1 cameras on a 48-port switch with a 740 W budget:

```
   power_used  = 24 × 15.4 = 369.6 W
   utilization = 369.6 / 740 = 49.9%
   ports_free  = 48 − 24 = 24,  required = ceil(9.6) = 10   ✅
```

**No findings.** This is `test_clean_switch_has_no_findings`, and it is worth studying as the
shape of a comfortable design: about half the power budget and half the ports, on both axes.

---

## Port count and power budget are separate constraints

**This is the capacity-planning insight.** A switch has two capacities and either can bind first.

### 🧮 Worked example 5.6 — filling a 48-port / 740 W switch with Type 1 cameras

| Cameras | Power used | Utilization | Ports free | Findings |
|---|---|---|---|---|
| 24 | 369.6 W | 49.9% | 24 | none ✅ |
| 32 | 492.8 W | 66.6% | 16 | none ✅ |
| 40 | 616.0 W | **83.2%** | 8 | tight; spare ports short (need 10) |
| 48 | 739.2 W | **99.9%** | 0 | tight; no spares |

**Notice what happens at 48: 739.2 W against a 740 W budget.** This switch is *exactly* sized so
that a full complement of Type 1 devices consumes the entire budget. That is not a coincidence —
switch vendors size PoE supplies that way. **It means the switch has no margin at full port
occupancy, by design, and any device above Type 1 breaks it sooner.**

### 🧮 Worked example 5.7 — the mix changes which constraint binds

20 Type 1 cameras plus 4 Type 2 PTZs on the same 48-port / 740 W switch:

```
   20 × 15.4  =  308.0 W
    4 × 30.0  =  120.0 W
                 428.0 W        utilization 57.8%
   ports used = 24, free = 24, required spare = 10     ✅ no findings
```

24 devices, comfortable on both axes. But scale the PTZ count and power binds long before ports:

- **Ports bind** when devices are numerous and low-power — Type 1 cameras, door controllers,
  intercoms.
- **Power binds** when devices are few and hungry — PTZs, cameras with heaters and blowers,
  multi-sensor cameras, Type 3/4 anything.

> 🧠 **The planning habit: compute both numbers for every switch and state which one binds.**
> "SW-3: 34/48 ports, 612/740 W — power-bound" is a sentence that tells the next person what
> happens when they add a device. "SW-3: 34 cameras" is not.

---

## PoE does not need lesson 06's voltage-drop calculation

A reasonable question after lesson 06: shouldn't you compute voltage drop over the Cat cable?

**No, and the reason is instructive.** PoE handles cable loss *inside the standard*:

- PoE is delivered at 44–57 V and devices are specified to work across that range.
  `[STANDARD][VERIFY]`
- The **PSE minus PD difference is the loss allowance** — that gap *is* the voltage-drop budget,
  pre-computed by the standard for the worst permitted cable.
- The **100 m channel limit** is what keeps the real loss inside that allowance.

**So the design rule for PoE is not a calculation, it is a constraint: stay within 100 m of
channel, use cable that meets the category spec, and budget by PSE class.** Do that and the
standard has done the voltage arithmetic for you.

**Lesson 06's calculation applies to the other thing:** dedicated low-voltage DC runs at 12 or
24 V to locks, strikes, and power supplies, where there is no standard doing it for you and a
long run at a few amps will fail silently. See
[`../35_Doors_and_Hardware/06_electrified_hardware_power_transfer.md`](../35_Doors_and_Hardware/06_electrified_hardware_power_transfer.md)
for what that failure looks like in a building.

> ⚠️ **Where PoE distance does bite:** the 100 m limit is *channel* length — patch cords included,
> not just the horizontal run. A 95 m horizontal run with 3 m of patch at each end is 101 m and
> out of spec. Measure the channel, not the cable pull.

---

## Assumptions and limits

| Assumption | Reality |
|---|---|
| Class allocation is what the switch does | Static vs. dynamic is per-model `[VERIFY]` |
| The PoE budget is a single number | Some switches have per-port or per-ASIC-group limits, and stacked switches may share or not share budget `[VERIFY]` |
| Full budget is always available | Budget may depend on which power supplies are installed, and on redundancy mode — an N+1 configuration may halve usable budget `[VERIFY]` |
| Temperature is irrelevant | Some switches derate PoE budget at elevated ambient temperature `[VERIFY]` |
| Devices draw their class | Devices with heaters draw far more in winter than the datasheet's typical figure |
| 20% spare ports is enough | `[PRACTICE]`; project-dependent |
| PoE is the only load | Non-PoE ports still consume ports, and uplinks consume ports |

**The redundancy one catches people.** A switch advertised with a 1440 W budget across two 740 W
supplies has 1440 W in combined mode and **740 W in N+1 redundant mode.** If the design assumed
1440 and the deployment is redundant, half the budget vanished at commissioning.

---

## Common mistakes

⚠️ **Budgeting on datasheet (PD) draw instead of class (PSE) allocation.**

⚠️ **Using the actual-draw override without confirming dynamic allocation.**

⚠️ **Computing ports and forgetting power, or vice versa.**

⚠️ **Ignoring redundancy mode's effect on usable budget.**

⚠️ **Forgetting that uplinks consume ports.**

⚠️ **Sizing spare ports by rounding rather than `ceil`.**

⚠️ **Measuring the cable pull instead of the channel** for the 100 m limit.

⚠️ **Ignoring camera heaters.** A PTZ with a heater is a different device in January.

⚠️ **Filling a switch to 99% and calling it fully utilized rather than fully consumed.**

---

## Junior vs. Senior

**Junior:** budgets by PSE class; computes utilization and spare ports; runs all four checks;
knows PoE has a 100 m limit.

**Senior:** states which constraint binds on every switch and why; verifies the switch's allocation
model and redundancy mode before trusting a budget number; accounts for heaters and seasonal draw;
treats the 20% spare rule as a project decision rather than a default; knows the PSE/PD gap *is*
the standard's voltage-drop budget and can explain why that means no calculation is needed; and
never uses the actual-draw override without a written note saying why it is safe.

---

## Problem set

**P5.1** For each PoE class, compute the loss allowance in watts and as a percentage of PSE power.
Which class has the largest percentage allowance, and speculate on why.

**P5.2** A design has 30 cameras whose datasheets say 11 W each. They classify as Type 2.
- (a) What does a naive budget from the datasheet give?
- (b) What must the switch actually source, assuming static allocation?
- (c) A 48-port switch with a 740 W budget is proposed. Does it work? Show both constraints.
- (d) What single piece of information would change your answer, and where would you get it?

**P5.3** A 24-port switch with a 370 W budget is loaded with 6 Type 3 PTZs and 10 Type 1 cameras.
- (a) Compute ports used, power used, and utilization.
- (b) Run all four checks and list every finding.
- (c) Propose two different fixes and state what each costs.

**P5.4** You are planning switch capacity for 140 devices: 96 Type 1 cameras, 24 Type 2
multi-sensor cameras, 12 Type 3 PTZs, and 8 non-PoE door controllers. Available switches are
48-port/740 W. Determine the number of switches required, state which constraint binds, and show
your allocation. Remember uplinks.

**P5.5** Explain, in under 130 words to a project manager, why the switch you specified costs more
than the one the contractor proposed, when both are "48-port PoE switches."

**P5.6** A switch datasheet says "PoE budget: 1440 W (2 × 740 W supplies)." The installation will
be configured N+1 redundant. Compute the usable budget and explain the consequence for a design
that assumed 1440 W and loaded the switch to 1100 W.

**P5.7** 🧮 The `spare_port_pct` default is 0.20 and the code uses `ceil`. For port counts of 8,
12, 24, and 48, compute the required spare ports at 10%, 20%, and 25%. Identify every case where
`ceil` and `round` differ, and argue which is correct for this rule.

> Answers: [`_solutions/05_poe_solutions.md`](_solutions/05_poe_solutions.md)

---

## Retrieval check

1. Define PSE power and PD power. What is the difference, physically?
2. Which one do you budget against, and why?
3. Why does the calculator default to class allocation rather than measured draw?
4. Name the four switch checks.
5. Why `ceil` rather than `round` for spare ports?
6. What are the two independent capacities of a switch, and what kind of device mix makes each one
   bind?
7. Why doesn't PoE need a voltage-drop calculation?
8. How does redundancy mode change a switch's usable PoE budget?

---

## References

- IEEE 802.3af / 802.3at / 802.3bt — Power over Ethernet. `[STANDARD][VERIFY current edition]`
- TIA-568 cabling standards — the 100 m channel limit and its composition.
  `[STANDARD][VERIFY]`
- [`../28_Calculators/psec/power.py`](../28_Calculators/psec/power.py) — the implementation.
- [`../28_Calculators/tests/test_psec.py`](../28_Calculators/tests/test_psec.py) — `TestPower`.
- Switch manufacturer datasheets — allocation model, per-port limits, redundancy behaviour, and
  temperature derating. `[MFR][VERIFY]`
- [`../08_Networking/`](../08_Networking/) — switch architecture and topology *(not yet written)*.

**Next:** [06 — Voltage Drop and Conductor Selection](06_voltage_drop.md)
