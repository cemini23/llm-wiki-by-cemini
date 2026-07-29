"""K191/K193 turn-aware street scores (ToolVerse credit-assignment pattern).

Per-street / per-decision tallies for trajectory diagnosis — not only session
PnL. Advisory eval helper; never a hard submit gate or decide() path.

See ``references/turn-street-scores.md`` and
``references/expert-rubric-checklist.md``.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any, Iterable, Mapping, Sequence

STREETS: tuple[str, ...] = ("Preflop", "Flop", "Turn", "River")
_STREET_ALIASES: dict[str, str] = {
    "preflop": "Preflop",
    "pre": "Preflop",
    "flop": "Flop",
    "turn": "Turn",
    "river": "River",
    "pre-flop": "Preflop",
}

_FOLD = frozenset({"fold"})
_PASSIVE = frozenset({"check", "call"})
_AGGRESSIVE = frozenset({"bet", "raise", "all-in", "allin", "all_in"})


def normalize_street(raw: Any) -> str:
    if raw is None:
        return "unknown"
    s = str(raw).strip()
    if not s:
        return "unknown"
    if s in STREETS:
        return s
    return _STREET_ALIASES.get(s.lower(), s if s[:1].isupper() else s.capitalize())


def classify_action(action: Any) -> str:
    a = str(action or "").strip().lower().replace(" ", "-")
    if a in _FOLD or a == "fold":
        return "fold"
    if a in _PASSIVE:
        return "passive"
    if a in _AGGRESSIVE or a.replace("-", "_") in {"all_in", "allin"}:
        return "aggressive"
    if a in {"", "none", "null"}:
        return "unknown"
    return "other"


def classify_facing(record: Mapping[str, Any]) -> str:
    """Whether hero faces a bet/raise (to_call > 0) or free action."""
    for key in ("facing", "facing_action", "facing_type"):
        raw = record.get(key)
        if raw is None:
            continue
        s = str(raw).strip().lower()
        if s in {"check", "free", "no_bet", "unopened"}:
            return "check"
        if s in {"bet", "raise", "all-in", "allin", "shove", "facing_bet"}:
            return "bet" if s in {"bet", "facing_bet"} else "raise"
    call = record.get("call_chips")
    if call is None:
        call = record.get("to_call")
    if call is None:
        call = record.get("call")
    try:
        call_f = float(call) if call is not None else None
    except (TypeError, ValueError):
        call_f = None
    if call_f is not None:
        if call_f <= 0:
            return "check"
        # Optional: distinguish bet vs raise via prior commits if present.
        raised = record.get("facing_raise") or record.get("is_raise")
        if raised in (True, 1, "1", "true", "yes"):
            return "raise"
        return "bet"
    allowed = record.get("allowed") or record.get("legal_actions") or {}
    if isinstance(allowed, Mapping):
        cc = allowed.get("call_chips")
        if cc is not None:
            try:
                return "check" if float(cc) <= 0 else "bet"
            except (TypeError, ValueError):
                pass
    return "unknown"


def _optional_success(record: Mapping[str, Any]) -> bool | None:
    if "success" in record and record["success"] is not None:
        v = record["success"]
        if isinstance(v, bool):
            return v
        if str(v).strip().lower() in {"1", "true", "yes", "ok", "pass"}:
            return True
        if str(v).strip().lower() in {"0", "false", "no", "fail"}:
            return False
    if "won" in record and record["won"] is not None:
        return bool(record["won"])
    delta = record.get("chip_delta")
    if delta is not None:
        try:
            return float(delta) > 0
        except (TypeError, ValueError):
            pass
    return None


def score_decision_street(record: Mapping[str, Any]) -> dict[str, Any]:
    """Score one decision row for street-level credit assignment.

    Returns street, facing class, action class, and optional success flag.
    """
    street = normalize_street(record.get("street"))
    action_raw = record.get("action")
    action_class = classify_action(action_raw)
    facing = classify_facing(record)
    success = _optional_success(record)
    out: dict[str, Any] = {
        "schema": "devfun.turn_street_score.v1",
        "street": street,
        "facing": facing,
        "action": str(action_raw or "").lower() or None,
        "action_class": action_class,
        "success": success,
        "hand_id": record.get("hand_id") or record.get("handId"),
        "position": record.get("position"),
    }
    return out


def aggregate_turn_scores(
    trajectory_rows: Sequence[Mapping[str, Any]] | Iterable[Mapping[str, Any]],
) -> dict[str, Any]:
    """Aggregate per-street tallies from trajectory rows (not only session PnL).

    Accepts selfplay JSONL-style rows. Decision rows preferred
    (``record_type == "decision"``); bare decision dicts without
    ``record_type`` are also accepted.
    """
    rows = list(trajectory_rows)
    decisions: list[Mapping[str, Any]] = []
    for r in rows:
        if not isinstance(r, Mapping):
            continue
        rt = r.get("record_type")
        if rt is None or rt == "decision":
            if r.get("action") is not None or r.get("street") is not None:
                decisions.append(r)

    by_street: dict[str, dict[str, Any]] = {}
    for street in STREETS:
        by_street[street] = {
            "n": 0,
            "action_class_counts": Counter(),
            "facing_counts": Counter(),
            "success_n": 0,
            "success_known": 0,
        }

    unknown_street = 0
    scored: list[dict[str, Any]] = []
    for d in decisions:
        sc = score_decision_street(d)
        scored.append(sc)
        street = sc["street"]
        bucket = by_street.get(street)
        if bucket is None:
            unknown_street += 1
            continue
        bucket["n"] += 1
        bucket["action_class_counts"][sc["action_class"]] += 1
        bucket["facing_counts"][sc["facing"]] += 1
        if sc["success"] is not None:
            bucket["success_known"] += 1
            if sc["success"]:
                bucket["success_n"] += 1

    streets_out: dict[str, Any] = {}
    for street, bucket in by_street.items():
        n = int(bucket["n"])
        sk = int(bucket["success_known"])
        streets_out[street] = {
            "n": n,
            "action_class_counts": dict(bucket["action_class_counts"]),
            "facing_counts": dict(bucket["facing_counts"]),
            "success_rate": (
                round(bucket["success_n"] / sk, 4) if sk > 0 else None
            ),
            "success_known": sk,
        }

    total = sum(int(v["n"]) for v in streets_out.values())
    return {
        "schema": "devfun.turn_street_scores.v1",
        "advisory_only": True,
        "decision_count": total,
        "unknown_street_count": unknown_street,
        "by_street": streets_out,
        "k": "K191/K193",
        "reference": "references/turn-street-scores.md",
    }


def turn_street_scores_brief_section(summary: Mapping[str, Any]) -> str:
    """Markdown snippet for HL / Discord briefs."""
    by = summary.get("by_street") or {}
    lines = [
        "### Turn-street scores (K191 advisory)",
        "",
        "| Street | n | success_rate | top action_class |",
        "|--------|---|--------------|------------------|",
    ]
    for street in STREETS:
        row = by.get(street) or {}
        n = row.get("n", 0)
        sr = row.get("success_rate")
        sr_s = "—" if sr is None else f"{sr:.2%}"
        counts = row.get("action_class_counts") or {}
        top = max(counts, key=counts.get) if counts else "—"
        lines.append(f"| {street} | {n} | {sr_s} | {top} |")
    lines.append("")
    lines.append(
        f"_decisions={summary.get('decision_count', 0)} · advisory_only · "
        "not a submit gate_"
    )
    return "\n".join(lines)
