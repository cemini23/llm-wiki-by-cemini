"""Smoke tests for harness_sandbox_agent (gate / live bundle path)."""
from __future__ import annotations

import importlib
import os
import sys
from pathlib import Path

import pytest

_AGENT_ROOT = Path(__file__).resolve().parent.parent
_EXAMPLES = _AGENT_ROOT / "examples"
_HARNESS = _AGENT_ROOT / "harness"
for _p in (_EXAMPLES, _HARNESS):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

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


def test_cemini_default_poker_bot_strategy(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("POKER_BOT_STRATEGY", raising=False)
    monkeypatch.setenv("CEMINI_SANDBOX_ENGINE", "cemini")
    import strategy as strat_mod

    importlib.reload(strat_mod)
    assert os.environ.get("POKER_BOT_STRATEGY") == "cemini_k131b"
