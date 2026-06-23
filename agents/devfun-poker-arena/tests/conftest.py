"""Pytest path setup for cemini agent tests."""
from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "examples"

for p in (str(ROOT), str(EXAMPLES)):
    if p not in sys.path:
        sys.path.insert(0, p)


def pytest_configure(config):  # noqa: ARG001
    os.environ.pop("CEMINI_TRAJECTORY_BOUND", None)


def pytest_runtest_teardown(item, nextitem):  # noqa: ARG001
    """Trajectory-bound integration tests mutate module globals — reset each test."""
    try:
        import cemini_decide as mod  # noqa: WPS433
    except ImportError:
        return
    os.environ.pop("CEMINI_TRAJECTORY_BOUND", None)
    mod._TRAJECTORY_BOUND_CFG = None
    mod._TRAJECTORY_BOUND_STATE = mod.TrajectoryBoundState()
    mod._TRAJECTORY_BOUND_HAND_KEY = None
