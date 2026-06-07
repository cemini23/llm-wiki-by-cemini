#!/usr/bin/env python3
"""Competition metrics report — chip proxies, VPIP field, V2/V3 readiness gaps.

Playground ranks on totalChips, not adjustedBbPer100. Submissions export
payout_chips = pot won (≥0), not chipDelta — use replays or participant
status for hero EV proxies.

Usage:
    uv run python examples/competition_metrics_report.py reports/exports/playground-s1-live/
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from statistics import mean, median

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from competition_field_report import _dedupe_agents, _load_jsonl  # noqa: E402
from export_bundle import crawl_progress, load_export_agents, load_export_submissions  # noqa: E402


def _participant_bb100(
    *,
    total_chips: int,
    initial_chips: int,
    hands: int,
    big_blind: int = 20,
) -> dict[str, float]:
    net = total_chips - initial_chips
    if hands <= 0:
        return {"net_chips": net, "chips_per_hand": 0.0, "bb100_chip_proxy": 0.0}
    cph = net / hands
    bb100 = (net / big_blind) / hands * 100
    return {"net_chips": net, "chips_per_hand": cph, "bb100_chip_proxy": bb100}


def _hero_from_submissions(submissions: list[dict], handle: str) -> dict:
    rows = [r for r in submissions if r.get("agent_handle") == handle]
    payouts = [int(r.get("payout_chips") or 0) for r in rows]
    wins = sum(1 for p in payouts if p > 0)
    return {
        "submission_rows": len(rows),
        "pot_wins": wins,
        "win_rate_pot": round(wins / max(len(rows), 1), 4),
        "note": "payout_chips is pot won (≥0), not chipDelta — cannot compute bb/100 from this alone",
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Competition metrics + V2/V3 readiness report")
    p.add_argument("export_dir", type=Path)
    p.add_argument("--hero", default="cemini_wiki_poker")
    p.add_argument("--initial-chips", type=int, default=1000)
    p.add_argument("--big-blind", type=int, default=20)
    args = p.parse_args(argv)

    export_dir = args.export_dir
    agents = load_export_agents(export_dir)
    submissions = load_export_submissions(export_dir)

    hero_row = next((a for a in agents if a.get("handle") == args.hero), None)
    if not hero_row:
        print(f"No hero {args.hero} in agents.jsonl", file=sys.stderr)
        return 1

    chips = int(hero_row.get("chips") or 0)
    hands = int(hero_row.get("hands") or 0)
    stats = hero_row.get("stats") or {}
    chip_proxy = _participant_bb100(
        total_chips=chips,
        initial_chips=args.initial_chips,
        hands=hands,
        big_blind=args.big_blind,
    )
    hero_sub = _hero_from_submissions(submissions, args.hero)

    top20 = agents[:20]
    vpip_nums = [
        v for v in ((a.get("stats") or {}).get("vpip") for a in top20)
        if isinstance(v, (int, float))
    ]
    pfr_nums = [
        v for v in ((a.get("stats") or {}).get("pfr") for a in top20)
        if isinstance(v, (int, float))
    ]

    crawl = crawl_progress(export_dir)

    report = {
        "export_dir": str(export_dir),
        "hero": args.hero,
        "rank": hero_row.get("rank"),
        "chips": chips,
        "hands": hands,
        "vpip": stats.get("vpip"),
        "pfr": stats.get("pfr"),
        "three_bet_pct": stats.get("three_bet_pct"),
        "playing_style": stats.get("playing_style"),
        "chip_accumulation_proxy": chip_proxy,
        "hero_submissions": hero_sub,
        "field_top20_avg_vpip": round(mean(vpip_nums), 4) if vpip_nums else None,
        "field_top20_avg_pfr": round(mean(pfr_nums), 4) if pfr_nums else None,
        "field_top20_median_vpip": round(median(vpip_nums), 4) if vpip_nums else None,
        "agents_in_export": len(agents),
        "submission_rows": len(submissions),
        "crawl_progress": crawl,
        "v2_v3_readiness": {
            "playground_rank_metric": "totalChips (not adjustedBbPer100)",
            "adjusted_bb100_visible": False,
            "street_actions_in_export": False,
            "replay_chip_delta_cap": 50,
            "risk": (
                "Chip #1 with 10% VPIP may underperform when scoring switches to "
                "all-in EV / AIVAT — need replay-backed leak audit + eval-style self-play"
            ),
            "mitigations": [
                "Tier-1 hourly: recent-tables + top-200 submissions (live)",
                "Tier-2 nightly: full-field stats + batched submissions-all crawl",
                "Tier-3 selective: replay URLs for HL worst-15 table IDs only",
                "Track participant totalChips/hands as chip proxy; do not confuse with EV bb/100",
            ],
        },
    }

    print("=== Competition metrics ===\n")
    print(f"Hero #{report['rank']} {args.hero}: {chips:,} chips / {hands:,} hands")
    print(
        f"  VPIP {stats.get('vpip')}  PFR {stats.get('pfr')}  "
        f"style {stats.get('playing_style')}"
    )
    print(
        f"  Chip proxy bb/100: {chip_proxy['bb100_chip_proxy']:.1f} "
        f"(net {chip_proxy['net_chips']:,} chips — NOT all-in EV)"
    )
    print(
        f"  Pot win rate (submissions): {hero_sub['win_rate_pot']:.1%} "
        f"({hero_sub['pot_wins']}/{hero_sub['submission_rows']} rows)"
    )
    print(
        f"\nField top-20 avg VPIP {report['field_top20_avg_vpip']} / "
        f"PFR {report['field_top20_avg_pfr']}"
    )
    print(f"Export: {len(agents)} agents, {len(submissions)} submission rows")
    if crawl:
        total = crawl.get("leaderboard_total") or "?"
        done = len(crawl.get("completed_agent_ids") or [])
        print(f"Crawl: {done}/{total} agents, cycles {crawl.get('cycles', 0)}")
    print("\n=== V2/V3 readiness ===")
    for line in report["v2_v3_readiness"]["mitigations"]:
        print(f"  • {line}")
    print(f"\nRisk: {report['v2_v3_readiness']['risk']}")

    out_path = export_dir / "metrics_report.json"
    out_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nWrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
