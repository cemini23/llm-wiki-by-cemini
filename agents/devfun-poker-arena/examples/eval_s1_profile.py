"""Eval S1 (`seed_poker_eval_s1`) 6-max panel-exploit profile.

Arena now requires static-agent submit for Eval (403 sandbox_submission_required).
Top board styles are maniac / calling-station — not HU blueprint nits.

Activate via:
  - env ``CEMINI_ARENA_PROFILE=eval_s1`` (or ``eval`` / ``eval_panel``)
  - or file ``harness/arena_profile`` containing that token (baked into zip)

When active, harness setdefaults flip to 6-max + exploit stack and
``cemini_decide`` applies value-heavy / light-call-down margins vs panel.
"""
from __future__ import annotations

import os
from pathlib import Path
from typing import Any

EVAL_COMPETITION_IDS = frozenset(
    {
        "seed_poker_eval_s1",
        # public quick / definitive seasons (same PVE panel family)
        "cmpdk0pt00eawvcaf1es8plw2",
        "cmpkdus9200syw8do5644oymp",
    }
)

_PROFILE_ALIASES = frozenset({"eval_s1", "eval", "eval_panel", "poker_eval"})

# Panel seats observed on Eval recent-tables (6-max).
PANEL_AGENT_IDS = frozenset(
    {
        "devfun_arena_poker_bot_1",
        "devfun_arena_poker_bot_2",
        "devfun_arena_poker_bot_3",
        "devfun_arena_poker_bot_4",
        "devfun_arena_poker_bot_5",
    }
)

# Value-print vs stations; light call-down vs maniac — not lane_tight eval_panel_mode.
# v2 (after +39 @ VPIP18 ranked #1331): widen harder — tops print at VPIP 80%+ / AF≫1.
_EVAL_EXPLOIT_MARGINS: dict[str, float] = {
    "bet_bar_delta": -0.10,
    "call_margin_delta": -0.10,
    "fold_slack_delta": -0.08,
    "preflop_fold_margin_delta": -0.10,
    "open_steal_equity": 0.18,
}


def _read_profile_file() -> str:
    # harness/ next to strategy.py in bundle; examples/ sibling for local runs
    here = Path(__file__).resolve()
    candidates = [
        here.parent.parent / "harness" / "arena_profile",
        Path.cwd() / "harness" / "arena_profile",
        here.parent / "arena_profile",
    ]
    for path in candidates:
        try:
            if path.is_file():
                return path.read_text(encoding="utf-8").strip().lower()
        except OSError:
            continue
    return ""


def resolve_arena_profile() -> str:
    env = os.environ.get("CEMINI_ARENA_PROFILE", "").strip().lower()
    if env:
        return env
    return _read_profile_file()


def eval_s1_profile_active() -> bool:
    return resolve_arena_profile() in _PROFILE_ALIASES


def competition_is_eval(competition_id: str | None) -> bool:
    return (competition_id or "").strip() in EVAL_COMPETITION_IDS


def apply_eval_s1_env_defaults() -> None:
    """Force Eval exploit posture (overrides HU researcher setdefaults)."""
    os.environ["CEMINI_ARENA_PROFILE"] = "eval_s1"
    os.environ["CEMINI_TABLE_FORMAT"] = "6max"
    os.environ["CEMINI_RESEARCHER_MODE"] = "0"
    os.environ["CEMINI_SOLVER_V3"] = "0"
    os.environ["CEMINI_SOLVER_HARD"] = "0"
    os.environ["CEMINI_EVAL_PANEL_MODE"] = "0"
    os.environ["CEMINI_EVAL_CRUSH"] = "1"
    os.environ["CEMINI_ISO_PASSIVE_LP"] = "1"
    os.environ["CEMINI_S1B_EXPLOIT"] = "1"
    os.environ["CEMINI_GIN_V2_EXPLOITS"] = "1"
    os.environ["CEMINI_GIN_STYLE"] = "1"
    os.environ["CEMINI_GIN_STYLE_PREFLOP"] = "1"
    os.environ["CEMINI_GIN_STYLE_POSTFLOP"] = "1"
    # Wider gin floors (S2 gate path) — needed for panel crush VPIP.
    os.environ["CEMINI_GIN_STYLE_GATE"] = "1"
    os.environ["CEMINI_NEMESIS_EXPLOIT"] = "1"
    os.environ["CEMINI_NEMESIS_WIDE_PASSIVE"] = "1"
    os.environ["CEMINI_NEMESIS_LINEAR_AGGRO"] = "1"
    os.environ["CEMINI_OPPONENT_MODES"] = "1"
    os.environ["CEMINI_MAFP_CHART"] = "1"
    os.environ["CEMINI_POSTFLOP_BUCKETS"] = "1"
    os.environ.setdefault("CEMINI_MANIAC_CALL_MARGIN_DELTA", "-0.12")
    # Seed panel IDs as named nemeses (wide_passive default).
    existing = os.environ.get("CEMINI_NEMESIS_HANDLES", "").strip()
    panel = ",".join(sorted(PANEL_AGENT_IDS))
    if existing:
        os.environ["CEMINI_NEMESIS_HANDLES"] = f"{existing},{panel}"
    else:
        os.environ["CEMINI_NEMESIS_HANDLES"] = panel


def eval_crush_enabled() -> bool:
    if not eval_s1_profile_active():
        return False
    return os.environ.get("CEMINI_EVAL_CRUSH", "1").strip().lower() in (
        "1",
        "true",
        "yes",
        "on",
    )


def _crush_preflop_score(hole: list[str]) -> int:
    """Lightweight gin-like score (avoid circular import)."""
    ranks = "23456789TJQKA"
    cards = []
    for c in hole or []:
        s = (c or "").strip()
        if s.startswith("[") and s.endswith("]"):
            s = s[1:-1]
        if len(s) >= 2 and s[0].upper() in ranks:
            cards.append(s[0].upper() + s[-1].lower())
    if len(cards) != 2:
        return 0
    r1, s1 = cards[0][0], cards[0][1]
    r2, s2 = cards[1][0], cards[1][1]
    v1, v2 = ranks.index(r1) + 2, ranks.index(r2) + 2
    high, low = max(v1, v2), min(v1, v2)
    score = high * 3 + low
    if v1 == v2:
        score += 34 + high * 2
    if s1 == s2:
        score += 8
    if abs(v1 - v2) == 1:
        score += 5
    if high >= 12 and low >= 10:
        score += 12
    return score


def try_eval_panel_crush(
    table: dict[str, Any],
    allowed: dict[str, Any],
    available: list[str],
    hole: list[str],
    board: list[str],
    street: str,
    pot: int,
    call_chips: int,
) -> tuple[str, int | None] | None:
    """Maniac/station hybrid vs soft Eval panel (top LB is VPIP 80%+).

    Returns ``(action, amount)`` or None to fall through.
    """
    if not eval_crush_enabled():
        return None
    avail = [str(a).lower() for a in (available or [])]
    score = _crush_preflop_score(hole)
    st = (street or "Preflop").strip().lower()

    def _raise_to(strong: bool = False) -> int | None:
        rr = allowed.get("raiseRange") or allowed.get("betRange") or {}
        mn = int(rr.get("min") or 0)
        mx = int(rr.get("max") or mn)
        if mn <= 0:
            return None
        if strong:
            return max(mn, min(mx, int(pot * 1.0 + call_chips * 2) or mn))
        return max(mn, min(mx, mn))

    # ── Preflop ──────────────────────────────────────────────────────────
    if st.startswith("pre"):
        can_raise = "raise" in avail and bool(allowed.get("canRaise") or allowed.get("canBet"))
        can_bet = "bet" in avail and bool(allowed.get("canBet"))
        can_call = "call" in avail and bool(allowed.get("canCall") or call_chips > 0)
        can_check = "check" in avail and bool(allowed.get("canCheck"))
        can_fold = "fold" in avail

        open_spot = call_chips <= 0 and (can_raise or can_bet or can_check)
        if open_spot:
            # Steal / open extremely wide — tops print at ~80–95% VPIP.
            if score >= 18 and (can_raise or can_bet):
                act = "raise" if can_raise else "bet"
                return act, _raise_to(strong=score >= 60)
            if can_check:
                return "check", None
            if can_fold:
                return "fold", None
            return None

        price = float(call_chips) / float(max(pot, 1))
        if score >= 55 and can_raise:
            return "raise", _raise_to(strong=True)
        if can_call and (score >= 12 or price <= 0.70):
            return "call", None
        if can_check:
            return "check", None
        if can_fold:
            return "fold", None
        return None

    # ── Postflop ─────────────────────────────────────────────────────────
    can_bet = "bet" in avail and bool(allowed.get("canBet"))
    can_raise = "raise" in avail and bool(allowed.get("canRaise"))
    can_call = "call" in avail
    can_check = "check" in avail and bool(allowed.get("canCheck"))
    can_fold = "fold" in avail
    price = float(call_chips) / float(max(pot + call_chips, 1))

    board_ranks = {(c[0].upper() if c else "") for c in (board or []) if c}
    hole_ranks = {(c[0].upper() if c else "") for c in (hole or []) if c}
    paired = bool(hole_ranks & board_ranks)
    overcard = any(r in "AKQJT" for r in hole_ranks)

    if (paired or overcard or score >= 40) and (can_bet or can_raise):
        if can_raise and call_chips > 0:
            return "raise", _raise_to(strong=paired or score >= 55)
        if can_bet:
            return "bet", _raise_to(strong=paired)
    if can_call and (paired or overcard or price <= 0.55 or score >= 30):
        return "call", None
    if can_check:
        return "check", None
    if can_bet:
        return "bet", _raise_to(strong=False)
    if can_fold and price > 0.80 and not paired and score < 25:
        return "fold", None
    if can_call:
        return "call", None
    if can_fold:
        return "fold", None
    return None



def eval_exploit_margins() -> dict[str, float]:
    """Base margins when Eval profile is active (cold-start panel)."""
    out = dict(_EVAL_EXPLOIT_MARGINS)
    try:
        delta = float(os.environ.get("CEMINI_MANIAC_CALL_MARGIN_DELTA", "-0.07"))
    except ValueError:
        delta = -0.07
    # Extra call-down vs aggression; stacked with call_margin_delta above.
    out["call_margin_delta"] = float(out["call_margin_delta"]) + delta
    return out


def table_has_eval_panel(table: dict[str, Any]) -> bool:
    for seat in table.get("seats") or []:
        aid = str(seat.get("agentId") or "").strip().lower()
        if aid in PANEL_AGENT_IDS:
            return True
        handle = str(seat.get("agentHandle") or seat.get("agentName") or "").lower()
        if handle.startswith("devfun_arena_poker_bot"):
            return True
    return False
