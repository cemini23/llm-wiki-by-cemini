#!/usr/bin/env python3
"""Merge JSONL shards from librarian/egress harvest workers into prod canonical dir."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from export_competition_hands import _append_chip_delta_sidecar, _append_jsonl  # noqa: E402


def _merge_file(
    canonical_dir: Path,
    worker_dir: Path,
    name: str,
    dedupe_key: str,
) -> int:
    src = worker_dir / name
    if not src.is_file():
        return 0
    rows: list[dict] = []
    for line in src.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    if not rows:
        return 0
    return _append_jsonl(canonical_dir / name, rows, dedupe_key)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Merge harvest worker JSONL into canonical export")
    p.add_argument(
        "--canonical",
        required=True,
        help="Canonical export dir (e.g. reports/exports/s1-tournament-live)",
    )
    p.add_argument(
        "--worker",
        action="append",
        default=[],
        help="Worker export dir (repeat for each host)",
    )
    args = p.parse_args(argv)

    canonical = Path(args.canonical)
    canonical.mkdir(parents=True, exist_ok=True)
    totals: dict[str, int] = {}

    for worker in args.worker:
        wdir = Path(worker)
        if not wdir.is_dir():
            print(f"WARN: skip missing worker dir {wdir}", file=sys.stderr)
            continue
        label = wdir.name
        for fname, key in (
            ("submissions.jsonl", "submission_id"),
            ("submissions-all.jsonl", "submission_id"),
            ("agents-all.jsonl", "agent_id"),
            ("tables.jsonl", "table_id"),
            ("chip_deltas.jsonl", "submission_id"),
        ):
            n = _merge_file(canonical, wdir, fname, key)
            if n:
                totals[f"{label}/{fname}"] = n

        chip_sidecar = wdir / "submissions.jsonl"
        if chip_sidecar.is_file():
            subs = []
            for line in chip_sidecar.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    subs.append(json.loads(line))
            n = _append_chip_delta_sidecar(canonical, subs)
            if n:
                totals[f"{label}/chip_deltas-sidecar"] = n

    print(json.dumps({"merged": totals, "canonical": str(canonical)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
