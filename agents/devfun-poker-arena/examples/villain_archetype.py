"""Villain archetype classification + exploit margins (S2 audit consensus).

Archetypes: premium_nit, wide_passive, linear_aggro, phoenix_passive, unknown.
Zero runtime LLM — env toggles gate each exploit lane.
"""
from __future__ import annotations

import os
from typing import Any

_MIN_SAMPLE = 8

_PHOENIX_PREFIXES = (
    "phoenix-rises-nrkdhd",
    "phoenix-nrkdhd",
    "phoenix-",
)


def _env_on(key: str, default: str = "1") -> bool:
    return os.environ.get(key, default).strip().lower() in ("1", "true", "yes")


def archetype_toggles_enabled() -> bool:
    return _env_on("CEMINI_NEMESIS_ARCHETYPE", "1")


def premium_nit_exploit_on() -> bool:
    return archetype_toggles_enabled() and _env_on("CEMINI_NEMESIS_PREMIUM_NIT", "1")


def wide_passive_exploit_on() -> bool:
    return _env_on("CEMINI_ISO_PASSIVE_LP", "1") or (
        archetype_toggles_enabled() and _env_on("CEMINI_NEMESIS_WIDE_PASSIVE", "1")
    )


def linear_aggro_exploit_on() -> bool:
    return archetype_toggles_enabled() and _env_on("CEMINI_NEMESIS_LINEAR_AGGRO", "1")


def phoenix_cluster_exploit_on() -> bool:
    return archetype_toggles_enabled() and _env_on("CEMINI_NEMESIS_PHOENIX_CLUSTER", "1")


def seat_matrix_v2_enabled() -> bool:
    return _env_on("CEMINI_SEAT_MATRIX_V2", "1")


def eval_panel_gate_enabled() -> bool:
    return _env_on("CEMINI_EVAL_PANEL_GATE", "1")


def eval_panel_bb100_floor() -> float:
    try:
        return float(os.environ.get("CEMINI_EVAL_PANEL_BB100_FLOOR", "-17.45"))
    except ValueError:
        return -17.45


def phoenix_cluster_handle(handle: str) -> bool:
    h = (handle or "").strip().lower()
    return any(h.startswith(p) for p in _PHOENIX_PREFIXES)


def _playing_style_str(stats: dict) -> str:
    style = stats.get("playingStyle") or stats.get("playing_style") or {}
    if isinstance(style, dict):
        return str(style.get("archetype") or style.get("playingStyle") or "").lower()
    return str(style).lower()


def raise_gap(stats: dict) -> float:
    vpip = stats.get("vpip")
    pfr = stats.get("pfr")
    if vpip is None:
        return 0.0
    return max(0.0, float(vpip) - float(pfr or 0.0))


def premium_concentration_index(stats: dict) -> float:
    """Proxy for premium-heavy villains (low VPIP / low PFR, high trap risk)."""
    vpip = stats.get("vpip")
    pfr = stats.get("pfr")
    if vpip is None:
        return 0.0
    vp, pf = float(vpip), float(pfr or 0.0)
    if vp < 0.12:
        return min(1.0, 0.65 + (0.12 - vp) * 2.5)
    if vp < 0.18 and pf < 0.08:
        return 0.55
    if vp < 0.22 and pf < 0.10:
        return 0.35
    return max(0.0, 0.20 - vp * 0.25)


def classify_villain_archetype(stats: dict, *, handle: str = "") -> str:
    sample = int(stats.get("sampleSize") or stats.get("hands") or 0)
    vpip = stats.get("vpip")
    if vpip is None and sample < _MIN_SAMPLE:
        if phoenix_cluster_handle(handle):
            return "phoenix_passive"
        return "unknown"
    if vpip is None:
        return "unknown"

    pfr = float(stats.get("pfr") or 0.0)
    vp = float(vpip)
    style = _playing_style_str(stats)
    rg = raise_gap(stats)

    if phoenix_cluster_handle(handle) and phoenix_cluster_exploit_on():
        if vp < 0.20 and pfr < 0.10:
            return "phoenix_passive"
        return "wide_passive" if rg > 0.18 else "phoenix_passive"

    if vp < 0.18 and pfr < 0.08:
        return "premium_nit"
    if "tight-measured" in style or "tight-aggressive" in style:
        return "premium_nit" if pfr < 0.12 else "linear_aggro"
    if vp >= 0.35 and pfr < 0.12:
        return "wide_passive"
    if "loose-passive" in style or (vp >= 0.30 and rg >= 0.18):
        return "wide_passive"
    if vp >= 0.28 and pfr >= 0.16:
        return "linear_aggro"
    if "loose-aggressive" in style or "lag" in style:
        return "linear_aggro"
    if "balanced-aggressive" in style and pfr >= 0.15:
        return "linear_aggro"
    return "unknown"


def archetype_to_legacy_mode(archetype: str) -> str:
    if archetype == "premium_nit":
        return "rock"
    if archetype in ("wide_passive", "phoenix_passive"):
        return "tight"
    if archetype == "linear_aggro":
        return "maniac"
    return "unknown"


def exploit_margins_for_archetype(archetype: str) -> dict[str, float]:
    """Archetype-specific margin deltas (merged into decide margins)."""
    if archetype == "premium_nit" and premium_nit_exploit_on():
        return {
            "bet_bar_delta": -0.12,
            "call_margin_delta": 0.04,
            "fold_slack_delta": 0.06,
            "preflop_fold_margin_delta": 0.05,
            "open_steal_equity": 0.30,
        }
    if archetype in ("wide_passive", "phoenix_passive") and wide_passive_exploit_on():
        return {
            "bet_bar_delta": 0.08,
            "call_margin_delta": -0.04,
            "fold_slack_delta": -0.02,
            "preflop_fold_margin_delta": -0.02,
            "open_steal_equity": 0.38,
        }
    if archetype == "linear_aggro" and linear_aggro_exploit_on():
        return {
            "bet_bar_delta": 0.04,
            "call_margin_delta": -0.05,
            "fold_slack_delta": -0.03,
            "preflop_fold_margin_delta": -0.03,
            "open_steal_equity": 0.99,
        }
    return {
        "bet_bar_delta": 0.0,
        "call_margin_delta": 0.0,
        "fold_slack_delta": 0.0,
        "preflop_fold_margin_delta": 0.0,
        "open_steal_equity": 0.99,
    }


def _seat_stats(seat: dict) -> dict:
    raw = seat.get("stats") or seat.get("agentStats") or {}
    if not isinstance(raw, dict):
        return {}
    out: dict[str, Any] = dict(raw)
    if out.get("vpip") is None and seat.get("vpip") is not None:
        out["vpip"] = seat.get("vpip")
    if out.get("pfr") is None and seat.get("pfr") is not None:
        out["pfr"] = seat.get("pfr")
    if out.get("sampleSize") is None:
        out["sampleSize"] = seat.get("handsPlayed") or seat.get("hands")
    return out


def dominant_villain_from_table(table: dict) -> tuple[str, dict, str]:
    """Return (handle, stats, archetype) for largest preflop bettor (non-hero)."""
    hero = table.get("selfSeatNumber")
    best_bet = -1
    best_seat: dict | None = None
    for seat in table.get("seats") or []:
        if seat.get("seatNumber") == hero:
            continue
        bet = int(seat.get("currentBetChips") or 0)
        if bet > best_bet:
            best_bet = bet
            best_seat = seat
    if not best_seat:
        return "", {}, "unknown"
    handle = str(
        best_seat.get("agentHandle") or best_seat.get("agentName") or ""
    )
    stats = _seat_stats(best_seat)
    arch = classify_villain_archetype(stats, handle=handle)
    return handle, stats, arch


def enrich_hud_from_table(hud: dict, table: dict) -> dict:
    """Attach archetype + concentration metrics to opponent HUD dict."""
    from field_export_hud import (  # noqa: WPS433
        enrich_table_seats_from_export,
        overlay_export_field_stats,
    )

    out = dict(hud)
    handle, stats, arch = dominant_villain_from_table(table)
    if handle:
        out["villain_handle"] = handle
    stats = overlay_export_field_stats(handle, stats or {})
    if stats:
        out.setdefault("stats", stats)
        out["vpip"] = stats.get("vpip")
        out["pfr"] = stats.get("pfr")
    if stats and arch == "unknown":
        arch = classify_villain_archetype(stats, handle=handle)
    if arch != "unknown":
        out["archetype"] = arch
        out["mode"] = archetype_to_legacy_mode(arch)
        arch_margins = exploit_margins_for_archetype(arch)
        base = out.get("margins") or {}
        out["margins"] = {**base, **arch_margins}
    if stats:
        out["premium_concentration"] = premium_concentration_index(stats)
        out["raise_gap"] = raise_gap(stats)
    seat_field = enrich_table_seats_from_export(table)
    if seat_field:
        out["field_export_seats"] = seat_field
    return out


def jeff_nemesis_handle(handle: str) -> bool:
    return (handle or "").strip().lower() in ("0xjeff_ai", "0xjeff")
