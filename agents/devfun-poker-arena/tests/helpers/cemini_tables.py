"""Build Arena-shaped table dicts for cemini decide() regression tests.

The starter kit's `examples/testing.py` uses HU tables with seat 1 = hero
and no button — fine for smoke tests, but it hides position/HUD/multi-way
bugs that burned chips in Playground (74o MP, cold-start steals, etc.).
"""
from __future__ import annotations

from typing import Any, Optional


def _seat(
    num: int,
    *,
    agent_id: str = "villain",
    hole: list[str] | None = None,
    stack: int = 1000,
    bet: int = 0,
    committed: int = 0,
    position: str | None = None,
    training_archetype: str | None = None,
) -> dict:
    s: dict[str, Any] = {
        "seatId": f"s{num}",
        "seatNumber": num,
        "agentId": agent_id,
        "agentName": agent_id,
        "agentHandle": agent_id,
        "status": "Active",
        "stackChips": stack,
        "currentBetChips": bet,
        "totalCommittedChips": committed,
        "payoutChips": None,
        "holeCards": hole,
    }
    if position:
        s["position"] = position
    if training_archetype:
        s["trainingArchetype"] = training_archetype
    return s


def _allowed(
    *,
    can_fold: bool = True,
    can_check: bool = False,
    can_call: bool = False,
    can_bet: bool = False,
    can_raise: bool = False,
    can_all_in: bool = True,
    call_chips: int = 0,
    call_to: int = 0,
    bet_range: dict | None = None,
    raise_range: dict | None = None,
    all_in_to: int = 1000,
    max_commit: int = 1000,
) -> dict:
    available: list[str] = []
    if can_fold:
        available.append("fold")
    if can_check:
        available.append("check")
    if can_call:
        available.append("call")
    if can_bet:
        available.append("bet")
    if can_raise:
        available.append("raise")
    if can_all_in:
        available.append("all-in")
    return {
        "canFold": can_fold,
        "canCheck": can_check,
        "canCall": can_call,
        "canBet": can_bet,
        "canRaise": can_raise,
        "canAllIn": can_all_in,
        "callAmount": call_chips,
        "callChips": call_chips,
        "callToAmount": call_to,
        "maxCommit": max_commit,
        "allInToAmount": all_in_to,
        "betRange": bet_range,
        "raiseRange": raise_range,
        "availableActions": available,
        "amountSemantics": "toAmount",
    }


def six_max_table(
    *,
    name: str,
    hero_seat: int,
    button_seat: int,
    street: str,
    board: list[str],
    pot: int,
    hero_hole: list[str],
    hero_stack: int,
    allowed: dict,
    hero_bet: int = 0,
    villain_bets: dict[int, int] | None = None,
    stacks: dict[int, int] | None = None,
    competition_id: str = "regression-local",
    recent_events: list[dict] | None = None,
) -> dict:
    """6-max table with explicit button + hero seat (Playground-shaped)."""
    villain_bets = villain_bets or {}
    stacks = stacks or {}
    seats = []
    for num in range(1, 7):
        is_hero = num == hero_seat
        seats.append(
            _seat(
                num,
                agent_id="hero" if is_hero else f"bot_{num}",
                hole=hero_hole if is_hero else None,
                stack=stacks.get(num, hero_stack if is_hero else 1000),
                bet=villain_bets.get(num, hero_bet if is_hero else 0),
                training_archetype="rock" if num != hero_seat and num in (2, 5) else "maniac",
            )
        )
    return {
        "id": f"tbl_{name}",
        "tableId": f"tbl_{name}",
        "competitionId": competition_id,
        "status": "Active",
        "street": street,
        "potChips": pot,
        "boardCards": board,
        "smallBlindChips": 10,
        "bigBlindChips": 20,
        "buttonSeatNumber": button_seat,
        "selfSeatNumber": hero_seat,
        "actingSeatNumber": hero_seat,
        "seats": seats,
        "allowedActions": allowed,
        "recentEvents": recent_events or [],
    }


def hu_table(
    *,
    name: str,
    hero_seat: int,
    street: str,
    board: list[str],
    pot: int,
    hero_hole: list[str],
    hero_stack: int,
    allowed: dict,
    hero_bet: int = 0,
    villain_bets: dict[int, int] | None = None,
    stacks: dict[int, int] | None = None,
    button_seat: int = 1,
    competition_id: str = "regression-hu",
    recent_events: list[dict] | None = None,
) -> dict:
    """Heads-up table — seat 1 = BTN/SB, seat 2 = BB (Challenge-shaped)."""
    villain_bets = villain_bets or {}
    stacks = stacks or {}
    seats = []
    for num in range(1, 3):
        is_hero = num == hero_seat
        seats.append(
            _seat(
                num,
                agent_id="hero" if is_hero else "villain",
                hole=hero_hole if is_hero else None,
                stack=stacks.get(num, hero_stack if is_hero else 200),
                bet=villain_bets.get(num, hero_bet if is_hero else 0),
                training_archetype="tight" if num != hero_seat else None,
            )
        )
    return {
        "id": f"tbl_hu_{name}",
        "tableId": f"tbl_hu_{name}",
        "competitionId": competition_id,
        "status": "Active",
        "street": street,
        "potChips": pot,
        "boardCards": board,
        "smallBlindChips": 1,
        "bigBlindChips": 2,
        "buttonSeatNumber": button_seat,
        "selfSeatNumber": hero_seat,
        "actingSeatNumber": hero_seat,
        "maxPlayers": 2,
        "seats": seats,
        "allowedActions": allowed,
        "recentEvents": recent_events or [],
    }


def hu_btn_vs_shove(
    hero_hole: list[str], *, shove_to: int = 95, hero_stack: int = 100
) -> dict:
    """HU BTN/SB facing BB shove — R34 AJo leak shape."""
    return hu_table(
        name="btn_vs_shove",
        hero_seat=1,
        street="Preflop",
        board=[],
        pot=3 + shove_to,
        hero_hole=hero_hole,
        hero_stack=hero_stack,
        hero_bet=1,
        villain_bets={1: 1, 2: shove_to},
        stacks={1: hero_stack, 2: shove_to},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            can_all_in=True,
            call_chips=shove_to - 1,
            call_to=shove_to,
            all_in_to=hero_stack,
        ),
    )


def hu_sb_unopened(hero_hole: list[str], *, hero_stack: int = 198) -> dict:
    """HU SB first-in — should open premium, fold trash."""
    return hu_table(
        name="sb_unopened",
        hero_seat=1,
        street="Preflop",
        board=[],
        pot=3,
        hero_hole=hero_hole,
        hero_stack=hero_stack,
        hero_bet=1,
        villain_bets={1: 1, 2: 2},
        stacks={1: hero_stack, 2: 198},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            can_raise=True,
            call_chips=1,
            call_to=2,
            raise_range={"min": 4, "max": hero_stack},
        ),
    )


def hu_bb_vs_minraise(hero_hole: list[str], *, raise_to: int = 6, hero_stack: int = 194) -> dict:
    """HU BB facing BTN min-raise — defend discipline."""
    return hu_table(
        name="bb_vs_minraise",
        hero_seat=2,
        street="Preflop",
        board=[],
        pot=3 + raise_to,
        hero_hole=hero_hole,
        hero_stack=hero_stack,
        hero_bet=2,
        villain_bets={1: raise_to, 2: 2},
        stacks={1: 194, 2: hero_stack},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            can_raise=True,
            call_chips=raise_to - 2,
            call_to=raise_to,
            raise_range={"min": raise_to * 2, "max": hero_stack},
        ),
    )


def mp_unopened(hero_hole: list[str], *, equity_boost: bool = False) -> dict:
    """Hero MP, 6-max, unopened pot — classic 74o leak spot."""
    # seat layout: BTN=1, SB=2, BB=3, UTG=4, MP=5, CO=6
    return six_max_table(
        name="mp_unopened",
        hero_seat=5,
        button_seat=1,
        street="Preflop",
        board=[],
        pot=30,
        hero_hole=hero_hole,
        hero_stack=980,
        hero_bet=0,
        villain_bets={2: 10, 3: 20},
        allowed=_allowed(
            can_check=False,
            can_call=True,
            can_raise=True,
            call_chips=20,
            call_to=20,
            raise_range={"min": 60, "max": 980},
        ),
    )


def utg_a7s_ace_high_turn_r33(*, villain_bet: int = 233, pot: int = 500) -> dict:
    """A7s UTG ace-high turn — HL R33 #01."""
    return six_max_table(
        name="utg_a7s_ace_high_turn_r33",
        hero_seat=4,
        button_seat=1,
        street="Turn",
        board=["6d", "4s", "Th", "2h"],
        pot=pot,
        hero_hole=["As", "7s"],
        hero_stack=400,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={4: 400},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def utg_77_paired_river_r33(*, villain_bet: int = 78, pot: int = 200) -> dict:
    """77 UTG underpair paired — HL R33 #02."""
    return six_max_table(
        name="utg_77_paired_river_r33",
        hero_seat=4,
        button_seat=1,
        street="River",
        board=["Ts", "Jh", "3d", "3c", "4d"],
        pot=pot,
        hero_hole=["7d", "7c"],
        hero_stack=200,
        hero_bet=0,
        villain_bets={6: villain_bet},
        stacks={4: 200},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def utg_q6_kk_flop_r33(*, villain_bet: int = 41, pot: int = 120) -> dict:
    """Q6s UTG air on KK flop — HL R33 #05."""
    return six_max_table(
        name="utg_q6_kk_flop_r33",
        hero_seat=4,
        button_seat=1,
        street="Flop",
        board=["Ks", "Kd", "3c"],
        pot=pot,
        hero_hole=["Qh", "6h"],
        hero_stack=300,
        hero_bet=0,
        villain_bets={6: villain_bet},
        stacks={4: 300},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def mp_j3_weak_top_r33(*, villain_bet: int = 40, pot: int = 150) -> dict:
    """J3s MP weak top pair — HL R33 #06."""
    return six_max_table(
        name="mp_j3_weak_top_r33",
        hero_seat=5,
        button_seat=1,
        street="River",
        board=["Jd", "8d", "7c", "Kd", "As"],
        pot=pot,
        hero_hole=["Js", "3s"],
        hero_stack=200,
        hero_bet=0,
        villain_bets={6: villain_bet},
        stacks={5: 200},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def utg_unopened(hero_hole: list[str]) -> dict:
    """Hero UTG first to act (after blinds)."""
    return six_max_table(
        name="utg_unopened",
        hero_seat=4,
        button_seat=1,
        street="Preflop",
        board=[],
        pot=30,
        hero_hole=hero_hole,
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


def utg_a3s_paired_river(*, villain_bet: int = 400, pot: int = 900) -> dict:
    """A3s UTG OOP on double-paired runout — HL R9 analyze #01 (−887)."""
    return six_max_table(
        name="utg_a3s_paired_river",
        hero_seat=4,
        button_seat=1,
        street="River",
        board=["6s", "Jc", "5s", "Js", "5c"],
        pot=pot,
        hero_hole=["As", "3s"],
        hero_stack=450,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={4: 450},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def utg_94s_paired_river(*, villain_bet: int = 400, pot: int = 800) -> dict:
    """94s UTG OOP on double-paired broadway runout — HL R10 analyze #02 (−100)."""
    return six_max_table(
        name="utg_94s_paired_river",
        hero_seat=4,
        button_seat=1,
        street="River",
        board=["Ad", "Qd", "Kd", "Qc", "Kh"],
        pot=pot,
        hero_hole=["4d", "9d"],
        hero_stack=500,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={4: 500},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def co_t3s_paired_turn(*, villain_bet: int = 300, pot: int = 600) -> dict:
    """T3s CO OOP on paired 88 + ace turn — HL R10 analyze #10 (−100)."""
    return six_max_table(
        name="co_t3s_paired_turn",
        hero_seat=6,
        button_seat=1,
        street="Turn",
        board=["8d", "8s", "Ac"],
        pot=pot,
        hero_hole=["Tc", "3s"],
        hero_stack=600,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={6: 600},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def utg_facing_raise(hero_hole: list[str], *, raise_to: int = 60) -> dict:
    """Hero UTG facing a standard open from CO."""
    return six_max_table(
        name="utg_facing_raise",
        hero_seat=4,
        button_seat=1,
        street="Preflop",
        board=[],
        pot=30 + raise_to,
        hero_hole=hero_hole,
        hero_stack=980,
        villain_bets={6: raise_to},
        allowed=_allowed(
            can_call=True,
            can_raise=True,
            call_chips=raise_to,
            call_to=raise_to,
            raise_range={"min": raise_to * 2, "max": 980},
        ),
    )


def mp_facing_raise(hero_hole: list[str], *, raise_to: int = 60) -> dict:
    """Hero MP facing an UTG/early open."""
    return six_max_table(
        name="mp_facing_raise",
        hero_seat=5,
        button_seat=1,
        street="Preflop",
        board=[],
        pot=30 + raise_to,
        hero_hole=hero_hole,
        hero_stack=980,
        villain_bets={4: raise_to},
        allowed=_allowed(
            can_call=True,
            can_raise=True,
            call_chips=raise_to,
            call_to=raise_to,
            raise_range={"min": raise_to * 2, "max": 980},
        ),
    )


def co_first_in_raise_only(hero_hole: list[str]) -> dict:
    """CO first-in when Arena exposes raise but not bet (K118 selfplay/Arena shape)."""
    return six_max_table(
        name="co_raise_only_open",
        hero_seat=6,
        button_seat=1,
        street="Preflop",
        board=[],
        pot=30,
        hero_hole=hero_hole,
        hero_stack=980,
        villain_bets={2: 10, 3: 20},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            can_raise=True,
            call_chips=20,
            call_to=20,
            raise_range={"min": 40, "max": 980},
        ),
    )


def co_unopened(hero_hole: list[str]) -> dict:
    """CO unopened pot — 98o open leak (HL R11 #01)."""
    return six_max_table(
        name="co_unopened",
        hero_seat=6,
        button_seat=1,
        street="Preflop",
        board=[],
        pot=30,
        hero_hole=hero_hole,
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


def co_facing_raise(hero_hole: list[str], *, raise_to: int = 60) -> dict:
    """CO facing MP open — 98o defend leak (HL R11 #01)."""
    return six_max_table(
        name="co_facing_raise",
        hero_seat=6,
        button_seat=1,
        street="Preflop",
        board=[],
        pot=30 + raise_to,
        hero_hole=hero_hole,
        hero_stack=960,
        hero_bet=0,
        villain_bets={5: raise_to},
        stacks={6: 960},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            can_raise=True,
            call_chips=raise_to,
            call_to=raise_to,
            raise_range={"min": raise_to * 2, "max": 960},
        ),
    )


def co_unopened_steal_vs_rock(hero_hole: list[str]) -> dict:
    """CO unopened — J2o HUD steal leak."""
    return six_max_table(
        name="co_steal_rock",
        hero_seat=6,
        button_seat=1,
        street="Preflop",
        board=[],
        pot=30,
        hero_hole=hero_hole,
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


def ep_oop_postflop_weak(
    hero_hole: list[str],
    board: list[str],
    *,
    hero_seat: int = 5,
    villain_bet: int = 120,
    pot: int = 240,
) -> dict:
    """MP/UTG OOP facing ~50% pot with a weak hand."""
    return six_max_table(
        name="ep_oop_weak",
        hero_seat=hero_seat,
        button_seat=1,
        street="Flop",
        board=board,
        pot=pot,
        hero_hole=hero_hole,
        hero_stack=500,
        hero_bet=0,
        villain_bets={3: villain_bet},
        stacks={hero_seat: 500},
        allowed=_allowed(
            can_call=True,
            can_raise=True,
            call_chips=villain_bet,
            call_to=villain_bet,
            raise_range={"min": villain_bet * 2, "max": 500},
        ),
    )


def sb_facing_open(hero_hole: list[str], *, raise_to: int = 60) -> dict:
    """SB facing BTN open — 83o complete/call leak."""
    return six_max_table(
        name="sb_facing_open",
        hero_seat=2,
        button_seat=1,
        street="Preflop",
        board=[],
        pot=30 + raise_to,
        hero_hole=hero_hole,
        hero_stack=990,
        hero_bet=10,
        villain_bets={1: raise_to},
        stacks={2: 990},
        allowed=_allowed(
            can_call=True,
            can_raise=True,
            call_chips=raise_to - 10,
            call_to=raise_to,
            raise_range={"min": raise_to * 2, "max": 990},
        ),
    )


def bb_facing_raise(hero_hole: list[str], *, raise_to: int = 60) -> dict:
    """BB facing CO/BTN open — Q6o defend leak (analyze round 4 #02)."""
    return six_max_table(
        name="bb_facing_raise",
        hero_seat=3,
        button_seat=1,
        street="Preflop",
        board=[],
        pot=30 + raise_to,
        hero_hole=hero_hole,
        hero_stack=940,
        hero_bet=20,
        villain_bets={5: raise_to},
        stacks={3: 940},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            can_raise=True,
            call_chips=raise_to - 20,
            call_to=raise_to,
            raise_range={"min": raise_to * 2, "max": 940},
        ),
    )


def co_63s_paired_river(*, villain_bet: int = 100, pot: int = 220) -> dict:
    """63s CO IP on double-paired runout — HL R23 analyze #01 (−100)."""
    return six_max_table(
        name="co_63s_paired_river",
        hero_seat=6,
        button_seat=1,
        street="River",
        board=["7s", "5s", "5h", "3h", "Js"],
        pot=pot,
        hero_hole=["6c", "3s"],
        hero_stack=400,
        hero_bet=0,
        villain_bets={5: villain_bet},
        stacks={6: 400},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def co_22_paired_river(*, villain_bet: int = 3, pot: int = 20) -> dict:
    """22 CO IP on double-paired ace runout — HL S2 R1 analyze #01 (−9)."""
    return six_max_table(
        name="co_22_paired_river",
        hero_seat=5,
        button_seat=6,
        street="River",
        board=["8c", "5h", "Ad", "8h", "As"],
        pot=pot,
        hero_hole=["2d", "2c"],
        hero_stack=400,
        hero_bet=0,
        villain_bets={6: villain_bet},
        stacks={5: 400},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def co_72o_paired_river(*, villain_bet: int = 50, pot: int = 150) -> dict:
    """72o CO IP on paired runout — HL R6 analyze #01."""
    return six_max_table(
        name="co_72o_paired_river",
        hero_seat=6,
        button_seat=1,
        street="River",
        board=["3d", "3c", "Ts", "Jh", "6h"],
        pot=pot,
        hero_hole=["7d", "2s"],
        hero_stack=500,
        hero_bet=0,
        villain_bets={5: villain_bet},
        stacks={6: 500},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def co_j2o_paired_river(*, villain_bet: int = 400, pot: int = 1200) -> dict:
    """J2o CO bottom pair on paired runout — HL R13 analyze #01 (−2072)."""
    return six_max_table(
        name="co_j2o_paired_river",
        hero_seat=6,
        button_seat=1,
        street="River",
        board=["Kc", "Ah", "Td", "2h", "2s"],
        pot=pot,
        hero_hole=["Jd", "2d"],
        hero_stack=800,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={6: 800},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            can_raise=True,
            call_chips=villain_bet,
            call_to=villain_bet,
            raise_range={"min": villain_bet * 2, "max": 800},
        ),
    )


def bb_t2s_facing_open(*, raise_to: int = 60) -> dict:
    """T2s BB vs open — HL R6 analyze #05."""
    return bb_facing_raise(["Ts", "2s"], raise_to=raise_to)


def bb_j8s_k65_flop(*, villain_bet: int = 55, pot: int = 115) -> dict:
    """J8s BB OOP unpaired on K65 vs c-bet — HL R7 analyze #01."""
    return six_max_table(
        name="bb_j8s_k65_flop",
        hero_seat=3,
        button_seat=1,
        street="Flop",
        board=["Ks", "6d", "5h"],
        pot=pot,
        hero_hole=["8s", "Js"],
        hero_stack=950,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={3: 950},
        allowed=_allowed(
            can_call=True,
            can_raise=True,
            call_chips=villain_bet,
            call_to=villain_bet,
            raise_range={"min": villain_bet * 2, "max": 400},
        ),
    )


def co_t5o_river(*, villain_bet: int = 100, pot: int = 200) -> dict:
    """T5o CO OOP weak top pair vs river bet — analyze round 4 #12."""
    return six_max_table(
        name="co_t5o_river",
        hero_seat=5,
        button_seat=1,
        street="River",
        board=["Tc", "2s", "6h", "Qs", "7h"],
        pot=pot,
        hero_hole=["Ts", "5h"],
        hero_stack=800,
        hero_bet=0,
        villain_bets={4: villain_bet},
        stacks={5: 800},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def sb_qq_connected_river(*, river_bet: int = 450, pot: int = 900) -> dict:
    """QQ SB OOP on 8J376 connected runout — HL R12 analyze #01 (−1000)."""
    return six_max_table(
        name="sb_qq_connected_river",
        hero_seat=2,
        button_seat=1,
        street="River",
        board=["8s", "Jc", "3c", "7h", "6c"],
        pot=pot,
        hero_hole=["Qh", "Qs"],
        hero_stack=500,
        hero_bet=0,
        villain_bets={1: river_bet},
        stacks={2: 500},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            can_raise=True,
            call_chips=river_bet,
            call_to=river_bet,
            raise_range={"min": river_bet * 2, "max": 500},
        ),
    )


def sb_a9s_paired_river(*, villain_bet: int = 400, pot: int = 600) -> dict:
    """A9s SB OOP on paired runout — HL R5 analyze #01 (−492)."""
    return six_max_table(
        name="sb_a9s_paired_river",
        hero_seat=2,
        button_seat=1,
        street="River",
        board=["7s", "Jc", "Jh", "Ks", "Ac"],
        pot=pot,
        hero_hole=["9s", "As"],
        hero_stack=500,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={2: 500},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def btn_facing_shove(hero_hole: list[str], *, shove_to: int = 1329, hero_stack: int = 1329) -> dict:
    """BTN facing preflop shove — HL R32 A9o −1329."""
    return six_max_table(
        name="btn_facing_shove",
        hero_seat=5,
        button_seat=1,
        street="Preflop",
        board=[],
        pot=30 + shove_to,
        hero_hole=hero_hole,
        hero_stack=hero_stack,
        hero_bet=0,
        villain_bets={6: shove_to},
        stacks={5: hero_stack},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            can_all_in=True,
            call_chips=shove_to,
            call_to=shove_to,
            all_in_to=hero_stack,
        ),
    )


def btn_k6_aa_board_r32(*, villain_bet: int = 334, pot: int = 700) -> dict:
    """K6 BTN on double-ace board — HL R32 #03."""
    return six_max_table(
        name="btn_k6_aa_board_r32",
        hero_seat=5,
        button_seat=1,
        street="Turn",
        board=["As", "Ad", "9d", "3s"],
        pot=pot,
        hero_hole=["6c", "Kh"],
        hero_stack=400,
        hero_bet=0,
        villain_bets={6: villain_bet},
        stacks={5: 400},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def btn_k3_top_pair_flop_r32(*, villain_bet: int = 22, pot: int = 60) -> dict:
    """K3 BTN top pair weak kicker flop — HL R32 #12."""
    return six_max_table(
        name="btn_k3_top_pair_flop_r32",
        hero_seat=5,
        button_seat=1,
        street="Flop",
        board=["3h", "5d", "Kc"],
        pot=pot,
        hero_hole=["Kh", "3s"],
        hero_stack=200,
        hero_bet=0,
        villain_bets={6: villain_bet},
        stacks={5: 200},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def btn_t9_paired_board_r32(*, villain_bet: int = 220, pot: int = 500) -> dict:
    """T9 BTN on paired 8s — HL R32 #04."""
    return six_max_table(
        name="btn_t9_paired_board_r32",
        hero_seat=5,
        button_seat=1,
        street="River",
        board=["9s", "6c", "8h", "8s", "Js"],
        pot=pot,
        hero_hole=["9d", "Tc"],
        hero_stack=300,
        hero_bet=0,
        villain_bets={6: villain_bet},
        stacks={5: 300},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def co_facing_shove(hero_hole: list[str], *, shove_to: int = 1000, hero_stack: int = 1000) -> dict:
    """CO facing large preflop shove — HL R5 QTo leak."""
    return six_max_table(
        name="co_facing_shove",
        hero_seat=6,
        button_seat=1,
        street="Preflop",
        board=[],
        pot=30 + shove_to,
        hero_hole=hero_hole,
        hero_stack=hero_stack,
        hero_bet=0,
        villain_bets={5: shove_to},
        stacks={6: hero_stack},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            can_all_in=True,
            call_chips=shove_to,
            call_to=shove_to,
            all_in_to=hero_stack,
        ),
    )


def mp_facing_shove(hero_hole: list[str], *, shove_to: int = 1000, hero_stack: int = 1000) -> dict:
    """MP facing large preflop shove — HL R5 Q9o leak."""
    return six_max_table(
        name="mp_facing_shove",
        hero_seat=5,
        button_seat=1,
        street="Preflop",
        board=[],
        pot=30 + shove_to,
        hero_hole=hero_hole,
        hero_stack=hero_stack,
        hero_bet=0,
        villain_bets={4: shove_to},
        stacks={5: hero_stack},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            can_all_in=True,
            call_chips=shove_to,
            call_to=shove_to,
            all_in_to=hero_stack,
        ),
    )


def sb_63s_broadway_river(*, villain_bet: int = 60, pot: int = 200) -> dict:
    """63s SB OOP on broadway river — HL R4 analyze #01 (−100)."""
    return six_max_table(
        name="sb_63s_broadway_river",
        hero_seat=2,
        button_seat=1,
        street="River",
        board=["Qs", "Jc", "2c", "Ts", "Kh"],
        pot=pot,
        hero_hole=["3d", "6s"],
        hero_stack=400,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={2: 400},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def sb_a6o_vs_shove(*, shove_to: int = 1000, hero_stack: int = 1000) -> dict:
    """A6o SB facing preflop stack-off — HL R4 analyze #02."""
    return six_max_table(
        name="sb_a6o_vs_shove",
        hero_seat=2,
        button_seat=1,
        street="Preflop",
        board=[],
        pot=30 + shove_to,
        hero_hole=["As", "6h"],
        hero_stack=hero_stack,
        hero_bet=0,
        villain_bets={1: shove_to},
        stacks={2: hero_stack},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            can_all_in=True,
            call_chips=shove_to,
            call_to=shove_to,
            all_in_to=hero_stack,
        ),
    )


def sb_k4o_flop_r26(*, villain_bet: int = 12, pot: int = 40) -> dict:
    """K4o SB missed flop — HL R26 #01 (−6 on 9d3hQc)."""
    return six_max_table(
        name="sb_k4o_flop_r26",
        hero_seat=2,
        button_seat=1,
        street="Flop",
        board=["9d", "3h", "Qc"],
        pot=pot,
        hero_hole=["4d", "Kd"],
        hero_stack=200,
        hero_bet=0,
        villain_bets={3: villain_bet},
        stacks={2: 200},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def sb_t7s_paired_flop(*, villain_bet: int = 45, pot: int = 90) -> dict:
    """T7s SB on paired 88 flop — HL R19 analyze #01 (−45)."""
    return six_max_table(
        name="sb_t7s_paired_flop",
        hero_seat=2,
        button_seat=1,
        street="Flop",
        board=["8s", "5c", "8h"],
        pot=pot,
        hero_hole=["7c", "Tc"],
        hero_stack=200,
        hero_bet=0,
        villain_bets={3: villain_bet},
        stacks={2: 200},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def mp_j9o_turn_facing_bet(*, villain_bet: int = 45, pot: int = 180) -> dict:
    """J9o MP OOP turn top pair — K5J6 (HL R37 #01)."""
    return six_max_table(
        name="mp_j9o_turn_facing_bet",
        hero_seat=5,
        button_seat=1,
        street="Turn",
        board=["Ks", "5h", "Jc", "6d"],
        pot=pot,
        hero_hole=["9c", "Js"],
        hero_stack=400,
        hero_bet=0,
        villain_bets={4: villain_bet},
        stacks={5: 400},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def utg_jts_paired_turn(*, villain_bet: int = 30, pot: int = 80) -> dict:
    """JTs UTG on paired 5443 turn — HL R19 analyze #02 (−30)."""
    return six_max_table(
        name="utg_jts_paired_turn",
        hero_seat=0,
        button_seat=5,
        street="Turn",
        board=["5h", "4h", "4c", "3h"],
        pot=pot,
        hero_hole=["Td", "Jd"],
        hero_stack=250,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={0: 250},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def co_t4o_broadway_flop(*, villain_bet: int = 10, pot: int = 40) -> dict:
    """T4o CO flop top pair weak kicker — HL R18 analyze #02 (−10 on TQ6)."""
    return six_max_table(
        name="co_t4o_broadway_flop",
        hero_seat=6,
        button_seat=1,
        street="Flop",
        board=["Td", "Qh", "6h"],
        pot=pot,
        hero_hole=["4d", "Ts"],
        hero_stack=300,
        hero_bet=0,
        villain_bets={5: villain_bet},
        stacks={6: 300},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def co_a8o_paired_river(*, villain_bet: int = 100, pot: int = 200) -> dict:
    """A8o CO ace-high on paired runout — HL R16 analyze #01 (−100 on 9669JQh)."""
    return six_max_table(
        name="co_a8o_paired_river",
        hero_seat=6,
        button_seat=1,
        street="River",
        board=["9d", "6h", "9h", "Jh", "Qh"],
        pot=pot,
        hero_hole=["Ac", "8c"],
        hero_stack=300,
        hero_bet=0,
        villain_bets={5: villain_bet},
        stacks={6: 300},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def co_ato_paired_river(*, villain_bet: int = 80, pot: int = 240) -> dict:
    """ATo CO OOP on paired river — HL R4 analyze #03 (−100)."""
    return six_max_table(
        name="co_ato_paired_river",
        hero_seat=6,
        button_seat=1,
        street="River",
        board=["Jc", "Qs", "7h", "Kc", "7c"],
        pot=pot,
        hero_hole=["Th", "Ad"],
        hero_stack=400,
        hero_bet=0,
        villain_bets={5: villain_bet},
        stacks={6: 400},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def co_q7o_paired_river(*, villain_bet: int = 400, pot: int = 520) -> dict:
    """Q7o CO OOP on paired runout — HL R11 bust #01 (−747)."""
    return six_max_table(
        name="co_q7o_paired_river",
        hero_seat=6,
        button_seat=1,
        street="River",
        board=["3h", "Th", "7d", "3s", "8c"],
        pot=pot,
        hero_hole=["7h", "Qh"],
        hero_stack=787,
        hero_bet=0,
        villain_bets={5: villain_bet},
        stacks={6: 787},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def sb_95s_paired_river(*, villain_bet: int = 50, pot: int = 180) -> dict:
    """95s SB OOP on ace-paired runout — HL S2 R3 analyze #01 (−100)."""
    return six_max_table(
        name="sb_95s_paired_river",
        hero_seat=2,
        button_seat=1,
        street="River",
        board=["Ah", "6h", "Qd", "Qc", "As"],
        pot=pot,
        hero_hole=["9s", "5s"],
        hero_stack=400,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={2: 400},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def btn_facing_shove(hero_hole: list[str], *, shove_to: int = 1000, hero_stack: int = 1000) -> dict:
    """BTN facing large preflop shove — HL S2 R3 −100 cluster."""
    return six_max_table(
        name="btn_facing_shove",
        hero_seat=1,
        button_seat=1,
        street="Preflop",
        board=[],
        pot=30 + shove_to,
        hero_hole=hero_hole,
        hero_stack=hero_stack,
        hero_bet=0,
        villain_bets={4: shove_to},
        stacks={1: hero_stack},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            can_all_in=True,
            call_chips=shove_to,
            call_to=shove_to,
            all_in_to=hero_stack,
        ),
    )


def btn_a9s_vs_shove_r25(*, shove_to: int = 674, hero_stack: int = 842) -> dict:
    """A9s BTN vs stack-off — S2 HL R25 #01 (−674 preflop)."""
    return btn_facing_shove(["9h", "Ah"], shove_to=shove_to, hero_stack=hero_stack)


def sb_jj_paired_river(*, river_bet: int = 120, pot: int = 280) -> dict:
    """JJ SB OOP on paired runout — analyze #01 leak."""
    return six_max_table(
        name="sb_jj_paired_river",
        hero_seat=2,
        button_seat=1,
        street="River",
        board=["Ks", "6d", "2c", "Ts", "2s"],
        pot=pot,
        hero_hole=["Js", "Jc"],
        hero_stack=400,
        hero_bet=0,
        villain_bets={1: river_bet},
        stacks={2: 400},
        allowed=_allowed(
            can_call=True,
            can_raise=True,
            call_chips=river_bet,
            call_to=river_bet,
            raise_range={"min": river_bet * 2, "max": 400},
        ),
    )


def bb_ako_vulnerable_flop(*, villain_bet: int = 55, pot: int = 170) -> dict:
    """AKo BB OOP TPTK on AJ4 — HL R10 analyze #01 (−116)."""
    return six_max_table(
        name="bb_ako_vulnerable_flop",
        hero_seat=3,
        button_seat=1,
        street="Flop",
        board=["Ad", "4c", "Jh"],
        pot=pot,
        hero_hole=["Kh", "As"],
        hero_stack=900,
        hero_bet=0,
        villain_bets={5: villain_bet},
        stacks={3: 900},
        allowed=_allowed(
            can_call=True,
            can_raise=True,
            call_chips=villain_bet,
            call_to=villain_bet,
            raise_range={"min": villain_bet * 2, "max": 900},
        ),
    )


def sb_k2o_three_flush_river(*, villain_bet: int = 120, pot: int = 280) -> dict:
    """K2o SB OOP top pair weak kicker on three-flush — HL R24 analyze #01."""
    return six_max_table(
        name="sb_k2o_three_flush_river",
        hero_seat=2,
        button_seat=1,
        street="River",
        board=["Kh", "7h", "Tc", "Qc", "6h"],
        pot=pot,
        hero_hole=["Kc", "2d"],
        hero_stack=800,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={2: 800},
        allowed=_allowed(
            can_call=True,
            can_raise=True,
            call_chips=villain_bet,
            call_to=villain_bet,
            raise_range={"min": villain_bet * 2, "max": 800},
        ),
    )


def sb_98s_missed_ace_flop(*, villain_bet: int = 30, pot: int = 70) -> dict:
    """98s SB OOP missed on A-high flop — HL R21 #01 (−25)."""
    return six_max_table(
        name="sb_98s_missed_ace_flop",
        hero_seat=2,
        button_seat=1,
        street="Flop",
        board=["Ac", "Qs", "6s"],
        pot=pot,
        hero_hole=["9c", "8c"],
        hero_stack=900,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={2: 900},
        allowed=_allowed(
            can_call=True,
            can_raise=True,
            call_chips=villain_bet,
            call_to=villain_bet,
            raise_range={"min": villain_bet * 2, "max": 900},
        ),
    )


def btn_97o_unopened(hero_hole: list[str] | None = None) -> dict:
    """97o BTN unopened — HL R21 #03."""
    hole = hero_hole or ["7s", "9c"]
    return six_max_table(
        name="btn_97o_unopened",
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


def utg_a8o_ace_high_river(*, villain_bet: int = 50, pot: int = 150) -> dict:
    """A8o UTG OOP ace-high river — HL R21 #02."""
    return six_max_table(
        name="utg_a8o_ace_high_river",
        hero_seat=4,
        button_seat=1,
        street="River",
        board=["6c", "9d", "Qc", "Th", "2h"],
        pot=pot,
        hero_hole=["Ah", "8d"],
        hero_stack=850,
        hero_bet=0,
        villain_bets={6: villain_bet},
        stacks={4: 850},
        allowed=_allowed(
            can_call=True,
            can_raise=True,
            call_chips=villain_bet,
            call_to=villain_bet,
            raise_range={"min": villain_bet * 2, "max": 850},
        ),
    )


def sb_a3o_ace_high_river(*, villain_bet: int = 120, pot: int = 400) -> dict:
    """A3o SB OOP ace-high only on connected runout — HL R20 #01 (−355)."""
    return six_max_table(
        name="sb_a3o_ace_high_river",
        hero_seat=2,
        button_seat=1,
        street="River",
        board=["Ts", "7h", "Qh", "Kc", "8c"],
        pot=pot,
        hero_hole=["Ah", "3d"],
        hero_stack=600,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={2: 600},
        allowed=_allowed(
            can_call=True,
            can_raise=True,
            call_chips=villain_bet,
            call_to=villain_bet,
            raise_range={"min": villain_bet * 2, "max": 600},
        ),
    )


def sb_a8o_tptk_flop(*, villain_bet: int = 40, pot: int = 120) -> dict:
    """A8o SB OOP top pair weak kicker — analyze #03."""
    return six_max_table(
        name="sb_a8o_tptk_flop",
        hero_seat=2,
        button_seat=1,
        street="Flop",
        board=["6h", "Jh", "8h"],
        pot=pot,
        hero_hole=["8c", "Ad"],
        hero_stack=900,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={2: 900},
        allowed=_allowed(
            can_call=True,
            can_raise=True,
            call_chips=villain_bet,
            call_to=villain_bet,
            raise_range={"min": villain_bet * 2, "max": 900},
        ),
    )


def sb_22_overcard_turn(*, villain_bet: int = 70, pot: int = 200) -> dict:
    """22 SB OOP under overcards — analyze #09."""
    return six_max_table(
        name="sb_22_overcard_turn",
        hero_seat=2,
        button_seat=1,
        street="Turn",
        board=["7d", "Ac", "4c", "8s"],
        pot=pot,
        hero_hole=["2s", "2d"],
        hero_stack=800,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={2: 800},
        allowed=_allowed(
            can_call=True,
            can_raise=True,
            call_chips=villain_bet,
            call_to=villain_bet,
            raise_range={"min": villain_bet * 2, "max": 800},
        ),
    )


def btn_tt_paired_river(*, villain_bet: int = 115, pot: int = 320) -> dict:
    """TT BTN IP underpair on paired runout — HL R8 analyze #01 (−115)."""
    return six_max_table(
        name="btn_tt_paired_river",
        hero_seat=1,
        button_seat=1,
        street="River",
        board=["6d", "Jh", "Js", "As", "8c"],
        pot=pot,
        hero_hole=["Th", "Td"],
        hero_stack=400,
        hero_bet=0,
        villain_bets={3: villain_bet},
        stacks={1: 400},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def btn_q9o_vs_limp(*, call_chips: int = 20) -> dict:
    """Q9o BTN facing multiway limp — HL R20 analyze #01 (−100 on 682 flop)."""
    return six_max_table(
        name="btn_q9o_vs_limp",
        hero_seat=6,
        button_seat=6,
        street="Preflop",
        board=[],
        pot=30 + call_chips * 2,
        hero_hole=["9c", "Qs"],
        hero_stack=980,
        villain_bets={2: 10, 3: call_chips, 4: call_chips, 5: 10},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            can_bet=True,
            call_chips=call_chips,
            call_to=call_chips,
            bet_range={"min": call_chips * 2, "max": 980},
        ),
    )


def btn_q6o_flop_j74(*, villain_bet: int = 40, pot: int = 120) -> dict:
    """Q6o BTN flop air — J74 c-bet (HL R36 #02)."""
    return six_max_table(
        name="btn_q6o_flop_j74",
        hero_seat=6,
        button_seat=6,
        street="Flop",
        board=["4s", "Jc", "7c"],
        pot=pot,
        hero_hole=["Qc", "6h"],
        hero_stack=900,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={6: 900},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def utg_j4s_flop_tk8(*, villain_bet: int = 50, pot: int = 120) -> dict:
    """J4s UTG flop junk — Th Kc 8d (HL R36 #04)."""
    return six_max_table(
        name="utg_j4s_flop_tk8",
        hero_seat=2,
        button_seat=6,
        street="Flop",
        board=["Th", "Kc", "8d"],
        pot=pot,
        hero_hole=["Jc", "4s"],
        hero_stack=900,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={2: 900},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def btn_q9o_flop_facing_bet(*, villain_bet: int = 100, pot: int = 120) -> dict:
    """Q9o BTN IP on 682 — air vs flop bet after limp (HL R20 #01)."""
    return six_max_table(
        name="btn_q9o_flop_facing_bet",
        hero_seat=6,
        button_seat=6,
        street="Flop",
        board=["6s", "8h", "2c"],
        pot=pot,
        hero_hole=["9c", "Qs"],
        hero_stack=900,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={6: 900},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def btn_unopened_cold_start(hero_hole: list[str]) -> dict:
    """BTN unopened — cold-start chart steal block (98s HL R21)."""
    return six_max_table(
        name="btn_unopened_cold",
        hero_seat=1,
        button_seat=1,
        street="Preflop",
        board=[],
        pot=30,
        hero_hole=hero_hole,
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


def co_q5o_vs_limp(*, call_chips: int = 20) -> dict:
    """CO Q5o facing multiway limp — HL R21 mirror of R20 BTN guard."""
    return six_max_table(
        name="co_q5o_vs_limp",
        hero_seat=6,
        button_seat=1,
        street="Preflop",
        board=[],
        pot=30 + call_chips * 2,
        hero_hole=["5c", "Qd"],
        hero_stack=980,
        villain_bets={2: 10, 3: call_chips, 4: call_chips, 5: 10},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            can_bet=True,
            call_chips=call_chips,
            call_to=call_chips,
            bet_range={"min": call_chips * 2, "max": 980},
        ),
    )


def sb_72o_vs_limp(*, complete_chips: int = 10) -> dict:
    """SB 72o vs limpers — never complete (HL R21)."""
    return six_max_table(
        name="sb_72o_vs_limp",
        hero_seat=2,
        button_seat=1,
        street="Preflop",
        board=[],
        pot=30 + 20 + 20,
        hero_hole=["7c", "2d"],
        hero_stack=990,
        hero_bet=10,
        villain_bets={4: 20, 5: 20},
        stacks={2: 990},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            can_raise=True,
            call_chips=complete_chips,
            call_to=20,
            raise_range={"min": 60, "max": 990},
        ),
    )


def sb_nemesis_facing_open(
    hero_hole: list[str],
    *,
    nemesis_handle: str = "hunterguy102",
    raise_to: int = 60,
) -> dict:
    """SB vs nemesis BTN open — tight defend (A5s fold HL R21)."""
    table = six_max_table(
        name="sb_nemesis_open",
        hero_seat=2,
        button_seat=1,
        street="Preflop",
        board=[],
        pot=30 + raise_to,
        hero_hole=hero_hole,
        hero_stack=990,
        hero_bet=10,
        villain_bets={1: raise_to},
        stacks={2: 990},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            can_raise=True,
            call_chips=raise_to - 10,
            call_to=raise_to,
            raise_range={"min": raise_to * 2, "max": 990},
        ),
    )
    for seat in table["seats"]:
        if seat["seatNumber"] == 1:
            seat["agentHandle"] = nemesis_handle
            seat["agentName"] = nemesis_handle
            seat["agentId"] = nemesis_handle
    return table


def btn_qto_flush_river(*, villain_bet: int = 130, pot: int = 300) -> dict:
    """QTo BTN IP second pair on three-flush runout — analyze #01."""
    return six_max_table(
        name="btn_qto_flush_river",
        hero_seat=1,
        button_seat=1,
        street="River",
        board=["2s", "Kd", "Qd", "6h", "5d"],
        pot=pot,
        hero_hole=["Td", "Qs"],
        hero_stack=700,
        hero_bet=0,
        villain_bets={3: villain_bet},
        stacks={1: 700},
        allowed=_allowed(
            can_call=True,
            can_raise=True,
            call_chips=villain_bet,
            call_to=villain_bet,
            raise_range={"min": villain_bet * 2, "max": 700},
        ),
    )


def mp_a9o_second_pair_river(*, villain_bet: int = 100, pot: int = 200) -> dict:
    """A9o MP OOP second pair vs river bet — HL R9 analyze #14 (−100)."""
    return six_max_table(
        name="mp_a9o_second_pair_river",
        hero_seat=5,
        button_seat=1,
        street="River",
        board=["Ts", "9s", "3c", "7c", "2s"],
        pot=pot,
        hero_hole=["Ad", "9d"],
        hero_stack=500,
        hero_bet=0,
        villain_bets={3: villain_bet},
        stacks={5: 500},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def co_99_ace_paired_river(*, villain_bet: int = 400, pot: int = 900) -> dict:
    """99 CO on ace-paired runout — Fable audit: CO leg was dead (not in_position)."""
    return six_max_table(
        name="co_99_ace_paired_river",
        hero_seat=6,
        button_seat=1,
        street="River",
        board=["As", "7s", "2s", "Ac", "6c"],
        pot=pot,
        hero_hole=["9c", "9s"],
        hero_stack=448,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={6: 448},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def bb_kk_low_straight_river(*, villain_bet: int = 800, pot: int = 1200) -> dict:
    """KK on 86532 — HL R15 export #01 (−1132)."""
    return six_max_table(
        name="bb_kk_low_straight_river",
        hero_seat=3,
        button_seat=1,
        street="River",
        board=["8s", "6h", "5d", "3d", "2s"],
        pot=pot,
        hero_hole=["Kc", "Kd"],
        hero_stack=1132,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={3: 1132},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def bb_kqs_paired_river(*, villain_bet: int = 51, pot: int = 120) -> dict:
    """KQs BB on paired runout — HL R15 analyze #01 (−51 on 249443)."""
    return six_max_table(
        name="bb_kqs_paired_river",
        hero_seat=3,
        button_seat=1,
        street="River",
        board=["2s", "4d", "9h", "4c", "3h"],
        pot=pot,
        hero_hole=["Kh", "Qh"],
        hero_stack=200,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={3: 200},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def bb_55_ace_river(*, villain_bet: int = 225, pot: int = 500) -> dict:
    """55 BB on ace-high river — HL R14 analyze #01 (−225 on 2c7hAsT9d)."""
    return six_max_table(
        name="bb_55_ace_river",
        hero_seat=3,
        button_seat=1,
        street="River",
        board=["2c", "7h", "As", "Ts", "9d"],
        pot=pot,
        hero_hole=["5h", "5s"],
        hero_stack=225,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={3: 225},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def co_55_paired_river_r31(*, villain_bet: int = 110, pot: int = 280) -> dict:
    """55 CO on paired runout — HL R31 #02 (−110 on Td Qc 3c 3s 8s)."""
    return six_max_table(
        name="co_55_paired_river_r31",
        hero_seat=6,
        button_seat=1,
        street="River",
        board=["Td", "Qc", "3c", "3s", "8s"],
        pot=pot,
        hero_hole=["5c", "5s"],
        hero_stack=200,
        hero_bet=0,
        villain_bets={5: villain_bet},
        stacks={6: 200},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def co_77_overcard_river_r31(*, villain_bet: int = 50, pot: int = 150) -> dict:
    """77 CO under J/K board — HL R31 #04."""
    return six_max_table(
        name="co_77_overcard_river_r31",
        hero_seat=6,
        button_seat=1,
        street="River",
        board=["Js", "Kd", "8d", "3c", "2d"],
        pot=pot,
        hero_hole=["7c", "7d"],
        hero_stack=200,
        hero_bet=0,
        villain_bets={5: villain_bet},
        stacks={6: 200},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def co_t9_kq_river_r31(*, villain_bet: int = 118, pot: int = 350) -> dict:
    """T9d CO on K+Q runout — HL R31 #01."""
    return six_max_table(
        name="co_t9_kq_river_r31",
        hero_seat=6,
        button_seat=1,
        street="River",
        board=["2c", "5h", "Qc", "Kd", "4c"],
        pot=pot,
        hero_hole=["Td", "9d"],
        hero_stack=300,
        hero_bet=0,
        villain_bets={5: villain_bet},
        stacks={6: 300},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def btn_t7_paired_river_r31(*, villain_bet: int = 30, pot: int = 90) -> dict:
    """T7 BTN on paired 9s — HL R31 #08."""
    return six_max_table(
        name="btn_t7_paired_river_r31",
        hero_seat=5,
        button_seat=1,
        street="River",
        board=["9d", "Ks", "9s", "8c", "Td"],
        pot=pot,
        hero_hole=["Th", "7c"],
        hero_stack=150,
        hero_bet=0,
        villain_bets={6: villain_bet},
        stacks={5: 150},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def co_66_ace_river(*, villain_bet: int = 250, pot: int = 550) -> dict:
    """66 CO on ace-high river — HL R13 export #02 (−292 on Js9hAh4h7c)."""
    return six_max_table(
        name="co_66_ace_river",
        hero_seat=6,
        button_seat=1,
        street="River",
        board=["Js", "9h", "Ah", "4h", "7c"],
        pot=pot,
        hero_hole=["6d", "6h"],
        hero_stack=292,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={6: 292},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def mp_ak_paired_river(*, villain_bet: int = 500, pot: int = 1100) -> dict:
    """AK MP on paired runout — HL R13 analyze #01 (−624 on 8Ah4434)."""
    return six_max_table(
        name="mp_ak_paired_river",
        hero_seat=5,
        button_seat=1,
        street="River",
        board=["8c", "Ah", "4s", "3s", "4c"],
        pot=pot,
        hero_hole=["Ac", "Kc"],
        hero_stack=624,
        hero_bet=0,
        villain_bets={6: villain_bet},
        stacks={5: 624},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def mp_ak_river_stackoff_r24(*, villain_bet: int = 2200, pot: int = 3000) -> dict:
    """AK MP OOP single pair vs stack-off — HL R24 #01 (−2203 on Qh8d3d2cKd)."""
    return six_max_table(
        name="mp_ak_river_stackoff_r24",
        hero_seat=5,
        button_seat=1,
        street="River",
        board=["Qh", "8d", "3d", "2c", "Kd"],
        pot=pot,
        hero_hole=["Ac", "Kc"],
        hero_stack=2203,
        hero_bet=0,
        villain_bets={6: villain_bet},
        stacks={5: 2203},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            can_all_in=True,
            call_chips=villain_bet,
            call_to=villain_bet,
            all_in_to=2203,
        ),
    )


def btn_99_paired_river_stackoff_r25(*, villain_bet: int = 574, pot: int = 900) -> dict:
    """99 BTN IP single pair vs stack-off — S1 bust −574 on KsQh3h3cTd."""
    return six_max_table(
        name="btn_99_paired_river_stackoff_r25",
        hero_seat=1,
        button_seat=1,
        street="River",
        board=["Ks", "Qh", "3h", "3c", "Td"],
        pot=pot,
        hero_hole=["9c", "9s"],
        hero_stack=574,
        hero_bet=0,
        villain_bets={3: villain_bet},
        stacks={1: 574},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            can_all_in=True,
            call_chips=villain_bet,
            call_to=villain_bet,
            all_in_to=574,
        ),
    )


def mp_99_ace_paired_river(*, villain_bet: int = 400, pot: int = 900) -> dict:
    """99 MP OOP on ace-paired runout — HL R12 analyze #01 (−448)."""
    return six_max_table(
        name="mp_99_ace_paired_river",
        hero_seat=5,
        button_seat=1,
        street="River",
        board=["As", "7s", "2s", "Ac", "6c"],
        pot=pot,
        hero_hole=["9c", "9s"],
        hero_stack=448,
        hero_bet=0,
        villain_bets={6: villain_bet},
        stacks={5: 448},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def mp_t6o_paired_river(*, villain_bet: int = 180, pot: int = 520) -> dict:
    """T6o MP OOP on paired runout — analyze round 3 #01 (−290)."""
    return six_max_table(
        name="mp_t6o_paired_river",
        hero_seat=5,
        button_seat=1,
        street="River",
        board=["5h", "Th", "4s", "7h", "4d"],
        pot=pot,
        hero_hole=["Td", "6s"],
        hero_stack=400,
        hero_bet=0,
        villain_bets={3: villain_bet},
        stacks={5: 400},
        allowed=_allowed(
            can_call=True,
            can_raise=True,
            call_chips=villain_bet,
            call_to=villain_bet,
            raise_range={"min": villain_bet * 2, "max": 400},
        ),
    )


def sb_43s_facing_open(*, raise_to: int = 60) -> dict:
    """43s SB vs open — analyze round 3 #08."""
    return sb_facing_open(["4s", "3s"], raise_to=raise_to)


def bb_a8o_paired_runout(*, villain_bet: int = 80, pot: int = 320) -> dict:
    """A8o BB OOP top pair on paired runout — As8c BB −29 9822 (HL R36 #01)."""
    return six_max_table(
        name="bb_a8o_paired_runout",
        hero_seat=3,
        button_seat=1,
        street="River",
        board=["8d", "9c", "Jc", "2h", "2s"],
        pot=pot,
        hero_hole=["As", "8c"],
        hero_stack=500,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={3: 500},
        allowed=_allowed(
            can_call=True,
            can_raise=True,
            call_chips=villain_bet,
            call_to=villain_bet,
            raise_range={"min": villain_bet * 2, "max": 500},
        ),
    )


def bb_a6o_paired_river(*, villain_bet: int = 100, pot: int = 280) -> dict:
    """A6o BB OOP weak ace on paired board — analyze #07."""
    return six_max_table(
        name="bb_a6o_paired_river",
        hero_seat=3,
        button_seat=1,
        street="River",
        board=["9s", "9c", "3c", "Jh", "4c"],
        pot=pot,
        hero_hole=["Ad", "6h"],
        hero_stack=600,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={3: 600},
        allowed=_allowed(
            can_call=True,
            can_raise=True,
            call_chips=villain_bet,
            call_to=villain_bet,
            raise_range={"min": villain_bet * 2, "max": 600},
        ),
    )


def nuts_straight_river_value(*, pot: int = 120) -> dict:
    """Nut straight BTN river — free to act; must value bet (nuts detect)."""
    return six_max_table(
        name="nuts_straight_river_value",
        hero_seat=1,
        button_seat=1,
        street="River",
        board=["9s", "8h", "7d", "6c", "2s"],
        pot=pot,
        hero_hole=["Jc", "Th"],
        hero_stack=800,
        hero_bet=0,
        stacks={1: 800},
        allowed=_allowed(
            can_check=True,
            can_bet=True,
            bet_range={"min": 20, "max": 800},
        ),
    )


def nuts_quads_facing_bet(*, villain_bet: int = 400, pot: int = 800) -> dict:
    """Quad aces facing pot-size bet — must never fold (nuts detect)."""
    return six_max_table(
        name="nuts_quads_facing_bet",
        hero_seat=1,
        button_seat=1,
        street="River",
        board=["As", "Ad", "7c", "2h", "3s"],
        pot=pot,
        hero_hole=["Ac", "Ah"],
        hero_stack=1200,
        hero_bet=0,
        villain_bets={3: villain_bet},
        stacks={1: 1200},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            can_raise=True,
            call_chips=villain_bet,
            call_to=villain_bet,
            raise_range={"min": villain_bet * 2, "max": 1200},
        ),
    )


def second_nut_flush_river(*, villain_bet: int = 200, pot: int = 450) -> dict:
    """High card on monotone flush board — not unbeatable; fold vs bet."""
    return six_max_table(
        name="second_nut_flush_river",
        hero_seat=1,
        button_seat=1,
        street="River",
        board=["Qh", "Jh", "2h", "7h", "3c"],
        pot=pot,
        hero_hole=["Ad", "Kc"],
        hero_stack=700,
        hero_bet=0,
        villain_bets={3: villain_bet},
        stacks={1: 700},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def board_quad_chop_river(*, villain_bet: int = 150, pot: int = 300) -> dict:
    """Board quads chop — hero must not fold when nuts detect on."""
    return six_max_table(
        name="board_quad_chop_river",
        hero_seat=1,
        button_seat=1,
        street="River",
        board=["2c", "2d", "2h", "2s", "Ac"],
        pot=pot,
        hero_hole=["3d", "4c"],
        hero_stack=600,
        hero_bet=0,
        villain_bets={3: villain_bet},
        stacks={1: 600},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            can_raise=True,
            call_chips=villain_bet,
            call_to=villain_bet,
            raise_range={"min": villain_bet * 2, "max": 600},
        ),
    )


def nuts_quads_facing_shove(*, villain_bet: int = 800, pot: int = 1600) -> dict:
    """Quad aces vs shove-only action menu — must all-in, never fold."""
    return six_max_table(
        name="nuts_quads_facing_shove",
        hero_seat=1,
        button_seat=1,
        street="River",
        board=["As", "Ad", "7c", "2h", "3s"],
        pot=pot,
        hero_hole=["Ac", "Ah"],
        hero_stack=800,
        hero_bet=0,
        villain_bets={3: villain_bet},
        stacks={1: 800},
        allowed=_allowed(
            can_fold=True,
            can_call=False,
            can_all_in=True,
            call_chips=villain_bet,
            call_to=villain_bet,
            all_in_to=800,
            max_commit=800,
        ),
    )


def overcommit_spot(hero_hole: list[str], *, call_chips: int = 200) -> dict:
    """Short stack, large call vs weak hand (board misses hero)."""
    return six_max_table(
        name="overcommit",
        hero_seat=5,
        button_seat=1,
        street="Turn",
        board=["As", "9d", "2c", "Kh"],
        pot=400,
        hero_hole=hero_hole,
        hero_stack=500,
        villain_bets={3: call_chips},
        stacks={5: 500},
        allowed=_allowed(
            can_call=True,
            call_chips=call_chips,
            call_to=call_chips,
        ),
    )


def sb_jj_boat_paired_river(*, river_bet: int = 120, pot: int = 280) -> dict:
    """JJ full house on KKJxx — must not fold under SB underpair guard."""
    return six_max_table(
        name="sb_jj_boat_paired_river",
        hero_seat=2,
        button_seat=1,
        street="River",
        board=["Kh", "Kd", "Jc", "5s", "4h"],
        pot=pot,
        hero_hole=["Js", "Jc"],
        hero_stack=400,
        hero_bet=0,
        villain_bets={1: river_bet},
        stacks={2: 400},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            can_raise=True,
            call_chips=river_bet,
            call_to=river_bet,
            raise_range={"min": river_bet * 2, "max": 400},
        ),
    )


def co_72o_boat_paired_river(*, villain_bet: int = 50, pot: int = 150) -> dict:
    """72o boat on 772xx — must not fold CO trash-on-paired guard."""
    return six_max_table(
        name="co_72o_boat_paired_river",
        hero_seat=6,
        button_seat=1,
        street="River",
        board=["7h", "7d", "2c", "2s", "3h"],
        pot=pot,
        hero_hole=["7c", "2d"],
        hero_stack=500,
        hero_bet=0,
        villain_bets={5: villain_bet},
        stacks={6: 500},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def sb_qq_top_set_connected_river(*, river_bet: int = 450, pot: int = 900) -> dict:
    """QQ top set on QJTxx — must not fold SB medium-pair connected guard."""
    return six_max_table(
        name="sb_qq_top_set_connected_river",
        hero_seat=2,
        button_seat=1,
        street="River",
        board=["Qh", "Jc", "Td", "8s", "2c"],
        pot=pot,
        hero_hole=["Qs", "Qd"],
        hero_stack=500,
        hero_bet=0,
        villain_bets={1: river_bet},
        stacks={2: 500},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            can_raise=True,
            call_chips=river_bet,
            call_to=river_bet,
            raise_range={"min": river_bet * 2, "max": 500},
        ),
    )


def sb_49s_river_leak(*, river_bet: int = 180, pot: int = 400) -> dict:
    """49s SB OOP river — HL R16 analyze #01 (−2085)."""
    return six_max_table(
        name="sb_49s_river_leak",
        hero_seat=2,
        button_seat=1,
        street="River",
        board=["Kh", "Qc", "4h", "5c", "Ad"],
        pot=pot,
        hero_hole=["4s", "9s"],
        hero_stack=600,
        hero_bet=0,
        villain_bets={1: river_bet},
        stacks={2: 600},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=river_bet,
            call_to=river_bet,
        ),
    )


def sb_tt_ace_pair_river(*, river_bet: int = 200, pot: int = 450) -> dict:
    """TT SB OOP on ace-paired runout — HL R16 analyze #02 (−2002)."""
    return six_max_table(
        name="sb_tt_ace_pair_river",
        hero_seat=2,
        button_seat=1,
        street="River",
        board=["3s", "Ad", "8c", "As", "2h"],
        pot=pot,
        hero_hole=["Td", "Ts"],
        hero_stack=500,
        hero_bet=0,
        villain_bets={1: river_bet},
        stacks={2: 500},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=river_bet,
            call_to=river_bet,
        ),
    )


def sb_j3o_flop_leak(*, villain_bet: int = 40, pot: int = 80) -> dict:
    """J3o SB OOP flop — HL R17 analyze #01."""
    return six_max_table(
        name="sb_j3o_flop_leak",
        hero_seat=2,
        button_seat=1,
        street="Flop",
        board=["Ts", "Qc", "9d"],
        pot=pot,
        hero_hole=["3d", "Jh"],
        hero_stack=900,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={2: 900},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def sb_j4o_flop_r29(*, villain_bet: int = 50, pot: int = 100) -> dict:
    """J4o SB OOP weak top pair — HL R29 S2T analyze #01 (4c Js −128)."""
    return six_max_table(
        name="sb_j4o_flop_r29",
        hero_seat=2,
        button_seat=1,
        street="Flop",
        board=["7c", "2d", "Jd"],
        pot=pot,
        hero_hole=["4c", "Js"],
        hero_stack=900,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={2: 900},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def sb_q8s_flop_leak(*, villain_bet: int = 45, pot: int = 90) -> dict:
    """Q8s SB OOP top pair weak kicker — HL R17 analyze #05."""
    return six_max_table(
        name="sb_q8s_flop_leak",
        hero_seat=2,
        button_seat=1,
        street="Flop",
        board=["Th", "Qd", "7d"],
        pot=pot,
        hero_hole=["8s", "Qs"],
        hero_stack=900,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={2: 900},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def sb_k3s_turn_leak(*, villain_bet: int = 55, pot: int = 110) -> dict:
    """K3s SB OOP turn — HL R17 analyze #04."""
    return six_max_table(
        name="sb_k3s_turn_leak",
        hero_seat=2,
        button_seat=1,
        street="Turn",
        board=["8d", "4c", "5s", "6c"],
        pot=pot,
        hero_hole=["3d", "Kd"],
        hero_stack=900,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={2: 900},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def mp_t4o_river_leak(*, villain_bet: int = 50, pot: int = 120) -> dict:
    """T4o MP OOP river bottom pair — HL R18 analyze #01."""
    return six_max_table(
        name="mp_t4o_river_leak",
        hero_seat=5,
        button_seat=1,
        street="River",
        board=["9c", "Jh", "7c", "4s", "Kh"],
        pot=pot,
        hero_hole=["Th", "4d"],
        hero_stack=900,
        hero_bet=0,
        villain_bets={4: villain_bet},
        stacks={5: 900},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )


def sb_a9o_trips_flop(*, villain_bet: int = 45, pot: int = 90) -> dict:
    """A9o trips on AAx — must not fold (HL R18 #05 guard fix)."""
    return six_max_table(
        name="sb_a9o_trips_flop",
        hero_seat=2,
        button_seat=1,
        street="Flop",
        board=["Ac", "Ad", "2c"],
        pot=pot,
        hero_hole=["As", "9c"],
        hero_stack=900,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={2: 900},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            can_raise=True,
            call_chips=villain_bet,
            call_to=villain_bet,
            raise_range={"min": villain_bet * 2, "max": 900},
        ),
    )


def mp_77_set_flop(*, villain_bet: int = 55, pot: int = 110) -> dict:
    """77 set on 775 — must not fold paired-runout trash guard (HL R19)."""
    return six_max_table(
        name="mp_77_set_flop",
        hero_seat=4,
        button_seat=1,
        street="Flop",
        board=["7h", "7d", "5c"],
        pot=pot,
        hero_hole=["7s", "7c"],
        hero_stack=900,
        hero_bet=0,
        villain_bets={5: villain_bet},
        stacks={4: 900},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            can_raise=True,
            call_chips=villain_bet,
            call_to=villain_bet,
            raise_range={"min": villain_bet * 2, "max": 900},
        ),
    )


def bb_53s_turn_leak(*, villain_bet: int = 50, pot: int = 100) -> dict:
    """53s BB OOP turn — HL R18 analyze #10."""
    return six_max_table(
        name="bb_53s_turn_leak",
        hero_seat=3,
        button_seat=1,
        street="Turn",
        board=["7d", "8s", "6c", "Tc"],
        pot=pot,
        hero_hole=["5h", "3h"],
        hero_stack=900,
        hero_bet=0,
        villain_bets={1: villain_bet},
        stacks={3: 900},
        allowed=_allowed(
            can_fold=True,
            can_call=True,
            call_chips=villain_bet,
            call_to=villain_bet,
        ),
    )
