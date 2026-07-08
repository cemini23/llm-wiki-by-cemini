"""K150 TEN selfplay villain — BOT_POOL + handle tagging."""
from __future__ import annotations

import os
import sys
from pathlib import Path
from unittest.mock import MagicMock

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))
sys.path.insert(0, str(ROOT))

from selfplay import BOT_POOL, bot_ten_wide_passive, _opponents_for_selfplay  # noqa: E402


def test_ten_in_bot_pool():
    assert "ten" in BOT_POOL
    assert "ten_wide_passive" in BOT_POOL
    assert BOT_POOL["ten"] is bot_ten_wide_passive


def test_ten_opponents_for_selfplay():
    bots = _opponents_for_selfplay(2, "ten")
    assert len(bots) == 1
    assert bots[0] is bot_ten_wide_passive


def test_ten_bot_limps_or_opens_preflop_free():
    """Facing check+raise available (SB open), TEN mostly continues."""
    table = {
        "street": "Preflop",
        "potChips": 3,
        "bigBlindChips": 2,
        "allowedActions": {
            "availableActions": ["fold", "call", "raise"],
            "callChips": 1,
            "raiseRange": {"min": 4, "max": 200},
        },
        "seats": [],
        "selfSeatNumber": 1,
    }
    # With call_chips>0 SB vs BB blinds, TEN should not always fold.
    outs = [bot_ten_wide_passive(table)["action"] for _ in range(40)]
    continue_n = sum(1 for a in outs if a in ("call", "raise"))
    assert continue_n >= 20, f"TEN too tight first-in: {outs[:10]}"


def test_ten_bot_calls_wide_facing_small_bet():
    table = {
        "street": "Flop",
        "potChips": 20,
        "bigBlindChips": 2,
        "allowedActions": {
            "availableActions": ["fold", "call", "raise"],
            "callChips": 8,
            "raiseRange": {"min": 16, "max": 200},
        },
    }
    outs = [bot_ten_wide_passive(table)["action"] for _ in range(30)]
    assert outs.count("call") >= 20


def test_selfplay_tags_ten_handle(monkeypatch):
    monkeypatch.setenv("CEMINI_SELFPLAY_VILLAIN_HANDLE", "TEN")
    # Minimal state mock shaped like pokerkit State enough for _build_table.
    from selfplay import _build_table  # noqa: WPS433

    state = MagicMock()
    state.actor_index = 0
    state.pots = []
    state.bets = [1, 2]
    state.stacks = [198, 198]
    state.hole_cards = [["As", "Kd"], ["7h", "2c"]]
    state.board_cards = []
    state.can_fold.return_value = True
    state.can_check_or_call.return_value = True
    state.checking_or_calling_amount = 1
    state.can_complete_bet_or_raise_to.return_value = False

    table = _build_table(state, hero_idx=0, table_id="t1", starting_stacks=[200, 200],
                         small_blind=1, big_blind=2)
    handles = {s["agentHandle"] for s in table["seats"]}
    assert "hero" in handles
    assert "TEN" in handles
