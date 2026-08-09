"""P2-5 villain action sketch — fail-open jsonl + open% helper."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from villain_action_log import (  # noqa: E402
    log_villain_action,
    open_pct_by_handle,
    villain_actions_path,
)


def test_villain_action_writes_jsonl(tmp_path, monkeypatch):
    export = tmp_path / "export"
    monkeypatch.setenv("CEMINI_EXPORT_DIR", str(export))
    monkeypatch.delenv("CEMINI_VILLAIN_ACTIONS_LOG_PATH", raising=False)
    log_villain_action("hunterguy102", street="preflop", action="raise", spot="open")
    path = export / "villain_actions.jsonl"
    assert path.is_file()
    row = json.loads(path.read_text(encoding="utf-8").strip().splitlines()[0])
    assert row["handle"] == "hunterguy102"
    assert row["street"] == "preflop"
    assert row["action"] == "raise"
    assert row["spot"] == "open"


def test_open_pct_by_handle(tmp_path, monkeypatch):
    export = tmp_path / "export"
    monkeypatch.setenv("CEMINI_EXPORT_DIR", str(export))
    monkeypatch.delenv("CEMINI_VILLAIN_ACTIONS_LOG_PATH", raising=False)
    for action in ("raise", "call", "fold"):
        log_villain_action("alice", street="preflop", action=action, spot="open")
    log_villain_action("bob", street="preflop", action="raise", spot="open")
    log_villain_action("bob", street="flop", action="bet", spot="cbet")
    pct = open_pct_by_handle(export / "villain_actions.jsonl")
    assert pct["alice"] == pytest.approx(1 / 3)
    assert pct["bob"] == pytest.approx(1.0)  # flop row excluded


def test_open_pct_skips_bad_rows(tmp_path):
    p = tmp_path / "mixed.jsonl"
    p.write_text(
        '{"handle":"a","street":"preflop","action":"raise"}\n'
        "not-json\n"
        '{"handle":"b","street":"turn","action":"bet"}\n',
        encoding="utf-8",
    )
    pct = open_pct_by_handle(p)
    assert pct["a"] == 1.0
    assert "b" not in pct


def test_open_pct_missing_file(tmp_path):
    assert open_pct_by_handle(tmp_path / "nope.jsonl") == {}


def test_villain_action_fail_open_no_env(monkeypatch):
    monkeypatch.delenv("CEMINI_EXPORT_DIR", raising=False)
    monkeypatch.delenv("CEMINI_VILLAIN_ACTIONS_LOG_PATH", raising=False)
    log_villain_action("alice", street="preflop", action="raise")


def test_villain_actions_path_none_when_no_env(monkeypatch):
    monkeypatch.delenv("CEMINI_EXPORT_DIR", raising=False)
    monkeypatch.delenv("CEMINI_VILLAIN_ACTIONS_LOG_PATH", raising=False)
    assert villain_actions_path() is None
