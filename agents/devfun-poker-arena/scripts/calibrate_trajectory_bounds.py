#!/usr/bin/env python3
"""Calibrate K125 trajectory-bound predicate upper bounds from selfplay JSONL."""
from __future__ import annotations

import argparse
import importlib.util
import json
import math
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "examples"
TESTS = ROOT / "tests"
if str(EXAMPLES) not in sys.path:
    sys.path.insert(0, str(EXAMPLES))
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    from cemini_trajectory_bound import BoundConfig, load_bound_config  # type: ignore

    BOUND_IMPORT_NOTE = "using examples/cemini_trajectory_bound.py"
except ModuleNotFoundError:
    BOUND_IMPORT_NOTE = (
        "examples/cemini_trajectory_bound.py not found; using inline compatible "
        "BoundConfig loader for merge"
    )

    @dataclass
    class BoundConfig:  # type: ignore[no-redef]
        tau: float
        mode: str
        predicates: dict[str, dict[str, Any]]
        raw: dict[str, Any]

    def load_bound_config(path: Path) -> BoundConfig:  # type: ignore[no-redef]
        raw = json.loads(path.read_text(encoding="utf-8"))
        return BoundConfig(
            tau=float(raw.get("tau", 0.05)),
            mode=str(raw.get("mode", "independent")),
            predicates=dict(raw.get("predicates") or {}),
            raw=raw,
        )


DEFAULT_CONFIG: dict[str, Any] = {
    "schema": "devfun.trajectory_bound.v1",
    "tau": 0.05,
    "mode": "independent",
    "predicates": {
        "legality": {
            "enabled": True,
            "u": 0.0001,
            "source": "deterministic allowedActions oracle; epsilon ~= 0",
        },
        "mc_equity": {
            "enabled": True,
            "u": 0.03,
            "source": "Monte Carlo equity estimator variance proxy",
        },
        "m8_factual": {
            "enabled": True,
            "u": 0.05,
            "source": "M8 reasoning factuality regex proxy",
        },
        "regression": {
            "enabled": True,
            "u": 0.02,
            "source": "HL regression spot replay/match guard",
        },
        "axis_floor": {
            "enabled": True,
            "u": 0.05,
            "source": "Researcher multi-axis floor gate",
        },
    },
}

KNOWN_ACTIONS = frozenset({"fold", "check", "call", "bet", "raise", "all-in"})
CARD_RE = re.compile(r"(?<![A-Za-z0-9])([2-9TJQKA][hdcs])(?![A-Za-z0-9])", re.I)
EQUITY_RE = re.compile(r"\b(?:eq|equity|mc)\s*[:=]?\s*(-?\d+(?:\.\d+)?)\s*%?", re.I)


@dataclass
class Estimate:
    name: str
    samples: int
    failures: int
    default_u: float
    empirical_u95: float
    calibrated_u: float
    note: str


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            print(f"WARN: skipping invalid JSONL line {line_no}: {exc}", file=sys.stderr)
            continue
        if isinstance(row, dict):
            rows.append(row)
    return rows


def wilson_upper(failures: int, samples: int, z: float = 1.96) -> float:
    if samples <= 0:
        return 0.0
    phat = failures / samples
    denom = 1 + z * z / samples
    center = phat + z * z / (2 * samples)
    margin = z * math.sqrt((phat * (1 - phat) + z * z / (4 * samples)) / samples)
    return min(1.0, (center + margin) / denom)


def rate(failures: int, samples: int) -> float:
    return failures / samples if samples else 0.0


def default_u(config: dict[str, Any], name: str) -> float:
    pred = (config.get("predicates") or {}).get(name) or {}
    return float(pred.get("u") or 0.0)


def estimate(config: dict[str, Any], name: str, samples: int, failures: int, note: str) -> Estimate:
    base = default_u(config, name)
    empirical = wilson_upper(failures, samples)
    calibrated = max(base, rate(failures, samples)) if samples else base
    return Estimate(name, samples, failures, base, empirical, calibrated, note)


def hole_cards(hole_key: str) -> list[str]:
    compact = str(hole_key or "").replace(" ", "")
    return [
        compact[i:i + 2].lower()
        for i in range(0, len(compact), 2)
        if len(compact[i:i + 2]) == 2
    ]


def cards_in_text(text: str) -> set[str]:
    return {m.group(1).lower() for m in CARD_RE.finditer(text or "")}


def allowed_cards(row: dict[str, Any]) -> set[str]:
    cards = set(hole_cards(str(row.get("hole_key") or "")))
    board = row.get("board") or row.get("board_cards") or row.get("boardCards") or []
    for card in board:
        text = str(card).strip()
        if len(text) >= 2:
            cards.add(text[:2].lower())
    return cards


def estimate_legality(decisions: list[dict[str, Any]], config: dict[str, Any]) -> Estimate:
    samples = failures = 0
    for row in decisions:
        action = str(row.get("action") or "").lower()
        legal = (
            row.get("available_actions")
            or row.get("legal_actions")
            or row.get("availableActions")
            or (row.get("allowedActions") or {}).get("availableActions")
        )
        if legal:
            samples += 1
            if action not in {str(a).lower() for a in legal}:
                failures += 1
        elif action:
            samples += 1
            if action not in KNOWN_ACTIONS:
                failures += 1
    return estimate(
        config,
        "legality",
        samples,
        failures,
        "action outside legal menu when present; otherwise unknown action enum",
    )


def estimate_m8(decisions: list[dict[str, Any]], config: dict[str, Any]) -> Estimate:
    samples = failures = 0
    for row in decisions:
        reasoning = str(row.get("reasoning") or "")
        if not reasoning:
            continue
        samples += 1
        found = cards_in_text(reasoning)
        extra = found - allowed_cards(row)
        hole_key = str(row.get("hole_key") or "").replace(" ", "").lower()
        leak = bool(hole_key and hole_key in reasoning.lower().replace(" ", ""))
        if extra or leak:
            failures += 1
    return estimate(
        config,
        "m8_factual",
        samples,
        failures,
        "reasoning mentions hallucinated cards or concatenated hole cards",
    )


def estimate_mc_equity(decisions: list[dict[str, Any]], config: dict[str, Any]) -> Estimate:
    samples = failures = 0
    for row in decisions:
        reasoning = str(row.get("reasoning") or "")
        for match in EQUITY_RE.finditer(reasoning):
            samples += 1
            value = float(match.group(1))
            if value < 0 or value > 100:
                failures += 1
    return estimate(
        config,
        "mc_equity",
        samples,
        failures,
        "malformed equity claims in reasoning; true MC variance keeps default when unobservable",
    )


def hand_class(cards: list[str]) -> str:
    if len(cards) != 2:
        return ""
    ranks = "23456789TJQKA"
    r1, r2 = str(cards[0])[:1].upper(), str(cards[1])[:1].upper()
    if r1 not in ranks or r2 not in ranks:
        return ""
    if r1 == r2:
        return r1 + r2
    ordered = sorted((r1, r2), key=ranks.index, reverse=True)
    suited = str(cards[0])[-1:].lower() == str(cards[1])[-1:].lower()
    return "".join(ordered) + ("s" if suited else "o")


def row_hand_class(row: dict[str, Any]) -> str:
    return hand_class(hole_cards(str(row.get("hole_key") or "")))


def spot_signature(spot: Any) -> dict[str, Any]:
    table = getattr(spot, "table", {}) or {}
    self_num = table.get("selfSeatNumber")
    hero_hole: list[str] = []
    for seat in table.get("seats") or []:
        if seat.get("seatNumber") == self_num:
            hero_hole = list(seat.get("holeCards") or [])
            break
    position = ""
    try:
        from position_utils import hero_position_label  # noqa: WPS433

        position = hero_position_label(table)
    except Exception:
        pass
    return {
        "id": getattr(spot, "id", ""),
        "street": table.get("street"),
        "position": position,
        "hand_class": hand_class(hero_hole),
        "forbidden": {str(a).lower() for a in getattr(spot, "forbidden", frozenset())},
        "required": {str(a).lower() for a in getattr(spot, "required", frozenset())},
    }


def regression_signatures() -> list[dict[str, Any]]:
    fixture = TESTS / "fixtures" / "regression_spots.py"
    spec = importlib.util.spec_from_file_location("regression_spots", fixture)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {fixture}")
    module = importlib.util.module_from_spec(spec)
    sys.modules.setdefault("regression_spots", module)
    spec.loader.exec_module(module)
    spots: list[Any] = []
    for name in ("regression_spots", "nuts_regression_spots"):
        fn = getattr(module, name, None)
        if callable(fn):
            spots.extend(fn())
    return [spot_signature(spot) for spot in spots]


def estimate_regression(decisions: list[dict[str, Any]], config: dict[str, Any], enabled: bool) -> Estimate:
    if not enabled:
        return estimate(config, "regression", 0, 0, "regression spot matching disabled")
    try:
        signatures = regression_signatures()
    except Exception as exc:
        return estimate(
            config,
            "regression",
            0,
            0,
            f"could not import tests/fixtures/regression_spots.py: {exc}",
        )

    samples = failures = 0
    for row in decisions:
        cls = row_hand_class(row)
        if not cls:
            continue
        action = str(row.get("action") or "").lower()
        street = str(row.get("street") or "")
        position = str(row.get("position") or "")
        for sig in signatures:
            if sig["hand_class"] != cls:
                continue
            if sig["street"] and str(sig["street"]) != street:
                continue
            if sig["position"] and sig["position"] != position:
                continue
            samples += 1
            if action in sig["forbidden"] or (sig["required"] and action not in sig["required"]):
                failures += 1
            break
    return estimate(
        config,
        "regression",
        samples,
        failures,
        f"matched {samples} selfplay decisions against regression spot signatures",
    )


def estimate_axis_floor(rows: list[dict[str, Any]], config: dict[str, Any]) -> Estimate:
    try:
        from researcher_trajectory_summary import (  # noqa: WPS433
            DEFAULT_GATE_THRESHOLDS,
            summarize_selfplay_trajectory,
        )
    except Exception as exc:
        return estimate(
            config,
            "axis_floor",
            0,
            0,
            f"could not import researcher_trajectory_summary axis logic: {exc}",
        )

    summary = summarize_selfplay_trajectory(rows)
    axes = summary.get("axes") or {}
    if not axes:
        return estimate(config, "axis_floor", 0, 0, "no axis data in selfplay trajectory")
    gap = float(axes.get("M9_positional_vpip_gap") or axes.get("M9_btn_minus_utg_vpip") or 0)
    failures = int(gap < float(DEFAULT_GATE_THRESHOLDS["M9_btn_minus_utg_vpip_min"]))
    return estimate(config, "axis_floor", 1, failures, f"M9 positional VPIP floor sample; gap={gap:.4f}")


def load_config(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return json.loads(json.dumps(DEFAULT_CONFIG))
    loaded = load_bound_config(path)
    raw = getattr(loaded, "raw", None)
    if isinstance(raw, dict):
        return raw
    return {
        "schema": "devfun.trajectory_bound.v1",
        "tau": getattr(loaded, "tau", 0.05),
        "mode": getattr(loaded, "mode", "independent"),
        "predicates": getattr(loaded, "predicates", {}),
    }


def update_config(config: dict[str, Any], estimates: list[Estimate], selfplay: Path) -> dict[str, Any]:
    out = json.loads(json.dumps(config))
    out.setdefault("schema", "devfun.trajectory_bound.v1")
    out.setdefault("tau", 0.05)
    out.setdefault("mode", "independent")
    predicates = out.setdefault("predicates", {})
    for est in estimates:
        pred = predicates.setdefault(est.name, {"enabled": True})
        pred["u"] = round(est.calibrated_u, 6)
        pred["empirical_fn_rate"] = round(rate(est.failures, est.samples), 6)
        pred["empirical_u95"] = round(est.empirical_u95, 6)
        pred["samples"] = est.samples
        pred["failures"] = est.failures
        pred["calibration_note"] = est.note
    out["calibrated_at"] = datetime.now(timezone.utc).isoformat()
    out["calibration_source"] = str(selfplay)
    out["calibration_method"] = "empirical failure rate; max(default_u, empirical_fn_rate); empirical_u95 is reported for review"
    return out


def print_summary(estimates: list[Estimate]) -> None:
    print("predicate      samples  failures  fn_rate  u_default  u_emp95  u_written")
    print("-------------  -------  --------  -------  ---------  -------  ---------")
    for est in estimates:
        print(
            f"{est.name:<13}  {est.samples:>7}  {est.failures:>8}  "
            f"{rate(est.failures, est.samples):>7.4f}  {est.default_u:>9.4f}  "
            f"{est.empirical_u95:>7.4f}  {est.calibrated_u:>9.4f}"
        )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Calibrate K125 trajectory-bound predicate upper bounds",
    )
    parser.add_argument("--selfplay", type=Path, required=True, help="selfplay trajectory JSONL")
    parser.add_argument(
        "--out",
        type=Path,
        default=EXAMPLES / "trajectory_bound_config.json",
        help="output config JSON (default: examples/trajectory_bound_config.json)",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=None,
        help="base config JSON (default: --out if it exists, else built-in defaults)",
    )
    parser.add_argument(
        "--regression-spots",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="match tests/fixtures/regression_spots.py patterns (default: enabled)",
    )
    args = parser.parse_args(argv)

    if not args.selfplay.is_file():
        print(f"ERROR: selfplay JSONL not found: {args.selfplay}", file=sys.stderr)
        return 2

    rows = load_jsonl(args.selfplay)
    decisions = [row for row in rows if row.get("record_type") == "decision"]
    config = load_config(args.config or args.out)
    estimates = [
        estimate_legality(decisions, config),
        estimate_mc_equity(decisions, config),
        estimate_m8(decisions, config),
        estimate_regression(decisions, config, args.regression_spots),
        estimate_axis_floor(rows, config),
    ]

    updated = update_config(config, estimates, args.selfplay)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(updated, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(f"[trajectory-bound] {args.out}")
    print(f"[trajectory-bound] loader: {BOUND_IMPORT_NOTE}")
    print_summary(estimates)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
