"""Opponent-conditioned best-response modes (risk-spectrum → margins).

Maps K156 participation × proactiveness tags to bounded overlay deltas
(``nit`` / ``lag`` / ``wide_passive`` / ``balanced``). Does **not** copy
frontier-LLM aggression spectra into decide() — only best-response nudges
vs tagged foes. See ``references/opponent-modes.md``.

Flag: ``CEMINI_OPPONENT_MODES=1`` (off → no overlay, identical decide path).
Each delta clamped to ±0.06. ``cemini_decide`` applies only when private HUD
mode is ``unknown``/``balanced`` — does not double-stack on rock/maniac/tight.
"""
from __future__ import annotations

import os
from typing import Any, Optional

from risk_spectrum import (
    attach_risk_spectrum_to_hud,
    build_risk_spectrum,
    validate_risk_spectrum,
)

MODES = ("nit", "lag", "wide_passive", "balanced")
DELTA_CLAMP = 0.06

# Approx overlays from master plan (clamped on apply).
_MODE_DELTAS: dict[str, dict[str, float]] = {
    "nit": {
        # Steal / bluff more; fold to aggression
        "bet_bar_delta": -0.04,
        "fold_slack_delta": 0.04,
        "preflop_fold_margin_delta": -0.03,
    },
    "lag": {
        # Tighten calls, fewer bluffs, trap
        "bet_bar_delta": 0.04,
        "fold_slack_delta": -0.03,
        "call_margin_delta": 0.04,
    },
    "wide_passive": {
        # Value bet / iso more
        "bet_bar_delta": -0.05,
        "call_margin_delta": -0.02,
    },
    "balanced": {},
}

# Absolute open-steal equity bar (lower = steal more). Only applied for nit
# when HUD did not already set open_steal_equity.
_NIT_OPEN_STEAL_EQUITY = 0.48


def opponent_modes_enabled() -> bool:
    return os.environ.get("CEMINI_OPPONENT_MODES", "").strip().lower() in (
        "1",
        "true",
        "yes",
        "on",
    )


def _clamp_delta(x: float) -> float:
    return max(-DELTA_CLAMP, min(DELTA_CLAMP, float(x)))


def mode_from_spectrum(spectrum: Optional[dict[str, Any]]) -> str:
    """Map participation × proactiveness → mode label.

    | participation | proactiveness | mode          |
    |---------------|---------------|---------------|
    | low           | low/medium    | nit           |
    | high          | high          | lag           |
    | high          | low/medium    | wide_passive  |
    | else          | else          | balanced      |
    """
    if not isinstance(spectrum, dict):
        return "balanced"
    if validate_risk_spectrum(spectrum):
        return "balanced"
    part = str(spectrum.get("participation") or "").lower()
    pro = str(spectrum.get("proactiveness") or "").lower()
    if part == "low" and pro in ("low", "medium"):
        return "nit"
    if part == "high" and pro == "high":
        return "lag"
    if part == "high" and pro in ("low", "medium"):
        return "wide_passive"
    return "balanced"


def resolve_opponent_mode(
    hud: Optional[dict[str, Any]] = None,
    *,
    spectrum: Optional[dict[str, Any]] = None,
    cold_start: Optional[bool] = None,
) -> str:
    """Resolve mode from spectrum / HUD. Cold-start or missing → balanced."""
    h = dict(hud or {})
    if cold_start is None:
        cold_start = bool(h.get("coldStart"))
    if cold_start:
        return "balanced"
    if spectrum is None:
        spectrum = h.get("risk_spectrum") if isinstance(h.get("risk_spectrum"), dict) else None
    if spectrum is None:
        # Derive from HUD VPIP/PFR when present
        if h.get("vpip") is not None or h.get("VPIP") is not None or h.get("pfr") is not None:
            spectrum = build_risk_spectrum(
                float(h.get("vpip") if h.get("vpip") is not None else h.get("VPIP") or 0.0),
                float(h.get("pfr") if h.get("pfr") is not None else h.get("PFR") or 0.0),
                source="heuristic",
            )
        else:
            return "balanced"
    return mode_from_spectrum(spectrum)


def mode_margin_deltas(mode: str) -> dict[str, float]:
    """Bounded margin deltas for *mode* (empty for balanced / unknown)."""
    raw = _MODE_DELTAS.get(str(mode).lower().strip(), {})
    if not raw:
        return {}
    return {k: _clamp_delta(v) for k, v in raw.items()}


def apply_opponent_mode_to_margins(
    margins: dict[str, Any],
    hud: Optional[dict[str, Any]] = None,
    *,
    mode: Optional[str] = None,
    spectrum: Optional[dict[str, Any]] = None,
) -> dict[str, Any]:
    """Stack mode deltas onto *margins*. Absolute open_steal only if unset.

    Does not replace private HUD exploit keys already present except additive
    ``*_delta`` fields. Returns a new dict.
    """
    out = dict(margins or {})
    m = mode if mode is not None else resolve_opponent_mode(hud, spectrum=spectrum)
    deltas = mode_margin_deltas(m)
    for k, v in deltas.items():
        out[k] = float(out.get(k, 0.0) or 0.0) + float(v)
    # Nit steal bar: only fill when HUD/exploit did not set open_steal_equity
    if m == "nit" and "open_steal_equity" not in out:
        out["open_steal_equity"] = float(_NIT_OPEN_STEAL_EQUITY)
    return out


def attach_opponent_mode_to_hud(
    hud: dict[str, Any],
    *,
    spectrum: Optional[dict[str, Any]] = None,
) -> dict[str, Any]:
    """Tag HUD with risk_spectrum (if missing) + opponent_mode label.

    Tags only when flag is off still safe — mode label is informational;
    margins apply only via ``apply_opponent_mode_to_margins`` under the flag.
    """
    out = attach_risk_spectrum_to_hud(hud, spectrum=spectrum)
    mode = resolve_opponent_mode(out, spectrum=out.get("risk_spectrum") if isinstance(out.get("risk_spectrum"), dict) else spectrum)
    out["opponent_mode"] = mode
    return out
