"""Aggregate trade list + equity into sweep-row metrics."""
from __future__ import annotations

from typing import Dict

import numpy as np
import pandas as pd


def trades_to_equity(trades_df: pd.DataFrame) -> pd.DataFrame:
    if trades_df is None or trades_df.empty:
        return pd.DataFrame(columns=["ts", "cum_pnl_usd"])
    t = trades_df.sort_values("exit_ts")
    cum = t["net_pnl_usd"].cumsum()
    return pd.DataFrame({"ts": t["exit_ts"].values, "cum_pnl_usd": cum.values})


def compute_metrics(
    trades_df: pd.DataFrame,
    initial_capital: float = 200.0,
    periods_per_year: float = 252 * 24,
) -> Dict:
    if trades_df is None or trades_df.empty:
        return {
            "n_trades": 0,
            "hit_rate": 0.0,
            "total_pnl_usd": 0.0,
            "total_pnl_pct": 0.0,
            "sharpe_annual": 0.0,
            "max_drawdown_pct": 0.0,
            "profit_factor": 0.0,
            "avg_pnl_pct": 0.0,
            "pct_tp": 0.0,
            "pct_sl": 0.0,
            "avg_hours_held": 0.0,
        }

    n = len(trades_df)
    wins = trades_df[trades_df["net_pnl_usd"] > 0]
    losses = trades_df[trades_df["net_pnl_usd"] < 0]
    total_pnl = float(trades_df["net_pnl_usd"].sum())
    gross_profit = float(wins["net_pnl_usd"].sum()) if len(wins) else 0.0
    gross_loss = float(abs(losses["net_pnl_usd"].sum())) if len(losses) else 0.0
    pf = gross_profit / gross_loss if gross_loss > 0 else (999.0 if gross_profit > 0 else 0.0)

    eq = trades_to_equity(trades_df)
    if len(eq) > 1:
        peak = eq["cum_pnl_usd"].cummax()
        dd = eq["cum_pnl_usd"] - peak
        max_dd_pct = float(abs(dd.min()) / initial_capital * 100)
    else:
        max_dd_pct = 0.0

    rets = trades_df["net_pnl_pct"].values
    if len(rets) > 1 and np.std(rets) > 1e-9:
        sharpe = float(
            np.mean(rets) / np.std(rets) * np.sqrt(periods_per_year)
        )
    else:
        sharpe = 0.0

    exit_col = trades_df.get("exit_reason", pd.Series(dtype=str))
    return {
        "n_trades": n,
        "hit_rate": float((trades_df["net_pnl_usd"] > 0).mean() * 100),
        "total_pnl_usd": total_pnl,
        "total_pnl_pct": total_pnl / initial_capital * 100,
        "sharpe_annual": sharpe,
        "max_drawdown_pct": max_dd_pct,
        "profit_factor": min(pf, 999.0),
        "avg_pnl_pct": float(trades_df["net_pnl_pct"].mean()),
        "pct_tp": float((exit_col == "reward_only").mean() * 100) if len(exit_col) else 0.0,
        "pct_sl": float((exit_col == "adverse_fill").mean() * 100) if len(exit_col) else 0.0,
        "avg_hours_held": float(trades_df.get("hours_held", pd.Series([1])).mean()),
    }


def per_segment_summary(trades_df: pd.DataFrame, segment_col: str = "segment") -> pd.DataFrame:
    if trades_df is None or trades_df.empty:
        return pd.DataFrame(columns=[segment_col, "total_pnl_usd", "n_trades"])
    g = trades_df.groupby(segment_col).agg(
        total_pnl_usd=("net_pnl_usd", "sum"),
        n_trades=("net_pnl_usd", "count"),
    )
    return g.reset_index().sort_values("total_pnl_usd", ascending=False)
