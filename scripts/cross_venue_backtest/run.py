#!/usr/bin/env python3
"""PM × Kalshi divergence sweep → HTML report."""
from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parents[1]
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from backtest_common.metrics import per_segment_summary, trades_to_equity
from cemini_backtest_report import ReportConfig, generate_report

from cross_venue_backtest.engine import ArbParams, run_arb_backtest
from cross_venue_backtest.fetch import load_venue_pairs
from cross_venue_backtest.sweep import FULL_GRID, QUICK_GRID, run_sweep

WORKSPACE = Path(__file__).resolve().parents[2]
DEFAULT_OUT = WORKSPACE / ".local" / "reports"


def _fmt_cfg(row) -> str:
    return (
        f"edge≥{row['min_edge_cents']:.0f}¢ · "
        f"latency+{row['latency_penalty_cents']:.1f}¢ · "
        f"hold≤{int(row['max_hold_hours'])}h"
    )


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--quick", action="store_true")
    p.add_argument("--refresh", action="store_true")
    p.add_argument("--min-bars", type=int, default=4)
    p.add_argument("--output", type=Path, default=None)
    args = p.parse_args()

    cache = DEFAULT_OUT / "cross-venue-backtest" / "cache"
    print("Loading PM + Kalshi BTC pair…")
    pairs = load_venue_pairs(cache, refresh=args.refresh, min_bars=args.min_bars)
    if not pairs:
        print("No aligned pair (check PM/Kalshi BTC markets).", file=sys.stderr)
        return 1

    grid = QUICK_GRID if args.quick else FULL_GRID
    sweep_df = run_sweep(pairs, grid=grid)
    best_idx = sweep_df["sharpe_annual"].idxmax()
    best_row = sweep_df.loc[best_idx]
    params = ArbParams(
        min_edge_cents=float(best_row["min_edge_cents"]),
        latency_penalty_cents=float(best_row["latency_penalty_cents"]),
        max_hold_hours=int(best_row["max_hold_hours"]),
    )
    best_trades = run_arb_backtest(pairs, params)
    best_eq = trades_to_equity(best_trades)
    per_seg = per_segment_summary(best_trades, "segment")

    pair = pairs[0]
    df = pair.aligned
    data_summary = (
        f"Pair: {pair.pair_id}\n"
        f"PM: {pair.pm_slug}\n"
        f"Kalshi: {pair.kalshi_ticker}\n"
        f"Bars: {len(df)} hourly ({df['ts'].min().date()} → {df['ts'].max().date()})\n"
        f"Combos: {len(sweep_df)}"
    )

    out = args.output or (
        DEFAULT_OUT / f"cross-venue-backtest-{date.today().isoformat()}.html"
    )
    sweep_df.to_csv(out.with_suffix(".sweep.csv"), index=False)

    config = ReportConfig(
        title="PM × Kalshi Divergence — Backtest Report",
        subtitle="Hourly mid spread · convergence proxy (not atomic dual-fill)",
        param_cols=["min_edge_cents", "latency_penalty_cents", "max_hold_hours"],
        format_config=_fmt_cfg,
        heatmap_pairs=[
            ("min_edge_cents", "latency_penalty_cents", "sharpe_annual", "", "RdYlGn"),
            ("min_edge_cents", "max_hold_hours", "total_pnl_usd", "", "RdYlGn"),
            ("latency_penalty_cents", "max_hold_hours", "n_trades", "", "Blues"),
        ],
        disclaimer_html=(
            "<strong>Disclaimer:</strong> This is a <em>convergence lab</em> on "
            "hourly mids — not fill-realistic cross-venue execution. "
            "Comparable-event matching is BTC-proxy only. "
            "Use @concepts/cross-venue-arbitrage-pattern.md + hftbacktest before prod."
        ),
    )
    path = generate_report(
        config, sweep_df, best_trades, best_eq, per_seg, data_summary, out
    )
    print(f"Report: {path}")
    print(f"file://{path.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
