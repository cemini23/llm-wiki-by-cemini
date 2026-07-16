#!/usr/bin/env python3
"""XSP Ops Loop CLI — seven roles + full loop.

Usage:
  python3 scripts/xsp_ops/cli.py <role> [--dry-run]
  python3 -m xsp_ops.cli <role> [--dry-run]   # with scripts/ on PYTHONPATH

Roles: sensor | parse | land | enqueue | triage | packet | scale | loop
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Ensure scripts/ is on path for xsp_ops + intel.core
_SCRIPTS = Path(__file__).resolve().parents[1]
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from xsp_ops.enqueue import run_enqueue  # noqa: E402
from xsp_ops.land import run_land  # noqa: E402
from xsp_ops.packet import run_packet  # noqa: E402
from xsp_ops.parse_post import run_parse  # noqa: E402
from xsp_ops.paths import ensure_layout  # noqa: E402
from xsp_ops.scale import run_scale  # noqa: E402
from xsp_ops.sensor import run_sensor  # noqa: E402
from xsp_ops.triage import run_triage  # noqa: E402

ROLES = ("sensor", "parse", "land", "enqueue", "triage", "packet", "scale", "loop")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="XSP Ops Loop — Macro Charts sensor → brain → queue → packets",
    )
    p.add_argument(
        "role",
        choices=ROLES,
        help="Ops role to run (loop = sensor→…→scale)",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="No network / no durable writes where applicable; print plan",
    )
    p.add_argument(
        "--ops-root",
        type=Path,
        default=None,
        help="Override ops root (tests); else .local/ops/xsp/",
    )
    return p


def run_role(role: str, *, dry_run: bool = False, root: Path | None = None) -> int:
    ensure_layout(root)
    if role == "sensor":
        out = run_sensor(dry_run=dry_run, root=root)
        return 0 if out.get("ok", True) or dry_run else int(out.get("exit_code") or 1)
    if role == "parse":
        run_parse(dry_run=dry_run, root=root)
        return 0
    if role == "land":
        run_land(dry_run=dry_run, root=root)
        return 0
    if role == "enqueue":
        run_enqueue(dry_run=dry_run, root=root)
        return 0
    if role == "triage":
        run_triage(dry_run=dry_run, root=root)
        return 0
    if role == "packet":
        run_packet(dry_run=dry_run, root=root)
        return 0
    if role == "scale":
        run_scale(dry_run=dry_run, root=root)
        return 0
    if role == "loop":
        for r in ("sensor", "parse", "land", "enqueue", "triage", "packet", "scale"):
            print(f"--- loop:{r} ---")
            code = run_role(r, dry_run=dry_run, root=root)
            if code != 0 and r == "sensor" and not dry_run:
                # Continue loop even if sensor fails (offline); other roles still useful
                print(f"[loop] sensor returned {code}; continuing", file=sys.stderr)
        return 0
    raise ValueError(f"unknown role: {role}")


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    root = args.ops_root
    if root is not None:
        root = root.resolve()
        # Point path module env for nested imports that read OPS_ROOT at call time
        # Most roles accept root= explicitly.
    return run_role(args.role, dry_run=args.dry_run, root=root)


if __name__ == "__main__":
    raise SystemExit(main())
