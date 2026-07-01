"""Bundle build respects CEMINI_SANDBOX_ENGINE (cemini vs gin_hu004 vendor)."""
from __future__ import annotations

import os
import sys
import zipfile
from pathlib import Path

import pytest

AGENT_ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = AGENT_ROOT / "examples"

sys.path.insert(0, str(EXAMPLES))

from submit_sandbox_pvp import build_bundle  # noqa: E402

GIN_VENDOR_PATH = "assets/_vendor/gin_hu004/hu004.py"


@pytest.fixture
def out_zip(tmp_path: Path) -> Path:
    return tmp_path / "bundle.zip"


def test_cemini_bundle_excludes_gin_vendor(monkeypatch: pytest.MonkeyPatch, out_zip: Path) -> None:
    monkeypatch.setenv("CEMINI_SANDBOX_ENGINE", "cemini")
    build_bundle(out_zip)
    with zipfile.ZipFile(out_zip) as zf:
        names = zf.namelist()
    assert "harness/strategy.py" in names
    assert GIN_VENDOR_PATH not in names


def test_gin_engine_bundle_includes_gin_vendor(
    monkeypatch: pytest.MonkeyPatch, out_zip: Path
) -> None:
    gin_src = AGENT_ROOT / "vendor" / "gin_hu004" / "hu004.py"
    if not gin_src.is_file():
        pytest.skip("vendor/gin_hu004/hu004.py not present")

    monkeypatch.setenv("CEMINI_SANDBOX_ENGINE", "gin_hu004")
    build_bundle(out_zip)
    with zipfile.ZipFile(out_zip) as zf:
        names = zf.namelist()
    assert GIN_VENDOR_PATH in names
