"""K143 memoryless-threshold docs + config tag (advisory; no decide path)."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REF = ROOT / "references" / "memoryless-threshold.md"
CFG = ROOT / "config" / "hu_hierarchical_memory.json"


def test_memoryless_threshold_reference_exists():
    assert REF.is_file()
    text = REF.read_text(encoding="utf-8")
    assert "memoryless_threshold" in text
    assert "2607.16145" in text
    assert "absolute thresholds" in text.lower() or "absolute" in text.lower()
    assert "no `decide()`" in text.lower() or "no decide()" in text.lower()


def test_config_documents_memoryless_threshold_tag():
    cfg = json.loads(CFG.read_text(encoding="utf-8"))
    assert cfg.get("memoryless_threshold_tag") == "memoryless_threshold"
    block = cfg.get("memoryless_threshold") or {}
    assert block.get("k") == "K143"
    assert block.get("advisory_only") is True
    assert "absolute" in (block.get("rule") or "").lower()
