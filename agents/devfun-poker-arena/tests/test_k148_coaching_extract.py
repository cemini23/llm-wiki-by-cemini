"""K148 sanitize_untrusted_text + coaching_video_extract."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SANITIZE = ROOT / "scripts" / "sanitize_untrusted_text.py"
EXTRACT = ROOT / "scripts" / "coaching_video_extract.py"
CLEAN = ROOT / "tests" / "fixtures" / "coaching_transcript_clean.txt"
INJECT = ROOT / "tests" / "fixtures" / "coaching_transcript_injection.txt"


def _run(script: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(script), *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def test_sanitize_clean_passes():
    r = _run(SANITIZE, str(CLEAN), "--gate", "--json")
    assert r.returncode == 0, r.stderr
    data = json.loads(r.stdout)
    assert data["ok"] is True


def test_sanitize_injection_fails_gate():
    r = _run(SANITIZE, str(INJECT), "--gate", "--json")
    assert r.returncode == 1
    data = json.loads(r.stdout)
    assert data["ok"] is False
    assert data["hit_count"] >= 1


def test_coaching_extract_builds_candidate(tmp_path: Path):
    r = _run(
        EXTRACT,
        "--transcript-file",
        str(CLEAN),
        "--slug",
        "test-clean",
        "--out-dir",
        str(tmp_path),
        "--gate",
        "--json",
    )
    assert r.returncode == 0, r.stderr + r.stdout
    data = json.loads(r.stdout)
    md = tmp_path / "test-clean.strategy-candidate.md"
    assert md.is_file()
    body = md.read_text()
    assert "UNTRUSTED" in body
    assert "c-bet" in body.lower() or "cbet" in body.lower()
    assert data["pattern_counts"]["preflop_lines"] >= 1
