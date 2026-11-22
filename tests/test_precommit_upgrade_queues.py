"""Test the upgrade-queue pre-commit gate against the real queues.

`briefs/` is gitignored, so the gate must read the queues from disk. This test
runs it exactly as the hook does, from the repo root.
"""

import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def test_real_queues_pass():
    proc = subprocess.run(
        [sys.executable, "scripts/precommit_upgrade_queues.py"],
        cwd=str(REPO),
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "queue(s) checked" in proc.stdout
