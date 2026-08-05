"""Discover live Playground seasons and retarget the lobby mid-run.

S12 (cmseo8d3e4fmh12qragnvqct6) ran ~3.5h on 2026-08-04 and ended while the
lobby stayed pinned to dead S11. Poll list-active / list-all and switch.
"""
from __future__ import annotations

import os
import re
import time
from pathlib import Path
from typing import Any, Optional

_PLAYGROUND_RE = re.compile(r"playground\s*s?(\d+)", re.I)


def _norm_comp_list(raw: Any) -> list[dict]:
    if isinstance(raw, list):
        return [c for c in raw if isinstance(c, dict)]
    if isinstance(raw, dict):
        for key in ("data", "competitions", "items"):
            val = raw.get(key)
            if isinstance(val, list):
                return [c for c in val if isinstance(c, dict)]
    return []


def _is_poker_playground(comp: dict) -> bool:
    name = str(comp.get("name") or "")
    blob = f"{name} {comp.get('description') or ''}".lower()
    if "playground" not in blob:
        return False
    if "tournament" in blob and "playground" not in name.lower():
        return False
    return True


def _season_number(comp: dict) -> int:
    try:
        sn = int(comp.get("seasonNumber") or 0)
        if sn:
            return sn
    except (TypeError, ValueError):
        pass
    m = _PLAYGROUND_RE.search(str(comp.get("name") or ""))
    if m:
        return int(m.group(1))
    return 0


def _status(comp: dict) -> str:
    return str(comp.get("status") or comp.get("arenaStatus") or "").strip()


def discover_active_playground(client: Any) -> Optional[dict]:
    """Return the newest Active poker Playground, or None."""
    rows: list[dict] = []
    try:
        rows.extend(_norm_comp_list(client.get("/competition/list-active")))
    except Exception:
        pass
    try:
        rows.extend(_norm_comp_list(client.get("/competition/list-all")))
    except Exception:
        pass

    seen: set[str] = set()
    playgrounds: list[dict] = []
    for comp in rows:
        cid = str(comp.get("id") or "").strip()
        if not cid or cid in seen or not _is_poker_playground(comp):
            continue
        seen.add(cid)
        playgrounds.append(comp)

    live = [c for c in playgrounds if _status(c).lower() in ("active", "live", "")]
    # list-active rows often omit status — treat as live if they came from active list
    # and are playgrounds. Re-fetch active-only set:
    active_ids: set[str] = set()
    try:
        active_ids = {
            str(c.get("id") or "")
            for c in _norm_comp_list(client.get("/competition/list-active"))
            if c.get("id")
        }
    except Exception:
        active_ids = set()

    candidates = []
    for comp in playgrounds:
        cid = str(comp.get("id") or "")
        st = _status(comp).lower()
        if cid in active_ids and st not in ("ended", "closed", "complete", "completed"):
            candidates.append(comp)
        elif st in ("active", "live"):
            candidates.append(comp)
    if not candidates:
        return None
    candidates.sort(key=_season_number, reverse=True)
    best = candidates[0]
    return {
        "id": str(best.get("id")),
        "name": str(best.get("name") or ""),
        "seasonNumber": _season_number(best),
        "status": _status(best) or "Active",
    }


def apply_live_playground_env(hit: dict, *, env_path: str | Path | None = None) -> dict[str, str]:
    """Update process env (+ optional .env) for a discovered playground."""
    season = int(hit.get("seasonNumber") or 0)
    cid = str(hit["id"])
    slug = f"playground-s{season}-live" if season else "playground-next-live"
    label = f"Playground_S{season}" if season else "Playground"
    role = f"s{season}_playground" if season else "playground"
    kv = {
        "ARENA_LOBBY_COMPETITION_ID": cid,
        "CEMINI_LOBBY_LABEL": label,
        "CEMINI_LOBBY_ROLE": role,
        "CEMINI_PRIMARY_TRACK": "playground",
        "CEMINI_PRIMARY": "lobby",
        "CEMINI_HL_PRIMARY_COMP": cid,
        "CEMINI_EXPORT_MATCH": cid,
        "CEMINI_EXPORT_DIR": f"reports/exports/{slug}",
        "CEMINI_FIELD_EXPORT_DIR": f"reports/exports/{slug}",
        "CEMINI_PREFLOP_LOG": "1",
        "CEMINI_PREFLOP_LOG_PATH": f"reports/exports/{slug}/preflop_decisions.jsonl",
        "AGENT_VERSION": (
            f"playground-s{season}.qual.2026-08-05.watch-v1"
            if season
            else "playground-next.qual.2026-08-05.watch-v1"
        ),
        "CEMINI_NEMESIS_TIGHT": "0",
        "CEMINI_KO_SURVIVAL_MIN_STACK": "400",
        "CEMINI_TAG_WIDEN": "1",
        "CEMINI_GIN_KILL": "1",
    }
    if season:
        kv[f"S{season}_PLAYGROUND_COMP"] = cid
    os.environ.update(kv)
    path = Path(env_path) if env_path else None
    if path is None:
        guess = Path(__file__).resolve().parent.parent / ".env"
        if guess.is_file():
            path = guess
    if path is not None and path.is_file():
        _upsert_env_file(path, kv)
    export_dir = Path(kv["CEMINI_EXPORT_DIR"])
    if not export_dir.is_absolute():
        export_dir = Path(__file__).resolve().parent.parent / export_dir
    export_dir.mkdir(parents=True, exist_ok=True)
    state_path = export_dir / "crawl_state.json"
    if not state_path.exists():
        state_path.write_text(
            '{"completed_agent_ids":[],"cycles":0,"leaderboard_total":0}\n',
            encoding="utf-8",
        )
    return kv


def _upsert_env_file(path: Path, kv: dict[str, str]) -> None:
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    lines = text.splitlines()
    seen: set[str] = set()
    out: list[str] = []
    for line in lines:
        if "=" in line and not line.strip().startswith("#"):
            key = line.split("=", 1)[0]
            if key in kv:
                out.append(f"{key}={kv[key]}")
                seen.add(key)
                continue
        out.append(line)
    for key, value in kv.items():
        if key not in seen:
            out.append(f"{key}={value}")
    path.write_text("\n".join(out) + "\n", encoding="utf-8")


class PlaygroundWatcher:
    def __init__(self, *, interval_s: float = 45.0) -> None:
        self.interval_s = max(15.0, float(interval_s))
        self._last_poll = 0.0

    def poll(self, client: Any, current_id: str, *, force: bool = False) -> Optional[dict]:
        now = time.time()
        if not force and (now - self._last_poll) < self.interval_s:
            return None
        self._last_poll = now
        hit = discover_active_playground(client)
        if not hit:
            return None
        if hit["id"] == current_id:
            return None
        return hit
