#!/usr/bin/env python3
"""Offline bake: TexasSolver console dumps → research/postflop_hu_buckets.json.

NOT used at decide() runtime. Aggregates root OOP + CHECK-child IP (+ facing
BET-child IP) strategies into ``{street}|{role}|{texture}|{strength_bin}``.

Pre-install / supply-chain: see ``references/preinstall-gate.md`` (pin versions,
allowlist registries, prebind before solver/binary deps).

Strength bin choice
-------------------
Cheap **hand-category equity heuristic** vs board (pair / set / two-pair /
flush-draw / straight-draw / overcards / air), mapped through
``postflop_buckets.strength_bin``. Deterministic, no treys dependency, fast
enough for full-grid aggregation. Documented here so audits do not mistake
it for solver-internal EV.

Solver binary (never bundled):
  CEMINI_TEXASSOLVER_BIN or
  .local/texassolver/TexasSolver-v0.2.0-MacOs/console_solver

Caches dumps under ``.local/texassolver/dumps/`` (gitignored).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import secrets
import subprocess
import sys
import time
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Any, Optional

# examples/ on path
_EXAMPLES = Path(__file__).resolve().parent
_ROOT = _EXAMPLES.parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from postflop_buckets import (  # noqa: E402
    STREETS,
    ROLES,
    TEXTURES,
    STRENGTH_BINS,
    _FREQ_KEYS,
    _heuristic_freqs,
    _normalize_freqs,
    bucket_key,
    strength_bin,
)

DEFAULT_BIN = (
    _ROOT
    / ".local"
    / "texassolver"
    / "TexasSolver-v0.2.0-MacOs"
    / "console_solver"
)
DEFAULT_GRID = _ROOT / "research" / "texassolver_spot_grid.json"
DEFAULT_OUT = _ROOT / "research" / "postflop_hu_buckets.json"
# Prefer space-free dump dir: TexasSolver mishandles paths with spaces
# (workspace lives under "OSINT WORKSPACE"). Repo .local is a secondary copy.
DEFAULT_DUMP_DIR = Path("/tmp/cemini-texassolver-dumps")
REPO_DUMP_DIR = _ROOT / ".local" / "texassolver" / "dumps"

MIN_SUCCESSFUL_FLOP = 12
_ACTION_RE = re.compile(
    r"^(CHECK|CALL|FOLD|BET|RAISE|ALLIN|DONK)(?:\s+([0-9.]+))?$",
    re.IGNORECASE,
)

_RANK_ORDER = "23456789TJQKA"
_RANK_VAL = {r: i for i, r in enumerate(_RANK_ORDER)}


# ---------------------------------------------------------------------------
# Paths / solver
# ---------------------------------------------------------------------------

def resolve_solver_bin() -> Path:
    env = os.environ.get("CEMINI_TEXASSOLVER_BIN", "").strip()
    if env:
        p = Path(env).expanduser().resolve()
        if not p.is_file():
            raise FileNotFoundError(f"CEMINI_TEXASSOLVER_BIN not a file: {p}")
        return p
    p = DEFAULT_BIN.resolve()
    if not p.is_file():
        raise FileNotFoundError(
            f"TexasSolver binary missing: {p}\n"
            "Set CEMINI_TEXASSOLVER_BIN or install under .local/texassolver/."
        )
    return p


def _log(msg: str) -> None:
    print(f"[bake-texassolver] {msg}", flush=True)


# ---------------------------------------------------------------------------
# Strength bin — hand-category equity heuristic (documented choice)
# ---------------------------------------------------------------------------

def parse_hand_combo(combo: str) -> Optional[tuple[str, str]]:
    """TexasSolver hand key 'AhKd' → ('Ah', 'Kd')."""
    s = (combo or "").strip()
    if len(s) != 4:
        return None
    c1, c2 = s[:2], s[2:]
    if c1[0].upper() not in _RANK_VAL or c2[0].upper() not in _RANK_VAL:
        return None
    return c1[0].upper() + c1[1].lower(), c2[0].upper() + c2[1].lower()


def _board_cards(board: list[str]) -> list[str]:
    out = []
    for c in board:
        c = c.strip()
        if not c:
            continue
        if len(c) >= 2:
            out.append(c[0].upper() + c[-1].lower())
    return out


def estimate_equity_category(hole: list[str], board: list[str]) -> float:
    """Deterministic coarse equity in [0,1] from hand-vs-board categories.

    Used only for strength_bin bucketing during bake — not for decide().
    """
    if len(hole) < 2:
        return 0.40
    h0, h1 = hole[0], hole[1]
    hr = [h0[0].upper(), h1[0].upper()]
    hs = [h0[-1].lower(), h1[-1].lower()]
    br = [c[0].upper() for c in board if c]
    bs = [c[-1].lower() for c in board if c]
    board_rank_counts: dict[str, int] = {}
    for r in br:
        board_rank_counts[r] = board_rank_counts.get(r, 0) + 1

    # Made hand strength
    pair_board = 0
    for r in hr:
        if r in board_rank_counts:
            pair_board += board_rank_counts[r]
    pocket = hr[0] == hr[1]
    trips_or_better = False
    two_pair = False
    one_pair = False
    set_like = False

    if pocket:
        if hr[0] in board_rank_counts:
            # set or quads
            set_like = True
            trips_or_better = True
        else:
            # underpair / overpair / mid pair
            board_max = max((_RANK_VAL.get(r, 0) for r in br), default=0)
            pocket_v = _RANK_VAL.get(hr[0], 0)
            if pocket_v > board_max:
                one_pair = True
                eq_pair = 0.72  # overpair-ish
            elif pocket_v >= board_max - 2:
                one_pair = True
                eq_pair = 0.58
            else:
                one_pair = True
                eq_pair = 0.48
    else:
        hits = [r for r in hr if r in board_rank_counts]
        if len(hits) == 2:
            two_pair = True
        elif len(hits) == 1:
            one_pair = True
            # top pair vs bottom
            hit_v = _RANK_VAL.get(hits[0], 0)
            board_sorted = sorted((_RANK_VAL.get(r, 0) for r in br), reverse=True)
            if board_sorted and hit_v >= board_sorted[0]:
                eq_pair = 0.68  # top pair
            elif board_sorted and hit_v >= (board_sorted[1] if len(board_sorted) > 1 else 0):
                eq_pair = 0.58
            else:
                eq_pair = 0.48

    # Full house / quads rough
    if set_like and any(board_rank_counts.get(r, 0) >= 2 for r in br):
        return 0.95
    if trips_or_better and two_pair:
        return 0.92
    if set_like:
        return 0.88
    if two_pair:
        return 0.78

    # Flush / straight draws
    suit_counts: dict[str, int] = {}
    for s in bs:
        suit_counts[s] = suit_counts.get(s, 0) + 1
    flush_draw = False
    flush_made = False
    for s in set(hs):
        total = suit_counts.get(s, 0) + hs.count(s)
        if total >= 5:
            flush_made = True
        elif total == 4 and len(board) < 5:
            flush_draw = True

    if flush_made:
        return 0.90

    # Straight made / OESD / gutshot (coarse)
    all_ranks = sorted({_RANK_VAL[r] for r in hr + br if r in _RANK_VAL})
    straight_made = False
    oesd = False
    gutshot = False
    if len(all_ranks) >= 5:
        for i in range(len(all_ranks) - 4):
            window = all_ranks[i : i + 5]
            if window[-1] - window[0] == 4 and len(window) == 5:
                straight_made = True
                break
    if not straight_made and len(board) < 5:
        hero_vals = sorted({_RANK_VAL[r] for r in hr if r in _RANK_VAL})
        # rough: connected board + hero glue
        board_vals = sorted({_RANK_VAL[r] for r in br if r in _RANK_VAL})
        connected = False
        if len(board_vals) >= 2 and board_vals[-1] - board_vals[0] <= 4:
            connected = True
        if connected and abs(hero_vals[-1] - hero_vals[0]) <= 4:
            oesd = True
        elif connected:
            gutshot = True

    if straight_made:
        return 0.88

    if one_pair:
        base = eq_pair  # type: ignore[name-defined]
        if flush_draw:
            base = min(0.84, base + 0.10)
        if oesd:
            base = min(0.84, base + 0.08)
        elif gutshot:
            base = min(0.80, base + 0.04)
        return base

    # Air / draws only / overcards
    overs = 0
    board_max = max((_RANK_VAL.get(r, 0) for r in br), default=0)
    for r in hr:
        if _RANK_VAL.get(r, 0) > board_max:
            overs += 1
    if flush_draw and oesd:
        return 0.52
    if flush_draw:
        return 0.42
    if oesd:
        return 0.38
    if gutshot and overs:
        return 0.36
    if overs == 2:
        return 0.34
    if overs == 1:
        return 0.30
    return 0.22


def strength_bin_for_combo(combo: str, board: list[str]) -> str:
    parsed = parse_hand_combo(combo)
    if parsed is None:
        return "medium"
    hole = list(parsed)
    eq = estimate_equity_category(hole, _board_cards(board))
    return strength_bin(eq)


# ---------------------------------------------------------------------------
# Action parsing + tree walk
# ---------------------------------------------------------------------------

def classify_action(label: str) -> tuple[str, Optional[float]]:
    """Map solver action string → (freq_key, size_chips_or_None)."""
    s = (label or "").strip()
    m = _ACTION_RE.match(s)
    if not m:
        up = s.upper()
        if "ALLIN" in up or "ALL-IN" in up:
            return "raise", None
        return "check", None
    kind = m.group(1).upper()
    amt = float(m.group(2)) if m.group(2) else None
    if kind == "CHECK":
        return "check", None
    if kind == "CALL":
        return "call", None
    if kind == "FOLD":
        return "fold", None
    if kind in ("BET", "DONK"):
        return "bet", amt
    if kind in ("RAISE", "ALLIN"):
        return "raise", amt
    return "check", None


def player_to_role(player: Any) -> str:
    """TexasSolver root player 1 is typically OOP; player 0 is IP."""
    try:
        p = int(player)
    except (TypeError, ValueError):
        return "oop"
    return "oop" if p == 1 else "ip"


def _iter_strategy_hands(node: dict) -> tuple[list[str], dict[str, list[float]]]:
    strat = node.get("strategy") or {}
    actions = list(strat.get("actions") or node.get("actions") or [])
    hands = strat.get("strategy") or {}
    if not isinstance(hands, dict):
        return actions, {}
    return actions, hands  # type: ignore[return-value]


def extract_decision_nodes(root: dict) -> list[tuple[str, dict]]:
    """Collect (role, node) for free + facing decisions at dump depth.

    - Root: OOP free (player 1)
    - CHECK child: IP free
    - BET/DONK/RAISE child of root: IP facing
    - CHECK → BET path: OOP facing (when present under dump_rounds ≥ 2)
    """
    out: list[tuple[str, dict]] = []
    if not isinstance(root, dict):
        return out
    if root.get("node_type") == "action_node" or root.get("strategy"):
        role = player_to_role(root.get("player", 1))
        out.append((role, root))

    children = root.get("childrens") or root.get("children") or {}
    if not isinstance(children, dict):
        return out

    for label, child in children.items():
        if not isinstance(child, dict):
            continue
        if child.get("node_type") == "chance_node":
            continue
        act_key, _ = classify_action(str(label))
        role = player_to_role(child.get("player", 0))
        if child.get("strategy") or child.get("node_type") == "action_node":
            out.append((role, child))

        # One level deeper: after IP bet, OOP faces
        grand = child.get("childrens") or child.get("children") or {}
        if not isinstance(grand, dict):
            continue
        for glabel, gchild in grand.items():
            if not isinstance(gchild, dict):
                continue
            if gchild.get("node_type") == "chance_node":
                continue
            if not (gchild.get("strategy") or gchild.get("node_type") == "action_node"):
                continue
            # Only take facing nodes (not pure chance chains)
            g_act, _ = classify_action(str(glabel))
            if g_act in ("bet", "raise") or act_key == "check":
                grole = player_to_role(gchild.get("player", 1))
                # Prefer nodes that actually have fold/call/raise
                g_actions, _ = _iter_strategy_hands(gchild)
                keys = {classify_action(a)[0] for a in g_actions}
                if keys & {"fold", "call", "raise"} or g_act in ("bet", "raise", "check"):
                    out.append((grole, gchild))
    return out


def accumulate_node(
    acc: dict[str, dict[str, float]],
    size_acc: dict[str, list[tuple[float, float]]],
    *,
    street: str,
    role: str,
    texture: str,
    board: list[str],
    node: dict,
    pot: float,
) -> int:
    """Add strategy mass into free/facing accumulators. Returns hand count."""
    actions, hands = _iter_strategy_hands(node)
    if not actions or not hands:
        return 0
    mapped = [classify_action(a) for a in actions]
    n = 0
    for combo, probs in hands.items():
        if not isinstance(probs, (list, tuple)):
            continue
        sbin = strength_bin_for_combo(str(combo), board)
        key = bucket_key(street, role, texture, sbin)
        bucket = acc.setdefault(
            key,
            {k: 0.0 for k in _FREQ_KEYS},
        )
        weight = 1.0  # solver already restricts to range; equal combo weight
        for i, (freq_key, size) in enumerate(mapped):
            if i >= len(probs):
                break
            p = float(probs[i]) * weight
            if p <= 0:
                continue
            if freq_key in bucket:
                bucket[freq_key] += p
            if freq_key in ("bet", "raise") and size is not None and pot > 0:
                frac = float(size) / float(pot)
                # Skip shove / all-in sizes for sizing hint (BET 100 on pot 20 → 5.0).
                # Keep standard open/c-bet fractions only.
                if 0.20 <= frac <= 0.90:
                    size_acc.setdefault(key, []).append((p, frac))
        n += 1
    return n


# ---------------------------------------------------------------------------
# Input file + run solver
# ---------------------------------------------------------------------------

def _bet_sizes_for_street(bet_sizes: list[str], street: str) -> list[str]:
    """Keep only bet-size lines for the spot street (flop-only trees for flop).

    Full flop→turn→river trees with wide HU ranges hang / OOM on laptop.
    dump_rounds=1 only needs the current street's root decisions anyway.
    """
    st = street.lower().strip()
    filtered = []
    for bs in bet_sizes:
        parts = [p.strip() for p in str(bs).split(",")]
        if len(parts) >= 2 and parts[1].lower() == st:
            filtered.append(bs)
    return filtered or list(bet_sizes)


def build_input_text(
    spot: dict,
    defaults: dict,
    dump_path: Path,
    *,
    thread_num: Optional[int] = None,
    use_isomorphism: Optional[int] = None,
) -> str:
    pot = spot.get("pot", defaults.get("pot", 20))
    stack = spot.get("effective_stack", defaults.get("effective_stack", 100))
    board = spot["board"]
    if isinstance(board, list):
        board_s = ",".join(board)
    else:
        board_s = str(board)
    range_ip = spot.get("range_ip", defaults["range_ip"])
    range_oop = spot.get("range_oop", defaults["range_oop"])
    street = str(spot.get("street") or "flop").lower()
    bet_sizes = _bet_sizes_for_street(
        list(spot.get("bet_sizes", defaults.get("bet_sizes") or [])),
        street,
    )
    accuracy = spot.get("accuracy", defaults.get("accuracy", 1.0))
    max_iter = spot.get("max_iteration", defaults.get("max_iteration", 120))
    dump_rounds = spot.get("dump_rounds", defaults.get("dump_rounds", 1))
    # Default 2 threads + iso off: TexasSolver v0.2.0 abort (exit 134) on
    # some boards with thread_num≥8 + use_isomorphism=1 (e.g. Kd,8c,2h).
    if thread_num is None:
        thread_num = int(spot.get("thread_num", defaults.get("thread_num", 2)))
    thread_num = max(1, min(int(thread_num), os.cpu_count() or 2))
    if use_isomorphism is None:
        use_isomorphism = int(
            spot.get("use_isomorphism", defaults.get("use_isomorphism", 0))
        )
    allin = spot.get("allin_threshold", defaults.get("allin_threshold", 0.67))

    # Absolute path MUST be space-free for TexasSolver dump_result.
    dump_abs = dump_path.resolve()
    if " " in str(dump_abs):
        raise ValueError(
            f"dump path has spaces (TexasSolver will hang): {dump_abs}"
        )

    lines = [
        f"set_pot {pot}",
        f"set_effective_stack {stack}",
        f"set_board {board_s}",
        f"set_range_ip {range_ip}",
        f"set_range_oop {range_oop}",
    ]
    for bs in bet_sizes:
        lines.append(f"set_bet_sizes {bs}")
    lines += [
        f"set_allin_threshold {allin}",
        "build_tree",
        f"set_thread_num {thread_num}",
        f"set_accuracy {accuracy}",
        f"set_max_iteration {max_iter}",
        "set_print_interval 40",
        f"set_use_isomorphism {int(use_isomorphism)}",
        "start_solve",
        f"set_dump_rounds {dump_rounds}",
        f"dump_result {dump_abs}",
    ]
    return "\n".join(lines) + "\n"


def spot_cache_key(spot: dict, defaults: dict) -> str:
    street = str(spot.get("street") or "flop").lower()
    raw_sizes = list(spot.get("bet_sizes", defaults.get("bet_sizes") or []))
    payload = {
        "id": spot.get("id"),
        "board": spot.get("board"),
        "street": street,
        "pot": spot.get("pot", defaults.get("pot")),
        "stack": spot.get("effective_stack", defaults.get("effective_stack")),
        "range_ip": spot.get("range_ip", defaults.get("range_ip")),
        "range_oop": spot.get("range_oop", defaults.get("range_oop")),
        "bet_sizes": _bet_sizes_for_street(raw_sizes, street),
        "accuracy": spot.get("accuracy", defaults.get("accuracy")),
        "max_iteration": spot.get("max_iteration", defaults.get("max_iteration")),
        "dump_rounds": spot.get("dump_rounds", defaults.get("dump_rounds")),
        "allin_threshold": spot.get("allin_threshold", defaults.get("allin_threshold")),
        "tree": "street_scoped_v1",
    }
    raw = json.dumps(payload, sort_keys=True)
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def run_solver(
    bin_path: Path,
    input_text: str,
    dump_path: Path,
    *,
    timeout_s: int = 600,
) -> None:
    """Run console_solver with CWD = binary directory (needs resources/)."""
    cwd = bin_path.parent
    dump_path.parent.mkdir(parents=True, exist_ok=True)
    inp = dump_path.with_suffix(".input.txt")
    inp.write_text(input_text, encoding="utf-8")
    # Remove stale dump so we don't accept a previous partial
    if dump_path.exists():
        try:
            dump_path.unlink()
        except OSError:
            pass
    cmd = [str(bin_path), "-i", str(inp.resolve())]
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            timeout=timeout_s,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(f"console_solver timeout after {timeout_s}s") from exc
    if proc.returncode != 0:
        tail = (proc.stderr or proc.stdout or "")[-800:]
        raise RuntimeError(f"console_solver exit {proc.returncode}: {tail}")
    if not dump_path.is_file() or dump_path.stat().st_size < 50:
        # Some builds write relative to cwd
        alt = cwd / dump_path.name
        if alt.is_file() and alt.stat().st_size >= 50:
            dump_path.write_bytes(alt.read_bytes())
        else:
            raise RuntimeError(f"dump missing or tiny: {dump_path}")


def run_solver_with_fallback(
    bin_path: Path,
    spot: dict,
    defaults: dict,
    dump_path: Path,
    *,
    timeout_s: int = 600,
) -> None:
    """Solve spot; on abort/crash retry with thread=1 + isomorphism=0."""
    attempts = (
        {},  # grid / spot defaults
        {"thread_num": 1, "use_isomorphism": 0},
        {"thread_num": 1, "use_isomorphism": 0},  # second chance after flaky abort
    )
    last_err: Optional[Exception] = None
    for i, override in enumerate(attempts):
        inp = build_input_text(spot, defaults, dump_path, **override)
        try:
            if override:
                _log(
                    f"  retry {i} thread={override.get('thread_num')} "
                    f"iso={override.get('use_isomorphism')}"
                )
            run_solver(bin_path, inp, dump_path, timeout_s=timeout_s)
            return
        except Exception as exc:
            last_err = exc
            # exit 134 = SIGABRT; also catch missing dumps / timeouts
            _log(f"  solver attempt failed: {exc}")
            continue
    raise RuntimeError(f"all solver attempts failed: {last_err}")


def load_dump(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("dump root not an object")
    return data


# ---------------------------------------------------------------------------
# Aggregation + write
# ---------------------------------------------------------------------------

def _size_pot_frac_for_key(
    key: str,
    size_acc: dict[str, list[tuple[float, float]]],
    street: str,
    texture: str,
) -> float:
    samples = size_acc.get(key) or []
    if samples:
        wsum = sum(w for w, _ in samples)
        if wsum > 0:
            frac = sum(w * f for w, f in samples) / wsum
            return max(0.25, min(1.0, frac))
    # Street/texture defaults aligned with heuristic sizing
    defaults = {
        ("dry", "flop"): 0.33,
        ("dry", "turn"): 0.50,
        ("dry", "river"): 0.66,
        ("wet", "flop"): 0.50,
        ("wet", "turn"): 0.66,
        ("wet", "river"): 0.75,
        ("paired", "flop"): 0.40,
        ("paired", "turn"): 0.55,
        ("paired", "river"): 0.66,
    }
    # parse texture/street from key
    parts = key.split("|")
    if len(parts) == 4:
        return defaults.get((parts[2], parts[0]), 0.50)
    return defaults.get((texture, street), 0.50)


def finalize_buckets(
    acc: dict[str, dict[str, float]],
    size_acc: dict[str, list[tuple[float, float]]],
    *,
    streets_solved: list[str],
    fill_heuristic: bool = True,
) -> dict[str, dict[str, float]]:
    """Normalize solver mass; fill missing free/facing halves + missing keys."""
    buckets: dict[str, dict[str, float]] = {}

    # Start from full heuristic grid so every key exists
    if fill_heuristic:
        for street in STREETS:
            for role in ROLES:
                for texture in TEXTURES:
                    for sbin in STRENGTH_BINS:
                        k = bucket_key(street, role, texture, sbin)
                        buckets[k] = _heuristic_freqs(street, role, texture, sbin)

    for key, mass in acc.items():
        parts = key.split("|")
        if len(parts) != 4:
            continue
        street, role, texture, sbin = parts
        free_mass = mass.get("bet", 0.0) + mass.get("check", 0.0)
        face_mass = (
            mass.get("call", 0.0) + mass.get("fold", 0.0) + mass.get("raise", 0.0)
        )
        heur = _heuristic_freqs(street, role, texture, sbin)

        if free_mass > 1e-9:
            bet = mass["bet"] / free_mass
            check = mass["check"] / free_mass
        else:
            # recover free from heuristic packing
            fh = heur["bet"] + heur["check"]
            if fh > 0:
                bet, check = heur["bet"] / fh, heur["check"] / fh
            else:
                bet, check = 0.35, 0.65

        if face_mass > 1e-9:
            fold = mass["fold"] / face_mass
            call = mass["call"] / face_mass
            raise_f = mass["raise"] / face_mass
        else:
            ff = heur["fold"] + heur["call"] + heur["raise"]
            if ff > 0:
                fold = heur["fold"] / ff
                call = heur["call"] / ff
                raise_f = heur["raise"] / ff
            else:
                fold, call, raise_f = 0.40, 0.40, 0.20

        size = _size_pot_frac_for_key(key, size_acc, street, texture)
        raw = {
            "bet": bet * 0.5,
            "check": check * 0.5,
            "call": call * 0.35,
            "fold": fold * 0.35,
            "raise": raise_f * 0.30,
            "size_pot_frac": size,
        }
        buckets[key] = _normalize_freqs(raw)

    # Street extrapolation: if turn/river not solved, copy flop with size nudge
    solved = set(streets_solved)
    for street in STREETS:
        if street in solved:
            continue
        for role in ROLES:
            for texture in TEXTURES:
                for sbin in STRENGTH_BINS:
                    src = bucket_key("flop", role, texture, sbin)
                    dst = bucket_key(street, role, texture, sbin)
                    if src not in buckets:
                        continue
                    base = dict(buckets[src])
                    # size nudge by street
                    size = float(base.get("size_pot_frac", 0.5))
                    if street == "turn":
                        size = min(1.0, size + 0.10)
                    elif street == "river":
                        size = min(1.0, size + 0.18)
                    base["size_pot_frac"] = size
                    # Slightly fewer river bluffs (air/weak)
                    if street == "river" and sbin in ("air", "weak"):
                        b = float(base["bet"])
                        base["bet"] = max(0.02, b * 0.85)
                        base["check"] = float(base["check"]) + (b - base["bet"])
                    buckets[dst] = _normalize_freqs(base)

    return buckets


def build_payload(
    buckets: dict[str, dict[str, float]],
    *,
    spots_solved: int,
    spots_failed: list[str],
    streets_solved: list[str],
    streets_extrapolated: list[str],
    grid_path: Path,
) -> dict[str, Any]:
    generator = (
        "texas_solver_v2" if spots_solved >= 60 else "texas_solver_v1"
    )
    meta = {
        "generator": generator,
        "solver": "bupticybee/TexasSolver@v0.2.0",
        "spots_solved": spots_solved,
        "spots_failed": spots_failed,
        "streets_solved": streets_solved,
        "streets_extrapolated": streets_extrapolated,
        "key_count": len(buckets),
        "baked_at": date.today().isoformat(),
        "grid": str(grid_path.as_posix()),
        "strength_bin_method": (
            "hand_category_equity_heuristic→strength_bin "
            "(pair/set/draw/overcard categories; not solver EV)"
        ),
        "streets": list(STREETS),
        "roles": list(ROLES),
        "textures": list(TEXTURES),
        "strength_bins": list(STRENGTH_BINS),
        "thread_iso_note": (
            "defaults thread_num=2 use_isomorphism=0; abort-retry to 1/0 "
            "(TexasSolver v0.2.0 SIGABRT on some boards with 8+threads+iso)"
        ),
    }
    payload: dict[str, Any] = {
        "schema": "postflop-hu-buckets-v1",
        "source": "examples/bake_texassolver_buckets.py",
        "meta": meta,
        "buckets": buckets,
    }
    try:
        from solver_provenance import solver_provenance, stamp_chart_provenance

        prov = solver_provenance(
            "cfr_plus",
            version="texas_solver_v0.2.0",
            equilibrium_selection="time_average",
            nash_set_singleton=None,
            notes=(
                f"{generator}: aggregated TexasSolver console dumps over "
                "research/texassolver_spot_grid.json; O(1) bucket table only — "
                "binary not redistributed (AGPL)"
            ),
        )
        payload = stamp_chart_provenance(payload, prov)
    except Exception as exc:  # pragma: no cover
        payload["solver_provenance"] = {
            "solver_family": "cfr_plus",
            "notes": f"{generator} ({exc})",
        }
    return payload


def atomic_write_json(path: Path, payload: dict[str, Any]) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + f".tmp.{secrets.token_hex(4)}")
    try:
        tmp.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        os.replace(tmp, path)
    finally:
        if tmp.exists():
            try:
                tmp.unlink()
            except OSError:
                pass
    return path


def parse_board(spot: dict) -> list[str]:
    b = spot.get("board")
    if isinstance(b, list):
        return [str(x).strip() for x in b]
    return [p.strip() for p in str(b).split(",") if p.strip()]


def bake(
    *,
    grid_path: Path,
    out_path: Path,
    dump_dir: Path,
    bin_path: Path,
    only_streets: Optional[set[str]] = None,
    min_flop: int = MIN_SUCCESSFUL_FLOP,
    timeout_s: int = 600,
    skip_solve: bool = False,
) -> dict[str, Any]:
    grid = json.loads(Path(grid_path).read_text(encoding="utf-8"))
    defaults = grid.get("defaults") or {}
    spots = list(grid.get("spots") or [])
    if only_streets:
        spots = [s for s in spots if s.get("street") in only_streets]

    dump_dir = Path(dump_dir)
    dump_dir.mkdir(parents=True, exist_ok=True)

    acc: dict[str, dict[str, float]] = {}
    size_acc: dict[str, list[tuple[float, float]]] = {}
    ok_ids: list[str] = []
    failed: list[str] = []
    streets_with_data: set[str] = set()

    for spot in spots:
        sid = str(spot.get("id") or spot.get("board"))
        street = str(spot.get("street") or "flop").lower()
        texture = str(spot.get("texture") or "dry").lower()
        board = parse_board(spot)
        ck = spot_cache_key(spot, defaults)
        dump_path = dump_dir / f"{sid}_{ck}.json"

        try:
            if dump_path.is_file() and dump_path.stat().st_size > 50:
                _log(f"cache hit {sid}")
                root = load_dump(dump_path)
            elif skip_solve:
                raise RuntimeError(f"no cache for {sid} and --skip-solve set")
            else:
                _log(f"solving {sid} board={','.join(board)} …")
                t0 = time.time()
                run_solver_with_fallback(
                    bin_path, spot, defaults, dump_path, timeout_s=timeout_s,
                )
                root = load_dump(dump_path)
                _log(f"  ok {sid} in {time.time() - t0:.1f}s "
                     f"({dump_path.stat().st_size} bytes)")

            nodes = extract_decision_nodes(root)
            n_hands = 0
            pot = float(spot.get("pot", defaults.get("pot", 20)))
            for role, node in nodes:
                n_hands += accumulate_node(
                    acc,
                    size_acc,
                    street=street,
                    role=role,
                    texture=texture,
                    board=board,
                    node=node,
                    pot=pot,
                )
            if n_hands <= 0:
                raise RuntimeError("no strategy hands extracted")
            ok_ids.append(sid)
            streets_with_data.add(street)
            _log(f"  aggregated {sid}: {len(nodes)} nodes, {n_hands} hand rows")
        except Exception as exc:
            failed.append(f"{sid}: {exc}")
            _log(f"FAIL {sid}: {exc}")
            continue

    flop_ok = sum(1 for s in spots if s.get("street") == "flop" and str(s.get("id")) in ok_ids)
    # ok_ids holds ids; recount flop successes properly
    flop_ids = {str(s.get("id")) for s in spots if s.get("street") == "flop"}
    flop_ok = len([i for i in ok_ids if i in flop_ids])
    if flop_ok < min_flop:
        raise SystemExit(
            f"Need ≥{min_flop} successful flop spots, got {flop_ok}. "
            f"Failed: {failed[:5]}"
        )

    # Prefer declaring streets with real solver data as solved
    streets_solved = [s for s in STREETS if s in streets_with_data]
    # If turn/river have any real spots, they're solved; else extrapolated from flop
    if "flop" not in streets_solved and streets_with_data:
        streets_solved = sorted(streets_with_data)
    streets_extrapolated = [s for s in STREETS if s not in streets_solved]

    buckets = finalize_buckets(
        acc,
        size_acc,
        streets_solved=streets_solved,
        fill_heuristic=True,
    )
    payload = build_payload(
        buckets,
        spots_solved=len(ok_ids),
        spots_failed=failed,
        streets_solved=streets_solved,
        streets_extrapolated=streets_extrapolated,
        grid_path=Path(grid_path),
    )
    atomic_write_json(out_path, payload)
    _log(
        f"wrote {out_path} keys={len(buckets)} "
        f"solved={streets_solved} extrapolated={streets_extrapolated} "
        f"spots_ok={len(ok_ids)} failed={len(failed)}"
    )
    return payload


def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Bake postflop buckets from TexasSolver")
    ap.add_argument(
        "--grid",
        type=Path,
        default=DEFAULT_GRID,
        help="Spot grid JSON",
    )
    ap.add_argument(
        "--out",
        type=Path,
        default=DEFAULT_OUT,
        help="Output buckets JSON",
    )
    ap.add_argument(
        "--dump-dir",
        type=Path,
        default=DEFAULT_DUMP_DIR,
        help="Cache directory for solver dumps",
    )
    ap.add_argument(
        "--bin",
        type=Path,
        default=None,
        help="console_solver path (else CEMINI_TEXASSOLVER_BIN / default)",
    )
    ap.add_argument(
        "--streets",
        default="",
        help="Comma list to restrict (e.g. flop,turn)",
    )
    ap.add_argument(
        "--min-flop",
        type=int,
        default=MIN_SUCCESSFUL_FLOP,
    )
    ap.add_argument(
        "--timeout",
        type=int,
        default=int(os.environ.get("CEMINI_TEXASSOLVER_TIMEOUT", "900")),
        help="Per-spot solver timeout seconds",
    )
    ap.add_argument(
        "--skip-solve",
        action="store_true",
        help="Only use cached dumps (fail spots without cache)",
    )
    args = ap.parse_args(argv)

    bin_path = Path(args.bin).resolve() if args.bin else resolve_solver_bin()
    only = None
    if args.streets.strip():
        only = {s.strip().lower() for s in args.streets.split(",") if s.strip()}

    payload = bake(
        grid_path=Path(args.grid),
        out_path=Path(args.out),
        dump_dir=Path(args.dump_dir),
        bin_path=bin_path,
        only_streets=only,
        min_flop=args.min_flop,
        timeout_s=args.timeout,
        skip_solve=args.skip_solve,
    )
    meta = payload.get("meta") or {}
    assert meta.get("generator") in ("texas_solver_v1", "texas_solver_v2")
    assert int(meta.get("key_count") or 0) >= 90
    assert int(meta.get("spots_solved") or 0) >= 44
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
