#!/usr/bin/env python3
"""Summarize postflop_decisions.jsonl — fold-to-cbet + row count.

Usage: summarize_postflop_log.py <postflop_decisions.jsonl>
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "examples"))

from postflop_telemetry import fold_to_cbet_rate  # noqa: E402


def _load_rows(path: Path) -> list[dict]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return rows


def main() -> int:
    if len(sys.argv) < 2:
        print(
            "usage: summarize_postflop_log.py <postflop_decisions.jsonl>",
            file=sys.stderr,
        )
        return 2
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"no such file: {path}", file=sys.stderr)
        return 2
    rows = _load_rows(path)
    stats = fold_to_cbet_rate(rows)
    print(
        f"rows={len(rows)} flop_facing={stats['flop_facing']} "
        f"fold={stats['fold']} call/raise={stats['call_raise']} "
        f"fold_to_cbet_rate={stats['fold_to_cbet_rate']:.2f}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
