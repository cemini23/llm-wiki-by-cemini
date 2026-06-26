"""PokerKit stack smoke tests for K130 Track A."""
from __future__ import annotations

from dataclasses import dataclass
import importlib.metadata
from pathlib import Path
import tomllib

from gin_style import _hand_class as gin_hand_class
from gin_style import _norm_card
from research_static_chart import _hand_class as chart_hand_class
from research_static_chart import research_static_chart
from selfplay import _arena_card_str, _build_table

ROOT = Path(__file__).resolve().parent.parent


@dataclass
class _FakePot:
    amount: int


@dataclass
class _FakeState:
    actor_index: int
    hole_cards: list[list[str]]
    board_cards: list[str]
    stacks: list[int]
    bets: list[int]
    pots: list[_FakePot]
    opener_index: int | None = 0


def test_pyproject_pins_pokerkit_min_version() -> None:
    data = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    deps = data["project"]["dependencies"]
    assert "pokerkit>=0.5" in deps


def test_pokerkit_import_smoke() -> None:
    import pokerkit  # noqa: F401

    assert importlib.metadata.version("pokerkit")


def test_pokerkit_card_string_parity_for_hole_and_board_cards() -> None:
    assert _arena_card_str("Ah") == "Ah"
    assert _arena_card_str("[Ah]") == "Ah"
    assert _norm_card("Ah") == "Ah"
    assert _norm_card("[Ah]") == "Ah"

    raw_hole = ["[Ah]", "[Kh]"]
    raw_board = ["[Qh]", "[Jh]", "[2c]"]

    normalized_hole = [_arena_card_str(card) for card in raw_hole]
    normalized_board = [_arena_card_str(card) for card in raw_board]

    assert normalized_hole == ["Ah", "Kh"]
    assert normalized_board == ["Qh", "Jh", "2c"]
    assert chart_hand_class(normalized_hole) == "AKs"
    assert gin_hand_class(raw_hole) == "AKs"


def test_selfplay_table_builder_feeds_chart_without_parse_failures() -> None:
    preflop_state = _FakeState(
        actor_index=1,
        hole_cards=[["[Ah]", "[Kh]"], ["[2c]", "[2d]"]],
        board_cards=[],
        stacks=[199, 198],
        bets=[1, 2],
        pots=[_FakePot(amount=0)],
        opener_index=0,
    )

    table = _build_table(
        preflop_state,
        hero_idx=0,
        table_id="k130-smoke",
        starting_stacks=[200, 200],
        small_blind=1,
        big_blind=2,
    )
    chart = research_static_chart(table)

    assert table["seats"][0]["holeCards"] == ["Ah", "Kh"]
    assert chart["hand_class"] == "AKs"
    assert chart["table_format"] == "hu"
    assert chart["preflop_action"] == "raise"

    flop_state = _FakeState(
        actor_index=1,
        hole_cards=[["[Ah]", "[Kh]"], ["[2c]", "[2d]"]],
        board_cards=["[Qh]", "[Jh]", "[2c]"],
        stacks=[198, 197],
        bets=[2, 2],
        pots=[_FakePot(amount=4)],
        opener_index=0,
    )
    flop_table = _build_table(
        flop_state,
        hero_idx=0,
        table_id="k130-flop-smoke",
        starting_stacks=[200, 200],
        small_blind=1,
        big_blind=2,
    )

    assert flop_table["boardCards"] == ["Qh", "Jh", "2c"]
