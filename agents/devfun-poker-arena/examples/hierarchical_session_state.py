"""K161 hierarchical session state — capped short/mid-term memory for lobby decide.

Ensemble QSP (2607.07666) pattern: O(1) slice for decide/HL; never dump full
Arena trajectories. Villain exploit path stays in session_memory.py.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

_REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_HIERARCHICAL_MEMORY_PATH = _REPO_ROOT / "config" / "hu_hierarchical_memory.json"

_FORBIDDEN_SLICE_KEYS = frozenset(
    {
        "reasoning",
        "action_history",
        "actions",
        "trajectory",
        "trajectories",
        "raw_trajectory",
        "full_log",
    }
)


def load_hierarchical_memory_config(path: str | Path | None = None) -> dict[str, Any]:
    cfg_path = Path(path) if path else DEFAULT_HIERARCHICAL_MEMORY_PATH
    if not cfg_path.is_file():
        raise FileNotFoundError(f"hierarchical memory config not found: {cfg_path}")
    data = json.loads(cfg_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("hierarchical memory config must be a JSON object")
    return data


def empty_state() -> dict[str, Any]:
    return {
        "short_term": {"hands": [], "scratchpad_facts": {}},
        "mid_term": {
            "active_goals": {},
            "session_summaries": [],
            "recent_jobs": {},
        },
    }


def reset_mid_term(state: dict[str, Any]) -> None:
    state["mid_term"] = {
        "active_goals": {},
        "session_summaries": [],
        "recent_jobs": {},
    }


def update_short_term(
    state: dict[str, Any],
    hand_summary: dict[str, Any],
    *,
    config: dict[str, Any] | str | Path | None = None,
) -> None:
    cfg = (
        load_hierarchical_memory_config(config)
        if config is None or isinstance(config, (str, Path))
        else config
    )
    max_hands = int((cfg.get("short_term") or {}).get("max_hands", 8))
    compact = {
        "hand_id": hand_summary.get("hand_id") or hand_summary.get("tableId"),
        "chip_delta": hand_summary.get("chip_delta"),
        "action": hand_summary.get("action"),
        "position": hand_summary.get("position"),
    }
    hands = state.setdefault("short_term", {}).setdefault("hands", [])
    hands.append(compact)
    while len(hands) > max_hands:
        hands.pop(0)


def update_scratchpad_facts(
    state: dict[str, Any],
    facts: dict[str, Any],
    *,
    config: dict[str, Any] | str | Path | None = None,
) -> None:
    cfg = (
        load_hierarchical_memory_config(config)
        if config is None or isinstance(config, (str, Path))
        else config
    )
    max_facts = int((cfg.get("short_term") or {}).get("max_scratchpad_facts", 12))
    pad = state.setdefault("short_term", {}).setdefault("scratchpad_facts", {})
    for key, val in facts.items():
        if key in _FORBIDDEN_SLICE_KEYS:
            continue
        pad[str(key)] = val
    # Cap by insertion order of keys
    while len(pad) > max_facts:
        oldest = next(iter(pad))
        pad.pop(oldest, None)


def append_session_summary(
    state: dict[str, Any],
    summary: str,
    *,
    config: dict[str, Any] | str | Path | None = None,
) -> None:
    cfg = (
        load_hierarchical_memory_config(config)
        if config is None or isinstance(config, (str, Path))
        else config
    )
    max_sum = int((cfg.get("mid_term") or {}).get("max_session_summaries", 3))
    summaries = state.setdefault("mid_term", {}).setdefault("session_summaries", [])
    text = str(summary).strip()
    if not text:
        return
    summaries.append(text[:400])
    while len(summaries) > max_sum:
        summaries.pop(0)


def upsert_active_goal(
    state: dict[str, Any],
    goal_id: str,
    goal: dict[str, Any],
    *,
    config: dict[str, Any] | str | Path | None = None,
) -> None:
    cfg = (
        load_hierarchical_memory_config(config)
        if config is None or isinstance(config, (str, Path))
        else config
    )
    max_goals = int((cfg.get("mid_term") or {}).get("max_active_goals", 5))
    goals = state.setdefault("mid_term", {}).setdefault("active_goals", {})
    goals[str(goal_id)] = dict(goal)
    while len(goals) > max_goals:
        oldest = next(iter(goals))
        goals.pop(oldest, None)


def upsert_recent_job(
    state: dict[str, Any],
    job_id: str,
    job: dict[str, Any],
    *,
    config: dict[str, Any] | str | Path | None = None,
) -> None:
    cfg = (
        load_hierarchical_memory_config(config)
        if config is None or isinstance(config, (str, Path))
        else config
    )
    max_jobs = int((cfg.get("mid_term") or {}).get("max_recent_jobs", 6))
    jobs = state.setdefault("mid_term", {}).setdefault("recent_jobs", {})
    jobs[str(job_id)] = dict(job)
    while len(jobs) > max_jobs:
        oldest = next(iter(jobs))
        jobs.pop(oldest, None)


def evict_completed(
    state: dict[str, Any],
    *,
    config: dict[str, Any] | str | Path | None = None,
) -> list[str]:
    cfg = (
        load_hierarchical_memory_config(config)
        if config is None or isinstance(config, (str, Path))
        else config
    )
    if not (cfg.get("mid_term") or {}).get("evict_completed_drills", True):
        return []
    removed: list[str] = []
    mid = state.setdefault("mid_term", {})
    for bucket_name in ("active_goals", "recent_jobs"):
        bucket = mid.setdefault(bucket_name, {})
        for key in list(bucket.keys()):
            status = str((bucket.get(key) or {}).get("status") or "").lower()
            if status == "completed":
                bucket.pop(key, None)
                removed.append(f"{bucket_name}:{key}")
    return removed


def estimate_slice_chars(slice_dict: dict[str, Any]) -> int:
    return len(json.dumps(slice_dict, sort_keys=True, default=str))


def build_memory_slice_for_decide(
    state: dict[str, Any],
    *,
    config: dict[str, Any] | str | Path | None = None,
) -> dict[str, Any]:
    cfg = (
        load_hierarchical_memory_config(config)
        if config is None or isinstance(config, (str, Path))
        else config
    )
    max_chars = int(cfg.get("slice_max_chars", 1200))
    short = state.get("short_term") or {}
    mid = state.get("mid_term") or {}
    facts = {
        k: v
        for k, v in (short.get("scratchpad_facts") or {}).items()
        if k not in _FORBIDDEN_SLICE_KEYS
    }
    slice_dict: dict[str, Any] = {
        "short_term": {
            "hands": list(short.get("hands") or []),
            "scratchpad_facts": facts,
        },
        "mid_term": {
            "active_goals": dict(mid.get("active_goals") or {}),
            "session_summaries": list(mid.get("session_summaries") or []),
            "recent_jobs": dict(mid.get("recent_jobs") or {}),
        },
        "long_term_refs": list(cfg.get("long_term_refs") or []),
    }
    # Trim oldest short-term hands until under budget
    while estimate_slice_chars(slice_dict) > max_chars and slice_dict["short_term"]["hands"]:
        slice_dict["short_term"]["hands"].pop(0)
    while (
        estimate_slice_chars(slice_dict) > max_chars
        and slice_dict["mid_term"]["session_summaries"]
    ):
        slice_dict["mid_term"]["session_summaries"].pop(0)
    return slice_dict


def compute_hierarchical_memory_advisory(
    slice_dict: dict[str, Any],
    *,
    config: dict[str, Any] | str | Path | None = None,
) -> dict[str, Any]:
    cfg = (
        load_hierarchical_memory_config(config)
        if config is None or isinstance(config, (str, Path))
        else config
    )
    chars = estimate_slice_chars(slice_dict)
    max_chars = int(cfg.get("slice_max_chars", 1200))
    return {
        "schema": "devfun.hierarchical_memory_advisory.v1",
        "advisory_only": True,
        "slice_chars": chars,
        "slice_max_chars": max_chars,
        "within_budget": chars <= max_chars,
        "n_short_hands": len((slice_dict.get("short_term") or {}).get("hands") or []),
        "n_session_summaries": len(
            (slice_dict.get("mid_term") or {}).get("session_summaries") or []
        ),
        "reference": "references/hierarchical-session-memory.md",
    }


def attach_hierarchical_slice(
    research_context: dict[str, Any],
    state: dict[str, Any],
    *,
    config: dict[str, Any] | str | Path | None = None,
) -> dict[str, Any]:
    """Inject bounded memory slice into research_context (lobby decide path)."""
    hier = state.setdefault("hierarchical_session", empty_state())
    slice_dict = build_memory_slice_for_decide(hier, config=config)
    research_context["hierarchical_memory_slice"] = slice_dict
    return slice_dict
