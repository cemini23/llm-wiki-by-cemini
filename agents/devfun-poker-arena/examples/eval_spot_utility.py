"""K197 — rank eval/training spots by downstream utility (advisory)."""
from __future__ import annotations

from typing import Any


def spot_utility(spot: dict[str, Any]) -> float:
    """Simple utility: lift * weight / cost (fail-rate alone is not enough)."""
    lift = float(spot.get("downstream_lift", spot.get("lift", 0.0)) or 0.0)
    weight = float(spot.get("weight", 1.0) or 1.0)
    cost = float(spot.get("cost", 1.0) or 1.0)
    fail = float(spot.get("fail_rate", 0.0) or 0.0)
    # Mild fail-rate bonus, but lift dominates
    return (lift * weight + 0.15 * fail) / max(cost, 1e-6)


def rank_spots_by_utility(spots: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return spots sorted by utility descending; attaches ``utility`` field."""
    ranked: list[dict[str, Any]] = []
    for s in spots:
        row = dict(s)
        row["utility"] = spot_utility(s)
        ranked.append(row)
    ranked.sort(key=lambda r: float(r.get("utility", 0.0)), reverse=True)
    return ranked
