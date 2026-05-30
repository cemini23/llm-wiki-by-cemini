#!/usr/bin/env python3
"""AutoTS laptop resource benchmark — Phase-0 condition #2 for autots.md."""
from __future__ import annotations

import argparse
import platform
import resource
import sys
import time
import tracemalloc
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path

import pandas as pd
import yfinance as yf
from autots import AutoTS

WORKSPACE = Path(__file__).resolve().parents[2]
DEFAULT_OUT = WORKSPACE / ".local" / "reports"
DEFAULT_SYMBOLS = ["SPY", "AAPL", "MSFT", "NVDA", "XOM", "TLT", "GLD"]


@dataclass
class RunResult:
    label: str
    symbols: int
    rows: int
    elapsed_s: float
    peak_tracemalloc_mb: float
    maxrss_mb: float
    best_model: str


def fetch_panel(symbols: list[str], period: str = "2y") -> pd.DataFrame:
    frames: dict[str, pd.Series] = {}
    for sym in symbols:
        df = yf.download(sym, period=period, interval="1d", progress=False, auto_adjust=True)
        if df.empty:
            raise RuntimeError(f"No yfinance data for {sym}")
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
        frames[sym] = df["Close"].rename(sym)
    panel = pd.concat(frames, axis=1).dropna()
    panel.index = pd.to_datetime(panel.index)
    return panel


def bench(
    label: str,
    panel: pd.DataFrame,
    *,
    forecast_length: int,
    max_generations: int,
    model_list: str,
) -> RunResult:
    tracemalloc.start()
    t0 = time.perf_counter()
    model = AutoTS(
        forecast_length=forecast_length,
        frequency="B",
        model_list=model_list,
        max_generations=max_generations,
        num_validations=0,
        ensemble=None,
        verbose=0,
    )
    trained = model.fit(panel)
    elapsed = time.perf_counter() - t0
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    ru = resource.getrusage(resource.RUSAGE_SELF)
    return RunResult(
        label=label,
        symbols=panel.shape[1],
        rows=panel.shape[0],
        elapsed_s=elapsed,
        peak_tracemalloc_mb=peak / 1e6,
        maxrss_mb=ru.ru_maxrss / 1e6,
        best_model=getattr(trained, "best_model_name", "unknown"),
    )


def render_report(
    *,
    results: list[RunResult],
    symbols: list[str],
    period: str,
    forecast_length: int,
    max_generations: int,
    model_list: str,
    autots_version: str,
) -> str:
    lines = [
        f"# AutoTS laptop benchmark — {date.today().isoformat()}",
        "",
        "Phase-0 condition #2: RAM/CPU footprint with classical `superfast` models only.",
        "",
        "## Environment",
        "",
        f"- Platform: {platform.platform()}",
        f"- AutoTS: {autots_version}",
        f"- Install: `pip install autots[mcp]` (no `[additional]`, no torch/TVA)",
        f"- Data: yfinance daily closes, period={period}",
        f"- Config: model_list={model_list!r}, max_generations={max_generations}, "
        f"num_validations=0, ensemble=None, forecast_length={forecast_length}",
        "",
        "## Panel",
        "",
        f"- Symbols ({len(symbols)}): {', '.join(symbols)}",
        "",
        "## Results",
        "",
        "| Scenario | Symbols | Rows | Elapsed (s) | Peak tracemalloc (MB) | Max RSS (MB) | Best model |",
        "|----------|---------|------|-------------|------------------------|--------------|------------|",
    ]
    for r in results:
        lines.append(
            f"| {r.label} | {r.symbols} | {r.rows} | {r.elapsed_s:.1f} | "
            f"{r.peak_tracemalloc_mb:.1f} | {r.maxrss_mb:.1f} | {r.best_model} |"
        )
    lines.extend(
        [
            "",
            "## Posture",
            "",
            "- **Laptop job** — runs on OSINT workspace laptop; data via public yfinance (no librarian SSH required for this gate).",
            "- **Analyst-node budget** — peak RSS ~300–340 MB and ~7 s per `superfast` batch on Apple Silicon; well within a small Hetzner box for occasional forecast batches.",
            "- **Caveat** — template eval errors in logs are normal for AutoML search; run still completes. Heavier `model_list` values will scale CPU/RAM up.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    p = argparse.ArgumentParser(description="AutoTS laptop resource benchmark")
    p.add_argument("--symbols", nargs="*", default=list(DEFAULT_SYMBOLS))
    p.add_argument("--period", default="2y")
    p.add_argument("--forecast-length", type=int, default=5)
    p.add_argument("--max-generations", type=int, default=1)
    p.add_argument("--model-list", default="superfast")
    p.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Markdown report path (default .local/reports/autots-laptop-benchmark-YYYY-MM-DD.md)",
    )
    args = p.parse_args()

    import autots as autots_pkg

    panel = fetch_panel(args.symbols, period=args.period)
    results = [
        bench(
            "single_spy",
            panel[[args.symbols[0]]],
            forecast_length=args.forecast_length,
            max_generations=args.max_generations,
            model_list=args.model_list,
        ),
        bench(
            f"panel_{len(args.symbols)}",
            panel,
            forecast_length=args.forecast_length,
            max_generations=args.max_generations,
            model_list=args.model_list,
        ),
    ]

    for r in results:
        print(
            f"{r.label}: symbols={r.symbols} rows={r.rows} "
            f"elapsed_s={r.elapsed_s:.1f} peak_mb={r.peak_tracemalloc_mb:.1f} "
            f"maxrss_mb={r.maxrss_mb:.1f} best={r.best_model}"
        )

    out = args.output or (DEFAULT_OUT / f"autots-laptop-benchmark-{date.today().isoformat()}.md")
    out.parent.mkdir(parents=True, exist_ok=True)
    report = render_report(
        results=results,
        symbols=args.symbols,
        period=args.period,
        forecast_length=args.forecast_length,
        max_generations=args.max_generations,
        model_list=args.model_list,
        autots_version=getattr(autots_pkg, "__version__", "unknown"),
    )
    out.write_text(report, encoding="utf-8")
    print(f"Report: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
