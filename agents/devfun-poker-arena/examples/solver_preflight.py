"""K244/K245 — clarify-before-solver preflight + redundant-dump skip.

Fail-open helpers for the Arena decide loop: report missing solver inputs
instead of launching heavy solver fan-out, and skip redundant table /
screenshot dumps after a consistent solver call.
"""
from __future__ import annotations

import hashlib
import json
import os
from typing import Any

MISSING_SCHEMA = "devfun.solver_preflight.v1"


def _hero_seat(table: dict) -> dict | None:
    if not isinstance(table, dict):
        return None
    seats = table.get("seats") or []
    if not seats:
        return None
    self_num = table.get("selfSeatNumber")
    if self_num is not None:
        for s in seats:
            if isinstance(s, dict) and s.get("seatNumber") == self_num:
                return s
        return None
    first = seats[0]
    return first if isinstance(first, dict) else None


def solver_inputs_ready(table_or_ctx: Any) -> list[str]:
    """Return list of missing solver inputs (empty list = ready).

    Checks street, stack/chips, and inference regime OR table format.
    Empty list means ready.
    """
    if not isinstance(table_or_ctx, dict):
        return ["street", "stack", "table_format"]
    table = table_or_ctx
    missing: list[str] = []
    if not (table.get("street") or table.get("round")):
        missing.append("street")
    hero = _hero_seat(table)
    if hero is None:
        missing.append("stack")
    if not (
        table.get("inference_regime")
        or table.get("tableFormat")
        or table.get("table_format")
    ):
        fmt = os.environ.get("CEMINI_TABLE_FORMAT", "").strip().lower()
        if not (fmt and fmt != "auto"):
            try:
                from table_format_utils import resolve_table_format

                resolve_table_format(table)
            except Exception:
                missing.append("table_format")
    return missing


def observation_hash(obs: Any) -> str:
    """Stable sha256 for an observation dict (fail-open)."""
    try:
        blob = json.dumps(obs, sort_keys=True, default=str)
    except Exception:
        blob = repr(obs)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def should_skip_redundant_table_dump(
    last_obs_hash: str,
    new_obs_hash: str,
    solver_ok: bool,
) -> bool:
    """After a successful solver call, skip redundant dump when unchanged."""
    return bool(solver_ok) and bool(last_obs_hash) and last_obs_hash == new_obs_hash


def preflight_skip_dict(missing: list[str]) -> dict:
    """Small skip dict for the compare harness (K244/K245)."""
    return {
        "solver_preflight": "skip",
        "missing": list(missing),
        "schema": MISSING_SCHEMA,
    }
