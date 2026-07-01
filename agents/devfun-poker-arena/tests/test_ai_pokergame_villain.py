"""Smoke tests for K138 AI_pokergame Hard villain port."""
from __future__ import annotations

from ai_pokergame_villain import bot_ai_pokergame_hard, hand_potential


def test_hand_potential_pair() -> None:
    assert hand_potential(["Ah", "Ad"]) >= 0.89


def test_bot_returns_legal_action_preflop() -> None:
    table = {
        "selfSeatNumber": 2,
        "potChips": 3,
        "bigBlindChips": 2,
        "currentBetChips": 2,
        "allowedActions": {
            "availableActions": ["fold", "call", "raise"],
            "callChips": 1,
            "raiseRange": {"min": 4, "max": 200},
        },
        "seats": [
            {"seatNumber": 1, "stackChips": 200, "holeCards": []},
            {"seatNumber": 2, "stackChips": 199, "holeCards": ["7h", "2c"]},
        ],
    }
    out = bot_ai_pokergame_hard(table)
    assert out["action"] in ("fold", "call", "raise", "check")
