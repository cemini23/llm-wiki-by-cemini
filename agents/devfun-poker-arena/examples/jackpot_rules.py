"""dev.fun Texas Hold'em jackpot rules (arena API + introspection).

GET /texas/jackpots?competitionId=… — public, no auth.

Official triggers (introspection 2026-06-08):
- RoyalFlush: fires at showdown with the qualifying hand unfolded.
- TwoSevenOffsuitBluff: uncontested pot — hero wins by folding everyone out
  while holding 7-2 offsuit.

S2 playground (cmq57o53r0bhw18g23qkydb08): 5× royal + 10× 27-bluff slots (MON).
"""
from __future__ import annotations

import os
from typing import Any, Optional

# Hand-class token for any 7-2 offsuit combo (_hand_class normalizes to 72o).
TWO_SEVEN_OFF_CLASS = "72o"

ROYAL_RULE = (
    "Royal flush jackpot fires only at showdown with the qualifying hand unfolded."
)
BLUFF_27_RULE = (
    "Offsuit 2-7 bluff jackpot fires when hero wins an uncontested pot by "
    "making everyone fold while holding 7-2 offsuit."
)


def royal_jackpot_enabled() -> bool:
    raw = os.environ.get("JACKPOT_ROYAL_ENABLED", "1").strip().lower()
    return raw in ("1", "true", "yes", "on")


def royal_showdown_mode() -> bool:
    """Prefer check/call/small bet so villains reach showdown (jackpot path)."""
    raw = os.environ.get("JACKPOT_ROYAL_SHOWDOWN", "1").strip().lower()
    return royal_jackpot_enabled() and raw in ("1", "true", "yes", "on")


def is_two_seven_offsuit_hand_class(hc: str) -> bool:
    return hc == TWO_SEVEN_OFF_CLASS


def summarize_jackpots(body: dict) -> dict[str, Any]:
    """Aggregate /texas/jackpots response for logging / monitor."""
    slots = body.get("jackpots") or []
    out: dict[str, Any] = {"total_slots": len(slots), "by_type": {}}
    for slot in slots:
        ht = str(slot.get("handType") or slot.get("fireType") or "unknown")
        bucket = out["by_type"].setdefault(
            ht,
            {"available": 0, "claimed": 0, "amounts": []},
        )
        status = str(slot.get("status") or "")
        if status == "Available":
            bucket["available"] += 1
        elif status == "Claimed":
            bucket["claimed"] += 1
        amt = slot.get("amount")
        if amt is not None:
            bucket["amounts"].append(amt)
    return out


def royal_showdown_action(
    table: dict,
    allowed: dict,
    available: list[str],
    pot: int,
    *,
    build_fn,
    binding: str,
    call_chips: int = 0,
) -> Optional[dict]:
    """Showdown-first line when hero has a made royal (jackpot > chip EV)."""
    label = "royal flush — showdown"

    if call_chips > 0:
        if "call" in available:
            return build_fn(
                "call", None, table, allowed, eq=0.99, po=0.0,
                msg=f"{binding}: {label} — call",
            )
        if allowed.get("canRaise") and "raise" in available:
            rr = allowed.get("raiseRange") or {}
            min_r = int(rr.get("min") or call_chips * 2)
            return build_fn(
                "raise", min_r, table, allowed, eq=0.99, po=0.0,
                msg=f"{binding}: {label} — min raise",
            )
        if allowed.get("canAllIn") and "all-in" in available:
            all_in_to = int(
                allowed.get("allInToAmount") or allowed.get("maxCommit") or 0
            )
            if all_in_to > 0:
                return build_fn(
                    "all-in", all_in_to, table, allowed, eq=0.99, po=0.0,
                    msg=f"{binding}: {label} — all-in",
                )

    if allowed.get("canCheck") and "check" in available:
        return build_fn(
            "check", None, table, allowed, eq=0.99, po=0.0,
            msg=f"{binding}: {label} — check",
        )

    if allowed.get("canBet") and "bet" in available:
        br = allowed.get("betRange") or {}
        min_bet = int(br.get("min") or max(int(pot * 0.25), 1))
        max_bet = int(br.get("max") or min_bet)
        target = max(min_bet, min(int(pot * 0.33), max_bet))
        return build_fn(
            "bet", target, table, allowed, eq=0.99, po=0.0,
            msg=f"{binding}: {label} — small value",
        )

    if allowed.get("canRaise") and "raise" in available:
        rr = allowed.get("raiseRange") or {}
        min_r = int(rr.get("min") or pot)
        max_r = int(rr.get("max") or min_r)
        target = max(min_r, min(int(pot * 0.33), max_r))
        return build_fn(
            "raise", target, table, allowed, eq=0.99, po=0.0,
            msg=f"{binding}: {label} — small raise",
        )

    if "call" in available:
        return build_fn(
            "call", None, table, allowed, eq=0.99, po=0.0,
            msg=f"{binding}: {label} — call",
        )
    return None
