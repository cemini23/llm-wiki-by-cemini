"""PTA (price-to-52-week-anchor) reproduction pilot — librarian data, laptop compute."""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import List, Tuple

import numpy as np
import pandas as pd

from equity_signal_backtest.fetch import DEFAULT_SYMBOLS, load_symbol_series

WORKSPACE = Path(__file__).resolve().parents[2]
DEFAULT_OUT = WORKSPACE / ".local" / "reports"


def compute_pta_panel(
    prices: pd.DataFrame,
    anchor_days: int = 252,
    past_win_days: int = 21,
    forward_days: int = 21,
) -> pd.DataFrame:
    """Rolling PTA + past-winner mask + forward return per bar."""
    df = prices.sort_values("ts").copy()
    close = df["close"].astype(float)
    h = close.rolling(anchor_days, min_periods=anchor_days).max()
    l = close.rolling(anchor_days, min_periods=anchor_days).min()
    span = (h - l).replace(0, np.nan)
    pta = (close - l) / span
    past_ret = close.pct_change(past_win_days)
    fwd_ret = close.shift(-forward_days) / close - 1.0
    out = pd.DataFrame(
        {
            "ts": df["ts"].values,
            "close": close.values,
            "pta": pta.values,
            "past_win": (past_ret > 0).values,
            "fwd_ret": fwd_ret.values,
        }
    )
    return out.dropna(subset=["pta", "fwd_ret"])


def quintile_spread(panel: pd.DataFrame) -> Tuple[float, int]:
    """Mean forward return: top PTA quintile minus bottom among past winners."""
    winners = panel[panel["past_win"]].copy()
    if len(winners) < 100:
        return float("nan"), len(winners)
    winners["q"] = pd.qcut(winners["pta"], 5, labels=False, duplicates="drop")
    if winners["q"].nunique() < 2:
        return float("nan"), len(winners)
    top = winners[winners["q"] == winners["q"].max()]["fwd_ret"].mean()
    bot = winners[winners["q"] == winners["q"].min()]["fwd_ret"].mean()
    return float(top - bot), len(winners)


def run_pilot(
    symbols: List[str],
    anchor_days: int = 252,
    micro_days: int = 52,
    lookback_years: int = 5,
    cache_dir: Path | None = None,
) -> dict:
    spreads: List[float] = []
    micro_spreads: List[float] = []
    n_obs = 0

    series_list = load_symbol_series(
        symbols, lookback_years=lookback_years, min_bars=anchor_days + 42, cache_dir=cache_dir
    )
    for s in series_list:
        panel = compute_pta_panel(s.prices, anchor_days=anchor_days)
        sp, n = quintile_spread(panel)
        if np.isfinite(sp):
            spreads.append(sp)
            n_obs += n
        panel_m = compute_pta_panel(s.prices, anchor_days=micro_days)
        sp_m, _ = quintile_spread(panel_m)
        if np.isfinite(sp_m):
            micro_spreads.append(sp_m)

    return {
        "symbols_loaded": len(series_list),
        "symbols": [s.symbol for s in series_list],
        "anchor_days": anchor_days,
        "micro_days": micro_days,
        "mean_quintile_spread_52w": float(np.mean(spreads)) if spreads else float("nan"),
        "mean_quintile_spread_micro": float(np.mean(micro_spreads)) if micro_spreads else float("nan"),
        "n_past_winner_obs": n_obs,
        "data_note": "librarian ArcticDB equity_bars (daily; corpus ends ~2017-11)",
    }


def main() -> int:
    p = argparse.ArgumentParser(description="PTA pilot on librarian ArcticDB via SSH")
    p.add_argument("--symbols", nargs="*", default=list(DEFAULT_SYMBOLS))
    p.add_argument("--anchor-days", type=int, default=252)
    p.add_argument("--micro-days", type=int, default=52)
    p.add_argument("--lookback-years", type=int, default=5)
    p.add_argument("--output", type=Path, default=None)
    args = p.parse_args()

    cache = DEFAULT_OUT / "equity-signal-backtest" / "cache"
    result = run_pilot(
        list(args.symbols),
        anchor_days=args.anchor_days,
        micro_days=args.micro_days,
        lookback_years=args.lookback_years,
        cache_dir=cache,
    )

    lines = [
        "# PTA reproduction pilot",
        "",
        f"- **Run surface:** laptop (`pta_pilot.py`)",
        f"- **Data surface:** cemini-librarian ArcticDB `equity_bars` (SSH)",
        f"- **Symbols:** {result['symbols']}",
        f"- **52w anchor ({args.anchor_days}d) quintile spread (high PTA − low PTA, past winners):** "
        f"{result['mean_quintile_spread_52w']:.4%}"
        if np.isfinite(result["mean_quintile_spread_52w"])
        else "- **52w spread:** insufficient data",
        f"- **Micro anchor ({args.micro_days}d) mean quintile spread:** "
        f"{result['mean_quintile_spread_micro']:.4%}"
        if np.isfinite(result["mean_quintile_spread_micro"])
        else "- **Micro spread:** insufficient data",
        f"- **Past-winner observations (pooled):** {result['n_past_winner_obs']}",
        f"- **Note:** {result['data_note']}",
        "",
        "Paper claim direction: high-PTA past-winners outperform low-PTA past-winners (positive spread).",
    ]
    text = "\n".join(lines)
    print(text)

    out = args.output or (DEFAULT_OUT / f"pta-pilot-{pd.Timestamp.now('UTC').date().isoformat()}.md")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text)
    print(f"\nWrote {out}")
    return 0 if result["symbols_loaded"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
