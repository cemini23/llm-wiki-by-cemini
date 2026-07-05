"""Workspace and thesis-scoped paths for intel monitors."""

from __future__ import annotations

from pathlib import Path

INTEL_ROOT = Path(__file__).resolve().parent
SCRIPTS_ROOT = INTEL_ROOT.parent
WORKSPACE_ROOT = SCRIPTS_ROOT.parent

THESIS_ID = "ice-turnkey"
THESIS_CONFIG_DIR = WORKSPACE_ROOT / "config" / "theses" / THESIS_ID
LOCAL_ROOT = WORKSPACE_ROOT / ".local"


def thesis_config(filename: str) -> Path:
    return THESIS_CONFIG_DIR / filename


def report_dir(lane: str) -> Path:
    return LOCAL_ROOT / "reports" / lane


def data_dir(lane: str) -> Path:
    return LOCAL_ROOT / lane
