"""Preflop guardrails — block trash open-steals (J2o CO leak)."""
from __future__ import annotations

import sys
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parents[1] / "examples"
_TESTS = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))
if str(_TESTS) not in sys.path:
    sys.path.insert(0, str(_TESTS))

from cemini_decide import (  # noqa: E402
    _blocks_open_steal,
    _preflop_open,
    _preflop_pot_committed_should_call,
    _preflop_vs_bet,
)


def test_blocks_j2o_co_steal():
    assert _blocks_open_steal("J2o", "CO") is True
    assert _blocks_open_steal("72o", "BTN") is True
    assert _blocks_open_steal("A5s", "CO") is False


def test_j2o_chart_fold_not_open_stolen_vs_rock():
    allowed = {"canBet": True, "betRange": {"min": 20, "max": 100}}
    available = ["fold", "check", "bet"]
    margins = {"open_steal_equity": 0.34}
    action, amount = _preflop_open(
        "fold", allowed, available, pot=40, equity=0.55,
        hand_class="J2o", position="CO", hud_mode="rock", margins=margins,
    )
    assert action in ("fold", "check")
    assert action != "bet"


def test_ep_no_steal_74o_mp():
    from cemini_decide import _preflop_open

    allowed = {"canBet": True, "betRange": {"min": 20, "max": 100}}
    available = ["fold", "check", "bet"]
    margins = {"open_steal_equity": 0.34}
    action, _ = _preflop_open(
        "fold", allowed, available, pot=40, equity=0.60,
        hand_class="74o", position="MP", hud_mode="rock", margins=margins,
    )
    assert action == "fold"


def test_overcommit_fold_weak_hand():
    from cemini_decide import _overcommit_should_fold

    table = {"selfSeatNumber": 1, "seats": [{"seatNumber": 1, "stackChips": 500}]}
    assert _overcommit_should_fold(table, "74o", 0.35, 200) is True
    assert _overcommit_should_fold(table, "AKs", 0.60, 200) is False


def test_preflop_pot_committed_call_guard():
    assert _preflop_pot_committed_should_call(50, 1900, ["fold", "call"]) is True
    assert _preflop_pot_committed_should_call(200, 300, ["fold", "call"]) is False


def test_preflop_vs_bet_calls_when_pot_committed_with_weak_ace():
    allowed = {
        "canFold": True,
        "canCall": True,
        "availableActions": ["fold", "call"],
        "callChips": 50,
    }
    table = {
        "selfSeatNumber": 1,
        "bigBlindChips": 20,
        "potChips": 1900,
        "allowedActions": allowed,
        "seats": [{"seatNumber": 1, "stackChips": 50}],
    }
    chart = {"hand_class": "A6o", "position": "SB", "suggested_action": "fold"}

    action, amount = _preflop_vs_bet(
        chart,
        allowed,
        ["fold", "call"],
        equity=0.25,
        pot_odds=50 / 1950,
        call_chips=50,
        pot=1900,
        in_position=False,
        table=table,
        hero_stack_chips=50,
        big_blind=20,
    )

    assert (action, amount) == ("call", None)


def _vs_raise_table(*, stack: int = 980, pot: int = 70, call_chips: int = 40) -> dict:
    """6-max-shaped facing-raise table (not HU)."""
    allowed = {
        "canFold": True,
        "canCall": True,
        "canRaise": True,
        "availableActions": ["fold", "call", "raise"],
        "callChips": call_chips,
        "raiseRange": {"min": call_chips * 2, "max": stack},
    }
    return {
        "selfSeatNumber": 1,
        "bigBlindChips": 20,
        "potChips": pot,
        "buttonSeatNumber": 4,
        "allowedActions": allowed,
        "seats": [
            {"seatNumber": 1, "stackChips": stack, "status": "Active", "agentId": "hero"},
            {"seatNumber": 2, "stackChips": 1000, "status": "Active", "agentId": "v2"},
            {"seatNumber": 3, "stackChips": 1000, "status": "Active", "agentId": "v3"},
            {"seatNumber": 4, "stackChips": 1000, "status": "Active", "agentId": "v4"},
            {"seatNumber": 5, "stackChips": 1000, "status": "Active", "agentId": "v5"},
            {"seatNumber": 6, "stackChips": 1000, "status": "Active", "agentId": "v6"},
        ],
    }


def _fold_vs_raise(hand_class: str, position: str, *, equity: float = 0.42) -> str:
    table = _vs_raise_table()
    allowed = table["allowedActions"]
    call_chips = int(allowed["callChips"])
    pot = int(table["potChips"])
    chart = {
        "hand_class": hand_class,
        "position": position,
        "suggested_action": "fold",
    }
    action, _ = _preflop_vs_bet(
        chart,
        allowed,
        ["fold", "call", "raise"],
        equity=equity,
        pot_odds=call_chips / max(pot + call_chips, 1),
        call_chips=call_chips,
        pot=pot,
        in_position=position in ("CO", "BTN"),
        table=table,
        hero_stack_chips=int(table["seats"][0]["stackChips"]),
        big_blind=20,
    )
    return action


# --- Playground S9 → S10 chip-survival guards ---


def test_s9_sb_q5s_vs_raise_fold():
    """S9: Q5s SB cold-called opens; dominated suited queen OOP."""
    assert _fold_vs_raise("Q5s", "SB") == "fold"


def test_s9_sb_q6s_vs_raise_fold():
    assert _fold_vs_raise("Q6s", "SB") == "fold"


def test_s9_sb_kts_vs_raise_fold():
    """S9: KTs SB call vs open — dominated broadway suited OOP."""
    assert _fold_vs_raise("KTs", "SB") == "fold"


def test_s9_sb_22_vs_raise_fold_no_setmine():
    """S9: 22/44/77 SB flats set-mined OOP and bled postflop."""
    assert _fold_vs_raise("22", "SB", equity=0.50) == "fold"
    assert _fold_vs_raise("44", "SB", equity=0.50) == "fold"
    assert _fold_vs_raise("77", "SB", equity=0.50) == "fold"


def test_s9_bb_75o_vs_raise_fold():
    """S9: 75o BB floated twice — offsuit connector gap in WEAK_FACING_RAISE."""
    assert _fold_vs_raise("75o", "BB") == "fold"


def test_s9_bb_76o_vs_raise_fold():
    assert _fold_vs_raise("76o", "BB") == "fold"


def test_s9_bb_j7s_vs_raise_fold():
    """S9: J7s BB float — dominated suited jack."""
    assert _fold_vs_raise("J7s", "BB") == "fold"


def test_s9_bb_k9s_vs_raise_fold():
    assert _fold_vs_raise("K9s", "BB") == "fold"


def test_s9_btn_kqo_vs_raise_fold():
    """S9: KQo BTN cold-call — extend broadway fold to BTN."""
    assert _fold_vs_raise("KQo", "BTN") == "fold"


def test_s9_btn_q5s_vs_raise_fold():
    assert _fold_vs_raise("Q5s", "BTN") == "fold"


def test_s9_co_j8s_vs_raise_fold():
    assert _fold_vs_raise("J8s", "CO") == "fold"


def test_s9_co_a6s_vs_raise_fold():
    """S9: A6s CO flat vs raise — weak suited ace multiway trap."""
    assert _fold_vs_raise("A6s", "CO") == "fold"


def test_s9_ep_pocket_under_overcards_folds():
    """S9 #01: 22 MP on 6c5sTdQh6d — OOP underpair peels too far."""
    from cemini_decide import _hero_pocket_under_board_overcards

    hole = ["2s", "2h"]
    board = ["6c", "5s", "Td", "Qh", "6d"]
    assert _hero_pocket_under_board_overcards(hole, board, "22") is True

    # Flop alone already has T overcard — guard applies from 3 board cards.
    assert _hero_pocket_under_board_overcards(hole, ["6c", "5s", "Td"], "22") is True


def test_s9_sb_tt_still_defends_vs_raise():
    """Do not over-nit: TT+ SB may still call/raise (not in LOW_PAIRS_PROTECT)."""
    action = _fold_vs_raise("TT", "SB", equity=0.55)
    assert action in ("call", "raise")


def test_s9_bb_kqs_still_defends_vs_raise():
    """Premium suited broadway BB defense stays live."""
    action = _fold_vs_raise("KQs", "BB", equity=0.48)
    assert action in ("call", "raise")


# --- Playground S10 climb — selective BTN/CO steal + maniac value call ---


def test_s10_allows_selective_steal_rock_and_loose_passive_only():
    from cemini_decide import _allows_selective_btn_co_steal

    assert _allows_selective_btn_co_steal("rock", {"open_steal_equity": 0.34}) is True
    # wide_passive → legacy "tight" + rock_steal_eq-style bar
    assert _allows_selective_btn_co_steal("tight", {"open_steal_equity": 0.38}) is True
    assert _allows_selective_btn_co_steal("loose-passive", {"open_steal_equity": 0.34}) is True
    # No global widen: high steal bar / unknown / maniac
    assert _allows_selective_btn_co_steal("tight", {"open_steal_equity": 0.99}) is False
    assert _allows_selective_btn_co_steal("unknown", {"open_steal_equity": 0.38}) is False
    assert _allows_selective_btn_co_steal("maniac", {"open_steal_equity": 0.99}) is False


def test_s10_lp_btn_a9s_steal_vs_loose_passive_hud():
    """S10 climb: A9s BTN chart-fold → open vs confirmed loose-passive (not maniac)."""
    allowed = {"canBet": True, "betRange": {"min": 20, "max": 100}}
    available = ["fold", "check", "bet"]
    margins = {"open_steal_equity": 0.38}
    action, _ = _preflop_open(
        "fold", allowed, available, pot=40, equity=0.50,
        hand_class="A9s", position="BTN", hud_mode="tight", margins=margins,
        cold_start=False,
    )
    assert action == "bet"


def test_s10_lp_co_k9s_steal_vs_loose_passive_hud():
    allowed = {"canBet": True, "betRange": {"min": 20, "max": 100}}
    available = ["fold", "check", "bet"]
    margins = {"open_steal_equity": 0.38}
    action, _ = _preflop_open(
        "fold", allowed, available, pot=40, equity=0.50,
        hand_class="K9s", position="CO", hud_mode="tight", margins=margins,
        cold_start=False,
    )
    assert action == "bet"


def test_s10_lp_j2o_still_blocked_vs_loose_passive():
    """Do not global-widen trash — J2o CO remains fold even vs LP HUD."""
    allowed = {"canBet": True, "betRange": {"min": 20, "max": 100}}
    available = ["fold", "check", "bet"]
    margins = {"open_steal_equity": 0.38}
    action, _ = _preflop_open(
        "fold", allowed, available, pot=40, equity=0.55,
        hand_class="J2o", position="CO", hud_mode="tight", margins=margins,
        cold_start=False,
    )
    assert action in ("fold", "check")
    assert action != "bet"


def test_s10_no_steal_widen_vs_maniac_hud():
    """Maniac lane: fold trash preflop / no steal widen (value is postflop call-down)."""
    allowed = {"canBet": True, "betRange": {"min": 20, "max": 100}}
    available = ["fold", "check", "bet"]
    margins = {"open_steal_equity": 0.99}
    action, _ = _preflop_open(
        "fold", allowed, available, pot=40, equity=0.50,
        hand_class="A9s", position="BTN", hud_mode="maniac", margins=margins,
        cold_start=False,
    )
    assert action in ("fold", "check")


def test_s10_maniac_value_call_boost_6max_and_hu():
    from cemini_decide import _maniac_value_call_margin_boost

    six = _maniac_value_call_margin_boost(
        hud_mode_raw="maniac", villain_vpip=0.65, is_hu=False,
    )
    hu = _maniac_value_call_margin_boost(
        hud_mode_raw="maniac", villain_vpip=0.65, is_hu=True,
    )
    assert six is not None and six["call_margin_delta"] < 0
    assert hu is not None and hu["call_margin_delta"] <= six["call_margin_delta"]
    # VPIP>>45% alone qualifies (grok* cluster without mode label)
    vpip_only = _maniac_value_call_margin_boost(
        hud_mode_raw="unknown", villain_vpip=0.50, is_hu=False,
    )
    assert vpip_only is not None
    # Low VPIP no boost
    assert _maniac_value_call_margin_boost(
        hud_mode_raw="unknown", villain_vpip=0.30, is_hu=False,
    ) is None


# --- Playground S10 climb2 — CO/MP overcommits (Cursor, Grok CLI out) ---


def test_s10_climb2_mp_55_under_king_folds():
    """S10 #02: 55 MP on 4h7dKc peels too far (−5)."""
    from cemini_decide import decide
    from tests.helpers.cemini_tables import mp_55_under_king_flop_s10

    out = decide(mp_55_under_king_flop_s10(), deadline_s=10.0)
    assert out.get("action") == "fold", out


def test_s10_climb2_co_k9s_king_high_air_folds():
    """S10 #01: K9s CO king-high on 43JTx (−11)."""
    from cemini_decide import decide
    from tests.helpers.cemini_tables import co_k9s_king_high_air_s10

    out = decide(co_k9s_king_high_air_s10(), deadline_s=10.0)
    assert out.get("action") == "fold", out


def test_s10_climb2_weak_king_high_helper():
    from cemini_decide import _hero_weak_king_high_air

    assert _hero_weak_king_high_air(
        ["9c", "Kc"], ["4s", "3d", "Js", "Th", "5h"], "K9s",
    ) is True
    # Paired king — not air
    assert _hero_weak_king_high_air(
        ["9c", "Kc"], ["4s", "Kd", "Js"], "K9s",
    ) is False
    # KTs stays out of weak-king air set
    assert _hero_weak_king_high_air(
        ["Tc", "Kc"], ["4s", "3d", "Js"], "KTs",
    ) is False

