"""Cemini / gambling-wiki dev.fun Poker Arena agent.

Layers on arena-pokerkit L1:
  1. Auto Research — preflop chart (research_static_chart)
  2. Skill binding stub — street/hand-class labels in reasoning (PokerSkill pattern)
  3. Equity + pot-odds postflop (treys MC from agent.py)
  4. Hard deadline fallbacks (check > fold)

Run:
  uv run examples/agent.py --agent examples/cemini_decide.py --dry-run --max-hands 20
  uv run examples/agent.py --agent examples/cemini_decide.py --competition-id <id>
"""
from __future__ import annotations

import os
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Optional

from blind_pressure import lead_blind_steal

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from agent import (  # noqa: E402
    _build,
    _hand_class,
    estimate_equity,
)
from position_utils import hero_is_in_position, hero_position_label  # noqa: E402
from qualification_guard import max_playable_chips  # noqa: E402
from opponent_hud import build_opponent_hud, enrich_hud_from_table, exploit_margins  # noqa: E402
from pokerskill_adapter import retrieve_pokerskill_hints  # noqa: E402
from session_memory import exploit_from_memory  # noqa: E402
from nemesis_seed import nemesis_handles, table_nemesis_opener, table_nemesis_pressure  # noqa: E402
from opponent_target import is_preflop_open_spot  # noqa: E402
from s1b_exploit import (  # noqa: E402
    exploit_lane_active,
    try_defend_bb_vs_steal,
    try_iso_vs_wide_passive_limp,
    try_jeff_nemesis_4bet,
    try_three_bet_lag_vs_open,
    try_trap_aa_kk_vs_3bet,
)
from villain_archetype import premium_concentration_index, seat_matrix_v2_enabled  # noqa: E402
from jackpot_27_decide import maybe_hunt_action  # noqa: E402
from jackpot_rules import royal_showdown_action, royal_showdown_mode  # noqa: E402

try:
    from train_config import threshold as _train_threshold  # noqa: E402
except ImportError:
    def _train_threshold(_name: str, default: float) -> float:  # noqa: E402
        return default
from research_static_chart import research_static_chart  # noqa: E402
from action_mix import resolve_postflop_call_fold  # noqa: E402
from hand_nuts import river_unbeatable, treys_available  # noqa: E402

# Preflop trash facing a raise — fold unless equity clearly covers price.
_WEAK_FACING_RAISE = frozenset({
    "A2o", "A3o", "A4o", "A5o", "A6o", "A7o", "A8o", "A9o",
    "K9o", "K8o", "K7o", "K6o", "K5o", "K4o", "K3o", "K2o",
    "Q9o", "Q8o", "Q7o", "Q6o", "Q5o", "Q4o", "Q3o", "Q2o",
    "J9o", "J8o", "J7o", "J6o", "J5o", "J4o", "J3o", "J2o",
    "T9o", "T8o", "T7o", "T6o", "T5o", "T4o", "T3o", "T2o",
    "98o", "97o", "96o", "95o", "94o", "93o", "92o", "87o",
    "KJo", "QJo", "JTo", "KTo", "QTo",
    "84o", "83o", "82o", "74o", "73o", "72o", "64o", "63o", "62o",
    "54o", "53o", "52o", "43o", "42o", "32o", "96o", "79o",
})

_LOW_PAIRS_PROTECT = frozenset({"77", "66", "55", "44", "33", "22"})
_CO_WEAK_CONNECTOR = frozenset({"98o", "87o", "T8o", "97o", "86o", "76o", "65o"})
_BB_BROADWAY_FOLD = frozenset({"KQo", "QJo", "KJo", "KTo", "QTo", "JTo", "AJo", "ATo"})
_SB_WEAK_SUITED_VS_OPEN = frozenset({
    "K9s", "K8s", "Q9s", "Q8s", "J9s", "J8s", "T9s", "T8s", "98s", "87s", "76s",
})
_PREFLOP_3BET_OK = frozenset({"AA", "KK", "QQ", "JJ", "TT", "AKs", "AKo", "AQs", "AQo"})
# HL R25: EP suited broadway opens/calls bleed vs LAG shoves (QJs UTG −100 #01, KQs UTG #12).
_EP_SUITED_BROADWAY_TRAP = frozenset({"KQs", "QJs", "KJs", "JTs"})

_RANKS = "23456789TJQKA"
_ROYAL_IDX = tuple(_RANKS.index(r) for r in "AKQJT")
def _survival_stack_threshold() -> int:
    """Below this stack, chart-first survival margins apply (tournament: ~80% of 1000)."""
    raw = os.environ.get("CEMINI_SURVIVAL_STACK_CHIPS", "800")
    try:
        return max(0, int(raw))
    except ValueError:
        return 800
_COLD_START_OPEN_OK = frozenset({"AA", "KK", "QQ", "JJ", "TT", "AKs", "AKo", "AQs", "AQo"})
_NEMESIS_SB_DEFEND_OK = frozenset({
    "AA", "KK", "QQ", "JJ", "TT", "99", "88", "77",
    "AKs", "AKo", "AQs", "AQo",
})


def _cold_start_no_steal_enabled() -> bool:
    raw = os.environ.get("CEMINI_COLD_START_NO_STEAL", "1")
    return raw.strip().lower() not in ("0", "false", "no", "off")


def _nemesis_tight_enabled() -> bool:
    raw = os.environ.get("CEMINI_NEMESIS_TIGHT", "1")
    return raw.strip().lower() not in ("0", "false", "no", "off")


def _survival_mode(self_seat: dict) -> bool:
    stack = int(self_seat.get("stackChips") or 99999)
    return stack < _survival_stack_threshold()


def _merge_margins(base: dict, *extras: dict) -> dict:
    out = dict(base)
    for extra in extras:
        for key, delta in extra.items():
            out[key] = out.get(key, 0.0) + float(delta)
    return out


def retrieve_solver_context(table: dict) -> dict:
    """Preflop chart + PokerSkill hints + skill-binding labels for decide()."""
    chart = research_static_chart(table)
    ps = retrieve_pokerskill_hints(table)
    self_seat_num = table.get("selfSeatNumber")
    seats = table.get("seats") or []
    self_seat = next((s for s in seats if s.get("seatNumber") == self_seat_num), {})
    hole = list(self_seat.get("holeCards") or [])
    board = list(table.get("boardCards") or [])
    street = (table.get("street") or "Preflop").lower()
    hc = _hand_class(hole) or chart.get("hand_class") or ""
    scenario = ps.get("scenario") or _scenario_label(street, board, hc)

    ctx: dict[str, Any] = {
        "preflop_chart": {
            "suggested_action": chart.get("preflop_action"),
            "hand_class": hc or chart.get("hand_class"),
            "position": chart.get("position"),
        },
        "pokerskill": ps,
        "skill_binding": {
            "street": street,
            "hand_class": hc or "unknown",
            "board_len": len(board),
            "scenario": scenario,
        },
    }
    if chart:
        ctx.update(chart)
    oh = build_opponent_hud(table)
    if oh:
        ctx["opponent_hud"] = enrich_hud_from_table(oh, table)
    try:
        from hl_runtime_config import load_style_overrides, is_kill_switch_active
        ctx["hl_style_overrides"] = load_style_overrides()
        if is_kill_switch_active():
            ctx["kill_switch"] = True
    except Exception:
        pass
    try:
        from table_chat_intel import extract_chat_intel

        ctx["chat_intel"] = extract_chat_intel(table)
    except Exception:
        pass
    return ctx


def _scenario_label(street: str, board: list[str], hc: str) -> str:
    if street == "preflop":
        return "open_defend" if hc else "preflop_unknown"
    if len(board) >= 3:
        suits = [c[-1].lower() for c in board if c]
        if suits and max(suits.count(s) for s in set(suits)) >= 2:
            return "wet_board_pot_control"
    return "dry_board_value"


def decide(
    table: dict,
    deadline_s: float = 10.0,
    research_context: Optional[dict] = None,
) -> dict:
    allowed = table.get("allowedActions") or {}
    available = allowed.get("availableActions") or []

    self_seat_num = table.get("selfSeatNumber")
    seats = table.get("seats") or []
    self_seat = next((s for s in seats if s.get("seatNumber") == self_seat_num), {})
    hole = list(self_seat.get("holeCards") or [])
    board = list(table.get("boardCards") or [])
    street = (table.get("street") or "Preflop")
    pot = int(table.get("potChips") or 0)
    call_chips = int(allowed.get("callChips") or 0)

    if deadline_s < 2.0:
        out = _emergency_made_hand_action(
            table, allowed, available, hole, board, street, pot, call_chips,
        )
        if out:
            return out
        if allowed.get("canCheck"):
            return _build("check", None, table, allowed, eq=0.5, po=0.0,
                          msg="clock pressure — free check")
        return _build("fold", None, table, allowed, eq=0.0, po=1.0,
                      msg="clock pressure — fold")

    if research_context is None:
        research_context = retrieve_solver_context(table)
    ctx = research_context
    pot_odds = call_chips / max(pot + call_chips, 1) if call_chips else 0.0
    sims = 500 if deadline_s > 5 else (350 if deadline_s > 3 else 200)
    equity = estimate_equity(hole, board, sims=sims, deadline_s=deadline_s)

    chart = ctx.get("preflop_chart") or {}
    suggested = chart.get("suggested_action") or ctx.get("preflop_action")
    ps = ctx.get("pokerskill") or {}
    binding = (ctx.get("skill_binding") or {}).get("scenario", "unknown")
    in_position = hero_is_in_position(table)
    pot_control = bool(ps.get("pot_control"))
    ps_bias = ps.get("bias")
    ps_library = ps.get("mode") == "library"
    ps_hand_eval = ps.get("hand_eval")
    position = chart.get("position") or ctx.get("position") or hero_position_label(table)
    hc = _hand_class(hole) or chart.get("hand_class") or ""
    hud = enrich_hud_from_table(ctx.get("opponent_hud") or {}, table)
    ctx["opponent_hud"] = hud
    jp_out = maybe_hunt_action(
        table,
        allowed,
        available,
        hole,
        board,
        street,
        pot,
        call_chips,
        research_context=ctx,
        deadline_s=deadline_s,
    )
    if jp_out is not None:
        return jp_out
    hud_mode = hud.get("mode") or "unknown"
    qual_protect = bool(ctx.get("qualification_protect"))
    lead_protect = bool(ctx.get("lead_protect"))
    first_protect = bool(ctx.get("first_protect"))
    eval_panel = bool(ctx.get("eval_panel_mode"))
    ko_survival = bool(ctx.get("ko_survival_lane"))
    lane_tight = first_protect or qual_protect or lead_protect or eval_panel
    # Tournament hour-one: keep HUD exploit; do not treat ko_survival as exploit_gate.
    exploit_gate = qual_protect or first_protect or eval_panel
    if exploit_gate and hud_mode == "maniac":
        hud_mode = "unknown"
    margins = hud.get("margins") or exploit_margins(hud_mode)
    villain_mem = ctx.get("session_villain_memory") or {}
    if exploit_gate:
        mem_margins: dict[str, float] = {}
    else:
        mem_margins = exploit_from_memory(villain_mem) if villain_mem else {}
    margins = _merge_margins(margins, mem_margins)
    if eval_panel:
        margins = _merge_margins(
            margins,
            {"fold_slack_delta": 0.04, "call_margin_delta": 0.06},
        )
    max_playable = ctx.get("max_playable_chips")
    if max_playable is None and (qual_protect or lead_protect or first_protect):
        max_playable = max_playable_chips(
            ctx.get("leaderboard_chips"),
            cutoff_chips=ctx.get("cutoff_chips"),
            qualification_protect=qual_protect,
            lead_protect=lead_protect,
            first_protect=first_protect,
        )
    survival_tight = (
        _survival_mode(self_seat)
        or bool(ctx.get("survival_mode"))
        or qual_protect
        or lead_protect
    )
    survival = survival_tight or ko_survival
    if survival_tight:
        margins = _merge_margins(margins, {"fold_slack_delta": 0.04, "call_margin_delta": 0.05})
    elif ko_survival:
        margins = _merge_margins(margins, {"fold_slack_delta": 0.02, "call_margin_delta": 0.02})
    style_ov = ctx.get("hl_style_overrides") or {}
    if style_ov:
        tweak: dict[str, float] = {}
        for key in ("fold_slack_delta", "call_margin_delta"):
            if style_ov.get(key) is not None:
                tweak[key] = float(style_ov[key])
        if tweak:
            margins = _merge_margins(margins, tweak)

    try:
        from hl_runtime_config import (
            is_kill_switch_active,
            kill_switch_action,
            match_runtime_guard,
            apply_runtime_guard_action,
        )
        if ctx.get("kill_switch") or is_kill_switch_active():
            ks_out = kill_switch_action(
                table=table,
                allowed=allowed,
                available=available,
                equity=equity,
                pot_odds=pot_odds,
                build_fn=_build,
            )
            if ks_out:
                return ks_out
        guard = match_runtime_guard(
            street=street,
            position=position,
            hand_class=hc,
            call_chips=call_chips,
            can_check=bool(allowed.get("canCheck")),
            hero_stack_chips=_hero_stack_chips(table),
        )
        if guard:
            g_out = apply_runtime_guard_action(
                guard,
                table=table,
                allowed=allowed,
                available=available,
                equity=equity,
                pot_odds=pot_odds,
                build_fn=_build,
            )
            if g_out:
                return g_out
    except Exception:
        pass

    if qual_protect:
        margins = _merge_margins(margins, {"preflop_fold_margin_delta": 0.03})
    if lead_protect:
        margins = _merge_margins(margins, {
            "fold_slack_delta": 0.03,
            "call_margin_delta": 0.04,
            "bet_bar_delta": -0.06,
            "preflop_fold_margin_delta": 0.02,
        })
    if first_protect:
        margins = _merge_margins(margins, {
            "preflop_fold_margin_delta": 0.02,
            "open_steal_equity": 0.99,
        })
    if deadline_s < 4.0:
        margins = _merge_margins(margins, {"fold_slack_delta": 0.03})
    cold_start = bool(hud.get("coldStart"))
    hc = chart.get("hand_class") or _hand_class(hole) or ""

    action_name: str
    amount: Optional[int] = None

    river_unbeatable_flag = False
    if (_nuts_detect_enabled() and street == "River" and len(board) == 5
            and deadline_s >= 2.0 and treys_available()):
        from table_chat_intel import nuts_extra_dead_cards

        extra_dead = nuts_extra_dead_cards(table, hole, board, ctx.get("chat_intel"))
        river_unbeatable_flag, _, _ = river_unbeatable(
            hole, board, extra_dead_arena=extra_dead or None,
        )

    def _hero_cannot_lose() -> bool:
        if street != "Preflop" and _hero_made_royal_flush(hole, board):
            return True
        return river_unbeatable_flag

    # Made royal — showdown path for S2 jackpot (API: hand unfolded at showdown).
    if street != "Preflop" and _hero_made_royal_flush(hole, board):
        out = _royal_made_action(
            table, allowed, available, pot, binding=binding, call_chips=call_chips,
        )
        if out:
            return _apply_chip_reserve(out, max_playable, table, hc)

    # River unbeatable (enumeration) — never fold; value when free (CEMINI_NUTS_DETECT=1).
    if river_unbeatable_flag:
        out = _unbeatable_made_action(table, allowed, available, pot, binding=binding)
        if out:
            return _apply_chip_reserve(out, max_playable, table, hc)
        if call_chips > 0 and "fold" in available:
            if "all-in" in available:
                all_in_to = int(
                    allowed.get("allInToAmount") or allowed.get("maxCommit") or 0
                )
                if all_in_to > 0:
                    out = _build("all-in", all_in_to, table, allowed, eq=0.99, po=0.0,
                                  msg=f"{binding}: river unbeatable — all-in")
                    return _apply_chip_reserve(out, max_playable, table, hc)
            if "call" in available:
                return _build("call", None, table, allowed, eq=0.99, po=0.0,
                              msg=f"{binding}: river unbeatable — call")

    # Staggered bankroll lock — only risk playable chips above top-20 floor + tiers.
    if (max_playable is not None and call_chips > 0 and "fold" in available
            and call_chips > int(max_playable)
            and hc not in {"AA", "KK", "QQ"}
            and not _hero_cannot_lose()):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: stagger lock — fold over playable bankroll")

    # Cold start: chart-first — no marginal postflop calls until HUD reads land.
    if (cold_start and street != "Preflop" and call_chips > 0 and "fold" in available
            and hc not in {"AA", "KK", "QQ", "JJ", "TT", "AKs", "AKo", "AQs"}
            and not _hero_cannot_lose()
            and equity < pot_odds + 0.08):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: cold-start — fold marginal spot")

    if (street != "Preflop" and call_chips > 0 and "fold" in available
            and _overcommit_should_fold(
                table, hc, equity, call_chips, lead_protect=lead_protect,
                max_playable=max_playable)
            and not _hero_cannot_lose()):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: stack cap — fold overcommit")

    if (street != "Preflop" and call_chips > 0 and "fold" in available
            and position == "SB" and not in_position
            and _hero_underpair_on_paired_board(hc, board)
            and not _hero_cannot_lose()
            and call_chips >= max(int(pot * 0.32), 1)):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: SB underpair on paired board — fold")

    # SB OOP low suited wheel on ace-paired runout — 95s SB −100 (HL S2 R3 #01).
    if (street != "Preflop" and call_chips > 0 and "fold" in available
            and position == "SB" and not in_position
            and _board_has_ace_pair(board)
            and _is_low_suited_wheel(hc)
            and not _hero_made_hand_exempt(hole, board)
            and not _hero_cannot_lose()
            and call_chips >= max(int(pot * 0.15), 1)):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: SB low suited on ace-paired board — fold")

    # SB OOP low suited wheel on broadway river — 63s SB −100 (HL R4 #01).
    if (street == "River" and call_chips > 0 and "fold" in available
            and position == "SB" and not in_position
            and _is_low_suited_wheel(hc)
            and _board_broadway_count(board) >= 3
            and not _hero_made_hand_exempt(hole, board)
            and not _hero_cannot_lose()
            and call_chips >= max(int(pot * 0.10), 1)):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: SB low suited on broadway river — fold")

    # SB OOP marginal ace on paired runout — A9s SB −492 (HL R5 #01).
    if (street != "Preflop" and call_chips > 0 and "fold" in available
            and position == "SB" and not in_position
            and _marginal_ace_kicker(hc)
            and _board_is_paired(board)
            and len(board) >= 4
            and not _hero_made_hand_exempt(hole, board)
            and not _hero_has_ace_on_paired_ace_board(hole, board)
            and not _hero_cannot_lose()
            and call_chips >= max(int(pot * 0.12), 1)):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: SB marginal ace on paired board — fold")

    # SB OOP king-low offsuit on ace-paired board — K3o SB −100 (HL R5 #03).
    if (street != "Preflop" and call_chips > 0 and "fold" in available
            and position == "SB" and not in_position
            and _is_king_low_offsuit(hc)
            and _board_has_ace_pair(board)
            and not _hero_made_hand_exempt(hole, board)
            and not _hero_cannot_lose()
            and call_chips >= max(int(pot * 0.15), 1)):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: SB king-low on ace-paired board — fold")

    if (street != "Preflop" and call_chips > 0 and "fold" in available
            and not in_position
            and _is_wheel_offsuit(hc)
            and not _hero_cannot_lose()
            and call_chips >= max(int(pot * 0.18), 1)):
        pos_tag = position or "OOP"
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: {pos_tag} wheel offsuit vs bet — fold")

    if (street != "Preflop" and call_chips > 0 and "fold" in available
            and position == "SB" and not in_position
            and len(board) == 3
            and hc in _SB_WEAK_SUITED_VS_OPEN
            and not _hero_cannot_lose()
            and call_chips >= max(int(pot * 0.22), 1)):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: SB weak suited vs flop bet — fold")

    if (street != "Preflop" and call_chips > 0 and "fold" in available
            and position == "SB" and not in_position
            and _is_sb_suited_trash(hc)
            and not _hero_cannot_lose()
            and call_chips >= max(int(pot * 0.20), 1)):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: SB low suited trash vs bet — fold")

    if (street != "Preflop" and call_chips > 0 and "fold" in available
            and position == "SB" and not in_position
            and (_medium_pocket_pair(hc) or _small_pocket_pair(hc))
            and _board_has_ace_pair(board)
            and not _hero_pocket_set(hole, board)
            and not _hero_cannot_lose()
            and call_chips >= max(int(pot * 0.22), 1)):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: SB pocket pair under ace pair — fold")

    # SB OOP medium pair on connected runout vs big bet — QQ SB −1000 (HL R12 #01).
    if (street != "Preflop" and call_chips > 0 and "fold" in available
            and position == "SB" and not in_position
            and _medium_pocket_pair(hc)
            and not _hero_pocket_set(hole, board)
            and not _hero_cannot_lose()
            and len(board) >= 4
            and _board_has_three_consecutive_ranks(board)
            and call_chips >= max(int(pot * 0.38), 1)):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: SB medium pair on connected board — fold")

    # SB/BB OOP weak kicker top pair on three-flush — K2o SB −100 (HL R24 #01).
    if (street != "Preflop" and call_chips > 0 and "fold" in available
            and position in ("SB", "BB") and not in_position
            and _board_has_three_flush(board)
            and not _hero_has_flush(hole, board)
            and not _hero_cannot_lose()
            and _weak_kicker_top_pair(hole, board)
            and call_chips >= max(int(pot * 0.22), 1)):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: OOP weak top pair on three-flush — fold")

    # BTN/CO IP pocket under board pair — TT BTN −115 on JhJsAx (HL R8 #01).
    # Small pairs (22–99): lower bar — 22 CO −9 on A88xA missed micro river (HL R1 #01).
    if (street != "Preflop" and call_chips > 0 and "fold" in available
            and position in ("CO", "BTN") and in_position
            and _pocket_under_board_pair(hole, board)):
        ip_under_ratio = 0.12 if _small_pocket_pair(hc) else 0.28
        if _board_has_ace_pair(board) and _small_pocket_pair(hc):
            ip_under_ratio = 0.08
        if call_chips >= max(int(pot * ip_under_ratio), 1):
            return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                          msg=f"{binding}: IP underpair on paired board — fold")

    # EP OOP marginal top pair on paired runouts — T6o MP −290 (analyze #01).
    if (street != "Preflop" and call_chips > 0 and "fold" in available
            and position in ("UTG", "MP") and not in_position
            and _board_is_paired(board)
            and _marginal_offsuit_top_pair(hc)
            and call_chips >= max(int(pot * 0.28), 1)):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: EP weak top pair on paired board — fold")

    # CO weak two-pair on paired board — Q7o CO −747 bust (HL R11 #01).
    if (street != "Preflop" and call_chips > 0 and "fold" in available
            and position == "CO"
            and _board_is_paired(board)
            and len(board) >= 4
            and _hero_weak_two_pair_on_paired_board(hole, board)
            and not _hero_cannot_lose()
            and call_chips >= max(int(pot * 0.18), 1)):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: CO weak two-pair paired board — fold")

    # EP/MP/CO pocket 77–QQ on ace-paired runout — 99 MP −448 (HL R12 #01).
    if (street != "Preflop" and call_chips > 0 and "fold" in available
            and position in ("UTG", "MP", "CO")
            and _hero_vulnerable_pocket_on_ace_paired_board(hole, board, hc)
            and not _hero_cannot_lose()
            and call_chips >= max(int(pot * 0.22), 1)):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: OOP pocket under ace pair — fold")

    # EP/MP/CO AK/AQ on paired runout — AK MP −624 on 8Ah4434 (HL R13 #01).
    if (street != "Preflop" and call_chips > 0 and "fold" in available
            and position in ("UTG", "MP", "CO")
            and _hero_ace_broadway_vulnerable_on_paired_board(hole, board, hc)
            and not _hero_cannot_lose()
            and call_chips >= max(int(pot * 0.22), 1)):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: ace broadway on paired board — fold")

    # SB/BB/EP/CO small pocket under board ace — 55 BB −225 (HL R14 #01).
    if (street != "Preflop" and call_chips > 0 and "fold" in available
            and position in ("UTG", "MP", "CO", "SB", "BB")
            and _hero_small_pocket_under_board_ace(hole, board, hc)
            and not _hero_cannot_lose()
            and call_chips >= max(int(pot * 0.22), 1)):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: small pocket under board ace — fold")

    # TT+ overpair on low straight-heavy board — KK −1132 on 86532 (HL R15 #01).
    if (street != "Preflop" and call_chips > 0 and "fold" in available
            and _pocket_vulnerable_on_low_straight_board(hole, board, hc)
            and not _hero_cannot_lose()):
        stack = _hero_stack_chips(table)
        ratio = call_chips / max(stack, 1)
        if hc in {"KK", "QQ"} and ratio >= 0.45:
            if call_chips >= max(int(pot * 0.28), 1):
                return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                              msg=f"{binding}: overpair on straight board — fold")
        elif (_medium_pocket_pair(hc) or _small_pocket_pair(hc)):
            if call_chips >= max(int(pot * 0.22), 1):
                return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                              msg=f"{binding}: pocket on straight board — fold")

    # SB/BB suited broadway on paired board — KQs BB −51 (HL R15 analyze #01).
    if (street != "Preflop" and call_chips > 0 and "fold" in available
            and position in ("SB", "BB") and not in_position
            and _oop_suited_broadway_vulnerable_paired(hole, board, hc)
            and not _hero_cannot_lose()
            and call_chips >= max(int(pot * 0.18), 1)):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: OOP suited broadway paired — fold")

    # BB OOP AK/AQ on A-high broadway flops — Kh As BB −116 on AJ4 (HL R10 #01).
    if (street != "Preflop" and call_chips > 0 and "fold" in available
            and position == "BB" and not in_position
            and _oop_vulnerable_ace_tptk(hole, board, hc)
            and call_chips >= max(int(pot * 0.32), 1)):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: BB vulnerable ace TPTK OOP — fold")

    # EP/MP/CO ace-x second pair — A9o MP −100 (HL R9 #14).
    if (street != "Preflop" and call_chips > 0 and "fold" in available
            and position in ("UTG", "MP", "CO")
            and len(board) >= 4
            and _marginal_ace_kicker(hc)
            and _ace_kicker_second_pair(hole, board)
            and call_chips >= max(int(pot * 0.28), 1)):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: EP weak ace second pair — fold")

    # UTG/MP — never open chart trash (35o UTG, 94o UTG — HL R4/R8).
    if (street == "Preflop" and is_preflop_open_spot(table, allowed, call_chips)
            and position in ("UTG", "MP")
            and _is_ep_preflop_trash(hc) and "fold" in available):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: EP trash — fold")

    # MP/UTG chart-trash vs any raise — K3o MP, Q9o MP (HL R5/R8).
    if (street == "Preflop" and call_chips > 0 and position in ("UTG", "MP")
            and _is_ep_preflop_trash(hc) and "fold" in available):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: EP trash vs raise — fold")

    # EP suited broadway — fold opens under protect/eval lanes (HL R8; not tournament baseline).
    if (street == "Preflop" and is_preflop_open_spot(table, allowed, call_chips)
            and lane_tight
            and position in ("UTG", "MP")
            and hc in _EP_SUITED_BROADWAY_TRAP and "fold" in available):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: EP suited broadway trap — fold open")

    # EP OOP weak suited ace on paired runout — A3s UTG −887 (HL R9 #01).
    if (street != "Preflop" and call_chips > 0 and "fold" in available
            and position in ("UTG", "MP") and not in_position
            and _is_weak_suited_ace(hc)
            and _board_is_paired(board)
            and len(board) >= 4
            and not _hero_made_hand_exempt(hole, board)
            and not _hero_cannot_lose()
            and call_chips >= max(int(pot * 0.10), 1)):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: EP weak suited ace paired board — fold")

    # EP OOP low suited trash on paired runout — 94s UTG −100 (HL R10 #02).
    if (street != "Preflop" and call_chips > 0 and "fold" in available
            and position in ("UTG", "MP") and not in_position
            and _is_ep_low_suited_trash(hc)
            and _board_is_paired(board)
            and len(board) >= 4
            and not _hero_made_hand_exempt(hole, board)
            and not _hero_cannot_lose()
            and call_chips >= max(int(pot * 0.10), 1)):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: EP low suited trash paired board — fold")

    # CO dominated broadway vs raise — QTo CO −100 preflop (HL R5 #09).
    if (street == "Preflop" and call_chips > 0 and position == "CO"
            and hc in _BB_BROADWAY_FOLD and "fold" in available):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: CO broadway trash vs raise — fold")

    hero_stack_early = _hero_stack_chips(table)
    if (street == "Preflop" and call_chips > 0 and "fold" in available
            and _preflop_stackoff_should_fold(
                hc, call_chips, hero_stack_early, position=position)
            and not _hero_cannot_lose()):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: preflop stack-off — fold")

    # CO/BTN weak broadway on paired river — ATo CO −100 (HL R4 #03).
    if (street != "Preflop" and call_chips > 0 and "fold" in available
            and position in ("CO", "MP", "BTN")
            and hc in _BB_BROADWAY_FOLD
            and _board_is_paired(board)
            and len(board) >= 5
            and not _hero_made_hand_exempt(hole, board)
            and not _hero_cannot_lose()
            and call_chips >= max(int(pot * 0.15), 1)):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: weak broadway on paired river — fold")

    # CO weak connector offsuit — never open or call preflop (98o CO −100 HL R11 #01).
    if (street == "Preflop" and position == "CO" and hc in _CO_WEAK_CONNECTOR
            and "fold" in available):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: CO weak connector — fold")

    # HL R26 #01: CO chart-trash opens under first_protect (62o CO −100 preflop).
    if (street == "Preflop" and first_protect and position == "CO"
            and hc in _WEAK_FACING_RAISE and "fold" in available):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: first_protect CO trash — fold")

    # HL R27 / S2 R3: CO/SB/BTN panel trash — protect/eval lanes only (tournament S1 ship).
    if (street == "Preflop" and lane_tight and position in ("CO", "SB", "BTN")
            and hc in _WEAK_FACING_RAISE and "fold" in available):
        if call_chips > 0 or position in ("CO", "BTN"):
            return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                          msg=f"{binding}: panel trash {position} — fold")
    if (street == "Preflop" and position == "SB" and call_chips == 0
            and _is_sb_complete_trash(hc) and "check" in available):
        return _build("check", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: SB complete trash — check")

    # CO/BTN: never call limps/raises with dominated trash (Q9o/Q5o multiway −100 HL R20/R21).
    if (street == "Preflop" and position in ("CO", "BTN") and call_chips > 0
            and _is_sb_complete_trash(hc) and "fold" in available):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: CO/BTN trash vs limp/raise — fold")

    # Live leak: never pay with bottom offsuit trash postflop (64o-type lines).
    trash_eq = _train_threshold("trash_fold_eq", 0.30)
    garbage_margin = _train_threshold("garbage_postflop_margin", 0.04)
    if (street != "Preflop" and call_chips > 0 and "fold" in available
            and _is_garbage_offsuit(hc)
            and equity < max(pot_odds + garbage_margin, trash_eq)):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: trash hand vs bet — fold")

    # HL R6 #01 / R13 #01 / R23 #01 — CO/BTN trash on paired runouts (J2o, 63s).
    if (street != "Preflop" and call_chips > 0 and "fold" in available
            and position in ("CO", "BTN")
            and _is_paired_runout_trash_hand(hc)
            and _board_is_paired(board)
            and not _hero_made_hand_exempt(hole, board)
            and not _hero_cannot_lose()):
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: CO/BTN trash on paired board — fold")

    # PokerSkill library / stub: explicit fold when facing a bet (weak hands only).
    if (ps_bias == "fold" and call_chips > 0 and "fold" in available
            and (_should_fold_weak_preflop(chart.get("hand_class") or "", equity, pot_odds)
                 or equity < pot_odds + 0.04)):
        action_name, amount = "fold", None
    # Chart drives opens — library bias can nudge HU opens/checks.
    elif street == "Preflop" and is_preflop_open_spot(table, allowed, call_chips):
        eff = _effective_preflop_open(suggested, ps_library, ps_bias, equity)
        action_name, amount = _preflop_open(
            eff, allowed, available, pot, equity,
            hand_class=hc,
            position=position, ps_bias=ps_bias, ps_library=ps_library,
            hud_mode=hud_mode, margins=margins, cold_start=cold_start,
            lead_protect=lead_protect, qual_protect=qual_protect,
            first_protect=first_protect, eval_panel=eval_panel,
            lane_tight=lane_tight)
    elif street == "Preflop" and call_chips > 0:
        nemesis_ctx = ctx.get("nemesis_handles")
        handles = (
            frozenset(str(h).lower() for h in nemesis_ctx)
            if nemesis_ctx else nemesis_handles()
        )
        nemesis_opener = False
        if _nemesis_tight_enabled():
            nemesis_opener = table_nemesis_pressure(table, handles)
        bb = int(table.get("bigBlindChips") or 20)
        hero_stack = _hero_stack_chips(table)
        action_name, amount = _preflop_vs_bet(
            chart, allowed, available, equity, pot_odds, call_chips, pot,
            in_position=in_position, ps_bias=ps_bias, ps_library=ps_library,
            hud_mode=hud_mode, margins=margins, lead_protect=lead_protect,
            qual_protect=qual_protect, first_protect=first_protect,
            nemesis_opener=nemesis_opener, eval_panel=eval_panel,
            lane_tight=lane_tight,
            ko_survival=ko_survival, cold_start=cold_start, hud=hud,
            hero_stack_chips=hero_stack, big_blind=bb)
    elif call_chips == 0:
        action_name, amount = _postflop_free(
            equity, allowed, available, pot, pot_control=pot_control,
            ps_bias=ps_bias, ps_library=ps_library,
            hand_eval=ps_hand_eval,
            hand_class=hc, hud_mode=hud_mode, margins=margins)
    else:
        action_name, amount = _postflop_facing_bet(
            equity, pot_odds, allowed, available, call_chips, pot,
            in_position=in_position, pot_control=pot_control,
            hand_class=hc,
            hole=hole, board=board, ps_bias=ps_bias, ps_library=ps_library,
            hand_eval=ps_hand_eval, hud_mode=hud_mode, margins=margins,
            table=table, position=position, lead_protect=lead_protect,
            max_playable=max_playable)

    if action_name in ("fold", "check", "call"):
        amount = None

    msg = _message(
        action_name, equity, pot_odds, binding, suggested, hud_mode=hud_mode,
        survival=survival, deadline_s=deadline_s, villain_mem=villain_mem,
        candor_fold=(action_name == "fold"))
    out = _build(action_name, amount, table, allowed, eq=equity, po=pot_odds, msg=msg)
    out = _apply_chip_reserve(out, max_playable, table, hc)
    out["reasoning"] = _skill_reasoning(
        out.get("reasoning", ""), binding, suggested, chart, ps, hud_mode=hud_mode)
    return out


def _effective_preflop_open(
    suggested: Optional[str],
    ps_library: bool,
    ps_bias: Optional[str],
    equity: float,
) -> str:
    """Merge chart open with PokerSkill library nudges (HU priority)."""
    base = suggested or "check"
    if not ps_library or not ps_bias:
        return base
    if ps_bias == "check":
        return "check"
    if ps_bias == "raise" and equity > 0.45:
        return "raise"
    if ps_bias == "fold":
        return "fold"
    return base


def _is_garbage_offsuit(hc: str) -> bool:
    """Bottom offsuit trash — no postflop calls without a strong price edge."""
    if not hc:
        return False
    return hc in _WEAK_FACING_RAISE or _is_low_trash_offsuit(hc)


def _should_block_chart_open(
    hand_class: str,
    position: str,
    *,
    lead_protect: bool = False,
) -> bool:
    """Block chart-suggested opens for trash (KTo UTG, K8o CO chart bypass)."""
    if position in ("UTG", "MP"):
        return hand_class in _WEAK_FACING_RAISE
    if position in ("CO", "BTN"):
        if hand_class in _WEAK_FACING_RAISE:
            if lead_protect and lead_blind_steal(hand_class, position):
                return False
            return True
    if position == "SB" and (
        hand_class in _WEAK_FACING_RAISE or _is_sb_complete_trash(hand_class)
    ):
        return True
    return _blocks_open_steal(hand_class, position) and position in ("CO", "BTN")


def _blocks_open_steal(hand_class: str, position: str) -> bool:
    """Chart-fold trash — never open-steal (J2o CO leak vs rock HUD)."""
    if position in ("UTG", "MP"):
        return True
    if not hand_class:
        return True
    if hand_class in _WEAK_FACING_RAISE or _is_low_trash_offsuit(hand_class):
        return True
    if _is_sb_complete_trash(hand_class):
        return True
    # CO/BTN: block wheel + low broadway offsuit steals (J4o, T3o, …).
    if position in ("CO", "BTN") and len(hand_class) == 3 and hand_class[2] == "o":
        if hand_class[0] == hand_class[1]:
            return False
        hi, lo = _RANKS.index(hand_class[0]), _RANKS.index(hand_class[1])
        if hi <= 9 and lo <= 4:
            return True
    return False


def _preflop_open(suggested: str, allowed: dict, available: list,
                  pot: int, equity: float,
                  hand_class: str = "", position: str = "",
                  ps_bias: Optional[str] = None,
                  ps_library: bool = False,
                  hud_mode: str = "unknown",
                  margins: Optional[dict] = None,
                  cold_start: bool = False,
                  lead_protect: bool = False,
                  qual_protect: bool = False,
                  first_protect: bool = False,
                  eval_panel: bool = False,
                  lane_tight: bool = False) -> tuple[str, Optional[int]]:
    margins = margins or exploit_margins(hud_mode)
    if (position == "SB" and _weak_ace_offsuit(hand_class)
            and suggested == "raise" and "check" in available):
        return "check", None
    if (position == "SB" and _is_sb_complete_trash(hand_class)
            and "check" in available):
        return "check", None
    if ps_library and ps_bias == "check" and "check" in available:
        return "check", None
    # Seat matrix v2 — SB/BB never open non-premium trash (S2 audit blind bleed).
    if (seat_matrix_v2_enabled() and position in ("SB", "BB")
            and hand_class not in _NEMESIS_SB_DEFEND_OK
            and hand_class in _WEAK_FACING_RAISE and "fold" in available):
        return "fold", None
    # EP: chart-only — no HUD steals (74o MP -916 leak).
    if position in ("UTG", "MP") and _is_ep_preflop_trash(hand_class) and "fold" in available:
        return "fold", None
    if (lane_tight and position in ("UTG", "MP") and hand_class in _EP_SUITED_BROADWAY_TRAP
            and "fold" in available):
        return "fold", None
    if (seat_matrix_v2_enabled() and position == "UTG"
            and hand_class not in {
                "AA", "KK", "QQ", "JJ", "TT", "99", "88", "77",
                "AKs", "AKo", "AQs", "AQo", "AJs", "KQs",
            } and "fold" in available):
        return "fold", None
    if position in ("UTG", "MP") and suggested != "raise":
        if "fold" in available:
            return "fold", None
        if "check" in available:
            return "check", None
    # HL R27 / S2 R3: CO/SB/BTN chart-trash — protect/eval lanes only (tournament S1).
    if (lane_tight and position in ("CO", "SB", "BTN") and hand_class in _WEAK_FACING_RAISE
            and "fold" in available):
        return "fold", None
    # HL R8: EP suited-broadway opens off (always-on — eval + playground).
    # HL R26 #01: CO chart-trash — no opens while chip #1 (62o/Q2o CO −100).
    if (first_protect and position == "CO" and hand_class in _WEAK_FACING_RAISE
            and "fold" in available):
        return "fold", None
    # Qual/lead protect: CO/BTN chart-only — no HUD steals (K8o/T7o CO −100 leaks).
    if (qual_protect or lead_protect) and position in ("CO", "BTN") and suggested != "raise":
        if (lead_protect and not first_protect and lead_blind_steal(hand_class, position)
                and allowed.get("canBet") and "bet" in available):
            br = allowed.get("betRange") or {}
            min_bet = int(br.get("min") or max(int(pot * 0.5), 1))
            max_bet = int(br.get("max") or min_bet)
            target = max(min_bet, min(int(pot * 0.5), max_bet))
            return "bet", target
        if "fold" in available:
            return "fold", None
        if "check" in available:
            return "check", None
    # Cold start: chart-only CO/BTN opens — no marginal steals until HUD sample (HL R21).
    if (_cold_start_no_steal_enabled() and cold_start and position in ("CO", "BTN")
            and suggested == "raise" and hand_class not in _COLD_START_OPEN_OK):
        if "check" in available:
            return "check", None
        if "fold" in available:
            return "fold", None
    # vs rock: steal when chart is passive but equity supports an open (CO/BTN only).
    steal_eq = float(margins.get("open_steal_equity", 0.99))
    if (not lead_protect and not qual_protect and not cold_start and hud_mode == "rock"
            and suggested in ("check", "fold")
            and position in ("CO", "BTN")
            and equity >= steal_eq and allowed.get("canBet") and "bet" in available
            and not _is_sb_complete_trash(hand_class)
            and not _blocks_open_steal(hand_class, position)):
        br = allowed.get("betRange") or {}
        min_bet = int(br.get("min") or max(int(pot * 0.5), 1))
        max_bet = int(br.get("max") or min_bet)
        target = max(min_bet, min(int(pot * 0.5), max_bet))
        return "bet", target
    if (suggested == "raise" and allowed.get("canBet") and "bet" in available
            and not _should_block_chart_open(hand_class, position, lead_protect=lead_protect)
            and not (
                _cold_start_no_steal_enabled()
                and cold_start
                and position in ("CO", "BTN")
                and hand_class not in _COLD_START_OPEN_OK
            )):
        br = allowed.get("betRange") or {}
        min_bet = int(br.get("min") or max(int(pot * 0.5), 1))
        max_bet = int(br.get("max") or min_bet)
        target = max(min_bet, min(int(pot * 0.55), max_bet))
        return "bet", target
    if suggested == "fold" and "fold" in available:
        return "fold", None
    if "check" in available:
        return "check", None
    return ("call" if "call" in available else "fold"), None


def _preflop_vs_bet(chart: dict, allowed: dict, available: list,
                    equity: float, pot_odds: float, call_chips: int,
                    pot: int, *, in_position: bool,
                    ps_bias: Optional[str] = None,
                    ps_library: bool = False,
                    hud_mode: str = "unknown",
                    margins: Optional[dict] = None,
                    lead_protect: bool = False,
                    qual_protect: bool = False,
                    first_protect: bool = False,
                    nemesis_opener: bool = False,
                    eval_panel: bool = False,
                    lane_tight: bool = False,
                    ko_survival: bool = False,
                    cold_start: bool = False,
                    hud: Optional[dict] = None,
                    hero_stack_chips: int = 0,
                    big_blind: int = 20) -> tuple[str, Optional[int]]:
    margins = margins or exploit_margins(hud_mode)
    hc = chart.get("hand_class") or ""
    position = chart.get("position") or ""
    suggested = chart.get("suggested_action") or "fold"
    hud = hud or {}

    # Premium-nit / tight-measured — overfold vs aggression (S2 audit HUD PCI).
    pci = float(hud.get("premium_concentration") or 0.0)
    if pci <= 0.0 and hud.get("stats"):
        pci = premium_concentration_index(hud["stats"])
    arch = (hud.get("archetype") or "").lower()
    if (pci >= 0.45 or arch == "premium_nit") and call_chips > 0:
        nit_premium = frozenset({
            "AA", "KK", "QQ", "JJ", "AKs", "AKo", "AQs",
        })
        if hc not in nit_premium and "fold" in available:
            ratio = call_chips / max(hero_stack_chips, 1)
            if ratio >= 0.12 or call_chips >= big_blind * 4:
                return "fold", None

    # Preflop stack-off discipline — fold dominated trash vs large commits (HL S2 R3 −100 cluster).
    if (_preflop_stackoff_should_fold(
            hc, call_chips, hero_stack_chips, position=position)
            and "fold" in available):
        return "fold", None

    jeff_4b = try_jeff_nemesis_4bet(
        hand_class=hc,
        call_chips=call_chips,
        big_blind=big_blind,
        allowed=allowed,
        available=available,
        hero_stack_chips=hero_stack_chips,
        villain_handle=str(hud.get("villain_handle") or ""),
    )
    if jeff_4b:
        return jeff_4b

    iso_lp = try_iso_vs_wide_passive_limp(
        hand_class=hc,
        position=position,
        call_chips=call_chips,
        pot=pot,
        allowed=allowed,
        available=available,
        hero_stack_chips=hero_stack_chips,
        big_blind=big_blind,
        hud=hud,
    )
    if iso_lp:
        return iso_lp

    # Static chart is open-range only — facing a raise, downgrade spurious "raise" (77 MP −100).
    if call_chips > 0 and suggested == "raise" and hc not in _PREFLOP_3BET_OK:
        suggested = "fold"

    # BB: never defend chart-trash vs raises (Q6o BB −100 — IP preflop pricing leak).
    if (position == "BB" and call_chips > 0 and hc in _WEAK_FACING_RAISE
            and hc not in {"AA", "KK", "QQ", "JJ", "TT", "AKs", "AKo", "AQs", "AQo"}
            and "fold" in available):
        return "fold", None

    # BB: fold dominated broadway vs opens (KQo BB −100 analyze #10).
    if (position == "BB" and call_chips > 0 and hc in _BB_BROADWAY_FOLD
            and "fold" in available):
        return "fold", None

    # SB: fold dominated broadway vs opens (QJo SB −100 HL R22 #01).
    if (position == "SB" and call_chips > 0 and hc in _BB_BROADWAY_FOLD
            and "fold" in available):
        return "fold", None

    # SB: fold marginal ace vs any open (A6o SB −100 HL R4 #02).
    if (position == "SB" and call_chips > 0 and _marginal_ace_kicker(hc)
            and "fold" in available):
        return "fold", None

    # BB: fold low suited trash vs opens (T2s, 98s — HL R6 #04/#05).
    if (position == "BB" and call_chips > 0 and _is_bb_suited_trash(hc)
            and "fold" in available):
        return "fold", None

    # CO: fold weak connector trash vs any raise (98o CO −100 HL R11 #01).
    if (position == "CO" and call_chips > 0 and hc in _CO_WEAK_CONNECTOR
            and "fold" in available):
        return "fold", None

    # HL R27 / S2 R3: CO/SB/BTN chart-trash vs raise — protect/eval lanes only.
    if (lane_tight and position in ("CO", "SB", "BTN") and call_chips > 0
            and hc in _WEAK_FACING_RAISE and "fold" in available):
        return "fold", None

    # HL R26 #01: CO chart-trash vs raise under first_protect (62o shove traps).
    if (first_protect and position == "CO" and call_chips > 0
            and hc in _WEAK_FACING_RAISE and "fold" in available):
        return "fold", None

    # EP/MP: no medium-pair calls vs raises (77 MP −100 analyze #02).
    if (position in ("UTG", "MP") and call_chips > 0
            and hc in _LOW_PAIRS_PROTECT and "fold" in available):
        return "fold", None

    # EP chart-trash vs raise — protect/eval lanes (tournament baseline uses chart).
    if (lane_tight and position in ("UTG", "MP") and call_chips > 0
            and hc in _WEAK_FACING_RAISE and "fold" in available):
        return "fold", None

    # CO broadway trash vs raise — QTo CO −100 (HL R5 #09).
    if (position == "CO" and call_chips > 0 and hc in _BB_BROADWAY_FOLD
            and "fold" in available):
        return "fold", None

    # HL R8: EP suited broadway vs raise — protect/eval lanes (eval shove traps).
    if (lane_tight and position in ("UTG", "MP") and call_chips > 0
            and hc in _EP_SUITED_BROADWAY_TRAP and "fold" in available):
        return "fold", None

    # v12 / nemesis opens — fold EP suited broadway even IP to the open.
    if (nemesis_opener and position in ("UTG", "MP", "CO", "BTN") and call_chips > 0
            and hc in _EP_SUITED_BROADWAY_TRAP and "fold" in available):
        return "fold", None

    # Lead protect: no wide CO/BTN defends — chart + premiums only.
    if (lead_protect and position in ("CO", "BTN")
            and hc not in {"AA", "KK", "QQ", "JJ", "TT", "AKs", "AKo", "AQs", "AQo"}
            and suggested == "fold" and "fold" in available):
        return "fold", None
    # BB: defend priced pairs/suited only — no broadway/trash float (KQo/J4o leaks).
    if (lead_protect and position == "BB" and suggested != "fold"
            and not _is_bb_float_trash(hc)
            and equity >= pot_odds + 0.02 and "call" in available):
        return "call", None

    # SB: fold weak suited trash vs opens (K9s SB −100 HL R14 #06).
    if (position == "SB" and call_chips > 0 and hc in _SB_WEAK_SUITED_VS_OPEN
            and "fold" in available):
        return "fold", None

    # Nemesis tight: SB vs known hunters — premiums only (HL R21 S1a export).
    if (nemesis_opener and position == "SB" and call_chips > 0
            and hc not in _NEMESIS_SB_DEFEND_OK and "fold" in available):
        return "fold", None

    if exploit_lane_active(
        qual_protect=qual_protect,
        first_protect=first_protect,
        ko_survival=ko_survival,
        eval_panel=eval_panel,
        cold_start=cold_start,
        hud_mode=hud_mode,
        hero_stack_bb=hero_stack_chips / max(big_blind, 1),
        hud=hud,
        nemesis_opener=nemesis_opener,
    ):
        lag_3b = try_three_bet_lag_vs_open(
            hand_class=hc,
            position=position,
            call_chips=call_chips,
            pot=pot,
            allowed=allowed,
            available=available,
            hero_stack_chips=hero_stack_chips,
            big_blind=big_blind,
        )
        if lag_3b:
            return lag_3b
        trap = try_trap_aa_kk_vs_3bet(
            hand_class=hc,
            call_chips=call_chips,
            big_blind=big_blind,
            available=available,
            hero_stack_chips=hero_stack_chips,
            hud=hud,
        )
        if trap:
            return trap
        defend = try_defend_bb_vs_steal(
            hand_class=hc,
            position=position,
            call_chips=call_chips,
            pot_odds=pot_odds,
            equity=equity,
            available=available,
            hero_stack_chips=hero_stack_chips,
        )
        if defend:
            return defend

    # SB: never complete/call/defend with chart trash (83o/72o −100 preflop leaks).
    _sb_defend_premium = frozenset({"AA", "KK", "QQ", "JJ", "TT", "AKs", "AKo", "AQs"})
    if (position == "SB" and _is_sb_complete_trash(hc) and hc not in _sb_defend_premium
            and "fold" in available):
        return "fold", None

    if ps_library and ps_bias == "fold" and "fold" in available:
        if _should_fold_weak_preflop(hc, equity, pot_odds) or equity < pot_odds + 0.04:
            return "fold", None
    if ps_library and ps_bias == "call" and equity >= pot_odds and "call" in available:
        return "call", None

    if _should_fold_weak_preflop(hc, equity, pot_odds) and "fold" in available:
        return "fold", None
    # EP facing raise: strict chart — no wide defends (MP/UTG VPIP leak).
    if (position in ("UTG", "MP") and suggested == "fold"
            and hc not in {"AA", "KK", "QQ", "JJ", "AKs", "AKo"}
            and "fold" in available):
        return "fold", None
    if (position in ("UTG", "MP") and suggested == "fold"
            and equity < pot_odds + 0.10 and "fold" in available):
        return "fold", None
    # SB OOP: don't defend chart-fold trash without a clear price edge.
    if (position == "SB" and suggested == "fold"
            and equity < pot_odds + 0.08 and "fold" in available):
        return "fold", None
    if (_is_low_trash_offsuit(hc) and not in_position
            and equity < pot_odds + 0.06 and "fold" in available):
        return "fold", None
    # BTN/IP: 64o–98o trash — fold vs opens without a clear edge (S28 64o leak).
    if (in_position and _is_low_trash_offsuit(hc)
            and equity < pot_odds + _train_threshold("ip_trash_margin", 0.06)
            and "fold" in available):
        return "fold", None
    # BTN/IP: weak offsuit aces fold vs raises without a solid edge.
    if (in_position and _weak_ace_offsuit(hc)
            and equity < pot_odds + 0.08 and "fold" in available):
        return "fold", None
    premium = hc in {"AA", "KK", "QQ", "JJ", "AKs", "AKo"}
    strong_3bet = premium or (in_position and hc in {"AQs", "AQo", "TT"})
    if strong_3bet and equity > 0.52 and allowed.get("canRaise") and "raise" in available:
        rr = allowed.get("raiseRange") or {}
        min_r = int(rr.get("min") or call_chips * 2)
        max_r = int(rr.get("max") or min_r)
        target = max(min_r, min(int(pot * 0.75 + call_chips * 2.5), max_r))
        return "raise", target
    call_margin = 0.03 if in_position else 0.06
    fold_margin = 0.08 if in_position else 0.05
    if position in ("UTG", "MP"):
        call_margin += 0.05
        fold_margin -= 0.03
    call_margin += float(margins.get("call_margin_delta", 0))
    fold_margin += float(margins.get("preflop_fold_margin_delta", 0))
    # vs rock: their raise is polarized — fold more marginal opens.
    if hud_mode == "rock" and not premium and not strong_3bet:
        fold_margin += 0.03
    if equity >= pot_odds + call_margin and "call" in available:
        return "call", None
    if equity < pot_odds - fold_margin and "fold" in available:
        return "fold", None
    return ("call" if "call" in available else "fold"), None


def _should_fold_weak_preflop(hc: str, equity: float, pot_odds: float) -> bool:
    """Fold dominated trash preflop unless MC equity clears price with margin."""
    if not hc:
        return False
    if hc not in _WEAK_FACING_RAISE:
        return False
    # Weak aces / broadways need a clear edge, not a marginal call.
    return equity < pot_odds + _train_threshold("weak_preflop_margin", 0.07)


def _is_low_suited_wheel(hc: str) -> bool:
    """9-high and below suited wheel — 95s SB paired ace leak (HL S2 R3 #01)."""
    if len(hc) != 3 or hc[2] != "s" or hc[0] == hc[1]:
        return False
    i1, i2 = _RANKS.index(hc[0]), _RANKS.index(hc[1])
    hi, lo = max(i1, i2), min(i1, i2)
    return hi <= _RANKS.index("9") and lo <= _RANKS.index("5")


def _is_ep_low_suited_trash(hc: str) -> bool:
    """EP opens with low suited junk (65s UTG −100 HL R8)."""
    if len(hc) != 3 or hc[2] != "s" or hc[0] == hc[1]:
        return False
    hi, lo = _RANKS.index(hc[0]), _RANKS.index(hc[1])
    hi, lo = max(hi, lo), min(hi, lo)
    if hi > _RANKS.index("T"):
        return False
    return lo <= _RANKS.index("6") and hi <= _RANKS.index("9")


def _is_weak_suited_ace(hc: str) -> bool:
    """A2s–A6s — EP open/stack-off traps (A3s UTG −887 HL R9)."""
    if len(hc) != 3 or hc[2] != "s" or hc[0] != "A" or hc[1] == "A":
        return False
    kicker = _RANKS.index(hc[1])
    return kicker <= _RANKS.index("6")


def _is_ep_preflop_trash(hc: str) -> bool:
    """UTG/MP chart trash — offsuit wheel + low suited opens."""
    if not hc:
        return False
    if hc in _WEAK_FACING_RAISE or _is_low_trash_offsuit(hc):
        return True
    if _is_weak_suited_ace(hc) or _is_ep_low_suited_trash(hc):
        return True
    return False


def _preflop_stackoff_should_fold(
    hc: str,
    call_chips: int,
    hero_stack_chips: int,
    *,
    position: str = "",
) -> bool:
    """Fold non-premium vs large preflop commits (empty-board −100 cluster)."""
    if call_chips <= 0 or hero_stack_chips <= 0 or not hc:
        return False
    if hc in _PREFLOP_3BET_OK:
        return False
    ratio = call_chips / hero_stack_chips
    if hc in {"AA", "KK", "QQ", "AKs", "AKo"}:
        return False
    if hc in {"JJ", "TT", "AQs"}:
        return ratio >= 0.40
    if hc in {"99", "88", "AQo", "AJs", "KQs"}:
        return ratio >= 0.25
    if ratio >= 0.40:
        return True
    if ratio >= 0.18 and hc in _WEAK_FACING_RAISE:
        return True
    if ratio >= 0.18 and _is_low_trash_offsuit(hc):
        return True
    if ratio >= 0.18 and _marginal_ace_kicker(hc):
        return True
    if ratio >= 0.18 and hc in _EP_SUITED_BROADWAY_TRAP:
        return True
    if (ratio >= 0.18 and position in ("UTG", "MP")
            and hc in {"ATs", "A9s", "A8s", "KJs", "KTs", "QTs"}):
        return True
    if ratio >= 0.22 and (
        _is_sb_complete_trash(hc)
        or hc in _CO_WEAK_CONNECTOR
        or hc in _BB_BROADWAY_FOLD
        or _is_ep_low_suited_trash(hc)
    ):
        return True
    return False


def _weak_ace_offsuit(hc: str) -> bool:
    return len(hc) == 3 and hc[0] == "A" and hc[2] == "o"


def _marginal_ace_kicker(hc: str) -> bool:
    """A9 and worse — ace with low kicker (suited or offsuit)."""
    if len(hc) != 3 or hc[0] != "A":
        return False
    return _RANKS.index(hc[1]) <= _RANKS.index("9")


def _is_king_low_offsuit(hc: str) -> bool:
    """K5o and below — K3o SB ace-paired leak (HL R5 #03)."""
    if len(hc) != 3 or hc[0] != "K" or hc[2] != "o" or hc[0] == hc[1]:
        return False
    return _RANKS.index(hc[1]) <= _RANKS.index("5")


def _ace_kicker_second_pair(hole: list[str], board: list[str]) -> bool:
    """Axo low card paired, ace kicker only — second pair (A9 on T9xxx)."""
    if len(hole) != 2 or len(board) < 3:
        return False
    hranks = [c[0].upper() for c in hole]
    if hranks[0] == hranks[1] or "A" not in hranks:
        return False
    low = hranks[1] if hranks[0] == "A" else hranks[0]
    branks = [c[0].upper() for c in board]
    if low not in branks or "A" in branks:
        return False
    top_board = max(branks, key=lambda r: _RANKS.index(r))
    return _RANKS.index(low) < _RANKS.index(top_board)


def _is_low_trash_offsuit(hc: str) -> bool:
    """Both ranks below T, offsuit, unpaired — live SB leak hands."""
    if len(hc) != 3 or hc[2] != "o" or hc[0] == hc[1]:
        return False
    i1, i2 = _RANKS.index(hc[0]), _RANKS.index(hc[1])
    return i1 < 8 and i2 < 8


def _hero_has_ace_on_paired_ace_board(hole: list[str], board: list[str]) -> bool:
    """Hero holds an ace when the board is paired with aces (trips+)."""
    if len(hole) != 2 or not _board_has_ace_pair(board):
        return False
    return any(c[0].upper() == "A" for c in hole)


def _hero_small_pocket_under_board_ace(
    hole: list[str], board: list[str], hc: str,
) -> bool:
    """22–99 under board ace — dominated (55 BB −225 on 2c7hAsT9d HL R14)."""
    if len(board) < 4 or not _board_has_ace(board):
        return False
    if not _small_pocket_pair(hc):
        return False
    if _hero_made_hand_exempt(hole, board) or _hero_pocket_set(hole, board):
        return False
    return _RANKS.index(hc[0]) < _RANKS.index("A")


def _hero_ace_broadway_vulnerable_on_paired_board(
    hole: list[str], board: list[str], hc: str,
) -> bool:
    """AK/AQ two-pair on paired runout — dominated by any board-pair trips (AK MP −624)."""
    if len(board) < 4 or not _board_is_paired(board):
        return False
    if hc not in {"AKs", "AKo", "AQs", "AQo"}:
        return False
    if _hero_made_hand_exempt(hole, board) or _hero_boat_or_quads_on_paired_board(
        hole, board,
    ):
        return False
    hranks = [c[0].upper() for c in hole]
    if "A" not in hranks:
        return False
    branks = [c[0].upper() for c in board]
    bc = Counter(branks)
    for r in hranks:
        if bc.get(r, 0) >= 2:
            return False
    return True


def _hero_vulnerable_pocket_on_ace_paired_board(
    hole: list[str], board: list[str], hc: str,
) -> bool:
    """Pocket 77–QQ on AAx without set/boat — dominated two pair (99 MP −448 HL R12)."""
    if not _board_has_ace_pair(board) or len(board) < 4:
        return False
    if not (_small_pocket_pair(hc) or _medium_pocket_pair(hc)):
        return False
    if _hero_made_hand_exempt(hole, board) or _hero_pocket_set(hole, board):
        return False
    if _hero_boat_or_quads_on_paired_board(hole, board):
        return False
    hranks = [c[0].upper() for c in hole]
    if len(hranks) != 2 or hranks[0] != hranks[1]:
        return False
    branks = [c[0].upper() for c in board]
    return hranks[0] not in branks


def _hero_weak_two_pair_on_paired_board(hole: list[str], board: list[str]) -> bool:
    """Small hole-board pair + board pair — dominated two-pair (Q7 on 3T7338)."""
    if len(hole) != 2 or len(board) < 4 or not _board_is_paired(board):
        return False
    if _hero_made_hand_exempt(hole, board):
        return False
    hranks = [c[0].upper() for c in hole]
    branks = [c[0].upper() for c in board]
    bc = Counter(branks)
    if hranks[0] == hranks[1]:
        pocket = hranks[0]
        on_board = bc.get(pocket, 0)
        if on_board == 1:
            return False
        if on_board == 0 and _RANKS.index(pocket) >= _RANKS.index("T"):
            return False
        return False
    singletons = {r for r, n in bc.items() if n == 1}
    matches = [r for r in hranks if r in singletons]
    if not matches:
        return False
    pair_rank = max(matches, key=lambda r: _RANKS.index(r))
    top_board = max(branks, key=lambda r: _RANKS.index(r))
    return _RANKS.index(pair_rank) < _RANKS.index(top_board)


def _hero_made_hand_exempt(hole: list[str], board: list[str]) -> bool:
    """Skip trash-class postflop fold guards — set+, boat+, top trips (not bottom trips)."""
    if len(hole) != 2 or len(board) < 3:
        return False
    if _hero_pocket_set(hole, board):
        return True
    if _hero_boat_or_quads_on_paired_board(hole, board):
        return True
    if not _board_is_paired(board):
        return False
    hranks = [c[0].upper() for c in hole]
    branks = [c[0].upper() for c in board]
    bc = Counter(branks)
    top_board = max(branks, key=lambda r: _RANKS.index(r))
    for r in hranks:
        if bc.get(r, 0) >= 2:
            if r == "A" or _RANKS.index(r) >= _RANKS.index(top_board):
                return True
    return False


def _weak_ace_vulnerable_on_paired_board(hole: list[str], board: list[str], hc: str) -> bool:
    """Weak ace-x that missed trips on a paired board — not A9 on AAx."""
    if _hero_made_hand_exempt(hole, board):
        return False
    if not _weak_ace_offsuit(hc) or not _board_is_paired(board):
        return False
    return not _hero_has_ace_on_paired_ace_board(hole, board)


def _is_wheel_offsuit(hc: str) -> bool:
    """9-high and below wheel offsuit — J3o SB flop −100 (HL R17 #01)."""
    if len(hc) != 3 or hc[2] != "o" or hc[0] == hc[1]:
        return False
    hi, lo = max(_RANKS.index(hc[0]), _RANKS.index(hc[1])), min(
        _RANKS.index(hc[0]), _RANKS.index(hc[1])
    )
    return hi <= 9 and lo <= 4


def _is_paired_runout_trash(hc: str) -> bool:
    """J-x low and wheel trash — never pay on paired boards (J2d CO −2072).

    Rank/suit bands only — do not mirror _WEAK_FACING_RAISE (preflop set).
    """
    if _is_low_trash_offsuit(hc):
        return True
    if _is_low_suited_wheel(hc):
        return True
    if len(hc) != 3 or hc[0] == hc[1]:
        return False
    i1, i2 = _RANKS.index(hc[0]), _RANKS.index(hc[1])
    hi, lo = max(i1, i2), min(i1, i2)
    if hi <= 9 and lo <= 4:
        return True
    return False


def _is_paired_runout_trash_hand(hc: str) -> bool:
    """Offsuit wheel + low suited junk on paired runouts (63s CO −100 HL R23 #01)."""
    return _is_paired_runout_trash(hc) or _is_sb_suited_trash(hc)


def _marginal_offsuit_top_pair(hc: str) -> bool:
    """T6o/K6o-style top pair weak kicker (MP −290 on paired runout)."""
    if _weak_top_pair_offsuit(hc):
        return True
    if len(hc) != 3 or hc[2] != "o" or hc[0] == hc[1]:
        return False
    hi, lo = _RANKS.index(hc[0]), _RANKS.index(hc[1])
    return hi <= 9 and lo <= 7


def _is_sb_suited_trash(hc: str) -> bool:
    """Low suited junk SB completes (43s −100; 49s −2085; K3s HL R17 #04)."""
    if len(hc) != 3 or hc[2] != "s" or hc[0] == hc[1]:
        return False
    hi, lo = _RANKS.index(hc[0]), _RANKS.index(hc[1])
    if hi == _RANKS.index("K") and lo <= 4:
        return True
    return hi <= 9 and lo <= 4


def _is_bb_float_trash(hc: str) -> bool:
    """BB hands that must not float vs opens under lead/first protect (J4o HL R15 #08)."""
    if hc in _BB_BROADWAY_FOLD or hc in _WEAK_FACING_RAISE:
        return True
    if _is_low_trash_offsuit(hc) or _is_bb_suited_trash(hc):
        return True
    return False


def _is_bb_suited_trash(hc: str) -> bool:
    """Low suited junk BB floats (T2s, 98s — HL R6 #04/#05)."""
    if len(hc) != 3 or hc[2] != "s" or hc[0] == hc[1]:
        return False
    if _is_sb_suited_trash(hc):
        return True
    hi, lo = _RANKS.index(hc[0]), _RANKS.index(hc[1])
    if hi <= 6 and lo <= 4:
        return True
    return hc in {"J8s", "T8s", "K8s"}


def _is_sb_complete_trash(hc: str) -> bool:
    """Hands SB should never open — complete or fold only."""
    if not hc:
        return False
    if hc in _WEAK_FACING_RAISE or _is_low_trash_offsuit(hc):
        return True
    if _weak_ace_offsuit(hc) or _is_sb_suited_trash(hc):
        return True
    return hc in {"K9o", "Q9o", "Q8o", "Q7o", "Q6o", "Q5o", "Q4o", "Q3o", "Q2o",
                  "J9o", "T9o", "T8o", "T7o", "T6o", "T5o",
                  "97o", "86o", "75o", "J8o", "96o", "85o", "74o"}


def _board_paired_hero_missed(hole: list[str], board: list[str]) -> bool:
    """True when board is paired/trips and hero did not connect."""
    if len(board) < 3 or len(hole) != 2:
        return False
    branks = [c[0].upper() for c in board]
    bc = Counter(branks)
    if not any(v >= 2 for v in bc.values()):
        return False
    hranks = {c[0].upper() for c in hole}
    return not any(bc.get(r, 0) >= 2 for r in hranks)


def _hero_stack_chips(table: dict) -> int:
    sn = table.get("selfSeatNumber")
    for seat in table.get("seats") or []:
        if seat.get("seatNumber") == sn:
            return int(seat.get("stackChips") or 0)
    return 0


def _effective_stack_chips(table: dict, max_playable: int | None) -> int:
    stack = _hero_stack_chips(table)
    if max_playable is None:
        return stack
    return min(stack, int(max_playable))


def _emergency_made_hand_action(
    table: dict,
    allowed: dict,
    available: list[str],
    hole: list[str],
    board: list[str],
    street: str,
    pot: int,
    call_chips: int,
) -> Optional[dict]:
    """Clock-pressure fast path — never fold royal / river nuts."""
    binding = "clock"
    if street != "Preflop" and _hero_made_royal_flush(hole, board):
        out = _royal_made_action(
            table, allowed, available, pot, binding=binding, call_chips=call_chips,
        )
        if out:
            return out
    if (_nuts_detect_enabled() and street == "River" and len(board) == 5
            and treys_available()):
        from table_chat_intel import nuts_extra_dead_cards

        extra_dead = nuts_extra_dead_cards(table, hole, board)
        unbeatable, _, _ = river_unbeatable(
            hole, board, extra_dead_arena=extra_dead or None,
        )
        if unbeatable:
            out = _unbeatable_made_action(table, allowed, available, pot, binding=binding)
            if out:
                return out
            if call_chips > 0 and "fold" in available:
                if "all-in" in available:
                    all_in_to = int(
                        allowed.get("allInToAmount") or allowed.get("maxCommit") or 0
                    )
                    if all_in_to > 0:
                        return _build("all-in", all_in_to, table, allowed, eq=0.99, po=0.0,
                                      msg=f"{binding}: river unbeatable — all-in")
                if "call" in available:
                    return _build("call", None, table, allowed, eq=0.99, po=0.0,
                                  msg=f"{binding}: river unbeatable — call")
    return None


def _clamp_sized_action_to_cap(
    action: str,
    amount: int,
    cap: int,
    table: dict,
    allowed: dict,
    available: list[str],
    *,
    eq: float,
    po: float,
    msg: str,
) -> dict:
    """Cap sized action; degrade to call/check/fold when cap is below legal min."""
    capped = min(amount, cap)
    if action == "bet":
        br = allowed.get("betRange") or {}
        legal_min = int(br.get("min") or capped)
        legal_max = int(br.get("max") or capped)
        if capped < legal_min:
            if allowed.get("canCheck") and "check" in available:
                return _build("check", None, table, allowed, eq=eq, po=po, msg=msg + "→check")
            if "call" in available:
                return _build("call", None, table, allowed, eq=eq, po=po, msg=msg + "→call")
            return _build("fold", None, table, allowed, eq=eq, po=po, msg=msg + "→fold")
        return _build(action, min(capped, legal_max), table, allowed, eq=eq, po=po, msg=msg)
    if action == "raise":
        rr = allowed.get("raiseRange") or {}
        legal_min = int(rr.get("min") or capped)
        legal_max = int(rr.get("max") or capped)
        if capped < legal_min:
            if "call" in available:
                return _build("call", None, table, allowed, eq=eq, po=po, msg=msg + "→call")
            if allowed.get("canCheck") and "check" in available:
                return _build("check", None, table, allowed, eq=eq, po=po, msg=msg + "→check")
            return _build("fold", None, table, allowed, eq=eq, po=po, msg=msg + "→fold")
        return _build(action, min(capped, legal_max), table, allowed, eq=eq, po=po, msg=msg)
    if action == "all-in":
        all_in_to = int(allowed.get("allInToAmount") or allowed.get("maxCommit") or 0)
        if all_in_to > 0 and capped < all_in_to:
            if "call" in available:
                return _build("call", None, table, allowed, eq=eq, po=po, msg=msg + "→call")
            if allowed.get("canCheck") and "check" in available:
                return _build("check", None, table, allowed, eq=eq, po=po, msg=msg + "→check")
            return _build("fold", None, table, allowed, eq=eq, po=po, msg=msg + "→fold")
        target = all_in_to if all_in_to > 0 else capped
        return _build(action, min(capped, target), table, allowed, eq=eq, po=po, msg=msg)
    return _build(action, capped, table, allowed, eq=eq, po=po, msg=msg)


def _apply_chip_reserve(
    out: dict,
    max_playable: int | None,
    table: dict,
    hand_class: str,
) -> dict:
    """Cap bet/raise/all-in to playable bankroll above chip reserve."""
    if max_playable is None:
        return out
    action = out.get("action")
    amount = out.get("amount")
    if action not in ("bet", "raise", "all-in") or amount is None:
        return out
    allowed = table.get("allowedActions") or {}
    available = allowed.get("availableActions") or []
    cap = min(_hero_stack_chips(table), int(max_playable))
    if cap <= 0:
        return out
    if int(amount) <= cap:
        return out
    eq = 0.99 if "unbeatable" in (out.get("message") or "").lower() else 0.5
    po = 0.0
    capped = _clamp_sized_action_to_cap(
        action, int(amount), cap, table, allowed, available, eq=eq, po=po,
        msg=(out.get("message") or "")[:400] + " [reserve cap]",
    )
    if hand_class in {"AA", "KK", "QQ"} and capped.get("action") == action:
        return capped
    return capped


def _is_strong_continue(hc: str) -> bool:
    return hc in {
        "AA", "KK", "QQ", "JJ", "TT", "99", "88",
        "AKs", "AKo", "AQs", "AQo", "AJs", "KQs",
    }


def _overcommit_should_fold(
    table: dict,
    hand_class: str,
    equity: float,
    call_chips: int,
    *,
    lead_protect: bool = False,
    max_playable: int | None = None,
) -> bool:
    """Cap stack commitment with marginal hands (74o MP -916 style disasters)."""
    stack = _effective_stack_chips(table, max_playable)
    if stack <= 0 or call_chips <= 0:
        return False
    if _is_strong_continue(hand_class):
        return False
    ratio = call_chips / stack
    min_ratio = 0.12 if lead_protect else 0.18
    if ratio < min_ratio:
        return False
    if lead_protect and ratio >= 0.12 and equity < 0.52:
        return True
    if ratio >= 0.35 and equity < 0.55:
        return True
    if ratio >= 0.22 and equity < 0.45:
        return True
    if ratio >= 0.22 and _hero_underpair_on_paired_board(hand_class, list(table.get("boardCards") or [])):
        return True
    board = list(table.get("boardCards") or [])
    if (ratio >= 0.15 and _board_is_paired(board)
            and _marginal_offsuit_top_pair(hand_class) and equity < 0.62):
        return True
    if ratio >= 0.18 and (
        hand_class in _WEAK_FACING_RAISE or _is_low_trash_offsuit(hand_class)
    ) and equity < 0.40:
        return True
    return False


def _board_is_paired(board: list[str]) -> bool:
    if len(board) < 3:
        return False
    branks = [c[0].upper() for c in board]
    return max(Counter(branks).values()) >= 2


def _board_has_ace(board: list[str]) -> bool:
    return any(c and c[0].upper() == "A" for c in board)


def _board_has_ace_pair(board: list[str]) -> bool:
    if len(board) < 3:
        return False
    branks = [c[0].upper() for c in board]
    return Counter(branks).get("A", 0) >= 2


def _board_low_straight_heavy(board: list[str]) -> bool:
    """86532-style runout — straights likely (KK −1132 HL R15 export)."""
    if len(board) < 5:
        return False
    idxs = sorted({_RANKS.index(c[0].upper()) for c in board})
    if max(idxs) > _RANKS.index("T"):
        return False
    return len(idxs) >= 4 and (idxs[-1] - idxs[0]) <= 6


def _pocket_vulnerable_on_low_straight_board(
    hole: list[str], board: list[str], hc: str,
) -> bool:
    """TT+ overpair on low connected board without set — loses to straights."""
    if len(hole) != 2 or len(board) < 5 or hc == "AA":
        return False
    if hole[0][0] != hole[1][0]:
        return False
    if _RANKS.index(hc[0]) < _RANKS.index("T"):
        return False
    if not _board_low_straight_heavy(board):
        return False
    if _hero_made_hand_exempt(hole, board) or _hero_pocket_set(hole, board):
        return False
    return True


_OOP_SUITED_BROADWAY_PAIRED = frozenset({"KQs", "KJs", "QJs", "JTs"})


def _oop_suited_broadway_vulnerable_paired(
    hole: list[str], board: list[str], hc: str,
) -> bool:
    """KQs BB −51 on paired 99443 — no boat/trips."""
    if len(board) < 4 or not _board_is_paired(board):
        return False
    if hc not in _OOP_SUITED_BROADWAY_PAIRED:
        return False
    if _hero_made_hand_exempt(hole, board):
        return False
    return True


def _board_broadway_count(board: list[str]) -> int:
    """T+ ranks on board — 63s SB river leak on QJ2TK (HL R4 #01)."""
    if not board:
        return 0
    t_idx = _RANKS.index("T")
    return sum(1 for c in board if _RANKS.index(c[0].upper()) >= t_idx)


def _hero_underpair_on_paired_board(hand_class: str, board: list[str]) -> bool:
    """Pocket pair below the top board rank on a paired runout (JJ on Kxx22).

    Excludes set/boat spots where hero's pocket rank appears on board."""
    if len(hand_class) != 2 or hand_class[0] != hand_class[1]:
        return False
    if not _board_is_paired(board) or len(board) < 3:
        return False
    branks = [c[0].upper() for c in board]
    bc = Counter(branks)
    pr = hand_class[0]
    if bc.get(pr, 0) >= 1:
        return False
    top = max(branks, key=lambda r: _RANKS.index(r))
    return _RANKS.index(top) > _RANKS.index(pr)


def _hero_pocket_set(hole: list[str], board: list[str]) -> bool:
    """Pocket pair flopped a set (or better) on this board."""
    if len(hole) != 2 or len(board) < 3:
        return False
    hranks = [c[0].upper() for c in hole]
    if hranks[0] != hranks[1]:
        return False
    branks = [c[0].upper() for c in board]
    return hranks[0] in branks


def _hero_boat_or_quads_on_paired_board(hole: list[str], board: list[str]) -> bool:
    """Trash-class hands that improved to boat+ on a paired board (not bottom pair)."""
    if len(hole) != 2 or not _board_is_paired(board):
        return False
    hranks = [c[0].upper() for c in hole]
    bc = Counter(c[0].upper() for c in board)
    if hranks[0] == hranks[1]:
        return bc.get(hranks[0], 0) >= 1
    for r in hranks:
        if bc.get(r, 0) >= 3:
            return True
        if bc.get(r, 0) >= 2:
            other = hranks[1] if r == hranks[0] else hranks[0]
            if bc.get(other, 0) >= 1:
                return True
    return False


def _pocket_under_board_pair(hole: list[str], board: list[str]) -> bool:
    """Pocket pair strictly below the board pair rank — not trips (TT on JhJs, not 99 on TT9)."""
    if len(hole) != 2 or len(board) < 3:
        return False
    hranks = [c[0].upper() for c in hole]
    if hranks[0] != hranks[1]:
        return False
    if not _board_is_paired(board):
        return False
    branks = [c[0].upper() for c in board]
    bc = Counter(branks)
    pair_rank = max((r for r, c in bc.items() if c >= 2), key=lambda r: _RANKS.index(r))
    pr = hranks[0]
    if _RANKS.index(pr) >= _RANKS.index(pair_rank):
        return False
    if bc.get(pr, 0) == 1:
        return False
    return True


def _hero_pairs_flop(hole: list[str], board: list[str]) -> bool:
    if len(hole) != 2 or len(board) < 3:
        return False
    hr = {_RANKS.index(c[0].upper()) for c in hole}
    br = {_RANKS.index(c[0].upper()) for c in board[:3]}
    return bool(hr & br)


def _bb_oop_missed_k_high(hole: list[str], board: list[str], hand_class: str) -> bool:
    """BB defended trash that whiffs K-high flops — J8s on K65 (HL R7 #01)."""
    if len(board) < 3:
        return False
    br = [_RANKS.index(c[0].upper()) for c in board]
    if max(br) < _RANKS.index("K"):
        return False
    if _hero_pairs_flop(hole, board):
        return False
    if _is_strong_continue(hand_class):
        return False
    if hand_class in {
        "J8s", "J8o", "T8s", "T8o", "T9s", "98s", "87s", "76s",
        "K8o", "K7o", "Q8o", "J9o",
    }:
        return True
    if len(hand_class) == 3 and hand_class[2] == "s":
        hi, lo = _RANKS.index(hand_class[0]), _RANKS.index(hand_class[1])
        return hi <= _RANKS.index("J") and lo <= _RANKS.index("8")
    return False


def _oop_vulnerable_ace_tptk(hole: list[str], board: list[str], hc: str) -> bool:
    """AK/AQ TPTK on A-high flop with broadway scare card (BB AJ4 — HL R10 #01)."""
    if hc not in {"AKs", "AKo", "AQs", "AQo"}:
        return False
    if len(board) < 3 or len(hole) != 2:
        return False
    branks = [c[0].upper() for c in board]
    hranks = [c[0].upper() for c in hole]
    if "A" not in branks or "A" not in hranks:
        return False
    kicker = hranks[1] if hranks[0] == "A" else hranks[0]
    if kicker in branks:
        return False
    scare = frozenset({"K", "Q", "J", "T"})
    return any(r in scare and r != kicker for r in branks)


def _weak_kicker_top_pair(hole: list[str], board: list[str]) -> bool:
    """Top pair with kicker 7 or lower (T5o on T-high — MC overestimates)."""
    if len(hole) != 2 or len(board) < 3:
        return False
    if _hero_boat_or_quads_on_paired_board(hole, board):
        return False
    hranks = [c[0].upper() for c in hole]
    if hranks[0] == hranks[1]:
        return False
    branks = [c[0].upper() for c in board]
    paired_rank = next((r for r in hranks if r in branks), None)
    if not paired_rank:
        return False
    kicker = hranks[1] if hranks[0] == paired_rank else hranks[0]
    return _RANKS.index(kicker) <= _RANKS.index("7")


def _weak_top_pair_offsuit(hc: str) -> bool:
    """Top-pair-weak-kicker hands that bleed OOP (KQ MP, A8 SB −100 leaks)."""
    if _weak_ace_offsuit(hc):
        return True
    return hc in {"KQo", "KJo", "QJo", "KTo", "QTo", "JTo", "AJo", "ATo"}


def _small_pocket_pair(hc: str) -> bool:
    if len(hc) != 2 or hc[0] != hc[1]:
        return False
    return _RANKS.index(hc[0]) <= _RANKS.index("9")


def _medium_pocket_pair(hc: str) -> bool:
    """TT–QQ — fold OOP on connected runouts vs big bets (QQ SB −1000)."""
    if len(hc) != 2 or hc[0] != hc[1]:
        return False
    r = _RANKS.index(hc[0])
    return _RANKS.index("T") <= r <= _RANKS.index("Q")


def _board_has_three_consecutive_ranks(board: list[str]) -> bool:
    """Three or more consecutive unique ranks on board (876-type runouts)."""
    if len(board) < 3:
        return False
    idxs = sorted(set(_RANKS.index(c[0].upper()) for c in board))
    if len(idxs) < 3:
        return False
    run = best = 1
    for i in range(1, len(idxs)):
        if idxs[i] == idxs[i - 1] + 1:
            run += 1
            best = max(best, run)
        elif idxs[i] != idxs[i - 1]:
            run = 1
    return best >= 3


def _board_has_three_flush(board: list[str]) -> bool:
    if len(board) < 3:
        return False
    suits = [c[-1].lower() for c in board]
    return max(Counter(suits).values()) >= 3


def _board_overcard_to_pocket(hc: str, board: list[str]) -> bool:
    if not _small_pocket_pair(hc) or len(board) < 3:
        return False
    pr = _RANKS.index(hc[0])
    branks = [c[0].upper() for c in board]
    return max(_RANKS.index(r) for r in branks) > pr


def _weak_broadway_offsuit(hc: str) -> bool:
    return hc in {
        "AJo", "ATo", "A9o", "KJo", "KTo", "K9o", "QJo", "QTo", "Q9o",
        "JTo", "J9o",
    }


def _hero_has_flush(hole: list[str], board: list[str]) -> bool:
    if len(hole) != 2 or len(board) < 3:
        return False
    for suit in {c[-1].lower() for c in hole}:
        if sum(1 for c in hole + board if c[-1].lower() == suit) >= 5:
            return True
    return False


def _nuts_detect_enabled() -> bool:
    raw = os.environ.get("CEMINI_NUTS_DETECT", "0").strip().lower()
    return raw in ("1", "true", "yes", "on")


def _hero_made_royal_flush(hole: list[str], board: list[str]) -> bool:
    """Hero participates in a made A-high straight flush."""
    if len(hole) != 2 or len(board) < 5:
        return False
    hole_suits = {c[-1].lower() for c in hole}
    for suit in hole_suits:
        idx = sorted(
            (_RANKS.index(c[0].upper()) for c in hole + board if c[-1].lower() == suit),
            reverse=True,
        )
        if len(idx) >= 5 and idx[:5] == list(_ROYAL_IDX):
            return True
    return False


def _royal_made_action(
    table: dict,
    allowed: dict,
    available: list[str],
    pot: int,
    *,
    binding: str,
    call_chips: int = 0,
) -> Optional[dict]:
    if royal_showdown_mode():
        out = royal_showdown_action(
            table,
            allowed,
            available,
            pot,
            build_fn=_build,
            binding=binding,
            call_chips=call_chips,
        )
        if out:
            return out
    return _unbeatable_made_action(
        table, allowed, available, pot, binding=binding, label="royal flush",
    )


def _unbeatable_made_action(
    table: dict,
    allowed: dict,
    available: list[str],
    pot: int,
    *,
    binding: str,
    label: str = "river unbeatable",
) -> Optional[dict]:
    if allowed.get("canBet") and "bet" in available:
        br = allowed.get("betRange") or {}
        max_bet = int(br.get("max") or pot * 2)
        target = max(int(br.get("min") or pot), min(int(pot * 0.85), max_bet))
        return _build("bet", target, table, allowed, eq=0.99, po=0.0,
                      msg=f"{binding}: {label} — value bet")
    if allowed.get("canRaise") and "raise" in available:
        rr = allowed.get("raiseRange") or {}
        max_r = int(rr.get("max") or pot * 2)
        min_r = int(rr.get("min") or pot)
        target = max(min_r, min(max_r, int(pot * 0.9)))
        return _build("raise", target, table, allowed, eq=0.99, po=0.0,
                      msg=f"{binding}: {label} — raise")
    if allowed.get("canCheck") and "check" in available:
        return _build("check", None, table, allowed, eq=0.99, po=0.0,
                      msg=f"{binding}: {label} — check trap")
    if "call" in available:
        return _build("call", None, table, allowed, eq=0.99, po=0.0,
                      msg=f"{binding}: {label} — call")
    if allowed.get("canAllIn") and "all-in" in available:
        all_in_to = int(
            allowed.get("allInToAmount") or allowed.get("maxCommit") or 0
        )
        if all_in_to > 0:
            return _build("all-in", all_in_to, table, allowed, eq=0.99, po=0.0,
                          msg=f"{binding}: {label} — all-in")
    return None


def _hero_second_pair_or_worse(hole: list[str], board: list[str]) -> bool:
    """Hero pairs below the top board rank (QTo on K-high — analyze #01)."""
    if len(hole) != 2 or len(board) < 3:
        return False
    hranks = [c[0].upper() for c in hole]
    branks = [c[0].upper() for c in board]
    if hranks[0] == hranks[1]:
        top_board = max(branks, key=lambda r: _RANKS.index(r))
        return _RANKS.index(hranks[0]) < _RANKS.index(top_board)
    paired = [r for r in hranks if r in branks]
    if not paired:
        return True
    best = max(paired, key=lambda r: _RANKS.index(r))
    top_board = max(branks, key=lambda r: _RANKS.index(r))
    return _RANKS.index(best) < _RANKS.index(top_board)


def _hero_ace_high_on_paired_board(hole: list[str], board: list[str]) -> bool:
    """Ace-high only on paired runouts (AJo on 55x — S28 -46 leak)."""
    if not _board_is_paired(board) or len(hole) != 2:
        return False
    hranks = [c[0].upper() for c in hole]
    if hranks[0] == hranks[1]:
        return False
    if "A" not in hranks:
        return False
    branks = [c[0].upper() for c in board]
    return not any(r in branks for r in hranks)


def _hero_vulnerable_on_paired_board(hole: list[str], board: list[str]) -> bool:
    """Underpair / single non-boat pair on paired boards (fold vs big bets)."""
    if not _board_is_paired(board) or len(hole) != 2:
        return False
    branks = [c[0].upper() for c in board]
    bc = Counter(branks)
    pair_rank = next(r for r, c in bc.items() if c >= 2)
    hranks = [c[0].upper() for c in hole]
    if hranks[0] == hranks[1]:
        return _RANKS.index(hranks[0]) < _RANKS.index(pair_rank)
    if any(r in branks and branks.count(r) >= 2 for r in hranks):
        return False
    return any(r in branks and branks.count(r) == 1 for r in hranks)


def _hero_overcards_only(hole: list[str], board: list[str]) -> bool:
    """Paired board, hero missed — only unpaired overcards (Kh4c on TTT)."""
    if not _board_paired_hero_missed(hole, board) or len(hole) != 2:
        return False
    hranks = [c[0].upper() for c in hole]
    if hranks[0] == hranks[1]:
        return False
    branks = [c[0].upper() for c in board]
    return not any(r in branks for r in hranks)


def _postflop_mix_allowed(
    hand_class: str,
    hole: list[str],
    board: list[str],
    position: str,
    in_position: bool,
) -> bool:
    """No random mixing on Playground leak classes — MC variance must not open calls."""
    if hand_class in _WEAK_FACING_RAISE or _is_garbage_offsuit(hand_class):
        return False
    if _weak_ace_offsuit(hand_class) and _board_is_paired(board):
        return False
    if position in ("CO", "BTN") and in_position and _is_paired_runout_trash(hand_class):
        if _board_is_paired(board):
            return False
    if _weak_top_pair_offsuit(hand_class) or _marginal_offsuit_top_pair(hand_class):
        return False
    if _small_pocket_pair(hand_class) and _board_overcard_to_pocket(hand_class, board):
        return False
    if _hero_underpair_on_paired_board(hand_class, board):
        return False
    if _board_is_paired(board) and _weak_broadway_offsuit(hand_class):
        return False
    if position in ("UTG", "MP", "CO") and not _is_strong_continue(hand_class):
        return False
    if _board_paired_hero_missed(hole, board) or _hero_overcards_only(hole, board):
        return False
    if in_position and _board_is_paired(board):
        if (_hero_ace_high_on_paired_board(hole, board)
                or _hero_vulnerable_on_paired_board(hole, board)
                or _weak_broadway_offsuit(hand_class)):
            return False
    return True


def _postflop_free(equity: float, allowed: dict, available: list,
                   pot: int, *, pot_control: bool = False,
                   ps_bias: Optional[str] = None,
                   ps_library: bool = False,
                   hand_eval: Optional[str] = None,
                   hand_class: str = "",
                   hud_mode: str = "unknown",
                   margins: Optional[dict] = None) -> tuple[str, Optional[int]]:
    margins = margins or exploit_margins(hud_mode)
    # PokerSkill: nut-high + draw → pot control, don't lead.
    if hand_eval == "nut_high_draw" and "check" in available:
        return "check", None
    if ps_library and ps_bias == "check" and "check" in available:
        return "check", None
    bet_bar = 0.78 if pot_control else 0.72
    bet_bar += float(margins.get("bet_bar_delta", 0))
    if ps_bias == "probe_small" and allowed.get("canBet") and "bet" in available:
        bet_bar = 0.58 + float(margins.get("bet_bar_delta", 0))
    if ps_library and ps_bias == "raise" and equity > 0.62:
        bet_bar = 0.55 + float(margins.get("bet_bar_delta", 0))
    if equity > bet_bar and allowed.get("canBet") and "bet" in available:
        br = allowed.get("betRange") or {}
        min_bet = int(br.get("min") or max(int(pot * 0.33), 1))
        max_bet = int(br.get("max") or min_bet)
        target = max(min_bet, min(int(pot * 0.66), max_bet))
        return "bet", target
    if "check" in available:
        return "check", None
    return ("call" if "call" in available else "fold"), None


def _postflop_facing_bet(equity: float, pot_odds: float, allowed: dict,
                         available: list, call_chips: int,
                         pot: int, *, in_position: bool,
                         pot_control: bool = False,
                         hand_class: str = "",
                         hole: Optional[list[str]] = None,
                         board: Optional[list[str]] = None,
                         ps_bias: Optional[str] = None,
                         ps_library: bool = False,
                         hand_eval: Optional[str] = None,
                         hud_mode: str = "unknown",
                         margins: Optional[dict] = None,
                         table: Optional[dict] = None,
                         position: str = "",
                         lead_protect: bool = False,
                         max_playable: int | None = None) -> tuple[str, Optional[int]]:
    margins = margins or exploit_margins(hud_mode)
    hole = hole or []
    board = board or []

    if table and _overcommit_should_fold(
            table, hand_class, equity, call_chips, lead_protect=lead_protect,
            max_playable=max_playable):
        return "fold", None

    # BB OOP air on K-high flops — J8s on K65 (HL R7 analyze #01).
    if (position == "BB" and not in_position
            and _bb_oop_missed_k_high(hole, board, hand_class)
            and call_chips >= max(int(pot * 0.25), 1)
            and "fold" in available):
        return "fold", None

    # Lead protect: fold IP weak broadway vs medium+ bets (preserve chip stack).
    if (lead_protect and in_position and len(board) >= 3
            and _weak_broadway_offsuit(hand_class)
            and call_chips >= max(int(pot * 0.33), 1)
            and "fold" in available):
        return "fold", None

    # CO/EP OOP weak top pair on later streets (T5o CO −100 analyze #12).
    if (position in ("CO", "MP", "UTG")
            and len(board) >= 4
            and _weak_kicker_top_pair(hole, board)
            and call_chips >= max(int(pot * 0.33), 1)
            and "fold" in available):
        return "fold", None

    # SB/BB OOP weak kicker top pair on three-flush — K2o SB −100 (HL R24 #01).
    if (position in ("SB", "BB") and not in_position
            and _board_has_three_flush(board)
            and not _hero_has_flush(hole, board)
            and _weak_kicker_top_pair(hole, board)
            and call_chips >= max(int(pot * 0.22), 1)
            and "fold" in available):
        return "fold", None

    # EP OOP: fold weak hands vs significant bets without strong equity.
    if (position in ("UTG", "MP") and not in_position and call_chips > 0
            and not _is_strong_continue(hand_class)
            and equity < 0.50 and call_chips >= max(int(pot * 0.35), 1)
            and "fold" in available):
        return "fold", None

    # OOP weak top-pair offsuit vs pot-sized bets (KQo MP −100).
    if (not in_position and _weak_top_pair_offsuit(hand_class)
            and not _hero_made_hand_exempt(hole, board)
            and call_chips >= max(int(pot * 0.40), 1)
            and "fold" in available):
        return "fold", None

    # SB OOP medium pair under top board card on paired runouts (JJ SB −101).
    if (position == "SB" and not in_position
            and _hero_underpair_on_paired_board(hand_class, board)
            and call_chips >= max(int(pot * 0.32), 1)
            and "fold" in available):
        return "fold", None

    if (position == "SB" and not in_position
            and _is_wheel_offsuit(hand_class)
            and call_chips >= max(int(pot * 0.18), 1)
            and "fold" in available):
        return "fold", None

    if (not in_position
            and _is_wheel_offsuit(hand_class)
            and call_chips >= max(int(pot * 0.18), 1)
            and "fold" in available):
        return "fold", None

    if (position == "SB" and not in_position
            and len(board) == 3
            and hand_class in _SB_WEAK_SUITED_VS_OPEN
            and call_chips >= max(int(pot * 0.22), 1)
            and "fold" in available):
        return "fold", None

    if (position == "SB" and not in_position
            and _is_sb_suited_trash(hand_class)
            and call_chips >= max(int(pot * 0.20), 1)
            and "fold" in available):
        return "fold", None

    if (position == "SB" and not in_position
            and (_medium_pocket_pair(hand_class) or _small_pocket_pair(hand_class))
            and _board_has_ace_pair(board)
            and not _hero_pocket_set(hole, board)
            and call_chips >= max(int(pot * 0.22), 1)
            and "fold" in available):
        return "fold", None

    if (position in ("UTG", "MP", "CO")
            and _hero_vulnerable_pocket_on_ace_paired_board(hole, board, hand_class)
            and call_chips >= max(int(pot * 0.22), 1)
            and "fold" in available):
        return "fold", None

    if (position in ("UTG", "MP", "CO")
            and _hero_ace_broadway_vulnerable_on_paired_board(hole, board, hand_class)
            and call_chips >= max(int(pot * 0.22), 1)
            and "fold" in available):
        return "fold", None

    if (position in ("UTG", "MP", "CO", "SB", "BB")
            and _hero_small_pocket_under_board_ace(hole, board, hand_class)
            and call_chips >= max(int(pot * 0.22), 1)
            and "fold" in available):
        return "fold", None

    if (_pocket_vulnerable_on_low_straight_board(hole, board, hand_class)
            and call_chips >= max(int(pot * 0.22), 1)
            and "fold" in available):
        return "fold", None

    if (position in ("SB", "BB") and not in_position
            and _oop_suited_broadway_vulnerable_paired(hole, board, hand_class)
            and call_chips >= max(int(pot * 0.18), 1)
            and "fold" in available):
        return "fold", None

    # SB OOP TT–QQ on connected runout vs big bet — QQ SB −1000 (HL R12 #01).
    if (position == "SB" and not in_position
            and _medium_pocket_pair(hand_class)
            and not _hero_pocket_set(hole, board)
            and len(board) >= 4
            and _board_has_three_consecutive_ranks(board)
            and call_chips >= max(int(pot * 0.38), 1)
            and "fold" in available):
        return "fold", None

    # SB OOP small pair vs overcard board — 22/88 −100 lines (analyze #09, #14).
    if (position == "SB" and not in_position
            and _small_pocket_pair(hand_class)
            and _board_overcard_to_pocket(hand_class, board)
            and call_chips >= max(int(pot * 0.32), 1)
            and equity < 0.52 and "fold" in available):
        return "fold", None

    # SB OOP weak ace top-pair — A8 on J86 monotone (analyze #03).
    if (position == "SB" and not in_position
            and _weak_ace_offsuit(hand_class)
            and not _hero_made_hand_exempt(hole, board)
            and len(board) >= 3
            and call_chips >= max(int(pot * 0.30), 1)
            and "fold" in available):
        wet = _board_has_three_flush(board)
        eq_cap = 0.68 if wet else 0.62
        if equity < eq_cap:
            return "fold", None

    # BB OOP AK/AQ on A-high broadway flops — Kh As BB −116 on AJ4 (HL R10 #01).
    if (position == "BB" and not in_position
            and _oop_vulnerable_ace_tptk(hole, board, hand_class)
            and call_chips >= max(int(pot * 0.32), 1)
            and "fold" in available):
        return "fold", None

    # OOP weak ace on paired boards — A6 BB, A7 CO; skip A9 on AAx (HL R18 #05).
    if (not in_position and _weak_ace_vulnerable_on_paired_board(hole, board, hand_class)
            and call_chips >= max(int(pot * 0.32), 1)
            and "fold" in available):
        return "fold", None

    # EP OOP marginal top pair on paired boards — T6o MP −290 (analyze #01).
    if (position in ("UTG", "MP") and not in_position
            and _board_is_paired(board)
            and _marginal_offsuit_top_pair(hand_class)
            and call_chips >= max(int(pot * 0.28), 1)
            and "fold" in available):
        return "fold", None

    # EP/MP/CO ace-x second pair — A9o MP −100 (HL R9 #14).
    if (position in ("UTG", "MP", "CO")
            and len(board) >= 4
            and _marginal_ace_kicker(hand_class)
            and _ace_kicker_second_pair(hole, board)
            and call_chips >= max(int(pot * 0.28), 1)
            and "fold" in available):
        return "fold", None

    if ps_library and ps_bias == "fold" and "fold" in available:
        if (_should_fold_weak_preflop(hand_class, equity, pot_odds)
                or equity < pot_odds + 0.04):
            return "fold", None

    # J2o-type trash: fold vs bets on paired boards (662A2 / KAT22 / 63s 75553 runouts).
    if (_is_paired_runout_trash_hand(hand_class) and _board_is_paired(board)
            and not _hero_made_hand_exempt(hole, board)
            and call_chips > 0 and "fold" in available):
        return "fold", None

    # PokerSkill nut-high + draw: check-call line, avoid spewy raises.
    if hand_eval == "nut_high_draw":
        raise_bar = 0.88
        call_margin = -0.02 if in_position else 0.01
        if equity > raise_bar and allowed.get("canRaise") and "raise" in available:
            rr = allowed.get("raiseRange") or {}
            min_r = int(rr.get("min") or call_chips * 2)
            max_r = int(rr.get("max") or min_r)
            target = max(min_r, min(int(pot * 0.65 + call_chips * 2), max_r))
            return "raise", target
        if equity >= pot_odds + call_margin and "call" in available:
            return "call", None
        if equity < pot_odds - 0.03 and "fold" in available:
            return "fold", None
        if "check" in available:
            return "check", None

    # Live leak: air on paired boards (Kh4c on TTT-type runouts).
    if (_hero_overcards_only(hole, board) and not in_position
            and equity < 0.48 and "fold" in available):
        return "fold", None
    if (_board_paired_hero_missed(hole, board) and not in_position
            and equity < 0.44 and "fold" in available):
        return "fold", None
    if (_board_paired_hero_missed(hole, board) and pot_control
            and equity < 0.50 and "fold" in available):
        return "fold", None

    # S28 leak: AJo IP on paired boards — don't pay large bets with ace-high / weak pair.
    big_bet = call_chips >= max(int(pot * 0.42), 1)
    if (in_position and len(board) >= 3 and big_bet and "fold" in available):
        paired_ip = _train_threshold("paired_ip_fold_eq", 0.42)
        paired_vuln = _train_threshold("paired_vuln_fold_eq", 0.44)
        # QTo BTN on three-flush — MC equity overstates vs value (analyze #01).
        if (_board_has_three_flush(board)
                and not _hero_has_flush(hole, board)
                and (_weak_broadway_offsuit(hand_class)
                     or _hero_second_pair_or_worse(hole, board))):
            return "fold", None
        if (_hero_ace_high_on_paired_board(hole, board) and equity < paired_ip):
            return "fold", None
        if ((_hero_vulnerable_on_paired_board(hole, board)
             or _weak_broadway_offsuit(hand_class))
                and equity < paired_vuln):
            return "fold", None

    # Live leak: weak ace-high folds cheaply on later streets (Ad3c-type spots).
    if _weak_ace_offsuit(hand_class) and equity < 0.38 and "fold" in available:
        return "fold", None
    if _weak_ace_offsuit(hand_class) and not in_position and equity < 0.45:
        if equity < pot_odds and "fold" in available:
            return "fold", None
    fold_slack = 0.06 if in_position else 0.04
    call_margin = 0.04 if in_position else 0.07
    fold_slack += float(margins.get("fold_slack_delta", 0))
    call_margin += float(margins.get("call_margin_delta", 0))
    if pot_control:
        call_margin += 0.03
        fold_slack -= 0.01
    # vs rock OOP: respect aggression — don't over-fold IP medium hands.
    rock_oop_eq = _train_threshold("rock_oop_fold_eq", 0.40)
    if hud_mode == "rock" and not in_position and equity < rock_oop_eq and "fold" in available:
        fold_slack += 0.02
    raise_bar = 0.82 if in_position else 0.86
    if equity > raise_bar and allowed.get("canRaise") and "raise" in available:
        rr = allowed.get("raiseRange") or {}
        min_r = int(rr.get("min") or call_chips * 2)
        max_r = int(rr.get("max") or min_r)
        target = max(min_r, min(int(pot * 0.75 + call_chips * 2), max_r))
        return "raise", target
    table_ctx = table if table is not None else {}
    allow_mix = _postflop_mix_allowed(hand_class, hole, board, position, in_position)
    return resolve_postflop_call_fold(
        table_ctx, equity, pot_odds, fold_slack, call_margin, available,
        allow_mix=allow_mix,
    )


def _message(action: str, equity: float, pot_odds: float,
             binding: str, suggested: Optional[str],
             hud_mode: str = "unknown",
             survival: bool = False,
             deadline_s: float = 10.0,
             villain_mem: Optional[dict] = None,
             candor_fold: bool = False) -> str:
    eq = int(round(equity * 100))
    po = int(round(pot_odds * 100))
    hud = f" vs {hud_mode}" if hud_mode not in ("unknown", "") else ""
    mem_note = ""
    villains = (villain_mem or {}).get("villains") or {}
    if deadline_s > 8 and villains:
        labels = {v.get("label") for v in villains.values() if v.get("confidence") != "low"}
        if labels:
            mem_note = f" [session: {','.join(sorted(labels))}]"
    if action == "fold":
        if candor_fold and equity < pot_odds - 0.08:
            base = f"{binding}{hud}: honest fold — {eq}% vs {po}% price{mem_note}"
        else:
            base = f"{binding}{hud}: equity {eq}% short of price, folding{mem_note}"
        return base + (" (survival)" if survival else "")
    if action == "check":
        return f"{binding}: free card, equity {eq}%{mem_note}"
    if action == "call":
        return f"{binding}: calling — equity covers pot odds{mem_note}"
    if suggested and action in ("bet", "raise"):
        return f"chart says {suggested}; executing {action} for value{mem_note}"
    return f"{binding}: {action} with {eq}% equity{mem_note}"


def _skill_reasoning(base: str, binding: str, suggested: Optional[str],
                     chart: dict, ps: Optional[dict] = None,
                     hud_mode: str = "unknown") -> str:
    """Append skill tag within 150-char YAML cap."""
    pos = chart.get("position") or "?"
    layer = (ps or {}).get("layer", "stub")
    hud = hud_mode if hud_mode not in ("unknown", "") else "-"
    tag = f'sk: "{binding}@{pos}|{layer}|{hud}"'
    if suggested:
        tag = f'sk: "{binding}|{suggested}@{pos}|{hud}"'
    if len(base) + len(tag) + 2 <= 150:
        return base[:-1] + f", {tag}}}" if base.endswith("}") else f"{{{tag}}}"
    return base[:150]
