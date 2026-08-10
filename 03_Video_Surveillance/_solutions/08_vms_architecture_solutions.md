# Solutions — 08 VMS Architecture

> Work the exercises in [`../08_vms_architecture.md`](../08_vms_architecture.md) before reading
> this. Bandwidth and storage figures were produced by running
> [`../../28_Calculators/psec/video.py`](../../28_Calculators/psec/video.py) and transcribed.

---

## E8.1 — 200 cameras, one recorder, 1 GbE NIC, 6 workstations

**(a) The two loads.**

```
recording:  200 cameras × 5.0 Mbps                = 1000 Mbps
live view:  6 workstations × 16 streams × 5.0 Mbps =  480 Mbps
total on the recorder's NIC                        = 1480 Mbps
```

**(b) Does it fit?**

**No.** A 1 GbE NIC carries 1000 Mbps in total. The design needs **1480 Mbps — 1.48× the
interface**, exceeding it by 480 Mbps.

⚠️ **Note the sharper problem: recording alone is exactly 1000 Mbps.** The interface is fully
consumed by the recording load before a single operator opens a client. Real-world usable
throughput on a 1 GbE link is meaningfully below line rate once protocol overhead is counted, so
this design is over capacity **even with zero viewers** — and the failure mode is dropped frames,
which produce recordings that look normal until you need the missing seconds
([lesson 01](../01_imaging_chain.md), link [6]).

**(c) Two fixes, and what each costs.**

| Fix | Result | Cost |
|---|---|---|
| **10 GbE NIC on the recorder** | 1480 Mbps = **14.8%** of 10 GbE. Comfortable, with room for growth | A 10 GbE NIC, a 10 GbE switch port, and the uplink capacity to carry it. Usually the cheapest fix if the switching supports it |
| **Split across two recorders** | Each: 500 Mbps recording + 240 Mbps live = **740 Mbps**, fits a 1 GbE NIC | A second server and its licences — **but it also halves the failure domain from 200 cameras to 100**, which is a benefit, not just a cost |

> ⚠️ **A third option that does *not* work alone, and is worth understanding.** Enabling substreams
> cuts live view from 480 Mbps to about 48 Mbps — a 90% reduction — but the total only falls to
> **1048 Mbps, still 105% of the NIC.** Substreams are a real and worthwhile improvement, and they
> cannot rescue a design whose *recording* load already equals the interface. **Fix the binding
> constraint first.** This is [lesson 01](../01_imaging_chain.md)'s limiting-link principle
> reappearing in the network tier: optimising the stage that is not the bottleneck changes nothing.

**The recommendation:** split across two recorders **and** enable substreams. The split fixes the
throughput and halves the failure domain; substreams then give both recorders large headroom and
fix the workstation decode load at the same time. On a 200-camera site, one recorder with no
failover was a poor architecture regardless of the NIC arithmetic.

---

## E8.2 — 30 stores, centralised recording to head office

**(a) WAN load.**

```
per store:  24 cameras × 3.0 Mbps =    72 Mbps sustained, 24/7
total:      30 stores × 72 Mbps   = 2160 Mbps = 2.16 Gbps at head office
```

Storage, for context: **777.6 GB per store per day**, and **699.8 TB** for 30 days across all 30
stores.

**(b) Why it fails, beyond the raw number.**

The 2.16 Gbps aggregate is the obvious problem. Four more, each independently fatal:

1. **72 Mbps per store is a *sustained floor*, not a peak.** It runs 24 hours a day, forever,
   alongside the store's point-of-sale, stock, card processing, and staff traffic. Typical retail
   branch circuits are not sized for a permanent 72 Mbps baseline, and video will either be shaped
   into failure or will starve the traffic the business actually runs on.
2. **A WAN outage destroys the recording, not just the view.** With centralised recording, when the
   link drops the video is simply not recorded — it does not queue. Retail WAN links fail routinely.
   The store is blind for the duration, permanently, with no recovery.
3. **Upstream bandwidth is the constraint, and it is the scarce direction.** Branch connections are
   usually asymmetric with far less upstream than downstream. Video recording is almost entirely
   upstream, on the side with least capacity.
4. **The cost is recurring and grows.** 2.16 Gbps of committed WAN into head office is an ongoing
   operating expense that scales with every new store and every camera added, and it buys nothing
   the alternative does not.

**(c) Recommended architecture, and what is lost.**

> **Record locally at each store, manage centrally.** A small recorder per store holding its 24
> cameras and its own retention, joined to a central management server at head office. Only streams
> someone is actively watching cross the WAN — intermittent, one or two streams at a time, a few
> Mbps rather than 72 sustained.

**What is lost by adopting it:**

- **Equipment at every site** — 30 recorders to buy, patch, monitor, and eventually replace, in
  locations with no technical staff. This is the real cost and it is an operational one.
- **Physical security of the recorder itself.** The recorder is now in the store, where it can be
  stolen or destroyed by the same person the video is recording. Mitigate by locating it in a
  secure back-of-house space, and consider that **for a robbery, the offsite copy is exactly what
  you want** — which is an argument for streaming a small set of critical cameras or key frames to
  head office in addition to local recording.
- **Central visibility depends on the management link**, so a WAN outage means head office cannot
  view or search that store — **but the store keeps recording**, and everything is available once
  the link returns. That is a dramatically better failure mode than losing the footage entirely.
- Cross-site search is slower than a single central database.

**On balance this is not a close call.** The centralised design fails on bandwidth, cost, and
failure behaviour simultaneously; the distributed one costs more equipment and more operational
attention. That is the correct trade, and it is why local recording with central management is the
standard multi-site pattern.

---

## E8.3 — Five failure-behaviour questions for a VMS vendor

| # | Question | What a weak answer reveals |
|---|---|---|
| 1 | **If the management server goes down, do the recorders keep recording, and can operators still log in to view live and playback?** | "It's fully redundant" without specifics means they have not been asked before, or the answer is unflattering. The common real answer — recording continues, login fails — is fine **if stated**, because you can design around it. Evasion means you will discover it during an outage |
| 2 | **If the database is lost or corrupted, what is lost — configuration, event history, or recorded video? And what is the documented recovery procedure and time?** | Any suggestion that recorded video is lost with the database is a serious architectural concern. Vagueness about recovery time means nobody has tested a restore |
| 3 | **When a recording server fails, what happens to its cameras — do they fail over, and if so how many seconds of video are lost in the transition?** | "It fails over seamlessly" with no number is marketing. There is **always** a gap; a vendor who names it (e.g. 10–30 s) is being straight with you. A vendor who claims zero has not measured |
| 4 | **Is video from before a failover still retrievable after it, and from which server?** | Hesitation here reveals the most commonly overlooked gap. Failover that records going forward but orphans prior footage is a partial solution presented as a complete one |
| 5 | **What happens when the licence server or licence file expires or becomes unreachable — does recording stop?** | If recording can stop for a *commercial* reason, that is a critical operational risk and must be designed around. Some platforms enter a grace period; some do not. This question is asked far too rarely |

*(A strong sixth: **what is the documented behaviour when storage reaches 100%** — does it overwrite
oldest-first as intended, stop recording, or fail unpredictably?)*

**How to use the answers:** put them in the architecture deliverable's failure-behaviour section
verbatim, attributed and dated, and **test the two most important at commissioning.** A vendor
statement that has never been tested on the delivered configuration is a claim, not a fact.

---

## E8.4 — 140 cameras on one recorder, no failover

**(a) What you need to know first.**

Do not answer "yes, you need redundancy" — it is unfounded until you know:

1. **What is the site's tolerance for a total recording outage?** Four hours? A day? A week? This is
   the question that determines the answer and nobody has asked them.
2. **Is there a live-monitoring function**, or is video reviewed after the fact? If nobody watches
   live, an outage costs recorded evidence for its duration; if there is a staffed console, it also
   costs situational awareness in real time.
3. **What is the realistic repair time today?** Spares on the shelf, a support contract with a
   4-hour response, or ordering a server? This sets the actual exposure and is often the cheapest
   thing to improve.
4. **Are there regulatory or insurance obligations** requiring continuous recording? `[VERIFY]` If
   so, the decision may not be theirs to make on cost grounds.
5. **Which of the 140 cameras are critical?** Frequently 15 or 20 matter far more than the rest, and
   that changes the shape of the answer entirely.

**(b) The options.**

| Option | What it changes | Rough cost |
|---|---|---|
| **Do nothing, improve spares** | Exposure falls from "order a server" to "swap a spare" — hours instead of days. **No architecture change** | A spare server on the shelf, or a support contract |
| **Split across two recorders** | Failure domain halves: 140 → ~70 cameras lost per failure. Also relieves NIC and throughput pressure | One server + licences |
| **Add a failover recorder (N+1)** | A failure is covered automatically; brief gap at transition | One server + licences + failover feature, if licensed separately |
| **Failover + split (2+1)** | ~70-camera domain *and* automatic cover | Three servers total |
| **Edge recording on critical cameras** | The most important cameras keep recording locally through any server or network failure, and backfill | SD cards; verify the VMS supports backfill `[MFR][VERIFY]` |

> 🧠 **The often-correct answer is a combination of the cheapest two:** a spare server on the shelf,
> plus edge recording on the 15–20 critical cameras. That covers the two things that actually matter
> — bounded repair time, and no loss at all on the cameras that count — for a fraction of a
> failover licence. Reach for the expensive architecture only when the tolerance answer in (a)(1)
> genuinely demands it.

**(c) The two-sentence framing.**

> Right now, if that recorder fails you lose recording on all 140 cameras until it is repaired or
> replaced — realistically somewhere between four hours and several days depending on whether you
> have a spare, and video from that window is gone permanently rather than delayed. The question
> isn't really whether you need redundancy, it's how long a total recording outage you can live
> with: tell me that number and I'll tell you the cheapest way to get inside it, because the answer
> ranges from a spare server on a shelf to a full failover pair.

**Why this framing works:** it states the exposure factually without alarm, it makes clear the loss
is **permanent** rather than an inconvenience (which is the part clients under-estimate), and it
converts an open-ended "do we need redundancy" into a single answerable question that they are
qualified to answer and you are not.

---

## E8.5 — 🧠 Six questions to unpack "fully redundant"

"Fully redundant" is not a specification. It is a category. These six establish what is inside it.

| # | Question | What a weak answer reveals |
|---|---|---|
| 1 | **Redundant against what, component by component?** Recording server, management server, database, storage, network, power — which of those have redundancy and which do not? | If the answer does not decompose cleanly, "fully redundant" means "the storage is RAID." That is redundancy against **disk failure only** ([lesson 07](../07_storage_and_retention.md)) being presented as system-wide redundancy — the single most common overstatement in this industry |
| 2 | **How many seconds of video are lost during a recording-server failover?** | "None" is not credible; there is always a detection interval plus a transition. A vendor who says "typically 15–30 seconds, depending on the heartbeat setting" is being straight and is telling you something you can design around |
| 3 | **Is video recorded *before* the failover still retrievable *after* it, and transparently to the operator?** | Hesitation reveals the orphaned-footage gap. A system that records forward but requires an administrator to manually re-attach prior recordings is not what the operator will experience as redundancy at 3 a.m. |
| 4 | **Is the redundancy active-active or active-standby, and if standby, is the standby's own health monitored?** | An unmonitored standby is a coin flip. The classic failure is a standby that died months ago and was never noticed — so at the moment of failover there is no redundancy at all, and the monitoring gap was invisible precisely because nothing was using it |
| 5 | **What is the documented, tested failover *test procedure*, and can we execute it at commissioning and annually?** | Reluctance to test is the strongest possible signal. Untested redundancy has an unknown probability of working, and the client believes it is one. If the vendor cannot describe how to test it, it has not been tested |
| 6 | **Does redundancy extend to licensing — does a failover server need its own licences, and does recording continue if the licence server is unreachable?** | This catches the commercial failure mode. A "fully redundant" system whose standby cannot legally record, or which stops recording when a licence check fails, is redundant against hardware failure and not against the thing most likely to actually stop it |

*(A strong seventh: **is the redundancy tested under load?** Failover on an idle system and failover
while writing 200 cameras are different events, and only one of them is the real one.)*

**The meta-point, and what this exercise is really teaching:** the phrase "fully redundant" is
answered by decomposing it into components, quantifying the transition, and demanding a test
procedure. Any vendor claim containing an absolute — *fully*, *seamless*, *zero downtime*, *no data
loss* — should trigger the same reflex: **which component, how many seconds, and how do we prove
it at commissioning?** Vendors who can answer those in specifics are usually the ones worth
buying from, and asking the questions early tends to improve the answers you get for the rest of
the project.

---

## Retrieval check — answers

1. **Recording server** (hardware failure, disk full, NIC saturation); **storage** (disk failure,
   capacity exhaustion); **management server** (service failure, licence or certificate expiry);
   **database** (corruption, unchecked growth); **clients** (decode capacity); **gateway/mobile**
   (security exposure).
2. Recording usually **continues** on the last known configuration; **operator login typically
   fails**, because authentication and permissions live on the management server. So the system
   records video nobody can watch. `[MFR][VERIFY per product]`
3. **Sustained write throughput, NIC capacity, licensing, and failure domain** — take the smallest.
   The real one is usually the **failure domain** (or the NIC), rarely raw throughput.
4. On the **recorder's network interface**, concentrated rather than spread across the camera VLAN.
   **Substreams** mitigate it — 59–71% reductions in the worked figures — and also relieve client
   decode load.
5. Because video is a **sustained** load, not a spike (72 Mbps per 24-camera store, permanently),
   it consumes the scarce **upstream** direction, and a WAN outage **destroys the recording**
   rather than merely interrupting the view.
6. Federation buys **one operator interface across independently owned, administered, or versioned
   systems**. It costs **weaker cross-site search**, complicated permissions, and a permanent
   version-compatibility obligation.
7. **A stated failure behaviour** — for each component, what stops working, for how long, and what
   the remedy would cost — so the client can accept or reject the exposure knowingly.
