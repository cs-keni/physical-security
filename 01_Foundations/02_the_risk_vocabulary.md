# 02 — The Risk Vocabulary

## Learning objectives

- Define, precisely and distinguishably, the twenty core risk terms.
- Explain the risk equation, what each factor means, and where it breaks down.
- Distinguish threat from hazard, vulnerability from weakness, likelihood from probability,
  and consequence from impact.
- Explain residual risk and risk tolerance, and identify who owns each.
- Recognize when someone is using these words loosely, and know when it matters.

---

## Why precision here is not pedantry

You are going to sit in a meeting with a risk analyst, an insurance broker, a facilities
director, and a CFO. All four will use the word "risk" to mean four different things:

- The **risk analyst** means a computed function of threat, vulnerability, and consequence.
- The **insurance broker** means expected annual loss in dollars.
- The **facilities director** means "the thing I'm worried about" — a hazard.
- The **CFO** means variance in financial outcomes, including *upside*.

If you don't notice this, you will spend an hour in violent agreement, or worse, produce a
deliverable that answers a question nobody asked. The vocabulary below is the standard used
in security engineering. Learn it precisely, then translate for your audience.

---

## The core chain

Everything hangs on this chain. Learn the chain and the definitions fall out of it.

```
   ASSET            something of value, with an owner and a consequence-of-loss
     │
     │  is exposed to
     ▼
   THREAT           an actor with intent + capability to cause an undesired event
   (or HAZARD)      (a hazard has no intent — flood, fire, earthquake)
     │
     │  exploits a
     ▼
   VULNERABILITY    a weakness in protection that the threat can actually use
     │
     │  producing an
     ▼
   UNDESIRED EVENT  theft, sabotage, breach, assault, disruption
     │
     │  causing a
     ▼
   CONSEQUENCE      the outcome: loss, injury, downtime, penalty, reputational harm
     │
     │  combined with LIKELIHOOD gives
     ▼
   RISK             a measure of how much this should worry us
     │
     │  reduced by
     ▼
   COUNTERMEASURE   a control that reduces threat, vulnerability, or consequence
     │
     │  leaving
     ▼
   RESIDUAL RISK    what remains — compared against RISK TOLERANCE to decide "enough?"
```

**Trace that chain out loud until it's automatic.** In a design review, you will be asked
"why is that there?" The correct answer walks this chain backward.

---

## The terms

### Asset
**Anything of value to the organization that warrants protection.**

Categories: people, property (equipment, inventory, cash), information (proprietary, PII,
classified), operations/continuity, reputation, and environment.

- Assets have **owners** — a person accountable for them. If you can't name the owner, you
  probably can't get a consequence rating either.
- Assets have **locations** — and the same asset class can exist in several places with
  different exposure.
- Assets have **criticality** — driven by consequence of loss, not by purchase price.

> ⚠️ The most-missed assets: *people* (always the highest consequence, always assumed rather
> than stated), *continuity of operations* (the ability to keep running — often worth more
> than any physical item), and *information in physical form* (drawings, prints, whiteboards,
> discarded documents, screens visible from windows).

### Threat
**An actor or force with the intent and capability to cause an undesired event.**

The security-engineering usage implies **intent**. Threats are adversarial.

Characterize a threat by:

| Attribute | Question |
|---|---|
| **Motivation** | Why do they want this? (financial, ideological, personal, recreational, revenge) |
| **Capability** | What can they actually do? (tools, skills, numbers, weapons, funding) |
| **Knowledge** | What do they know about the facility? (none, public, insider) |
| **Access** | Outsider, insider, or outsider colluding with insider? |
| **Risk aversion** | Will they act if they might be seen? Will they use force? Do they care about being caught? |

That last row is the one juniors forget and it changes designs more than any other. A
risk-averse adversary is stopped by *visible* controls. A risk-tolerant adversary is stopped
only by *effective* ones.

### Hazard
**A source of potential harm without intent.** Fire, flood, earthquake, wind, power failure,
equipment failure, pandemic, hazardous material release.

**Why the distinction matters engineering-wise:** hazards don't adapt. A flood will not
notice that you moved the generator and choose a different route. An adversary will. This
means:

- Hazard mitigation can be optimized against a known distribution (historical data, models).
- Threat mitigation must assume the adversary observes your countermeasures and adapts.
  This is why security design assumes the adversary knows the design — an assumption you'll
  recognize from Kerckhoffs's principle in cryptography.

Some events are both: a fire can be a hazard *or* arson. The consequence is identical; the
countermeasures differ entirely.

### Vulnerability
**A weakness in the protection system that a specific threat can exploit to reach an asset.**

Two words do a lot of work there:

- **"Specific threat"** — a vulnerability is always relative to an adversary. A 6-foot fence
  is not a vulnerability against a shoplifter; it's a vulnerability against a fit,
  determined intruder. State the pairing.
- **"Exploit to reach an asset"** — a weakness that leads nowhere is not a vulnerability
  worth reporting. An unlocked door to an empty mechanical closet with no further access is
  a finding of hygiene, not risk.

> ⚠️ **The most common junior vulnerability-assessment error** is producing a list of missing
> devices ("no camera at door 112") rather than a list of exploitable weaknesses ("an intruder
> entering via the north dock at night can reach the MDF without passing any detection, and
> would not be assessed until the morning shift"). The first is a shopping list. The second is
> an engineering finding, and it survives contact with a CFO.

### Likelihood
**The chance that an undesired event occurs in a stated period.**

In security, "likelihood" is usually preferred over "probability" because we rarely have the
data to state a real probability. Likelihood is typically expressed qualitatively (rare /
unlikely / possible / likely / almost certain) with defined anchors.

For **adversarial** events, likelihood is a function of:
- **Attractiveness** of the asset to that adversary
- **Accessibility** — how reachable it is
- **Adversary's perception** of being caught (not the actual chance — the *perceived* one)
- **Historical frequency** at this site and at similar sites

> **The honesty problem:** likelihood for rare, adversarial, high-consequence events is
> essentially unknowable, and pretending otherwise produces false precision. This is why
> mature security engineering for critical facilities often abandons likelihood entirely and
> uses a **Design Basis Threat** instead: "we will design to defeat *this specified
> adversary*," sidestepping the question of how likely they are. See `02_Risk_Assessment/03`.

### Consequence and Impact
**Consequence** — the direct outcome of the undesired event. The server is stolen.

**Impact** — the broader effect on the organization. 400 customers lose service for 9 hours,
the SLA penalty is $180k, two customers don't renew, and the incident is reported publicly.

Used interchangeably in casual speech; keep them separate in analysis, because they scale
differently. Ten stolen laptops = 10× the consequence of one. The impact may be 1× (annoying)
or 100× (if one of them held the only copy of something).

Consequence categories to always evaluate: **life safety, financial, operational,
regulatory/legal, reputational, environmental.** Run every scenario through all six; the one
that justifies the budget is often not the obvious one.

### Risk
**A measure of the potential for loss, expressed as a function of threat, vulnerability, and
consequence.**

The security-engineering form:

```
Risk = f(Threat, Vulnerability, Consequence)
```

Often written multiplicatively:

```
R = T × V × C
```

where T = likelihood of attack attempt, V = likelihood the attempt succeeds given attempt
(i.e., 1 − effectiveness of protection), C = consequence given success.

**What this formula is good for:** forcing you to identify all three factors, and showing
that reducing *any* factor to near-zero reduces risk to near-zero. That's a genuinely useful
insight — it's why relocating an asset (reducing accessibility → V) can beat any amount of
hardware.

**What this formula is bad for:** producing a number. Multiplying three estimates, each
uncertain by an order of magnitude, produces a result uncertain by three orders of magnitude,
presented with spurious authority. Use the *structure*; distrust the *product*.

The insurance/quantitative form you'll meet in cyber and finance:

```
ALE = SLE × ARO
```
Annualized Loss Expectancy = Single Loss Expectancy × Annual Rate of Occurrence.
Useful when you have actuarial data (retail shrink, cargo theft). Useless for events that
have never happened at a facility that has existed for six years.

### Countermeasure / Control / Mitigation
**A measure that reduces risk** by reducing threat, vulnerability, or consequence.

Classified by *type*:
- **Physical** — barriers, locks, lighting, hardware
- **Electronic/technical** — cameras, sensors, access control, analytics
- **Procedural/administrative** — policy, training, escort rules, key control, audits
- **Personnel** — guards, receptionists, employee awareness

And by *function* (this is the classification you'll use daily — lesson 03):
deter, detect, delay, assess, respond, recover.

> **The rule that will make you look senior:** always evaluate procedural countermeasures
> before hardware. They are dramatically cheaper, faster to implement, and often more
> effective — and proposing one when a client expected a quote demonstrates you're solving
> their problem rather than selling them yours. The catch, which you must also say: procedural
> controls decay without enforcement, and hardware doesn't. Present both.

### Residual Risk
**The risk remaining after countermeasures are applied.**

```
Residual Risk = Inherent Risk − Risk Reduced by Countermeasures
```

Three things to internalize:

1. **Residual risk is never zero.** Any design that claims otherwise is wrong.
2. **Residual risk must be documented and communicated.** If you know the loading dock is
   unmonitored after 2200 because the owner cut it from the budget, that belongs in writing,
   in the Basis of Design, in language the owner understands.
3. **The owner accepts residual risk. You do not.** This is a professional boundary that
   matters enormously. Your job is to identify, quantify as best you can, present clearly,
   and recommend. The decision to accept belongs to the person accountable for the assets.
   Document the acceptance.

### Risk Tolerance / Risk Appetite
**Risk tolerance** — the amount of risk an organization is willing to bear.
**Risk appetite** — the amount it is willing to *pursue* in service of objectives. (The
distinction is mostly used in enterprise risk management; in security work, "tolerance" is
the term you'll use.)

Risk tolerance is **set by the organization, not by you**, and it varies wildly:

- A bank branch tolerates robbery risk it cannot economically eliminate; it optimizes for
  employee safety and evidence rather than prevention. Tellers are trained to comply.
- A pharmaceutical warehouse holding controlled substances has near-zero tolerance because
  the regulator sets it, not the company `[VERIFY — DEA requirements are jurisdiction and
  schedule specific]`.
- A hyperscale data center has near-zero tolerance for unauthorized access to a customer cage
  because the *contract* sets it — the tolerance is a commercial obligation.

> 🧠 **The senior move:** find out what *external* force is setting the tolerance —
> regulator, contract, insurer, parent company, recent incident, or the CEO's personal
> anxiety. That force determines your budget far more than any risk analysis you produce. It
> is entirely fair to ask, "what's driving the timing on this project?" The answer is
> frequently "we failed an audit" or "a customer asked," and it tells you what the design must
> demonstrably achieve.

### Risk Treatment — the four options
Every identified risk gets exactly one of these:

| Treatment | Meaning | Security example |
|---|---|---|
| **Avoid** | Stop doing the thing that creates the risk | Don't store cash on site |
| **Reduce/Mitigate** | Apply countermeasures | Add detection and response |
| **Transfer/Share** | Move financial consequence to another party | Insurance; contractual liability shift to a vendor |
| **Accept** | Bear it knowingly | Document and monitor |

Note that **transfer moves the financial consequence, not the event.** Insurance does not
prevent the fire, and it does not restore your reputation or your people. Clients confuse
this constantly.

### Assurance vs. Effectiveness
**Effectiveness** — does the countermeasure work?
**Assurance** — how confident are we that it works, and how do we know?

An untested camera system has unknown effectiveness and zero assurance. This distinction is
the entire justification for commissioning (module `18_`) and for periodic testing. A design
without a test plan is a hypothesis.

---

## Threat vs. Hazard vs. Vulnerability vs. Risk — the disambiguation drill

People confuse these constantly. Practice:

| Statement | What it actually names |
|---|---|
| "Burglars operate in this neighborhood." | **Threat** |
| "The area floods every few years." | **Hazard** |
| "The rear door has no contact and is not visible from anywhere staffed." | **Vulnerability** |
| "Cash is kept in an unlocked drawer overnight." | **Vulnerability** (and an asset statement) |
| "We might lose $50k and be closed for two days." | **Consequence/Impact** |
| "There's a meaningful chance of an after-hours burglary causing a two-day closure." | **Risk** |
| "We're worried about break-ins." | Ambiguous — clarify before proceeding |

That last row is what clients actually say. Your first job is disambiguation.

---

## 🧮 Worked example: a small pharmacy

**Asset:** Schedule II controlled substances, ~$40k street value, in a stock room.
Owner: pharmacist-in-charge. Also: staff (people), and the DEA registration itself (the
ability to operate).

**Threats:**
- T1 — Opportunistic addict, low capability, low planning, high risk-tolerance while
  impaired, likely to attempt forced entry after hours or robbery during hours.
- T2 — Organized diversion crew, moderate capability, surveils first, targets multiple
  pharmacies, tools available, risk-averse to *detection* but not to force.
- T3 — **Insider** (employee diversion). High knowledge, authorized access, low volume per
  event, sustained over time. *Statistically the largest loss source in this industry* — and
  the one the client will not raise first.

**Hazards:** fire (destroying inventory and records), power loss (refrigerated stock).

**Vulnerabilities:**
- V1 — Stock room walls stop at the suspended ceiling; the plenum is continuous to the
  adjacent unleased retail space. (⚠️ balanced-protection violation — a UL-rated safe would
  be pointless while this exists.)
- V2 — Rear door has a mechanical lock and no monitoring; alley is unlit and unobserved.
- V3 — No perpetual inventory reconciliation → insider diversion is undetectable for months.

**Consequences:** loss of drugs ($40k), DEA reporting obligation and potential enforcement
action, potential loss of registration (**the business-ending consequence**), staff injury
during a robbery, reputational harm.

**Note what just happened:** the consequence that justifies the budget is not the $40k. It's
the registration. That reframing is the value the engineer adds, and it comes from asking
question 4 from lesson 01.

**Countermeasures (by function):**
| Function | Measure | Addresses |
|---|---|---|
| Deter | Visible signage, lighting the alley, visible camera at rear | T1, T2 |
| Delay | Slab-to-slab stock room walls, rated door + frame, safe for Schedule II | V1, T1, T2 |
| Detect | Door contact + interior motion, duress button at counter | T1, T2 |
| Assess | Camera at rear door, at stock room door, at counter | T1, T2 |
| Respond | Monitored alarm, police dispatch, robbery-response training | T1, T2 |
| **Detect (insider)** | **Perpetual inventory + reconciliation, access logging to stock room, video correlated to access events, audits** | **T3** |
| Recover | Insurance, DEA reporting procedure, incident response plan | all |

**Observe:** the insider threat is countered almost entirely by *procedure and audit*, not by
barriers. Barriers are irrelevant against someone authorized to be there. This is the general
pattern and it's worth memorizing.

**Residual risk:** insider diversion below the reconciliation detection threshold remains
possible; robbery during business hours cannot be prevented, only managed for staff safety
and evidence. Both are documented and presented to the owner for acceptance.

---

## Common mistakes

⚠️ **"Threat" used for everything.** "The threat is that the door doesn't lock." No — that's
a vulnerability. Sloppy here means sloppy analysis downstream.

⚠️ **Assessing vulnerability without a threat.** "Is this fence adequate?" is unanswerable.
"Is this fence adequate against an unequipped individual attempting entry unobserved at
night?" is answerable.

⚠️ **Confusing perceived risk with assessed risk.** The client's fear and the actual risk
profile are frequently uncorrelated. Both are real and both need managing — but don't let
one masquerade as the other in your report. Sometimes the honest finding is "the measure you
want reduces anxiety more than risk," and there are contexts where that's a legitimate
purchase; just label it accurately.

⚠️ **False precision.** A risk score of 14.7 derived from three guesses is not more rigorous
than "high"; it is less honest, because it hides its uncertainty.

⚠️ **Forgetting that likelihood is adversary-dependent.** Improving one control raises the
likelihood the adversary uses a *different* path. Risk doesn't always go down where you
pushed; sometimes it moves. Always ask "if I close this, where do they go next?"

---

## Junior vs. Senior

**Junior:** uses the terms correctly in writing; can build an asset register and a
vulnerability list from a checklist; knows residual risk exists.

**Senior:** elicits the asset and consequence picture from a client who has never thought
about it; recognizes when the stated concern is not the real driver; knows when to abandon
likelihood in favor of a design basis threat; can tell an owner "the control you asked for
doesn't address the risk you described" without damaging the relationship; and structures
findings so the residual risk acceptance is explicit and signed.

---

## Practice problems

For each, name the term(s) precisely and state what additional information you'd need.

1. "Our badge system is old."
2. "There were two car break-ins in the lot last month."
3. "If the chiller plant goes down, the whole floor of labs loses samples."
4. "The night cleaning crew has master keys and isn't background-checked."
5. "We're in a hurricane zone."
6. "The CEO wants a panic button."
7. "Anyone can walk from the public lobby to the executive floor without passing a person."
8. "Our competitor was hit by industrial espionage last year."

Then: for #4 and #7, walk the full chain (asset → threat → vulnerability → event →
consequence → countermeasure by function → residual risk).

> Solutions: [`_solutions/02_risk_vocabulary_solutions.md`](_solutions/02_risk_vocabulary_solutions.md) — **write your answers first.**

---

## Retrieval check

1. State the risk equation and explain what it's good for and bad for.
2. What's the difference between a threat and a hazard, and what engineering consequence follows?
3. Why is a vulnerability always relative to a specific threat?
4. Who accepts residual risk, and what is your obligation regarding it?
5. Name the four risk treatment options. Which one does insurance perform, and what does it *not* do?
6. What's the difference between effectiveness and assurance, and what activity provides assurance?

---

## References

- ASIS International — *Risk Assessment* standard. `[STANDARD]` `[VERIFY current edition]`
- ISO 31000 — *Risk management — Guidelines.* `[STANDARD]` The general risk vocabulary many
  clients' enterprise risk functions use; worth knowing for translation.
- ISO/IEC Guide 73 — *Risk management — Vocabulary.* `[STANDARD]`
- Garcia, M.L., *The Design and Evaluation of Physical Protection Systems*, 2nd ed. `[PRACTICE]`
- NIST SP 800-30 Rev. 1 — *Guide for Conducting Risk Assessments.* `[GUIDELINE]` Cyber-focused
  but the threat/vulnerability/likelihood/impact structure translates well and it's free.

**Next:** [03 — The Functional Chain](03_functional_chain.md)
