#!/usr/bin/env python3
"""Pre-commit gate: audit every project upgrade queue.

`briefs/` is gitignored, so a hook that filters on staged paths never sees the
`briefs/*-upgrade-queue.md` files. This gate therefore reads the queues from
disk and audits all of them on every commit. It uses the `upgrade-queue` profile
of `scripts/skill_audit.py`, which runs only the two structural checks:
`required_sections` (``## Target`` + ``## Summary``) and `crosslinks` (every
``@wiki-alias/...`` reference must resolve).

Verdict handling:
  0 PASS   allowed
  1 WARN   allowed — the queues carry warnings today, and a work-in-progress
           queue must not block a commit
  2 REJECT failed — a queue lost a required section or cites a dead alias
  3 ERROR  failed — the auditor could not read the file

Exit codes:
  0 — every queue passed (PASS or WARN)
  1 — at least one queue failed

Usage:
  python3 scripts/precommit_upgrade_queues.py
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BRIEFS = ROOT / "briefs"
TAIL_LINES = 15


def audit_queue(path: Path) -> tuple[bool, str]:
    """Return (failed, output_tail) for one queue file."""
    proc = subprocess.run(
        [
            sys.executable,
            "scripts/skill_audit.py",
            "--profile",
            "upgrade-queue",
            "--no-vet",
            str(path),
        ],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    output = (proc.stdout or "") + (proc.stderr or "")
    tail = "\n".join(output.rstrip().splitlines()[-TAIL_LINES:])
    # 0 PASS and 1 WARN are allowed. 2 REJECT and 3 ERROR are failures.
    failed = proc.returncode not in (0, 1)
    return failed, tail


def main() -> int:
    queues = sorted(BRIEFS.glob("*-upgrade-queue.md"))
    if not queues:
        print("precommit_upgrade_queues: no upgrade queues found")
        return 0

    failed_files = []
    for path in queues:
        failed, tail = audit_queue(path)
        if failed:
            print(f"REJECT  {path.name}")
            print(tail)
            print()
            failed_files.append(path.name)

    print(
        f"precommit_upgrade_queues: {len(queues)} queue(s) checked, "
        f"{len(failed_files)} failed"
    )
    return 1 if failed_files else 0


if __name__ == "__main__":
    sys.exit(main())
