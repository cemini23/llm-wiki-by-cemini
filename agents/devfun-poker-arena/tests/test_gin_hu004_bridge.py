"""Smoke tests for gin hu004 sandbox bridge."""
from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from tests.helpers.cemini_tables import hu_sb_unopened  # noqa: E402


@pytest.fixture(autouse=True)
def _gin_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CEMINI_SANDBOX_ENGINE", "gin_hu004")


def test_gin_hu004_bridge_import_and_decide() -> None:
    from gin_hu004_bridge import decide

    table = hu_sb_unopened(["Ah", "Kd"])
    out = decide(table, deadline_s=8.0)
    assert out["action"] in ("fold", "check", "call", "bet", "raise", "all-in")
    assert out.get("reasoning") or out.get("reasoning_text")
    assert len(str(out.get("reasoning") or "")) <= 150


def test_deadline_fallback_when_tight(monkeypatch: pytest.MonkeyPatch) -> None:
    """Harness clamps deadline floor to 2.0 — bridge must fallback at <=2.2."""
    from gin_hu004_bridge import decide

    def _should_not_load_hu004() -> None:
        raise AssertionError("_hu004_module must not run on tight deadline")

    monkeypatch.setattr("gin_hu004_bridge._hu004_module", _should_not_load_hu004)

    table = hu_sb_unopened(["Ah", "Kd"])
    out = decide(table, deadline_s=2.0)
    assert out["action"] in ("check", "call", "fold")
    assert "deadline tight" in str(out.get("message") or "")


def test_harness_choose_action_gin_engine() -> None:
    harness_dir = Path(__file__).resolve().parent.parent / "harness"
    sys.path.insert(0, str(harness_dir))
    os.environ["CEMINI_SANDBOX_ENGINE"] = "gin_hu004"
    # Re-import fresh
    import importlib

    import strategy as harness_strategy  # noqa: WPS433

    importlib.reload(harness_strategy)
    table = hu_sb_unopened(["Ah", "Kd"])
    out = harness_strategy.choose_action(table)
    if isinstance(out, dict):
        assert out.get("action")
    else:
        assert out
