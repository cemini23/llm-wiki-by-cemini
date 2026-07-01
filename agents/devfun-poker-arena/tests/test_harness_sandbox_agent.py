"""Smoke tests for harness_sandbox_agent (gate / live bundle path)."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from tests.helpers.cemini_tables import hu_sb_unopened  # noqa: E402

_LEGAL = frozenset({"fold", "check", "call", "bet", "raise", "all-in"})


@pytest.fixture(autouse=True)
def _cemini_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CEMINI_SANDBOX_ENGINE", "cemini")


def test_harness_sandbox_agent_decide() -> None:
    from harness_sandbox_agent import decide

    table = hu_sb_unopened(["Ah", "Kd"])
    out = decide(table, deadline_s=8.0)
    if isinstance(out, dict):
        assert out.get("action") in _LEGAL
    else:
        assert out in _LEGAL
