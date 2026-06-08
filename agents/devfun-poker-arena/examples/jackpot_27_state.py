"""Session state for S2 27o jackpot hunt — separate from prod cemini_decide."""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_AGENT_ROOT = Path(__file__).resolve().parent.parent
_INSTANCE = os.environ.get("JACKPOT_27_INSTANCE", "default").strip() or "default"
_REPORT_DIR = _AGENT_ROOT / "reports" / "jackpot-27" / _INSTANCE

_attempts: int = 0
_hand_hunting: str | None = None


def max_attempts() -> int:
    raw = os.environ.get("JACKPOT_27_MAX_ATTEMPTS", "").strip()
    if raw:
        return int(raw)
    phase = os.environ.get("JACKPOT_27_PHASE", "").strip().lower()
    aggressive = os.environ.get("JACKPOT_27_AGGRESSIVE", "0").strip().lower()
    if phase in ("early", "jackpot", "hunt") or aggressive in ("1", "true", "yes", "on"):
        return 10
    return 5


def reset_session() -> None:
    global _attempts, _hand_hunting
    _attempts = 0
    _hand_hunting = None


def attempts_used() -> int:
    return _attempts


def begin_hunt(hand_key: str) -> bool:
    """Mark hunt start; return False if session cap already hit."""
    global _attempts, _hand_hunting
    if _attempts >= max_attempts():
        return False
    if _hand_hunting == hand_key:
        return True
    _hand_hunting = hand_key
    _attempts += 1
    return True


def hand_key(table: dict, hole: list[str]) -> str:
    tid = table.get("tableId") or table.get("id") or "?"
    return f"{tid}:{'-'.join(hole)}"


def log_dealt(table: dict, hole: list[str], *, hand_class: str, position: str) -> None:
    _REPORT_DIR.mkdir(parents=True, exist_ok=True)
    row = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "hand_class": hand_class,
        "position": position,
        "tableId": table.get("tableId") or table.get("id"),
        "competitionId": table.get("competitionId"),
        "hole": hole,
    }
    path = _REPORT_DIR / "dealt.jsonl"
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row) + "\n")


def log_action(table: dict, *, action: str, phase: str, notes: str = "") -> None:
    _REPORT_DIR.mkdir(parents=True, exist_ok=True)
    row: dict[str, Any] = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "action": action,
        "phase": phase,
        "tableId": table.get("tableId") or table.get("id"),
        "notes": notes,
        "attempts_used": _attempts,
    }
    path = _REPORT_DIR / "actions.jsonl"
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row) + "\n")
