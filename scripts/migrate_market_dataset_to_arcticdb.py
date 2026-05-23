#!/usr/bin/env python3
"""Migrate cemini-bulk market-dataset CSV/txt files into a persistent ArcticDB LMDB store.

Run on cemini-librarian:

  /opt/cemini-bulk/.venv/bin/python migrate_market_dataset_to_arcticdb.py \\
    --data-root /opt/cemini-bulk/market-dataset \\
    --store-uri lmdb:///opt/cemini-bulk/arctic-market-dataset \\
    --library equity_bars

Dry-run first:

  ... --dry-run --limit 20
"""

from __future__ import annotations

import argparse
import json
import re
import time
from pathlib import Path

SKIP_PARTS = {"__MACOSX", ".git"}
SKIP_PREFIX = "._"


def _symbol_from_path(path: Path) -> str:
    stem = path.stem
    stem = re.sub(r"_data$", "", stem, flags=re.I)
    stem = re.sub(r"\.us$", "", stem, flags=re.I)
    return stem.upper()


def _load_table(path: Path):
    import pandas as pd

    if path.suffix.lower() == ".csv":
        df = pd.read_csv(path)
    else:
        df = pd.read_csv(path)  # .txt OHLCV

    cols = {c.lower(): c for c in df.columns}
    date_col = None
    for key in ("date", "datetime", "timestamp", "ts"):
        if key in cols:
            date_col = cols[key]
            break
    if date_col is None:
        date_col = df.columns[0]

    df[date_col] = pd.to_datetime(df[date_col], errors="coerce", utc=True)
    df = df.dropna(subset=[date_col])
    df = df.sort_values(date_col)
    df = df.set_index(date_col)
    return df


def _iter_files(data_root: Path):
    for path in sorted(data_root.rglob("*")):
        if not path.is_file():
            continue
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        if path.name.startswith(SKIP_PREFIX):
            continue
        if path.suffix.lower() not in {".csv", ".txt"}:
            continue
        yield path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-root", type=Path, required=True)
    parser.add_argument(
        "--store-uri",
        type=str,
        default="lmdb:///opt/cemini-bulk/arctic-market-dataset",
    )
    parser.add_argument("--library", type=str, default="equity_bars")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=0, help="Max files (0 = all)")
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("/opt/cemini-bulk/research/cemini-handoff/briefs/market_dataset_arctic_migration.json"),
    )
    args = parser.parse_args()

    files = list(_iter_files(args.data_root))
    if args.limit:
        files = files[: args.limit]

    report: dict = {
        "data_root": str(args.data_root),
        "store_uri": args.store_uri,
        "library": args.library,
        "dry_run": args.dry_run,
        "n_files": len(files),
        "written": 0,
        "skipped": 0,
        "errors": [],
        "total_rows": 0,
    }

    if args.dry_run:
        for f in files[:10]:
            report.setdefault("sample", []).append(
                {"path": str(f), "symbol": _symbol_from_path(f)}
            )
        print(json.dumps(report, indent=2))
        return 0

    from arcticdb import Arctic

    ac = Arctic(args.store_uri)
    if args.library in ac.list_libraries():
        lib = ac.get_library(args.library)
    else:
        lib = ac.create_library(args.library)

    seen_symbols: set[str] = set()
    t0 = time.perf_counter()

    for path in files:
        sym = _symbol_from_path(path)
        if sym in seen_symbols:
            report["skipped"] += 1
            continue
        try:
            df = _load_table(path)
            if df.empty:
                report["skipped"] += 1
                continue
            lib.write(sym, df)
            seen_symbols.add(sym)
            report["written"] += 1
            report["total_rows"] += len(df)
        except Exception as exc:  # noqa: BLE001
            msg = str(exc)
            if "No columns to parse" in msg or "EmptyDataError" in msg:
                report["skipped"] += 1
                continue
            report["errors"].append({"path": str(path), "error": msg[:200]})
            if len(report["errors"]) > 50:
                break

    report["elapsed_s"] = round(time.perf_counter() - t0, 1)
    report["unique_symbols"] = len(seen_symbols)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if len(report["errors"]) <= 50 else 1


if __name__ == "__main__":
    raise SystemExit(main())
