"""Kalshi market discovery + candlesticks / trade-derived hourly mids."""
from __future__ import annotations

import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional

import pandas as pd
import requests

BASE = "https://api.elections.kalshi.com/trade-api/v2"
DEFAULT_CACHE = (
    Path(__file__).resolve().parents[2] / ".local" / "reports" / "kalshi-lp-backtest" / "cache"
)

# Longer candle history than same-day sports books
MACRO_SERIES = (
    "KXFEDDECISION",
    "KXINX",
    "KXGDP",
    "KXCPI",
    "KXHIGHNY",
    "KXBTC",
    "KXETH",
)


@dataclass
class MarketSeries:
    market_id: str
    slug: str
    question: str
    token_id: str  # ticker (report kit uses segment labels)
    volume24hr: float
    series_ticker: str
    prices: pd.DataFrame  # ts, mid


def _series_ticker_for(market: dict, ticker: str) -> str:
    return market.get("series_ticker") or ticker.split("-")[0]


def fetch_top_markets(
    limit: int = 12,
    min_volume24hr: float = 500.0,
    session: Optional[requests.Session] = None,
) -> List[dict]:
    sess = session or requests.Session()
    r = sess.get(
        f"{BASE}/markets",
        params={
            "status": "open",
            "limit": 200,
            "mve_filter": "exclude",
        },
        timeout=30,
    )
    r.raise_for_status()
    markets = r.json().get("markets") or []
    rows = []
    for m in markets:
        if m.get("market_type") != "binary":
            continue
        vol = float(m.get("volume_24h_fp") or m.get("volume_24h") or 0)
        if vol < min_volume24hr:
            continue
        ticker = m["ticker"]
        rows.append(
            {
                "market_id": ticker,
                "slug": ticker[:48],
                "question": (m.get("title") or m.get("subtitle") or ticker)[:120],
                "token_id": ticker,
                "volume24hr": vol,
                "series_ticker": _series_ticker_for(m, ticker),
            }
        )
    rows.sort(key=lambda x: x["volume24hr"], reverse=True)
    return rows[:limit]


def fetch_macro_markets(
    per_series: int = 2,
    session: Optional[requests.Session] = None,
) -> List[dict]:
    """Open markets on macro/index series (longer candle history than sports)."""
    sess = session or requests.Session()
    rows: List[dict] = []
    for series in MACRO_SERIES:
        try:
            r = sess.get(
                f"{BASE}/markets",
                params={"series_ticker": series, "status": "open", "limit": per_series},
                timeout=30,
            )
            if r.status_code == 429:
                time.sleep(1.0)
                r = sess.get(
                    f"{BASE}/markets",
                    params={"series_ticker": series, "status": "open", "limit": per_series},
                    timeout=30,
                )
            r.raise_for_status()
        except requests.RequestException:
            continue
        for m in r.json().get("markets") or []:
            if m.get("market_type") != "binary":
                continue
            ticker = m["ticker"]
            vol = float(m.get("volume_24h_fp") or 0)
            rows.append(
                {
                    "market_id": ticker,
                    "slug": ticker[:48],
                    "question": (m.get("title") or ticker)[:120],
                    "token_id": ticker,
                    "volume24hr": vol,
                    "series_ticker": _series_ticker_for(m, ticker),
                }
            )
        time.sleep(0.15)
    return rows


def fetch_candidate_markets(
    limit: int = 12,
    min_volume24hr: float = 500.0,
    session: Optional[requests.Session] = None,
) -> List[dict]:
    """Macro series first, then high-volume open sports (deduped)."""
    sess = session or requests.Session()
    seen = set()
    out: List[dict] = []
    for m in fetch_macro_markets(per_series=2, session=sess):
        if m["token_id"] not in seen:
            seen.add(m["token_id"])
            out.append(m)
    for m in fetch_top_markets(limit * 3, min_volume24hr, sess):
        if m["token_id"] not in seen:
            seen.add(m["token_id"])
            out.append(m)
    return out[: limit * 4]


def _candles_to_df(candlesticks: list) -> pd.DataFrame:
    rows = []
    for c in candlesticks:
        price = c.get("price") or {}
        mid = price.get("close_dollars") or price.get("mean_dollars")
        if mid is None:
            continue
        ts = datetime.fromtimestamp(c["end_period_ts"], tz=timezone.utc)
        rows.append({"ts": ts, "mid": float(mid)})
    if not rows:
        return pd.DataFrame(columns=["ts", "mid"])
    return pd.DataFrame(rows).sort_values("ts").drop_duplicates("ts")


def fetch_candlesticks(
    series_ticker: str,
    ticker: str,
    start_ts: int,
    end_ts: int,
    session: Optional[requests.Session] = None,
    cache_dir: Optional[Path] = None,
    refresh: bool = False,
    period_interval: int = 60,
) -> pd.DataFrame:
    cache_dir = cache_dir or DEFAULT_CACHE
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_path = cache_dir / f"{ticker}_{period_interval}m.parquet"
    if cache_path.exists() and not refresh:
        return pd.read_parquet(cache_path)

    sess = session or requests.Session()
    url = f"{BASE}/series/{series_ticker}/markets/{ticker}/candlesticks"
    r = sess.get(
        url,
        params={
            "period_interval": period_interval,
            "start_ts": start_ts,
            "end_ts": end_ts,
        },
        timeout=60,
    )
    if r.status_code == 429:
        time.sleep(1.0)
        r = sess.get(
            url,
            params={
                "period_interval": period_interval,
                "start_ts": start_ts,
                "end_ts": end_ts,
            },
            timeout=60,
        )
    r.raise_for_status()
    df = _candles_to_df(r.json().get("candlesticks") or [])
    if len(df) < 24 and period_interval == 60:
        df = _trades_to_hourly(ticker, start_ts, end_ts, sess)
    if len(df) >= 12:
        df.to_parquet(cache_path, index=False)
    time.sleep(0.12)
    return df


def _trades_to_hourly(
    ticker: str, start_ts: int, end_ts: int, sess: requests.Session
) -> pd.DataFrame:
    """Fallback: aggregate public trades into hourly mids."""
    rows = []
    cursor = None
    for _ in range(20):
        params = {"ticker": ticker, "limit": 1000}
        if cursor:
            params["cursor"] = cursor
        r = sess.get(f"{BASE}/markets/trades", params=params, timeout=60)
        r.raise_for_status()
        body = r.json()
        trades = body.get("trades") or []
        if not trades:
            break
        for t in trades:
            created = t.get("created_time")
            if not created:
                continue
            ts = pd.to_datetime(created, utc=True)
            ts_unix = int(ts.timestamp())
            if ts_unix < start_ts or ts_unix > end_ts:
                continue
            yes = t.get("yes_price_dollars")
            if yes is None:
                continue
            rows.append({"ts": ts, "mid": float(yes)})
        cursor = body.get("cursor")
        if not cursor:
            break
        time.sleep(0.1)

    if not rows:
        return pd.DataFrame(columns=["ts", "mid"])
    df = pd.DataFrame(rows)
    df["hour"] = df["ts"].dt.floor("h")
    hourly = df.groupby("hour")["mid"].last().reset_index()
    hourly = hourly.rename(columns={"hour": "ts"})
    return hourly[["ts", "mid"]].sort_values("ts")


def load_market_series(
    limit: int = 12,
    min_volume24hr: float = 500.0,
    lookback_days: int = 30,
    min_bars: int = 24,
    cache_dir: Optional[Path] = None,
    refresh: bool = False,
) -> List[MarketSeries]:
    sess = requests.Session()
    end_ts = int(time.time())
    start_ts = end_ts - lookback_days * 86400
    markets = fetch_candidate_markets(limit, min_volume24hr, sess)
    out: List[MarketSeries] = []
    for m in markets:
        prices = fetch_candlesticks(
            m["series_ticker"],
            m["token_id"],
            start_ts,
            end_ts,
            sess,
            cache_dir,
            refresh,
        )
        if len(prices) < min_bars:
            continue
        out.append(
            MarketSeries(
                market_id=m["market_id"],
                slug=m["slug"],
                question=m["question"],
                token_id=m["token_id"],
                volume24hr=m["volume24hr"],
                series_ticker=m["series_ticker"],
                prices=prices,
            )
        )
        if len(out) >= limit:
            break
    return out
