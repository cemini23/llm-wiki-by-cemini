"""HL auto-analyst runtime artifacts: kill switch, guards, style tweaks.

Written by `cemini_hl_auto_analyst.py` (30 min monitor). Read by lobby + decide().
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Optional

_EXAMPLES = Path(__file__).resolve().parent
_AGENT_DIR = _EXAMPLES.parent
_REPORTS = Path(
    os.environ.get("ARENA_MONITOR_REPORTS_DIR", str(_AGENT_DIR / "reports"))
)
_HL_DIR = _REPORTS / "hl-loop"

def _kill_switch_path() -> Path:
    return Path(
        os.environ.get("CEMINI_KILL_SWITCH_PATH", str(_AGENT_DIR / ".arena-kill-switch.json"))
    )


def _runtime_guards_path() -> Path:
    return Path(
        os.environ.get("CEMINI_RUNTIME_GUARDS_PATH", str(_HL_DIR / "runtime_guards.json"))
    )


def _style_overrides_path() -> Path:
    return Path(
        os.environ.get("CEMINI_STYLE_OVERRIDES_PATH", str(_HL_DIR / "style_overrides.json"))
    )


def _deploy_grace_path() -> Path:
    return Path(
        os.environ.get("CEMINI_DEPLOY_GRACE_PATH", str(_HL_DIR / "deploy_grace.json"))
    )


AUTO_ANALYST_STATE_PATH = _HL_DIR / "auto_analyst_state.json"

# Back-compat aliases (prefer env-aware helpers above in new code).
KILL_SWITCH_PATH = _kill_switch_path()
RUNTIME_GUARDS_PATH = _runtime_guards_path()
STYLE_OVERRIDES_PATH = _style_overrides_path()
DEPLOY_GRACE_PATH = _deploy_grace_path()

MAX_RUNTIME_GUARDS = int(os.environ.get("CEMINI_HL_MAX_GUARDS", "25"))
DEFAULT_DEPLOY_GRACE_HOURS = float(os.environ.get("CEMINI_HL_DEPLOY_GRACE_HOURS", "6"))
MAX_FOLD_SLACK_DELTA = float(os.environ.get("CEMINI_HL_MAX_FOLD_SLACK", "0.08"))
MAX_CALL_MARGIN_DELTA = float(os.environ.get("CEMINI_HL_MAX_CALL_MARGIN", "0.08"))
DEFAULT_SHOVE_COMMIT_RATIO = float(os.environ.get("CEMINI_HL_SHOVE_COMMIT_RATIO", "0.28"))
_PREMIUM_HANDS = frozenset({"AA", "KK", "QQ", "JJ", "TT", "AKs", "AKo", "AQs", "AQo"})


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _parse_utc(ts: str) -> datetime | None:
    if not ts:
        return None
    try:
        return datetime.fromisoformat(ts.replace("Z", "+00:00"))
    except ValueError:
        return None


def _deploy_grace_hours() -> float:
    raw = os.environ.get("CEMINI_HL_DEPLOY_GRACE_HOURS", "").strip()
    if not raw:
        return DEFAULT_DEPLOY_GRACE_HOURS
    try:
        return max(0.0, float(raw))
    except ValueError:
        return DEFAULT_DEPLOY_GRACE_HOURS


def load_deploy_grace() -> dict:
    data = _read_json(_deploy_grace_path(), {})
    return data if isinstance(data, dict) else {}


def record_deploy_grace(
    *,
    commit: str = "",
    round_num: int | None = None,
    hands: int | None = None,
    source: str = "deploy",
    grace_hours: float | None = None,
) -> dict:
    """Mark a code deploy — auto-analyst will not re-kill during grace window."""
    hours = _deploy_grace_hours() if grace_hours is None else max(0.0, grace_hours)
    deployed_at = datetime.now(timezone.utc)
    expires_at = deployed_at + timedelta(hours=hours)
    payload = {
        "deployed_at": deployed_at.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "expires_at": expires_at.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "grace_hours": hours,
        "commit": (commit or "unknown").strip() or "unknown",
        "source": source,
    }
    if round_num is not None:
        payload["round"] = int(round_num)
    if hands is not None:
        payload["hands"] = int(hands)
    _write_json(_deploy_grace_path(), payload)
    reset_style_overrides(source=source, commit=payload["commit"])
    repair_runtime_guards(source=source)
    return payload


def deploy_grace_status() -> dict:
    """Current deploy grace window, if any."""
    data = load_deploy_grace()
    if not data:
        return {"active": False}
    expires = _parse_utc(str(data.get("expires_at") or ""))
    if expires is None:
        return {"active": False, **data}
    now = datetime.now(timezone.utc)
    remaining_s = max(0.0, (expires - now).total_seconds())
    active = remaining_s > 0
    return {
        "active": active,
        "remaining_hours": round(remaining_s / 3600.0, 2),
        **data,
    }


def is_deploy_grace_active() -> bool:
    return bool(deploy_grace_status().get("active"))


def kill_switch_suppressed_by_deploy_grace() -> tuple[bool, str]:
    """True when auto-analyst must not activate kill switch (post-deploy soak)."""
    status = deploy_grace_status()
    if not status.get("active"):
        return False, ""
    commit = status.get("commit") or "unknown"
    expires = status.get("expires_at") or "?"
    remaining = status.get("remaining_hours")
    rem = f", {remaining}h left" if remaining is not None else ""
    return True, (
        f"deploy grace until {expires} (commit {commit}{rem}) — "
        "analyze may reflect pre-patch hands"
    )


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
    data = _read_json(_kill_switch_path(), {})
    return bool(isinstance(data, dict) and data.get("active"))


def kill_switch_status() -> dict:
    data = _read_json(_kill_switch_path(), {})
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
    _write_json(_kill_switch_path(), payload)
    return payload


def clear_kill_switch(*, reason: str = "operator clear", source: str = "operator") -> dict:
    payload = {
        "active": False,
        "cleared_at": _utc_now(),
        "cleared_by": source,
        "clear_reason": reason.strip() or "operator clear",
    }
    _write_json(_kill_switch_path(), payload)
    return payload


def load_runtime_guards() -> list[dict]:
    data = _read_json(_runtime_guards_path(), {})
    guards = data.get("guards") if isinstance(data, dict) else data
    if not isinstance(guards, list):
        return []
    return [g for g in guards if isinstance(g, dict)]


def load_style_overrides() -> dict:
    data = _read_json(_style_overrides_path(), {})
    return data if isinstance(data, dict) else {}


def merge_runtime_guards(new_guards: list[dict], *, source: str = "hl_auto_analyst") -> list[dict]:
    """Upsert guards by id; cap at MAX_RUNTIME_GUARDS (newest win)."""
    existing = {g.get("id"): g for g in load_runtime_guards() if g.get("id")}
    for g in new_guards:
        gid = g.get("id")
        if not gid:
            continue
        g = normalize_runtime_guard(dict(g))
        g.setdefault("added_at", _utc_now())
        g.setdefault("source", source)
        existing[gid] = g
    merged = list(existing.values())
    existing_ids = {g.get("id") for g in merged if g.get("id")}
    for g in list(merged):
        for comp in _shove_companion_guards(g):
            cid = comp.get("id")
            if cid and cid not in existing_ids:
                comp.setdefault("added_at", _utc_now())
                comp.setdefault("source", source)
                merged.append(comp)
                existing_ids.add(cid)
    merged.sort(key=lambda x: x.get("added_at") or "", reverse=True)
    merged = merged[:MAX_RUNTIME_GUARDS]
    _write_json(
        _runtime_guards_path(),
        {"updated_at": _utc_now(), "source": source, "guards": merged},
    )
    return merged


def _clamp_style_value(key: str, val: Any) -> Any:
    if key == "fold_slack_delta":
        return min(max(float(val), 0.0), MAX_FOLD_SLACK_DELTA)
    if key == "call_margin_delta":
        return min(max(float(val), 0.0), MAX_CALL_MARGIN_DELTA)
    if key == "join_retry_multiplier":
        return min(max(float(val), 1.0), 3.0)
    return val


def reset_style_overrides(*, source: str = "deploy", commit: str = "") -> dict:
    """Clear cumulative HL style deltas after a code deploy."""
    note = f"reset on deploy {commit}".strip() if commit else "reset on deploy"
    payload = {
        "fold_slack_delta": 0.0,
        "call_margin_delta": 0.0,
        "join_retry_multiplier": 1.0,
        "notes": note,
        "updated_at": _utc_now(),
        "source": source,
    }
    _write_json(_style_overrides_path(), payload)
    return payload


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
            if key in ("fold_slack_delta", "call_margin_delta", "join_retry_multiplier"):
                current[key] = _clamp_style_value(key, val)
            else:
                current[key] = val
    current["updated_at"] = _utc_now()
    current["source"] = source
    _write_json(_style_overrides_path(), current)
    return current


def _shove_commit_ratio(guard: dict) -> float:
    raw = guard.get("min_commit_ratio")
    if raw is not None:
        try:
            return max(0.0, float(raw))
        except (TypeError, ValueError):
            pass
    return DEFAULT_SHOVE_COMMIT_RATIO


def _commit_ratio(call_chips: int, hero_stack_chips: int) -> float:
    if call_chips <= 0 or hero_stack_chips <= 0:
        return 0.0
    return call_chips / hero_stack_chips


def _is_shove_leak_hand(hand_class: str) -> bool:
    """Hands that must not call large preflop commits (offsuit trash / low suited)."""
    hc = (hand_class or "").strip()
    if not hc or hc in _PREMIUM_HANDS:
        return False
    if hc.endswith("o"):
        return True
    if hc.endswith("s") and len(hc) == 3:
        ranks = "23456789TJQKA"
        try:
            return ranks.index(hc[0]) <= ranks.index("9") and ranks.index(hc[1]) <= ranks.index("9")
        except ValueError:
            return False
    return False


def normalize_runtime_guard(guard: dict) -> dict:
    """Enforce mutually exclusive guard predicates."""
    g = dict(guard)
    if g.get("when_facing_shove"):
        g["when_facing_bet"] = False
        g["when_opening"] = False
    elif g.get("when_opening"):
        g["when_facing_bet"] = False
        g["when_facing_shove"] = False
    elif g.get("when_facing_bet"):
        g["when_opening"] = False
    return g


def _shove_companion_guards(guard: dict) -> list[dict]:
    """Opening guards listing trash hands also need a vs-shove companion."""
    if not guard.get("when_opening"):
        return []
    gid = (guard.get("id") or "").strip()
    if not gid or gid.endswith("_vs_shove"):
        return []
    hands = [
        h for h in (guard.get("hand_classes") or [])
        if _is_shove_leak_hand(str(h))
    ]
    if not hands:
        return []
    return [normalize_runtime_guard({
        "id": f"{gid}_vs_shove",
        "street": guard.get("street") or "Preflop",
        "positions": list(guard.get("positions") or []),
        "hand_classes": hands,
        "when_facing_shove": True,
        "min_commit_ratio": DEFAULT_SHOVE_COMMIT_RATIO,
        "action": guard.get("action") or "fold",
        "reason": f"vs shove — companion to {gid}",
    })]


def repair_runtime_guards(*, source: str = "guard_repair") -> list[dict]:
    """Normalize guards and add missing vs-shove companions for opening rules."""
    guards = [normalize_runtime_guard(g) for g in load_runtime_guards()]
    existing_ids = {g.get("id") for g in guards if g.get("id")}
    extras: list[dict] = []
    for g in guards:
        for comp in _shove_companion_guards(g):
            if comp.get("id") not in existing_ids:
                extras.append(comp)
                existing_ids.add(comp["id"])
    merged = guards + extras
    merged.sort(key=lambda x: x.get("added_at") or "", reverse=True)
    merged = merged[:MAX_RUNTIME_GUARDS]
    _write_json(
        _runtime_guards_path(),
        {"updated_at": _utc_now(), "source": source, "guards": merged},
    )
    return merged


def _guard_matches(
    guard: dict,
    *,
    street: str,
    position: str,
    hand_class: str,
    call_chips: int,
    can_check: bool,
    hero_stack_chips: int = 0,
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
    if guard.get("when_facing_shove"):
        if call_chips <= 0:
            return False
        if _commit_ratio(call_chips, hero_stack_chips) < _shove_commit_ratio(guard):
            return False
    elif guard.get("when_facing_bet") and call_chips <= 0:
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
    hero_stack_chips: int = 0,
) -> Optional[dict]:
    for guard in load_runtime_guards():
        if _guard_matches(
            guard,
            street=street,
            position=position,
            hand_class=hand_class,
            call_chips=call_chips,
            can_check=can_check,
            hero_stack_chips=hero_stack_chips,
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
