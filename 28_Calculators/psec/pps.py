"""Physical Protection System effectiveness: timely detection.

Implements the model taught in ../../01_Foundations/03_functional_chain.md.

    T_A = T_T - T_D              adversary time remaining after detection
    Effective  <=>  T_A > T_R    remaining delay must exceed response time

LIMITS OF THIS MODEL -- read before using it on anything real
-------------------------------------------------------------
* Delay values are estimates against an ASSUMED adversary with ASSUMED tools.
  Change the assumption and the answer changes. State it in writing, always.
* It assumes a single linear path. Real adversaries take the EASIEST path, so
  you must run this against the weakest path you can find, not the one you
  designed. Finding that path is adversary path analysis.
* Detection is modelled as binary and instantaneous at a task boundary. Real
  detection is probabilistic; a rigorous treatment carries P_d through the
  sequence (EASI-type models do this).
* It models INTERRUPTION, not neutralisation. Arriving is not stopping.
* It does not apply to insiders at all. An authorised insider trips nothing.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Task:
    """One step in an adversary's path, with the delay it imposes.

    ``detected_here`` marks the task at whose COMPLETION detection occurs.
    Placing detection at completion rather than start is the conservative
    choice: a door contact reports when the door opens, not when the adversary
    begins working on it.
    """
    name: str
    delay_s: float
    detected_here: bool = False
    detection_note: str = ""

    def __post_init__(self) -> None:
        if self.delay_s < 0:
            raise ValueError(f"delay_s must be >= 0 for task {self.name!r}")


@dataclass
class AdversaryPath:
    """An ordered sequence of tasks from the site boundary to the asset."""
    name: str
    tasks: list[Task] = field(default_factory=list)
    assessment_delay_s: float = 0.0   # operator time to assess and initiate response
    adversary_description: str = "UNSTATED -- state your assumed adversary and tools"

    def add(self, task: Task) -> "AdversaryPath":
        self.tasks.append(task)
        return self

    @property
    def total_task_time_s(self) -> float:
        """T_T -- total time from start to completing the act at the asset."""
        return sum(t.delay_s for t in self.tasks)

    @property
    def detection_time_s(self) -> float | None:
        """T_D -- time to detection AND assessment. None if never detected."""
        elapsed = 0.0
        for task in self.tasks:
            elapsed += task.delay_s
            if task.detected_here:
                return elapsed + self.assessment_delay_s
        return None

    @property
    def time_remaining_s(self) -> float | None:
        """T_A -- adversary time remaining after detection."""
        td = self.detection_time_s
        if td is None:
            return None
        return self.total_task_time_s - td

    def evaluate(self, response_time_s: float,
                 required_margin_s: float = 0.0) -> dict:
        """Assess timeliness against a response force time.

        ``required_margin_s`` is confidence headroom. Every input here is an
        estimate; designing to a zero margin means designing to fail half the
        time. Ask for a margin proportionate to your uncertainty.
        """
        if response_time_s < 0:
            raise ValueError("response_time_s must be >= 0")

        td = self.detection_time_s
        tt = self.total_task_time_s

        if td is None:
            return {
                "path": self.name,
                "adversary": self.adversary_description,
                "total_task_time_s": round(tt, 1),
                "detection_time_s": None,
                "time_remaining_s": None,
                "response_time_s": round(response_time_s, 1),
                "margin_s": None,
                "timely": False,
                "verdict": ("NO DETECTION ON THIS PATH. The system cannot "
                            "interrupt; it can only document after the fact."),
            }

        ta = tt - td
        margin = ta - response_time_s
        timely = margin > required_margin_s

        if timely:
            verdict = (f"TIMELY. {margin:.0f} s of margin beyond the "
                       f"{required_margin_s:.0f} s required.")
        elif margin > 0:
            verdict = (f"MARGINAL. {margin:.0f} s remaining but "
                       f"{required_margin_s:.0f} s of confidence margin was "
                       f"required. Treat as not timely.")
        else:
            verdict = (f"NOT TIMELY. Short by {abs(margin):.0f} s. The adversary "
                       f"completes the act before response arrives.")

        return {
            "path": self.name,
            "adversary": self.adversary_description,
            "total_task_time_s": round(tt, 1),
            "detection_time_s": round(td, 1),
            "time_remaining_s": round(ta, 1),
            "response_time_s": round(response_time_s, 1),
            "required_margin_s": round(required_margin_s, 1),
            "margin_s": round(margin, 1),
            "timely": timely,
            "verdict": verdict,
        }

    def required_detection_point_s(self, response_time_s: float,
                                   required_margin_s: float = 0.0) -> float:
        """Latest T_D that still yields a timely system.

            T_D_max = T_T - T_R - margin

        This is the DESIGN direction of the calculation: walk the path, find
        which task the adversary is executing at this elapsed time, and place
        detection at or before it. That is how a detection layer gets located by
        calculation instead of by habit.
        """
        return self.total_task_time_s - response_time_s - required_margin_s

    def timeline(self) -> list[dict]:
        """Cumulative timeline, for plotting or for putting in a report."""
        rows, elapsed = [], 0.0
        for t in self.tasks:
            start = elapsed
            elapsed += t.delay_s
            rows.append({
                "task": t.name,
                "delay_s": t.delay_s,
                "start_s": round(start, 1),
                "end_s": round(elapsed, 1),
                "detection": t.detected_here,
                "note": t.detection_note,
            })
        return rows


def compare_interventions(path: AdversaryPath, response_time_s: float,
                          required_margin_s: float = 0.0) -> dict:
    """What would it take to make this path timely?

    Returns the three levers, because when a system is not timely the answer is
    rarely "add hardware" -- and showing all three converts an argument about
    products into a decision about strategy.
    """
    base = path.evaluate(response_time_s, required_margin_s)
    if base["timely"]:
        return {"already_timely": True, "baseline": base}

    td = path.detection_time_s
    tt = path.total_task_time_s
    deficit = response_time_s + required_margin_s - (tt - (td or tt))
    cutoff = path.required_detection_point_s(response_time_s, required_margin_s)

    # If the required detection point is at or before t=0, no placement of
    # detection anywhere on this path can make the system timely. Saying
    # "move detection to -1150 s" would be arithmetically true and useless.
    if cutoff <= 0:
        earlier = (
            f"NOT ACHIEVABLE on this path. Timeliness would require detection "
            f"at t <= {cutoff:.0f} s, i.e. before the adversary sequence begins. "
            f"Even instantaneous detection at the property line leaves only "
            f"{tt:.0f} s against a {response_time_s:.0f} s response. Detection "
            f"alone cannot fix this -- go to the response or consequence lever.")
    elif td is None:
        earlier = (f"Add detection on this path at or before t = {cutoff:.0f} s "
                   f"(currently undetected).")
    else:
        earlier = (f"Move detection at least {deficit:.0f} s earlier in the path "
                   f"(T_D from {td:.0f} s to <= {cutoff:.0f} s). Constraint: "
                   f"detection is only useful where you can ASSESS it.")

    return {
        "already_timely": False,
        "baseline": base,
        "deficit_s": round(deficit, 1),
        "required_detection_point_s": round(cutoff, 1),
        "detection_lever_feasible": cutoff > 0,
        "levers": {
            "earlier_detection": earlier,
            "more_delay_after_detection": (
                f"Add at least {deficit:.0f} s of delay AFTER the detection "
                f"point. Delay added before detection buys nothing. Note that "
                f"delay cost rises steeply -- check this against the cost of "
                f"the other two levers before recommending it."),
            "faster_response": (
                f"Reduce response time by at least {deficit:.0f} s "
                f"(from {response_time_s:.0f} s to "
                f"<= {response_time_s - deficit:.0f} s). Usually the dominant "
                f"term and usually an OWNER decision, not an engineering one."),
            "reduce_consequence": (
                "Not a timeliness lever, but the one nobody proposes: move, "
                "reduce, or eliminate the asset so that a successful attack "
                "matters less. Frequently the cheapest option available."),
        },
    }
