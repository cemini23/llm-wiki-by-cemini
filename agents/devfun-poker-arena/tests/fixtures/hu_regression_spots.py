"""HU regression spots for Poker Agent Challenge / researcher sandbox."""
from __future__ import annotations

from tests.fixtures.regression_spots import RegressionSpot
from tests.helpers.cemini_tables import (
    hu_bb_vs_minraise,
    hu_btn_vs_shove,
    hu_sb_unopened,
)


def hu_regression_spots() -> list[RegressionSpot]:
    return [
        RegressionSpot(
            id="hu_ajo_btn_vs_shove_r34",
            source="R34 — gin overcalled AJo vs stack-off HU/BTN",
            table=hu_btn_vs_shove(["Jc", "Ad"], shove_to=95, hero_stack=100),
            context={
                "CEMINI_GIN_STYLE": "1",
                "CEMINI_GIN_STYLE_PREFLOP": "1",
            },
            forbidden=frozenset({"call", "raise", "all-in"}),
            required=frozenset({"fold"}),
            notes="HU shove spots frequent — fold broadway vs stack-off.",
        ),
        RegressionSpot(
            id="hu_sb_aa_open",
            source="HU SB must open AA first-in",
            table=hu_sb_unopened(["As", "Ad"]),
            forbidden=frozenset({"fold", "call"}),
            required=frozenset({"raise"}),
            notes="Premium open from SB/BTN in HU.",
        ),
        RegressionSpot(
            id="hu_sb_72o_fold",
            source="HU SB trash — no open",
            table=hu_sb_unopened(["7h", "2c"]),
            forbidden=frozenset({"raise", "all-in", "call"}),
            required=frozenset({"fold"}),
            notes="Trash offsuit — fold SB unopened.",
        ),
        RegressionSpot(
            id="hu_bb_72o_vs_minraise",
            source="HU BB — fold 72o vs minraise",
            table=hu_bb_vs_minraise(["7h", "2c"]),
            forbidden=frozenset({"call", "raise", "all-in"}),
            required=frozenset({"fold"}),
            notes="No defend trash vs small open in HU.",
        ),
        RegressionSpot(
            id="hu_bb_aks_defend",
            source="HU BB — defend AKs vs minraise",
            table=hu_bb_vs_minraise(["As", "Ks"]),
            forbidden=frozenset({"fold"}),
            required=frozenset({"call", "raise"}),
            notes="Premium BB defend vs minraise.",
        ),
    ]
