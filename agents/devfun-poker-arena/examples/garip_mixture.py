"""K127 GARIP — Polyak running-average villain mixture helpers.

Nested dict shape matches ``aggregate_stance_mixtures`` output:
``stance → position → bucket → {fold, call, raise}``.
"""
from __future__ import annotations

import copy
import math
from typing import Any, Optional

ACTION_KEYS = ("fold", "call", "raise")


def snapshot_mixtures(
    mixes: dict[str, dict[str, dict[str, dict[str, float]]]],
) -> dict[str, dict[str, dict[str, dict[str, float]]]]:
    return copy.deepcopy(mixes)


def _blend_rate(prev: float, cur: float, alpha: float) -> float:
    a = max(0.0, min(1.0, alpha))
    return (1.0 - a) * prev + a * cur


def polyak_update_mixtures(
    prev: Optional[dict[str, dict[str, dict[str, dict[str, float]]]]],
    current: dict[str, dict[str, dict[str, dict[str, float]]]],
    alpha: float,
) -> dict[str, dict[str, dict[str, dict[str, float]]]]:
    """μ̄_t ← (1-α)μ̄_{t-1} + α μ_t across stance×position×bucket rates."""
    if prev is None:
        return snapshot_mixtures(current)

    out: dict[str, dict[str, dict[str, dict[str, float]]]] = {}
    stances = set(prev.keys()) | set(current.keys())
    for stance in stances:
        out[stance] = {}
        prev_st = prev.get(stance, {})
        cur_st = current.get(stance, {})
        positions = set(prev_st.keys()) | set(cur_st.keys())
        for pos in positions:
            out[stance][pos] = {}
            prev_pos = prev_st.get(pos, {})
            cur_pos = cur_st.get(pos, {})
            buckets = set(prev_pos.keys()) | set(cur_pos.keys())
            for bucket in buckets:
                prev_rates = prev_pos.get(bucket, {})
                cur_rates = cur_pos.get(bucket, {})
                blended: dict[str, float] = {}
                for key in ACTION_KEYS:
                    p = float(prev_rates.get(key, cur_rates.get(key, 0.0)))
                    c = float(cur_rates.get(key, p))
                    blended[key] = _blend_rate(p, c, alpha)
                out[stance][pos][bucket] = blended
    return out


def _flatten_mixture_rates(
    mixes: dict[str, dict[str, dict[str, dict[str, float]]]],
) -> list[float]:
    vals: list[float] = []
    for stance in sorted(mixes.keys()):
        for pos in sorted(mixes[stance].keys()):
            for bucket in sorted(mixes[stance][pos].keys()):
                rates = mixes[stance][pos][bucket]
                for key in ACTION_KEYS:
                    vals.append(float(rates.get(key, 0.0)))
    return vals


def mixture_l2_drift(
    a: dict[str, dict[str, dict[str, dict[str, float]]]],
    b: dict[str, dict[str, dict[str, dict[str, float]]]],
) -> float:
    """L2 distance between flattened fold/call/raise vectors."""
    va = _flatten_mixture_rates(a)
    vb = _flatten_mixture_rates(b)
    if not va and not vb:
        return 0.0
    if len(va) != len(vb):
        keys_a = _flatten_mixture_rates(a)
        keys_b = _flatten_mixture_rates(b)
        n = max(len(keys_a), len(keys_b))
        while len(va) < n:
            va.append(0.0)
        while len(vb) < n:
            vb.append(0.0)
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(va, vb)))
