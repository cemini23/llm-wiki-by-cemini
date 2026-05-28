#!/usr/bin/env python3
"""Equity momentum sweep → HTML report (ArcticDB via SSH)."""
from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parents[1]
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from backtest_common.mcpt_gate import mcpt
from backtest_common.metrics import per_segment_summary, trades_to_equity
from cemini_backtest_report import ReportConfig, generate_report

from equity_signal_backtest.engine import MomParams, run_momentum_backtest
from equity_signal_backtest.fetch import DEFAULT_SYMBOLS, load_symbol_series
from equity_signal_backtest.sweep import FULL_GRID, QUICK_GRID, run_sweep

WORKSPACE = Path(__file__).resolve().parents[2]
DEFAULT_OUT = WORKSPACE / ".local" / "reports"


def _fmt_cfg(row) -> str:
    return (
        f"lookback {int(row['lookback'])}d · "
        f"entry z≥{row['entry_z']:.1f} · "
        f"SL {row['stop_loss_pct']:.0f}%"
    )


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--symbols", nargs="*", default=list(DEFAULT_SYMBOLS))
    p.add_argument("--lookback-years", type=int, default=5)
    p.add_argument("--quick", action="store_true")
    p.add_argument("--refresh", action="store_true")
    p.add_argument("--output", type=Path, default=None)
    args = p.parse_args()

    cache = DEFAULT_OUT / "equity-signal-backtest" / "cache"
    print(f"Loading {len(args.symbols)} symbols from librarian ArcticDB…")
    symbols = load_symbol_series(
        args.symbols,
        lookback_years=args.lookback_years,
        cache_dir=cache,
        refresh=args.refresh,
    )
    if not symbols:
        print("No symbol series loaded (SSH/arctic?).", file=sys.stderr)
        return 1

    grid = QUICK_GRID if args.quick else FULL_GRID
    sweep_df = run_sweep(symbols, grid=grid)
    print(f"Sweep: {len(sweep_df)} rows")

    best_idx = sweep_df["sharpe_annual"].idxmax()
    best_row = sweep_df.loc[best_idx]
    params = MomParams(
        lookback=int(best_row["lookback"]),
        entry_z=float(best_row["entry_z"]),
        stop_loss_pct=float(best_row["stop_loss_pct"]),
    )
    best_trades = run_momentum_backtest(symbols, params)
    mcpt_res = mcpt(best_trades["net_pnl_pct"].values) if len(best_trades) else {}
    best_eq = trades_to_equity(best_trades)
    per_seg = per_segment_summary(best_trades, "segment")

    t_min = min(s.prices["ts"].min() for s in symbols)
    t_max = max(s.prices["ts"].max() for s in symbols)
    mcpt_line = ""
    if mcpt_res:
        mcpt_line = (
            f"\nMCPT (best config): p={mcpt_res.get('p_value', 1):.4f} "
            f"pass@5%={mcpt_res.get('pass_5pct', False)}"
        )
    data_summary = (
        f"Symbols: {len(symbols)} ({', '.join(s.symbol for s in symbols)})\n"
        f"Window: {t_min.date()} → {t_max.date()} (UTC)\n"
        "Source: librarian ArcticDB / equity_bars\n"
        f"Combos: {len(sweep_df)}{mcpt_line}"
    )

    out = args.output or (
        DEFAULT_OUT / f"equity-signal-backtest-{date.today().isoformat()}.html"
    )
    sweep_df.to_csv(out.with_suffix(".sweep.csv"), index=False)
    if len(best_trades):
        best_trades.to_csv(out.with_suffix(".trades.csv"), index=False)

    config = ReportConfig(
        title="Equity Momentum — Backtest Report",
        subtitle="Daily z-score vs rolling mean · ArcticDB equity_bars (librarian)",
        param_cols=["lookback", "entry_z", "stop_loss_pct"],
        format_config=_fmt_cfg,
        heatmap_pairs=[
            ("lookback", "entry_z", "sharpe_annual", "", "RdYlGn"),
            ("lookback", "entry_z", "total_pnl_usd", "", "RdYlGn"),
            ("lookback", "stop_loss_pct", "total_pnl_usd", "", "Viridis"),
            ("entry_z", "stop_loss_pct", "n_trades", "", "Blues"),
        ],
        disclaimer_html=(
            "<strong>Disclaimer:</strong> Daily bars from migrated Kaggle-style "
            "OHLCV (may end ~2017 for some tickers). Momentum z-score is a "
            "<em>sanity lab</em> — run VR test + MCPT before any prod signal brief."
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
