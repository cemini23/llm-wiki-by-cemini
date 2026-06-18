#!/usr/bin/env python3
"""Multi-axis proxy summary for Researcher Round trajectory exports.

Reads selfplay trajectory JSONL or Arena export bundles and writes
axis_summary.json for Discord / researcher contribution narrative.

Usage:
    uv run python examples/researcher_trajectory_summary.py \\
        --selfplay reports/researcher-round/.../selfplay_trajectory.jsonl
    uv run python examples/researcher_trajectory_summary.py \\
        --export-dir reports/exports/<compId>/<ts>
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean
from typing import Any

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))


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
        if str(d.get("action")).lower() in ("call", "bet", "raise", "all-in")
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
    ]
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
    return {
        "schema": "devfun.researcher_trajectory.v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "bundle_dir": str(bundle_dir),
        "selfplay": selfplay_summary,
        "arena": arena_summary,
    }


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
    }
    with index_path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(index_row, sort_keys=True) + "\n")

    print(f"[trajectory] axis_summary → {out_dir / 'axis_summary.json'}")
    if selfplay_summary:
        print(
            f"  selfplay: {selfplay_summary.get('decision_count')} decisions "
            f"vpip_proxy={selfplay_summary.get('vpip_proxy')} "
            f"pfr_proxy={selfplay_summary.get('pfr_proxy')}"
        )
    if arena_summary:
        print(
            f"  arena: tables={arena_summary.get('tables')} "
            f"rank={arena_summary.get('hero_rank')} "
            f"bb100={arena_summary.get('hero_adjusted_bb100')}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
