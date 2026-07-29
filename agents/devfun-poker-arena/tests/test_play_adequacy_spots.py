"""K158 play-adequacy spots — competent-play / search-visited regressions.

These assert *safe actions* (fold/check), not mere legal transitions.
See references/play-adequacy-gates.md and danger law (1−r)^N.
"""
from __future__ import annotations

import sys
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parents[1] / "examples"
_TESTS = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))
if str(_TESTS) not in sys.path:
    sys.path.insert(0, str(_TESTS))

from cemini_decide import decide  # noqa: E402
from helpers.cemini_tables import (  # noqa: E402
    hu_btn_55_underpair_paired_kings_river_overbet,
)


def test_play_adequacy_underpair_overbet_paired_board_folds():
    """Rare pivotal: IP underpair on paired kings vs river overbet → fold.

    Random trajectory gates miss this class with high probability (danger law).
    Transition-only smoke would pass if decide returned any legal action;
    play-adequacy requires the *safe* action.
    """
    table = hu_btn_55_underpair_paired_kings_river_overbet()
    out = decide(table, deadline_s=10.0)
    assert isinstance(out, dict)
    assert out.get("action") == "fold", (
        f"play-adequacy expected fold, got {out.get('action')!r} "
        f"reasoning={out.get('reasoning')!r}"
    )


def test_play_adequacy_fixture_is_river_facing_bet():
    """Sanity: fixture is a river call/fold decision (not free check)."""
    table = hu_btn_55_underpair_paired_kings_river_overbet()
    assert table.get("street") == "River"
    assert int(table.get("potChips") or table.get("pot") or 0) > 0
    allowed = table.get("allowedActions") or {}
    # Must face a bet so fold is a real decision (not free check).
    assert allowed.get("canFold") is True or allowed.get("can_fold") is True
    call_chips = allowed.get("callChips") or allowed.get("call_chips") or 0
    assert int(call_chips) > 0
