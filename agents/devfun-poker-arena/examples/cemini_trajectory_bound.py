#!/usr/bin/env python3
"""Standalone K125 probabilistic trajectory bounds for poker decisions."""
from __future__ import annotations

from dataclasses import dataclass
import json
import math
from pathlib import Path
import re
import tomllib
from typing import Any


_CARD_TOKEN_RE = re.compile(r"(?<![A-Za-z0-9])([2-9TJQKA][hdcs])(?![A-Za-z0-9])", re.I)
_AGGRESSIVE_ACTIONS = frozenset({"bet", "raise", "all-in", "all_in", "allin"})


@dataclass(frozen=True)
class PredicateBound:
    """Upper bound for one verifier predicate at one decision."""

    name: str
    u: float
    reason: str = ""


@dataclass(frozen=True)
class DecisionContribution:
    """Composed risk contribution for one decision in a hand."""

    hand_id: Any
    action: str
    street: str = ""
    risk: float = 0.0
    bounds: tuple[PredicateBound, ...] = ()
    mode: str = "independent"


@dataclass(frozen=True)
class TrajectoryBoundState:
    """Current hand-level upper bound state."""

    hand_id: Any = None
    decision_count: int = 0
    cumulative_risk: float = 0.0
    contributions: tuple[DecisionContribution, ...] = ()


@dataclass(frozen=True)
class BoundConfig:
    """Configuration for WS-A trajectory-bound prototype."""

    veto_threshold: float = 0.05
    composition_mode: str = "independent"
    river_bluff_floor: float = 0.35
    m8_factual_u: float = 0.04
    regression_forbidden_u: float = 1.0
    axis_floor_u: float = 0.0
    legality_u: float = 0.0
    illegal_action_u: float = 1.0
    min_equity_sims: int = 1
    unknown_equity_u: float = 0.0
    prefer_regression_oracle: bool = True
    safest_action_order: tuple[str, ...] = (
        "check",
        "fold",
        "call",
        "bet",
        "raise",
        "all-in",
        "all_in",
    )


@dataclass(frozen=True)
class VetoResult:
    """Result of applying the trajectory-bound threshold."""

    veto: bool
    risk: float
    threshold: float
    action: str | None = None
    reason: str = ""


def _clamp01(x: float) -> float:
    if not math.isfinite(x):
        return 1.0 if x > 0 else 0.0
    return max(0.0, min(1.0, float(x)))


def _normal_cdf(z: float) -> float:
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def _norm_action(action: Any) -> str:
    return str(action or "").strip().lower().replace(" ", "-")


def _available_action_names(available_actions: Any) -> set[str]:
    if not available_actions:
        return set()
    if isinstance(available_actions, dict):
        return {_norm_action(k) for k, v in available_actions.items() if v is not False}
    if isinstance(available_actions, (list, tuple, set, frozenset)):
        return {_norm_action(a) for a in available_actions}
    return set()


def _cards_from_hole_key(hole_key: Any) -> set[str]:
    compact = str(hole_key or "").replace(" ", "")
    return {
        compact[i : i + 2].lower()
        for i in range(0, len(compact), 2)
        if _CARD_TOKEN_RE.fullmatch(compact[i : i + 2])
    }


def _cards_from_board(board: Any) -> set[str]:
    if board is None:
        return set()
    if isinstance(board, str):
        raw = board.replace(",", " ").split()
        if len(raw) == 1:
            compact = raw[0]
            raw = [compact[i : i + 2] for i in range(0, len(compact), 2)]
    elif isinstance(board, (list, tuple, set, frozenset)):
        raw = [str(c) for c in board]
    else:
        raw = []
    return {
        str(item).strip()[:2].lower()
        for item in raw
        if _CARD_TOKEN_RE.fullmatch(str(item).strip()[:2])
    }


def _has_m8_factual_violation(features: dict) -> bool:
    reasoning = str(features.get("reasoning") or "")
    found = {m.group(1).lower() for m in _CARD_TOKEN_RE.finditer(reasoning)}
    if not found:
        return False
    allowed = _cards_from_hole_key(features.get("hole_key")) | _cards_from_board(features.get("board"))
    return bool(found - allowed)


def _mc_equity_u(features: dict, cfg: BoundConfig) -> float:
    if _norm_action(features.get("action")) not in _AGGRESSIVE_ACTIONS:
        return 0.0
    equity = features.get("equity")
    sims = features.get("sims")
    if equity is None or sims is None:
        return _clamp01(cfg.unknown_equity_u)
    p = _clamp01(float(equity))
    if p >= cfg.river_bluff_floor:
        return 0.0
    n = max(int(sims), int(cfg.min_equity_sims), 1)
    se = math.sqrt(max(p * (1.0 - p), 1e-12) / n)
    return _clamp01(_normal_cdf((float(cfg.river_bluff_floor) - p) / se))


def per_decision_bounds(features: dict, cfg: BoundConfig) -> list[PredicateBound]:
    """Build verifier predicate bounds for a single decision feature dict."""

    action = _norm_action(features.get("action"))
    available = _available_action_names(features.get("available_actions"))
    illegal = bool(available and action and action not in available)
    bounds = [
        PredicateBound(
            "legality",
            _clamp01(cfg.illegal_action_u if illegal else cfg.legality_u),
            "action not in available_actions" if illegal else "legal action assumed",
        )
    ]
    if action in _AGGRESSIVE_ACTIONS:
        bounds.append(PredicateBound("mc_equity", _mc_equity_u(features, cfg), "equity floor"))
    bounds.append(
        PredicateBound(
            "m8_factual",
            _clamp01(cfg.m8_factual_u) if _has_m8_factual_violation(features) else 0.0,
            "card token outside hole/board" if _has_m8_factual_violation(features) else "no card violation",
        )
    )
    bounds.append(
        PredicateBound(
            "regression",
            _clamp01(cfg.regression_forbidden_u) if features.get("matches_regression_forbidden") else 0.0,
            "matches forbidden regression"
            if features.get("matches_regression_forbidden")
            else "no forbidden regression match",
        )
    )
    if cfg.axis_floor_u > 0:
        bounds.append(PredicateBound("axis_floor", _clamp01(cfg.axis_floor_u), "configured floor"))
    return bounds


def compose_decision(bounds: list[PredicateBound] | tuple[PredicateBound, ...], mode: str) -> float:
    """Compose predicate upper bounds into one decision-level upper bound."""

    us = [_clamp01(b.u) for b in bounds]
    if not us:
        return 0.0
    mode = str(mode or "independent").lower()
    if mode == "independent":
        keep = 1.0
        for u in us:
            keep *= 1.0 - u
        return _clamp01(1.0 - keep)
    if mode in {"union", "dro"}:
        return _clamp01(sum(us))
    raise ValueError(f"unsupported compose mode: {mode}")


def propagate(state: TrajectoryBoundState, contrib: DecisionContribution) -> TrajectoryBoundState:
    """Propagate one decision contribution into a monotone hand-level R* state."""

    same_hand = state.hand_id == contrib.hand_id
    prior = state.cumulative_risk if same_hand else 0.0
    merged = compose_decision(
        (PredicateBound("prior_trajectory", prior), PredicateBound("decision", contrib.risk)),
        contrib.mode,
    )
    return TrajectoryBoundState(
        hand_id=contrib.hand_id,
        decision_count=(state.decision_count + 1) if same_hand else 1,
        cumulative_risk=merged,
        contributions=(state.contributions + (contrib,)) if same_hand else (contrib,),
    )


def evaluate_veto(
    state: TrajectoryBoundState,
    available_actions: dict,
    cfg: BoundConfig,
) -> VetoResult:
    """Veto when cumulative trajectory risk exceeds the configured threshold."""

    risk = _clamp01(state.cumulative_risk)
    threshold = _clamp01(cfg.veto_threshold)
    veto = risk > threshold
    return VetoResult(
        veto=veto,
        risk=risk,
        threshold=threshold,
        action=safest_legal_action(available_actions, cfg) if veto else None,
        reason=(
            f"trajectory risk {risk:.6f} exceeds threshold {threshold:.6f}"
            if veto
            else f"trajectory risk {risk:.6f} within threshold {threshold:.6f}"
        ),
    )


def load_bound_config(path: Path) -> BoundConfig:
    """Load a BoundConfig from JSON or TOML, ignoring unknown keys."""

    if path.suffix.lower() == ".json":
        data = json.loads(path.read_text(encoding="utf-8"))
    elif path.suffix.lower() == ".toml":
        data = tomllib.loads(path.read_text(encoding="utf-8"))
    else:
        raise ValueError(f"unsupported config format: {path.suffix}")
    valid = set(BoundConfig.__dataclass_fields__)
    kwargs = {k: v for k, v in data.items() if k in valid}
    if "safest_action_order" in kwargs:
        kwargs["safest_action_order"] = tuple(str(a) for a in kwargs["safest_action_order"])
    return BoundConfig(**kwargs)


def safest_legal_action(
    available_actions: dict,
    cfg: BoundConfig,
    regression_oracle_action: str | None = None,
) -> str:
    """Return regression oracle action when legal, otherwise check/fold-first fallback."""

    available = _available_action_names(available_actions)
    if not available:
        return "fold"
    oracle = _norm_action(regression_oracle_action)
    if cfg.prefer_regression_oracle and oracle and oracle in available:
        return oracle
    for action in cfg.safest_action_order:
        norm = _norm_action(action)
        if norm in available:
            return norm
    return sorted(available)[0]


def contribution_from_features(features: dict, cfg: BoundConfig) -> DecisionContribution:
    """Convenience helper for examples/tests: features -> composed contribution."""

    bounds = tuple(per_decision_bounds(features, cfg))
    mode = str(features.get("composition_mode") or cfg.composition_mode)
    return DecisionContribution(
        hand_id=features.get("hand_id"),
        action=_norm_action(features.get("action")),
        street=str(features.get("street") or ""),
        risk=compose_decision(bounds, mode),
        bounds=bounds,
        mode=mode,
    )


# ---------------------------------------------------------------------------
# Offline trajectory JSONL rescoring (WS-C) — dict config, not BoundConfig
# ---------------------------------------------------------------------------

DEFAULT_OFFLINE_CONFIG: dict[str, Any] = {
    "tau": 0.05,
    "mode": "independent",
    "bounds": {
        "base": 0.001,
        "hallucinated_card": 0.20,
        "hole_leak": 0.03,
        "reasoning_over_150": 0.01,
        "missing_action": 0.02,
    },
}


def merged_config(config: dict[str, Any] | None = None) -> dict[str, Any]:
    merged = {
        "tau": DEFAULT_OFFLINE_CONFIG["tau"],
        "mode": DEFAULT_OFFLINE_CONFIG["mode"],
        "bounds": dict(DEFAULT_OFFLINE_CONFIG["bounds"]),
    }
    if not config:
        return merged
    for key, value in config.items():
        if key == "bounds" and isinstance(value, dict):
            merged["bounds"].update(value)
        elif key == "predicates" and isinstance(value, dict):
            # calibration JSON: map predicate u into offline bounds keys
            preds = value
            if "m8_factual" in preds:
                merged["bounds"]["hallucinated_card"] = float(
                    preds["m8_factual"].get("u", merged["bounds"]["hallucinated_card"])
                )
        else:
            merged[key] = value
    return merged


def _cards_in_text(text: str) -> set[str]:
    return {m.group(1).lower() for m in _CARD_TOKEN_RE.finditer(text or "")}


def _allowed_cards_from_hole_key(hole_key: str) -> set[str]:
    allowed: set[str] = set()
    compact = hole_key.replace(" ", "")
    for i in range(0, len(compact), 2):
        card = compact[i:i + 2]
        if len(card) == 2:
            allowed.add(card.lower())
    return allowed


def per_decision_bounds_trajectory(
    decisions: list[dict[str, Any]],
    config: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    """Assign upper-bound u to each trajectory decision row."""
    cfg = merged_config(config)
    bounds_cfg = cfg["bounds"]
    out: list[dict[str, Any]] = []
    for decision in sorted(decisions, key=lambda d: int(d.get("step") or 0)):
        reasons: list[str] = []
        u = float(bounds_cfg.get("base", 0.001))
        action = str(decision.get("action") or "").strip().lower()
        if not action:
            u += float(bounds_cfg.get("missing_action", 0.02))
            reasons.append("missing_action")
        reasoning = str(decision.get("reasoning") or "")
        if len(reasoning) > 150:
            u += float(bounds_cfg.get("reasoning_over_150", 0.01))
            reasons.append("reasoning_over_150")
        allowed_cards = _allowed_cards_from_hole_key(str(decision.get("hole_key") or ""))
        mentioned_cards = _cards_in_text(reasoning)
        if mentioned_cards - allowed_cards:
            u += float(bounds_cfg.get("hallucinated_card", 0.20))
            reasons.append("hallucinated_card")
        compact_hole = str(decision.get("hole_key") or "").replace(" ", "").lower()
        if compact_hole and compact_hole in reasoning.lower().replace(" ", ""):
            u += float(bounds_cfg.get("hole_leak", 0.03))
            reasons.append("hole_leak")
        out.append({
            "hand_id": decision.get("hand_id"),
            "step": decision.get("step"),
            "u": _clamp01(u),
            "reasons": reasons,
        })
    return out


def propagate_trajectory(
    decision_bounds: list[dict[str, Any] | float],
    config: dict[str, Any] | None = None,
) -> float:
    """Compose per-decision bounds into hand-level R*."""
    cfg = merged_config(config)
    mode = str(cfg.get("mode") or "independent").lower()
    probs = [_clamp01(_offline_bound_value(bound)) for bound in decision_bounds]
    if not probs:
        return 0.0
    if mode == "union":
        return round(_clamp01(sum(probs)), 6)
    clean_probability = math.prod(1.0 - p for p in probs)
    return round(_clamp01(1.0 - clean_probability), 6)


def _offline_bound_value(bound: dict[str, Any] | float) -> float:
    if isinstance(bound, dict):
        return float(bound.get("u") or 0.0)
    return float(bound)
