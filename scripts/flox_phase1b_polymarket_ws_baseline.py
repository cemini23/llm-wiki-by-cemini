#!/usr/bin/env python3
"""Python baseline: Polymarket CLOB market WS ingest (Step 197 Phase 1b)."""

from __future__ import annotations

import argparse
import asyncio
import json
import time
from pathlib import Path


def _is_book_like(item: dict) -> bool:
    et = item.get("event_type") or item.get("type")
    if et in ("book", "price_change", "last_trade_price", "trade"):
        return True
    return bool(item.get("bids") or item.get("asks") or item.get("asset_id"))


async def run(token_id: str, duration_sec: int) -> dict:
    import websockets

    uri = "wss://ws-subscriptions-clob.polymarket.com/ws/market"
    sub = {"assets_ids": [token_id], "type": "market", "operation": "subscribe"}
    headers = {"Origin": "https://polymarket.com"}

    t0 = time.perf_counter()
    book_updates = 0
    raw_messages = 0
    t_first_book_ms: float | None = None

    async with websockets.connect(uri, ping_interval=20, extra_headers=headers) as ws:
        t_connected_ms = (time.perf_counter() - t0) * 1000
        await ws.send(json.dumps(sub))
        deadline = time.perf_counter() + duration_sec

        while time.perf_counter() < deadline:
            try:
                raw = await asyncio.wait_for(ws.recv(), timeout=5.0)
            except asyncio.TimeoutError:
                continue
            if raw.strip() in ("[]", ""):
                continue
            raw_messages += 1
            try:
                payload = json.loads(raw)
            except json.JSONDecodeError:
                continue
            items = payload if isinstance(payload, list) else [payload]
            for item in items:
                if not isinstance(item, dict):
                    continue
                if not _is_book_like(item):
                    continue
                book_updates += 1
                if t_first_book_ms is None:
                    t_first_book_ms = (time.perf_counter() - t0) * 1000

    elapsed = time.perf_counter() - t0
    return {
        "impl": "python-websockets",
        "token_id": token_id,
        "duration_sec": duration_sec,
        "connect_ms": round(t_connected_ms, 2),
        "first_book_ms": round(t_first_book_ms, 2) if t_first_book_ms else None,
        "raw_messages": raw_messages,
        "book_updates": book_updates,
        "updates_per_sec": round(book_updates / max(elapsed, 0.001), 2),
        "elapsed_sec": round(elapsed, 2),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--token-id", required=True)
    parser.add_argument("--duration", type=int, default=60)
    parser.add_argument("--out", type=Path, default=Path("flox_phase1b_python.json"))
    args = parser.parse_args()

    report = asyncio.run(run(args.token_id, args.duration))
    args.out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["book_updates"] > 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
