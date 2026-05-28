#!/usr/bin/env python3
"""Fetch Pyth OHLC history and emit CSV + PythTerminalCSV-style JSON reports.

Uses Pyth Pro History API when PYTH_TERMINAL_API_KEY is set (workspace `.env`);
falls back to public benchmarks otherwise.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
import re
import statistics
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

BENCHMARK_BASE = "https://benchmarks.pyth.network/v1/shims/tradingview/history"
PRO_BASE = "https://pyth.dourolabs.app/v1"
USER_AGENT = "Mozilla/5.0 (compatible; CeminiOSINT/1.0)"

# (canonical symbol for reports, slug, optional catalog symbol override)
DEFAULT_FEEDS: list[tuple[str, str]] = [
    ("Crypto.BTC/USD", "btc-usd"),
    ("Crypto.ETH/USD", "eth-usd"),
    ("Crypto.SOL/USD", "sol-usd"),
    ("Crypto.HYPE/USD", "hype-usd"),
    ("Equity.US.NVDA/USD", "nvda-usd"),
    ("Equity.US.SPY/USD", "spy-usd"),
    ("Metal.XAU/USD", "xau-usd"),
]


@dataclass
class FeedSpec:
    symbol: str
    slug: str
    channel: str
    api_symbol: str


@dataclass
class PriceRow:
    ts: str
    price: float


def load_dotenv(path: Path) -> None:
    if not path.is_file():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, val = line.split("=", 1)
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        os.environ.setdefault(key, val)


def workspace_root() -> Path:
    return Path(__file__).resolve().parents[1]


def get_api_key() -> str | None:
    for name in ("PYTH_TERMINAL_API_KEY", "PYTH_API_KEY"):
        val = os.environ.get(name, "").strip()
        if val:
            return val
    return None


def load_catalog(path: Path) -> dict[str, dict[str, str]]:
    if not path.is_file():
        return {}
    with path.open(newline="") as f:
        rows = list(csv.DictReader(f))
    return {r["symbol"]: r for r in rows if r.get("symbol")}


def api_symbol_from_catalog(row: dict[str, str]) -> str:
    asset = (row.get("asset_type") or "").lower()
    if asset in ("crypto", "metal", "fx", "commodity", "crypto-index"):
        return row["symbol"]
    # equities: Pro history expects short ticker (NVDA), not Equity.US.NVDA/USD
    return (row.get("nasdaq_symbol") or row.get("name") or row["symbol"]).strip()


def build_feed_specs(
    feeds: list[tuple[str, str]], catalog: dict[str, dict[str, str]]
) -> list[FeedSpec]:
    specs: list[FeedSpec] = []
    for symbol, slug in feeds:
        row = catalog.get(symbol, {})
        channel = row.get("min_channel") or "real_time"
        api_symbol = api_symbol_from_catalog(row) if row else symbol
        specs.append(FeedSpec(symbol, slug, channel, api_symbol))
    return specs


def http_get_json(url: str, headers: dict[str, str] | None = None) -> dict:
    hdrs = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    if headers:
        hdrs.update(headers)
    req = urllib.request.Request(url, headers=hdrs)
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read())


def fetch_history_benchmark(
    symbol: str, days: int, resolution: str
) -> tuple[dict, str]:
    now = int(time.time())
    frm = now - days * 86400
    q = urllib.parse.urlencode(
        {"symbol": symbol, "from": frm, "to": now, "resolution": resolution}
    )
    url = f"{BENCHMARK_BASE}?{q}"
    data = http_get_json(url)
    if data.get("s") != "ok":
        raise RuntimeError(
            f"benchmark {symbol}: {data.get('s')} {data.get('errmsg', data)}"
        )
    return data, BENCHMARK_BASE


def fetch_history_pro(
    spec: FeedSpec, days: int, resolution: str, api_key: str
) -> tuple[dict, str]:
    now = int(time.time())
    frm = now - days * 86400
    q = urllib.parse.urlencode(
        {
            "symbol": spec.api_symbol,
            "from": frm,
            "to": now,
            "resolution": resolution,
        }
    )
    channel_path = urllib.parse.quote(spec.channel, safe="@")
    url = f"{PRO_BASE}/{channel_path}/history?{q}"
    data = http_get_json(url, headers={"Authorization": f"Bearer {api_key}"})
    if data.get("s") != "ok":
        raise RuntimeError(
            f"pro {spec.symbol} ({spec.api_symbol}@{spec.channel}): "
            f"{data.get('s')} {data.get('errmsg', data)}"
        )
    source = f"{PRO_BASE}/{spec.channel}/history"
    return data, source


def fetch_history(
    spec: FeedSpec,
    days: int,
    resolution: str,
    source_mode: str,
    api_key: str | None,
) -> tuple[dict, str, str]:
    """Returns (ohlc_data, source_url, source_label)."""
    if source_mode == "benchmark":
        data, src = fetch_history_benchmark(spec.symbol, days, resolution)
        return data, src, "benchmark"

    if source_mode == "pro":
        if not api_key:
            raise RuntimeError("PYTH_TERMINAL_API_KEY required for --source pro")
        data, src = fetch_history_pro(spec, days, resolution, api_key)
        return data, src, "pro"

    # auto: pro first, benchmark fallback
    if api_key:
        try:
            data, src = fetch_history_pro(spec, days, resolution, api_key)
            return data, src, "pro"
        except Exception as exc:
            print(f"  pro fallback ({exc}) -> benchmark", flush=True)
    data, src = fetch_history_benchmark(spec.symbol, days, resolution)
    return data, src, "benchmark"


def verify_api_key(api_key: str) -> bool:
    try:
        http_get_json(f"{PRO_BASE}/live", headers={"Authorization": f"Bearer {api_key}"})
        return True
    except Exception:
        return False


def to_rows(data: dict) -> list[PriceRow]:
    rows: list[PriceRow] = []
    for ts, close in zip(data.get("t") or [], data.get("c") or []):
        if close is None:
            continue
        iso = datetime.fromtimestamp(int(ts), tz=timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%S.000Z"
        )
        rows.append(PriceRow(iso, float(close)))
    rows.sort(key=lambda r: r.ts)
    return rows


def percentile(values: list[float], p: float) -> float:
    if not values:
        return float("nan")
    s = sorted(values)
    idx = min(len(s) - 1, max(0, int((p / 100) * len(s))))
    return s[idx]


def analyze(rows: list[PriceRow], z_threshold: float = 3.0, largest_n: int = 10) -> dict:
    if len(rows) < 2:
        raise ValueError("Need at least 2 price rows")

    returns: list[float] = []
    moves: list[dict] = []
    for i in range(1, len(rows)):
        prev, cur = rows[i - 1], rows[i]
        lr = math.log(cur.price / prev.price)
        returns.append(lr)
        bps = ((cur.price - prev.price) / prev.price) * 10000
        moves.append(
            {
                "from": prev.ts,
                "to": cur.ts,
                "fromPrice": prev.price,
                "toPrice": cur.price,
                "absBps": abs(bps),
                "signedBps": bps,
            }
        )

    mu = statistics.mean(returns)
    sigma = statistics.pstdev(returns) if len(returns) > 1 else 0.0
    anomalies = []
    for i, m in enumerate(moves):
        z = 0.0 if sigma == 0 else (returns[i] - mu) / sigma
        if abs(z) >= z_threshold:
            anomalies.append({**m, "zScore": z})
    anomalies.sort(key=lambda x: abs(x["zScore"]), reverse=True)

    peak = rows[0].price
    max_dd = 0.0
    dd_start = rows[0].ts
    dd_end = rows[0].ts
    peak_ts = rows[0].ts
    for row in rows:
        if row.price > peak:
            peak = row.price
            peak_ts = row.ts
        dd = (row.price - peak) / peak
        if dd < max_dd:
            max_dd = dd
            dd_start = peak_ts
            dd_end = row.ts

    prices = [r.price for r in rows]
    abs_bps = [m["absBps"] for m in moves]
    largest = sorted(moves, key=lambda m: m["absBps"], reverse=True)[:largest_n]

    return {
        "sampleCount": len(rows),
        "window": {"from": rows[0].ts, "to": rows[-1].ts},
        "price": {
            "start": rows[0].price,
            "end": rows[-1].price,
            "min": min(prices),
            "max": max(prices),
            "rangePct": ((max(prices) - min(prices)) / rows[0].price) * 100,
        },
        "returns": {
            "meanLogReturn": mu,
            "stdevLogReturn": sigma,
            "p95AbsBpsMove": percentile(abs_bps, 95),
            "maxAbsBpsMove": max(abs_bps) if abs_bps else 0.0,
        },
        "drawdown": {
            "maxDrawdownPct": max_dd * 100,
            "from": dd_start,
            "to": dd_end,
        },
        "anomalyCount": len(anomalies),
        "topAnomalies": anomalies[:5],
        "largestMoves": largest,
    }


def write_csv(path: Path, rows: list[PriceRow]) -> None:
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["timestamp", "price"])
        for r in rows:
            w.writerow([r.ts, f"{r.price:.8f}".rstrip("0").rstrip(".")])


def main() -> int:
    root = workspace_root()
    load_dotenv(root / ".env")

    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--out-dir",
        type=Path,
        default=Path.home() / "Desktop" / "pyth-reports-2026-05-28",
    )
    ap.add_argument(
        "--catalog",
        type=Path,
        default=Path.home() / "Desktop" / "pyth-feeds-2026-05-28.csv",
        help="Terminal feed catalog export (channel + API symbol mapping)",
    )
    ap.add_argument(
        "--source",
        choices=("auto", "pro", "benchmark"),
        default="auto",
        help="auto=Pro when PYTH_TERMINAL_API_KEY set, else benchmark",
    )
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--resolution", default="5")
    ap.add_argument("--z", type=float, default=3.0)
    ap.add_argument("--verify-key", action="store_true", help="Ping Pro /v1/live and exit")
    args = ap.parse_args()

    api_key = get_api_key()
    if args.verify_key:
        if not api_key:
            print("No PYTH_TERMINAL_API_KEY in environment / .env")
            return 1
        ok = verify_api_key(api_key)
        print("PYTH_TERMINAL_API_KEY:", "OK" if ok else "FAILED")
        return 0 if ok else 1

    catalog = load_catalog(args.catalog)
    specs = build_feed_specs(DEFAULT_FEEDS, catalog)
    if api_key and args.source != "benchmark":
        print("Using Pyth Pro History API (PYTH_TERMINAL_API_KEY loaded)")
    else:
        print("Using benchmarks.pyth.network (no Pro key or --source benchmark)")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    index: list[dict] = []

    for spec in specs:
        print(
            f"Fetching {spec.symbol} "
            f"[api={spec.api_symbol} channel={spec.channel}] ...",
            flush=True,
        )
        try:
            raw, source_url, source_label = fetch_history(
                spec, args.days, args.resolution, args.source, api_key
            )
            rows = to_rows(raw)
            report = analyze(rows, z_threshold=args.z)
            csv_path = args.out_dir / f"{spec.slug}-5m-{args.days}d.csv"
            json_path = args.out_dir / f"{spec.slug}-5m-{args.days}d-report.json"
            write_csv(csv_path, rows)
            payload = {
                "symbol": spec.symbol,
                "apiSymbol": spec.api_symbol,
                "channel": spec.channel,
                "source": source_url,
                "sourceLabel": source_label,
                "config": {
                    "days": args.days,
                    "resolution": args.resolution,
                    "zThreshold": args.z,
                },
                "report": report,
            }
            json_path.write_text(json.dumps(payload, indent=2) + "\n")
            index.append(
                {
                    "symbol": spec.symbol,
                    "apiSymbol": spec.api_symbol,
                    "channel": spec.channel,
                    "source": source_label,
                    "slug": spec.slug,
                    "candles": len(rows),
                    "csv": str(csv_path),
                    "report": str(json_path),
                    "maxDrawdownPct": report["drawdown"]["maxDrawdownPct"],
                    "maxAbsBpsMove": report["returns"]["maxAbsBpsMove"],
                    "p95AbsBpsMove": report["returns"]["p95AbsBpsMove"],
                }
            )
            print(
                f"  OK [{source_label}] {len(rows)} candles | "
                f"maxDD {report['drawdown']['maxDrawdownPct']:.2f}% | "
                f"max move {report['returns']['maxAbsBpsMove']:.1f} bps"
            )
        except Exception as exc:
            print(f"  FAIL {exc}")
            index.append({"symbol": spec.symbol, "slug": spec.slug, "error": str(exc)})

    args.out_dir.joinpath("index.json").write_text(json.dumps(index, indent=2) + "\n")

    source_note = (
        "Pyth Pro (`PYTH_TERMINAL_API_KEY` from workspace `.env`)"
        if api_key and args.source != "benchmark"
        else "benchmarks.pyth.network (public)"
    )
    md_lines = [
        "# Pyth feed reports",
        "",
        f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        f"Window: last **{args.days} days**, **{args.resolution}m** bars",
        f"Source: {source_note}",
        "",
        "| Feed | Source | Candles | Max DD % | Max abs move (bps) | P95 (bps) |",
        "|------|--------|---------|----------|--------------------|-----------|",
    ]
    for item in index:
        if item.get("error"):
            md_lines.append(
                f"| {item['symbol']} | FAIL | — | — | {item['error'][:30]} | — |"
            )
        else:
            md_lines.append(
                f"| {item['symbol']} | {item.get('source', '?')} | {item['candles']} | "
                f"{item['maxDrawdownPct']:.2f} | {item['maxAbsBpsMove']:.1f} | "
                f"{item['p95AbsBpsMove']:.1f} |"
            )
    md_lines.extend(
        [
            "",
            "## Regenerate",
            "",
            "```bash",
            f"cd \"{root}\" && python3 scripts/pyth_feed_report.py",
            "```",
            "",
            "## Files",
            "",
        ]
    )
    for item in index:
        if not item.get("error"):
            md_lines.append(
                f"- `{Path(item['csv']).name}` + `{Path(item['report']).name}`"
            )
    args.out_dir.joinpath("README.md").write_text("\n".join(md_lines) + "\n")
    print(f"\nWrote {args.out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
