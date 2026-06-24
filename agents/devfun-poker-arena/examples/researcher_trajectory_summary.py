#!/usr/bin/env python3
"""Multi-axis proxy summary for Researcher Round trajectory exports.

Reads selfplay trajectory JSONL or Arena export bundles and writes
axis_summary.json for Discord / researcher contribution narrative.

Usage:
    uv run python examples/researcher_trajectory_summary.py \\
        --selfplay reports/researcher-round/.../selfplay_trajectory.jsonl
    uv run python examples/researcher_trajectory_summary.py \\
        --export-dir reports/exports/<compId>/<ts> --gate
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean
from typing import Any

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

# Raeth M₁–M₉ proxies (K122) — deterministic axes for submit gates.
_CARD_TOKEN_RE = re.compile(r"(?<![A-Za-z0-9])([2-9TJQKA][hdcs])(?![A-Za-z0-9])", re.I)
_VPIP_ACTIONS = frozenset({"call", "bet", "raise", "all-in"})

DEFAULT_GATE_THRESHOLDS: dict[str, float] = {
    "M8_hallucination_rate_max": 0.05,
    "M8_hole_leak_rate_max": 0.02,
    "M9_btn_minus_utg_vpip_min": -0.20,
    "hero_submissions_min": 1.0,
}

_PREFLOP_POSITION_ORDER = ("UTG", "MP", "CO", "BTN", "SB", "BB")


def _load_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    if not path.is_file():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return rows


def _vpip_rate(preflop_rows: list[dict]) -> float:
    if not preflop_rows:
        return 0.0
    vol = sum(
        1 for d in preflop_rows
        if str(d.get("action") or "").lower() in _VPIP_ACTIONS
    )
    return vol / len(preflop_rows)


def _entropy(counts: Counter) -> float:
    total = sum(counts.values())
    if total <= 0:
        return 0.0
    ent = 0.0
    for c in counts.values():
        p = c / total
        if p > 0:
            ent -= p * math.log2(p)
    return ent


def _cards_in_text(text: str) -> set[str]:
    return {m.group(1).lower() for m in _CARD_TOKEN_RE.finditer(text or "")}


def _allowed_cards(hole_key: str, board: list[str] | None = None) -> set[str]:
    allowed: set[str] = set()
    if hole_key:
        # hole_key is concatenated e.g. AsKd — split into 2-char tokens.
        hk = hole_key.replace(" ", "")
        for i in range(0, len(hk), 2):
            chunk = hk[i:i + 2]
            if len(chunk) == 2:
                allowed.add(chunk.lower())
    for c in board or []:
        s = str(c).strip()
        if len(s) >= 2:
            allowed.add(s[:2].lower() if len(s) == 2 else s.lower())
    return allowed


def compute_memory_gap(decisions: list[dict]) -> dict:
    """Compute memory-gap statistics for trajectory analysis.

    Heuristic:
    - bound_veto_memory_off: veto applied when session_memory_on is False
    - misdecide_memory_on: veto applied when session_memory_on is True OR
      high hallucination rate when memory is off

    Returns dict with counts:
    - bound_veto_total: total vetoes
    - bound_veto_memory_off: vetoes when memory was off
    - misdecide_memory_on: mis-decisions (veto when memory on)
    """
    if not decisions:
        return {
            "bound_veto_total": 0,
            "bound_veto_memory_off": 0,
            "misdecide_memory_on": 0,
        }

    bound_veto_total = 0
    bound_veto_memory_off = 0
    misdecide_memory_on = 0

    for d in decisions:
        veto = bool(d.get("trajectory_bound_veto"))
        memory_on = d.get("session_memory_on")
        # Handle None case - default to True if telemetry missing
        if memory_on is None:
            continue

        if veto:
            bound_veto_total += 1
            if not memory_on:
                bound_veto_memory_off += 1
            else:
                misdecide_memory_on += 1

    return {
        "bound_veto_total": bound_veto_total,
        "bound_veto_memory_off": bound_veto_memory_off,
        "misdecide_memory_on": misdecide_memory_on,
    }


def compute_selfplay_axes(decisions: list[dict], results: list[dict]) -> dict[str, Any]:
    """Deterministic Raeth proxies on hero trajectory rows."""
    if not decisions:
        return {}

    preflop = [d for d in decisions if d.get("street") == "Preflop"]
    by_pos: dict[str, list[dict]] = defaultdict(list)
    for d in preflop:
        by_pos[str(d.get("position") or "?")].append(d)

    # M₉ — positional VPIP spread (6-max: BTN vs UTG; HU: BTN vs BB).
    vpip_by_pos = {pos: round(_vpip_rate(rows), 4) for pos, rows in by_pos.items()}
    btn_vpip = vpip_by_pos.get("BTN", 0.0)
    utg_vpip = vpip_by_pos.get("UTG", 0.0)
    bb_vpip = vpip_by_pos.get("BB", 0.0)
    if "UTG" in vpip_by_pos:
        m9_gap = round(btn_vpip - utg_vpip, 4)
        m9_gap_label = "btn_minus_utg"
    else:
        m9_gap = round(btn_vpip - bb_vpip, 4)
        m9_gap_label = "btn_minus_bb"

    # M₁ — bet-size bucket histogram on aggressive actions.
    bet_buckets = Counter(
        str(d.get("bet_size_bucket") or "none")
        for d in decisions
        if str(d.get("action") or "").lower() in ("bet", "raise", "all-in")
    )
    m1_total = sum(bet_buckets.values()) or 1
    m1_hist = {k: round(v / m1_total, 4) for k, v in bet_buckets.items()}

    # M₇ — mean action entropy per (street, position).
    mix_buckets: dict[str, Counter] = defaultdict(Counter)
    for d in decisions:
        key = f"{d.get('street')}|{d.get('position')}"
        mix_buckets[key][str(d.get("action") or "").lower()] += 1
    entropies = [_entropy(c) for c in mix_buckets.values() if sum(c.values()) >= 3]
    m7_mean_entropy = round(mean(entropies), 4) if entropies else 0.0

    # M₄ — VPIP delta in 7-hand windows after bad-beat hands (chip_delta < 0).
    bad_hand_ids = {
        int(r.get("hand_id"))
        for r in results
        if r.get("chip_delta") is not None and int(r.get("chip_delta")) < 0
    }
    session_vpip = _vpip_rate(preflop)
    post_bad: list[dict] = []
    for d in preflop:
        hid = d.get("hand_id")
        if hid is not None and int(hid) in bad_hand_ids:
            post_bad.append(d)
    post_bad_vpip = _vpip_rate(post_bad[:7 * max(len(bad_hand_ids), 1)])
    m4_vpip_delta = round(post_bad_vpip - session_vpip, 4)

    # M₈ — factual: hallucinated cards + hole-card leaks in reasoning YAML.
    hallucination_n = 0
    hole_leak_n = 0
    checked_n = 0
    for d in decisions:
        reasoning = str(d.get("reasoning") or "")
        if not reasoning:
            continue
        checked_n += 1
        hole_key = str(d.get("hole_key") or "")
        allowed = _allowed_cards(hole_key)
        found = _cards_in_text(reasoning)
        if hole_key:
            hk = hole_key.replace(" ", "").lower()
            if hk and hk in reasoning.lower().replace(" ", ""):
                hole_leak_n += 1
        extra = found - allowed
        if extra:
            hallucination_n += 1

    m8_hallucination_rate = round(hallucination_n / max(checked_n, 1), 4)
    m8_hole_leak_rate = round(hole_leak_n / max(checked_n, 1), 4)

    return {
        "M1_bet_size_histogram": m1_hist,
        "M4_vpip_delta_post_bad_beat": m4_vpip_delta,
        "M7_mean_action_entropy": m7_mean_entropy,
        "M8_hallucination_rate": m8_hallucination_rate,
        "M8_hole_leak_rate": m8_hole_leak_rate,
        "M8_checked_decisions": checked_n,
        "M9_vpip_by_position": vpip_by_pos,
        "M9_positional_vpip_gap": m9_gap,
        "M9_positional_gap_label": m9_gap_label,
        "M9_btn_minus_utg_vpip": m9_gap,
    }


def evaluate_gates(
    manifest: dict[str, Any],
    thresholds: dict[str, float] | None = None,
) -> list[str]:
    """Return human-readable gate failures (empty = pass)."""
    thr = dict(DEFAULT_GATE_THRESHOLDS)
    if thresholds:
        thr.update(thresholds)

    failures: list[str] = []
    selfplay = manifest.get("selfplay") or {}
    arena = manifest.get("arena") or {}
    axes = selfplay.get("axes") or {}

    if axes:
        hall = float(axes.get("M8_hallucination_rate") or 0)
        if hall > thr["M8_hallucination_rate_max"]:
            failures.append(
                f"M8 hallucination_rate {hall:.4f} > max {thr['M8_hallucination_rate_max']}"
            )
        leak = float(axes.get("M8_hole_leak_rate") or 0)
        if leak > thr["M8_hole_leak_rate_max"]:
            failures.append(
                f"M8 hole_leak_rate {leak:.4f} > max {thr['M8_hole_leak_rate_max']}"
            )
        gap = float(
            axes.get("M9_positional_vpip_gap") or axes.get("M9_btn_minus_utg_vpip") or 0
        )
        gap_label = str(axes.get("M9_positional_gap_label") or "btn_minus_utg").replace(
            "_", "-"
        )
        if gap < thr["M9_btn_minus_utg_vpip_min"]:
            failures.append(
                f"M9 {gap_label} vpip gap {gap:.4f} < min {thr['M9_btn_minus_utg_vpip_min']}"
            )

    if arena.get("source") == "arena_export":
        hero_subs = int(arena.get("hero_submissions") or 0)
        if hero_subs < int(thr["hero_submissions_min"]):
            failures.append(
                f"hero_submissions {hero_subs} < min {int(thr['hero_submissions_min'])}"
            )

    return failures


def summarize_selfplay_trajectory(rows: list[dict]) -> dict[str, Any]:
    decisions = [r for r in rows if r.get("record_type") == "decision"]
    results = [r for r in rows if r.get("record_type") == "hand_result"]
    if not decisions:
        return {"source": "selfplay", "decision_count": 0}

    actions = Counter(str(d.get("action") or "").lower() for d in decisions)
    buckets = Counter(str(d.get("bet_size_bucket") or "none") for d in decisions)
    by_pos: dict[str, list[dict]] = defaultdict(list)
    for d in decisions:
        by_pos[str(d.get("position") or "?")].append(d)

    preflop = [d for d in decisions if d.get("street") == "Preflop"]
    preflop_folds_by_pos: dict[str, float] = {}
    for pos, pos_rows in by_pos.items():
        pf = [d for d in pos_rows if d.get("street") == "Preflop"]
        if not pf:
            continue
        folds = sum(1 for d in pf if str(d.get("action")).lower() == "fold")
        preflop_folds_by_pos[pos] = round(folds / len(pf), 4)

    voluntary_preflop = sum(
        1 for d in preflop
        if str(d.get("action")).lower() in _VPIP_ACTIONS
    )
    vpip_proxy = round(voluntary_preflop / max(len(preflop), 1), 4)
    pfr_proxy = round(
        sum(1 for d in preflop if str(d.get("action")).lower() in ("bet", "raise"))
        / max(len(preflop), 1),
        4,
    )
    reasoning_lens = [int(d.get("reasoning_len") or 0) for d in decisions]

    net = sum(int(r.get("chip_delta") or 0) for r in results)
    hands = len(results) or len({d.get("hand_id") for d in decisions})
    axes = compute_selfplay_axes(decisions, results)
    memory_gap = compute_memory_gap(decisions)

    return {
        "source": "selfplay",
        "decision_count": len(decisions),
        "hands": hands,
        "net_chips": net,
        "action_counts": dict(actions),
        "bet_size_buckets": dict(buckets),
        "preflop_fold_rate_by_position": preflop_folds_by_pos,
        "vpip_proxy": vpip_proxy,
        "pfr_proxy": pfr_proxy,
        "reasoning_len_mean": round(mean(reasoning_lens), 1) if reasoning_lens else 0,
        "reasoning_len_max": max(reasoning_lens) if reasoning_lens else 0,
        "n_players_mode": Counter(
            int(d.get("n_players") or 0) for d in decisions
        ).most_common(1)[0][0] if decisions else None,
        "axes": axes,
        "memory_gap": memory_gap,
    }


def summarize_arena_export(export_dir: Path, hero: str) -> dict[str, Any]:
    agents = _load_jsonl(export_dir / "agents.jsonl")
    tables = _load_jsonl(export_dir / "tables.jsonl")
    submissions = _load_jsonl(export_dir / "submissions.jsonl")
    hero_row = next(
        (a for a in agents if a.get("handle") == hero or a.get("name") == hero),
        None,
    )
    hero_stats = (hero_row or {}).get("stats") or {}
    player_counts = Counter(int(t.get("player_count") or 0) for t in tables)
    hu_tables = sum(1 for t in tables if int(t.get("player_count") or 0) == 2)
    hero_subs = [
        s for s in submissions
        if s.get("agent_handle") == hero
        or s.get("agent_id") and hero_row and s.get("agent_id") == hero_row.get("agent_id")
    ]
    if not hero_subs and hero_row:
        hero_id = hero_row.get("agent_id")
        hero_subs = [s for s in submissions if s.get("agent_id") == hero_id]
    payouts = [int(s.get("payout_chips") or 0) for s in hero_subs]
    chip_deltas = [
        int(s.get("chip_delta"))
        for s in hero_subs
        if s.get("chip_delta") is not None
    ]

    out: dict[str, Any] = {
        "source": "arena_export",
        "export_dir": str(export_dir),
        "hero": hero,
        "tables": len(tables),
        "hu_table_pct": round(hu_tables / max(len(tables), 1), 4),
        "player_count_distribution": dict(player_counts),
        "hero_submissions": len(hero_subs),
        "hero_pot_win_rate": round(
            sum(1 for p in payouts if p > 0) / max(len(payouts), 1), 4,
        ),
        "hero_vpip": hero_stats.get("vpip"),
        "hero_pfr": hero_stats.get("pfr"),
        "hero_adjusted_bb100": hero_row.get("adjusted_bb100") if hero_row else None,
        "hero_rank": hero_row.get("rank") if hero_row else None,
        "hero_hands": hero_row.get("hands") if hero_row else None,
    }
    if chip_deltas:
        out["hero_net_chips_replay"] = sum(chip_deltas)
    return out


def build_manifest(
    *,
    selfplay_summary: dict | None,
    arena_summary: dict | None,
    bundle_dir: Path,
) -> dict[str, Any]:
    manifest: dict[str, Any] = {
        "schema": "devfun.researcher_trajectory.v2",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "bundle_dir": str(bundle_dir),
        "selfplay": selfplay_summary,
        "arena": arena_summary,
    }
    # Include memory_gap block in axis_summary if available
    if selfplay_summary and "memory_gap" in selfplay_summary:
        manifest["memory_gap"] = selfplay_summary["memory_gap"]
    manifest["gate_failures"] = evaluate_gates(manifest)
    manifest["gate_pass"] = not manifest["gate_failures"]
    return manifest


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Researcher Round axis proxy summary")
    p.add_argument("--selfplay", type=Path, default=None, help="selfplay trajectory JSONL")
    p.add_argument("--export-dir", type=Path, default=None, help="Arena export directory")
    p.add_argument("--hero", default="cemini_wiki_poker")
    p.add_argument(
        "--out-dir",
        type=Path,
        default=None,
        help="Write axis_summary.json + manifest.json (default: parent of selfplay or export-dir)",
    )
    p.add_argument(
        "--gate",
        action="store_true",
        help="Exit 1 if axis / hero_submission gates fail",
    )
    args = p.parse_args(argv)

    if not args.selfplay and not args.export_dir:
        print("ERROR: pass --selfplay and/or --export-dir", file=sys.stderr)
        return 2

    selfplay_summary = None
    if args.selfplay:
        selfplay_summary = summarize_selfplay_trajectory(_load_jsonl(args.selfplay))

    arena_summary = None
    if args.export_dir:
        arena_summary = summarize_arena_export(args.export_dir, args.hero)

    out_dir = args.out_dir
    if out_dir is None:
        if args.selfplay:
            out_dir = args.selfplay.parent
        elif args.export_dir:
            out_dir = args.export_dir
        else:
            out_dir = Path("reports/researcher-round")

    out_dir.mkdir(parents=True, exist_ok=True)
    manifest = build_manifest(
        selfplay_summary=selfplay_summary,
        arena_summary=arena_summary,
        bundle_dir=out_dir,
    )
    (out_dir / "axis_summary.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (out_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    index_path = Path("reports/hl-loop/researcher_trajectory_index.jsonl")
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_row = {
        "at": manifest["generated_at"],
        "bundle_dir": str(out_dir),
        "selfplay_decisions": (selfplay_summary or {}).get("decision_count"),
        "arena_tables": (arena_summary or {}).get("tables"),
        "vpip_proxy": (selfplay_summary or {}).get("vpip_proxy"),
        "bb100": (arena_summary or {}).get("hero_adjusted_bb100"),
        "gate_pass": manifest.get("gate_pass"),
    }
    with index_path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(index_row, sort_keys=True) + "\n")

    print(f"[trajectory] axis_summary → {out_dir / 'axis_summary.json'}")
    if selfplay_summary:
        axes = (selfplay_summary.get("axes") or {})
        print(
            f"  selfplay: {selfplay_summary.get('decision_count')} decisions "
            f"vpip_proxy={selfplay_summary.get('vpip_proxy')} "
            f"pfr_proxy={selfplay_summary.get('pfr_proxy')} "
            f"M8_hall={axes.get('M8_hallucination_rate')} "
            f"M9_gap={axes.get('M9_btn_minus_utg_vpip')}"
        )
    if arena_summary:
        print(
            f"  arena: tables={arena_summary.get('tables')} "
            f"hero_subs={arena_summary.get('hero_submissions')} "
            f"rank={arena_summary.get('hero_rank')} "
            f"bb100={arena_summary.get('hero_adjusted_bb100')}"
        )

    failures = manifest.get("gate_failures") or []
    if failures:
        print("[trajectory] GATE FAILURES:", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
    else:
        print("[trajectory] gates: PASS")

    if args.gate and failures:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
