"""Parameter grid for PM LP pilot."""
from __future__ import annotations

import itertools
import time
from typing import Dict, List

import pandas as pd

from .engine import LpParams, run_lp_backtest
from .fetch import MarketSeries
from .metrics import compute_metrics

QUICK_GRID: Dict[str, List] = {
    "spread_cents": [2, 3, 4, 5],
    "reward_scale": [0.5, 1.0, 1.5],
    "adverse_multiplier": [1.0, 1.5],
}

FULL_GRID: Dict[str, List] = {
    "spread_cents": [2, 3, 4, 5, 6],
    "reward_scale": [0.5, 1.0, 1.5, 2.0],
    "adverse_multiplier": [0.8, 1.0, 1.2, 1.5],
}


def run_sweep(
    markets: List[MarketSeries],
    grid: Dict[str, List] | None = None,
    notional_usd: float = 10.0,
) -> pd.DataFrame:
    grid = grid or QUICK_GRID
    keys = list(grid.keys())
    rows = []
    t0 = time.time()
    for combo in itertools.product(*[grid[k] for k in keys]):
        params_dict = dict(zip(keys, combo))
        params = LpParams(
            spread_cents=float(params_dict["spread_cents"]),
            reward_scale=float(params_dict["reward_scale"]),
            adverse_multiplier=float(params_dict.get("adverse_multiplier", 1.0)),
            notional_usd=notional_usd,
        )
        trades = run_lp_backtest(markets, params)
        metrics = compute_metrics(trades, initial_capital=200.0)
        row = {**params_dict, **metrics}
        rows.append(row)
    elapsed = time.time() - t0
    df = pd.DataFrame(rows)
    df.attrs["elapsed_sec"] = elapsed
    return df
