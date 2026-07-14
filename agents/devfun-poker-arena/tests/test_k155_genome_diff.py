"""K155 GenomeDiff compositional gate tests."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from patch_genome_diff import (  # noqa: E402
    empty_genome_diff,
    genome_diff_markdown_table,
    load_genome_diff_config,
    validate_genome_diff,
)

CFG = ROOT / "config" / "hu_patch_genome_diff.json"


def test_config_schema():
    cfg = load_genome_diff_config(CFG)
    assert cfg["schema"] == "devfun.hu_patch_genome_diff.v1"
    assert cfg["advisory_only"] is True
    assert "mutate" in cfg["delta_values"]


def test_mutate_pass():
    rec = empty_genome_diff(parent_mechanism="table_nemesis_pressure", delta="mutate")
    rec["mutated"] = ["TEN → wide_passive branch"]
    rec["lost"] = ["TEN labeled linear_aggro"]
    rec["inherited"] = ["nemesis seed table"]
    rec["verification"] = "tests/test_k150_ten_nemesis.py"
    gate = validate_genome_diff(rec, config=CFG)
    assert gate["ok"] is True
    assert gate["failures"] == []


def test_novel_requires_novel_field():
    rec = empty_genome_diff(parent_mechanism="cemini_decide", delta="novel")
    rec["inherited"] = ["preflop chart"]
    rec["verification"] = "pytest tests/"
    gate = validate_genome_diff(rec, config=CFG)
    assert gate["ok"] is False
    assert "novel_requires_novel_field" in gate["failures"]


def test_missing_parent_and_verification_fail():
    gate = validate_genome_diff({}, config=CFG)
    assert gate["ok"] is False
    assert "missing_parent_mechanism" in gate["failures"]
    assert "missing_verification" in gate["failures"]
    assert "empty_lineage_fields" in gate["failures"]


def test_markdown_table_renders():
    rec = {
        "parent_mechanism": "hu_bb_defend",
        "delta": "mutate",
        "mutated": ["wider call vs steal"],
        "verification": "spot:hu_bb_defend_vs_minraise",
    }
    md = genome_diff_markdown_table(rec)
    assert "hu_bb_defend" in md
    assert "wider call vs steal" in md
