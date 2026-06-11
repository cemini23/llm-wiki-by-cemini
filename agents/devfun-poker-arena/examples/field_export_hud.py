"""Overlay live opponent HUD with field export stats (agents.jsonl from hourly export).

Stub/minimal runtime mining: when arena seat stats are missing or low-sample,
pull VPIP/PFR/3b from the latest export crawl on disk (CEMINI_EXPORT_DIR).
"""
from __future__ import annotations

import os
import time
from pathlib import Path
from typing import Any

_AGENT_ROOT = Path(__file__).resolve().parent.parent
_EXAMPLES = Path(__file__).resolve().parent

import sys

if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from export_bundle import load_export_agents  # noqa: E402

_CACHE: dict[str, Any] = {
    "index": {},
    "loaded_at": 0.0,
    "export_dir": "",
    "agents_mtime": 0.0,
}


def field_export_hud_enabled() -> bool:
    raw = os.environ.get("CEMINI_FIELD_EXPORT_HUD", "1").strip().lower()
    return raw not in ("0", "false", "no", "off")


def _ttl_seconds() -> float:
    raw = os.environ.get("CEMINI_FIELD_EXPORT_HUD_TTL_S", "3600")
    try:
        return max(60.0, float(raw))
    except ValueError:
        return 3600.0


def _min_live_sample() -> int:
    raw = os.environ.get("CEMINI_FIELD_EXPORT_MIN_LIVE_SAMPLE", "8")
    try:
        return max(0, int(raw))
    except ValueError:
        return 8


def _resolve_export_dir() -> Path | None:
    raw = (
        os.environ.get("CEMINI_FIELD_EXPORT_DIR")
        or os.environ.get("CEMINI_EXPORT_DIR")
        or ""
    ).strip()
    if not raw:
        return None
    path = Path(raw)
    if not path.is_absolute():
        path = (_AGENT_ROOT / path).resolve()
    return path if path.is_dir() else None


def _agents_file_mtime(export_dir: Path) -> float:
    best = 0.0
    for name in ("agents.jsonl", "agents-all.jsonl"):
        p = export_dir / name
        if p.is_file():
            best = max(best, p.stat().st_mtime)
    for batch in export_dir.glob("agents-crawl-batch*.jsonl"):
        best = max(best, batch.stat().st_mtime)
    return best


def _norm_handle(handle: str | None) -> str:
    return (handle or "").strip().lower()


def _export_stats_to_live(stats: dict, hands: int | None) -> dict[str, Any]:
    """Map export agent.stats keys to arena seat stat shape."""
    out: dict[str, Any] = {}
    sample = stats.get("sample_size") or stats.get("sampleSize") or hands
    if sample is not None:
        out["sampleSize"] = int(sample)
    vpip = stats.get("vpip")
    if vpip is not None:
        out["vpip"] = float(vpip)
    pfr = stats.get("pfr")
    if pfr is not None:
        out["pfr"] = float(pfr)
    tb = stats.get("three_bet_pct") or stats.get("threeBetPct")
    if tb is not None:
        out["threeBetPct"] = float(tb)
        out["three_bet_pct"] = float(tb)
    style_label = stats.get("playing_style") or stats.get("playingStyle")
    if style_label:
        out["playingStyle"] = {"label": style_label}
    return out


def _build_index(export_dir: Path) -> dict[str, dict]:
    index: dict[str, dict] = {}
    for row in load_export_agents(export_dir):
        handle = _norm_handle(row.get("handle") or row.get("name"))
        if not handle:
            continue
        stats = row.get("stats") or {}
        live_stats = _export_stats_to_live(stats, row.get("hands"))
        index[handle] = {
            "handle": row.get("handle"),
            "rank": row.get("rank"),
            "chips": row.get("chips"),
            "hands": row.get("hands"),
            "stats": live_stats,
        }
    return index


def _refresh_cache_if_needed() -> dict[str, dict]:
    export_dir = _resolve_export_dir()
    if export_dir is None:
        _CACHE["index"] = {}
        return {}
    mtime = _agents_file_mtime(export_dir)
    now = time.time()
    stale = (
        _CACHE.get("export_dir") != str(export_dir)
        or _CACHE.get("agents_mtime") != mtime
        or now - float(_CACHE.get("loaded_at") or 0) > _ttl_seconds()
    )
    if stale:
        _CACHE["index"] = _build_index(export_dir)
        _CACHE["loaded_at"] = now
        _CACHE["export_dir"] = str(export_dir)
        _CACHE["agents_mtime"] = mtime
    return _CACHE["index"]


def lookup_export_agent(handle: str) -> dict | None:
    if not field_export_hud_enabled():
        return None
    key = _norm_handle(handle)
    if not key:
        return None
    return _refresh_cache_if_needed().get(key)


def overlay_export_field_stats(handle: str, live_stats: dict | None) -> dict:
    """Merge export stats when live HUD is thin or missing VPIP."""
    live = dict(live_stats or {})
    if not field_export_hud_enabled():
        return live
    row = lookup_export_agent(handle)
    if not row:
        return live
    export_stats = row.get("stats") or {}
    if not export_stats:
        return live

    live_sample = int(live.get("sampleSize") or live.get("handsPlayed") or live.get("hands") or 0)
    export_hands = int(row.get("hands") or export_stats.get("sampleSize") or 0)
    min_live = _min_live_sample()
    trust_live = live_sample >= min_live and live.get("vpip") is not None
    if trust_live:
        return live

    merged = dict(live)
    for key, val in export_stats.items():
        if merged.get(key) is None and val is not None:
            merged[key] = val
    if export_hands:
        merged["sampleSize"] = max(live_sample, export_hands)
    merged["field_export_overlay"] = True
    merged["field_export_hands"] = export_hands
    return merged


def enrich_table_seats_from_export(table: dict) -> dict[str, dict]:
    """handle → export stats for all non-hero seats (session memory / debugging)."""
    if not field_export_hud_enabled():
        return {}
    hero = table.get("selfSeatNumber")
    out: dict[str, dict] = {}
    for seat in table.get("seats") or []:
        if seat.get("seatNumber") == hero:
            continue
        handle = str(seat.get("agentHandle") or seat.get("agentName") or "")
        row = lookup_export_agent(handle)
        if row and row.get("stats"):
            out[_norm_handle(handle)] = dict(row["stats"])
    return out
