"""Align Polymarket + Kalshi hourly mids on overlapping windows."""
from __future__ import annotations

import ast
import json
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional, Tuple

import pandas as pd
import requests

GAMMA = "https://gamma-api.polymarket.com/markets"
CLOB_HIST = "https://clob.polymarket.com/prices-history"
KALSHI = "https://api.elections.kalshi.com/trade-api/v2"
DEFAULT_CACHE = (
    Path(__file__).resolve().parents[2]
    / ".local"
    / "reports"
    / "cross-venue-backtest"
    / "cache"
)


@dataclass
class VenuePair:
    pair_id: str
    pm_slug: str
    pm_token: str
    kalshi_ticker: str
    kalshi_series: str
    aligned: pd.DataFrame  # ts, pm_mid, kalshi_mid


def _parse_token_ids(raw: str) -> List[str]:
    if not raw:
        return []
    try:
        ids = json.loads(raw) if raw.startswith("[") else ast.literal_eval(raw)
    except (json.JSONDecodeError, ValueError, SyntaxError):
        return []
    return [str(x) for x in ids]


def find_pm_btc_market(session: requests.Session) -> Optional[dict]:
    r = session.get(
        GAMMA,
        params={
            "active": "true",
            "closed": "false",
            "limit": 100,
            "order": "volume24hr",
            "ascending": "false",
        },
        timeout=30,
    )
    r.raise_for_status()
    for m in r.json():
        q = (m.get("question") or "").lower()
        if "bitcoin" in q or "btc" in q:
            tids = _parse_token_ids(m.get("clobTokenIds") or "")
            if tids:
                return {
                    "slug": m.get("slug", ""),
                    "token_id": tids[0],
                    "question": m.get("question", ""),
                }
    return None


def find_kalshi_btc_market(session: requests.Session) -> Optional[dict]:
    for series in ("KXBTC", "KXBTCD"):
        r = session.get(
            f"{KALSHI}/markets",
            params={"series_ticker": series, "status": "open", "limit": 10},
            timeout=30,
        )
        if r.status_code != 200:
            continue
        markets = r.json().get("markets") or []
        if not markets:
            continue
        m = max(
            markets,
            key=lambda x: float(x.get("volume_24h_fp") or 0),
        )
        return {
            "ticker": m["ticker"],
            "series_ticker": series,
            "title": m.get("title") or m["ticker"],
        }
    return None


def _pm_history(token: str, session: requests.Session) -> pd.DataFrame:
    r = session.get(
        CLOB_HIST,
        params={"market": token, "interval": "max", "fidelity": 60},
        timeout=60,
    )
    r.raise_for_status()
    rows = r.json().get("history") or []
    if not rows:
        return pd.DataFrame(columns=["ts", "pm_mid"])
    df = pd.DataFrame(rows).rename(columns={"t": "ts_unix", "p": "pm_mid"})
    df["ts"] = pd.to_datetime(df["ts_unix"], unit="s", utc=True)
    return df[["ts", "pm_mid"]].sort_values("ts")


def _kalshi_history(
    series: str, ticker: str, start_ts: int, end_ts: int, session: requests.Session
) -> pd.DataFrame:
    url = f"{KALSHI}/series/{series}/markets/{ticker}/candlesticks"
    r = session.get(
        url,
        params={"period_interval": 60, "start_ts": start_ts, "end_ts": end_ts},
        timeout=60,
    )
    r.raise_for_status()
    rows = []
    for c in r.json().get("candlesticks") or []:
        price = c.get("price") or {}
        mid = price.get("close_dollars") or price.get("mean_dollars")
        if mid is None:
            continue
        rows.append(
            {
                "ts": datetime.fromtimestamp(c["end_period_ts"], tz=timezone.utc),
                "kalshi_mid": float(mid),
            }
        )
    return pd.DataFrame(rows).sort_values("ts")


def align_pair(pm: dict, kalshi: dict, session: requests.Session) -> pd.DataFrame:
    pm_df = _pm_history(pm["token_id"], session)
    if pm_df.empty:
        return pd.DataFrame()
    start_ts = int(pm_df["ts"].min().timestamp())
    end_ts = int(pm_df["ts"].max().timestamp())
    k_df = _kalshi_history(
        kalshi["series_ticker"], kalshi["ticker"], start_ts, end_ts, session
    )
    if k_df.empty:
        return pd.DataFrame()
    left = pm_df.sort_values("ts").copy()
    right = k_df.sort_values("ts").copy()
    left["ts"] = pd.to_datetime(left["ts"], utc=True).dt.as_unit("ns")
    right["ts"] = pd.to_datetime(right["ts"], utc=True).dt.as_unit("ns")
    merged = pd.merge_asof(
        left,
        right,
        on="ts",
        direction="nearest",
        tolerance=pd.Timedelta("2h"),
    )
    return merged.dropna(subset=["pm_mid", "kalshi_mid"])


def load_venue_pairs(
    cache_dir: Optional[Path] = None,
    refresh: bool = False,
    min_bars: int = 48,
) -> List[VenuePair]:
    cache_dir = cache_dir or DEFAULT_CACHE
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_path = cache_dir / "btc_pair_aligned.parquet"
    meta_path = cache_dir / "btc_pair_meta.json"

    sess = requests.Session()
    pm = find_pm_btc_market(sess)
    kalshi = find_kalshi_btc_market(sess)
    if not pm or not kalshi:
        return []

    if cache_path.exists() and meta_path.exists() and not refresh:
        merged = pd.read_parquet(cache_path)
    else:
        merged = align_pair(pm, kalshi, sess)
        if len(merged) >= min_bars:
            merged.to_parquet(cache_path, index=False)
            meta_path.write_text(
                json.dumps({"pm": pm, "kalshi": kalshi}, indent=2),
                encoding="utf-8",
            )
        time.sleep(0.2)

    if len(merged) < min_bars:
        return []

    pair_id = f"PM:{pm['slug'][:24]}_K:{kalshi['ticker'][:24]}"
    return [
        VenuePair(
            pair_id=pair_id,
            pm_slug=pm.get("slug", "pm"),
            pm_token=pm.get("token_id", ""),
            kalshi_ticker=kalshi["ticker"],
            kalshi_series=kalshi["series_ticker"],
            aligned=merged,
        )
    ]
