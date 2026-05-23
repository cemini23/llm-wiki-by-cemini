#!/usr/bin/env python3
"""FLOX Phase 2 — continuous Polymarket CLOB market WS → intel:polymarket_flox_ws.

Run on cemini-librarian only. Uses the Phase 1b WS contract (Origin header, Gamma tokens).
Publishes Intel Bus envelope to prod Redis (REDIS_HOST=10.0.0.3 after private-net bind).

Env:
  REDIS_HOST, REDIS_PORT, REDIS_PASSWORD — prod Redis over Hetzner private net
  FLOX_PM_TOKEN_IDS — comma-separated clob token ids (optional)
  FLOX_PM_MARKET_COUNT — if no tokens, subscribe top N by Gamma volume24hr (default 8)
  FLOX_PM_REDIS_TTL — key TTL seconds (default 120)
  FLOX_PM_PUBLISH_INTERVAL_SEC — min seconds between Redis writes (default 1.0)
"""

from __future__ import annotations

import asyncio
import json
import logging
import os
import sys
import time
import urllib.request
from datetime import datetime, timezone
from typing import Any

try:
    import redis
except ImportError:
    print("pip install redis", file=sys.stderr)
    raise SystemExit(1) from None

LOG = logging.getLogger("flox_phase2")
INTEL_KEY = "intel:polymarket_flox_ws"
WS_URI = "wss://ws-subscriptions-clob.polymarket.com/ws/market"
GAMMA_MARKETS = (
    "https://gamma-api.polymarket.com/markets"
    "?active=true&closed=false&limit={limit}&order=volume24hr&ascending=false"
)
UA = "CeminiOSINT/1.0 flox-phase2"


def _env_int(name: str, default: int) -> int:
    raw = os.getenv(name)
    return int(raw) if raw else default


def _env_float(name: str, default: float) -> float:
    raw = os.getenv(name)
    return float(raw) if raw else default


def _redis_client() -> redis.Redis:
    host = os.getenv("REDIS_HOST", "10.0.0.3")
    port = int(os.getenv("REDIS_PORT", "6379"))
    password = os.getenv("REDIS_PASSWORD") or None
    return redis.Redis(
        host=host,
        port=port,
        password=password,
        decode_responses=True,
        socket_connect_timeout=5,
        socket_timeout=5,
    )


def _gamma_fetch_meta(limit: int) -> dict[str, dict[str, Any]]:
    """token_id -> {question, volume24hr, condition_id, outcome}."""
    url = GAMMA_MARKETS.format(limit=limit)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        markets = json.loads(resp.read().decode())
    meta: dict[str, dict[str, Any]] = {}
    for m in markets:
        try:
            ids = json.loads(m.get("clobTokenIds") or "[]")
        except json.JSONDecodeError:
            continue
        if not ids:
            continue
        vol = float(m.get("volume24hr") or 0)
        question = m.get("question") or m.get("slug") or ""
        cond = m.get("conditionId") or m.get("condition_id") or ""
        for i, tid in enumerate(ids[:2]):
            meta[str(tid)] = {
                "question": question,
                "volume24hr": vol,
                "condition_id": cond,
                "outcome_index": i,
            }
    return meta


def _token_ids() -> list[str]:
    explicit = os.getenv("FLOX_PM_TOKEN_IDS", "").strip()
    if explicit:
        return [t.strip() for t in explicit.split(",") if t.strip()]
    count = _env_int("FLOX_PM_MARKET_COUNT", 8)
    url = GAMMA_MARKETS.format(limit=max(count + 4, 12))
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        markets = json.loads(resp.read().decode())
    tokens: list[str] = []
    for m in markets:
        try:
            ids = json.loads(m.get("clobTokenIds") or "[]")
        except json.JSONDecodeError:
            continue
        if ids:
            tokens.append(str(ids[0]))
        if len(tokens) >= count:
            break
    if not tokens:
        raise RuntimeError("no token ids resolved from Gamma")
    return tokens


def _top_of_book(item: dict[str, Any]) -> tuple[float | None, float | None]:
    bids = item.get("bids") or []
    asks = item.get("asks") or []
    best_bid = float(bids[0]["price"]) if bids and isinstance(bids[0], dict) else None
    best_ask = float(asks[0]["price"]) if asks and isinstance(asks[0], dict) else None
    return best_bid, best_ask


def _normalize_book(item: dict[str, Any], meta: dict[str, Any]) -> dict[str, Any] | None:
    asset_id = str(item.get("asset_id") or "")
    if not asset_id and not (item.get("bids") or item.get("asks")):
        et = item.get("event_type")
        if et not in ("book", "price_change", None):
            return None
    if not asset_id:
        return None
    m = meta.get(asset_id, {})
    best_bid, best_ask = _top_of_book(item)
    if best_bid is None and best_ask is None:
        return None
    yes_price = best_bid if best_bid is not None else (best_ask or 0.5)
    return {
        "asset_id": asset_id,
        "market_id": item.get("market") or m.get("condition_id") or asset_id[:16],
        "question": m.get("question") or "",
        "best_bid": best_bid,
        "best_ask": best_ask,
        "yes_price": yes_price,
        "volume_24h": float(m.get("volume24hr") or 0),
        "timestamp": item.get("timestamp"),
        "event_type": item.get("event_type") or "book",
    }


def _is_book_like(item: dict[str, Any]) -> bool:
    et = item.get("event_type") or item.get("type")
    if et in ("book", "price_change", "last_trade_price", "trade"):
        return True
    return bool(item.get("bids") or item.get("asks") or item.get("asset_id"))


class Phase2State:
    def __init__(self, meta: dict[str, dict[str, Any]]) -> None:
        self.meta = meta
        self.books: dict[str, dict[str, Any]] = {}
        self.seq = 0
        self.last_publish = 0.0
        self.messages = 0

    def apply(self, raw: str) -> None:
        if raw.strip() in ("[]", ""):
            return
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError:
            return
        items = payload if isinstance(payload, list) else [payload]
        for item in items:
            if not isinstance(item, dict) or not _is_book_like(item):
                continue
            norm = _normalize_book(item, self.meta)
            if norm:
                self.books[norm["asset_id"]] = norm
                self.messages += 1

    def snapshot(self, token_ids: list[str]) -> dict[str, Any]:
        self.seq += 1
        books = list(self.books.values())
        return {
            "status": "live",
            "impl": "flox_phase2_ws_publish",
            "books": books,
            "subscribed_tokens": token_ids,
            "book_count": len(books),
            "seq": self.seq,
            "ws_messages": self.messages,
        }


def _publish(r: redis.Redis, snapshot: dict[str, Any], ttl: int) -> None:
    envelope = {
        "value": snapshot,
        "source_system": "flox_phase2_librarian",
        "timestamp": time.time(),
        "confidence": 1.0,
        "updated_at": datetime.now(tz=timezone.utc).isoformat(),
    }
    r.set(INTEL_KEY, json.dumps(envelope), ex=ttl)
    LOG.info(
        "published %s books=%s seq=%s",
        INTEL_KEY,
        snapshot.get("book_count"),
        snapshot.get("seq"),
    )


async def _ws_loop(
    token_ids: list[str],
    state: Phase2State,
    r: redis.Redis,
    ttl: int,
    publish_interval: float,
) -> None:
    import websockets

    sub = {"assets_ids": token_ids, "type": "market", "operation": "subscribe"}
    headers = {"Origin": "https://polymarket.com"}
    backoff = 2.0

    def _connect():
        try:
            return websockets.connect(
                WS_URI, ping_interval=20, additional_headers=headers
            )
        except TypeError:
            return websockets.connect(
                WS_URI, ping_interval=20, extra_headers=headers
            )

    while True:
        try:
            async with _connect() as ws:
                LOG.info("connected tokens=%s", len(token_ids))
                await ws.send(json.dumps(sub))
                backoff = 2.0
                while True:
                    try:
                        raw = await asyncio.wait_for(ws.recv(), timeout=30.0)
                    except asyncio.TimeoutError:
                        # heartbeat publish on quiet markets
                        now = time.monotonic()
                        if now - state.last_publish >= publish_interval:
                            _publish(r, state.snapshot(token_ids), ttl)
                            state.last_publish = now
                        continue
                    state.apply(raw)
                    now = time.monotonic()
                    if now - state.last_publish >= publish_interval:
                        _publish(r, state.snapshot(token_ids), ttl)
                        state.last_publish = now
        except Exception as exc:
            LOG.warning("ws error: %s — reconnect in %.0fs", exc, backoff)
            await asyncio.sleep(backoff)
            backoff = min(backoff * 1.5, 60.0)


def main() -> int:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )
    ttl = _env_int("FLOX_PM_REDIS_TTL", 120)
    publish_interval = _env_float("FLOX_PM_PUBLISH_INTERVAL_SEC", 1.0)

    token_ids = _token_ids()
    LOG.info("subscribing to %s tokens", len(token_ids))

    meta = _gamma_fetch_meta(_env_int("FLOX_PM_MARKET_COUNT", 8) * 3)
    for tid in token_ids:
        meta.setdefault(tid, {"question": tid[:12], "volume24hr": 0, "condition_id": ""})

    r = _redis_client()
    try:
        r.ping()
    except Exception as exc:
        LOG.error("redis ping failed: %s", exc)
        return 1

    state = Phase2State(meta)
    # initial publish so prod can enable Phase 2
    snap = state.snapshot(token_ids)
    snap["status"] = "starting"
    _publish(r, snap, ttl)

    asyncio.run(_ws_loop(token_ids, state, r, ttl, publish_interval))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
