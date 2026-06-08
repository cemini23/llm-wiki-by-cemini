"""HL auto-analyst runtime artifacts: kill switch, guards, style tweaks.

Written by `cemini_hl_auto_analyst.py` (30 min monitor). Read by lobby + decide().
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

_EXAMPLES = Path(__file__).resolve().parent
_AGENT_DIR = _EXAMPLES.parent
_REPORTS = Path(
    os.environ.get("ARENA_MONITOR_REPORTS_DIR", str(_AGENT_DIR / "reports"))
)
_HL_DIR = _REPORTS / "hl-loop"

KILL_SWITCH_PATH = Path(
    os.environ.get("CEMINI_KILL_SWITCH_PATH", str(_AGENT_DIR / ".arena-kill-switch.json"))
)
RUNTIME_GUARDS_PATH = Path(
    os.environ.get("CEMINI_RUNTIME_GUARDS_PATH", str(_HL_DIR / "runtime_guards.json"))
)
STYLE_OVERRIDES_PATH = Path(
    os.environ.get("CEMINI_STYLE_OVERRIDES_PATH", str(_HL_DIR / "style_overrides.json"))
)
AUTO_ANALYST_STATE_PATH = _HL_DIR / "auto_analyst_state.json"

MAX_RUNTIME_GUARDS = int(os.environ.get("CEMINI_HL_MAX_GUARDS", "25"))


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _read_json(path: Path, default: Any) -> Any:
    if not path.is_file():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def _write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def is_kill_switch_active() -> bool:
    data = _read_json(KILL_SWITCH_PATH, {})
    return bool(isinstance(data, dict) and data.get("active"))


def kill_switch_status() -> dict:
    data = _read_json(KILL_SWITCH_PATH, {})
    if not isinstance(data, dict):
        return {"active": False}
    return data


def activate_kill_switch(*, reason: str, severity: str = "catastrophic", source: str = "operator") -> dict:
    payload = {
        "active": True,
        "reason": reason.strip() or "unspecified",
        "severity": severity,
        "activated_at": _utc_now(),
        "activated_by": source,
    }
    _write_json(KILL_SWITCH_PATH, payload)
    return payload


def clear_kill_switch(*, reason: str = "operator clear", source: str = "operator") -> dict:
    payload = {
        "active": False,
        "cleared_at": _utc_now(),
        "cleared_by": source,
        "clear_reason": reason.strip() or "operator clear",
    }
    _write_json(KILL_SWITCH_PATH, payload)
    return payload


def load_runtime_guards() -> list[dict]:
    data = _read_json(RUNTIME_GUARDS_PATH, {})
    guards = data.get("guards") if isinstance(data, dict) else data
    if not isinstance(guards, list):
        return []
    return [g for g in guards if isinstance(g, dict)]


def load_style_overrides() -> dict:
    data = _read_json(STYLE_OVERRIDES_PATH, {})
    return data if isinstance(data, dict) else {}


def merge_runtime_guards(new_guards: list[dict], *, source: str = "hl_auto_analyst") -> list[dict]:
    """Upsert guards by id; cap at MAX_RUNTIME_GUARDS (newest win)."""
    existing = {g.get("id"): g for g in load_runtime_guards() if g.get("id")}
    for g in new_guards:
        gid = g.get("id")
        if not gid:
            continue
        g = dict(g)
        g.setdefault("added_at", _utc_now())
        g.setdefault("source", source)
        existing[gid] = g
    merged = list(existing.values())
    merged.sort(key=lambda x: x.get("added_at") or "", reverse=True)
    merged = merged[:MAX_RUNTIME_GUARDS]
    _write_json(
        RUNTIME_GUARDS_PATH,
        {"updated_at": _utc_now(), "source": source, "guards": merged},
    )
    return merged


def apply_style_overrides(tweaks: dict, *, source: str = "hl_auto_analyst") -> dict:
    allowed_keys = {
        "fold_slack_delta",
        "call_margin_delta",
        "open_steal_equity_min",
        "join_retry_multiplier",
        "notes",
    }
    current = load_style_overrides()
    for key, val in tweaks.items():
        if key in allowed_keys and val is not None:
            current[key] = val
    current["updated_at"] = _utc_now()
    current["source"] = source
    _write_json(STYLE_OVERRIDES_PATH, current)
    return current


def _guard_matches(
    guard: dict,
    *,
    street: str,
    position: str,
    hand_class: str,
    call_chips: int,
    can_check: bool,
) -> bool:
    g_street = (guard.get("street") or "").strip()
    if g_street and g_street.lower() != street.lower():
        return False
    positions = guard.get("positions") or []
    if positions and position not in positions:
        return False
    hand_classes = guard.get("hand_classes") or []
    if hand_classes and hand_class not in hand_classes:
        return False
    if guard.get("when_facing_bet") and call_chips <= 0:
        return False
    if guard.get("when_opening") and call_chips > 0:
        return False
    if guard.get("require_can_check") and not can_check:
        return False
    return True


def match_runtime_guard(
    *,
    street: str,
    position: str,
    hand_class: str,
    call_chips: int,
    can_check: bool,
) -> Optional[dict]:
    for guard in load_runtime_guards():
        if _guard_matches(
            guard,
            street=street,
            position=position,
            hand_class=hand_class,
            call_chips=call_chips,
            can_check=can_check,
        ):
            return guard
    return None


def apply_runtime_guard_action(
    guard: dict,
    *,
    table: dict,
    allowed: dict,
    available: list,
    equity: float,
    pot_odds: float,
    build_fn,
) -> Optional[dict]:
    action = (guard.get("action") or "fold").lower()
    reason = guard.get("reason") or guard.get("id") or "runtime_guard"
    msg = f"hl_guard: {reason}"
    if action == "fold" and "fold" in available:
        return build_fn("fold", None, table, allowed, eq=equity, po=pot_odds, msg=msg)
    if action == "check" and allowed.get("canCheck") and "check" in available:
        return build_fn("check", None, table, allowed, eq=equity, po=pot_odds, msg=msg)
    if action == "fold" and allowed.get("canCheck") and "check" in available:
        return build_fn("check", None, table, allowed, eq=equity, po=pot_odds, msg=msg)
    return None


def kill_switch_action(
    *,
    table: dict,
    allowed: dict,
    available: list,
    equity: float,
    pot_odds: float,
    build_fn,
) -> Optional[dict]:
    if allowed.get("canCheck") and "check" in available:
        return build_fn(
            "check", None, table, allowed, eq=equity, po=pot_odds,
            msg="kill_switch: survival check",
        )
    if "fold" in available:
        return build_fn(
            "fold", None, table, allowed, eq=equity, po=pot_odds,
            msg="kill_switch: survival fold",
        )
    return None
