"""Load daily OHLCV from cemini-librarian ArcticDB equity_bars."""
from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

import pandas as pd

DEFAULT_SYMBOLS = ("NVDA", "AAPL", "MSFT", "SPY", "QQQ", "TSLA", "AMD")
DEFAULT_CACHE = (
    Path(__file__).resolve().parents[2]
    / ".local"
    / "reports"
    / "equity-signal-backtest"
    / "cache"
)
SSH_HOST = "cemini-librarian"
REMOTE_PY = "/opt/cemini-bulk/.venv/bin/python3"
STORE_URI = "lmdb:///opt/cemini-bulk/arctic-market-dataset"
LIBRARY = "equity_bars"


@dataclass
class SymbolSeries:
    symbol: str
    slug: str
    question: str
    token_id: str
    volume24hr: float
    prices: pd.DataFrame  # ts, close


def _remote_export_csv(symbol: str, remote_path: str, ssh_host: str) -> None:
    script = f"""from arcticdb import Arctic
lib = Arctic({STORE_URI!r}).get_library({LIBRARY!r})
df = lib.read({symbol!r}).data
col = "Close" if "Close" in df.columns else "close"
out = df[col].to_frame("close")
out.index.name = "ts"
out.reset_index().to_csv({remote_path!r}, index=False)
"""
    subprocess.run(
        ["ssh", ssh_host, REMOTE_PY],
        input=script,
        check=True,
        capture_output=True,
        text=True,
    )


def fetch_symbol(
    symbol: str,
    cache_dir: Optional[Path] = None,
    refresh: bool = False,
    ssh_host: str = SSH_HOST,
) -> pd.DataFrame:
    cache_dir = cache_dir or DEFAULT_CACHE
    cache_dir.mkdir(parents=True, exist_ok=True)
    local = cache_dir / f"{symbol}.csv"
    if local.exists() and not refresh:
        df = pd.read_csv(local)
    else:
        remote = f"/tmp/cemini_eq_{symbol}.csv"
        _remote_export_csv(symbol, remote, ssh_host)
        subprocess.run(
            ["scp", f"{ssh_host}:{remote}", str(local)],
            check=True,
            capture_output=True,
        )
        subprocess.run(
            ["ssh", ssh_host, f"rm -f {remote}"],
            check=False,
            capture_output=True,
        )
        df = pd.read_csv(local)

    df["ts"] = pd.to_datetime(df["ts"], utc=True)
    df = df.sort_values("ts").drop_duplicates("ts")
    return df[["ts", "close"]]


def load_symbol_series(
    symbols: Optional[List[str]] = None,
    lookback_years: int = 5,
    min_bars: int = 252,
    cache_dir: Optional[Path] = None,
    refresh: bool = False,
) -> List[SymbolSeries]:
    symbols = list(symbols or DEFAULT_SYMBOLS)
    out: List[SymbolSeries] = []
    for sym in symbols:
        try:
            prices = fetch_symbol(sym, cache_dir, refresh)
        except (subprocess.CalledProcessError, OSError) as exc:
            print(f"skip {sym}: {exc}")
            continue
        end = prices["ts"].max()
        start = end - pd.DateOffset(years=lookback_years)
        prices = prices[prices["ts"] >= start].tail(max(min_bars, 252 * lookback_years))
        if len(prices) < min_bars:
            continue
        out.append(
            SymbolSeries(
                symbol=sym,
                slug=sym,
                question=f"{sym} daily momentum",
                token_id=sym,
                volume24hr=float(len(prices)),
                prices=prices,
            )
        )
    return out
