"""K150 TEN-shaped HU ladder regression — BB defend + limp iso."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))
sys.path.insert(0, str(ROOT))

from tests.fixtures.hu_regression_spots import hu_regression_spots  # noqa: E402
from tests.test_cemini_regression import _run  # noqa: E402

_TEN_IDS = frozenset({
    "hu_bb_k8o_vs_ten_minraise",
    "hu_bb_kto_vs_ten_minraise",
    "hu_bb_qjo_vs_ten_minraise",
    "hu_bb_76s_vs_ten_minraise",
    "hu_bb_72o_vs_ten_minraise",
    "hu_bb_aks_iso_vs_ten_limp",
    "hu_bb_aa_iso_vs_ten_limp",
    "hu_bb_qjs_iso_vs_ten_limp",
})


def test_ten_hu_spots_present():
    ids = {s.id for s in hu_regression_spots()}
    missing = _TEN_IDS - ids
    assert not missing, f"missing TEN spots: {sorted(missing)}"


def test_ten_hu_regression_spots():
    spots = [s for s in hu_regression_spots() if s.id in _TEN_IDS]
    assert len(spots) == len(_TEN_IDS)
    for spot in spots:
        action = _run(spot.table, spot.context)["action"]
        if spot.forbidden:
            assert action not in spot.forbidden, (
                f"{spot.id}: got {action!r}, forbidden={sorted(spot.forbidden)} "
                f"— {spot.notes}"
            )
        if spot.required:
            assert action in spot.required, (
                f"{spot.id}: expected one of {sorted(spot.required)}, got {action!r}"
            )


def test_gin_s1b_still_folds_72o_vs_anonymous_minraise():
    """Trash fold must hold under prod gin/S1B even without TEN tagged."""
    from tests.helpers.cemini_tables import hu_bb_vs_minraise  # noqa: WPS433

    out = _run(
        hu_bb_vs_minraise(["7h", "2c"]),
        {
            "CEMINI_GIN_STYLE": "1",
            "CEMINI_GIN_STYLE_PREFLOP": "1",
            "CEMINI_GIN_STYLE_GATE": "1",
            "CEMINI_GIN_V008": "1",
            "CEMINI_S1B_EXPLOIT": "1",
            "CEMINI_RESEARCHER_MODE": "1",
        },
    )
    assert out["action"] == "fold"
