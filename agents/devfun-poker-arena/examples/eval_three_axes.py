"""K160 — three-axis eval scoring stub (HL / sandbox advisory).

Axes: calibration, decision_quality, self_knowledge.
Requires a non-LLM baseline score for decision_quality comparisons.
"""
from __future__ import annotations

from typing import Any, Optional


AXES = ("calibration", "decision_quality", "self_knowledge")


def score_axes(
    report: dict[str, Any],
    *,
    baseline_bb100: Optional[float] = None,
) -> dict[str, Any]:
    """Score a preflight/HL report on the three WC2026-Agents axes.

    Expected optional keys on ``report``:
      calibration: float in [0,1] or bool
      decision_bb100: float (hero policy)
      baseline_bb100: float (non-LLM baseline) — or pass as arg
      self_knowledge: float in [0,1] or bool (reflection honesty fingerprint)
    """
    cal = _unit(report.get("calibration"))
    hero = report.get("decision_bb100")
    base = report.get("baseline_bb100", baseline_bb100)
    sk = _unit(report.get("self_knowledge"))

    decision_ok: Optional[bool] = None
    if hero is not None and base is not None:
        try:
            decision_ok = float(hero) >= float(base)
        except (TypeError, ValueError):
            decision_ok = None

    missing_baseline = base is None
    return {
        "schema": "devfun.eval_three_axes.v1",
        "calibration": cal,
        "decision_quality": {
            "hero_bb100": _float_or_none(hero),
            "baseline_bb100": _float_or_none(base),
            "beats_baseline": decision_ok,
            "missing_baseline": missing_baseline,
        },
        "self_knowledge": sk,
        "advisory_only": True,
        "notes": (
            "Hard non-LLM baseline required for decision_quality. "
            "Self-knowledge is a deploy fingerprint — not runtime decide()."
        ),
    }


def _unit(v: Any) -> Optional[float]:
    if v is None:
        return None
    if isinstance(v, bool):
        return 1.0 if v else 0.0
    try:
        x = float(v)
    except (TypeError, ValueError):
        return None
    return max(0.0, min(1.0, x))


def _float_or_none(v: Any) -> Optional[float]:
    if v is None:
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None
