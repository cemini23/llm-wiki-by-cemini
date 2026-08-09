"""P1-3 short-stack jam tiers — ≤8bb jam-or-fold vs 8–12bb selective."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from short_stack import short_stack_jam_bb_threshold, short_stack_preflop_action  # noqa: E402


@pytest.fixture(autouse=True)
def _clear_env(monkeypatch):
    monkeypatch.delenv("CEMINI_SHORT_STACK_JAM_BB", raising=False)
    monkeypatch.delenv("CEMINI_SHORT_STACK_BB", raising=False)


def _allowed() -> dict:
    return {
        "canRaise": True,
        "canAllIn": True,
        "canCall": True,
        "canCheck": True,
        "canFold": True,
    }


_JAM = ("raise", "all-in")


def test_jam_bb_default_8():
    assert short_stack_jam_bb_threshold() == 8.0


def test_jam_bb_env_override(monkeypatch):
    monkeypatch.setenv("CEMINI_SHORT_STACK_JAM_BB", "7")
    assert short_stack_jam_bb_threshold() == 7.0


def test_band_79bb_kqo_jams_wide():
    """≤8bb uses the push chart — KQo BTN jams."""
    out = short_stack_preflop_action(
        hand_class="KQo", position="BTN",
        available=["fold", "raise", "all-in"],
        allowed=_allowed(), call_chips=0, stack_chips=158,
        stack_bb=7.9,
    )
    assert out is not None and out[0] in _JAM


def test_band_8bb_kqo_jams_wide():
    out = short_stack_preflop_action(
        hand_class="KQo", position="BTN",
        available=["fold", "raise", "all-in"],
        allowed=_allowed(), call_chips=0, stack_chips=160,
        stack_bb=8.0,
    )
    assert out is not None and out[0] in _JAM


def test_band_119bb_kqo_not_selective():
    """8–12bb selective band — KQo is NOT in the selective jam set."""
    out = short_stack_preflop_action(
        hand_class="KQo", position="BTN",
        available=["fold", "raise", "all-in"],
        allowed=_allowed(), call_chips=0, stack_chips=238,
        stack_bb=11.9,
    )
    assert out is None or out[0] not in _JAM


def test_band_119bb_ak_selective_jam():
    out = short_stack_preflop_action(
        hand_class="AKs", position="BTN",
        available=["fold", "raise", "all-in"],
        allowed=_allowed(), call_chips=0, stack_chips=238,
        stack_bb=11.9,
    )
    assert out is not None and out[0] in _JAM


def test_band_12bb_selective_still_applies():
    out = short_stack_preflop_action(
        hand_class="KQo", position="BTN",
        available=["fold", "raise", "all-in"],
        allowed=_allowed(), call_chips=0, stack_chips=240,
        stack_bb=12.0,
    )
    assert out is None or out[0] not in _JAM


def test_band_19bb_at_selective_jam():
    out = short_stack_preflop_action(
        hand_class="ATs", position="BTN",
        available=["fold", "raise", "all-in"],
        allowed=_allowed(), call_chips=0, stack_chips=380,
        stack_bb=19.0,
    )
    assert out is not None and out[0] in _JAM
