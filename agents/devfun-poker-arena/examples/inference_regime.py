"""K152 — test-time scaling inference regime label (advisory).

Three regimes from the TTS taxonomy (arXiv 2608.04001):

- ``sequential``: one evolving thought stream / adaptive stop (default).
- ``leaf_reduce``: sample N complete actions, then vote/verifier/MBR —
  ``CEMINI_VERIFIER_BON`` maps here.
- ``prefix_search``: ToT-style partial action trees. Labeled only when an
  operator already runs a tree/ToT solver under one of the declared flags;
  nothing in this repo invents new solver trees.

Fail-open: never raises; a bare env reports ``sequential``.
"""
from __future__ import annotations

import os
from typing import Any

REGIME_SEQUENTIAL = "sequential"
REGIME_LEAF_REDUCE = "leaf_reduce"
REGIME_PREFIX_SEARCH = "prefix_search"

# Operator-set flags that mean a ToT-style prefix search is already active.
# Do not add new solver trees here — this list only *labels* existing ones.
_PREFIX_SEARCH_FLAGS = (
    "CEMINI_TOT_SEARCH",
    "CEMINI_TREE_SEARCH",
    "CEMINI_PREFIX_SEARCH",
)


def _truthy(val: str | None) -> bool:
    return (val or "").strip().lower() in ("1", "true", "yes", "on")


def infer_regime_from_env() -> str:
    """Return the declared TTS inference regime label from env flags."""
    if _truthy(os.environ.get("CEMINI_VERIFIER_BON")):
        return REGIME_LEAF_REDUCE
    for key in _PREFIX_SEARCH_FLAGS:
        if _truthy(os.environ.get(key)):
            return REGIME_PREFIX_SEARCH
    return REGIME_SEQUENTIAL


def _regime_source() -> tuple[str, str]:
    if _truthy(os.environ.get("CEMINI_VERIFIER_BON")):
        return REGIME_LEAF_REDUCE, "env:CEMINI_VERIFIER_BON"
    for key in _PREFIX_SEARCH_FLAGS:
        if _truthy(os.environ.get(key)):
            return REGIME_PREFIX_SEARCH, f"env:{key}"
    return REGIME_SEQUENTIAL, "default"


def tag_inference_regime(ctx: dict) -> dict:
    """Return a shallow copy of ctx tagged with inference_regime + source."""
    out = dict(ctx or {})
    regime, source = _regime_source()
    out["inference_regime"] = regime
    out["inference_regime_source"] = source
    return out
