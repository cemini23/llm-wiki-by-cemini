#!/usr/bin/env python3
"""Extend librarian ArcticDB equity_bars from last bar through today (yfinance).

One-time migration (migrate_market_dataset_to_arcticdb.py) copied Kaggle CSVs that
end ~2017-11-10. OSINT backtests read librarian Arctic via SSH — refresh here first.

Usage:
  python3 scripts/refresh_arctic_equity_bars.py --dry-run
  python3 scripts/refresh_arctic_equity_bars.py --symbols NVDA,AAPL,MSFT,SPY,QQQ,TSLA,AMD
  python3 scripts/refresh_arctic_equity_bars.py  # default 7-symbol backtest set

Then re-run:
  bash scripts/run_equity_signal_backtest.sh --quick --refresh
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional

import pandas as pd

DEFAULT_SYMBOLS = ("NVDA", "AAPL", "MSFT", "SPY", "QQQ", "TSLA", "AMD")
SSH_HOST = "cemini-librarian"
REMOTE_PY = "/opt/cemini-bulk/.venv/bin/python3"
STORE_URI = "lmdb:///opt/cemini-bulk/arctic-market-dataset"
LIBRARY = "equity_bars"
OVERLAP_START = "2017-11-01"


def _fetch_yfinance(symbol: str, start: str) -> pd.DataFrame:
    import yfinance as yf

    ticker = yf.Ticker(symbol)
    hist = ticker.history(start=start, auto_adjust=False)
    if hist is None or hist.empty:
        return pd.DataFrame()
    df = hist.rename(
        columns={
            "Open": "Open",
            "High": "High",
            "Low": "Low",
            "Close": "Close",
            "Volume": "Volume",
        }
    )[["Open", "High", "Low", "Close", "Volume"]].copy()
    if df.index.tz is None:
        df.index = df.index.tz_localize("UTC")
    else:
        df.index = df.index.tz_convert("UTC")
    df = df[~df.index.duplicated(keep="last")].sort_index()
    return df


def _remote_last_date(symbol: str) -> Optional[str]:
    script = f"""
from arcticdb import Arctic
lib = Arctic({STORE_URI!r}).get_library({LIBRARY!r})
sym = {symbol!r}
if not lib.has_symbol(sym):
    print("null")
else:
    df = lib.read(sym).data
    print(df.index.max())
"""
    proc = subprocess.run(
        ["ssh", SSH_HOST, REMOTE_PY],
        input=script,
        capture_output=True,
        text=True,
        check=True,
    )
    line = proc.stdout.strip().splitlines()[-1] if proc.stdout.strip() else "null"
    return None if line == "null" else line


def _remote_merge(symbol: str, csv_path: Path) -> dict:
    remote_csv = f"/tmp/cemini_refresh_{symbol}.csv"
    subprocess.run(
        ["scp", str(csv_path), f"{SSH_HOST}:{remote_csv}"],
        check=True,
        capture_output=True,
    )
    script = f"""
import pandas as pd
from arcticdb import Arctic

sym = {symbol!r}
uri = {STORE_URI!r}
lib_name = {LIBRARY!r}
remote_csv = {remote_csv!r}

new_df = pd.read_csv(remote_csv, parse_dates=["Date"], index_col="Date")
if new_df.index.tz is None:
    new_df.index = new_df.index.tz_localize("UTC")
else:
    new_df.index = new_df.index.tz_convert("UTC")
new_df = new_df[~new_df.index.duplicated(keep="last")].sort_index()

ac = Arctic(uri)
if lib_name not in ac.list_libraries():
    ac.create_library(lib_name)
lib = ac.get_library(lib_name)

before_rows = 0
before_max = None
if lib.has_symbol(sym):
    existing = lib.read(sym).data
    before_rows = len(existing)
    before_max = str(existing.index.max())
    merged = existing.combine_first(new_df)
    merged = merged[~merged.index.duplicated(keep="last")].sort_index()
else:
    merged = new_df

lib.write(sym, merged)
import os
os.remove(remote_csv)
print(__import__("json").dumps({{
    "symbol": sym,
    "before_rows": before_rows,
    "before_max": before_max,
    "after_rows": len(merged),
    "after_max": str(merged.index.max()),
    "new_rows": len(merged) - before_rows,
}}))
"""
    proc = subprocess.run(
        ["ssh", SSH_HOST, REMOTE_PY],
        input=script,
        capture_output=True,
        text=True,
        check=True,
    )
    line = proc.stdout.strip().splitlines()[-1]
    return json.loads(line)


def main() -> int:
    p = argparse.ArgumentParser(description="Refresh librarian equity_bars via yfinance")
    p.add_argument(
        "--symbols",
        default=",".join(DEFAULT_SYMBOLS),
        help="Comma-separated tickers",
    )
    p.add_argument("--dry-run", action="store_true")
    p.add_argument(
        "--start",
        default=OVERLAP_START,
        help="yfinance start date (overlap with 2017 canon)",
    )
    args = p.parse_args()
    symbols = [s.strip().upper() for s in args.symbols.split(",") if s.strip()]

    print(f"Target: {SSH_HOST} {STORE_URI} / {LIBRARY}")
    print(f"Symbols: {', '.join(symbols)}")
    failures = 0

    for sym in symbols:
        try:
            last = _remote_last_date(sym)
        except subprocess.CalledProcessError as exc:
            print(f"  FAIL {sym}: cannot read Arctic ({exc.stderr[:120]})")
            failures += 1
            continue

        print(f"  {sym}: Arctic last={last or 'missing'}", end="")
        if args.dry_run:
            print(" → would fetch yfinance from", args.start)
            continue

        try:
            df = _fetch_yfinance(sym, args.start)
        except Exception as exc:
            print(f" → yfinance FAIL ({exc})")
            failures += 1
            continue
        if df.empty:
            print(" → yfinance empty")
            failures += 1
            continue

        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".csv", delete=False, prefix=f"{sym}_"
        ) as tmp:
            out = df.copy()
            out.index.name = "Date"
            out.reset_index().to_csv(tmp.name, index=False)
            tmp_path = Path(tmp.name)

        try:
            result = _remote_merge(sym, tmp_path)
        except subprocess.CalledProcessError as exc:
            print(f" → merge FAIL ({exc.stderr[:160]})")
            failures += 1
            continue
        finally:
            tmp_path.unlink(missing_ok=True)

        print(
            f" → merged +{result['new_rows']} rows "
            f"({result['before_max']} → {result['after_max']})"
        )

    if not args.dry_run:
        print("\nVerify:")
        for sym in symbols[:3]:
            try:
                last = _remote_last_date(sym)
                print(f"  {sym}: max={last}")
            except subprocess.CalledProcessError:
                print(f"  {sym}: verify failed")
        print("\nNext: bash scripts/run_equity_signal_backtest.sh --quick --refresh")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
