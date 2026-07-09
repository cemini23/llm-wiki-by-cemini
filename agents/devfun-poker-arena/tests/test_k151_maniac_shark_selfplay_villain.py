"""K151 maniac_shark selfplay villain — BOT_POOL + handle tagging."""
from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import MagicMock

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))
sys.path.insert(0, str(ROOT))

from selfplay import (  # noqa: E402
    BOT_POOL,
    bot_maniac_shark_lag,
    _opponents_for_selfplay,
)


def test_maniac_shark_in_bot_pool():
    assert "maniac_shark_lag" in BOT_POOL
    assert "maniac_shark_lite_2" in BOT_POOL
    assert BOT_POOL["maniac_shark_lite_2"] is bot_maniac_shark_lag


def test_maniac_shark_opponents_for_selfplay():
    bots = _opponents_for_selfplay(2, "maniac_shark_lag")
    assert len(bots) == 1
    assert bots[0] is bot_maniac_shark_lag


def test_maniac_shark_opens_measured_not_hyper():
    """LAG opens ~30% first-in — not hyper-maniac 72% bet frequency."""
    table = {
        "street": "Preflop",
        "potChips": 3,
        "bigBlindChips": 2,
        "allowedActions": {
            "availableActions": ["fold", "check", "raise"],
            "callChips": 0,
            "raiseRange": {"min": 4, "max": 200},
        },
        "seats": [],
        "selfSeatNumber": 1,
    }
    outs = [bot_maniac_shark_lag(table)["action"] for _ in range(80)]
    raise_n = sum(1 for a in outs if a == "raise")
    assert 10 <= raise_n <= 40, f"expected ~30% opens, got {raise_n}/80: {outs[:12]}"


def test_maniac_shark_folds_postflop_more_than_ten():
    table = {
        "street": "Flop",
        "potChips": 24,
        "bigBlindChips": 2,
        "allowedActions": {
            "availableActions": ["fold", "call", "raise"],
            "callChips": 10,
            "raiseRange": {"min": 20, "max": 200},
        },
    }
    outs = [bot_maniac_shark_lag(table)["action"] for _ in range(40)]
    assert outs.count("fold") >= 8
    assert outs.count("call") <= 28


def test_selfplay_tags_maniac_shark_handle(monkeypatch):
    monkeypatch.setenv("CEMINI_SELFPLAY_VILLAIN_HANDLE", "maniac_shark_lite_2")
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

    table = _build_table(
        state,
        hero_idx=0,
        table_id="t1",
        starting_stacks=[200, 200],
        small_blind=1,
        big_blind=2,
    )
    handles = {s["agentHandle"] for s in table["seats"]}
    assert "hero" in handles
    assert "maniac_shark_lite_2" in handles
