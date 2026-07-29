"""K198 swap-regret + verifier–deployment gap docs (advisory; no decide path)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SWAP = ROOT / "references" / "swap-regret-training-notes.md"
GAP = ROOT / "references" / "verifier-deployment-gap.md"
RUBRIC = ROOT / "references" / "league-promotion-rubric.md"


def test_swap_regret_notes_exist():
    text = SWAP.read_text(encoding="utf-8")
    assert "2607.23333" in text
    assert "no hard" in text.lower() or "Hard-gate" in text or "hard-gate" in text
    assert "cemini_decide" in text or "decide()" in text


def test_verifier_deployment_gap_notes_exist():
    text = GAP.read_text(encoding="utf-8")
    assert "2607.24300" in text
    assert "self-authored" in text.lower() or "self-authored" in text
    assert "yardstick" in text.lower()
    assert "play-adequacy" in text.lower() or "play_adequacy" in text.lower()


def test_league_rubric_links_k198_gap():
    text = RUBRIC.read_text(encoding="utf-8")
    assert "K198" in text
    assert "verifier-deployment-gap.md" in text
