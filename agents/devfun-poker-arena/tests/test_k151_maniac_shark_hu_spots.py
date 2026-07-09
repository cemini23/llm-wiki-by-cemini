"""K151 maniac_shark-shaped HU ladder regression — BB defend + 3-bet fold."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))
sys.path.insert(0, str(ROOT))

from tests.fixtures.hu_regression_spots import hu_regression_spots  # noqa: E402
from tests.test_cemini_regression import _run  # noqa: E402

_SHARK_IDS = frozenset({
    "hu_bb_kto_vs_maniac_shark_minraise",
    "hu_bb_k8o_vs_maniac_shark_minraise",
    "hu_bb_qjo_vs_maniac_shark_minraise",
    "hu_bb_jts_vs_maniac_shark_minraise",
    "hu_bb_76s_vs_maniac_shark_minraise",
    "hu_bb_aks_vs_maniac_shark_minraise",
    "hu_bb_72o_vs_maniac_shark_minraise",
    "hu_bb_98o_vs_maniac_shark_3bet",
})


def test_maniac_shark_hu_spots_present():
    ids = {s.id for s in hu_regression_spots()}
    missing = _SHARK_IDS - ids
    assert not missing, f"missing maniac_shark spots: {sorted(missing)}"


def test_maniac_shark_hu_regression_spots():
    spots = [s for s in hu_regression_spots() if s.id in _SHARK_IDS]
    assert len(spots) == len(_SHARK_IDS)
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
