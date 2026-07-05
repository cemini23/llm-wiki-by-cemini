"""K146 docs_cli — AST projection + substrate audit."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "docs_cli.py"


def _run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(CLI), *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def test_module_lists_decide():
    r = _run("module", "examples/cemini_decide.py")
    assert r.returncode == 0
    assert "def decide" in r.stdout


def test_symbol_decide_docstring():
    r = _run("symbol", "examples/cemini_decide.py", "decide")
    assert r.returncode == 0
    assert "decide" in r.stdout.lower()


def test_audit_gate_passes_on_repo(tmp_path: Path):
    r = _run("audit", "--gate", "--out-dir", str(tmp_path))
    assert r.returncode == 0, r.stdout + r.stderr
    data = json.loads((tmp_path / "substrate_audit.json").read_text())
    assert data["gate_pass"] is True
    assert "examples/cemini_decide.py" in data["checked"]
    assert (tmp_path / "substrate_topology.txt").is_file()


def test_prepare_reviewer_pack(tmp_path: Path):
    import subprocess

    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "prepare_substrate_reviewer_pack.py"),
         "--out", str(tmp_path)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stderr
    assert (tmp_path / "review_prompt.md").is_file()
    assert (tmp_path / "hu_guards.txt").read_text().find("_hu_wide_open_hand") >= 0
