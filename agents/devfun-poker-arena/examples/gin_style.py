"""Gin poker-bot anti_threshold lanes — score-based preflop + HU aggression.

Ported from https://github.com/gin/poker-bot (v1) for Cemini tournament posture.
Enable via CEMINI_GIN_STYLE_PREFLOP / CEMINI_GIN_STYLE_POSTFLOP (or CEMINI_GIN_STYLE=1).
"""
from __future__ import annotations

import itertools
import os
from typing import Optional

from opponent_target import is_preflop_open_spot  # noqa: E402
from position_utils import hero_is_in_position
from table_format_utils import resolve_table_format

RANK_VALUES = {rank: index for index, rank in enumerate("23456789TJQKA", start=2)}
_RANK_CHARS = set(RANK_VALUES.keys())
BIG_BLIND = 20


def _norm_card(card: str) -> str:
    """Arena 'Ah' or selfplay pokerkit repr '[Ah]'."""
    s = (card or "").strip()
    if s.startswith("[") and s.endswith("]"):
        s = s[1:-1]
    if len(s) >= 2 and s[0].upper() in _RANK_CHARS:
        return s[0].upper() + s[-1].lower()
    return s


def _norm_cards(cards: list[str]) -> list[str]:
    return [_norm_card(c) for c in cards if c]


def _hand_class(hole_cards: list[str]) -> str:
    cards = _norm_cards(hole_cards)
    if len(cards) != 2:
        return ""
    ranks = "23456789TJQKA"
    r1, s1 = cards[0][0].upper(), cards[0][1]
    r2, s2 = cards[1][0].upper(), cards[1][1]
    if r1 not in ranks or r2 not in ranks:
        return ""
    if ranks.index(r1) < ranks.index(r2):
        r1, r2 = r2, r1
        s1, s2 = s2, s1
    if r1 == r2:
        return r1 + r2
    return f"{r1}{r2}{'s' if s1 == s2 else 'o'}"

ActionPair = tuple[str, Optional[int]]


def gin_killed() -> bool:
    """Master kill — T10 post-mortem 2026-08-01: gin ON zeroed the stack.

    Prod / playground always set CEMINI_GIN_KILL=1. Unit tests leave it unset
    so CEMINI_GIN_STYLE=* still exercises the ported lanes.
    """
    return os.environ.get("CEMINI_GIN_KILL", "0").strip().lower() in (
        "1", "true", "yes", "on",
    )


def gin_style_preflop_enabled() -> bool:
    if gin_killed():
        return False
    raw = os.environ.get(
        "CEMINI_GIN_STYLE_PREFLOP",
        os.environ.get("CEMINI_GIN_STYLE", "0"),
    )
    return raw.strip().lower() in ("1", "true", "yes", "on")


def gin_style_postflop_enabled() -> bool:
    if gin_killed():
        return False
    raw = os.environ.get(
        "CEMINI_GIN_STYLE_POSTFLOP",
        os.environ.get("CEMINI_GIN_STYLE", "0"),
    )
    return raw.strip().lower() in ("1", "true", "yes", "on")


def gin_v008_preflop_enabled() -> bool:
    """gin/poker-bot auto_research_v008 marginal defend + blind widen."""
    if gin_killed():
        return False
    explicit = os.environ.get("CEMINI_GIN_V008", "").strip().lower()
    if explicit in ("0", "false", "no", "off"):
        return False
    if explicit in ("1", "true", "yes", "on"):
        return True
    return gin_style_preflop_enabled()


# Ported from gin/poker-bot auto_research_v008 (2026-06 GitHub recon).
PREFLOP_LOOSE_CALL_MIN_SCORE = 38
PREFLOP_LOOSE_CALL_SCORE_THRESHOLD = 50
PREFLOP_LOOSE_CALL_MAX_PRICE_IP = 0.28
PREFLOP_LOOSE_CALL_MAX_PRICE_BB = 0.25
PREFLOP_LOOSE_CALL_MAX_PRICE_OOP = 0.20
PREFLOP_LOOSE_CALL_MAX_OPPONENTS = 3
PREFLOP_DEFENSE_MIN_SCORE = 50
PREFLOP_DEFENSE_MAX_PRICE: dict[str, float] = {"BB": 0.40, "SB": 0.24}
PREFLOP_DEFENSE_MAX_STACK_FRACTION = 0.12
PREFLOP_V008_MAX_STACK_FRACTION = 0.15
HU_SB_STEAL_BET_OPEN = 42
HU_SB_STEAL_RAISE = 40
HU_TARGET_VPIP_MIN = 0.28
HU_TARGET_VPIP_MAX = 0.38
HU_BB_DEFEND_MIN_SCORE = 44
HU_SB_STEAL_TRIM = frozenset({"A5o", "A4o", "85s", "53s", "43s"})


def _gin_style_gate_open() -> bool:
    return os.environ.get("CEMINI_GIN_STYLE_GATE", "").strip().lower() in (
        "1", "true", "yes", "on",
    )


def _gin_preflop_thresholds(
    ip: bool,
    *,
    placement_chase: bool = False,
) -> tuple[int, int, int, int, int]:
    """Return play, bet-open, raise-open, premium-raise ip/oop score floors."""
    if _gin_style_gate_open():
        # S2 prep — wider opens so Arena PFR moves off ~1% nit baseline.
        play, bet_open, raise_open, premium_ip, premium_oop = (
            34, 46, 58 if ip else 64, 82 if ip else 88, 88 if ip else 92
        )
    else:
        play, bet_open, raise_open, premium_ip, premium_oop = (
            38 if ip else 44,
            56,
            72 if ip else 78,
            88 if ip else 92,
            92 if ip else 96,
        )
    if placement_chase:
        play -= 6
        bet_open -= 8
        raise_open -= 8
        premium_ip -= 4
        premium_oop -= 4
    return play, bet_open, raise_open, premium_ip, premium_oop


def preflop_score(hole_cards: list[str]) -> int:
    hole_cards = _norm_cards(hole_cards)
    if len(hole_cards) != 2:
        return 0
    first, second = card_values(hole_cards)
    high, low = max(first, second), min(first, second)
    score = high * 3 + low
    if first == second:
        score += 34 + high * 2
    if _norm_card(hole_cards[0])[1] == _norm_card(hole_cards[1])[1]:
        score += 8
    if abs(first - second) == 1:
        score += 5
    if high >= 12 and low >= 10:
        score += 12
    return score


def card_values(cards: list[str]) -> list[int]:
    return [RANK_VALUES.get(_norm_card(card)[0].upper(), 0) for card in cards]


def board_texture(board_cards: list[str]) -> dict:
    board_cards = _norm_cards(board_cards)
    suits = [_norm_card(card)[1] for card in board_cards]
    values = sorted(set(card_values(board_cards)))
    max_suit_count = max((suits.count(suit) for suit in set(suits)), default=0)
    connected = any(
        values[index + 2] - values[index] <= 4 for index in range(len(values) - 2)
    )
    paired = len(values) < len(board_cards)
    return {
        "wet": max_suit_count >= 3 or connected,
        "paired": paired,
        "high": any(value >= 12 for value in values),
    }


def rank_five(cards: list[str]) -> tuple:
    cards = _norm_cards(cards)
    values = RANK_VALUES
    ranks = sorted((values[_norm_card(card)[0].upper()] for card in cards), reverse=True)
    counts: dict[int, int] = {}
    suits: dict[str, int] = {}
    for card in cards:
        nc = _norm_card(card)
        rank = values[nc[0].upper()]
        suit = nc[1]
        counts[rank] = counts.get(rank, 0) + 1
        suits[suit] = suits.get(suit, 0) + 1

    sorted_counts = sorted(
        counts.items(), key=lambda item: (item[1], item[0]), reverse=True
    )
    flush_suit = next((suit for suit, count in suits.items() if count >= 5), None)
    flush_ranks: list[int] = []
    if flush_suit:
        flush_ranks = sorted(
            [values[_norm_card(card)[0].upper()] for card in cards if _norm_card(card)[1] == flush_suit],
            reverse=True,
        )

    unique_ranks = sorted(set(ranks), reverse=True)
    wheel_ranks = [5, 4, 3, 2, 1] if 14 in unique_ranks else []

    def straight_top(rank_list: list[int]) -> Optional[int]:
        for index in range(len(rank_list) - 4):
            window = rank_list[index : index + 5]
            if window[0] - window[4] == 4 and len(set(window)) == 5:
                return window[0]
        return None

    straight_top_rank = straight_top(unique_ranks)
    if (
        straight_top_rank is None
        and wheel_ranks
        and all(rank in unique_ranks for rank in [5, 4, 3, 2, 14])
    ):
        straight_top_rank = 5

    straight_flush_top = None
    if flush_suit:
        flush_cards = [card for card in cards if _norm_card(card)[1] == flush_suit]
        flush_ranks_unique = sorted(
            {values[_norm_card(card)[0].upper()] for card in flush_cards}, reverse=True
        )
        straight_flush_top = straight_top(flush_ranks_unique)
        if (
            straight_flush_top is None
            and wheel_ranks
            and all(rank in flush_ranks_unique for rank in [5, 4, 3, 2, 14])
        ):
            straight_flush_top = 5

    if straight_flush_top:
        return (8, straight_flush_top)

    if sorted_counts[0][1] == 4:
        quad_rank = sorted_counts[0][0]
        kicker = max(rank for rank in unique_ranks if rank != quad_rank)
        return (7, quad_rank, kicker)

    if sorted_counts[0][1] == 3 and len(sorted_counts) > 1 and sorted_counts[1][1] >= 2:
        return (6, sorted_counts[0][0], sorted_counts[1][0])

    if flush_ranks:
        return (5,) + tuple(flush_ranks[:5])

    if straight_top_rank:
        return (4, straight_top_rank)

    if sorted_counts[0][1] == 3:
        triple_rank = sorted_counts[0][0]
        kickers = [rank for rank in unique_ranks if rank != triple_rank][:2]
        return (3, triple_rank, *kickers)

    if sorted_counts[0][1] == 2 and len(sorted_counts) > 1 and sorted_counts[1][1] == 2:
        pair_high = sorted_counts[0][0]
        pair_low = sorted_counts[1][0]
        kicker = [rank for rank in unique_ranks if rank not in (pair_high, pair_low)][0]
        return (2, pair_high, pair_low, kicker)

    if sorted_counts[0][1] == 2:
        pair_rank = sorted_counts[0][0]
        kickers = [rank for rank in unique_ranks if rank != pair_rank][:3]
        return (1, pair_rank, *kickers)

    return (0, *unique_ranks[:5])


def evaluate_hand(cards: list[str]) -> tuple:
    return max(rank_five(list(combo)) for combo in itertools.combinations(cards, 5))


def made_hand_rank(hole_cards: list[str], board_cards: list[str]) -> int:
    hole_cards = _norm_cards(hole_cards)
    board_cards = _norm_cards(board_cards)
    if len(board_cards) < 3:
        return 0
    board_rank = evaluate_hand(board_cards) if len(board_cards) >= 5 else (0,)
    full_rank = evaluate_hand(list(hole_cards) + list(board_cards))
    category = full_rank[0]
    if len(board_cards) >= 5 and full_rank == board_rank:
        return 0
    return category


def has_top_pair_or_better(hole_cards: list[str], board_cards: list[str]) -> bool:
    hole_cards = _norm_cards(hole_cards)
    board_cards = _norm_cards(board_cards)
    if not board_cards:
        return False
    board_high = max(card_values(board_cards))
    hole_values = card_values(hole_cards)
    all_values = card_values(list(hole_cards) + list(board_cards))
    return any(
        value == board_high and all_values.count(value) >= 2 for value in hole_values
    )


def pot_odds(call_amount: int, pot: int) -> float:
    if call_amount <= 0:
        return 0.0
    return call_amount / (pot + call_amount)


def _capped(amount: int, allowed: dict) -> int:
    max_commit = int(allowed.get("maxCommit") or amount)
    return max(0, min(amount, max_commit))


def _call_chips(allowed: dict) -> int:
    return int(allowed.get("callChips") or allowed.get("callAmount") or 0)


def _min_bet(allowed: dict, pot: int) -> int:
    br = allowed.get("betRange") or {}
    if br.get("min") is not None:
        return int(br["min"])
    raw = allowed.get("minBet")
    if raw is not None:
        return int(raw)
    return max(int(pot * 0.33), BIG_BLIND)


def _min_raise_to(table: dict, allowed: dict) -> Optional[int]:
    rr = allowed.get("raiseRange") or {}
    if rr.get("min") is not None:
        return int(rr["min"])
    raw = allowed.get("minRaiseTo")
    if raw is not None:
        return int(raw)
    return None


def active_opponents(table: dict) -> int:
    seats = table.get("seats") or []
    self_num = table.get("selfSeatNumber")
    count = 0
    for seat in seats:
        if seat.get("seatNumber") == self_num:
            continue
        if seat.get("folded") or seat.get("hasFolded"):
            continue
        count += 1
    return max(1, count)


def _value_bet_amount(pot: int, allowed: dict, *, strong: bool = False) -> int:
    minimum = _min_bet(allowed, pot)
    if pot <= 0:
        return _capped(max(minimum, BIG_BLIND), allowed)
    size = 0.50 if strong else 0.33
    return _capped(max(minimum, int(pot * size)), allowed)


def _pressure_amount(pot: int, allowed: dict, target_required: float = 0.20) -> int:
    minimum = _min_bet(allowed, pot)
    if pot <= 0:
        return _capped(max(minimum, BIG_BLIND), allowed)
    raw = int((target_required * pot) / max(0.01, 1 - target_required))
    amount = max(minimum, raw + 1, int(pot * 0.30))
    return _capped(amount, allowed)


def _raise_amount(table: dict, allowed: dict, *, strong: bool = False) -> Optional[int]:
    minimum = _min_raise_to(table, allowed)
    if minimum is None:
        return None
    pot = int(table.get("potChips") or 0)
    current_bet = int(table.get("currentBet") or 0)
    size = 0.66 if strong else 0.40
    target = current_bet + int(max(pot, BIG_BLIND) * size)
    return _capped(max(minimum, target), allowed)


def _should_cbet(texture: dict, opponents: int) -> bool:
    if not texture:
        return True
    return not texture.get("wet", False) or opponents <= 1


def try_preflop(
    table: dict,
    allowed: dict,
    available: list[str],
    hole: list[str],
    position: str,
    *,
    in_position: Optional[bool] = None,
    placement_chase: bool = False,
) -> Optional[ActionPair]:
    """Score-based preflop (anti_threshold thresholds). None = defer to chart."""
    if not gin_style_preflop_enabled():
        return None

    ip = in_position if in_position is not None else hero_is_in_position(table)
    pot = int(table.get("potChips") or 0)
    call_amount = _call_chips(allowed)
    required = pot_odds(call_amount, pot)
    score = preflop_score(hole)
    open_spot = is_preflop_open_spot(table, allowed, call_amount)

    play_threshold, bet_open_threshold, raise_threshold, premium_threshold, _ = (
        _gin_preflop_thresholds(ip, placement_chase=placement_chase)
    )
    hu = resolve_table_format(table) == "hu"
    if hu:
        raise_threshold = min(raise_threshold, bet_open_threshold)
    if hu and open_spot and position in ("SB", "BTN"):
        bet_open_threshold = max(38, min(bet_open_threshold, HU_SB_STEAL_BET_OPEN))
        raise_threshold = max(38, min(raise_threshold, HU_SB_STEAL_RAISE))
        if _hand_class(hole) in HU_SB_STEAL_TRIM:
            if "fold" in available:
                return "fold", None
            return None

    if call_amount > 0 and not open_spot:
        # HU BB: defer to research_static_chart + S1B defend (gin score floors over-fold).
        if hu and position == "BB":
            return None
        hu_raise_floor = raise_threshold - (14 if hu else 0)
        if "raise" in available and score >= hu_raise_floor:
            amount = _raise_amount(table, allowed, strong=score >= premium_threshold)
            if amount is not None:
                return "raise", amount
        if "call" in available:
            call_floor = play_threshold + (10 if hu else 0)
            max_price = 0.10 if hu else 0.12
            if score >= call_floor or required <= max_price:
                return "call", call_amount
            if "check" in available:
                return "check", None
            if "fold" in available:
                return "fold", None
        return None

    # Open / blind complete spot
    if "raise" in available and score >= raise_threshold:
        amount = _raise_amount(table, allowed, strong=score >= premium_threshold)
        if amount is not None:
            return "raise", amount
    if "bet" in available and score >= bet_open_threshold:
        amount = _value_bet_amount(pot, allowed)
        return "bet", amount
    if hu:
        return None
    if "check" in available:
        return "check", None
    if "fold" in available:
        return "fold", None
    return None


def _hero_hole_cards(table: dict) -> list[str]:
    self_num = table.get("selfSeatNumber")
    for seat in table.get("seats") or []:
        if seat.get("seatNumber") == self_num:
            return list(seat.get("holeCards") or [])
    return []


def _hero_stack_chips(table: dict) -> int:
    self_num = table.get("selfSeatNumber")
    for seat in table.get("seats") or []:
        if seat.get("seatNumber") == self_num:
            return int(seat.get("stackChips") or 0)
    return 0


def _loose_call_max_price(position: str) -> float:
    if position in ("BTN", "CO"):
        return PREFLOP_LOOSE_CALL_MAX_PRICE_IP
    if position == "BB":
        return PREFLOP_LOOSE_CALL_MAX_PRICE_BB
    return PREFLOP_LOOSE_CALL_MAX_PRICE_OOP


def _preflop_defense_min_score(table: dict, position: str) -> int:
    if resolve_table_format(table) == "hu" and position == "BB":
        return HU_BB_DEFEND_MIN_SCORE
    return PREFLOP_DEFENSE_MIN_SCORE


def _preflop_defense_max_price(table: dict, position: str) -> float | None:
    max_price = PREFLOP_DEFENSE_MAX_PRICE.get(position)
    if max_price is None:
        return None
    if resolve_table_format(table) == "hu" and position == "BB":
        return 0.48
    return max_price


def try_preflop_loose_call(
    table: dict,
    allowed: dict,
    available: list[str],
    hole: list[str],
    position: str,
) -> Optional[ActionPair]:
    """Marginal score 38–49: call when pot odds within position cap (gin v008)."""
    call_amount = _call_chips(allowed)
    if call_amount <= 0 or "call" not in available:
        return None

    if resolve_table_format(table) == "hu" and position in ("SB", "BTN"):
        if is_preflop_open_spot(table, allowed, call_amount) and call_amount > 0:
            return None  # HU: no limp-complete — open or fold

    score = preflop_score(hole)
    if (
        score < PREFLOP_LOOSE_CALL_MIN_SCORE
        or score >= PREFLOP_LOOSE_CALL_SCORE_THRESHOLD
    ):
        return None

    if active_opponents(table) > PREFLOP_LOOSE_CALL_MAX_OPPONENTS:
        return None

    pot = int(table.get("potChips") or 0)
    required = pot_odds(call_amount, pot)
    max_price = _loose_call_max_price(position)
    if required > max_price:
        return None

    stack = _hero_stack_chips(table)
    if stack > 0 and call_amount > stack * PREFLOP_V008_MAX_STACK_FRACTION:
        return None

    return "call", call_amount


def try_preflop_blind_defense(
    table: dict,
    allowed: dict,
    available: list[str],
    hole: list[str],
    position: str,
) -> Optional[ActionPair]:
    """BB/SB defend wider vs full-ring fold threshold (gin v008 telemetry fix)."""
    max_price = _preflop_defense_max_price(table, position)
    if max_price is None:
        return None

    call_amount = _call_chips(allowed)
    if call_amount <= 0 or "call" not in available:
        return None

    score = preflop_score(hole)
    if score < _preflop_defense_min_score(table, position):
        return None

    pot = int(table.get("potChips") or 0)
    required = pot_odds(call_amount, pot)
    if required > max_price:
        return None

    stack = _hero_stack_chips(table)
    if stack > 0 and call_amount > stack * PREFLOP_DEFENSE_MAX_STACK_FRACTION:
        return None

    return "call", call_amount


def try_preflop_bb_defend_floor(
    table: dict,
    allowed: dict,
    available: list[str],
    hole: list[str],
    position: str,
) -> Optional[ActionPair]:
    """HU BB defend floor: widen calls vs small opens without touching BTN opens."""
    if resolve_table_format(table) != "hu" or position != "BB":
        return None
    return try_preflop_blind_defense(table, allowed, available, hole, position)


def try_preflop_sb_steal_floor(
    table: dict,
    allowed: dict,
    available: list[str],
    hole: list[str],
    position: str,
) -> Optional[ActionPair]:
    """HU SB/BTN first-in floor: open any hand that clears the steal score."""
    if resolve_table_format(table) != "hu":
        return None
    if position not in ("SB", "BTN"):
        return None
    if not is_preflop_open_spot(table, allowed, _call_chips(allowed)):
        return None
    if _hand_class(hole) in HU_SB_STEAL_TRIM:
        return None
    if preflop_score(hole) < HU_SB_STEAL_BET_OPEN:
        return None

    if "raise" in available:
        amount = _raise_amount(table, allowed)
        if amount is not None:
            return "raise", amount
    if "bet" in available:
        pot = int(table.get("potChips") or 0)
        return "bet", _value_bet_amount(pot, allowed)
    return None


def try_preflop_v008_rescue(
    table: dict,
    allowed: dict,
    available: list[str],
    hole: list[str],
    position: str,
    proposed_action: str,
    *,
    lane_tight: bool = False,
) -> Optional[ActionPair]:
    """Intercept chart/gin folds with gin v008 loose-call + blind-defense layers."""
    if not gin_v008_preflop_enabled() or lane_tight:
        return None
    if proposed_action != "fold":
        return None
    if not hole:
        hole = _hero_hole_cards(table)

    loose = try_preflop_loose_call(table, allowed, available, hole, position)
    if loose is not None:
        return loose
    return try_preflop_blind_defense(table, allowed, available, hole, position)


def try_postflop_free(
    table: dict,
    allowed: dict,
    available: list[str],
    hole: list[str],
    board: list[str],
) -> Optional[ActionPair]:
    """HU aggression when checked to (c-bet + value). None = defer to MC path."""
    if not gin_style_postflop_enabled():
        return None

    pot = int(table.get("potChips") or 0)
    opponents = active_opponents(table)
    made_rank = made_hand_rank(hole, board)
    top_pair = has_top_pair_or_better(hole, board)
    texture = board_texture(board) if board else {}
    strong_threshold = 2 if opponents <= 2 else 3
    strong = made_rank >= strong_threshold
    medium = made_rank == 1 or top_pair
    no_made = made_rank == 0

    if "bet" not in available:
        if "check" in available:
            return "check", None
        return None

    if strong:
        amount = _value_bet_amount(pot, allowed, strong=made_rank >= 3)
        return "bet", amount
    if medium and opponents <= 1 and _should_cbet(texture, opponents):
        amount = _value_bet_amount(pot, allowed)
        return "bet", amount
    if no_made and opponents <= 1 and _should_cbet(texture, opponents):
        amount = _pressure_amount(pot, allowed, 0.16)
        return "bet", amount
    if medium and opponents <= 2:
        amount = _value_bet_amount(pot, allowed)
        return "bet", amount
    if "check" in available:
        return "check", None
    return None
