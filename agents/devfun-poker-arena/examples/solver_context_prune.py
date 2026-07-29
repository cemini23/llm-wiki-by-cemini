"""K199/K201 — cap verbose solver / tool context dumps (advisory).

Fail-open: never raises on weird input; returns a smaller dict safe for
HL / trajectory summaries. Not a substitute for trusted bake tables.
"""
from __future__ import annotations

from typing import Any


def prune_solver_context(
    ctx: Any,
    *,
    max_keys: int = 12,
    max_str: int = 400,
    max_list: int = 20,
) -> Any:
    """Prune nested tool/solver context for long-thread summaries."""
    if ctx is None:
        return None
    if isinstance(ctx, (int, float, bool)):
        return ctx
    if isinstance(ctx, str):
        if len(ctx) <= max_str:
            return ctx
        return ctx[: max(0, max_str - 3)] + "..."
    if isinstance(ctx, list):
        trimmed = [prune_solver_context(x, max_keys=max_keys, max_str=max_str, max_list=max_list) for x in ctx[:max_list]]
        if len(ctx) > max_list:
            trimmed.append({"_truncated": f"+{len(ctx) - max_list} items"})
        return trimmed
    if isinstance(ctx, dict):
        keys = list(ctx.keys())
        out: dict[str, Any] = {}
        for k in keys[:max_keys]:
            out[str(k)] = prune_solver_context(
                ctx[k], max_keys=max_keys, max_str=max_str, max_list=max_list
            )
        if len(keys) > max_keys:
            out["_truncated"] = f"+{len(keys) - max_keys} keys"
        return out
    return str(ctx)[:max_str]


def assert_solver_grounded(numbers: dict[str, Any], *, source: str) -> dict[str, Any]:
    """Tag numeric claims with a trusted source label (narrate-only contract)."""
    src = (source or "").strip() or "unknown"
    return {
        "schema": "devfun.solver_grounded.v1",
        "source": src,
        "trusted": src not in ("", "unknown", "llm", "invented"),
        "numbers": dict(numbers),
    }
