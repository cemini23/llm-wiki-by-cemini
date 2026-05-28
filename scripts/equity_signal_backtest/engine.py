"""Daily z-score momentum on ArcticDB closes."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List

import numpy as np
import pandas as pd

from .fetch import SymbolSeries


@dataclass
class MomParams:
    lookback: int = 20
    entry_z: float = 1.0
    exit_z: float = 0.0
    stop_loss_pct: float = 5.0
    notional_usd: float = 1000.0


def _simulate_symbol(series: SymbolSeries, params: MomParams) -> pd.DataFrame:
    df = series.prices.copy()
    close = df["close"].astype(float)
    ma = close.rolling(params.lookback).mean()
    std = close.rolling(params.lookback).std().replace(0, np.nan)
    z = (close - ma) / std

    rows: List[dict] = []
    in_pos = False
    entry_i = entry_price = 0.0

    for i in range(params.lookback, len(df) - 1):
        zi = z.iloc[i]
        if not np.isfinite(zi):
            continue
        px = close.iloc[i]
        nxt = close.iloc[i + 1]

        if not in_pos and zi >= params.entry_z:
            in_pos = True
            entry_i = i
            entry_price = px
        elif in_pos:
            stop_hit = (px - entry_price) / entry_price * 100 <= -params.stop_loss_pct
            exit_sig = zi <= params.exit_z or stop_hit
            if exit_sig:
                pnl_pct = (nxt - entry_price) / entry_price * 100
                rows.append(
                    {
                        "segment": series.symbol,
                        "entry_ts": df["ts"].iloc[entry_i],
                        "exit_ts": df["ts"].iloc[i + 1],
                        "net_pnl_usd": pnl_pct / 100 * params.notional_usd,
                        "net_pnl_pct": pnl_pct,
                        "exit_reason": "stop" if stop_hit else "signal",
                        "hours_held": 24.0,
                    }
                )
                in_pos = False

    return pd.DataFrame(rows)


def run_momentum_backtest(
    symbols: List[SymbolSeries], params: MomParams
) -> pd.DataFrame:
    frames = [_simulate_symbol(s, params) for s in symbols]
    frames = [f for f in frames if not f.empty]
    if not frames:
        return pd.DataFrame()
    return pd.concat(frames, ignore_index=True)
