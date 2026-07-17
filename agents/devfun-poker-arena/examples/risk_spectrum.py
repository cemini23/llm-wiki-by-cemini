"""K156 — Participation (VPIP) + Proactiveness (PFR) risk-spectrum tags.

Tags for HL / nemesis exploit selection only. Do **not** copy GPT spectra
into decide() aggression. See references/risk-spectrum-tags.md.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Optional, Union

# Bands (document + tests). Tune only if existing fixtures require it.
VPIP_HIGH = 0.45
VPIP_MEDIUM = 0.25
PFR_HIGH = 0.15
PFR_MEDIUM = 0.05

_VALID_BANDS = frozenset({"high", "medium", "low"})
_VALID_SOURCES = frozenset({"arena_stats", "heuristic"})


def band_participation(vpip: float) -> str:
    """Map VPIP in [0,1] → high | medium | low."""
    v = float(vpip)
    if v >= VPIP_HIGH:
        return "high"
    if v >= VPIP_MEDIUM:
        return "medium"
    return "low"


def band_proactiveness(pfr: float) -> str:
    """Map PFR in [0,1] → high | medium | low."""
    p = float(pfr)
    if p >= PFR_HIGH:
        return "high"
    if p >= PFR_MEDIUM:
        return "medium"
    return "low"


def build_risk_spectrum(
    vpip: float,
    pfr: float,
    *,
    source: str = "heuristic",
) -> dict[str, Any]:
    """Build a risk_spectrum block from VPIP/PFR floats."""
    src = source if source in _VALID_SOURCES else "heuristic"
    return {
        "participation": band_participation(vpip),
        "proactiveness": band_proactiveness(pfr),
        "vpip": float(vpip),
        "pfr": float(pfr),
        "source": src,
    }


def validate_risk_spectrum(block: dict[str, Any]) -> list[str]:
    """Return list of validation errors (empty = ok)."""
    errs: list[str] = []
    if not isinstance(block, dict):
        return ["risk_spectrum must be an object"]
    for key in ("participation", "proactiveness", "vpip", "pfr", "source"):
        if key not in block:
            errs.append(f"missing {key}")
    if block.get("participation") not in _VALID_BANDS:
        errs.append("participation must be high|medium|low")
    if block.get("proactiveness") not in _VALID_BANDS:
        errs.append("proactiveness must be high|medium|low")
    if block.get("source") not in _VALID_SOURCES:
        errs.append("source must be arena_stats|heuristic")
    try:
        float(block.get("vpip"))  # type: ignore[arg-type]
        float(block.get("pfr"))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        errs.append("vpip/pfr must be numeric")
    return errs


def risk_spectrum_from_stats(
    stats: dict[str, Any],
    *,
    source: str = "arena_stats",
) -> dict[str, Any]:
    """Derive spectrum from an arena_stats-like dict."""
    vpip = float(stats.get("vpip") or stats.get("VPIP") or 0.0)
    pfr = float(stats.get("pfr") or stats.get("PFR") or 0.0)
    return build_risk_spectrum(vpip, pfr, source=source)


def load_profile_risk_spectrum(
    path: Union[str, Path],
) -> dict[str, Any]:
    """Load opponent profile JSON and return its risk_spectrum (derive if missing)."""
    p = Path(path)
    data = json.loads(p.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"profile must be object: {p}")
    existing = data.get("risk_spectrum")
    if isinstance(existing, dict) and not validate_risk_spectrum(existing):
        return existing
    stats = data.get("arena_stats") if isinstance(data.get("arena_stats"), dict) else {}
    return risk_spectrum_from_stats(stats, source="arena_stats")


def attach_risk_spectrum_to_hud(
    hud: dict[str, Any],
    spectrum: Optional[dict[str, Any]] = None,
    *,
    stats: Optional[dict[str, Any]] = None,
) -> dict[str, Any]:
    """Optional HUD enrich hook — tags only, no aggression rewrite."""
    out = dict(hud or {})
    if spectrum is None and stats is not None:
        spectrum = risk_spectrum_from_stats(stats)
    if spectrum is None:
        # Derive from HUD VPIP/PFR if present.
        if out.get("vpip") is not None or out.get("VPIP") is not None:
            spectrum = risk_spectrum_from_stats(out, source="heuristic")
        else:
            return out
    errs = validate_risk_spectrum(spectrum)
    if errs:
        return out
    out["risk_spectrum"] = spectrum
    return out


def default_opponent_profile_paths(
    root: Optional[Path] = None,
) -> list[Path]:
    """Known nemesis / sandbox opponent card paths."""
    base = root or Path(__file__).resolve().parent.parent
    opp = base / "research" / "opponents"
    return [
        opp / "ten-ladder-s1-profile.json",
        opp / "maniac-shark-ladder-s1-profile.json",
    ]
