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
from export_bundle import crawl_progress, load_export_agents_with_bb100, load_export_submissions  # noqa: E402


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
    agents = load_export_agents_with_bb100(export_dir)
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

    hero_adj = hero_row.get("adjusted_bb100")
    agents_with_bb = [a for a in agents if a.get("adjusted_bb100") is not None]
    ev_rank = None
    chip_rank = hero_row.get("rank")
    if hero_adj is not None and agents_with_bb:
        by_ev = sorted(
            agents_with_bb,
            key=lambda a: float(a.get("adjusted_bb100") or 0),
            reverse=True,
        )
        for i, a in enumerate(by_ev, start=1):
            if a.get("handle") == args.hero:
                ev_rank = i
                break

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
        "adjusted_bb100": hero_adj,
        "ev_rank_among_export": ev_rank,
        "chip_rank": chip_rank,
        "chip_vs_ev_rank_delta": (
            (chip_rank - ev_rank) if chip_rank and ev_rank else None
        ),
        "chip_accumulation_proxy": chip_proxy,
        "hero_submissions": hero_sub,
        "field_top20_avg_vpip": round(mean(vpip_nums), 4) if vpip_nums else None,
        "field_top20_avg_pfr": round(mean(pfr_nums), 4) if pfr_nums else None,
        "field_top20_median_vpip": round(median(vpip_nums), 4) if vpip_nums else None,
        "agents_in_export": len(agents),
        "submission_rows": len(submissions),
        "crawl_progress": crawl,
        "v2_v3_readiness": {
            "playground_rank_metric": (
                "totalChips (qualification) + adjustedBbPer100 (UI test column, ephemeral S1a)"
                if hero_adj is not None
                else "totalChips; bb/100 from UI snapshot if bb100_ui_snapshot.json present"
            ),
            "adjusted_bb100_visible": hero_adj is not None,
            "adjusted_bb100_source": hero_row.get("adjusted_bb100_source", "api_or_snapshot"),
            "ui_snapshot_note": (
                "S1a column was brief UI test — not sortable, removed same session. "
                "See tests/fixtures/bb100_ui_snapshot_s1a_2026-06-08.json"
                if (export_dir / "bb100_ui_snapshot.json").is_file()
                or hero_row.get("adjusted_bb100_source") == "ui_snapshot"
                else None
            ),
            "street_actions_in_export": False,
            "replay_chip_delta_cap": 50,
            "risk": (
                "Chip #1 may trail EV leaders on adjusted bb/100 — "
                "0xJeff_ai-style LAGs can rank higher on EV with fewer chips"
                if hero_adj is not None
                else "Chip #1 with 10% VPIP may underperform when scoring switches to "
                "all-in EV / AIVAT — need replay-backed leak audit + eval-style self-play"
            ),
            "mitigations": [
                "Refresh agents.jsonl export to capture leaderboard adjusted_bb100",
                "Tier-2 crawl: full-field stats + submissions-all",
                "Gap audit: compare chip rank vs adjusted bb/100 rank side-by-side",
                "HL patches for structural leaks; do not widen for vanity EV",
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
    if hero_adj is not None:
        print(f"  Adjusted bb/100 (leaderboard): {hero_adj:+.1f}")
        if ev_rank and chip_rank:
            print(f"  Chip rank #{chip_rank} vs EV rank #{ev_rank} among export")
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
