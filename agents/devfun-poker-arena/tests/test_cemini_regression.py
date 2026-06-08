"""Playground leak regression — cemini decide() on prod-shaped 6-max spots."""
from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))
sys.path.insert(0, str(ROOT))

from cemini_decide import decide, retrieve_solver_context  # noqa: E402
from tests.fixtures.regression_spots import regression_spots  # noqa: E402


def _merge_context(table: dict, extra: dict | None) -> dict:
    ctx = retrieve_solver_context(table)
    if not extra:
        return ctx
    for key, val in extra.items():
        if key == "opponent_hud" and isinstance(val, dict):
            base = dict(ctx.get("opponent_hud") or {})
            base.update(val)
            ctx["opponent_hud"] = base
        else:
            ctx[key] = val
    return ctx


def _run(spot_table: dict, context: dict | None = None) -> dict:
    env_saved: dict[str, str | None] = {}
    ctx_extra = dict(context or {})
    for key in list(ctx_extra.keys()):
        if key.startswith(("CEMINI_", "JACKPOT_", "ARENA_")):
            env_saved[key] = os.environ.get(key)
            os.environ[key] = str(ctx_extra.pop(key))
    try:
        ctx = _merge_context(spot_table, ctx_extra or None)
        out = decide(spot_table, deadline_s=10.0, research_context=ctx)
    finally:
        for key, prev in env_saved.items():
            if prev is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = prev
    legal = set(spot_table["allowedActions"]["availableActions"])
    assert out["action"] in legal, (
        f"illegal {out['action']!r} legal={sorted(legal)}"
    )
    assert "reasoning" in out and len(out["reasoning"]) <= 150
    return out


def test_all_regression_spots():
    for spot in regression_spots():
        action = _run(spot.table, spot.context)["action"]
        if spot.forbidden:
            assert action not in spot.forbidden, (
                f"{spot.id}: got {action!r}, forbidden={sorted(spot.forbidden)} "
                f"— {spot.notes}"
            )
        if spot.required:
            assert action in spot.required, (
                f"{spot.id}: expected one of {sorted(spot.required)}, got {action!r}"
            )


def test_regression_count_grows_with_analyze():
    """Guardrail: we should keep adding spots after each analyze cycle."""
    n = len(regression_spots())
    assert n >= 20, f"expected ≥20 regression spots, got {n}"
