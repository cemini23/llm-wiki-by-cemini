"""K152 — TTS inference regime labeling."""
from __future__ import annotations

import sys
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from inference_regime import (  # noqa: E402
    REGIME_LEAF_REDUCE,
    REGIME_SEQUENTIAL,
    infer_regime_from_env,
    tag_inference_regime,
)

_ENV_FLAGS = (
    "CEMINI_VERIFIER_BON",
    "CEMINI_TOT_SEARCH",
    "CEMINI_TREE_SEARCH",
    "CEMINI_PREFIX_SEARCH",
)


def test_env_off_defaults_to_sequential(monkeypatch):
    for key in _ENV_FLAGS:
        monkeypatch.delenv(key, raising=False)
    assert infer_regime_from_env() == REGIME_SEQUENTIAL


def test_verifier_bon_maps_to_leaf_reduce(monkeypatch):
    monkeypatch.delenv("CEMINI_TOT_SEARCH", raising=False)
    monkeypatch.setenv("CEMINI_VERIFIER_BON", "1")
    assert infer_regime_from_env() == REGIME_LEAF_REDUCE


def test_tag_inference_regime_adds_tags_without_mutating(monkeypatch):
    monkeypatch.delenv("CEMINI_VERIFIER_BON", raising=False)
    ctx = {"table_format": "hu", "street": "preflop"}
    tagged = tag_inference_regime(ctx)
    assert tagged["inference_regime"] == REGIME_SEQUENTIAL
    assert tagged["inference_regime_source"]
    assert tagged["table_format"] == "hu"
    assert "inference_regime" not in ctx


def test_docs_mention_arxiv_id():
    docs = Path(__file__).resolve().parent.parent / "references" / "tts-inference-regimes.md"
    assert "2608.04001" in docs.read_text(encoding="utf-8")
