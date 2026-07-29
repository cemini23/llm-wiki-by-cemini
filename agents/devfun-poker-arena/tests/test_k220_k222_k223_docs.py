"""Jul 29 steals: K220 claim ceiling, K222 containment, K223 tool hierarchy."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CEILING = ROOT / "references" / "eval-claim-ceiling.md"
CONTAIN = ROOT / "references" / "sandbox-live-containment.md"
HIER = ROOT / "references" / "tool-output-instruction-hierarchy.md"
CLAIMED = ROOT / "references" / "claimed-authorization-guard.md"
SWAP = ROOT / "references" / "swap-regret-training-notes.md"
RUBRIC = ROOT / "references" / "league-promotion-rubric.md"


def test_k220_eval_claim_ceiling_docs():
    text = CEILING.read_text(encoding="utf-8")
    assert "2607.21735" in text
    assert "crossing" in text.lower() or "harm" in text.lower()
    assert "yardstick" in text.lower() or "play-adequacy" in text.lower()
    assert "K220" in RUBRIC.read_text(encoding="utf-8")


def test_k222_sandbox_live_containment_docs():
    text = CONTAIN.read_text(encoding="utf-8")
    assert "2607.25379" in text
    assert "FORCE_CREDS" in text or "FORCE_CREDS" in text.upper()
    assert "LIVE" in text
    assert "sandbox" in text.lower()


def test_k223_tool_output_hierarchy_docs():
    text = HIER.read_text(encoding="utf-8")
    assert "2607.25987" in text
    assert "tool_result" in text
    assert "observation" in text
    assert "untrusted" in text.lower()
    claimed = CLAIMED.read_text(encoding="utf-8")
    assert "tool-output-instruction-hierarchy.md" in claimed


def test_k163_shelf_cross_ref_on_swap_regret_notes():
    text = SWAP.read_text(encoding="utf-8")
    assert "K163" in text or "shelf" in text.lower()
    assert "gambling-wiki" in text
