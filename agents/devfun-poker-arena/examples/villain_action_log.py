"""P2-5 villain action sketch — append-only jsonl, fail-open.

Rows: {handle, street, action, spot}. No range_ledger ML — just a cheap
per-handle action history to compute open% by handle offline.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

_OPEN_ACTIONS = frozenset({"raise", "open"})
_ACTION_STREET_PREFLOP = ("preflop", "pre-flop", "")


def villain_actions_path() -> Path | None:
    """Resolve villain-actions jsonl — CEMINI_VILLAIN_ACTIONS_LOG_PATH or export dir."""
    raw = os.environ.get("CEMINI_VILLAIN_ACTIONS_LOG_PATH", "").strip()
    if raw:
        return Path(raw)
    export = os.environ.get("CEMINI_EXPORT_DIR", "").strip()
    if export:
        return Path(export) / "villain_actions.jsonl"
    return None


def log_villain_action(
    handle: str,
    *,
    street: str,
    action: str,
    spot: str = "",
) -> None:
    """Fail-open append to villain_actions.jsonl. Never raises."""
    try:
        path = villain_actions_path()
        if path is None or not handle:
            return
        path.parent.mkdir(parents=True, exist_ok=True)
        row = {
            "handle": str(handle).strip(),
            "street": str(street or "").strip(),
            "action": str(action or "").strip(),
            "spot": str(spot or "").strip(),
            "agent_version": os.environ.get("AGENT_VERSION", ""),
        }
        with path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(row, separators=(",", ":")) + "\n")
    except Exception:
        pass


def open_pct_by_handle(path: str | Path) -> dict[str, float]:
    """Preflop open rate per handle: raise rows / preflop action rows."""
    counts: dict[str, list[int]] = {}
    p = Path(path)
    if not p.exists():
        return {}
    with p.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except Exception:
                continue
            handle = str(row.get("handle") or "").strip()
            if not handle:
                continue
            street = str(row.get("street") or "").strip().lower()
            if street not in _ACTION_STREET_PREFLOP:
                continue
            action = str(row.get("action") or "").strip().lower()
            slot = counts.setdefault(handle, [0, 0])
            slot[1] += 1
            if action in _OPEN_ACTIONS:
                slot[0] += 1
    out: dict[str, float] = {}
    for handle, (opens, total) in counts.items():
        out[handle] = opens / total if total else 0.0
    return out
