"""Workspace and thesis-scoped paths for intel monitors.

The active thesis defaults to ``ice-turnkey`` but can be overridden per-process
via the ``CEMINI_THESIS_ID`` environment variable, or per-call by passing
``thesis_id=`` to :func:`thesis_config`. This lets a single monitor codebase
serve multiple theses (e.g. ``gov-asset-rerate``) without forking paths.
"""

from __future__ import annotations

import os
from pathlib import Path

INTEL_ROOT = Path(__file__).resolve().parent
SCRIPTS_ROOT = INTEL_ROOT.parent
WORKSPACE_ROOT = SCRIPTS_ROOT.parent

DEFAULT_THESIS_ID = "ice-turnkey"
THESIS_ID = os.environ.get("CEMINI_THESIS_ID", DEFAULT_THESIS_ID)
THESES_ROOT = WORKSPACE_ROOT / "config" / "theses"
# Backward-compatible default config dir for the active thesis.
THESIS_CONFIG_DIR = THESES_ROOT / THESIS_ID
LOCAL_ROOT = WORKSPACE_ROOT / ".local"


def thesis_config(filename: str, thesis_id: str | None = None) -> Path:
    """Resolve a thesis config file.

    ``thesis_id`` overrides the process-level :data:`THESIS_ID` (env-driven)
    when provided; otherwise the active thesis is used.
    """
    tid = thesis_id or THESIS_ID
    return THESES_ROOT / tid / filename


def report_dir(lane: str) -> Path:
    return LOCAL_ROOT / "reports" / lane


def data_dir(lane: str) -> Path:
    return LOCAL_ROOT / lane
