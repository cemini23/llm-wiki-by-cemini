"""Filesystem layout for the XSP ops loop.

State root: ``.local/ops/xsp/``
  - state/brain.json
  - state/posts/<slug>.json
  - queue/{pending,running,done,failed}/
  - packets/
  - events/
"""

from __future__ import annotations

import os
from pathlib import Path

# scripts/xsp_ops/paths.py → scripts → repo root
PACKAGE_DIR = Path(__file__).resolve().parent
SCRIPTS_ROOT = PACKAGE_DIR.parent
REPO_ROOT = SCRIPTS_ROOT.parent

# Allow override for tests
_OPS_OVERRIDE = os.environ.get("XSP_OPS_ROOT")
OPS_ROOT = Path(_OPS_OVERRIDE) if _OPS_OVERRIDE else (REPO_ROOT / ".local" / "ops" / "xsp")

STATE_DIR = OPS_ROOT / "state"
BRAIN_PATH = STATE_DIR / "brain.json"
POSTS_DIR = STATE_DIR / "posts"

QUEUE_DIR = OPS_ROOT / "queue"
QUEUE_PENDING = QUEUE_DIR / "pending"
QUEUE_RUNNING = QUEUE_DIR / "running"
QUEUE_DONE = QUEUE_DIR / "done"
QUEUE_FAILED = QUEUE_DIR / "failed"

PACKETS_DIR = OPS_ROOT / "packets"
EVENTS_DIR = OPS_ROOT / "events"

INBOX_DIR = REPO_ROOT / "research to be indexed"

# LaunchAgent label (documented only — install_workflow_launchagents.sh is Cursor's lane)
LAUNCHAGENT_LABEL = "com.cemini.xsp-ops-loop"
LAUNCHAGENT_START_INTERVAL = 3600  # seconds


def ensure_layout(root: Path | None = None) -> Path:
    """Create ops directory tree. Returns ops root."""
    base = root if root is not None else OPS_ROOT
    for d in (
        base / "state" / "posts",
        base / "queue" / "pending",
        base / "queue" / "running",
        base / "queue" / "done",
        base / "queue" / "failed",
        base / "packets",
        base / "events",
    ):
        d.mkdir(parents=True, exist_ok=True)
    return base


def posts_path(slug: str, root: Path | None = None) -> Path:
    base = root if root is not None else OPS_ROOT
    return base / "state" / "posts" / f"{slug}.json"


def brain_path(root: Path | None = None) -> Path:
    base = root if root is not None else OPS_ROOT
    return base / "state" / "brain.json"


def queue_path(status: str, slug: str, root: Path | None = None) -> Path:
    base = root if root is not None else OPS_ROOT
    return base / "queue" / status / f"{slug}.json"
