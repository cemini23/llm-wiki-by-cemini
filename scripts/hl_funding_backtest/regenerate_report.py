#!/usr/bin/env python3
"""Regenerate HL funding HTML from sweep parquet using cemini_backtest_report."""
from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parents[1]
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

import pandas as pd

from backtest_common.metrics import per_segment_summary, trades_to_equity
from cemini_backtest_report import ReportConfig, generate_report

WORKSPACE = Path(__file__).resolve().parents[2]
DEFAULT_REF = WORKSPACE / ".local" / "tools" / "hl-funding-sniper-reference"


def _fmt_cfg(row) -> str:
    return (
        f"funding≥{row.get('min_funding_apr_pct', 0):.0f}% · "
        f"|z|≥{row.get('min_funding_zscore', 0):.1f} · "
        f"TP {row.get('take_profit_pct', 0):.0f}% / "
        f"SL {row.get('stop_loss_pct', 0):.0f}%"
    )


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--sweep",
        type=Path,
        default=DEFAULT_REF / "data" / "cache" / "sweep_results.parquet",
    )
    p.add_argument(
        "--trades",
        type=Path,
        default=DEFAULT_REF / "data" / "cache" / "best_trades.parquet",
    )
    p.add_argument(
        "--equity",
        type=Path,
        default=DEFAULT_REF / "data" / "cache" / "best_equity.parquet",
    )
    p.add_argument(
        "--per-coin",
        type=Path,
        default=DEFAULT_REF / "data" / "cache" / "per_coin.parquet",
    )
    p.add_argument("--data-summary", type=str, default="HL Dune backtest (regenerated)")
    p.add_argument("--output", type=Path, default=None)
    args = p.parse_args()

    if not args.sweep.exists():
        print(f"Missing sweep file: {args.sweep}", file=sys.stderr)
        return 1

    sweep_df = pd.read_parquet(args.sweep)
    best_trades = pd.read_parquet(args.trades) if args.trades.exists() else pd.DataFrame()
    best_eq = (
        pd.read_parquet(args.equity)
        if args.equity.exists()
        else trades_to_equity(best_trades)
    )
    per_seg = (
        pd.read_parquet(args.per_coin)
        if args.per_coin.exists()
        else per_segment_summary(best_trades, "coin")
    )
    if "coin" in per_seg.columns and "segment" not in per_seg.columns:
        per_seg = per_seg.rename(columns={"coin": "segment"})

    param_cols = [
        c
        for c in [
            "min_funding_apr_pct",
            "min_funding_zscore",
            "persistence_hours",
            "take_profit_pct",
            "stop_loss_pct",
            "timeout_hours",
            "funding_apr_exit_threshold_ratio",
        ]
        if c in sweep_df.columns
    ]

    out = args.output or (
        WORKSPACE
        / ".local"
        / "reports"
        / f"hl-funding-backtest-{date.today().isoformat()}.html"
    )

    config = ReportConfig(
        title="HL Funding Sniper — Backtest Report",
        subtitle="Regenerated via cemini_backtest_report (shared kit)",
        param_cols=param_cols,
        format_config=_fmt_cfg,
        segment_col="segment" if "segment" in (best_trades.columns if len(best_trades) else []) else "coin",
        heatmap_pairs=[
            ("min_funding_apr_pct", "min_funding_zscore", "sharpe_annual", "", "RdYlGn"),
            ("min_funding_apr_pct", "min_funding_zscore", "total_pnl_usd", "", "RdYlGn"),
            ("take_profit_pct", "stop_loss_pct", "total_pnl_usd", " (TP>SL)", "RdYlGn"),
        ],
    )
    path = generate_report(
        config, sweep_df, best_trades, best_eq, per_seg, args.data_summary, out
    )
    print(path)
    print(f"file://{path.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
