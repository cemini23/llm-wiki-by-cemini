"""P2-3 fold-guard ledger — fail-open jsonl audit hook."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from fold_guard_ledger import fold_guards_path, record_fold_guard  # noqa: E402


def test_fold_guard_writes_jsonl(tmp_path, monkeypatch):
    export = tmp_path / "export"
    monkeypatch.setenv("CEMINI_EXPORT_DIR", str(export))
    monkeypatch.delenv("CEMINI_FOLD_GUARD_LOG_PATH", raising=False)
    record_fold_guard(
        "bb_broadway_fold", hand_class="KQo", position="BB", spot="vs_open",
    )
    path = export / "fold_guards.jsonl"
    assert path.is_file()
    row = json.loads(path.read_text(encoding="utf-8").strip().splitlines()[0])
    assert row["guard_id"] == "bb_broadway_fold"
    assert row["hand_class"] == "KQo"
    assert row["position"] == "BB"
    assert row["spot"] == "vs_open"


def test_fold_guard_custom_path(tmp_path, monkeypatch):
    target = tmp_path / "custom" / "guards.jsonl"
    monkeypatch.setenv("CEMINI_FOLD_GUARD_LOG_PATH", str(target))
    monkeypatch.delenv("CEMINI_EXPORT_DIR", raising=False)
    record_fold_guard("nemesis_sb_tight", hand_class="98s", position="SB")
    assert target.is_file()


def test_fold_guard_fail_open_no_env(monkeypatch):
    monkeypatch.delenv("CEMINI_EXPORT_DIR", raising=False)
    monkeypatch.delenv("CEMINI_FOLD_GUARD_LOG_PATH", raising=False)
    record_fold_guard("x")  # must not raise


def test_fold_guards_path_none_when_no_env(monkeypatch):
    monkeypatch.delenv("CEMINI_EXPORT_DIR", raising=False)
    monkeypatch.delenv("CEMINI_FOLD_GUARD_LOG_PATH", raising=False)
    assert fold_guards_path() is None
