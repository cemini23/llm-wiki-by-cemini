#!/usr/bin/env python3
"""K129 IRumAI-inspired HU range probe — linear model on public action history.

Exports selfplay trajectories with showdown villain labels, trains a tiny
logistic probe on aggregated per-hand features, and compares AUC vs a
position-only baseline. Offline only — no Arena API required.

Usage:
    uv run python examples/irumai_range_probe.py --hands 500
    uv run python examples/irumai_range_probe.py --decide examples/cemini_decide.py --hands 200
"""
from __future__ import annotations

import argparse
import json
import math
import random
import sys
from pathlib import Path
from typing import Any, Callable, Optional

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from treys import Card, Evaluator  # noqa: E402

from selfplay import (  # noqa: E402
    _load_decide_from_path,
    _opponents_for_selfplay,
    play_one_hand,
)

DEFAULT_STACK = 200
DEFAULT_SMALL_BLIND = 1
DEFAULT_BIG_BLIND = 2

EVALUATOR = Evaluator()
MAX_HAND_RANK = 7462.0
STREET_ORDER = {"Preflop": 0, "Flop": 1, "Turn": 2, "River": 3}
ACTION_RAISE = frozenset({"bet", "raise", "all-in"})


def treys_card_list(key: str) -> list[int]:
    cards: list[int] = []
    i = 0
    while i + 1 < len(key):
        cards.append(Card.new(key[i : i + 2]))
        i += 2
    return cards


def _preflop_strength_norm(hole_key: str) -> float:
    """Rough 0–1 strength when board is incomplete (<5 cards for treys evaluate)."""
    cards = treys_card_list(hole_key)
    if len(cards) < 2:
        return 0.5
    r1 = Card.get_rank_int(cards[0])
    r2 = Card.get_rank_int(cards[1])
    high = max(r1, r2)
    pair_bonus = 0.25 if r1 == r2 else 0.0
    return min(1.0, (high / 12.0) * 0.75 + pair_bonus)


def hand_strength_norm(hole_key: str, board_key: str) -> float:
    if len(hole_key) < 4:
        return 0.5
    hand = treys_card_list(hole_key)
    board = treys_card_list(board_key) if board_key else []
    if len(board) + len(hand) < 5:
        return _preflop_strength_norm(hole_key)
    rank = EVALUATOR.evaluate(board, hand)
    return 1.0 - (float(rank) / MAX_HAND_RANK)


def aggregate_hand_features(decisions: list[dict]) -> list[float]:
    """Public-only features: position, street aggression, action mix, pot context."""
    btn = 1.0 if any(d.get("position") == "BTN" for d in decisions) else 0.0
    fold_c = call_c = raise_c = 0.0
    street_raise = {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0}
    pot_ratios: list[float] = []
    last_street = 0.0

    for d in decisions:
        act = str(d.get("action") or "").lower()
        street = STREET_ORDER.get(str(d.get("street") or ""), 0)
        last_street = float(street)
        pot = float(d.get("pot_chips") or 0)
        if act == "fold":
            fold_c += 1.0
        elif act in ("call", "check"):
            call_c += 1.0
        elif act in ACTION_RAISE:
            raise_c += 1.0
            street_raise[street] = 1.0
        if pot > 0 and d.get("amount") is not None:
            try:
                pot_ratios.append(float(d["amount"]) / pot)
            except (TypeError, ValueError):
                pass

    n = max(len(decisions), 1)
    avg_pot_ratio = sum(pot_ratios) / len(pot_ratios) if pot_ratios else 0.0
    return [
        btn,
        float(len(decisions)),
        street_raise[0],
        street_raise[1],
        street_raise[2],
        street_raise[3],
        fold_c / n,
        call_c / n,
        raise_c / n,
        avg_pot_ratio,
        last_street,
    ]


FEATURE_NAMES = [
    "btn",
    "n_decisions",
    "preflop_aggr",
    "flop_aggr",
    "turn_aggr",
    "river_aggr",
    "fold_rate",
    "call_rate",
    "raise_rate",
    "avg_pot_ratio",
    "last_street",
]


def rank_auc(labels: list[float], scores: list[float]) -> float:
    pairs = 0.0
    correct = 0.0
    for i, yi in enumerate(labels):
        for j, yj in enumerate(labels):
            if yi > yj:
                pairs += 1.0
                si, sj = scores[i], scores[j]
                if si > sj:
                    correct += 1.0
                elif si == sj:
                    correct += 0.5
    if pairs <= 0:
        return 0.5
    return correct / pairs


def _sigmoid(z: float) -> float:
    if z >= 0:
        ez = math.exp(-z)
        return 1.0 / (1.0 + ez)
    ez = math.exp(z)
    return ez / (1.0 + ez)


def train_logistic(
    x: list[list[float]],
    y: list[float],
    *,
    epochs: int = 300,
    lr: float = 0.05,
    seed: int = 0,
) -> tuple[list[float], float]:
    rng = random.Random(seed)
    n_feat = len(x[0])
    w = [rng.uniform(-0.01, 0.01) for _ in range(n_feat)]
    b = 0.0
    for _ in range(epochs):
        for xi, yi in zip(x, y):
            z = b + sum(wj * xij for wj, xij in zip(w, xi))
            err = _sigmoid(z) - yi
            for j in range(n_feat):
                w[j] -= lr * err * xi[j]
            b -= lr * err
    return w, b


def predict_scores(x: list[list[float]], w: list[float], b: float) -> list[float]:
    out: list[float] = []
    for xi in x:
        z = b + sum(wj * xij for wj, xij in zip(w, xi))
        out.append(_sigmoid(z))
    return out


def baseline_scores(x: list[list[float]]) -> list[float]:
    """Position-only baseline: BTN flag + normalized decision count."""
    out: list[float] = []
    for xi in x:
        btn = xi[0]
        n_dec = xi[1]
        out.append(0.35 * btn + 0.05 * min(n_dec, 6.0))
    return out


def extract_probe_samples(trajectory: list[dict]) -> list[dict[str, Any]]:
    by_hand: dict[int, list[dict]] = {}
    results: dict[int, dict] = {}
    for row in trajectory:
        hid = row.get("hand_id")
        if hid is None:
            continue
        if row.get("record_type") == "decision":
            by_hand.setdefault(int(hid), []).append(row)
        elif row.get("record_type") == "hand_result":
            results[int(hid)] = row

    samples: list[dict[str, Any]] = []
    for hid, decisions in by_hand.items():
        hr = results.get(hid)
        if not hr:
            continue
        villain_key = str(hr.get("villain_hole_key") or "")
        board_key = str(hr.get("board_key") or "")
        if len(villain_key) < 4:
            continue
        strength = hand_strength_norm(villain_key, board_key)
        feats = aggregate_hand_features(decisions)
        samples.append({
            "hand_id": hid,
            "features": feats,
            "villain_strength": strength,
            "villain_hole_key": villain_key,
            "board_key": board_key,
        })
    return samples


def run_probe(
    decide_fn: Callable,
    *,
    hands: int = 500,
    starting_stack: int = DEFAULT_STACK,
    small_blind: int = DEFAULT_SMALL_BLIND,
    big_blind: int = DEFAULT_BIG_BLIND,
    seed: int = 42,
    opponent_label: str = "tight",
) -> dict[str, Any]:
    rng = random.Random(seed)
    trajectory: list[dict] = []
    opponents = _opponents_for_selfplay(2, opponent_label)

    for hand_id in range(1, hands + 1):
        hero_idx = rng.randint(0, 1)
        play_one_hand(
            decide_fn,
            opponents,
            starting_stack,
            small_blind,
            big_blind,
            hand_id,
            hero_idx=hero_idx,
            trajectory=trajectory,
        )

    samples = extract_probe_samples(trajectory)
    if len(samples) < 20:
        return {
            "hands_requested": hands,
            "labeled_hands": len(samples),
            "error": "insufficient labeled showdown hands",
        }

    x = [s["features"] for s in samples]
    y = [s["villain_strength"] for s in samples]
    baseline = baseline_scores(x)
    baseline_auc = rank_auc(y, baseline)

    w, b = train_logistic(x, y, seed=seed)
    probe_scores = predict_scores(x, w, b)
    probe_auc = rank_auc(y, probe_scores)

    return {
        "hands_requested": hands,
        "labeled_hands": len(samples),
        "feature_names": FEATURE_NAMES,
        "baseline_auc": round(baseline_auc, 4),
        "probe_auc": round(probe_auc, 4),
        "auc_delta": round(probe_auc - baseline_auc, 4),
        "beats_baseline": probe_auc > baseline_auc + 0.02,
        "weights": [round(v, 6) for v in w],
        "bias": round(b, 6),
    }


def main(argv: Optional[list[str]] = None) -> int:
    p = argparse.ArgumentParser(description="K129 IRumAI HU linear range probe")
    p.add_argument("--decide", type=str, default="examples/cemini_decide.py")
    p.add_argument("--hands", type=int, default=500)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--opponent", type=str, default="tight")
    p.add_argument("--json-out", type=str, default="")
    args = p.parse_args(argv)

    decide_path = Path(args.decide)
    if not decide_path.is_file():
        print(f"decide module not found: {decide_path}", file=sys.stderr)
        return 1

    decide_fn = _load_decide_from_path(str(decide_path))
    report = run_probe(
        decide_fn,
        hands=args.hands,
        seed=args.seed,
        opponent_label=args.opponent,
    )
    text = json.dumps(report, indent=2)
    print(text)
    if args.json_out:
        Path(args.json_out).write_text(text + "\n", encoding="utf-8")
    return 0 if "error" not in report else 1


if __name__ == "__main__":
    raise SystemExit(main())
