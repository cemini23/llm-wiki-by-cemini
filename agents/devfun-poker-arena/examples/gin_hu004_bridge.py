"""Arena bridge for vendored gin/poker-bot hu004 (https://github.com/gin/poker-bot tree v3).

Loads vendor/gin_hu004/hu004.py in Daytona /assets/_vendor/gin_hu004 or local vendor/.
"""
from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path
from typing import Any, Optional

STRATEGY_NAME = os.environ.get("POKER_BOT_STRATEGY", "hu004")


def _hu004_module():
    env_path = os.environ.get("CEMINI_GIN_HU004_PATH", "").strip()
    candidates: list[Path] = []
    if env_path:
        candidates.append(Path(env_path))
    here = Path(__file__).resolve().parent
    candidates.extend(
        [
            here / "_vendor" / "gin_hu004" / "hu004.py",
            here.parent / "vendor" / "gin_hu004" / "hu004.py",
            here / "gin_hu004" / "hu004.py",
        ]
    )
    for path in candidates:
        if not path.is_file():
            continue
        mod_name = "_cemini_gin_hu004_vendored"
        spec = importlib.util.spec_from_file_location(mod_name, path)
        if spec is None or spec.loader is None:
            continue
        mod = importlib.util.module_from_spec(spec)
        sys.modules[mod_name] = mod
        spec.loader.exec_module(mod)
        return mod
    raise ImportError(
        "gin hu004 not found; run scripts/sync_gin_hu004.sh and rebuild sandbox bundle"
    )


def _hero_seat(table: dict) -> dict:
    self_num = table.get("selfSeatNumber")
    seats = table.get("seats") or []
    if self_num is not None:
        for seat in seats:
            if seat.get("seatNumber") == self_num:
                return seat
    acting_num = table.get("actingSeatNumber")
    if acting_num is not None:
        for seat in seats:
            if seat.get("seatNumber") == acting_num:
                return seat
    return seats[0] if seats else {}


def _clean_card(card: object) -> object:
    if isinstance(card, str):
        stripped = card.strip()
        if stripped.startswith("[") and stripped.endswith("]"):
            return stripped[1:-1]
    return card


def _normalize_table(table: dict) -> dict:
    normalized = dict(table)
    normalized["boardCards"] = [_clean_card(c) for c in (table.get("boardCards") or [])]
    seats = []
    for seat in table.get("seats") or []:
        ns = dict(seat)
        ns["holeCards"] = [_clean_card(c) for c in (seat.get("holeCards") or [])]
        seats.append(ns)
    normalized["seats"] = seats
    return normalized


def _reasoning(action: str, table: dict) -> str:
    board = table.get("boardCards") or []
    street = table.get("street") or "Preflop"
    seat = table.get("selfSeatNumber") or table.get("actingSeatNumber") or 0
    pos = "IP" if seat and int(seat) % 2 == 0 else "OOP"
    plan = {"Preflop": "ranges", "Flop": "spot", "Turn": "pressure", "River": "resolve"}
    pp = f"{pos} {plan.get(street, 'pot ctrl')}"[:30]
    if not board:
        bf = "[pf]"
    else:
        suits = [str(card)[-1].lower() for card in board]
        ranks = [str(card)[0].upper() for card in board]
        features = []
        for suit in set(suits):
            if suits.count(suit) >= 2:
                features.append(f"FD-{suit}")
        if len(set(ranks)) < len(ranks):
            features.append("paired")
        bf = "[" + ",".join(features[:3]) + "]" if features else "[dry]"
    parts = [
        f'vr: "{STRATEGY_NAME}"',
        f'ke: "legal {action}"',
        f"bf: {bf}",
        f'pp: "{pp}"',
    ]
    yaml = "{" + ", ".join(parts) + "}"
    if len(yaml) <= 150:
        return yaml
    return f'{{vr: "{STRATEGY_NAME}", ke: "legal", pp: "pot control"}}'


def _payload(action: str, amount: Optional[int], table: dict, message: str) -> dict[str, Any]:
    allowed = table.get("allowedActions") or {}
    available = allowed.get("availableActions") or []
    if action not in available and available:
        action = available[0]

    if action in {"fold", "check", "call"}:
        amount = None
    elif action == "all-in":
        amount = int(allowed.get("allInToAmount") or amount or 0)
    elif action == "raise":
        rr = allowed.get("raiseRange") or {}
        if rr:
            lo, hi = int(rr.get("min") or 1), int(rr.get("max") or int(amount or 1))
            amount = max(lo, min(int(amount or lo), hi))
        else:
            amount = int(amount or allowed.get("minRaiseTo") or 1)
    elif action == "bet":
        br = allowed.get("betRange") or {}
        if br:
            lo, hi = int(br.get("min") or 1), int(br.get("max") or int(amount or 1))
            amount = max(lo, min(int(amount or lo), hi))
        else:
            amount = int(amount or allowed.get("minBet") or 1)
    else:
        amount = None

    payload: dict[str, Any] = {
        "action": action,
        "message": (message or f"{STRATEGY_NAME} chose {action}")[:500],
        "reasoning": _reasoning(action, table),
        "reasoning_text": _reasoning(action, table),
    }
    if amount is not None:
        payload["amount"] = int(amount)
    return payload


def _deadline_fallback(table: dict) -> dict[str, Any]:
    allowed = table.get("allowedActions") or {}
    available = allowed.get("availableActions") or []
    for action in ("check", "call", "fold"):
        if action in available:
            return _payload(action, None, table, "deadline tight, safe legal fallback")
    if available:
        return _payload(available[0], None, table, "deadline tight, legal fallback")
    return _payload("fold", None, table, "no legal action available")


def decide(
    table: dict, deadline_s: float = 10.0, research_context: Optional[dict] = None
) -> dict[str, Any]:
    """Arena-compatible decide() using gin hu004 choose_action."""
    _ = research_context
    if deadline_s <= 2.2:
        return _deadline_fallback(table)

    mod = _hu004_module()
    choose_action = getattr(mod, "choose_action", None)
    if not callable(choose_action):
        raise ImportError("vendored hu004 missing choose_action()")

    normalized = _normalize_table(table)
    hero = _hero_seat(normalized)
    result = choose_action(normalized, hero)
    if result is None:
        return _deadline_fallback(table)
    if isinstance(result, dict):
        action = str(result.get("action") or "fold")
        return _payload(action, result.get("amount"), table, str(result.get("message") or STRATEGY_NAME))
    if not isinstance(result, (tuple, list)) or len(result) < 1:
        return _deadline_fallback(table)
    action = str(result[0] or "fold")
    amount = result[1] if len(result) > 1 else None
    message = str(result[2]) if len(result) > 2 else STRATEGY_NAME
    return _payload(action, amount, table, message)
