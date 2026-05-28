"""Cross-venue arb parameter grid."""
from __future__ import annotations

import itertools
import time
from typing import Dict, List

import pandas as pd

from backtest_common.metrics import compute_metrics

from .engine import ArbParams, run_arb_backtest
from .fetch import VenuePair

QUICK_GRID: Dict[str, List] = {
    "min_edge_cents": [2, 3, 5],
    "latency_penalty_cents": [0.5, 1.0, 2.0],
    "max_hold_hours": [6, 12, 24],
}

FULL_GRID: Dict[str, List] = {
    "min_edge_cents": [2, 3, 4, 5, 6],
    "latency_penalty_cents": [0.5, 1.0, 1.5, 2.0],
    "max_hold_hours": [6, 12, 24, 48],
}


def run_sweep(
    pairs: List[VenuePair],
    grid: Dict[str, List] | None = None,
    notional_usd: float = 100.0,
) -> pd.DataFrame:
    grid = grid or QUICK_GRID
    keys = list(grid.keys())
    rows = []
    t0 = time.time()
    for combo in itertools.product(*[grid[k] for k in keys]):
        d = dict(zip(keys, combo))
        params = ArbParams(
            min_edge_cents=float(d["min_edge_cents"]),
            latency_penalty_cents=float(d["latency_penalty_cents"]),
            max_hold_hours=int(d["max_hold_hours"]),
            notional_usd=notional_usd,
        )
        trades = run_arb_backtest(pairs, params)
        metrics = compute_metrics(trades, initial_capital=1000.0, periods_per_year=252 * 24)
        rows.append({**d, **metrics})
    df = pd.DataFrame(rows)
    df.attrs["elapsed_sec"] = time.time() - t0
    return df
