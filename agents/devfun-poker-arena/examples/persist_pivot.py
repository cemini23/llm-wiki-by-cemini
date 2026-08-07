"""K253 — verification-gated persist/pivot decision helpers (fail-open)."""
from __future__ import annotations

from typing import Any


def should_persist(evidence_ok: Any, review_ok: Any) -> bool:
    """Persist only when evidence still holds AND independent review passed."""
    return bool(evidence_ok) and bool(review_ok)


def should_pivot(evidence_ok: Any) -> bool:
    """Pivot when street/evidence falsifies the line (measured failure)."""
    return not bool(evidence_ok)
