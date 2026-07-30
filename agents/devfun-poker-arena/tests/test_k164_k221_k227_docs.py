"""Jul 30 steals: K164 CCS-MCCFR, K221/K229 tool depth, K227 KV isolation."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CCS = ROOT / "references" / "ccs-mccfr-chance-sampling.md"
DEPTH = ROOT / "references" / "tool-depth-standing-policy.md"
KV = ROOT / "references" / "session-kv-isolation.md"
DEEP = ROOT / "references" / "deepcfr-lite.md"
HIER = ROOT / "references" / "hierarchical-session-memory.md"
COG = ROOT / "references" / "cognitive-security-deploy.md"


def test_k164_ccs_mccfr_docs():
    text = CCS.read_text(encoding="utf-8")
    assert "2607.27035" in text
    assert "decide()" in text or "cemini_decide" in text
    assert "Linear CFR" in text or "linear" in text.lower()
    assert "ccs-mccfr-chance-sampling.md" in DEEP.read_text(encoding="utf-8")


def test_k221_k229_tool_depth_standing_docs():
    text = DEPTH.read_text(encoding="utf-8")
    assert "standing" in text.lower()
    assert "advantage" in text.lower()
    assert "K199" in text or "solver-grounded" in text.lower()
    assert "tool-depth-standing-policy.md" in COG.read_text(encoding="utf-8")


def test_k227_session_kv_isolation_docs():
    text = KV.read_text(encoding="utf-8")
    assert "2607.27090" in text
    assert "session_villain_memory" in text
    assert "cross" in text.lower()
    assert "session-kv-isolation.md" in HIER.read_text(encoding="utf-8")
