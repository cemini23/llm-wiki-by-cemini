"""Simulate convergence trades on PM vs Kalshi mid divergence."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List

import pandas as pd

from .fetch import VenuePair


@dataclass
class ArbParams:
    min_edge_cents: float = 3.0
    latency_penalty_cents: float = 1.0
    notional_usd: float = 100.0
    max_hold_hours: int = 24


def run_arb_backtest(pairs: List[VenuePair], params: ArbParams) -> pd.DataFrame:
    rows: List[dict] = []
    for pair in pairs:
        df = pair.aligned.copy()
        spread_cents = (df["pm_mid"] - df["kalshi_mid"]).abs() * 100
        eff_edge = params.min_edge_cents + params.latency_penalty_cents

        i = 0
        while i < len(df) - 1:
            if spread_cents.iloc[i] < eff_edge:
                i += 1
                continue
            entry = df.iloc[i]
            exit_i = min(i + params.max_hold_hours, len(df) - 1)
            exit_row = df.iloc[exit_i]
            # Convergence PnL: spread narrowed
            entry_spread = abs(entry["pm_mid"] - entry["kalshi_mid"])
            exit_spread = abs(exit_row["pm_mid"] - exit_row["kalshi_mid"])
            pnl_c = (entry_spread - exit_spread) * 100 * params.notional_usd / 100
            rows.append(
                {
                    "segment": pair.pair_id[:40],
                    "entry_ts": entry["ts"],
                    "exit_ts": exit_row["ts"],
                    "net_pnl_usd": pnl_c,
                    "net_pnl_pct": pnl_c / params.notional_usd * 100,
                    "exit_reason": "converged" if exit_spread < entry_spread else "timeout",
                    "hours_held": float((exit_row["ts"] - entry["ts"]).total_seconds() / 3600),
                }
            )
            i = exit_i + 1

    return pd.DataFrame(rows)
