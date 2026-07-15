"""Runnable Auto Research example — tiny in-memory preflop chart.

A drop-in `retrieve_solver_context(table)` that returns the recommended
preflop action for the hero's hand class + position bucket. No network,
no API key — pure lookup table. Good enough to make decide()'s preflop
play meaningfully better than the default heuristic.

Wire it into agent.py by replacing the no-op stub:

    # in examples/agent.py, near the top of the file
    from research_static_chart import research_static_chart as retrieve_solver_context

Or call it explicitly from llm_agent.py — the result is serialized into
the LLM prompt as AUTO-RESEARCH CONTEXT.

Run standalone for a quick smoke check:

    uv run examples/research_static_chart.py

When CEMINI_MAFP_CHART is truthy, a MAFP HU overlay is loaded once (O(1)
after first call) and applied to a working copy of the HU open chart.
Loader is replicated here — do NOT import mafp_chart_refinement at runtime.
"""
from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

from position_utils import hero_position_label
from table_format_utils import resolve_table_format  # noqa: E402

# MAFP overlay cache: (resolved_path_str | None, mtime | None) -> chart copy
_mafp_overlay_cache: Optional[dict[str, dict[str, set[str]]]] = None
_mafp_overlay_cache_key: Optional[tuple[Optional[str], Optional[float]]] = None

# HU NLHE — BTN/SB combined seat uses BTN chart; BB defends wider than 6-max BB chart.
_HU_OPEN_CHART = {
    "BTN": {
        "raise": {
            "AA", "KK", "QQ", "JJ", "TT", "99", "88", "77", "66", "55", "44", "33", "22",
            "AKs", "AKo", "AQs", "AQo", "AJs", "AJo", "ATs", "ATo", "A9s", "A9o", "A8s", "A8o", "A7s",
            "A6s", "A3s", "A2s",
            "KQs", "KQo", "KJs", "KJo", "KTs", "KTo", "K9s", "K9o", "K8s", "K7s", "K6s", "K5s", "K4s",
            "QJs", "QJo", "QTs", "QTo", "Q9s", "Q9o", "Q8s", "Q7s", "Q6s",
            "JTs", "JTo", "J9s", "J9o", "J8s", "T9s", "T9o", "T8s", "T7s", "98s", "97s", "96s",
            "87s", "86s", "76s", "65s", "54s",
        },
        "call": set(),
    },
    "BB": {
        "raise": {
            "AA", "KK", "QQ", "JJ", "TT", "99", "88", "AKs", "AKo", "AQs", "AQo",
            "AJs", "AJo", "KQs", "KJs", "QJs",
            "A5s", "A4s", "A3s", "A2s", "76s", "65s", "54s", "87s", "86s", "98s",
        },
        "call": {
            "TT", "99", "88", "77", "66", "55", "44", "33", "22",
            "AQo", "AJs", "AJo", "ATs", "ATo", "A9s", "A9o", "A8s", "A8o", "A7s", "A7o", "A6s", "A6o",
            "A5s", "A5o", "A4s", "A4o", "A3s", "A2s",
            "KQs", "KQo", "KJs", "KJo", "KTs", "KTo", "K9s", "K9o", "K8s", "K7s", "K6s", "K5s", "K4s",
            "K3s", "K2s", "QJs", "QJo", "QTs", "QTo", "Q9s", "Q9o", "Q8s", "Q7s", "Q6s", "Q5s",
            "JTs", "JTo", "J9s", "J9o", "J8s", "T9s", "T9o", "T8s", "T7s", "98s", "97s", "87s", "86s",
            "85s", "76s", "75s", "65s", "64s", "56s", "54s", "53s", "43s",
        },
    },
}


# 6-max NLHE opening ranges, position × hand class → suggested action.
# This is a coarse caricature of a real preflop chart — good enough to
# show shape, NOT good enough to win a benchmark. Replace with a real
# GTOWizard / WASM Postflop / TexasSolver export when you ship.
_OPEN_CHART = {
    # UTG (tightest)
    "UTG": {
        "raise": {"AA", "KK", "QQ", "JJ", "TT", "99",
                  "AKs", "AKo", "AQs", "AJs", "KQs"},
        "call":  set(),
    },
    # Middle position
    "MP": {
        "raise": {"AA", "KK", "QQ", "JJ", "TT", "99", "88", "77",
                  "AKs", "AKo", "AQs", "AQo", "AJs", "AJo", "ATs",
                  "KQs", "KJs", "QJs"},
        "call":  set(),
    },
    # Cutoff (wider)
    "CO": {
        "raise": {"AA", "KK", "QQ", "JJ", "TT", "99", "88", "77", "66", "55",
                  "AKs", "AKo", "AQs", "AQo", "AJs", "AJo", "ATs", "ATo",
                  "A9s", "A8s", "A7s", "A6s", "A5s",
                  "KQs", "KQo", "KJs", "KTs", "QJs", "QTs", "JTs", "T9s", "98s"},
        "call":  set(),
    },
    # Button (widest open)
    "BTN": {
        "raise": {"AA", "KK", "QQ", "JJ", "TT", "99", "88", "77", "66", "55", "44", "33", "22",
                  "AKs", "AKo", "AQs", "AQo", "AJs", "AJo", "ATs", "ATo",
                  "A9s", "A8s", "A7s", "A6s", "A5s", "A4s", "A3s", "A2s",
                  "KQs", "KQo", "KJs", "KJo", "KTs", "K9s",
                  "QJs", "QTs", "Q9s", "JTs", "J9s", "T9s", "98s", "87s", "76s"},
        "call":  set(),
    },
    # Small blind (mixed, here simplified to a tight raise)
    "SB": {
        "raise": {"AA", "KK", "QQ", "JJ", "TT", "99", "88",
                  "AKs", "AKo", "AQs", "AQo", "AJs", "ATs", "KQs", "KJs", "QJs"},
        "call":  set(),
    },
    # Big blind (defends wide vs late opens; treat as call/check by default)
    "BB": {
        "raise": {"AA", "KK", "QQ", "JJ", "TT",
                  "AKs", "AKo", "AQs"},
        "call":  set(),  # BB calls happen automatically when checked to
    },
}

def _hand_class(hole: list[str]) -> str:
    """Convert ['As', 'Ks'] -> 'AKs'. Returns '' if unparseable."""
    ranks = "23456789TJQKA"
    if not hole or len(hole) != 2:
        return ""
    r1, s1 = hole[0][0].upper(), hole[0][-1].lower()
    r2, s2 = hole[1][0].upper(), hole[1][-1].lower()
    if r1 not in ranks or r2 not in ranks:
        return ""
    if ranks.index(r1) < ranks.index(r2):
        r1, r2 = r2, r1
        s1, s2 = s2, s1
    if r1 == r2:
        return r1 + r2
    return f"{r1}{r2}{'s' if s1 == s2 else 'o'}"


def _env_truthy(name: str) -> bool:
    return os.environ.get(name, "").strip().lower() in ("1", "true", "yes", "on")


def resolve_mafp_chart_path() -> Optional[Path]:
    """Bundle-aware MAFP chart path.

    Order: CEMINI_MAFP_CHART_PATH (tests) → assets/research (bundle) →
    repo research/ next to examples/.
    """
    override = os.environ.get("CEMINI_MAFP_CHART_PATH", "").strip()
    if override:
        return Path(override)

    module_dir = Path(__file__).resolve().parent  # assets/ in bundle, examples/ in repo
    candidates = (
        module_dir / "research" / "mafp_hu_chart.json",  # assets/research (sandbox bundle)
        module_dir.parent / "assets" / "research" / "mafp_hu_chart.json",
        module_dir.parent / "research" / "mafp_hu_chart.json",  # repo research/
    )
    for p in candidates:
        if p.is_file():
            return p
    return None


def load_mafp_chart_ranges(path: Optional[Path] = None) -> Optional[dict[str, dict[str, str]]]:
    """Load MAFP ranges from JSON. Fail-open: None on missing/unparseable."""
    p = path if path is not None else resolve_mafp_chart_path()
    if p is None or not Path(p).is_file():
        return None
    try:
        import json

        data = json.loads(Path(p).read_text(encoding="utf-8"))
    except Exception:
        return None
    ranges = data.get("ranges") if isinstance(data, dict) else None
    return ranges if isinstance(ranges, dict) else None


def _deep_copy_hu_chart() -> dict[str, dict[str, set[str]]]:
    out: dict[str, dict[str, set[str]]] = {}
    for pos, rules in _HU_OPEN_CHART.items():
        out[pos] = {
            "raise": set(rules.get("raise", set())),
            "call": set(rules.get("call", set())),
        }
    return out


def apply_mafp_overlay_to_chart(
    chart: dict[str, dict[str, set[str]]],
    ranges: dict[str, dict[str, str]],
) -> int:
    """Merge MAFP hand→action ranges into a HU chart copy. Returns cells touched."""
    n = 0
    for pos, hands in ranges.items():
        if pos not in chart:
            continue
        if not isinstance(hands, dict):
            continue
        rules = chart[pos]
        raise_set = rules.setdefault("raise", set())
        call_set = rules.setdefault("call", set())
        for hand, action in hands.items():
            if not isinstance(hand, str) or not isinstance(action, str):
                continue
            raise_set.discard(hand)
            call_set.discard(hand)
            if action == "raise":
                raise_set.add(hand)
            elif action == "call":
                call_set.add(hand)
            # fold: leave out of both sets
            n += 1
    return n


def _reset_mafp_overlay_cache() -> None:
    """Test helper: clear overlay cache so path/flag changes take effect."""
    global _mafp_overlay_cache, _mafp_overlay_cache_key
    _mafp_overlay_cache = None
    _mafp_overlay_cache_key = None


def _hu_chart_for_lookup() -> dict[str, dict[str, set[str]]]:
    """Return HU open chart, with MAFP overlay when CEMINI_MAFP_CHART is on.

    Does not mutate the module-level `_HU_OPEN_CHART` baseline (flag-off
    parity). Overlay is cached by resolved path + mtime (idempotent).
    """
    global _mafp_overlay_cache, _mafp_overlay_cache_key

    if not _env_truthy("CEMINI_MAFP_CHART"):
        return _HU_OPEN_CHART

    path = resolve_mafp_chart_path()
    mtime: Optional[float] = None
    path_str: Optional[str] = None
    if path is not None:
        try:
            path_str = str(path.resolve())
            if path.is_file():
                mtime = path.stat().st_mtime
        except OSError:
            path_str = str(path)
            mtime = None

    cache_key = (path_str, mtime)
    if _mafp_overlay_cache is not None and _mafp_overlay_cache_key == cache_key:
        return _mafp_overlay_cache

    chart = _deep_copy_hu_chart()
    ranges = load_mafp_chart_ranges(path)
    if ranges:
        apply_mafp_overlay_to_chart(chart, ranges)
    _mafp_overlay_cache = chart
    _mafp_overlay_cache_key = cache_key
    return chart


def research_static_chart(table: dict) -> dict:
    """Return a small dict with preflop chart recommendation, hand class,
    and position bucket. Empty on postflop streets — postflop spots need
    a real solver, not a static chart.

    Shape:
      {
        "preflop_action": "raise" | "call" | "fold",
        "hand_class": "AKs",
        "position": "BTN",
        "source": "static-chart-v1",
      }
    """
    street = (table.get("street") or "Preflop").lower()
    if street != "preflop":
        return {}

    self_seat_num = table.get("selfSeatNumber")
    seats = table.get("seats") or []
    self_seat = next((s for s in seats if s.get("seatNumber") == self_seat_num), {})
    hole = list(self_seat.get("holeCards") or [])
    cls = _hand_class(hole)
    if not cls:
        return {}

    pos = hero_position_label(table)
    fmt = resolve_table_format(table)
    if fmt == "hu":
        chart_source = _hu_chart_for_lookup()
        if pos == "SB":
            pos = "BTN"
    else:
        chart_source = _OPEN_CHART
    rules = chart_source.get(pos) or {}
    if cls in rules.get("raise", set()):
        action = "raise"
    elif cls in rules.get("call", set()):
        action = "call"
    else:
        action = "fold"

    source = f"static-chart-v1-{fmt}"
    if fmt == "hu" and _env_truthy("CEMINI_MAFP_CHART"):
        p = resolve_mafp_chart_path()
        if p is not None and p.is_file():
            source = f"mafp-overlay-v1-{fmt}"

    return {
        "preflop_action": action,
        "hand_class": cls,
        "position": pos,
        "source": source,
        "table_format": fmt,
    }


def _demo() -> int:
    """Quick smoke check: print recommendations for a few canonical spots."""
    spots = [
        {"label": "BTN AKs preflop",
         "table": {"street": "Preflop", "selfSeatNumber": 1,
                   "seats": [{"seatNumber": 1, "holeCards": ["As", "Ks"]}]}},
        {"label": "UTG 72o preflop",
         "table": {"street": "Preflop", "selfSeatNumber": 4,
                   "seats": [{"seatNumber": 4, "holeCards": ["7d", "2c"]}]}},
        {"label": "SB QQ preflop",
         "table": {"street": "Preflop", "selfSeatNumber": 2,
                   "seats": [{"seatNumber": 2, "holeCards": ["Qh", "Qd"]}]}},
        {"label": "BTN AKs FLOP (chart skips postflop)",
         "table": {"street": "Flop", "selfSeatNumber": 1,
                   "boardCards": ["Ah", "Kd", "7c"],
                   "seats": [{"seatNumber": 1, "holeCards": ["As", "Ks"]}]}},
        {"label": "CO 22 preflop",
         "table": {"street": "Preflop", "selfSeatNumber": 6,
                   "seats": [{"seatNumber": 6, "holeCards": ["2s", "2c"]}]}},
    ]
    for s in spots:
        print(f"{s['label']:48s} -> {research_static_chart(s['table'])}")
    return 0


def _export_preflop_json(out_path: str = "research/preflop.json") -> str:
    """Write the static preflop chart to ./research/preflop.json so that
    decide() / retrieve_solver_context() can load it without re-running the
    script. Schema: {position: {hand_class: action}}. Atomic write via a
    sibling `.tmp` file then os.replace, so a crash mid-write can't leave a
    half-written file.

    Returns the absolute path of the file written."""
    import json
    import os
    from pathlib import Path

    # K136: Local import to keep module-level imports minimal (lazy import pattern)
    from solver_provenance import solver_provenance, stamp_chart_provenance

    path = Path(out_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    chart: dict[str, dict[str, str]] = {}
    for pos, rules in _OPEN_CHART.items():
        per_pos: dict[str, str] = {}
        for hand in rules.get("raise", set()):
            per_pos[hand] = "raise"
        for hand in rules.get("call", set()):
            # raise wins ties (a hand in both sets favours the more aggressive
            # action), but in this chart `call` sets are empty so this is a
            # forward-compatibility no-op.
            per_pos.setdefault(hand, "call")
        chart[pos] = per_pos

    payload = {
        "schema": "preflop-chart-v1",
        "source": "examples/research_static_chart.py",
        "note": "6-max NLHE opening chart. {position: {hand_class: action}}. "
                "Hands not listed default to fold. Postflop is not covered.",
        "ranges": chart,
    }

    # K136: Stamp solver provenance (backward-compatible optional key)
    payload = stamp_chart_provenance(payload, solver_provenance(
        "static_chart",
        equilibrium_selection="heuristic",
        notes="hand-authored 6-max opening caricature; not solver output",
    ))

    # Unique temp name (NamedTemporaryFile-style) to avoid collisions when
    # two concurrent runs write the same target — fixed `.tmp` suffix would
    # let one overwrite the other mid-flight. Mirrors arena_client.py
    # _atomic_write pattern.
    import secrets as _secrets
    tmp_path = path.with_suffix(path.suffix + f".tmp.{_secrets.token_hex(4)}")
    try:
        tmp_path.write_text(json.dumps(payload, indent=2, sort_keys=True))
        os.replace(tmp_path, path)
    finally:
        if tmp_path.exists():
            try:
                tmp_path.unlink()
            except OSError:
                pass
    return str(path.resolve())


def load_preflop_chart(path: str = "research/preflop.json") -> Optional[dict]:
    """Load a previously-exported preflop chart from disk. Returns None if
    the file is missing or unparseable — callers should fall back to the
    in-memory `_OPEN_CHART` heuristic in that case."""
    import json
    from pathlib import Path

    p = Path(path)
    if not p.exists():
        return None
    try:
        data = json.loads(p.read_text())
    except Exception:
        return None
    ranges = data.get("ranges") if isinstance(data, dict) else None
    if not isinstance(ranges, dict):
        return None
    return ranges


if __name__ == "__main__":
    import sys
    rc = _demo()
    out = _export_preflop_json()
    print(f"\nwrote preflop chart -> {out}")
    sys.exit(rc)
