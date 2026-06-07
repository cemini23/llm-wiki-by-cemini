"""Playground qualification + lead protection — tighten decide() when safely ahead."""
from __future__ import annotations

import os
from typing import Any

DEFAULT_CUTOFF_RANK = 20
DEFAULT_BUFFER_CHIPS = 1000  # chips above rank-20 floor before protect mode
DEFAULT_LEAD_RANK = 5
DEFAULT_LEAD_BUFFER_CHIPS = 3000  # extra cushion before lead-protect tier
DEFAULT_FIRST_RANK = 1  # rank #1 with lead buffer → slowest join pace

# Lock/playable math uses ratios vs qual_floor and total — no absolute chip ladders.
_DEFAULT_FIRST_LOCK_SURPLUS_PCT = 0.80
_DEFAULT_FIRST_MAX_PLAYABLE_FRAC = 0.28


def _safe_int(raw: str | None, default: int) -> int:
    if raw is None or raw.strip() == "":
        return default
    try:
        return int(raw)
    except ValueError:
        return default


def _safe_float(raw: str | None, default: float) -> float:
    if raw is None or raw.strip() == "":
        return default
    try:
        return float(raw)
    except ValueError:
        return default


_PLAYABLE_FRAC_BY_TIER: dict[str, float] = {
    "marginal_top20": 0.42,
    "comfort_top20": 0.35,
    "strong_top20": 0.30,
    "top10": 0.26,
    "top5": 0.22,
    "dominant": 0.32,
}


def _buffer_threshold() -> int:
    return _safe_int(os.environ.get("CEMINI_QUAL_BUFFER_CHIPS"), DEFAULT_BUFFER_CHIPS)


def _lead_buffer_threshold() -> int:
    return _safe_int(os.environ.get("CEMINI_LEAD_BUFFER_CHIPS"), DEFAULT_LEAD_BUFFER_CHIPS)


def _lead_rank_threshold() -> int:
    return _safe_int(os.environ.get("CEMINI_LEAD_RANK"), DEFAULT_LEAD_RANK)


def _first_rank_threshold() -> int:
    return _safe_int(os.environ.get("CEMINI_FIRST_RANK"), DEFAULT_FIRST_RANK)


def _legacy_flat_reserve() -> int:
    """Optional prod-only override (CEMINI_CHIP_RESERVE). Not set in repo deploy."""
    return max(0, _safe_int(os.environ.get("CEMINI_CHIP_RESERVE"), 0))


def _stagger_locks_enabled() -> bool:
    raw = os.environ.get("CEMINI_STAGGER_LOCKS", "1").strip().lower()
    return raw not in ("0", "false", "no", "off")


def _first_lock_surplus_pct() -> float:
    return _safe_float(os.environ.get("CEMINI_FIRST_LOCK_SURPLUS_PCT"), _DEFAULT_FIRST_LOCK_SURPLUS_PCT)


def _first_max_playable_frac() -> float:
    return _safe_float(os.environ.get("CEMINI_FIRST_MAX_PLAYABLE_FRAC"), _DEFAULT_FIRST_MAX_PLAYABLE_FRAC)


def _tier_from_buffer_ratio(buffer: int, qual_floor: int) -> tuple[str, float]:
    """Map cushion above cutoff to lock tier using buffer / qual_floor (tournament-agnostic)."""
    ratio = buffer / max(int(qual_floor), 1)
    if ratio < 0.12:
        return "marginal_top20", 0.08
    if ratio < 0.25:
        return "comfort_top20", 0.18
    if ratio < 0.50:
        return "strong_top20", 0.32
    if ratio < 1.0:
        return "top10", 0.48
    if ratio < 2.5:
        return "top5", 0.62
    return "dominant", 0.72


def _playable_frac(tier: str, *, first_protect: bool) -> float:
    frac = _PLAYABLE_FRAC_BY_TIER.get(tier, 0.30)
    if first_protect:
        return min(frac, _first_max_playable_frac())
    return frac


def staggered_chip_lock(
    total_chips: int,
    cutoff_chips: int,
    *,
    qual_buffer: int | None = None,
    qualification_protect: bool = False,
    lead_protect: bool = False,
    first_protect: bool = False,
) -> dict[str, Any]:
    """Compute locked vs playable bankroll to preserve top-20 qualification.

    Always locks at least ``cutoff + qual_buffer`` (top-20 floor + safety margin).
    Above that, locks a fraction of surplus chips and caps playable as a fraction of
    total stack — all ratios, no hard-coded chip milestones.
    """
    if qual_buffer is None:
        qual_buffer = _buffer_threshold()

    qual_floor = int(cutoff_chips) + int(qual_buffer)
    out: dict[str, Any] = {
        "qual_floor_chips": qual_floor,
        "locked_chips": 0,
        "playable_chips": max(0, int(total_chips)),
        "lock_tier": "off",
        "chip_reserve": 0,
        "max_playable_chips": None,
    }

    if not _stagger_locks_enabled():
        flat = _legacy_flat_reserve()
        if flat > 0 and first_protect:
            locked = min(flat, int(total_chips))
            out.update(
                locked_chips=locked,
                playable_chips=max(0, int(total_chips) - locked),
                lock_tier="flat_reserve",
                chip_reserve=locked,
                max_playable_chips=max(0, int(total_chips) - locked),
            )
        return out

    if not qualification_protect and not lead_protect:
        return out

    total = int(total_chips)
    buffer = total - int(cutoff_chips)
    tier, surplus_pct = _tier_from_buffer_ratio(buffer, qual_floor)
    if first_protect:
        surplus_pct = max(surplus_pct, _first_lock_surplus_pct())

    surplus = max(0, total - qual_floor)
    locked_from_pct = qual_floor + int(surplus * surplus_pct)
    playable_frac = _playable_frac(tier, first_protect=first_protect)
    locked_from_cap = total - int(total * playable_frac)
    locked = max(locked_from_pct, locked_from_cap, qual_floor)

    flat_min = _legacy_flat_reserve()
    if first_protect and flat_min > 0:
        locked = max(locked, min(flat_min, total))

    playable = max(0, total - locked)

    out.update(
        locked_chips=locked,
        playable_chips=playable,
        lock_tier=tier,
        chip_reserve=locked,
        max_playable_chips=playable,
    )
    return out


def max_playable_chips(
    total_chips: int | None,
    *,
    cutoff_chips: int | None = None,
    qualification_protect: bool = False,
    lead_protect: bool = False,
    first_protect: bool = False,
) -> int | None:
    """Back-compat wrapper — prefer ``staggered_chip_lock()``."""
    if total_chips is None or cutoff_chips is None:
        return None
    if not (qualification_protect or lead_protect or first_protect):
        return None
    st = staggered_chip_lock(
        int(total_chips),
        int(cutoff_chips),
        qualification_protect=qualification_protect,
        lead_protect=lead_protect,
        first_protect=first_protect,
    )
    return st.get("max_playable_chips")


def fetch_qualification_status(
    client: Any,
    competition_id: str,
    *,
    cutoff_rank: int = DEFAULT_CUTOFF_RANK,
    buffer_chips: int | None = None,
    lead_rank: int | None = None,
    lead_buffer_chips: int | None = None,
) -> dict[str, Any]:
    """Return rank/chips and protection flags for decide().

    qualification_protect: rank <= cutoff_rank AND chips >= floor + buffer_chips
    lead_protect: rank <= lead_rank AND chips >= floor + lead_buffer_chips
    """
    if buffer_chips is None:
        buffer_chips = _buffer_threshold()
    if lead_rank is None:
        lead_rank = _lead_rank_threshold()
    if lead_buffer_chips is None:
        lead_buffer_chips = _lead_buffer_threshold()

    out: dict[str, Any] = {
        "qualification_protect": False,
        "lead_protect": False,
        "first_protect": False,
        "rank": None,
        "chips": None,
        "cutoff_chips": None,
        "buffer_chips": 0,
        "qual_floor_chips": None,
        "chip_reserve": 0,
        "locked_chips": 0,
        "max_playable_chips": None,
        "lock_tier": "off",
    }
    try:
        me = client.get("/agent/me")
    except Exception:
        return out

    row = next(
        (r for r in (me.get("leaderboard") or []) if r.get("arenaId") == competition_id),
        None,
    )
    if not row:
        return out

    rank = row.get("rank")
    chips = row.get("totalScore")
    out["rank"] = rank
    out["chips"] = chips

    try:
        lb = client.get(
            f"/competition/leaderboard?competitionId={competition_id}"
            f"&limit=1&offset={max(cutoff_rank - 1, 0)}"
        )
        cutoff_rows = lb.get("data") or []
        cutoff_chips = cutoff_rows[0].get("totalScore") if cutoff_rows else None
    except Exception:
        cutoff_chips = None

    out["cutoff_chips"] = cutoff_chips
    if rank is None or chips is None or cutoff_chips is None:
        return out

    buffer = int(chips) - int(cutoff_chips)
    out["buffer_chips"] = buffer
    if buffer >= buffer_chips and int(rank) <= cutoff_rank:
        out["qualification_protect"] = True
    if buffer >= lead_buffer_chips and int(rank) <= lead_rank:
        out["lead_protect"] = True
    if out["lead_protect"] and int(rank) <= _first_rank_threshold():
        out["first_protect"] = True

    if out["qualification_protect"] or out["lead_protect"]:
        lock = staggered_chip_lock(
            int(chips),
            int(cutoff_chips),
            qual_buffer=buffer_chips,
            qualification_protect=bool(out["qualification_protect"]),
            lead_protect=bool(out["lead_protect"]),
            first_protect=bool(out["first_protect"]),
        )
        out.update(lock)

    return out
