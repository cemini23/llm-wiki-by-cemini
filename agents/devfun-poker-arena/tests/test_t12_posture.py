"""T12 posture env knobs (P1-6 + P1/P2 climb) wired into the s12 tournament block."""
from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from run_cemini_lobby import _apply_competition_posture  # noqa: E402


@pytest.fixture
def _isolate_env():
    saved = dict(os.environ)
    yield
    os.environ.clear()
    os.environ.update(saved)


def test_s12_posture_sets_climb_knobs(_isolate_env):
    for k in list(os.environ):
        if k.startswith("CEMINI_"):
            del os.environ[k]
    os.environ["CEMINI_LOBBY_ROLE"] = "s12_tournament"
    os.environ["CEMINI_PRIMARY_TRACK"] = "tournament"
    os.environ["S12_TOURNAMENT_COMP"] = "comp_s12"
    _apply_competition_posture("comp_s12")
    assert os.environ["CEMINI_TOURNAMENT_MODE"] == "1"
    assert os.environ["CEMINI_GIN_KILL"] == "1"
    assert os.environ["CEMINI_MAX_REBUYS"] == "0"
    # P1-6: survival hands softened 60 → 30, min stack 250.
    assert os.environ["CEMINI_KO_SURVIVAL_HANDS"] == "30"
    assert os.environ["CEMINI_KO_SURVIVAL_MIN_STACK"] == "250"
    # P1/P2 climb knobs.
    assert os.environ["CEMINI_NAMED_NEMESIS_TIGHT"] == "0"
    assert os.environ["CEMINI_TOURNAMENT_3BET"] == "1"
    assert os.environ["CEMINI_SHORT_STACK_JAM_BB"] == "8"
    assert os.environ["CEMINI_SHORT_STACK_BB"] == "12"
    assert os.environ["CEMINI_FLAT_DOMINATE"] == "1"
    assert os.environ["CEMINI_TOURNAMENT_3BET_POLAR"] == "1"
    assert os.environ["CEMINI_STOP_WIN_MULT"] == "0"
    assert os.environ["CEMINI_TAG_BLIND_DEFEND"] == "1"
    assert os.environ["CEMINI_NEMESIS_TIGHT"] == "0"


def test_s12_posture_does_not_hit_playground(_isolate_env):
    for k in list(os.environ):
        if k.startswith("CEMINI_"):
            del os.environ[k]
    os.environ["CEMINI_LOBBY_ROLE"] = "s12_playground"
    os.environ["CEMINI_PRIMARY_TRACK"] = "playground"
    os.environ["S12_PLAYGROUND_COMP"] = "comp_pg"
    _apply_competition_posture("comp_pg")
    # Playground path must not receive the tournament climb knobs.
    assert os.environ.get("CEMINI_TOURNAMENT_3BET") != "1"
    assert os.environ.get("CEMINI_KO_SURVIVAL_HANDS") != "30"
