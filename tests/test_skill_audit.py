"""Tests for the `--profile upgrade-queue` mode of scripts/skill_audit.py.

The profile must run only `required_sections` and `crosslinks`, so a missing
`## Target` / `## Summary` or an unresolvable wiki alias still REJECTs.
"""

import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RUN = [
    sys.executable,
    str(REPO / "scripts" / "skill_audit.py"),
    "--profile",
    "upgrade-queue",
    "--no-vet",
]


def _audit(tmp_path: Path, body: str) -> subprocess.CompletedProcess:
    path = tmp_path / "queue.md"
    path.write_text(body, encoding="utf-8")
    return subprocess.run(
        [*RUN, "--json", str(path)],
        cwd=str(REPO),
        capture_output=True,
        text=True,
        check=False,
    )


def test_missing_summary_rejects(tmp_path):
    proc = _audit(tmp_path, "# Queue\n\n## Target\nclaude.ai\n")
    assert proc.returncode == 2, proc.stdout + proc.stderr


def test_bad_alias_rejects(tmp_path):
    proc = _audit(
        tmp_path,
        "# Queue\n\n## Target\nclaude.ai\n\n## Summary\nRolling list.\n\n"
        "See @cybersec-wiki/concepts/x.md for the eval.\n",
    )
    assert proc.returncode == 2, proc.stdout + proc.stderr


def test_good_alias_passes(tmp_path):
    proc = _audit(
        tmp_path,
        "# Queue\n\n## Target\nclaude.ai\n\n## Summary\nRolling list.\n\n"
        "See @osint-wiki/index.md for the catalog.\n",
    )
    assert proc.returncode in (0, 1), proc.stdout + proc.stderr
