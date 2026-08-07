"""K250 — canary trap classification for wrong tool picks (fail-open).

Keyword heuristics only: classify a description of a wrong tool/solver
pick into one of the six canary trap labels, or None when nothing
matches. Advisory — never a production gate.
"""
from __future__ import annotations

from typing import Any

TRAP_SEMANTIC_DECOY = "semantic_decoy"
TRAP_PARAMETER_TRAP = "parameter_trap"
TRAP_CAPABILITY_MIRAGE = "capability_mirage"
TRAP_PREREQUISITE_BLINDNESS = "prerequisite_blindness"
TRAP_TEMPORAL_DECOY = "temporal_decoy"
TRAP_GRANULARITY_TRAP = "granularity_trap"

_RULES = (
    (
        TRAP_SEMANTIC_DECOY,
        ("decoy", "looks like", "similar name", "imposter", "confused with"),
    ),
    (TRAP_PARAMETER_TRAP, ("parameter", "hyperparameter", "config value")),
    (
        TRAP_CAPABILITY_MIRAGE,
        ("capability mirage", "capability tier", "advanced solver", "premium", "overclaim"),
    ),
    (
        TRAP_PREREQUISITE_BLINDNESS,
        ("prerequisite", "missing dependency", "requires install", "requires setup", "not installed"),
    ),
    (
        TRAP_TEMPORAL_DECOY,
        ("temporal", "outdated", "stale version", "deprecated", "superseded"),
    ),
    (TRAP_GRANULARITY_TRAP, ("granularity", "granular", "too coarse", "too fine")),
)


def classify_trap(description: Any) -> str | None:
    """Return the first matching trap label, or None on empty/unknown.

    Fail-open: never raises; non-string and empty input return None.
    """
    if not description:
        return None
    text = str(description).lower()
    for label, keywords in _RULES:
        for keyword in keywords:
            if keyword in text:
                return label
    return None
