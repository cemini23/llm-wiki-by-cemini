#!/usr/bin/env python3
"""Merge UI-captured adjusted BB/100 snapshot into export dir + metrics.

Use when dev.fun shows the column in UI but API/export lack adjustedBbPer100
(ephemeral A/B — see briefs/2026-06-08_s1a-adjusted-bb100-ui-snapshot.md).

Usage:
  uv run python examples/import_bb100_snapshot.py \\
    --snapshot tests/fixtures/bb100_ui_snapshot_s1a_2026-06-08.json \\
    --export-dir reports/exports/playground-s1-live-archive/

  # Copy canonical snapshot into export dir for audit pack:
  uv run python examples/import_bb100_snapshot.py --snapshot path.json --export-dir DIR --install
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from export_bundle import apply_bb100_snapshot  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Import UI bb/100 snapshot into export dir")
    p.add_argument("--snapshot", type=Path, required=True, help="bb100_ui_snapshot JSON")
    p.add_argument("--export-dir", type=Path, required=True)
    p.add_argument(
        "--install",
        action="store_true",
        help="Copy snapshot to export-dir/bb100_ui_snapshot.json",
    )
    p.add_argument("--metrics", action="store_true", help="Run competition_metrics_report after merge")
    args = p.parse_args(argv)

    snap_path = args.snapshot.resolve()
    export_dir = args.export_dir.resolve()
    export_dir.mkdir(parents=True, exist_ok=True)

    raw = json.loads(snap_path.read_text(encoding="utf-8"))
    if args.install:
        dest = export_dir / "bb100_ui_snapshot.json"
        if snap_path != dest:
            shutil.copy2(snap_path, dest)
        print(f"Installed → {dest}")

    merged = apply_bb100_snapshot(export_dir, raw)
    meta = {
        "imported_at": datetime.now(timezone.utc).isoformat(),
        "source_snapshot": str(snap_path),
        "agents_with_bb100": sum(1 for a in merged if a.get("adjusted_bb100") is not None),
        "total_agents": len(merged),
        "hero_analysis": raw.get("hero_analysis"),
    }
    (export_dir / "bb100_snapshot_meta.json").write_text(
        json.dumps(meta, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(meta, indent=2))

    if args.metrics:
        import subprocess

        rc = subprocess.call(
            [sys.executable, str(_EXAMPLES / "competition_metrics_report.py"), str(export_dir)],
        )
        return rc
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
