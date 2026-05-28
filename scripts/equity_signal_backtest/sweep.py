"""Momentum parameter grid."""
from __future__ import annotations

import itertools
import time
from typing import Dict, List

import pandas as pd

from backtest_common.metrics import compute_metrics

from .engine import MomParams, run_momentum_backtest
from .fetch import SymbolSeries

QUICK_GRID: Dict[str, List] = {
    "lookback": [10, 20, 50],
    "entry_z": [0.5, 1.0, 1.5],
    "stop_loss_pct": [3.0, 5.0, 8.0],
}

FULL_GRID: Dict[str, List] = {
    "lookback": [10, 20, 30, 50],
    "entry_z": [0.5, 1.0, 1.5, 2.0],
    "stop_loss_pct": [3.0, 5.0, 8.0, 10.0],
}


def run_sweep(
    symbols: List[SymbolSeries],
    grid: Dict[str, List] | None = None,
    notional_usd: float = 1000.0,
) -> pd.DataFrame:
    grid = grid or QUICK_GRID
    keys = list(grid.keys())
    rows = []
    t0 = time.time()
    for combo in itertools.product(*[grid[k] for k in keys]):
        params_dict = dict(zip(keys, combo))
        params = MomParams(
            lookback=int(params_dict["lookback"]),
            entry_z=float(params_dict["entry_z"]),
            exit_z=0.0,
            stop_loss_pct=float(params_dict["stop_loss_pct"]),
            notional_usd=notional_usd,
        )
        trades = run_momentum_backtest(symbols, params)
        metrics = compute_metrics(
            trades, initial_capital=10_000.0, periods_per_year=252
        )
        rows.append({**params_dict, "exit_z": 0.0, **metrics})
    df = pd.DataFrame(rows)
    df.attrs["elapsed_sec"] = time.time() - t0
    return df
