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

# harness/strategy.py setdefault()s these for sandbox ship. Importing that
# module mid-suite would otherwise leave MAFP/postflop overlays on for
# unrelated regression tests (WP1/WP2 made CEMINI_MAFP_CHART live).
_HARNESS_DEFAULT_ENV = (
    "CEMINI_TRAJECTORY_BOUND",
    "CEMINI_MAFP_CHART",
    "CEMINI_MAFP_CHART_PATH",
    "CEMINI_POSTFLOP_BUCKETS",
    "CEMINI_POSTFLOP_BUCKETS_PATH",
    "CEMINI_TABLE_FORMAT",
    "CEMINI_RESEARCHER_MODE",
    "CEMINI_SANDBOX_ENGINE",
)


def _clear_harness_default_env() -> None:
    for key in _HARNESS_DEFAULT_ENV:
        os.environ.pop(key, None)
    try:
        from research_static_chart import _reset_mafp_overlay_cache  # noqa: WPS433

        _reset_mafp_overlay_cache()
    except Exception:
        pass
    try:
        from postflop_buckets import _reset_bucket_cache  # noqa: WPS433

        _reset_bucket_cache()
    except Exception:
        pass


def pytest_configure(config):  # noqa: ARG001
    _clear_harness_default_env()


def pytest_runtest_setup(item):  # noqa: ARG001
    """Isolate each test from harness setdefault pollution."""
    _clear_harness_default_env()


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
    _clear_harness_default_env()
