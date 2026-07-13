#!/usr/bin/env python3
"""Multi-axis proxy summary for Researcher Round trajectory exports.

Reads selfplay trajectory JSONL or Arena export bundles and writes
axis_summary.json for Discord / researcher contribution narrative.

Usage:
    uv run python examples/researcher_trajectory_summary.py \\
        --selfplay reports/researcher-round/.../selfplay_trajectory.jsonl
    uv run python examples/researcher_trajectory_summary.py \\
        --export-dir reports/exports/<compId>/<ts> --gate
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean
from typing import Any

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

# Raeth M₁–M₉ proxies (K122) — deterministic axes for submit gates.
_CARD_TOKEN_RE = re.compile(r"(?<![A-Za-z0-9])([2-9TJQKA][hdcs])(?![A-Za-z0-9])", re.I)
_VPIP_ACTIONS = frozenset({"call", "bet", "raise", "all-in"})

DEFAULT_GATE_THRESHOLDS: dict[str, float] = {
    "M8_hallucination_rate_max": 0.05,
    "M8_hole_leak_rate_max": 0.02,
    "M9_btn_minus_utg_vpip_min": -0.20,
    "hero_submissions_min": 1.0,
}

# FootsiesGym K151 — skill ≠ exploitability advisory (not a submit gate).
DEFAULT_EXPLOITABILITY_ADVISORY: dict[str, float] = {
    "skill_bb100_ok_min": 0.0,
    "yardstick_bb100_warn_max": -20.0,
    "skill_hand_wr_ok_min": 0.45,
}

DEFAULT_FORGETTING_DECAY = 0.95
DEFAULT_BIG_BLIND = 2
DEFAULT_DRIFT_BB_THRESHOLD = 3.0

_REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_YARDSTICK_POOL_PATH = _REPO_ROOT / "config" / "hu_yardstick_pool.json"
DEFAULT_STYLE_PRESERVATION_PATH = _REPO_ROOT / "config" / "hu_style_preservation.json"
DEFAULT_HIERARCHICAL_MEMORY_PATH = _REPO_ROOT / "config" / "hu_hierarchical_memory.json"
DEFAULT_DEEPSEARCH_FILTER_PATH = _REPO_ROOT / "config" / "hu_deepsearch_trajectory_filter.json"

_ACTION_BUCKETS = ("fold", "check", "call", "raise")

_PREFLOP_POSITION_ORDER = ("UTG", "MP", "CO", "BTN", "SB", "BB")


def _load_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    if not path.is_file():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return rows


def _vpip_rate(preflop_rows: list[dict]) -> float:
    if not preflop_rows:
        return 0.0
    vol = sum(
        1 for d in preflop_rows
        if str(d.get("action") or "").lower() in _VPIP_ACTIONS
    )
    return vol / len(preflop_rows)


def _entropy(counts: Counter) -> float:
    total = sum(counts.values())
    if total <= 0:
        return 0.0
    ent = 0.0
    for c in counts.values():
        p = c / total
        if p > 0:
            ent -= p * math.log2(p)
    return ent


def _cards_in_text(text: str) -> set[str]:
    return {m.group(1).lower() for m in _CARD_TOKEN_RE.finditer(text or "")}


def _allowed_cards(hole_key: str, board: list[str] | None = None) -> set[str]:
    allowed: set[str] = set()
    if hole_key:
        # hole_key is concatenated e.g. AsKd — split into 2-char tokens.
        hk = hole_key.replace(" ", "")
        for i in range(0, len(hk), 2):
            chunk = hk[i:i + 2]
            if len(chunk) == 2:
                allowed.add(chunk.lower())
    for c in board or []:
        s = str(c).strip()
        if len(s) >= 2:
            allowed.add(s[:2].lower() if len(s) == 2 else s.lower())
    return allowed


def compute_memory_gap(decisions: list[dict]) -> dict:
    """Compute memory-gap statistics for trajectory analysis.

    Heuristic:
    - bound_veto_memory_off: veto applied when session_memory_on is False
    - misdecide_memory_on: veto applied when session_memory_on is True OR
      high hallucination rate when memory is off

    Returns dict with counts:
    - bound_veto_total: total vetoes
    - bound_veto_memory_off: vetoes when memory was off
    - misdecide_memory_on: mis-decisions (veto when memory on)
    """
    if not decisions:
        return {
            "bound_veto_total": 0,
            "bound_veto_memory_off": 0,
            "misdecide_memory_on": 0,
        }

    bound_veto_total = 0
    bound_veto_memory_off = 0
    misdecide_memory_on = 0

    for d in decisions:
        veto = bool(d.get("trajectory_bound_veto"))
        memory_on = d.get("session_memory_on")
        # Handle None case - default to True if telemetry missing
        if memory_on is None:
            continue

        if veto:
            bound_veto_total += 1
            if not memory_on:
                bound_veto_memory_off += 1
            else:
                misdecide_memory_on += 1

    return {
        "bound_veto_total": bound_veto_total,
        "bound_veto_memory_off": bound_veto_memory_off,
        "misdecide_memory_on": misdecide_memory_on,
    }


def compute_selfplay_axes(decisions: list[dict], results: list[dict]) -> dict[str, Any]:
    """Deterministic Raeth proxies on hero trajectory rows."""
    if not decisions:
        return {}

    preflop = [d for d in decisions if d.get("street") == "Preflop"]
    by_pos: dict[str, list[dict]] = defaultdict(list)
    for d in preflop:
        by_pos[str(d.get("position") or "?")].append(d)

    # M₉ — positional VPIP spread (6-max: BTN vs UTG; HU: BTN vs BB).
    vpip_by_pos = {pos: round(_vpip_rate(rows), 4) for pos, rows in by_pos.items()}
    btn_vpip = vpip_by_pos.get("BTN", 0.0)
    utg_vpip = vpip_by_pos.get("UTG", 0.0)
    bb_vpip = vpip_by_pos.get("BB", 0.0)
    if "UTG" in vpip_by_pos:
        m9_gap = round(btn_vpip - utg_vpip, 4)
        m9_gap_label = "btn_minus_utg"
    else:
        m9_gap = round(btn_vpip - bb_vpip, 4)
        m9_gap_label = "btn_minus_bb"

    # M₁ — bet-size bucket histogram on aggressive actions.
    bet_buckets = Counter(
        str(d.get("bet_size_bucket") or "none")
        for d in decisions
        if str(d.get("action") or "").lower() in ("bet", "raise", "all-in")
    )
    m1_total = sum(bet_buckets.values()) or 1
    m1_hist = {k: round(v / m1_total, 4) for k, v in bet_buckets.items()}

    # M₇ — mean action entropy per (street, position).
    mix_buckets: dict[str, Counter] = defaultdict(Counter)
    for d in decisions:
        key = f"{d.get('street')}|{d.get('position')}"
        mix_buckets[key][str(d.get("action") or "").lower()] += 1
    entropies = [_entropy(c) for c in mix_buckets.values() if sum(c.values()) >= 3]
    m7_mean_entropy = round(mean(entropies), 4) if entropies else 0.0

    # M₄ — VPIP delta in 7-hand windows after bad-beat hands (chip_delta < 0).
    bad_hand_ids = {
        int(r.get("hand_id"))
        for r in results
        if r.get("chip_delta") is not None and int(r.get("chip_delta")) < 0
    }
    session_vpip = _vpip_rate(preflop)
    post_bad: list[dict] = []
    for d in preflop:
        hid = d.get("hand_id")
        if hid is not None and int(hid) in bad_hand_ids:
            post_bad.append(d)
    post_bad_vpip = _vpip_rate(post_bad[:7 * max(len(bad_hand_ids), 1)])
    m4_vpip_delta = round(post_bad_vpip - session_vpip, 4)

    # M₈ — factual: hallucinated cards + hole-card leaks in reasoning YAML.
    hallucination_n = 0
    hole_leak_n = 0
    checked_n = 0
    for d in decisions:
        reasoning = str(d.get("reasoning") or "")
        if not reasoning:
            continue
        checked_n += 1
        hole_key = str(d.get("hole_key") or "")
        allowed = _allowed_cards(hole_key)
        found = _cards_in_text(reasoning)
        if hole_key:
            hk = hole_key.replace(" ", "").lower()
            if hk and hk in reasoning.lower().replace(" ", ""):
                hole_leak_n += 1
        extra = found - allowed
        if extra:
            hallucination_n += 1

    m8_hallucination_rate = round(hallucination_n / max(checked_n, 1), 4)
    m8_hole_leak_rate = round(hole_leak_n / max(checked_n, 1), 4)

    return {
        "M1_bet_size_histogram": m1_hist,
        "M4_vpip_delta_post_bad_beat": m4_vpip_delta,
        "M7_mean_action_entropy": m7_mean_entropy,
        "M8_hallucination_rate": m8_hallucination_rate,
        "M8_hole_leak_rate": m8_hole_leak_rate,
        "M8_checked_decisions": checked_n,
        "M9_vpip_by_position": vpip_by_pos,
        "M9_positional_vpip_gap": m9_gap,
        "M9_positional_gap_label": m9_gap_label,
        "M9_btn_minus_utg_vpip": m9_gap,
    }


def load_yardstick_pool_config(path: str | Path | None = None) -> dict[str, Any]:
    """Load frozen HU yardstick pool spec (K152)."""
    pool_path = Path(path) if path else DEFAULT_YARDSTICK_POOL_PATH
    if not pool_path.is_file():
        raise FileNotFoundError(f"yardstick pool config not found: {pool_path}")
    data = json.loads(pool_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("yardstick pool config must be a JSON object")
    return data


def compute_yardstick_pool_grade(
    opponent_bb100: dict[str, float],
    pool_config: dict[str, Any] | str | Path | None = None,
) -> dict[str, Any]:
    """K152 advisory: % of frozen yardstick handles meeting min_bb100."""
    if pool_config is None or isinstance(pool_config, (str, Path)):
        cfg = load_yardstick_pool_config(pool_config)
    else:
        cfg = pool_config

    opponents = cfg.get("opponents") or {}
    per_handle: dict[str, Any] = {}
    passes = 0
    checked = 0

    for handle, spec in opponents.items():
        min_bb = float((spec or {}).get("min_bb100", 0))
        actual = opponent_bb100.get(handle)
        if actual is None:
            per_handle[handle] = {
                "min_bb100": min_bb,
                "actual_bb100": None,
                "pass": None,
                "missing": True,
            }
            continue
        checked += 1
        actual_f = float(actual)
        ok = actual_f >= min_bb
        if ok:
            passes += 1
        per_handle[handle] = {
            "min_bb100": min_bb,
            "actual_bb100": round(actual_f, 4),
            "pass": ok,
            "missing": False,
        }

    worst_handle = None
    worst_bb: float | None = None
    for handle, val in opponent_bb100.items():
        val_f = float(val)
        if worst_bb is None or val_f < worst_bb:
            worst_bb = val_f
            worst_handle = handle

    return {
        "schema": "devfun.yardstick_pool_grade.v1",
        "advisory_only": True,
        "pct_pass": round(passes / checked, 4) if checked else None,
        "n_checked": checked,
        "n_pass": passes,
        "per_handle": per_handle,
        "worst_handle": worst_handle,
        "worst_bb100": round(worst_bb, 4) if worst_bb is not None else None,
        "never_train": cfg.get("never_train"),
        "pool_schema": cfg.get("schema"),
        "reference": "references/expert-yardstick-pool.md",
    }


def compute_forgetting_factor_regret(
    chip_deltas: list[float],
    *,
    decay: float = DEFAULT_FORGETTING_DECAY,
    big_blind: int = DEFAULT_BIG_BLIND,
    drift_bb_threshold: float = DEFAULT_DRIFT_BB_THRESHOLD,
) -> dict[str, Any]:
    """K152 advisory: recency-weighted bb/100 vs lifetime mean (2607.07078)."""
    if not chip_deltas:
        return {
            "schema": "devfun.forgetting_factor_regret.v1",
            "advisory_only": True,
            "lifetime_mean_bb": None,
            "recency_weighted_mean_bb": None,
            "decay": decay,
            "n_hands": 0,
            "drift_flag": False,
            "reference": "references/expert-yardstick-pool.md",
        }

    bb_vals = [float(d) / big_blind for d in chip_deltas]
    n = len(bb_vals)
    lifetime_mean_bb = round(mean(bb_vals), 4)
    weights = [decay ** (n - 1 - i) for i in range(n)]
    w_sum = sum(weights)
    recency_weighted = sum(w * v for w, v in zip(weights, bb_vals)) / w_sum
    recency_weighted_mean_bb = round(recency_weighted, 4)
    drift_flag = (
        n >= 10
        and (lifetime_mean_bb - recency_weighted_mean_bb) > drift_bb_threshold
    )

    return {
        "schema": "devfun.forgetting_factor_regret.v1",
        "advisory_only": True,
        "lifetime_mean_bb": lifetime_mean_bb,
        "recency_weighted_mean_bb": recency_weighted_mean_bb,
        "decay": decay,
        "n_hands": n,
        "drift_flag": drift_flag,
        "reference": "references/expert-yardstick-pool.md",
    }


def load_style_preservation_config(path: str | Path | None = None) -> dict[str, Any]:
    """Load HU style-preservation spec (K153)."""
    cfg_path = Path(path) if path else DEFAULT_STYLE_PRESERVATION_PATH
    if not cfg_path.is_file():
        raise FileNotFoundError(f"style preservation config not found: {cfg_path}")
    data = json.loads(cfg_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("style preservation config must be a JSON object")
    return data


def _normalize_action_dist(dist: dict[str, float]) -> dict[str, float]:
    buckets = {b: 0.0 for b in _ACTION_BUCKETS}
    for key, val in dist.items():
        k = str(key).lower().strip()
        if k in buckets:
            buckets[k] += float(val)
    total = sum(buckets.values())
    if total <= 0:
        n = len(_ACTION_BUCKETS)
        return {b: 1.0 / n for b in _ACTION_BUCKETS}
    return {b: buckets[b] / total for b in _ACTION_BUCKETS}


def compute_d_policy_tv(
    seed_action_dist: dict[str, float],
    candidate_action_dist: dict[str, float],
) -> float:
    """Total-variation distance between action distributions (MPPO D_policy)."""
    seed = _normalize_action_dist(seed_action_dist)
    cand = _normalize_action_dist(candidate_action_dist)
    return round(0.5 * sum(abs(seed[b] - cand[b]) for b in _ACTION_BUCKETS), 6)


def compute_style_drift_d_policy(
    seed_action_dist: dict[str, float],
    candidate_action_dist: dict[str, float],
    *,
    config: dict[str, Any] | str | Path | None = None,
) -> dict[str, Any]:
    """K153 advisory: style drift vs seed demonstrator."""
    if config is None or isinstance(config, (str, Path)):
        cfg = load_style_preservation_config(config)
    else:
        cfg = config

    tv = compute_d_policy_tv(seed_action_dist, candidate_action_dist)
    max_tv = float(cfg.get("max_d_policy_tv_advisory", 0.25))
    style_ok = tv <= max_tv

    return {
        "schema": "devfun.style_drift_d_policy.v1",
        "advisory_only": True,
        "d_policy_tv": tv,
        "max_d_policy_tv_advisory": max_tv,
        "style_ok": style_ok,
        "beta_demo_mix": cfg.get("beta_demo_mix"),
        "d_policy_metric": cfg.get("d_policy_metric", "total_variation"),
        "seed_action_dist": _normalize_action_dist(seed_action_dist),
        "candidate_action_dist": _normalize_action_dist(candidate_action_dist),
        "reference": "references/mppo-style-preservation.md",
    }


def compute_league_promotion_rubric_advisory(
    *,
    yardstick_grade: dict[str, Any] | None = None,
    style_drift: dict[str, Any] | None = None,
    forgetting: dict[str, Any] | None = None,
    exploitability_advisory: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """K153+K160 advisory: yardstick vs style gaps for league promotion."""
    gaps: list[str] = []
    yardstick_gap = False
    style_gap = False
    forgetting_drift = False

    if yardstick_grade:
        pct = yardstick_grade.get("pct_pass")
        if pct is not None and float(pct) < 1.0:
            yardstick_gap = True
            gaps.append("yardstick_pool_incomplete")

    if style_drift:
        if style_drift.get("style_ok") is False:
            style_gap = True
            gaps.append("style_drift_exceeds_tv")

    if forgetting and forgetting.get("drift_flag"):
        forgetting_drift = True
        gaps.append("forgetting_regret_drift")

    footsiesgym_note = None
    if exploitability_advisory and exploitability_advisory.get("disconnect"):
        footsiesgym_note = (
            "FootsiesGym exploitability disconnect flagged — separate env; "
            "not an NLHE league promotion input"
        )

    return {
        "schema": "devfun.league_promotion_rubric.v1",
        "advisory_only": True,
        "yardstick_gap": yardstick_gap,
        "style_gap": style_gap,
        "forgetting_drift": forgetting_drift,
        "gaps": gaps,
        "footsiesgym_note": footsiesgym_note,
        "footsiesgym_env": "footsiesgym_separate",
        "yardstick_grade": yardstick_grade,
        "style_drift": style_drift,
        "forgetting_regret": forgetting,
        "reference": "references/league-promotion-rubric.md",
    }


def load_deepsearch_trajectory_filter_config(
    path: str | Path | None = None,
) -> dict[str, Any]:
    """Load DeepSearch generate→filter→mix advisory config (K161)."""
    cfg_path = Path(path) if path else DEFAULT_DEEPSEARCH_FILTER_PATH
    if not cfg_path.is_file():
        raise FileNotFoundError(f"deepsearch filter config not found: {cfg_path}")
    data = json.loads(cfg_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("deepsearch filter config must be a JSON object")
    return data


def build_failure_mining_units(rows: list[dict]) -> list[dict[str, Any]]:
    """Group loss hand_result rows into DeepSearch mining units."""
    units: list[dict[str, Any]] = []
    for i, row in enumerate(rows):
        if not isinstance(row, dict):
            continue
        kind = str(row.get("type") or row.get("event") or "").lower()
        chip = row.get("chip_delta")
        if chip is None:
            chip = row.get("hero_chip_delta")
        is_loss = False
        if chip is not None:
            try:
                is_loss = float(chip) < 0
            except (TypeError, ValueError):
                is_loss = False
        if not is_loss and kind not in ("hand_result", "hand", ""):
            continue
        if not is_loss and "hand_result" not in kind and row.get("result") != "loss":
            if chip is None:
                continue
            if not is_loss:
                continue
        if not is_loss:
            continue

        next_delta = None
        for j in range(i + 1, min(i + 6, len(rows))):
            nxt = rows[j]
            if not isinstance(nxt, dict):
                continue
            nd = nxt.get("chip_delta")
            if nd is None:
                nd = nxt.get("hero_chip_delta")
            if nd is not None:
                try:
                    next_delta = float(nd)
                    break
                except (TypeError, ValueError):
                    pass

        prior_veto = None
        post_veto = row.get("trajectory_bound_veto")
        prior_action = None
        post_action = row.get("action")
        for j in range(i - 1, max(-1, i - 6), -1):
            prev = rows[j]
            if not isinstance(prev, dict):
                continue
            if prior_veto is None and "trajectory_bound_veto" in prev:
                prior_veto = prev.get("trajectory_bound_veto")
            if prior_action is None and prev.get("action"):
                prior_action = prev.get("action")
            if prior_veto is not None and prior_action is not None:
                break

        units.append(
            {
                "hand_id": row.get("hand_id") or row.get("tableId") or f"loss-{i}",
                "chip_delta": float(chip) if chip is not None else None,
                "hole_key": row.get("hole_key") or row.get("hole"),
                "board": row.get("board") or [],
                "reasoning": row.get("reasoning") or row.get("reflection") or "",
                "verified": row.get("verified"),
                "teacher_imitation_only": bool(row.get("teacher_imitation_only")),
                "ungrounded_reflection": bool(row.get("ungrounded_reflection")),
                "next_hand_chip_delta": next_delta,
                "tags": row.get("tags") if isinstance(row.get("tags"), dict) else {},
                "post_loss_action_changed": (
                    prior_action is not None
                    and post_action is not None
                    and str(prior_action).lower() != str(post_action).lower()
                ),
                "trajectory_bound_veto_flipped": (
                    prior_veto is not None
                    and post_veto is not None
                    and bool(prior_veto) != bool(post_veto)
                ),
            }
        )
    return units


def infer_mining_tags(unit: dict[str, Any]) -> dict[str, bool]:
    """Infer DeepSearch filter tags; honor explicit tags when present."""
    explicit = unit.get("tags") if isinstance(unit.get("tags"), dict) else {}
    tags: dict[str, bool] = {}

    if "progress_verification" in explicit:
        tags["progress_verification"] = bool(explicit["progress_verification"])
    else:
        tags["progress_verification"] = bool(unit.get("verified")) or (
            unit.get("next_hand_chip_delta") is not None
            and float(unit["next_hand_chip_delta"]) > 0
        )

    if "grounded_reflection" in explicit:
        tags["grounded_reflection"] = bool(explicit["grounded_reflection"])
    else:
        text = str(unit.get("reasoning") or "").lower()
        hole = str(unit.get("hole_key") or "").replace(" ", "")
        allowed: set[str] = set()
        for i in range(0, len(hole), 2):
            chunk = hole[i : i + 2]
            if len(chunk) == 2:
                allowed.add(chunk.lower())
        for c in unit.get("board") or []:
            s = str(c).strip()
            if len(s) >= 2:
                allowed.add(s[:2].lower())
        cited = {m.lower() for m in _CARD_TOKEN_RE.findall(text)}
        # Also accept concatenated hole_key substring in reflection text
        grounded = bool(allowed) and (
            bool(cited & allowed) or any(tok in text for tok in allowed)
        )
        tags["grounded_reflection"] = grounded and not bool(
            unit.get("ungrounded_reflection")
        )

    if "failure_recovery" in explicit:
        tags["failure_recovery"] = bool(explicit["failure_recovery"])
    else:
        tags["failure_recovery"] = bool(unit.get("post_loss_action_changed")) or bool(
            unit.get("trajectory_bound_veto_flipped")
        )

    if "teacher_imitation_only" in explicit:
        tags["teacher_imitation_only"] = bool(explicit["teacher_imitation_only"])
    else:
        tags["teacher_imitation_only"] = bool(unit.get("teacher_imitation_only"))

    return tags


def filter_deepsearch_units(
    units: list[dict[str, Any]],
    *,
    config: dict[str, Any] | str | Path | None = None,
) -> dict[str, Any]:
    cfg = (
        load_deepsearch_trajectory_filter_config(config)
        if config is None or isinstance(config, (str, Path))
        else config
    )
    required = list(cfg.get("required_tags") or [])
    eligible: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    reasons: dict[str, int] = {}

    for unit in units:
        tags = infer_mining_tags(unit)
        reason = None
        if tags.get("teacher_imitation_only"):
            reason = "teacher_imitation_only"
        elif unit.get("ungrounded_reflection") or tags.get("grounded_reflection") is False:
            if not tags.get("grounded_reflection"):
                reason = "ungrounded_reflection"
        if reason is None:
            missing = [t for t in required if not tags.get(t)]
            if missing:
                reason = "missing_required_tags"

        record = {
            "hand_id": unit.get("hand_id"),
            "tags": tags,
            "reason": reason,
        }
        if reason:
            rejected.append(record)
            reasons[reason] = reasons.get(reason, 0) + 1
        else:
            eligible.append(record)

    return {
        "eligible": eligible,
        "rejected": rejected,
        "reasons": reasons,
        "n_units": len(units),
        "n_eligible": len(eligible),
        "n_rejected": len(rejected),
    }


def compute_deepsearch_trajectory_filter_advisory(
    rows_or_units: list[dict[str, Any]],
    *,
    config: dict[str, Any] | str | Path | None = None,
    units_prebuilt: bool = False,
) -> dict[str, Any]:
    """K161 advisory: generate→filter→mix eligibility for failure mining."""
    cfg = (
        load_deepsearch_trajectory_filter_config(config)
        if config is None or isinstance(config, (str, Path))
        else config
    )
    units = rows_or_units if units_prebuilt else build_failure_mining_units(rows_or_units)
    filtered = filter_deepsearch_units(units, config=cfg)
    n = filtered["n_units"]
    eligible_pct = round(filtered["n_eligible"] / n, 4) if n else None
    return {
        "schema": "devfun.deepsearch_trajectory_filter.v1",
        "advisory_only": True,
        "n_units": n,
        "n_eligible": filtered["n_eligible"],
        "n_rejected": filtered["n_rejected"],
        "eligible_pct": eligible_pct,
        "rejected_reasons": filtered["reasons"],
        "eligible_hand_ids": [u.get("hand_id") for u in filtered["eligible"]],
        "required_tags": list(cfg.get("required_tags") or []),
        "reference": "references/deepsearch-trajectory-filter.md",
    }


def compute_exploitability_advisory(
    *,
    skill_bb100: float | None = None,
    yardstick_bb100: float | None = None,
    opponent_bb100: dict[str, float] | None = None,
    skill_hand_win_rate: float | None = None,
    thresholds: dict[str, float] | None = None,
) -> dict[str, Any] | None:
    """FootsiesGym-style advisory: H2H skill can look fine while a yardstick crushes us.

    Advisory only — never appended to gate_failures. Returns None when no inputs.
    """
    thr = dict(DEFAULT_EXPLOITABILITY_ADVISORY)
    if thresholds:
        thr.update(thresholds)

    opp = {str(k): float(v) for k, v in (opponent_bb100 or {}).items()}
    yardstick_handle = None
    if opp:
        yardstick_handle, yard_from_opp = min(opp.items(), key=lambda kv: kv[1])
        if yardstick_bb100 is None:
            yardstick_bb100 = yard_from_opp
        if skill_bb100 is None:
            skill_bb100 = round(mean(opp.values()), 4)

    if skill_bb100 is None and yardstick_bb100 is None and skill_hand_win_rate is None:
        return None

    skill_ok = False
    if skill_bb100 is not None and skill_bb100 >= thr["skill_bb100_ok_min"]:
        skill_ok = True
    if (
        skill_hand_win_rate is not None
        and skill_hand_win_rate >= thr["skill_hand_wr_ok_min"]
    ):
        skill_ok = True

    yardstick_bad = (
        yardstick_bb100 is not None
        and yardstick_bb100 < thr["yardstick_bb100_warn_max"]
    )
    disconnect = bool(skill_ok and yardstick_bad)

    note = (
        "skill_proxy looks OK but yardstick bb/100 is deeply negative "
        "(FootsiesGym EMAgnet pattern: H2H ≠ exploitability)"
        if disconnect
        else "no skill-vs-yardstick disconnect flagged"
    )
    out: dict[str, Any] = {
        "schema": "devfun.exploitability_advisory.v1",
        "advisory_only": True,
        "skill_bb100": skill_bb100,
        "yardstick_bb100": yardstick_bb100,
        "yardstick_handle": yardstick_handle,
        "skill_hand_win_rate": skill_hand_win_rate,
        "opponent_bb100": opp or None,
        "skill_ok": skill_ok,
        "yardstick_bad": yardstick_bad,
        "disconnect": disconnect,
        "note": note,
        "thresholds": thr,
        "reference": "references/footsiesgym-raeth-axis-map.md",
    }
    return out


def evaluate_gates(
    manifest: dict[str, Any],
    thresholds: dict[str, float] | None = None,
) -> list[str]:
    """Return human-readable gate failures (empty = pass)."""
    thr = dict(DEFAULT_GATE_THRESHOLDS)
    if thresholds:
        thr.update(thresholds)

    failures: list[str] = []
    selfplay = manifest.get("selfplay") or {}
    arena = manifest.get("arena") or {}
    axes = selfplay.get("axes") or {}

    if axes:
        hall = float(axes.get("M8_hallucination_rate") or 0)
        if hall > thr["M8_hallucination_rate_max"]:
            failures.append(
                f"M8 hallucination_rate {hall:.4f} > max {thr['M8_hallucination_rate_max']}"
            )
        leak = float(axes.get("M8_hole_leak_rate") or 0)
        if leak > thr["M8_hole_leak_rate_max"]:
            failures.append(
                f"M8 hole_leak_rate {leak:.4f} > max {thr['M8_hole_leak_rate_max']}"
            )
        gap = float(
            axes.get("M9_positional_vpip_gap") or axes.get("M9_btn_minus_utg_vpip") or 0
        )
        gap_label = str(axes.get("M9_positional_gap_label") or "btn_minus_utg").replace(
            "_", "-"
        )
        if gap < thr["M9_btn_minus_utg_vpip_min"]:
            failures.append(
                f"M9 {gap_label} vpip gap {gap:.4f} < min {thr['M9_btn_minus_utg_vpip_min']}"
            )

    if arena.get("source") == "arena_export":
        hero_subs = int(arena.get("hero_submissions") or 0)
        if hero_subs < int(thr["hero_submissions_min"]):
            failures.append(
                f"hero_submissions {hero_subs} < min {int(thr['hero_submissions_min'])}"
            )

    return failures


def summarize_selfplay_trajectory(
    rows: list[dict],
    *,
    forgetting_decay: float = DEFAULT_FORGETTING_DECAY,
) -> dict[str, Any]:
    decisions = [r for r in rows if r.get("record_type") == "decision"]
    results = [r for r in rows if r.get("record_type") == "hand_result"]
    if not decisions:
        return {"source": "selfplay", "decision_count": 0}

    actions = Counter(str(d.get("action") or "").lower() for d in decisions)
    buckets = Counter(str(d.get("bet_size_bucket") or "none") for d in decisions)
    by_pos: dict[str, list[dict]] = defaultdict(list)
    for d in decisions:
        by_pos[str(d.get("position") or "?")].append(d)

    preflop = [d for d in decisions if d.get("street") == "Preflop"]
    preflop_folds_by_pos: dict[str, float] = {}
    for pos, pos_rows in by_pos.items():
        pf = [d for d in pos_rows if d.get("street") == "Preflop"]
        if not pf:
            continue
        folds = sum(1 for d in pf if str(d.get("action")).lower() == "fold")
        preflop_folds_by_pos[pos] = round(folds / len(pf), 4)

    voluntary_preflop = sum(
        1 for d in preflop
        if str(d.get("action")).lower() in _VPIP_ACTIONS
    )
    vpip_proxy = round(voluntary_preflop / max(len(preflop), 1), 4)
    pfr_proxy = round(
        sum(1 for d in preflop if str(d.get("action")).lower() in ("bet", "raise"))
        / max(len(preflop), 1),
        4,
    )
    reasoning_lens = [int(d.get("reasoning_len") or 0) for d in decisions]

    net = sum(int(r.get("chip_delta") or 0) for r in results)
    hands = len(results) or len({d.get("hand_id") for d in decisions})
    axes = compute_selfplay_axes(decisions, results)
    memory_gap = compute_memory_gap(decisions)
    chip_deltas = [
        float(r.get("chip_delta"))
        for r in results
        if r.get("chip_delta") is not None
    ]
    forgetting_regret = compute_forgetting_factor_regret(
        chip_deltas,
        decay=forgetting_decay,
    )

    return {
        "source": "selfplay",
        "decision_count": len(decisions),
        "hands": hands,
        "net_chips": net,
        "action_counts": dict(actions),
        "bet_size_buckets": dict(buckets),
        "preflop_fold_rate_by_position": preflop_folds_by_pos,
        "vpip_proxy": vpip_proxy,
        "pfr_proxy": pfr_proxy,
        "reasoning_len_mean": round(mean(reasoning_lens), 1) if reasoning_lens else 0,
        "reasoning_len_max": max(reasoning_lens) if reasoning_lens else 0,
        "n_players_mode": Counter(
            int(d.get("n_players") or 0) for d in decisions
        ).most_common(1)[0][0] if decisions else None,
        "axes": axes,
        "memory_gap": memory_gap,
        "forgetting_regret": forgetting_regret,
    }


def summarize_arena_export(export_dir: Path, hero: str) -> dict[str, Any]:
    agents = _load_jsonl(export_dir / "agents.jsonl")
    tables = _load_jsonl(export_dir / "tables.jsonl")
    submissions = _load_jsonl(export_dir / "submissions.jsonl")
    hero_row = next(
        (a for a in agents if a.get("handle") == hero or a.get("name") == hero),
        None,
    )
    hero_stats = (hero_row or {}).get("stats") or {}
    player_counts = Counter(int(t.get("player_count") or 0) for t in tables)
    hu_tables = sum(1 for t in tables if int(t.get("player_count") or 0) == 2)
    hero_subs = [
        s for s in submissions
        if s.get("agent_handle") == hero
        or s.get("agent_id") and hero_row and s.get("agent_id") == hero_row.get("agent_id")
    ]
    if not hero_subs and hero_row:
        hero_id = hero_row.get("agent_id")
        hero_subs = [s for s in submissions if s.get("agent_id") == hero_id]
    payouts = [int(s.get("payout_chips") or 0) for s in hero_subs]
    chip_deltas = [
        int(s.get("chip_delta"))
        for s in hero_subs
        if s.get("chip_delta") is not None
    ]

    out: dict[str, Any] = {
        "source": "arena_export",
        "export_dir": str(export_dir),
        "hero": hero,
        "tables": len(tables),
        "hu_table_pct": round(hu_tables / max(len(tables), 1), 4),
        "player_count_distribution": dict(player_counts),
        "hero_submissions": len(hero_subs),
        "hero_pot_win_rate": round(
            sum(1 for p in payouts if p > 0) / max(len(payouts), 1), 4,
        ),
        "hero_vpip": hero_stats.get("vpip"),
        "hero_pfr": hero_stats.get("pfr"),
        "hero_adjusted_bb100": hero_row.get("adjusted_bb100") if hero_row else None,
        "hero_rank": hero_row.get("rank") if hero_row else None,
        "hero_hands": hero_row.get("hands") if hero_row else None,
    }
    if chip_deltas:
        out["hero_net_chips_replay"] = sum(chip_deltas)
    return out


def build_manifest(
    *,
    selfplay_summary: dict | None,
    arena_summary: dict | None,
    bundle_dir: Path,
    exploitability_advisory: dict | None = None,
    yardstick_pool_grade: dict | None = None,
    style_drift: dict | None = None,
    league_promotion_rubric: dict | None = None,
    deepsearch_trajectory_filter: dict | None = None,
    hierarchical_memory_advisory: dict | None = None,
) -> dict[str, Any]:
    manifest: dict[str, Any] = {
        "schema": "devfun.researcher_trajectory.v2",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "bundle_dir": str(bundle_dir),
        "selfplay": selfplay_summary,
        "arena": arena_summary,
    }
    # Include memory_gap block in axis_summary if available
    if selfplay_summary and "memory_gap" in selfplay_summary:
        manifest["memory_gap"] = selfplay_summary["memory_gap"]
    if selfplay_summary and "forgetting_regret" in selfplay_summary:
        manifest["forgetting_regret"] = selfplay_summary["forgetting_regret"]
    if exploitability_advisory:
        manifest["exploitability_advisory"] = exploitability_advisory
    if yardstick_pool_grade:
        manifest["yardstick_pool_grade"] = yardstick_pool_grade
    if style_drift:
        manifest["style_drift_d_policy"] = style_drift
    if league_promotion_rubric:
        manifest["league_promotion_rubric"] = league_promotion_rubric
    if deepsearch_trajectory_filter:
        manifest["deepsearch_trajectory_filter"] = deepsearch_trajectory_filter
    if hierarchical_memory_advisory:
        manifest["hierarchical_memory_advisory"] = hierarchical_memory_advisory
    manifest["gate_failures"] = evaluate_gates(manifest)
    manifest["gate_pass"] = not manifest["gate_failures"]
    return manifest


def _parse_opponent_bb100(raw: str | None) -> dict[str, float] | None:
    """Parse 'ten:-5,maniac_shark_lag:-40' or JSON object string."""
    if not raw or not str(raw).strip():
        return None
    text = str(raw).strip()
    if text.startswith("{"):
        data = json.loads(text)
        if not isinstance(data, dict):
            raise ValueError("--opponent-bb100 JSON must be an object")
        return {str(k): float(v) for k, v in data.items()}
    out: dict[str, float] = {}
    for part in text.split(","):
        part = part.strip()
        if not part:
            continue
        if ":" not in part:
            raise ValueError(f"bad --opponent-bb100 token {part!r}; want handle:bb100")
        handle, val = part.rsplit(":", 1)
        out[handle.strip()] = float(val.strip())
    return out or None


def _parse_action_dist(raw: str | None) -> dict[str, float] | None:
    """Parse 'fold:0.1,call:0.5,raise:0.4' or JSON object string."""
    if not raw or not str(raw).strip():
        return None
    text = str(raw).strip()
    if text.startswith("{"):
        data = json.loads(text)
        if not isinstance(data, dict):
            raise ValueError("style dist JSON must be an object")
        return {str(k): float(v) for k, v in data.items()}
    out: dict[str, float] = {}
    for part in text.split(","):
        part = part.strip()
        if not part:
            continue
        if ":" not in part:
            raise ValueError(f"bad style dist token {part!r}; want action:freq")
        action, val = part.rsplit(":", 1)
        out[action.strip()] = float(val.strip())
    return out or None


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Researcher Round axis proxy summary")
    p.add_argument("--selfplay", type=Path, default=None, help="selfplay trajectory JSONL")
    p.add_argument("--export-dir", type=Path, default=None, help="Arena export directory")
    p.add_argument("--hero", default="cemini_wiki_poker")
    p.add_argument(
        "--out-dir",
        type=Path,
        default=None,
        help="Write axis_summary.json + manifest.json (default: parent of selfplay or export-dir)",
    )
    p.add_argument(
        "--gate",
        action="store_true",
        help="Exit 1 if axis / hero_submission gates fail",
    )
    p.add_argument(
        "--skill-bb100",
        type=float,
        default=None,
        help="Skill proxy bb/100 (mean across soft opponents) for exploitability advisory",
    )
    p.add_argument(
        "--yardstick-bb100",
        type=float,
        default=None,
        help="Worst / named nemesis bb/100 for exploitability advisory",
    )
    p.add_argument(
        "--skill-hand-wr",
        type=float,
        default=None,
        help="Optional hand win-rate skill proxy (0-1) for exploitability advisory",
    )
    p.add_argument(
        "--opponent-bb100",
        default=None,
        help="Per-opponent bb/100: 'ten:4.3,maniac_shark_lag:-40' or JSON object",
    )
    p.add_argument(
        "--yardstick-pool",
        type=Path,
        default=None,
        help="Frozen yardstick pool JSON for pool grade (default: config/hu_yardstick_pool.json)",
    )
    p.add_argument(
        "--forgetting-decay",
        type=float,
        default=DEFAULT_FORGETTING_DECAY,
        help="Exponential decay for forgetting-factor regret (default: 0.95)",
    )
    p.add_argument(
        "--style-seed-dist",
        default=None,
        help="Seed demonstrator action dist: 'fold:0.2,call:0.5,raise:0.3' or JSON",
    )
    p.add_argument(
        "--style-candidate-dist",
        default=None,
        help="Candidate action dist for D_policy TV vs seed",
    )
    p.add_argument(
        "--style-preservation-config",
        type=Path,
        default=None,
        help="Style preservation JSON (default: config/hu_style_preservation.json)",
    )
    p.add_argument(
        "--deepsearch-filter-config",
        type=Path,
        default=None,
        help="DeepSearch filter JSON (default: config/hu_deepsearch_trajectory_filter.json)",
    )
    p.add_argument(
        "--hierarchical-memory-config",
        type=Path,
        default=None,
        help="Hierarchical memory JSON (default: config/hu_hierarchical_memory.json)",
    )
    args = p.parse_args(argv)

    if not args.selfplay and not args.export_dir:
        print("ERROR: pass --selfplay and/or --export-dir", file=sys.stderr)
        return 2

    selfplay_summary = None
    if args.selfplay:
        selfplay_summary = summarize_selfplay_trajectory(
            _load_jsonl(args.selfplay),
            forgetting_decay=args.forgetting_decay,
        )

    arena_summary = None
    if args.export_dir:
        arena_summary = summarize_arena_export(args.export_dir, args.hero)

    try:
        opponent_bb100 = _parse_opponent_bb100(args.opponent_bb100)
    except (ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: --opponent-bb100: {exc}", file=sys.stderr)
        return 2

    try:
        style_seed_dist = _parse_action_dist(args.style_seed_dist)
        style_candidate_dist = _parse_action_dist(args.style_candidate_dist)
    except (ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: style dist: {exc}", file=sys.stderr)
        return 2

    exploitability_advisory = compute_exploitability_advisory(
        skill_bb100=args.skill_bb100,
        yardstick_bb100=args.yardstick_bb100,
        opponent_bb100=opponent_bb100,
        skill_hand_win_rate=args.skill_hand_wr,
    )

    yardstick_pool_grade = None
    if opponent_bb100 and (args.yardstick_pool is not None or args.opponent_bb100):
        try:
            yardstick_pool_grade = compute_yardstick_pool_grade(
                opponent_bb100,
                pool_config=args.yardstick_pool,
            )
        except (FileNotFoundError, ValueError, json.JSONDecodeError) as exc:
            print(f"WARN: yardstick pool grade skipped: {exc}", file=sys.stderr)

    style_drift = None
    if style_seed_dist and style_candidate_dist:
        try:
            style_drift = compute_style_drift_d_policy(
                style_seed_dist,
                style_candidate_dist,
                config=args.style_preservation_config,
            )
        except (FileNotFoundError, ValueError, json.JSONDecodeError) as exc:
            print(f"WARN: style drift skipped: {exc}", file=sys.stderr)

    forgetting_regret = (selfplay_summary or {}).get("forgetting_regret")
    league_promotion_rubric = compute_league_promotion_rubric_advisory(
        yardstick_grade=yardstick_pool_grade,
        style_drift=style_drift,
        forgetting=forgetting_regret,
        exploitability_advisory=exploitability_advisory,
    )

    deepsearch_trajectory_filter = None
    if args.selfplay:
        try:
            deepsearch_trajectory_filter = compute_deepsearch_trajectory_filter_advisory(
                _load_jsonl(args.selfplay),
                config=args.deepsearch_filter_config,
            )
        except (FileNotFoundError, ValueError, json.JSONDecodeError) as exc:
            print(f"WARN: deepsearch filter skipped: {exc}", file=sys.stderr)

    hierarchical_memory_advisory = None
    try:
        from hierarchical_session_state import (  # noqa: WPS433
            build_memory_slice_for_decide,
            compute_hierarchical_memory_advisory,
            empty_state,
        )

        empty_slice = build_memory_slice_for_decide(
            empty_state(),
            config=args.hierarchical_memory_config,
        )
        hierarchical_memory_advisory = compute_hierarchical_memory_advisory(
            empty_slice,
            config=args.hierarchical_memory_config,
        )
    except Exception as exc:  # noqa: BLE001 — advisory only
        print(f"WARN: hierarchical memory advisory skipped: {exc}", file=sys.stderr)

    out_dir = args.out_dir
    if out_dir is None:
        if args.selfplay:
            out_dir = args.selfplay.parent
        elif args.export_dir:
            out_dir = args.export_dir
        else:
            out_dir = Path("reports/researcher-round")

    out_dir.mkdir(parents=True, exist_ok=True)
    manifest = build_manifest(
        selfplay_summary=selfplay_summary,
        arena_summary=arena_summary,
        bundle_dir=out_dir,
        exploitability_advisory=exploitability_advisory,
        yardstick_pool_grade=yardstick_pool_grade,
        style_drift=style_drift,
        league_promotion_rubric=league_promotion_rubric,
        deepsearch_trajectory_filter=deepsearch_trajectory_filter,
        hierarchical_memory_advisory=hierarchical_memory_advisory,
    )
    (out_dir / "axis_summary.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (out_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    index_path = Path("reports/hl-loop/researcher_trajectory_index.jsonl")
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_row: dict[str, Any] = {
        "at": manifest["generated_at"],
        "bundle_dir": str(out_dir),
        "selfplay_decisions": (selfplay_summary or {}).get("decision_count"),
        "arena_tables": (arena_summary or {}).get("tables"),
        "vpip_proxy": (selfplay_summary or {}).get("vpip_proxy"),
        "bb100": (arena_summary or {}).get("hero_adjusted_bb100"),
        "gate_pass": manifest.get("gate_pass"),
    }

    # K134: Add rubric epoch and evaluator_id (best effort, guarded)
    try:
        from sandbox_rubric_epoch import load_rubric_config, current_epoch, evaluator_id

        _cfg = load_rubric_config()
        index_row["rubric_epoch"] = current_epoch(_cfg)
        index_row["evaluator_id"] = evaluator_id(_cfg)
    except Exception:
        # Backward compat: if rubric epoch tooling unavailable, omit keys
        pass

    with index_path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(index_row, sort_keys=True) + "\n")

    print(f"[trajectory] axis_summary → {out_dir / 'axis_summary.json'}")
    if selfplay_summary:
        axes = (selfplay_summary.get("axes") or {})
        print(
            f"  selfplay: {selfplay_summary.get('decision_count')} decisions "
            f"vpip_proxy={selfplay_summary.get('vpip_proxy')} "
            f"pfr_proxy={selfplay_summary.get('pfr_proxy')} "
            f"M8_hall={axes.get('M8_hallucination_rate')} "
            f"M9_gap={axes.get('M9_btn_minus_utg_vpip')}"
        )
    if arena_summary:
        print(
            f"  arena: tables={arena_summary.get('tables')} "
            f"hero_subs={arena_summary.get('hero_submissions')} "
            f"rank={arena_summary.get('hero_rank')} "
            f"bb100={arena_summary.get('hero_adjusted_bb100')}"
        )

    advisory = manifest.get("exploitability_advisory") or {}
    if advisory:
        flag = "DISCONNECT" if advisory.get("disconnect") else "ok"
        print(
            f"  exploitability_advisory: {flag} "
            f"skill_bb100={advisory.get('skill_bb100')} "
            f"yardstick_bb100={advisory.get('yardstick_bb100')} "
            f"({advisory.get('yardstick_handle') or 'n/a'})"
        )

    pool_grade = manifest.get("yardstick_pool_grade") or {}
    if pool_grade:
        print(
            f"  yardstick_pool_grade: pct_pass={pool_grade.get('pct_pass')} "
            f"n_pass={pool_grade.get('n_pass')}/{pool_grade.get('n_checked')} "
            f"worst={pool_grade.get('worst_handle')} "
            f"({pool_grade.get('worst_bb100')})"
        )

    style = manifest.get("style_drift_d_policy") or {}
    if style:
        flag = "STYLE_GAP" if not style.get("style_ok") else "ok"
        print(
            f"  style_drift_d_policy: {flag} "
            f"tv={style.get('d_policy_tv')} "
            f"max={style.get('max_d_policy_tv_advisory')}"
        )

    rubric = manifest.get("league_promotion_rubric") or {}
    if rubric.get("gaps") or rubric.get("footsiesgym_note"):
        print(
            f"  league_promotion_rubric: gaps={rubric.get('gaps')} "
            f"yardstick_gap={rubric.get('yardstick_gap')} "
            f"style_gap={rubric.get('style_gap')}"
        )
        if rubric.get("footsiesgym_note"):
            print(f"    footsiesgym: {rubric.get('footsiesgym_note')}")

    ds = manifest.get("deepsearch_trajectory_filter") or {}
    if ds.get("n_units") is not None:
        print(
            f"  deepsearch_filter: eligible={ds.get('n_eligible')}/{ds.get('n_units')} "
            f"pct={ds.get('eligible_pct')} reasons={ds.get('rejected_reasons')}"
        )

    hier = manifest.get("hierarchical_memory_advisory") or {}
    if hier:
        flag = "ok" if hier.get("within_budget") else "OVER_BUDGET"
        print(
            f"  hierarchical_memory: {flag} "
            f"chars={hier.get('slice_chars')}/{hier.get('slice_max_chars')}"
        )

    forgetting = manifest.get("forgetting_regret") or {}
    if forgetting.get("n_hands"):
        drift = "DRIFT" if forgetting.get("drift_flag") else "ok"
        print(
            f"  forgetting_regret: {drift} "
            f"lifetime_bb={forgetting.get('lifetime_mean_bb')} "
            f"recency_bb={forgetting.get('recency_weighted_mean_bb')} "
            f"n={forgetting.get('n_hands')}"
        )

    failures = manifest.get("gate_failures") or []
    if failures:
        print("[trajectory] GATE FAILURES:", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
    else:
        print("[trajectory] gates: PASS")

    if args.gate and failures:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
