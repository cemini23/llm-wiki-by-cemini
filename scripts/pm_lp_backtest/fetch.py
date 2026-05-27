"""Gamma market discovery + CLOB hourly price history."""
from __future__ import annotations

import ast
import json
import time
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

import pandas as pd
import requests

GAMMA_URL = "https://gamma-api.polymarket.com/markets"
CLOB_HISTORY_URL = "https://clob.polymarket.com/prices-history"
DEFAULT_CACHE = Path(__file__).resolve().parents[2] / ".local" / "reports" / "pm-lp-backtest" / "cache"


@dataclass
class MarketSeries:
    market_id: str
    slug: str
    question: str
    token_id: str
    volume24hr: float
    prices: pd.DataFrame  # columns: ts (datetime), mid (float)


def _parse_clob_token_ids(raw: str) -> List[str]:
    if not raw:
        return []
    try:
        ids = json.loads(raw) if raw.startswith("[") else ast.literal_eval(raw)
    except (json.JSONDecodeError, ValueError, SyntaxError):
        return []
    return [str(x) for x in ids]


def fetch_top_markets(
    limit: int = 12,
    min_volume24hr: float = 0.0,
    session: Optional[requests.Session] = None,
) -> List[dict]:
    sess = session or requests.Session()
    params = {
        "active": "true",
        "closed": "false",
        "limit": max(limit * 3, 30),
        "order": "volume24hr",
        "ascending": "false",
    }
    r = sess.get(GAMMA_URL, params=params, timeout=30)
    r.raise_for_status()
    markets = r.json()
    out = []
    for m in markets:
        vol = float(m.get("volume24hr") or 0)
        if vol < min_volume24hr:
            continue
        tids = _parse_clob_token_ids(m.get("clobTokenIds") or "")
        if not tids:
            continue
        out.append(
            {
                "market_id": str(m.get("id", "")),
                "slug": m.get("slug", ""),
                "question": (m.get("question") or "")[:120],
                "token_id": tids[0],
                "volume24hr": vol,
            }
        )
        if len(out) >= limit:
            break
    return out


def fetch_price_history(
    token_id: str,
    fidelity_minutes: int = 60,
    session: Optional[requests.Session] = None,
    cache_dir: Optional[Path] = None,
    refresh: bool = False,
) -> pd.DataFrame:
    cache_dir = cache_dir or DEFAULT_CACHE
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_path = cache_dir / f"{token_id}_f{fidelity_minutes}.parquet"
    if cache_path.exists() and not refresh:
        return pd.read_parquet(cache_path)

    sess = session or requests.Session()
    r = sess.get(
        CLOB_HISTORY_URL,
        params={"market": token_id, "interval": "max", "fidelity": fidelity_minutes},
        timeout=60,
    )
    r.raise_for_status()
    history = r.json().get("history") or []
    if not history:
        return pd.DataFrame(columns=["ts", "mid"])

    df = pd.DataFrame(history)
    df = df.rename(columns={"t": "ts_unix", "p": "mid"})
    df["ts"] = pd.to_datetime(df["ts_unix"], unit="s", utc=True)
    df = df[["ts", "mid"]].sort_values("ts").drop_duplicates("ts")
    df.to_parquet(cache_path, index=False)
    time.sleep(0.15)
    return df


def load_market_series(
    limit: int = 12,
    min_volume24hr: float = 0.0,
    cache_dir: Optional[Path] = None,
    refresh: bool = False,
) -> List[MarketSeries]:
    sess = requests.Session()
    markets = fetch_top_markets(limit, min_volume24hr, sess)
    series_list: List[MarketSeries] = []
    for m in markets:
        prices = fetch_price_history(
            m["token_id"], session=sess, cache_dir=cache_dir, refresh=refresh
        )
        if len(prices) < 48:
            continue
        series_list.append(
            MarketSeries(
                market_id=m["market_id"],
                slug=m["slug"],
                question=m["question"],
                token_id=m["token_id"],
                volume24hr=m["volume24hr"],
                prices=prices,
            )
        )
    return series_list
