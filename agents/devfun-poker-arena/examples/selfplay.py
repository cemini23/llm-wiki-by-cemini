"""Local headless self-play — fast feedback for `decide()` development.

NO network calls. NO Arena API. Just an in-process poker game where your
`decide()` function (from examples/agent.py or any custom file) plays N
hands against simple local opponents and prints bb/100.

Why: `pokerkit run` against Arena is the real benchmark, but each
50-hand preview takes ~3-5 minutes. For tight iteration on `decide()`
you want a 30-second feedback loop. This is that loop.

Caveat: local opponents are SIMPLE heuristic bots (random / tight-passive
/ loose-passive / always-call), NOT the DeepCFR reference panel that
Arena uses. Use selfplay to catch bugs and validate gross direction
("does my new range table actually open more hands?"). Use
`pokerkit run --max-hands 50` to confirm gains hold against DeepCFR.

Usage:
    pokerkit selfplay                              # 200 hands HU vs tight-passive
    pokerkit selfplay --hands 1000 --opponent random
    pokerkit selfplay --agent examples/agent.py    # explicit decide() source
    pokerkit selfplay --players 6                  # 6-max vs mixed bots
    pokerkit selfplay --seed 42                    # reproducible
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import random
import sys
import time
from pathlib import Path
from typing import Any, Callable, Optional

from pokerkit import (  # type: ignore
    Automation,
    BettingStructure,
    Deck,
    NoLimitTexasHoldem,
    Opening,
    State,
    Street,
)


# ─── Opponent bots (local decide-style functions) ───────────────────────────

def bot_always_check_call(table: dict, **_: Any) -> dict:
    """Free → check, else call. Never folds, never raises."""
    allowed = table.get("allowedActions") or {}
    avail = allowed.get("availableActions") or []
    if "check" in avail:
        return {"action": "check"}
    if "call" in avail:
        return {"action": "call"}
    return {"action": "fold"}


def bot_random(table: dict, **_: Any) -> dict:
    """Uniform random over legal actions; bet sizing 50% pot."""
    allowed = table.get("allowedActions") or {}
    avail = list(allowed.get("availableActions") or [])
    if not avail:
        return {"action": "fold"}
    pick = random.choice(avail)
    if pick == "bet":
        br = allowed.get("betRange") or {}
        lo, hi = int(br.get("min") or 1), int(br.get("max") or 1)
        pot = int(table.get("potChips") or 0)
        return {"action": "bet",
                "amount": max(lo, min(int(pot * 0.5), hi))}
    if pick == "raise":
        rr = allowed.get("raiseRange") or {}
        lo, hi = int(rr.get("min") or 1), int(rr.get("max") or 1)
        return {"action": "raise", "amount": max(lo, min(lo * 2, hi))}
    return {"action": pick}


def bot_tight_passive(table: dict, **_: Any) -> dict:
    """Folds weak hands preflop, calls/checks postflop with anything
    that connects (pair / draw)."""
    allowed = table.get("allowedActions") or {}
    avail = allowed.get("availableActions") or []
    call_chips = int(allowed.get("callChips") or 0)
    pot = int(table.get("potChips") or 0)

    self_seat_num = table.get("selfSeatNumber")
    seats = table.get("seats") or []
    self_seat = next((s for s in seats if s.get("seatNumber") == self_seat_num), {})
    hole = list(self_seat.get("holeCards") or [])
    board = list(table.get("boardCards") or [])

    ranks = "23456789TJQKA"
    def _rank(card: str) -> int:
        return ranks.index(card[0].upper()) if card and card[0].upper() in ranks else 0

    pair = len(hole) == 2 and hole[0][0] == hole[1][0]
    high_card = max((_rank(c) for c in hole), default=0)
    suited = len(hole) == 2 and len(hole[0]) > 1 and len(hole[1]) > 1 and hole[0][-1] == hole[1][-1]

    if not board:
        # Preflop: only continue with pair, high cards, or suited broadways.
        strong = pair or high_card >= 10 or (suited and high_card >= 9)
        if not strong and call_chips > 0:
            return {"action": "fold"}
        if call_chips == 0:
            return {"action": "check"} if "check" in avail else {"action": "fold"}
        return {"action": "call"}

    # Postflop: connect with board?
    board_ranks = {c[0].upper() for c in board}
    hole_ranks = {c[0].upper() for c in hole}
    connects = bool(hole_ranks & board_ranks) or pair
    if call_chips == 0:
        return {"action": "check"} if "check" in avail else {"action": "fold"}
    if connects:
        # call up to 50% pot
        if call_chips <= max(int(pot * 0.5), 1):
            return {"action": "call"}
    return {"action": "fold"}


def bot_loose_passive(table: dict, **_: Any) -> dict:
    """Calls almost anything. Won't fold to small bets, occasional fold to big."""
    allowed = table.get("allowedActions") or {}
    avail = allowed.get("availableActions") or []
    call_chips = int(allowed.get("callChips") or 0)
    pot = int(table.get("potChips") or 0)
    if call_chips == 0:
        return {"action": "check"} if "check" in avail else {"action": "fold"}
    # Fold only if bet is > 200% pot (huge overbet)
    if call_chips > pot * 2 and "fold" in avail:
        return {"action": "fold"}
    return {"action": "call"}


def bot_rock(table: dict, **_: Any) -> dict:
    """Ultra-tight passive — folds to pressure, rarely opens (River Shark shape)."""
    return bot_tight_passive(table)


def bot_maniac(table: dict, **_: Any) -> dict:
    """Loose-aggressive — bets and raises often, calls wide (CallMeMummy shape)."""
    allowed = table.get("allowedActions") or {}
    avail = allowed.get("availableActions") or []
    call_chips = int(allowed.get("callChips") or 0)
    pot = int(table.get("potChips") or 0)

    if call_chips == 0:
        if "bet" in avail and random.random() < 0.72:
            br = allowed.get("betRange") or {}
            lo, hi = int(br.get("min") or 1), int(br.get("max") or 1)
            target = max(lo, min(int(pot * 0.66), hi))
            return {"action": "bet", "amount": target}
        if "check" in avail:
            return {"action": "check"}
        return {"action": "fold"} if "fold" in avail else {"action": "check"}

    if "raise" in avail and random.random() < 0.38:
        rr = allowed.get("raiseRange") or {}
        lo, hi = int(rr.get("min") or 1), int(rr.get("max") or 1)
        target = max(lo, min(int(pot * 0.75 + call_chips * 2), hi))
        return {"action": "raise", "amount": target}
    if "call" in avail and random.random() < 0.78:
        return {"action": "call"}
    return {"action": "fold"} if "fold" in avail else {"action": "call"}


def bot_balanced_lag(table: dict, **_: Any) -> dict:
    """Balanced LAG — wide opens, frequent raises, disciplined calls (not random)."""
    allowed = table.get("allowedActions") or {}
    avail = allowed.get("availableActions") or []
    call_chips = int(allowed.get("callChips") or 0)
    pot = int(table.get("potChips") or 0)

    if call_chips == 0:
        if "bet" in avail and random.random() < 0.58:
            br = allowed.get("betRange") or {}
            lo, hi = int(br.get("min") or 1), int(br.get("max") or 1)
            target = max(lo, min(int(pot * 0.55 + 1), hi))
            return {"action": "bet", "amount": target}
        if "check" in avail:
            return {"action": "check"}
        return {"action": "fold"} if "fold" in avail else {"action": "check"}

    if "raise" in avail and random.random() < 0.32:
        rr = allowed.get("raiseRange") or {}
        lo, hi = int(rr.get("min") or 1), int(rr.get("max") or 1)
        target = max(lo, min(int(pot * 0.7 + call_chips * 2), hi))
        return {"action": "raise", "amount": target}
    if "call" in avail and random.random() < 0.62:
        return {"action": "call"}
    return {"action": "fold"} if "fold" in avail else {"action": "call"}


def bot_durrrr_bomb(table: dict, **_: Any) -> dict:
    """Dwan-shaped bomb LAG — oversized bets/raises for finale durrrr sim."""
    allowed = table.get("allowedActions") or {}
    avail = allowed.get("availableActions") or []
    call_chips = int(allowed.get("callChips") or 0)
    pot = int(table.get("potChips") or 0)

    if call_chips == 0:
        if "bet" in avail:
            br = allowed.get("betRange") or {}
            lo, hi = int(br.get("min") or 1), int(br.get("max") or 1)
            target = max(lo, min(int(max(pot, 1) * 0.85), hi))
            return {"action": "bet", "amount": target}
        if "check" in avail:
            return {"action": "check"}
        return {"action": "fold"} if "fold" in avail else {"action": "check"}

    if "raise" in avail and random.random() < 0.55:
        rr = allowed.get("raiseRange") or {}
        lo, hi = int(rr.get("min") or 1), int(rr.get("max") or 1)
        target = max(lo, min(int(pot * 1.1 + call_chips * 2), hi))
        return {"action": "raise", "amount": target}
    if "call" in avail and random.random() < 0.55:
        return {"action": "call"}
    return {"action": "fold"} if "fold" in avail else {"action": "call"}


def bot_jungleman_calldown(table: dict, **_: Any) -> dict:
    """Jungleman-shaped wide call-down — probes small, calls wide vs pressure."""
    allowed = table.get("allowedActions") or {}
    avail = allowed.get("availableActions") or []
    call_chips = int(allowed.get("callChips") or 0)
    pot = int(table.get("potChips") or 0)

    if call_chips == 0:
        if "bet" in avail and random.random() < 0.45:
            br = allowed.get("betRange") or {}
            lo, hi = int(br.get("min") or 1), int(br.get("max") or 1)
            target = max(lo, min(int(max(pot, 1) * 0.33), hi))
            return {"action": "bet", "amount": target}
        if "check" in avail:
            return {"action": "check"}
        return {"action": "fold"} if "fold" in avail else {"action": "check"}

    if call_chips <= int(max(pot, 1) * 0.55) and "call" in avail:
        return {"action": "call"}
    if "call" in avail and random.random() < 0.72:
        return {"action": "call"}
    return {"action": "fold"} if "fold" in avail else {"action": "call"}


def bot_ten_wide_passive(table: dict, **_: Any) -> dict:
    """TEN ladder S1 shape (K150 export): high VPIP, near-zero PFR, call-down WTSD.

    Arena stats: VPIP 51.6%, PFR ~0, WTSD 86%. Live H2H vs us: uncontested steal pots.
    Local model: limp/complete often first-in; occasional min-steal; call wide; rarely raise.
    """
    allowed = table.get("allowedActions") or {}
    avail = list(allowed.get("availableActions") or [])
    call_chips = int(allowed.get("callChips") or 0)
    pot = int(table.get("potChips") or 0)
    street = str(table.get("street") or "").lower()
    bb = int(table.get("bigBlindChips") or 2)

    if call_chips == 0:
        # First-in / free action: limp or min-steal more than check-fold.
        if street in ("preflop", "") and "call" in avail:
            # SB complete vs BB — limp path (PFR≈0).
            if random.random() < 0.62:
                return {"action": "call"}
        if street in ("preflop", "") and "raise" in avail and random.random() < 0.18:
            rr = allowed.get("raiseRange") or {}
            lo = int(rr.get("min") or max(bb * 2, 1))
            hi = int(rr.get("max") or lo)
            return {"action": "raise", "amount": max(lo, min(lo, hi))}
        if "bet" in avail and random.random() < 0.22:
            br = allowed.get("betRange") or {}
            lo, hi = int(br.get("min") or 1), int(br.get("max") or 1)
            target = max(lo, min(int(max(pot, 1) * 0.40), hi))
            return {"action": "bet", "amount": target}
        if "check" in avail:
            return {"action": "check"}
        if "call" in avail:
            return {"action": "call"}
        return {"action": "fold"} if "fold" in avail else {"action": "check"}

    # Facing a bet: call down (high WTSD); almost never 3-bet.
    if "call" in avail:
        if call_chips <= int(max(pot, 1) * 0.90):
            return {"action": "call"}
        if random.random() < 0.78:
            return {"action": "call"}
    if "raise" in avail and random.random() < 0.04:
        rr = allowed.get("raiseRange") or {}
        lo, hi = int(rr.get("min") or 1), int(rr.get("max") or 1)
        return {"action": "raise", "amount": max(lo, min(lo, hi))}
    return {"action": "fold"} if "fold" in avail else {"action": "call"}


def bot_maniac_shark_lag(table: dict, **_: Any) -> dict:
    """maniac_shark_lite_2 ladder S1 (K151 export): measured LAG, not hyper-maniac.

    Arena stats: VPIP 30.6%, PFR 15.1%, 3-bet 22%, WTSD 22%. Live H2H: min-steal
    bleed + occasional stack-off; folds most showdowns.
    """
    allowed = table.get("allowedActions") or {}
    avail = list(allowed.get("availableActions") or [])
    call_chips = int(allowed.get("callChips") or 0)
    pot = int(table.get("potChips") or 0)
    street = str(table.get("street") or "").lower()
    bb = int(table.get("bigBlindChips") or 2)

    if call_chips == 0:
        if street in ("preflop", "") and "raise" in avail and random.random() < 0.30:
            rr = allowed.get("raiseRange") or {}
            lo = int(rr.get("min") or max(bb * 2, 1))
            hi = int(rr.get("max") or lo)
            return {"action": "raise", "amount": max(lo, min(lo, hi))}
        if "bet" in avail and random.random() < 0.28:
            br = allowed.get("betRange") or {}
            lo, hi = int(br.get("min") or 1), int(br.get("max") or 1)
            target = max(lo, min(int(max(pot, 1) * 0.50), hi))
            return {"action": "bet", "amount": target}
        if "check" in avail:
            return {"action": "check"}
        return {"action": "fold"} if "fold" in avail else {"action": "check"}

    if "raise" in avail and random.random() < 0.22:
        rr = allowed.get("raiseRange") or {}
        lo, hi = int(rr.get("min") or 1), int(rr.get("max") or 1)
        target = max(lo, min(int(pot * 0.65 + call_chips * 2), hi))
        return {"action": "raise", "amount": target}
    if "call" in avail:
        postflop = street not in ("preflop", "")
        call_freq = 0.35 if postflop else 0.48
        if call_chips <= int(max(pot, 1) * 0.55) and random.random() < call_freq + 0.12:
            return {"action": "call"}
        if random.random() < call_freq:
            return {"action": "call"}
    return {"action": "fold"} if "fold" in avail else {"action": "call"}


BOT_POOL = {
    "tight": bot_tight_passive,
    "loose": bot_loose_passive,
    "random": bot_random,
    "call": bot_always_check_call,
    "rock": bot_rock,
    "maniac": bot_maniac,
    "lag": bot_balanced_lag,
    "durrrr_bomb": bot_durrrr_bomb,
    "jungleman_calldown": bot_jungleman_calldown,
    "ten": bot_ten_wide_passive,
    "ten_wide_passive": bot_ten_wide_passive,
    "maniac_shark_lag": bot_maniac_shark_lag,
    "maniac_shark_lite_2": bot_maniac_shark_lag,
    "maniac_shark": bot_maniac_shark_lag,
}

try:
    from ai_pokergame_villain import bot_ai_pokergame_hard  # noqa: WPS433

    BOT_POOL["ai_pokergame_hard"] = bot_ai_pokergame_hard
except ImportError:
    pass


# ─── pokerkit state → arena table dict adapter ──────────────────────────────

def _training_seat_archetypes(n_players: int) -> list[str]:
    """Per-seat archetype tags for mixed training tables."""
    default = (os.environ.get("TRAINING_OPPONENT_MODE") or "rock").lower()
    raw = os.environ.get("TRAINING_SEAT_ARCHETYPES", "").strip()
    if not raw:
        return [default] * n_players
    parts = [p.strip().lower() for p in raw.split(",") if p.strip()]
    if not parts:
        return [default] * n_players
    if len(parts) >= n_players:
        return parts[:n_players]
    return parts + [parts[-1]] * (n_players - len(parts))


def _opponents_for_selfplay(n_players: int, opponent_label: str) -> list[Callable]:
    """Build villain bot list — per-seat when TRAINING_SEAT_ARCHETYPES is set."""
    if os.environ.get("TRAINING_SEAT_ARCHETYPES", "").strip():
        tags = _training_seat_archetypes(n_players)
        default = (os.environ.get("TRAINING_OPPONENT_MODE") or opponent_label or "rock").lower()
        fns: list[Callable] = []
        for i in range(1, n_players):
            arch = tags[i] if i < len(tags) else default
            fns.append(BOT_POOL.get(arch) or BOT_POOL.get(default) or bot_tight_passive)
        return fns
    if opponent_label == "mixed":
        rotation = [bot_tight_passive, bot_loose_passive, bot_random,
                    bot_always_check_call, bot_tight_passive]
        return rotation[: n_players - 1]
    bot = BOT_POOL.get(opponent_label) or bot_tight_passive
    return [bot] * (n_players - 1)


def _arena_card_str(card: Any) -> str:
    """Normalize pokerkit Card / nested list shapes to Arena strings (e.g. ``Ah``)."""
    if isinstance(card, (list, tuple)):
        if not card:
            return ""
        return _arena_card_str(card[0])
    short = repr(card).strip()
    if short.startswith("'") and short.endswith("'"):
        short = short[1:-1]
    if len(short) >= 2 and short[0] == "[" and short[-1] == "]":
        short = short[1:-1]
    if " OF " in short and "(" in short and short.endswith(")"):
        short = short[short.rfind("(") + 1 : -1]
    return short


def _street_label(state: State) -> str:
    # 0 cards → Preflop; 3 → Flop; 4 → Turn; 5 → River.
    n = len(state.board_cards)
    if n <= 0:
        return "Preflop"
    return ("Flop", "Turn", "River")[min(max(n - 3, 0), 2)]


def _villain_handle_for_selfplay() -> str:
    """Optional named nemesis handle for local bots (CEMINI_SELFPLAY_VILLAIN_HANDLE)."""
    raw = (os.environ.get("CEMINI_SELFPLAY_VILLAIN_HANDLE") or "").strip()
    return raw or ""


def _build_table(state: State, hero_idx: int, table_id: str,
                 starting_stacks: list[int], small_blind: int,
                 big_blind: int,
                 *,
                 competition_id: Optional[str] = None) -> dict:
    """Convert a pokerkit State into the arena `table` dict shape that
    decide() expects. Only fields actually consumed by decide() are
    populated."""
    actor = state.actor_index
    is_my_turn = (actor == hero_idx)

    # Pot = sum of all pot amounts + sum of current-street bets.
    pot_total = sum(p.amount for p in state.pots) if state.pots else 0
    bets = list(state.bets) if state.bets else []
    pot_total += sum(bets)

    seats = []
    train_tags = _training_seat_archetypes(len(starting_stacks)) if competition_id else None
    villain_handle = _villain_handle_for_selfplay()
    for i in range(len(starting_stacks)):
        hole = list(state.hole_cards[i]) if i < len(state.hole_cards) else []
        hole_strs = [_arena_card_str(c) for c in hole] if (i == hero_idx and hole) else []
        street_bet = int(bets[i]) if i < len(bets) else 0
        is_hero = i == hero_idx
        handle = "hero" if is_hero else (villain_handle or f"bot_{i+1}")
        seat: dict = {
            "seatNumber": i + 1,
            "agentId": f"local_seat_{i+1}" if is_hero else (villain_handle or f"local_seat_{i+1}"),
            "agentHandle": handle,
            "holeCards": hole_strs,
            "stackChips": int(state.stacks[i]),
            "currentBetChips": street_bet,
            "status": "Active",
        }
        if not is_hero and villain_handle:
            seat["agentName"] = villain_handle
            seat["agentId"] = villain_handle
        if train_tags and i != hero_idx:
            seat["trainingArchetype"] = train_tags[i]
        seats.append(seat)

    table: dict = {
        "tableId": table_id,
        "potChips": int(pot_total),
        "street": _street_label(state),
        "boardCards": [_arena_card_str(c) for c in state.board_cards],
        "selfSeatNumber": hero_idx + 1,
        "smallBlindChips": int(small_blind),
        "bigBlindChips": int(big_blind),
        "seats": seats,
    }
    if competition_id:
        table["competitionId"] = competition_id

    available: list[str] = []
    call_chips = 0
    call_to_amount = 0
    can_check = can_bet = can_raise = False
    bet_min = bet_max = 0
    raise_min = raise_max = 0

    if is_my_turn:
        if state.can_fold():
            available.append("fold")
        if state.can_check_or_call():
            call_chips = int(state.checking_or_calling_amount or 0)
            if call_chips == 0:
                available.append("check")
                can_check = True
            else:
                available.append("call")
                call_to_amount = (bets[hero_idx] if hero_idx < len(bets) else 0) + call_chips
        if state.can_complete_bet_or_raise_to():
            try:
                rmin = int(state.min_completion_betting_or_raising_to_amount or 0)
                rmax = int(state.max_completion_betting_or_raising_to_amount or 0)
            except Exception:
                rmin, rmax = 0, 0
            # If any opponent has voluntarily put in chips on this street
            # beyond the blind, treat as "raise"; otherwise it's a "bet".
            max_bet_so_far = max(bets) if bets else 0
            if max_bet_so_far > big_blind or call_chips > 0:
                available.append("raise")
                can_raise, raise_min, raise_max = True, rmin, rmax
            else:
                available.append("bet")
                can_bet, bet_min, bet_max = True, rmin, rmax

    # Button seat — stable for the whole hand (opener_index works all streets).
    n_players = len(starting_stacks)
    if state.opener_index is not None and n_players >= 2:
        offset = {6: 3, 5: 2, 4: 1, 3: 0, 2: 0}.get(n_players, 3)
        btn_idx = (int(state.opener_index) - offset) % n_players
        table["buttonSeatNumber"] = btn_idx + 1
    else:
        try:
            _examples = Path(__file__).resolve().parent
            if str(_examples) not in sys.path:
                sys.path.insert(0, str(_examples))
            from position_utils import infer_button_seat  # noqa: WPS433
            btn = infer_button_seat(table)
            if btn is not None:
                table["buttonSeatNumber"] = btn
        except Exception:
            pass

    table["allowedActions"] = {
        "availableActions": available,
        "callChips": int(call_chips),
        "callToAmount": int(call_to_amount),
        "canCheck": bool(can_check),
        "canBet": bool(can_bet),
        "canRaise": bool(can_raise),
        "betRange": {"min": int(bet_min), "max": int(bet_max)},
        "raiseRange": {"min": int(raise_min), "max": int(raise_max)},
    }
    table["secondsUntilDeadline"] = 10.0
    return table


def _apply_action(state: State, action: dict, big_blind: int) -> None:
    """Apply the chosen action to the pokerkit state."""
    name = (action.get("action") or "").lower()
    amount = action.get("amount")
    try:
        if name == "fold":
            state.fold()
        elif name in ("check", "call"):
            state.check_or_call()
        elif name in ("bet", "raise"):
            try:
                lo = int(state.min_completion_betting_or_raising_to_amount or big_blind)
                hi = int(state.max_completion_betting_or_raising_to_amount or lo)
            except Exception:
                lo, hi = big_blind, big_blind * 100
            if amount is None:
                amount = lo
            amount = max(lo, min(int(amount), hi))
            state.complete_bet_or_raise_to(amount)
        else:
            # Unknown action → fold as safe fallback.
            state.fold()
    except Exception as e:
        # Illegal at the engine level — fold to keep the hand moving.
        print(f"  [selfplay] WARN: action {name}/{amount} rejected ({e}); folding",
              file=sys.stderr)
        try:
            state.fold()
        except Exception:
            pass


# ─── Decide loader (mirror agent.py's --agent loader) ────────────────────────

def _load_decide_from_path(path: str) -> Callable:
    p = Path(path).resolve()
    if not p.exists():
        raise SystemExit(f"--agent path not found: {p}")
    spec = importlib.util.spec_from_file_location("user_agent", str(p))
    if not spec or not spec.loader:
        raise SystemExit(f"could not load module from {p}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if not hasattr(mod, "decide"):
        raise SystemExit(f"{p} does not define decide()")
    return mod.decide


# ─── Selfplay engine ────────────────────────────────────────────────────────

def play_one_hand(decide_fn: Callable, opponents: list[Callable],
                  starting_stack: int, small_blind: int, big_blind: int,
                  hand_id: int, hero_idx: int = 0,
                  max_actions: int = 200,
                  *,
                  training_hud: bool = False,
                  trajectory: Optional[list[dict]] = None) -> int:
    """Play a single hand; return hero's chip delta (final stack -
    starting stack)."""
    n = 1 + len(opponents)
    stacks = [starting_stack] * n
    state: State = NoLimitTexasHoldem.create_state(
        automations=(
            Automation.ANTE_POSTING,
            Automation.BET_COLLECTION,
            Automation.BLIND_OR_STRADDLE_POSTING,
            Automation.CARD_BURNING,
            Automation.HOLE_DEALING,
            Automation.BOARD_DEALING,
            Automation.RUNOUT_COUNT_SELECTION,
            Automation.HOLE_CARDS_SHOWING_OR_MUCKING,
            Automation.HAND_KILLING,
            Automation.CHIPS_PUSHING,
            Automation.CHIPS_PULLING,
        ),
        ante_trimming_status=True,
        raw_antes=0,
        raw_blinds_or_straddles=(small_blind, big_blind) + (0,) * (n - 2),
        min_bet=big_blind,
        raw_starting_stacks=tuple(stacks),
        player_count=n,
    )

    table_id = f"local-{hand_id:05d}"
    train_cid = "training-local" if training_hud else None
    steps = 0
    hero_step = 0
    while state.status and state.actor_index is not None and steps < max_actions:
        actor = state.actor_index
        table = _build_table(
            state, actor, table_id, stacks, small_blind, big_blind,
            competition_id=train_cid,
        )
        # Pick the deciding function for this seat.
        if actor == hero_idx:
            fn = decide_fn
        else:
            opp_idx = actor if actor < hero_idx else actor - 1
            fn = opponents[opp_idx % len(opponents)]
        try:
            action = fn(table, deadline_s=10.0)
        except TypeError:
            action = fn(table)
        if not isinstance(action, dict):
            action = {"action": "fold"}
        if trajectory is not None and actor == hero_idx:
            hero_step += 1
            # K125 P2: collect telemetry from cemini_decide if available
            telemetry = None
            if fn.__module__ == "cemini_decide":
                try:
                    from cemini_decide import get_trajectory_bound_telemetry  # noqa: WPS433
                    telemetry = get_trajectory_bound_telemetry()
                except Exception:
                    pass
            trajectory.append(_hero_trajectory_row(
                hand_id=hand_id,
                step=hero_step,
                table=table,
                action=action,
                n_players=n,
                big_blind=big_blind,
                telemetry=telemetry,
            ))
        _apply_action(state, action, big_blind)
        steps += 1

    final = int(state.stacks[hero_idx])
    if trajectory is not None:
        hand_result: dict = {
            "record_type": "hand_result",
            "hand_id": hand_id,
            "chip_delta": final - starting_stack,
            "hero_decisions": hero_step,
        }
        if n == 2:
            probe = _hu_showdown_probe_labels(state, hero_idx)
            if probe:
                hand_result.update(probe)
        trajectory.append(hand_result)
    return final - starting_stack


def _hu_showdown_probe_labels(state: State, hero_idx: int) -> dict:
    """K129 IRumAI probe: villain hole + board at hand end (HU selfplay only)."""
    villain_idx = 1 if hero_idx == 0 else 0
    if villain_idx >= len(state.hole_cards):
        return {}
    vhole = list(state.hole_cards[villain_idx])
    if len(vhole) < 2:
        return {}
    board = [_arena_card_str(c) for c in state.board_cards]
    villain_key = "".join(_arena_card_str(c) for c in vhole)
    return {
        "board_key": "".join(board),
        "villain_hole_key": villain_key,
        "villain_seat": villain_idx + 1,
    }


def _hero_trajectory_row(
    hand_id: int,
    step: int,
    table: dict,
    action: dict,
    n_players: int,
    big_blind: int,
    telemetry: Optional[dict] = None,
) -> dict:
    """One hero decision for Researcher Round trajectory export.

    Args:
        telemetry: Optional telemetry dict from cemini_decide.get_trajectory_bound_telemetry()
    """
    aa = table.get("allowedActions") or {}
    reasoning = str(action.get("reasoning") or "")
    pos = "?"
    try:
        from position_utils import hero_position_label  # noqa: WPS433
        pos = hero_position_label(table)
    except Exception:
        pass
    hole_key = ""
    try:
        self_num = table.get("selfSeatNumber")
        seats = table.get("seats") or []
        self_seat = next(
            (s for s in seats if s.get("seatNumber") == self_num), {},
        )
        cards = self_seat.get("holeCards") or []
        hole_key = "".join(str(c) for c in cards)
    except Exception:
        pass
    pot = int(table.get("potChips") or 0)
    amt = action.get("amount")
    bet_bucket = _bet_size_bucket(action.get("action"), amt, pot, big_blind)
    row: dict = {
        "record_type": "decision",
        "hand_id": hand_id,
        "step": step,
        "street": table.get("street"),
        "position": pos,
        "n_players": n_players,
        "action": action.get("action"),
        "amount": amt,
        "pot_chips": pot,
        "call_chips": aa.get("callChips"),
        "bet_size_bucket": bet_bucket,
        "reasoning_len": len(reasoning),
        "reasoning": reasoning[:180],
        "hole_key": hole_key,
    }
    # K125 P2 Memory-Gap telemetry (only when using cemini_decide)
    if telemetry:
        row["session_memory_on"] = telemetry.get("session_memory_on")
        row["trajectory_bound_risk"] = telemetry.get("cumulative_risk")
        row["trajectory_bound_veto"] = telemetry.get("veto_applied")
    return row


def _bet_size_bucket(
    action_name: Optional[str],
    amount: Optional[int],
    pot: int,
    big_blind: int,
) -> str:
    name = (action_name or "").lower()
    if name not in ("bet", "raise", "all-in"):
        return "none"
    if amount is None:
        return "unknown"
    try:
        amt = int(amount)
    except (TypeError, ValueError):
        return "unknown"
    ref = max(pot, big_blind * 2, 1)
    ratio = amt / ref
    if ratio <= 0.4:
        return "small"
    if ratio <= 0.75:
        return "medium"
    if ratio <= 1.25:
        return "pot"
    return "large"


def _match_win_rate(wins: int, losses: int) -> Optional[float]:
    """Win rate excluding pushes; None when no decisive outcomes."""
    decisive = wins + losses
    if decisive <= 0:
        return None
    return wins / decisive


def _match_series_from_deltas(deltas: list[int], match_hands: int) -> dict:
    """Aggregate hand deltas into fixed-size matches (net chips per match)."""
    match_wins = match_losses = match_pushes = 0
    for start in range(0, len(deltas), match_hands):
        chunk = deltas[start:start + match_hands]
        if len(chunk) < match_hands:
            break
        net = sum(chunk)
        if net > 0:
            match_wins += 1
        elif net < 0:
            match_losses += 1
        else:
            match_pushes += 1
    return {
        "match_hands": match_hands,
        "matches": match_wins + match_losses + match_pushes,
        "match_wins": match_wins,
        "match_losses": match_losses,
        "match_pushes": match_pushes,
        "match_win_rate": _match_win_rate(match_wins, match_losses),
    }


def run_selfplay(decide_fn: Callable, n_hands: int, opponent_label: str,
                 n_players: int, starting_stack: int, small_blind: int,
                 big_blind: int, seed: Optional[int] = None,
                 *,
                 training_hud: bool = False,
                 trajectory_out: Optional[Path] = None,
                 match_hands: Optional[int] = None,
                 n_matches: Optional[int] = None) -> dict:
    """Run N hands and return aggregate stats."""
    if seed is not None:
        random.seed(seed)
    # Build opponents list (length = n_players - 1).
    opponents = _opponents_for_selfplay(n_players, opponent_label)

    trajectory: list[dict] = []
    deltas: list[int] = []
    t0 = time.time()
    for i in range(n_hands):
        try:
            d = play_one_hand(decide_fn, opponents,
                              starting_stack=starting_stack,
                              small_blind=small_blind, big_blind=big_blind,
                              hand_id=i + 1,
                              hero_idx=i % n_players,
                              training_hud=training_hud,
                              trajectory=trajectory if trajectory_out else None)
        except Exception as e:
            print(f"  [selfplay] WARN: hand {i+1} failed ({e}); counted as 0",
                  file=sys.stderr)
            d = 0
        deltas.append(d)
        if (i + 1) % max(1, n_hands // 10) == 0:
            print(f"  ... {i+1}/{n_hands} hands  net={sum(deltas):+d} chips")
    elapsed = time.time() - t0

    net = sum(deltas)
    wins = sum(1 for d in deltas if d > 0)
    losses = sum(1 for d in deltas if d < 0)
    pushes = n_hands - wins - losses
    bb_per_100 = (net / big_blind) / max(n_hands, 1) * 100

    match_stats: dict = {}
    if n_players == 2:
        match_stats["hand_match_win_rate"] = _match_win_rate(wins, losses)
    if match_hands is not None and match_hands > 0:
        match_stats.update(_match_series_from_deltas(deltas, match_hands))
    elif n_players == 2:
        match_stats.update({
            "match_wins": wins,
            "match_losses": losses,
            "match_pushes": pushes,
            "match_win_rate": match_stats["hand_match_win_rate"],
        })

    trajectory_path: Optional[str] = None
    if trajectory_out is not None:
        trajectory_out.parent.mkdir(parents=True, exist_ok=True)
        with trajectory_out.open("w", encoding="utf-8") as fh:
            for row in trajectory:
                fh.write(json.dumps(row, sort_keys=True) + "\n")
        trajectory_path = str(trajectory_out)

    result = {
        "hands": n_hands,
        "opponent": opponent_label,
        "players": n_players,
        "net_chips": net,
        "wins": wins,
        "losses": losses,
        "pushes": pushes,
        "bb_per_100": bb_per_100,
        "elapsed_s": elapsed,
        "hands_per_s": n_hands / max(elapsed, 0.001),
        "trajectory_path": trajectory_path,
        "trajectory_decisions": sum(
            1 for r in trajectory if r.get("record_type") == "decision"
        ),
    }
    result.update(match_stats)
    return result


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Run local self-play hands against simple bots for fast decide() "
            "iteration. No network. No Arena API. NOT a replacement for "
            "`pokerkit run` (which scores you against DeepCFR)."
        ),
    )
    parser.add_argument("--hands", type=int, default=200,
                        help="Number of hands to play (default 200)")
    parser.add_argument("--players", type=int, default=2,
                        help="Total players including hero, 2-6 (default 2 = HU)")
    parser.add_argument("--opponent", default="tight",
                        choices=sorted(set(BOT_POOL.keys()) | {"mixed"}),
                        help="Opponent profile (default tight)")
    parser.add_argument("--agent", default=None,
                        help="Path to a Python file defining decide(); "
                             "default uses examples/agent.py")
    parser.add_argument("--starting-stack", type=int, default=200,
                        help="Starting stack per player in chips (default 200 = 100 BB)")
    parser.add_argument("--small-blind", type=int, default=1)
    parser.add_argument("--big-blind", type=int, default=2)
    parser.add_argument("--seed", type=int, default=None,
                        help="RNG seed for reproducible runs")
    parser.add_argument("--training-hud", action="store_true",
                        help="Exercise cemini HUD path offline (competitionId=training-local; "
                             "set TRAINING_OPPONENT_MODE or match --opponent rock/maniac)")
    parser.add_argument("--trajectory-out", default=None,
                        help="Write hero decision trajectory JSONL (Researcher Round)")
    parser.add_argument("--match-hands", type=int, default=None,
                        help="HU: treat N hands as one match (net chips); "
                             "use with --matches for a series")
    parser.add_argument("--matches", type=int, default=None,
                        help="HU: number of matches when --match-hands is set "
                             "(total hands = match-hands × matches)")
    args = parser.parse_args(argv)

    if args.training_hud and args.opponent in ("rock", "maniac", "tight"):
        os.environ.setdefault("TRAINING_OPPONENT_MODE", args.opponent)

    if args.players < 2 or args.players > 6:
        print("ERROR: --players must be between 2 and 6.", file=sys.stderr)
        return 2

    match_hands = args.match_hands
    n_matches = args.matches
    n_hands = args.hands
    if match_hands is not None:
        if match_hands < 1:
            print("ERROR: --match-hands must be >= 1.", file=sys.stderr)
            return 2
        if n_matches is None:
            n_matches = max(1, n_hands // match_hands)
        if n_matches < 1:
            print("ERROR: --matches must be >= 1.", file=sys.stderr)
            return 2
        n_hands = match_hands * n_matches
        if args.players != 2:
            print("ERROR: --match-hands / --matches require --players 2 (HU).",
                  file=sys.stderr)
            return 2

    # Load decide().
    if args.agent:
        decide_fn = _load_decide_from_path(args.agent)
        src = args.agent
    else:
        # Default — import from sibling agent.py.
        here = Path(__file__).resolve().parent
        if str(here) not in sys.path:
            sys.path.insert(0, str(here))
        import agent  # noqa: WPS433
        decide_fn = agent.decide
        src = "examples/agent.py"

    print(f"[selfplay] hero=decide() from {src}")
    print(f"[selfplay] opponents={args.opponent} x{args.players - 1}  "
          f"players={args.players}  stacks={args.starting_stack}  "
          f"blinds={args.small_blind}/{args.big_blind}  seed={args.seed}")
    if match_hands is not None:
        print(f"[selfplay] playing {n_matches} matches × {match_hands} hands "
              f"({n_hands} total) ...")
    else:
        print(f"[selfplay] playing {n_hands} hands ...")
    if args.training_hud:
        print(f"[selfplay] training HUD mode={os.environ.get('TRAINING_OPPONENT_MODE', '?')} "
              f"(private opponent_hud_exploit required)")

    traj_out = Path(args.trajectory_out) if args.trajectory_out else None

    stats = run_selfplay(
        decide_fn=decide_fn,
        n_hands=n_hands,
        opponent_label=args.opponent,
        n_players=args.players,
        starting_stack=args.starting_stack,
        small_blind=args.small_blind,
        big_blind=args.big_blind,
        seed=args.seed,
        training_hud=args.training_hud,
        trajectory_out=traj_out,
        match_hands=match_hands,
        n_matches=n_matches,
    )

    sep = "─" * 56
    print("")
    print(sep)
    print(f"  hands       : {stats['hands']}")
    print(f"  opponent    : {stats['opponent']} x{stats['players'] - 1}")
    print(f"  wins/losses : {stats['wins']}/{stats['losses']}  "
          f"(push: {stats['pushes']})")
    if stats.get("players") == 2 and stats.get("hand_match_win_rate") is not None:
        hw = stats["wins"]
        hl = stats["losses"]
        print(f"  hand_win_rate: {stats['hand_match_win_rate']:.1%}  ({hw}/{hw + hl})")
    if match_hands is not None and stats.get("matches") is not None:
        mw = stats.get("match_wins", 0)
        ml = stats.get("match_losses", 0)
        mwr = stats.get("match_win_rate")
        mwr_s = f"{mwr:.1%}" if mwr is not None else "n/a"
        print(f"  match series: {mw}/{ml}  (push: {stats['match_pushes']})  "
              f"series_win_rate={mwr_s}  "
              f"@ {match_hands} hands/match × {stats['matches']} matches")
    print(f"  net chips   : {stats['net_chips']:+d}")
    print(f"  bb/100      : {stats['bb_per_100']:+.1f}")
    print(f"  elapsed     : {stats['elapsed_s']:.1f}s  "
          f"({stats['hands_per_s']:.0f} hands/s)")
    if stats.get("trajectory_path"):
        print(f"  trajectory  : {stats['trajectory_path']} "
              f"({stats.get('trajectory_decisions', 0)} decisions)")
    print(sep)
    print("")
    print("  Reminder: this is vs SIMPLE local bots, NOT DeepCFR.")
    print("  Confirm improvements with `pokerkit run --max-hands 50` on Arena.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
