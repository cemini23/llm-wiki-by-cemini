"""K138 — AI_pokergame Hard-tier heuristic villain (read-only port).

MIT source: PENEEEEE732/AI_pokergame backend/app/poker/ai.py HardStrategy
Profile: config/villain_ai_pokergame_hard.yaml
"""
from __future__ import annotations

import random
from typing import Any

_RANKS = "23456789TJQKA"


def _rank(card: str) -> int:
    if not card:
        return 0
    ch = card[0].upper()
    return _RANKS.index(ch) if ch in _RANKS else 0


def hand_potential(hole: list[str]) -> float:
    """HardStrategy._evaluate_hand_potential (preflop-centric)."""
    if len(hole) < 2:
        return 0.0
    r1, r2 = _rank(hole[0]), _rank(hole[1])
    if r1 == r2:
        score = 0.6 + (r1 / 40.0)
    elif hole[0][-1] == hole[1][-1] and abs(r1 - r2) == 1:
        score = 0.5 + (max(r1, r2) / 100.0)
    elif r1 >= 10 and r2 >= 10:
        score = 0.5 + ((r1 + r2) / 100.0)
    else:
        score = (r1 + r2) / 50.0
    return min(score, 1.0)


def bot_ai_pokergame_hard(table: dict, **_: Any) -> dict:
    """Arena-table decide() for HardStrategy heuristics."""
    allowed = table.get("allowedActions") or {}
    avail = list(allowed.get("availableActions") or [])
    if not avail:
        return {"action": "fold"}

    call_chips = int(allowed.get("callChips") or 0)
    pot = int(table.get("potChips") or 0)
    self_seat_num = table.get("selfSeatNumber")
    seats = table.get("seats") or []
    self_seat = next((s for s in seats if s.get("seatNumber") == self_seat_num), {})
    hole = list(self_seat.get("holeCards") or [])
    stack = int(self_seat.get("stackChips") or self_seat.get("chips") or 0)

    potential = hand_potential(hole)
    pot_odds = call_chips / (pot + call_chips + 1) if call_chips > 0 else 0.0

    if call_chips > stack * 0.4 and potential < 0.85:
        return {"action": "fold"} if "fold" in avail else {"action": "check"}

    bb = int(table.get("bigBlindChips") or table.get("bigBlind") or 2)
    current_bet = int(table.get("currentBetChips") or table.get("currentBet") or call_chips)

    if potential > 0.7:
        if "raise" in avail and current_bet <= bb * 2:
            rr = allowed.get("raiseRange") or {}
            lo, hi = int(rr.get("min") or 1), int(rr.get("max") or 1)
            target = int(pot * 0.7) + current_bet
            target = max(lo, min(target, hi))
            return {"action": "raise", "amount": target}
        if "call" in avail:
            return {"action": "call"}
        if "check" in avail:
            return {"action": "check"}
        return {"action": "fold"}

    if potential > pot_odds:
        if "raise" in avail and random.random() < 0.2 and current_bet == 0:
            rr = allowed.get("raiseRange") or {}
            lo, hi = int(rr.get("min") or 1), int(rr.get("max") or 1)
            return {"action": "raise", "amount": max(lo, min(lo * 2, hi))}
        if "call" in avail:
            return {"action": "call"}
        if "check" in avail:
            return {"action": "check"}

    if "check" in avail:
        return {"action": "check"}
    return {"action": "fold"} if "fold" in avail else {"action": "call"}
