"""K131b Track A — HU BB defend widening without extra BTN opens."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))
sys.path.insert(0, str(ROOT))

from research_static_chart import research_static_chart  # noqa: E402
from s1b_exploit import try_defend_bb_vs_steal  # noqa: E402
from tests.helpers.cemini_tables import hu_bb_vs_minraise, hu_sb_unopened  # noqa: E402
from tests.test_cemini_regression import _run  # noqa: E402


def _gin_ctx() -> dict:
    return {
        "CEMINI_GIN_STYLE": "1",
        "CEMINI_GIN_STYLE_PREFLOP": "1",
        "CEMINI_GIN_STYLE_GATE": "1",
    }


def test_hu_bb_defend_margin_calls_small_edge():
    table = hu_bb_vs_minraise(["Kd", "9c"])
    out = try_defend_bb_vs_steal(
        hand_class="K9o",
        position="BB",
        call_chips=4,
        pot_odds=4 / 13,
        equity=0.27,
        available=["fold", "call", "raise"],
        hero_stack_chips=194,
        table=table,
    )
    assert out == ("call", None)


def test_hu_bb_chart_call_defends_a4o():
    out = _run(hu_bb_vs_minraise(["Ad", "4c"]), _gin_ctx())
    assert out["action"] == "call"


def test_hu_bb_chart_expands_k9o_call_bucket():
    chart = research_static_chart(hu_bb_vs_minraise(["Kd", "9c"]))
    assert chart["position"] == "BB"
    assert chart["preflop_action"] == "call"


def test_hu_sb_trimmed_a4o_stays_folded_under_gin():
    out = _run(hu_sb_unopened(["Ad", "4c"]), _gin_ctx())
    assert out["action"] == "fold"


def test_hu_sb_trimmed_a5o_stays_folded_under_gin():
    out = _run(hu_sb_unopened(["Ah", "5d"]), _gin_ctx())
    assert out["action"] == "fold"


def test_hu_bb_chart_call_kto_vs_minraise():
    table = hu_bb_vs_minraise(["Kd", "Th"])
    out = _run(
        table,
        {
            **_gin_ctx(),
            "CEMINI_GIN_V008": "1",
            "CEMINI_S1B_EXPLOIT": "1",
        },
    )
    assert out["action"] in {"call", "raise"}


def test_hu_bb_defends_qjo_vs_steal():
    table = hu_bb_vs_minraise(["Qh", "Jc"])
    out = _run(
        table,
        {
            **_gin_ctx(),
            "CEMINI_GIN_V008": "1",
            "CEMINI_S1B_EXPLOIT": "1",
        },
    )
    assert out["action"] in {"call", "raise"}


def test_hu_bb_value_3bets_77_vs_minraise():
    out = _run(
        hu_bb_vs_minraise(["7h", "7d"]),
        {
            **_gin_ctx(),
            "CEMINI_GIN_V008": "1",
            "CEMINI_S1B_EXPLOIT": "1",
        },
    )
    assert out["action"] == "raise"


def test_hu_bb_kto_stays_call_not_value_3b():
    out = _run(
        hu_bb_vs_minraise(["Kd", "Th"]),
        {
            **_gin_ctx(),
            "CEMINI_GIN_V008": "1",
            "CEMINI_S1B_EXPLOIT": "1",
        },
    )
    assert out["action"] == "call"
