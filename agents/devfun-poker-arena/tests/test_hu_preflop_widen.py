"""Track A regression tests for widened HU SB/BTN opens."""
from __future__ import annotations

from tests.helpers.cemini_tables import hu_sb_unopened
from tests.test_cemini_regression import _run


def test_hu_sb_steal_opens_kto():
    out = _run(hu_sb_unopened(["Kd", "Th"]), {
        "CEMINI_GIN_STYLE": "1",
        "CEMINI_GIN_STYLE_PREFLOP": "1",
        "CEMINI_GIN_STYLE_GATE": "1",
    })
    assert out["action"] in {"raise", "bet"}


def test_hu_sb_steal_opens_q7s():
    out = _run(hu_sb_unopened(["Qs", "7s"]), {
        "CEMINI_GIN_STYLE": "1",
        "CEMINI_GIN_STYLE_PREFLOP": "1",
        "CEMINI_GIN_STYLE_GATE": "1",
    })
    assert out["action"] in {"raise", "bet"}


def test_hu_sb_steal_opens_j9o():
    out = _run(hu_sb_unopened(["Jh", "9c"]), {
        "CEMINI_GIN_STYLE": "1",
        "CEMINI_GIN_STYLE_PREFLOP": "1",
        "CEMINI_GIN_STYLE_GATE": "1",
    })
    assert out["action"] in {"raise", "bet"}


def test_hu_sb_still_folds_72o():
    out = _run(hu_sb_unopened(["7h", "2c"]), {
        "CEMINI_GIN_STYLE": "1",
        "CEMINI_GIN_STYLE_PREFLOP": "1",
        "CEMINI_GIN_STYLE_GATE": "1",
    })
    assert out["action"] == "fold"


def test_hu_sb_still_folds_t4o():
    out = _run(hu_sb_unopened(["Td", "4s"]), {
        "CEMINI_GIN_STYLE": "1",
        "CEMINI_GIN_STYLE_PREFLOP": "1",
        "CEMINI_GIN_STYLE_GATE": "1",
    })
    assert out["action"] == "fold"
