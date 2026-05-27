"""Hourly two-sided LP shadow simulator on CLOB mids."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List

import pandas as pd

from .fetch import MarketSeries


@dataclass
class LpParams:
    spread_cents: float = 4.0
    reward_scale: float = 1.0
    notional_usd: float = 10.0
    adverse_multiplier: float = 1.0


def _simulate_market(series: MarketSeries, params: LpParams) -> pd.DataFrame:
    """Return trade/event rows for one market."""
    df = series.prices.copy()
    if len(df) < 3:
        return pd.DataFrame()

    half = params.spread_cents / 200.0  # cents → probability half-spread
    rows: List[dict] = []

    mids = df["mid"].astype(float).values
    ts = df["ts"].values

    for i in range(len(df) - 1):
        mid = mids[i]
        nxt = mids[i + 1]
        if not (0.02 < mid < 0.98):
            continue

        bid = mid - half
        ask = mid + half
        reward_usd = params.reward_scale * (params.notional_usd * 0.01) / max(
            params.spread_cents, 1.0
        )

        # Adverse: price trades through our quote
        if nxt <= bid:
            pnl_prob = nxt - bid
            rows.append(
                {
                    "segment": series.slug[:40],
                    "market_slug": series.slug,
                    "entry_ts": ts[i],
                    "exit_ts": ts[i + 1],
                    "net_pnl_usd": pnl_prob * params.notional_usd * params.adverse_multiplier,
                    "net_pnl_pct": pnl_prob * 100 * params.adverse_multiplier,
                    "exit_reason": "adverse_fill",
                    "hours_held": 1.0,
                }
            )
        elif nxt >= ask:
            pnl_prob = ask - nxt
            rows.append(
                {
                    "segment": series.slug[:40],
                    "market_slug": series.slug,
                    "entry_ts": ts[i],
                    "exit_ts": ts[i + 1],
                    "net_pnl_usd": pnl_prob * params.notional_usd * params.adverse_multiplier,
                    "net_pnl_pct": pnl_prob * 100 * params.adverse_multiplier,
                    "exit_reason": "adverse_fill",
                    "hours_held": 1.0,
                }
            )
        else:
            rows.append(
                {
                    "segment": series.slug[:40],
                    "market_slug": series.slug,
                    "entry_ts": ts[i],
                    "exit_ts": ts[i + 1],
                    "net_pnl_usd": reward_usd,
                    "net_pnl_pct": reward_usd / params.notional_usd * 100,
                    "exit_reason": "reward_only",
                    "hours_held": 1.0,
                }
            )

    return pd.DataFrame(rows)


def run_lp_backtest(
    markets: List[MarketSeries], params: LpParams
) -> pd.DataFrame:
    frames = [_simulate_market(m, params) for m in markets]
    frames = [f for f in frames if not f.empty]
    if not frames:
        return pd.DataFrame()
    return pd.concat(frames, ignore_index=True)
