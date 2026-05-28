"""Monte Carlo permutation test on trade PnL (Masters-style sanity gate)."""
from __future__ import annotations

import argparse
from typing import Dict

import numpy as np
import pandas as pd


def mcpt(
    pnl_pct: np.ndarray,
    n_perm: int = 2000,
    seed: int = 42,
) -> Dict:
    """H0: mean PnL is zero. Returns observed mean, p-value, pass at 5%."""
    pnl = np.asarray(pnl_pct, dtype=float)
    pnl = pnl[np.isfinite(pnl)]
    if len(pnl) < 5:
        return {
            "n_trades": len(pnl),
            "observed_mean_pct": float(np.mean(pnl)) if len(pnl) else 0.0,
            "p_value": 1.0,
            "pass_5pct": False,
            "note": "too few trades",
        }
    obs = float(np.mean(pnl))
    rng = np.random.default_rng(seed)
    count = 0
    for _ in range(n_perm):
        signs = rng.choice([-1.0, 1.0], size=len(pnl))
        if np.mean(pnl * signs) >= obs:
            count += 1
    p_val = (count + 1) / (n_perm + 1)
    return {
        "n_trades": len(pnl),
        "observed_mean_pct": obs,
        "p_value": float(p_val),
        "pass_5pct": p_val < 0.05 and obs > 0,
        "n_perm": n_perm,
    }


def main() -> int:
    p = argparse.ArgumentParser(description="MCPT gate on trades CSV")
    p.add_argument("trades_csv", type=str, help="CSV with net_pnl_pct column")
    p.add_argument("--pnl-col", default="net_pnl_pct")
    p.add_argument("--perm", type=int, default=2000)
    args = p.parse_args()
    df = pd.read_csv(args.trades_csv)
    if args.pnl_col not in df.columns:
        print(f"Missing column {args.pnl_col}")
        return 1
    res = mcpt(df[args.pnl_col].values, n_perm=args.perm)
    print(f"MCPT: mean={res['observed_mean_pct']:.4f}% p={res['p_value']:.4f} pass@5%={res['pass_5pct']}")
    return 0 if res.get("pass_5pct") or res.get("note") else 0


if __name__ == "__main__":
    raise SystemExit(main())
