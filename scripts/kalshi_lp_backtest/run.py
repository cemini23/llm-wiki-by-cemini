#!/usr/bin/env python3
"""Run Kalshi LP spread sweep and write HTML report."""
from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parents[1]
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from cemini_backtest_report import ReportConfig, generate_report

from kalshi_lp_backtest.engine import LpParams, run_lp_backtest
from kalshi_lp_backtest.fetch import load_market_series
from kalshi_lp_backtest.sweep import FULL_GRID, QUICK_GRID, run_sweep
from pm_lp_backtest.metrics import (
    compute_metrics,
    per_segment_summary,
    trades_to_equity,
)

WORKSPACE = Path(__file__).resolve().parents[2]
DEFAULT_OUT = WORKSPACE / ".local" / "reports"


def _fmt_cfg(row) -> str:
    return (
        f"spread {row['spread_cents']:.0f}¢ · "
        f"reward×{row['reward_scale']:.1f} · "
        f"adverse×{row.get('adverse_multiplier', 1):.1f}"
    )


def main() -> int:
    p = argparse.ArgumentParser(description="Kalshi LP spread backtest pilot")
    p.add_argument("--markets", type=int, default=12)
    p.add_argument("--min-volume", type=float, default=500.0)
    p.add_argument("--lookback-days", type=int, default=30)
    p.add_argument("--min-bars", type=int, default=24)
    p.add_argument("--quick", action="store_true")
    p.add_argument("--refresh", action="store_true")
    p.add_argument("--output", type=Path, default=None)
    args = p.parse_args()

    cache_dir = DEFAULT_OUT / "kalshi-lp-backtest" / "cache"
    print(
        f"Loading {args.markets} Kalshi markets "
        f"(min 24h vol ${args.min_volume:,.0f}, {args.lookback_days}d lookback)…"
    )
    markets = load_market_series(
        limit=args.markets,
        min_volume24hr=args.min_volume,
        lookback_days=args.lookback_days,
        min_bars=args.min_bars,
        cache_dir=cache_dir,
        refresh=args.refresh,
    )
    if not markets:
        print("No markets with sufficient history.", file=sys.stderr)
        return 1

    grid = QUICK_GRID if args.quick else FULL_GRID
    print("Running sweep…")
    sweep_df = run_sweep(markets, grid=grid)
    print(f"Sweep done — {len(sweep_df)} rows")

    best_idx = sweep_df["sharpe_annual"].idxmax()
    best_row = sweep_df.loc[best_idx]
    params = LpParams(
        spread_cents=float(best_row["spread_cents"]),
        reward_scale=float(best_row["reward_scale"]),
        adverse_multiplier=float(best_row["adverse_multiplier"]),
    )
    best_trades = run_lp_backtest(markets, params)
    best_eq = trades_to_equity(best_trades)
    per_seg = per_segment_summary(best_trades, "segment")

    t_min = min(m.prices["ts"].min() for m in markets)
    t_max = max(m.prices["ts"].max() for m in markets)
    data_summary = (
        f"Markets: {len(markets)}\n"
        f"Window: {t_min.date()} → {t_max.date()} (UTC)\n"
        f"Bars: hourly candlesticks (trade fallback)\n"
        f"API: api.elections.kalshi.com\n"
        f"Combos: {len(sweep_df)}"
    )

    out = args.output or (
        DEFAULT_OUT / f"kalshi-lp-backtest-{date.today().isoformat()}.html"
    )
    sweep_df.to_csv(out.with_suffix(".sweep.csv"), index=False)

    config = ReportConfig(
        title="Kalshi LP Spread — Backtest Report",
        subtitle="Shadow simulator · reward proxy · Kalshi trade-api v2",
        param_cols=["spread_cents", "reward_scale", "adverse_multiplier"],
        format_config=_fmt_cfg,
        heatmap_pairs=[
            ("spread_cents", "reward_scale", "sharpe_annual", "", "RdYlGn"),
            ("spread_cents", "reward_scale", "total_pnl_usd", "", "RdYlGn"),
            ("spread_cents", "adverse_multiplier", "total_pnl_usd", "", "Viridis"),
            ("spread_cents", "reward_scale", "n_trades", "", "Blues"),
        ],
        disclaimer_html=(
            "<strong>Disclaimer:</strong> Kalshi LP reward uses the same inverse-spread "
            "<em>proxy</em> as the PM pilot, not exchange incentive formulas. "
            "Short-dated sports markets dominate volume — treat as spread-sensitivity "
            "lab, not production P&amp;L forecast."
        ),
    )

    path = generate_report(
        config,
        sweep_df,
        best_trades,
        best_eq,
        per_seg,
        data_summary,
        out,
    )
    print(f"Report: {path}")
    print(f"file://{path.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
