"""TexasSolver blueprint v3 — per-hand-bucket free/facing-split policy (O(1) lookup).

Key: ``{street}|{line}|{role}|{texture}|{spr}|{node}|{hand_bucket}``

FREE nodes use ``node=free`` (check / bet_033 / bet_075 / allin).
FACING nodes use ``node=vs_small|vs_mid|vs_big|vs_over|vs_raise`` — never
mixed with free freqs in one vector.

Fail-open: when ``CEMINI_SOLVER_V3`` is off, file missing, key missing, or
``coverage_ok`` fails → caller falls back to soft-bias / heuristics.
"""
from __future__ import annotations

import json
import os
import secrets
from pathlib import Path
from typing import Any, Optional

HAND_BUCKETS = (
    "air",
    "weak_pair",
    "mid_pair",
    "tp_weak",
    "tp_good",
    "overpair",
    "two_pair_plus",
    "nutted",
    "draw_weak",
    "draw_strong",
    "combo_draw",
)

SPR_BINS = ("le2", "2to5", "gt5")
LINES = ("srp",)
STREETS = ("flop", "turn", "river")
ROLES = ("ip", "oop")
TEXTURES = ("dry", "wet", "paired")
FREE_NODES = ("free",)
FACING_NODES = ("vs_small", "vs_mid", "vs_big", "vs_over", "vs_raise")

FREE_ACTIONS = ("check", "bet_033", "bet_075", "allin")
FACING_ACTIONS = ("fold", "call", "raise_060", "allin")

_RANK_ORDER = "23456789TJQKA"
_RANK_VAL = {r: i for i, r in enumerate(_RANK_ORDER)}

_v3_cache: Optional[dict[str, Any]] = None
_v3_cache_path: Optional[Path] = None


def _env_truthy(name: str) -> bool:
    return os.environ.get(name, "").strip().lower() in ("1", "true", "yes", "on")


def blueprint_v3_enabled() -> bool:
    if not _env_truthy("CEMINI_SOLVER_V3"):
        return False
    return resolve_blueprint_v3_path() is not None


def resolve_blueprint_v3_path() -> Optional[Path]:
    override = os.environ.get("CEMINI_BLUEPRINT_V3_PATH", "").strip()
    if override:
        p = Path(override).expanduser()
        return p if p.is_file() else None
    module_dir = Path(__file__).resolve().parent
    for cand in (
        module_dir / "research" / "postflop_hu_buckets_v3.json",
        module_dir.parent / "assets" / "research" / "postflop_hu_buckets_v3.json",
        module_dir.parent / "research" / "postflop_hu_buckets_v3.json",
    ):
        if cand.is_file():
            return cand
    return None


def load_blueprint_v3(*, force: bool = False) -> Optional[dict[str, Any]]:
    global _v3_cache, _v3_cache_path
    path = resolve_blueprint_v3_path()
    if path is None:
        _v3_cache = None
        _v3_cache_path = None
        return None
    if not force and _v3_cache is not None and _v3_cache_path == path:
        return _v3_cache
    data = json.loads(path.read_text(encoding="utf-8"))
    _v3_cache = data
    _v3_cache_path = path
    return data


def spr_bin(effective_stack: float, pot: float) -> str:
    pot_f = max(float(pot), 1e-9)
    spr = max(0.0, float(effective_stack)) / pot_f
    if spr <= 2.0:
        return "le2"
    if spr <= 5.0:
        return "2to5"
    return "gt5"


def facing_node(
    call_chips: float,
    pot: float,
    *,
    vs_raise: bool = False,
) -> str:
    if vs_raise:
        return "vs_raise"
    pot_f = max(float(pot), 1e-9)
    ratio = max(0.0, float(call_chips)) / pot_f
    if ratio <= 0.33:
        return "vs_small"
    if ratio <= 0.55:
        return "vs_mid"
    if ratio <= 0.85:
        return "vs_big"
    return "vs_over"


def build_key(
    street: str,
    line: str,
    role: str,
    texture: str,
    spr: str,
    node: str,
    hand_bucket: str,
) -> str:
    return (
        f"{street.lower()}|{line.lower()}|{role.lower()}|{texture.lower()}"
        f"|{spr.lower()}|{node.lower()}|{hand_bucket.lower()}"
    )


def _board_cards(board: list[str]) -> list[str]:
    out: list[str] = []
    for c in board:
        c = (c or "").strip()
        if len(c) >= 2:
            out.append(c[0].upper() + c[-1].lower())
    return out


def _parse_hole(hole: list[str]) -> Optional[tuple[str, str]]:
    if len(hole) < 2:
        return None
    h0, h1 = hole[0].strip(), hole[1].strip()
    if len(h0) < 2 or len(h1) < 2:
        return None
    return h0[0].upper() + h0[-1].lower(), h1[0].upper() + h1[-1].lower()


def hand_bucket(hole: list[str], board: list[str]) -> str:
    """Map hero hole + board to v3 hand_bucket label (deterministic categories)."""
    parsed = _parse_hole(hole)
    b = _board_cards(board)
    if parsed is None or len(b) < 3:
        return "air"
    h0, h1 = parsed
    hr = [h0[0], h1[0]]
    hs = [h0[-1], h1[-1]]
    br = [c[0] for c in b]
    bs = [c[-1] for c in b]

    board_rank_counts: dict[str, int] = {}
    for r in br:
        board_rank_counts[r] = board_rank_counts.get(r, 0) + 1

    pocket = hr[0] == hr[1]
    board_max = max((_RANK_VAL.get(r, 0) for r in br), default=0)
    board_sorted = sorted((_RANK_VAL.get(r, 0) for r in br), reverse=True)

    # Nutted / two_pair_plus
    if pocket and hr[0] in board_rank_counts:
        if board_rank_counts.get(hr[0], 0) >= 2:
            return "nutted"
        return "two_pair_plus" if board_rank_counts.get(hr[0], 0) else "two_pair_plus"
    if pocket and board_rank_counts.get(hr[0], 0) >= 2:
        return "nutted"

    hits = [r for r in hr if r in board_rank_counts]
    if len(hits) == 2:
        return "two_pair_plus"
    if len(set(br)) < len(br) and len(hits) >= 1:
        if max(_RANK_VAL.get(r, 0) for r in hits) >= board_max - 1:
            return "two_pair_plus"

    # Flush / straight made
    suit_counts: dict[str, int] = {}
    for s in bs:
        suit_counts[s] = suit_counts.get(s, 0) + 1
    flush_draw = False
    flush_made = False
    for s in set(hs):
        total = suit_counts.get(s, 0) + hs.count(s)
        if total >= 5:
            flush_made = True
        elif total == 4 and len(b) < 5:
            flush_draw = True

    all_ranks = sorted({_RANK_VAL[r] for r in hr + br if r in _RANK_VAL})
    straight_made = False
    oesd = False
    gutshot = False
    if len(all_ranks) >= 5:
        for i in range(len(all_ranks) - 4):
            window = all_ranks[i : i + 5]
            if window[-1] - window[0] == 4:
                straight_made = True
                break
    if not straight_made and len(b) < 5:
        board_vals = sorted({_RANK_VAL[r] for r in br if r in _RANK_VAL})
        hero_vals = sorted({_RANK_VAL[r] for r in hr if r in _RANK_VAL})
        connected = (
            len(board_vals) >= 2 and board_vals[-1] - board_vals[0] <= 4
        )
        if connected and hero_vals and abs(hero_vals[-1] - hero_vals[0]) <= 4:
            oesd = True
        elif connected:
            gutshot = True

    if straight_made or flush_made:
        return "nutted"

    if pocket:
        pv = _RANK_VAL.get(hr[0], 0)
        if pv > board_max:
            return "overpair"
        if pv >= board_max - 2:
            return "mid_pair"
        return "weak_pair"

    if len(hits) == 1:
        hit_v = _RANK_VAL.get(hits[0], 0)
        if board_sorted and hit_v >= board_sorted[0]:
            kicker = max(
                _RANK_VAL.get(r, 0) for r in hr if r != hits[0]
            )
            if kicker >= _RANK_VAL.get("T", 8):
                return "tp_good"
            return "tp_weak"
        if board_sorted and len(board_sorted) > 1 and hit_v >= board_sorted[1]:
            return "mid_pair"
        return "weak_pair"

    if flush_draw and oesd:
        return "combo_draw"
    if flush_draw or oesd:
        return "draw_strong"
    if gutshot:
        return "draw_weak"

    overs = sum(1 for r in hr if _RANK_VAL.get(r, 0) > board_max)
    if overs >= 1:
        return "draw_weak"
    return "air"


def lookup_policy(key: str, payload: Optional[dict[str, Any]] = None) -> Optional[dict[str, Any]]:
    data = payload if payload is not None else load_blueprint_v3()
    if not data:
        return None
    buckets = data.get("buckets") or {}
    entry = buckets.get(key)
    if isinstance(entry, dict):
        return entry
    return None


def coverage_ok(
    entry: Optional[dict[str, Any]],
    *,
    weight_min: float = 0.005,
    combos_min: int = 20,
    smoke: bool = False,
) -> bool:
    if not entry or not isinstance(entry, dict):
        return False
    freqs = entry.get("freqs") or entry
    if not isinstance(freqs, dict):
        return False
    w = float(entry.get("weight", entry.get("mass", 1.0)) or 0.0)
    combos = int(entry.get("combos", entry.get("combo_count", 0)) or 0)
    min_combos = 5 if smoke else combos_min
    if w < weight_min or combos < min_combos:
        return False
    total = sum(float(freqs.get(k, 0.0) or 0.0) for k in _action_keys_for_entry(entry))
    return total > 1e-9


def _action_keys_for_entry(entry: dict[str, Any]) -> tuple[str, ...]:
    node = str(entry.get("node") or "")
    if node == "free" or node in FREE_NODES:
        return FREE_ACTIONS
    if node.startswith("vs_"):
        return FACING_ACTIONS
    freqs = entry.get("freqs") or entry
    if any(k in freqs for k in FREE_ACTIONS):
        return FREE_ACTIONS
    return FACING_ACTIONS


def sample_action_v3(
    entry: dict[str, Any],
    available: list[str],
    *,
    facing: bool,
    pot: int,
    call_chips: int,
    rng: Any,
    allowed: Optional[dict[str, Any]] = None,
) -> Optional[tuple[str, Optional[int]]]:
    """Sample legal Arena action from v3 freqs. Returns (action, amount|None)."""
    if not entry or not available:
        return None
    freqs = entry.get("freqs") if isinstance(entry.get("freqs"), dict) else entry
    if not isinstance(freqs, dict):
        return None
    avail = {str(a).lower() for a in available}
    allowed = allowed or {}
    action_keys = FACING_ACTIONS if facing else FREE_ACTIONS

    weights: list[tuple[str, float]] = []
    for ak in action_keys:
        w = float(freqs.get(ak, 0.0) or 0.0)
        if w <= 0:
            continue
        if ak == "check" and "check" in avail:
            weights.append(("check", w))
        elif ak == "fold" and "fold" in avail:
            weights.append(("fold", w))
        elif ak == "call" and "call" in avail:
            weights.append(("call", w))
        elif ak in ("bet_033", "bet_075", "allin"):
            if "bet" in avail:
                weights.append((ak, w))
            elif "raise" in avail:
                weights.append((ak.replace("bet_", "raise_"), w))
            elif "all-in" in avail or "allin" in avail:
                weights.append(("allin", w))
        elif ak in ("raise_060", "allin"):
            if "raise" in avail:
                weights.append((ak, w))
            elif "bet" in avail:
                weights.append((ak.replace("raise_", "bet_"), w))
            elif "all-in" in avail:
                weights.append(("all-in", w))

    if not weights:
        # Drop illegal: if single passive action remains, fail-open to it.
        if not facing and "check" in avail:
            return "check", None
        if facing and "fold" in avail and "call" not in avail:
            return "fold", None
        return None
    total = sum(w for _, w in weights)
    if total <= 1e-12:
        return None
    pick = float(rng.random()) * total
    acc = 0.0
    chosen = weights[-1][0]
    for action, w in weights:
        acc += w
        if pick <= acc:
            chosen = action
            break

    if chosen in ("check", "fold", "call"):
        return chosen, None

    pot_i = max(int(pot), 1)
    if chosen in ("bet_033", "raise_033"):
        frac = 0.33
        arena = "bet" if "bet" in avail else "raise"
    elif chosen in ("bet_075", "raise_075"):
        frac = 0.75
        arena = "bet" if "bet" in avail else "raise"
    elif chosen in ("raise_060",):
        frac = 0.60
        arena = "raise" if "raise" in avail else "bet"
    elif chosen in ("allin", "all-in"):
        br = allowed.get("betRange") or allowed.get("raiseRange") or {}
        max_amt = int(br.get("max") or 0)
        if max_amt > 0:
            arena = "raise" if "raise" in avail else ("bet" if "bet" in avail else "all-in")
            return arena, max_amt
        frac = 1.0
        arena = "raise" if "raise" in avail else "bet"
    else:
        frac = 0.50
        arena = "bet" if "bet" in avail else "raise"

    if facing:
        rr = allowed.get("raiseRange") or allowed.get("betRange") or {}
        min_r = int(rr.get("min") or max(call_chips * 2, int(pot_i * frac), 1))
        max_r = int(rr.get("max") or min_r)
        target = max(min_r, min(int(pot_i * frac) + int(call_chips), max_r))
    else:
        br = allowed.get("betRange") or allowed.get("raiseRange") or {}
        min_b = int(br.get("min") or max(int(pot_i * frac), 1))
        max_b = int(br.get("max") or min_b)
        target = max(min_b, min(int(pot_i * frac), max_b))
    if arena not in avail and "all-in" in avail:
        arena = "all-in"
    if arena not in avail:
        return None
    return arena, target


def classify_board_texture(board: list[str]) -> str:
    from postflop_buckets import classify_board_texture as _classify

    return _classify(board)


def lookup_policy_for_table(
    table: dict,
    hole: list[str],
    board: list[str],
    *,
    in_position: bool,
    facing: bool,
    call_chips: int,
    pot: int,
    effective_stack: Optional[float] = None,
    line: str = "srp",
    vs_raise: bool = False,
    smoke: bool = False,
) -> Optional[dict[str, Any]]:
    street = (table.get("street") or "Preflop").lower()
    if street == "preflop":
        return None
    if street not in STREETS:
        n = len(board)
        if n >= 5:
            street = "river"
        elif n == 4:
            street = "turn"
        elif n >= 3:
            street = "flop"
        else:
            return None
    texture = classify_board_texture(board)
    role = "ip" if in_position else "oop"
    if effective_stack is None:
        seats = table.get("seats") or []
        hero = next((s for s in seats if s.get("isHero")), None)
        effective_stack = float((hero or {}).get("stackChips") or 100)
    spr = spr_bin(float(effective_stack), float(pot))
    hb = hand_bucket(hole, board)
    node = facing_node(call_chips, pot, vs_raise=vs_raise) if facing else "free"
    key = build_key(street, line, role, texture, spr, node, hb)
    entry = lookup_policy(key)
    if entry and coverage_ok(entry, smoke=smoke):
        return {**entry, "node": node, "key": key}
    return None
