"""Table builders for jackpot_27_decide regression tests."""
from __future__ import annotations

from tests.helpers.cemini_tables import _allowed, six_max_table, mp_unopened, btn_tt_paired_river  # noqa: F401


def btn_72o_unopened(*, hero_hole: list[str] | None = None) -> dict:
    """BTN unopened — hunt spot vs blinds."""
    hole = hero_hole or ["7d", "2h"]
    return six_max_table(
        name="btn_72o_unopened",
        hero_seat=1,
        button_seat=1,
        street="Preflop",
        board=[],
        pot=30,
        hero_hole=hole,
        hero_stack=980,
        villain_bets={2: 10, 3: 20},
        allowed=_allowed(
            can_check=False,
            can_call=True,
            can_bet=True,
            call_chips=20,
            call_to=20,
            bet_range={"min": 40, "max": 980},
        ),
    )


def btn_72o_facing_raise(*, raise_to: int = 120) -> dict:
    """BTN facing CO open — abort hunt."""
    return six_max_table(
        name="btn_72o_facing_raise",
        hero_seat=1,
        button_seat=1,
        street="Preflop",
        board=[],
        pot=30 + raise_to,
        hero_hole=["7d", "2h"],
        hero_stack=960,
        hero_bet=0,
        villain_bets={6: raise_to},
        stacks={1: 960},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=raise_to,
            call_to=raise_to,
            raise_range={"min": raise_to * 2, "max": 960},
        ),
    )


def btn_72o_multiway_limp() -> dict:
    """BTN with two limpers — no hunt (3+ in pot)."""
    return six_max_table(
        name="btn_72o_multiway",
        hero_seat=1,
        button_seat=1,
        street="Preflop",
        board=[],
        pot=90,
        hero_hole=["7d", "2h"],
        hero_stack=960,
        hero_bet=0,
        villain_bets={2: 10, 3: 20, 4: 20, 5: 20, 6: 20},
        stacks={1: 960, 4: 980, 5: 980, 6: 980},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            can_bet=True,
            call_chips=20,
            call_to=20,
            bet_range={"min": 60, "max": 960},
        ),
        recent_events=[],
    )
