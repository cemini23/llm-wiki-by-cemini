#!/usr/bin/env python3
"""Run PM LP spread sweep and write HTML report."""
from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

# Allow imports from scripts/
_SCRIPTS = Path(__file__).resolve().parents[1]
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from cemini_backtest_report import ReportConfig, generate_report  # noqa: E402

from pm_lp_backtest.engine import LpParams, run_lp_backtest  # noqa: E402
from pm_lp_backtest.fetch import load_market_series  # noqa: E402
from pm_lp_backtest.metrics import (  # noqa: E402
    compute_metrics,
    per_segment_summary,
    trades_to_equity,
)
from pm_lp_backtest.sweep import FULL_GRID, QUICK_GRID, run_sweep  # noqa: E402

WORKSPACE = Path(__file__).resolve().parents[2]
DEFAULT_OUT = WORKSPACE / ".local" / "reports"


def _fmt_cfg(row) -> str:
    return (
        f"spread {row['spread_cents']:.0f}¢ · "
        f"reward×{row['reward_scale']:.1f} · "
        f"adverse×{row.get('adverse_multiplier', 1):.1f}"
    )


def main() -> int:
    p = argparse.ArgumentParser(description="Polymarket LP spread backtest pilot")
    p.add_argument("--markets", type=int, default=12, help="Top markets by 24h volume")
    p.add_argument("--min-volume", type=float, default=5000.0, help="Gamma volume24hr floor")
    p.add_argument("--quick", action="store_true", help="Smaller parameter grid")
    p.add_argument("--refresh", action="store_true", help="Refetch CLOB history")
    p.add_argument(
        "--output",
        type=Path,
        default=None,
        help="HTML output path (default .local/reports/pm-lp-backtest-YYYY-MM-DD.html)",
    )
    args = p.parse_args()

    cache_dir = DEFAULT_OUT / "pm-lp-backtest" / "cache"
    print(f"Loading {args.markets} markets (min vol {args.min_volume:,.0f})…")
    markets = load_market_series(
        limit=args.markets,
        min_volume24hr=args.min_volume,
        cache_dir=cache_dir,
        refresh=args.refresh,
    )
    if not markets:
        print("No markets with sufficient history.", file=sys.stderr)
        return 1

    grid = QUICK_GRID if args.quick else FULL_GRID
    print(f"Running sweep ({len(list(__import__('itertools').product(*grid.values())))} combos)…")
    sweep_df = run_sweep(markets, grid=grid)
    elapsed = sweep_df.attrs.get("elapsed_sec", 0)
    print(f"Sweep done in {elapsed:.1f}s — {len(sweep_df)} rows")

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
        f"Bars: hourly CLOB prices-history\n"
        f"Combos: {len(sweep_df)}"
    )

    out = args.output or (
        DEFAULT_OUT / f"pm-lp-backtest-{date.today().isoformat()}.html"
    )
    sweep_csv = out.with_suffix(".sweep.csv")
    sweep_df.to_csv(sweep_csv, index=False)
    print(f"Sweep CSV: {sweep_csv}")

    config = ReportConfig(
        title="Polymarket LP Spread — Backtest Report",
        subtitle="Shadow simulator · reward proxy · hourly CLOB mids",
        param_cols=["spread_cents", "reward_scale", "adverse_multiplier"],
        format_config=_fmt_cfg,
        heatmap_pairs=[
            ("spread_cents", "reward_scale", "sharpe_annual", "", "RdYlGn"),
            ("spread_cents", "reward_scale", "total_pnl_usd", "", "RdYlGn"),
            ("spread_cents", "adverse_multiplier", "total_pnl_usd", "", "Viridis"),
            ("spread_cents", "reward_scale", "n_trades", "", "Blues"),
        ],
        disclaimer_html=(
            "<strong>Disclaimer:</strong> LP reward accrual uses an inverse-spread "
            "<em>proxy</em>, not Polymarket’s on-chain LP scoring. Adverse fills are "
            "modeled as hourly mid crosses through quoted bid/ask. Use for parameter "
            "sensitivity only — validate in shadow-live before any prod brief."
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
