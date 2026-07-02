"""Finale human-seat config — separate from ladder grind (see human-table exploit brief).

Gated by CEMINI_FINALE_EXPLOIT=1 and CEMINI_FINALE_VILLAIN=durrrr|jungleman.
Never enable on the default sandbox ladder bundle.
"""
from __future__ import annotations

import os
from typing import Literal

FinaleVillain = Literal["durrrr", "jungleman", "none"]

_VALID: frozenset[str] = frozenset({"durrrr", "jungleman"})
_ALIASES = {
    "dwan": "durrrr",
    "tom_dwan": "durrrr",
    "durrr": "durrrr",
    "cates": "jungleman",
    "daniel_cates": "jungleman",
    "jungle": "jungleman",
}


def _env_on(key: str, default: str = "0") -> bool:
    return os.environ.get(key, default).strip().lower() in ("1", "true", "yes", "on")


def finale_exploit_enabled() -> bool:
    return _env_on("CEMINI_FINALE_EXPLOIT")


def finale_villain() -> FinaleVillain:
    if not finale_exploit_enabled():
        return "none"
    raw = (os.environ.get("CEMINI_FINALE_VILLAIN") or "").strip().lower()
    if not raw:
        return "none"
    raw = _ALIASES.get(raw, raw)
    if raw in _VALID:
        return raw  # type: ignore[return-value]
    return "none"


def should_disable_ladder_exploits() -> bool:
    """Finale bundle contract — prefer env off; this is a runtime guard."""
    return finale_villain() != "none"


def resolve_finale_villain_from_context(
    *,
    table: dict | None = None,
    session: dict | None = None,
) -> FinaleVillain:
    """Env wins; optional table/session villain_id for live human seats."""
    env_v = finale_villain()
    if env_v != "none":
        return env_v
    if not finale_exploit_enabled():
        return "none"
    for src in (session or {}, (table or {}).get("session") or {}, table or {}):
        vid = src.get("villain_id") or src.get("finaleVillain") or src.get("finale_villain")
        if not vid:
            continue
        key = _ALIASES.get(str(vid).strip().lower(), str(vid).strip().lower())
        if key in _VALID:
            return key  # type: ignore[return-value]
    return "none"


def overlay_finale_hud(hud: dict, ctx: dict | None,
                        table: dict | None = None) -> dict:
    """Stamp finale villain on HUD; do not treat pro ids as arena nemesis handles."""
    out = dict(hud)
    session = ctx.get("session") if isinstance(ctx.get("session"), dict) else {}
    vid = resolve_finale_villain_from_context(table=table, session=session)
    if vid == "none":
        return out
    out["finale_villain"] = vid
    out["villain_id"] = vid
    if vid == "durrrr":
        out.setdefault("archetype", "linear_aggro")
        out["mode"] = "maniac"
    elif vid == "jungleman":
        out.setdefault("archetype", "wide_passive")
        out["mode"] = "lag"
    return out
