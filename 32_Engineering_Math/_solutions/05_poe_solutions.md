# Solutions — 05 PoE Budgets and Switch Capacity

---

## P5.1 — Loss allowances by class

| Class | PSE | PD | Allowance (W) | Allowance (%) |
|---|---|---|---|---|
| `af` (Type 1) | 15.4 | 12.95 | 2.45 | **15.9%** |
| `at` (Type 2) | 30.0 | 25.50 | 4.50 | 15.0% |
| `bt_t3` (Type 3) | 60.0 | 51.00 | 9.00 | 15.0% |
| `bt_t4` (Type 4) | 90.0 | 71.30 | 18.70 | **20.8%** |

**Largest percentage allowance: Type 4, at 20.8%.**

**Why, plausibly:** loss in the cable is `I²R`. Type 4 delivers 90 W over the same 100 m of the
same copper, so it must push substantially more current, and **loss scales with the square of
current while delivered power scales linearly.** Doubling the power roughly doubles the current
and roughly quadruples the loss — so the loss *fraction* grows as you push more power down the
same cable. Type 4 mitigates this by using all four pairs, which is why the jump isn't worse than
it is.

Type 1 sitting at 15.9% rather than 15.0% is a smaller effect and mostly an artifact of where the
round PD numbers landed.

> 🧠 The transferable point: **this is the same physics as lesson 06.** Loss goes as current
> squared, so high-current, low-voltage delivery is always the expensive case. PoE manages it by
> using a relatively high voltage (44–57 V) and by capping the distance. Lesson 06 covers what
> happens when you have neither of those protections.

---

## P5.2 — 30 cameras, 11 W datasheet, Type 2 class

**(a) Naive budget from the datasheet**
```
   30 × 11.0 W = 330 W
```

**(b) What the switch must actually source (static allocation)**
```
   30 × 30.0 W = 900 W
```

**The datasheet figure understates the requirement by 570 W — a factor of 2.7.**

**(c) Does a 48-port / 740 W switch work?**

| Constraint | Value | Verdict |
|---|---|---|
| **Ports** | 30 used, 18 free; required spare `ceil(48 × 0.20) = 10` | ✅ passes |
| **Power** | 900 W required vs. 740 W available — **over by 160 W**, 121.6% utilization | ❌ **fails** |

**No.** Ports are comfortable; power is 22% over budget. This is the canonical case of the two
constraints diverging, and the naive datasheet budget of 330 W would have made the switch look
like it had 55% headroom.

**(d) The one piece of information that changes the answer**

**Whether the switch performs static or dynamic PoE allocation.** `[VERIFY per switch datasheet]`

- **Static (by class):** 900 W is real. The switch fails and you need a bigger budget, a second
  switch, or devices that classify lower.
- **Dynamic (by actual draw):** the switch reserves what the cameras consume, around 330 W plus
  overhead, and the 740 W switch is comfortable.

**Where you get it:** the switch manufacturer's datasheet or configuration guide, confirmed in
writing — not from a salesperson, and not by assuming. If you cannot confirm it, budget by class,
because that is the failure mode that costs money rather than availability.

**A second piece of information worth having:** whether the cameras can be *forced* to a lower
class. Many cameras negotiate Type 2 for headroom they never use, and some can be pinned to Type 1
in configuration. That would take the class budget to `30 × 15.4 = 462 W` and the switch works
regardless of allocation model.

---

## P5.3 — 24-port / 370 W with 6 Type 3 PTZs and 10 Type 1 cameras

**(a)**
```
   Ports used  =  6 + 10  =  16   (of 24; 8 free)

   Power       =  6 × 60.0  =  360.0 W
                 10 × 15.4  =  154.0 W
                              ───────
                              514.0 W

   Utilization =  514 / 370  =  138.9%
```

**(b) All four checks**

| Check | Result |
|---|---|
| Oversubscribed ports | ✅ pass — 16 of 24 |
| **PoE budget exceeded** | ❌ **fail — 514 W vs 370 W, over by 144 W** |
| Insufficient spare ports | ✅ pass — 8 free, `ceil(24 × 0.20) = 5` required |
| **PoE budget tight** | ❌ **fail — 139% utilized** |

Two findings, both power. **Ports are not remotely the problem** — the switch is a third empty on
ports and 39% over on power. Six PTZs did that.

**(c) Two fixes**

**Fix 1 — Split the PTZs onto a second switch with a larger budget.**
Move the 6 Type 3 PTZs (360 W) to a switch rated for them; the 10 Type 1 cameras then sit at
154 W / 370 W = 42% on the original switch.
*Cost:* a second switch, a second uplink, another rack unit, and another device to manage and
power. Also splits the failure domain, which is a genuine benefit — losing one switch no longer
takes out both the PTZs and the fixed cameras.

**Fix 2 — Replace with a higher-budget switch.**
A 24-port switch with a ~740 W or larger PoE budget puts 514 W at 69% utilization — under the 80%
threshold, with room for two more PTZs.
*Cost:* the switch, plus the higher-budget model's power supply requirements at the panel. Simpler
to manage than fix 1, and keeps everything in one failure domain, which is the trade-off in
reverse.

**Recommendation:** fix 2 for simplicity if the rack and circuit support it, fix 1 if you want the
PTZ failure domain separated or if the circuit can't take a larger supply. Both are legitimate;
the choice is about operations, not arithmetic.

---

## P5.4 — Capacity planning for 140 devices

**Device inventory:**

| Device | Count | Class | Power each | Total |
|---|---|---|---|---|
| Fixed cameras | 96 | Type 1 | 15.4 W | 1,478.4 W |
| Multi-sensor cameras | 24 | Type 2 | 30.0 W | 720.0 W |
| PTZs | 12 | Type 3 | 60.0 W | 720.0 W |
| Door controllers | 8 | non-PoE | 0 W | 0 W |
| **Total** | **140** | | | **2,918.4 W** |

**Constraint 1 — Power**
```
   2,918.4 W / 740 W per switch  =  3.94  →  4 switches minimum
```

**Constraint 2 — Ports**

Usable ports per switch, accounting for what actually consumes them:
```
   48 total
   − 1 uplink                          = 47
   − ceil(48 × 0.20) = 10 spare        = 37 usable
```
```
   140 devices / 37 usable  =  3.78  →  4 switches minimum
```

**Answer: 4 switches. Power binds first (3.94 vs. 3.78), but only just** — the two constraints are
within 5% of each other, which means this device mix is almost perfectly balanced against a
48-port/740 W switch, and *either* constraint will bind depending on how you allocate.

**A workable allocation** — deliberately not filling any switch to the limit on either axis:

| Switch | Devices | Ports used | Power |
|---|---|---|---|
| SW-1 | 24 fixed + 3 PTZ | 27 | 369.6 + 180.0 = **549.6 W** (74%) |
| SW-2 | 24 fixed + 3 PTZ | 27 | **549.6 W** (74%) |
| SW-3 | 24 fixed + 3 PTZ + 4 controllers | 31 | **549.6 W** (74%) |
| SW-4 | 24 fixed + 3 PTZ + 24 multi-sensor... | — | **over** |

**That last row doesn't fit**, which is the point of doing the allocation rather than dividing
totals. Redistributing:

| Switch | Devices | Ports (+1 uplink) | Power | Utilization |
|---|---|---|---|---|
| SW-1 | 24 fixed, 6 multi-sensor | 30 + 1 | 369.6 + 180.0 = **549.6 W** | 74% |
| SW-2 | 24 fixed, 6 multi-sensor | 30 + 1 | **549.6 W** | 74% |
| SW-3 | 24 fixed, 6 multi-sensor, 4 ctrl | 34 + 1 | **549.6 W** | 74% |
| SW-4 | 24 fixed, 6 multi-sensor, 4 ctrl | 34 + 1 | **549.6 W** | 74% |
| **PTZs** | 12 Type 3 | — | **720 W** | **needs its own** |

**The 12 PTZs at 720 W cannot be distributed without pushing a switch over.** Adding 3 PTZs
(180 W) to any of the four above takes it to 729.6 W — 98.6% utilization, which trips "tight" and
leaves nothing for growth.

**So the honest answer is 5 switches**, with the PTZs on a dedicated switch at 720/740 = 97%… which
also trips tight. **Six**, or a higher-budget switch for the PTZs.

> 🧠 **The lesson: totals ÷ capacity gives you a lower bound, not an answer.** Devices come in
> indivisible units with different power weights, so this is a bin-packing problem, and the
> arithmetic answer of "4" is unreachable in practice. **Always do the allocation table.** The gap
> between 4 and 6 switches is real money and it does not appear in the division.
>
> Also note the spare-port rule and the uplink together cost you 11 of 48 ports — 23% of the
> switch — before any device is connected. That is the correct amount to spend, and it needs to be
> visible in the count rather than discovered when the switch fills.

---

## P5.5 — Why the specified switch costs more

Model answer (126 words):

> They're both 48-port PoE switches, but "PoE switch" doesn't say how much power it can actually
> deliver, and that's the number that matters here.
>
> The contractor's switch has a 370 watt PoE budget. Ours has 740. With 48 ports, the cheaper one
> can power about 24 standard cameras before it runs out — half its ports. Our device mix includes
> multi-sensor cameras and PTZs that each draw two to four times a standard camera.
>
> On the cheaper switch we'd need two of them to power what one of ours handles, plus a second
> uplink and another device to manage. It's not cheaper by the time it's installed.
>
> Happy to send the load calculation — it's one page and it shows exactly where the 740 goes.

**What makes it work:** it identifies the specific spec the two switches differ on rather than
arguing about quality, converts it into a device count the PM can picture, and shows that the
cheaper option isn't cheaper once you count the second switch. Offering the calculation closes it.

---

## P5.6 — N+1 redundancy and usable budget

```
   Advertised: 1440 W  (2 × 740 W supplies, combined mode)
   N+1 redundant: one supply must be able to carry the whole load alone

   Usable budget = 740 W
```

**The consequence for a design loaded to 1100 W:**

**In normal operation, nothing appears wrong.** Both supplies are running, 1100 W is within the
combined 1440 W, and every device powers up. The design passes commissioning.

**When one supply fails — which is the entire reason redundancy was specified — the remaining
supply can source 740 W against an 1100 W load.** The switch does not gracefully degrade
bandwidth; it sheds PoE. Depending on the model it will drop ports by priority or by port number
until the load fits, meaning **roughly a third of the cameras go dark at the moment a power supply
fails.**

Worse: the failure is *silent until it happens*, and it happens during exactly the kind of
electrical event that also merits having video.

**What should have happened:** the design budget for an N+1 configuration is the capacity of
**N supplies, not N+1** — here, 740 W. At 1100 W of load the correct answers are a switch with
larger supplies, a third supply if the chassis supports 2+1, or a second switch.

> ⚠️ **The general trap: redundancy specifications reduce usable capacity, and the reduction is
> invisible in the headline number.** The same applies to redundant power supplies in recorders,
> to RAID (lesson 04 — redundancy costs raw capacity), and to N+1 anything. **Whenever a
> datasheet gives you a total, ask what the total is in the redundancy mode you are actually
> deploying.**

---

## P5.7 — 🧮 `ceil` vs. `round` for spare ports

| Ports | 10% raw | ceil | round | 20% raw | ceil | round | 25% raw | ceil | round |
|---|---|---|---|---|---|---|---|---|---|
| 8 | 0.80 | 1 | 1 | 1.60 | 2 | 2 | 2.00 | 2 | 2 |
| 12 | 1.20 | **2** | **1** ⚠️ | 2.40 | **3** | **2** ⚠️ | 3.00 | 3 | 3 |
| 24 | 2.40 | **3** | **2** ⚠️ | 4.80 | 5 | 5 | 6.00 | 6 | 6 |
| 48 | 4.80 | 5 | 5 | 9.60 | 10 | 10 | 12.00 | 12 | 12 |

**They differ in three cases**, all where the fractional part is below 0.5:
- 12 ports at 10% (1.20 → ceil 2, round 1)
- 12 ports at 20% (2.40 → ceil 3, round 2)
- 24 ports at 10% (2.40 → ceil 3, round 2)

**Which is correct: `ceil`, unambiguously.**

The rule is stated as a **minimum** — "at least 20% spare ports." `round` can return a value
*below* the stated minimum, which means the check would pass a design that violates its own rule.
At 24 ports and 10%, `round` permits 2 spare ports when the policy requires 2.4, i.e. at least 3.

**The general principle:** `ceil` is the semantically correct operation whenever a requirement is
expressed as "at least," and `floor` whenever it is "at most." `round` is correct only when the
quantity is genuinely an estimate with no directional constraint — which a minimum never is.

**A related check worth making in any codebase:** wherever you see `round()` applied to a
requirement, ask which direction the error runs and whether that direction is safe. Lesson 03's
P3.6 asked the same question about a modelling exponent, and lesson 04's defect was a different
form of the same failure — an operation that was *approximately* right and silently wrong in one
direction.

**Note that the 8-port and 48-port cases never differ**, which is why this could easily ship
untested: the two most common switch sizes both happen to produce fractional parts of 0.5 or above
at 20%. **The bug would only appear on 12-port switches** — uncommon, but they exist, and that is
exactly the kind of gap a value-pinning test should close rather than a spot check on the sizes
you happened to think of.
