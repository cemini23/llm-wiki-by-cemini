"""S2 7-2 offsuit bluff jackpot hunt (API: TwoSevenOffsuitBluff).

Official rule: win an uncontested pot by folding everyone out while holding
7-2 offsuit. S2 pool: 10× slots @ 4500 MON (see GET /texas/jackpots).

Integrated into qual bot via `maybe_hunt_action()` when JACKPOT_27_HUNT_ENABLED=1.
Standalone probe loop (`run_jackpot_27_lobby.py`) is deprecated — use main bot.

Run dry-run:
  uv run examples/agent.py --agent examples/jackpot_27_decide.py --dry-run --max-hands 20
"""
from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any, Optional

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from agent import _build, _hand_class  # noqa: E402
from position_utils import hero_is_in_position, hero_position_label  # noqa: E402
from opponent_hud import build_opponent_hud  # noqa: E402
from jackpot_27_state import (  # noqa: E402
    begin_hunt,
    hand_key,
    log_action,
    log_dealt,
    max_attempts,
)

_JACKPOT_HANDS = frozenset(
    h.strip()
    for h in os.environ.get("JACKPOT_27_HANDS", "72o").split(",")
    if h.strip()
)
_DEFAULT_POSITIONS = frozenset({"CO", "BTN", "SB"})
_MIN_STACK_BB = 15


def _aggressive_phase() -> bool:
    """Early S2: more hunt volume while rebuy runway exists (JACKPOT_27_PHASE=early)."""
    phase = os.environ.get("JACKPOT_27_PHASE", "").strip().lower()
    if phase in ("early", "jackpot", "hunt"):
        return True
    raw = os.environ.get("JACKPOT_27_AGGRESSIVE", "0").strip().lower()
    return raw in ("1", "true", "yes", "on")


def _hunt_positions() -> frozenset[str]:
    raw = os.environ.get("JACKPOT_27_POSITIONS", "").strip()
    if raw:
        return frozenset(p.strip() for p in raw.split(",") if p.strip())
    if _aggressive_phase():
        return frozenset({"CO", "BTN", "SB", "BB"})
    return _DEFAULT_POSITIONS


def _max_villains() -> int:
    if _aggressive_phase():
        return int(os.environ.get("JACKPOT_27_MAX_VILLAINS", "3"))
    return 2


def _min_stack_bb() -> float:
    if _aggressive_phase():
        return float(os.environ.get("JACKPOT_27_MIN_STACK_BB", "12"))
    return _MIN_STACK_BB


def _hunt_enabled() -> bool:
    return os.environ.get("JACKPOT_27_HUNT_ENABLED", "0").strip().lower() in ("1", "true", "yes")


def _competition_ok(table: dict) -> bool:
    """When JACKPOT_27_COMPETITION_ONLY=1, hunt only in target playground."""
    if os.environ.get("JACKPOT_27_COMPETITION_ONLY", "1").strip().lower() in ("0", "false", "no"):
        return True
    comp = str(table.get("competitionId") or "")
    target = (
        os.environ.get("JACKPOT_27_COMPETITION_ID")
        or os.environ.get("ARENA_LOBBY_COMPETITION_ID")
        or ""
    ).strip()
    if not target:
        return True
    return comp == target


def retrieve_solver_context(table: dict) -> dict:
    hud = build_opponent_hud(table) or {}
    return {
        "opponent_hud": hud,
        "position": hero_position_label(table),
    }


def _is_jackpot_hand(hc: str) -> bool:
    return hc in _JACKPOT_HANDS


def _hero_stack_bb(table: dict) -> float:
    bb = int(table.get("bigBlindChips") or 20)
    sn = table.get("selfSeatNumber")
    for seat in table.get("seats") or []:
        if seat.get("seatNumber") == sn:
            return int(seat.get("stackChips") or 0) / max(bb, 1)
    return 0.0


def _villains_in_pot(table: dict) -> int:
    """Non-hero seats with chips committed this hand."""
    hero = table.get("selfSeatNumber")
    n = 0
    for seat in table.get("seats") or []:
        if seat.get("seatNumber") == hero:
            continue
        if seat.get("status") not in (None, "Active"):
            continue
        committed = int(seat.get("totalCommittedChips") or 0)
        bet = int(seat.get("currentBetChips") or 0)
        if committed > 0 or bet > 0:
            n += 1
    return n


def _fold_equity_ok(hud: dict, position: str) -> bool:
    positions = _hunt_positions()
    mode = (hud.get("mode") or "unknown").lower()
    if mode in ("rock", "passive", "nit"):
        return True
    if _aggressive_phase():
        if mode in ("maniac", "lag"):
            return False
        if mode in ("tag", "unknown") and position in positions:
            return True
        if hud.get("coldStart") and position in positions:
            return True
        return position in ("BTN", "SB")
    if hud.get("coldStart") and position in positions:
        return True
    return False


def _hunt_allowed(
    table: dict,
    hole: list[str],
    hc: str,
    position: str,
    hud: dict,
) -> bool:
    if not _hunt_enabled():
        return False
    if not _is_jackpot_hand(hc):
        return False
    if position not in _hunt_positions():
        return False
    if _hero_stack_bb(table) < _min_stack_bb():
        return False
    if _villains_in_pot(table) > _max_villains():
        return False
    if not _fold_equity_ok(hud, position):
        return False
    return begin_hunt(hand_key(table, hole))


def _passive(
    table: dict,
    allowed: dict,
    available: list[str],
    *,
    binding: str,
    equity: float = 0.0,
    pot_odds: float = 0.0,
) -> dict:
    if allowed.get("canCheck") and "check" in available:
        return _build("check", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: passive — free check")
    if "fold" in available:
        return _build("fold", None, table, allowed, eq=equity, po=pot_odds,
                      msg=f"{binding}: passive — fold")
    return _build("call", None, table, allowed, eq=equity, po=pot_odds,
                  msg=f"{binding}: passive — call")


def _skill_reasoning(base: str, tag: str) -> str:
    jp = f'jp: "{tag}"'
    if len(base) + len(jp) + 2 <= 150:
        return base[:-1] + f", {jp}}}" if base.endswith("}") else f"{{{jp}}}"
    return base[:150]


def maybe_hunt_action(
    table: dict,
    allowed: dict,
    available: list[str],
    hole: list[str],
    board: list[str],
    street: str,
    pot: int,
    call_chips: int,
    *,
    research_context: dict,
    deadline_s: float = 10.0,
) -> Optional[dict]:
    """Return hunt action when gates pass; None → main `cemini_decide` path."""
    if not _hunt_enabled() or not _competition_ok(table):
        return None
    ctx = research_context
    hud = ctx.get("opponent_hud") or {}
    hc = _hand_class(hole) or ""
    position = ctx.get("position") or hero_position_label(table)
    pot_odds = call_chips / max(pot + call_chips, 1) if call_chips else 0.0

    if _is_jackpot_hand(hc):
        log_dealt(table, hole, hand_class=hc, position=position)

    if not _hunt_allowed(table, hole, hc, position, hud):
        return None

    tag = f"hunt|{hc}@{position}|{hud.get('mode') or 'cold'}"
    bb = int(table.get("bigBlindChips") or 20)
    if street == "Preflop":
        facing_aggression = call_chips > bb
    else:
        facing_aggression = call_chips > 0

    if facing_aggression:
        log_action(table, action="fold", phase="abort_vs_bet", notes=tag)
        out = _build("fold", None, table, allowed, eq=0.05, po=pot_odds,
                     msg=f"jp: abort vs bet — {hc}")
        out["reasoning"] = _skill_reasoning(out.get("reasoning", ""), tag)
        return out

    if street == "Preflop" and allowed.get("canBet") and "bet" in available:
        br = allowed.get("betRange") or {}
        min_bet = int(br.get("min") or max(int(pot * 0.5), 1))
        max_bet = int(br.get("max") or min_bet)
        target = max(min_bet, min(int(pot * 0.75), max_bet))
        log_action(table, action="bet", phase="preflop_open", notes=tag)
        out = _build("bet", target, table, allowed, eq=0.35, po=0.0,
                     msg=f"jp: preflop steal — {hc}@{position}")
        out["reasoning"] = _skill_reasoning(out.get("reasoning", ""), tag)
        return out

    if allowed.get("canBet") and "bet" in available:
        br = allowed.get("betRange") or {}
        min_bet = int(br.get("min") or max(int(pot * 0.33), 1))
        max_bet = int(br.get("max") or min_bet)
        frac = 0.45 if len(board) >= 4 else 0.38
        target = max(min_bet, min(int(pot * frac), max_bet))
        phase = "turn_barrel" if len(board) >= 4 else "flop_cbet"
        log_action(table, action="bet", phase=phase, notes=tag)
        out = _build("bet", target, table, allowed, eq=0.22, po=0.0,
                     msg=f"jp: {phase} — {hc}")
        out["reasoning"] = _skill_reasoning(out.get("reasoning", ""), tag)
        return out

    out = _passive(table, allowed, available, binding="jp_giveup")
    out["reasoning"] = _skill_reasoning(out.get("reasoning", ""), f"giveup|{hc}")
    return out


def decide(
    table: dict,
    deadline_s: float = 10.0,
    research_context: Optional[dict] = None,
) -> dict:
    allowed = table.get("allowedActions") or {}
    available = allowed.get("availableActions") or []
    ctx = research_context or retrieve_solver_context(table)
    hud = ctx.get("opponent_hud") or {}

    if deadline_s < 2.0:
        if allowed.get("canCheck"):
            return _build("check", None, table, allowed, eq=0.5, po=0.0,
                          msg="clock — check")
        return _build("fold", None, table, allowed, eq=0.0, po=1.0,
                      msg="clock — fold")

    self_seat_num = table.get("selfSeatNumber")
    seats = table.get("seats") or []
    self_seat = next((s for s in seats if s.get("seatNumber") == self_seat_num), {})
    hole = list(self_seat.get("holeCards") or [])
    board = list(table.get("boardCards") or [])
    street = table.get("street") or "Preflop"
    pot = int(table.get("potChips") or 0)
    call_chips = int(allowed.get("callChips") or 0)
    pot_odds = call_chips / max(pot + call_chips, 1) if call_chips else 0.0
    hc = _hand_class(hole) or ""
    position = ctx.get("position") or hero_position_label(table)
    in_position = hero_is_in_position(table)

    if _is_jackpot_hand(hc):
        log_dealt(table, hole, hand_class=hc, position=position)

    hunting = _hunt_allowed(table, hole, hc, position, hud)

    if not _is_jackpot_hand(hc) or not hunting:
        out = _passive(table, allowed, available, binding="jp_idle")
        return out

    tag = f"hunt|{hc}@{position}|{hud.get('mode') or 'cold'}"

    bb = int(table.get("bigBlindChips") or 20)
    if street == "Preflop":
        facing_aggression = call_chips > bb
    else:
        facing_aggression = call_chips > 0

    # Facing a raise or postflop bet — never call down on 27o hunt.
    if facing_aggression:
        log_action(table, action="fold", phase="abort_vs_bet", notes=tag)
        out = _build("fold", None, table, allowed, eq=0.05, po=pot_odds,
                     msg=f"jp: abort vs bet — {hc}")
        out["reasoning"] = _skill_reasoning(out.get("reasoning", ""), tag)
        return out

    # Preflop open / steal
    if street == "Preflop" and allowed.get("canBet") and "bet" in available:
        br = allowed.get("betRange") or {}
        min_bet = int(br.get("min") or max(int(pot * 0.5), 1))
        max_bet = int(br.get("max") or min_bet)
        target = max(min_bet, min(int(pot * 0.75), max_bet))
        log_action(table, action="bet", phase="preflop_open", notes=tag)
        out = _build("bet", target, table, allowed, eq=0.35, po=0.0,
                     msg=f"jp: preflop steal — {hc}@{position}")
        out["reasoning"] = _skill_reasoning(out.get("reasoning", ""), tag)
        return out

    # Postflop c-bet when checked to
    if allowed.get("canBet") and "bet" in available:
        br = allowed.get("betRange") or {}
        min_bet = int(br.get("min") or max(int(pot * 0.33), 1))
        max_bet = int(br.get("max") or min_bet)
        frac = 0.45 if len(board) >= 4 else 0.38
        target = max(min_bet, min(int(pot * frac), max_bet))
        phase = "turn_barrel" if len(board) >= 4 else "flop_cbet"
        log_action(table, action="bet", phase=phase, notes=tag)
        out = _build("bet", target, table, allowed, eq=0.22, po=0.0,
                     msg=f"jp: {phase} — {hc}")
        out["reasoning"] = _skill_reasoning(out.get("reasoning", ""), tag)
        return out

    out = _passive(table, allowed, available, binding="jp_giveup")
    out["reasoning"] = _skill_reasoning(out.get("reasoning", ""), f"giveup|{hc}")
    return out
