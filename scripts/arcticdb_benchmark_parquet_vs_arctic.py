#!/usr/bin/env python3
"""Step 189 — Parquet/CSV vs ArcticDB throughput benchmark.

Run on cemini-librarian where `/opt/cemini-bulk/market-dataset/` lives:

  /opt/cemini-bulk/.venv/bin/python benchmark_parquet_vs_arctic.py \\
    --data-root /opt/cemini-bulk/market-dataset/Stocks \\
    --symbol AAPL --max-files 5

On prod VPS without bulk data, use `--synthetic` for methodology smoke only.
"""

from __future__ import annotations

import argparse
import json
import os
import tempfile
import time
from pathlib import Path


def _synthetic_parquet_dir(root: Path, n_files: int = 3, rows: int = 50_000) -> Path:
    import pandas as pd
    import numpy as np

    root.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(42)
    for i in range(n_files):
        df = pd.DataFrame(
            {
                "ts": pd.date_range("2024-01-01", periods=rows, freq="min"),
                "open": 100 + rng.standard_normal(rows).cumsum() * 0.01,
                "high": 101 + rng.standard_normal(rows).cumsum() * 0.01,
                "low": 99 + rng.standard_normal(rows).cumsum() * 0.01,
                "close": 100 + rng.standard_normal(rows).cumsum() * 0.01,
                "volume": rng.integers(100, 10_000, rows),
            },
        )
        df.to_parquet(root / f"SYM_part{i}.parquet", index=False)
    return root


def _bench_parquet(files: list[Path], *, max_rows: int | None = None) -> dict:
    import pandas as pd

    t0 = time.perf_counter()
    frames = []
    for f in files:
        if f.suffix.lower() == ".csv":
            frames.append(pd.read_csv(f, nrows=max_rows))
        else:
            frames.append(pd.read_parquet(f))
    read_s = time.perf_counter() - t0
    rows = sum(len(f) for f in frames)
    t1 = time.perf_counter()
    combined = pd.concat(frames, ignore_index=True)
    ts_col = "ts" if "ts" in combined.columns else combined.columns[0]
    _ = combined.sort_values(ts_col).tail(1000)
    query_s = time.perf_counter() - t1
    return {"rows": rows, "read_s": round(read_s, 3), "tail_query_s": round(query_s, 3)}


def _bench_arctic(
    files: list[Path],
    lib_name: str = "step189_bench",
    *,
    max_rows: int | None = None,
) -> dict:
    import pandas as pd
    from arcticdb import Arctic

    with tempfile.TemporaryDirectory() as tmp:
        uri = f"lmdb://{tmp}"
        ac = Arctic(uri)
        if lib_name in ac.list_libraries():
            ac.delete_library(lib_name)
        lib = ac.create_library(lib_name)

        t0 = time.perf_counter()
        for i, f in enumerate(files):
            if f.suffix.lower() == ".csv":
                df = pd.read_csv(f, nrows=max_rows)
            else:
                df = pd.read_parquet(f)
            lib.write(f"sym/part{i}", df)
        write_s = time.perf_counter() - t0

        t1 = time.perf_counter()
        total_rows = 0
        for i in range(len(files)):
            total_rows += len(lib.read(f"sym/part{i}").data)
        read_s = time.perf_counter() - t1

        t2 = time.perf_counter()
        last = lib.read(f"sym/part{len(files) - 1}").data.tail(1000)
        _ = len(last)
        tail_s = time.perf_counter() - t2

    return {
        "rows": total_rows,
        "write_s": round(write_s, 3),
        "read_all_s": round(read_s, 3),
        "tail_s": round(tail_s, 3),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-root", type=Path, help="Directory of parquet files")
    parser.add_argument("--symbol", default="", help="Filter filenames containing symbol")
    parser.add_argument("--max-files", type=int, default=5)
    parser.add_argument("--synthetic", action="store_true")
    parser.add_argument(
        "--csv-file",
        type=Path,
        help="Single CSV benchmark (librarian all_stocks_5yr.csv style)",
    )
    parser.add_argument(
        "--max-rows",
        type=int,
        default=200_000,
        help="Row cap for CSV reads (default 200k)",
    )
    parser.add_argument("--out", type=Path, default=Path("briefs/step189_arcticdb_benchmark.json"))
    args = parser.parse_args()

    if args.csv_file:
        csv_path = args.csv_file
        if not csv_path.exists():
            print(f"Missing {csv_path}")
            return 1
        files = [csv_path]
        mode = "live-csv"
        data_root = csv_path.parent
    elif args.synthetic:
        data_root = Path(tempfile.mkdtemp(prefix="step189_"))
        _synthetic_parquet_dir(data_root, n_files=args.max_files)
        mode = "synthetic"
    elif args.data_root:
        data_root = args.data_root
        mode = "live"
    else:
        print("Provide --data-root, --csv-file, or --synthetic")
        return 1

    if not args.csv_file:
        files = sorted(data_root.glob("**/*.parquet"))[: args.max_files]
        if args.symbol:
            files = [f for f in files if args.symbol in f.name][: args.max_files]
    if not files:
        print(f"No parquet under {data_root}")
        return 1

    report = {
        "mode": mode,
        "data_root": str(data_root),
        "n_files": len(files),
        "parquet": _bench_parquet(files, max_rows=args.max_rows),
    }
    try:
        report["arcticdb"] = _bench_arctic(files, max_rows=args.max_rows)
        report["arcticdb_available"] = True
    except ImportError:
        report["arcticdb_available"] = False
        report["arcticdb_error"] = "pip install arcticdb pandas pyarrow"

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
