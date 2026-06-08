"""Periodic playground metrics log — chipDelta from replays + leaderboard snapshot."""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

_EXAMPLES = Path(__file__).resolve().parent
_AGENT_ROOT = _EXAMPLES.parent
_DEFAULT_PATH = _AGENT_ROOT / "reports" / "hl-loop" / "playground_timeseries.jsonl"


def timeseries_path() -> Path:
    raw = os.environ.get("CEMINI_PLAYGROUND_TIMESERIES", "").strip()
    return Path(raw) if raw else _DEFAULT_PATH


def append_playground_snapshot(
    client: Any,
    *,
    agent_id: str,
    competition_id: str,
    qual_status: Optional[dict] = None,
    hands_played: int = 0,
) -> None:
    """Fetch replays (chipDelta cap 50) + qual rank; append one JSONL row."""
    if os.environ.get("CEMINI_PLAYGROUND_TIMESERIES", "1").strip().lower() in (
        "0",
        "false",
        "no",
        "off",
    ):
        return

    from analyze import _fetch_replays  # noqa: WPS433 — shared API helper

    replays = _fetch_replays(client, agent_id, limit=50)
    deltas = list(replays.values())
    chip_delta_sum = sum(deltas) if deltas else None
    chip_delta_n = len(deltas)

    st = qual_status or {}
    row: dict[str, Any] = {
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "competition_id": competition_id,
        "agent_id": agent_id,
        "hands_played_session": hands_played,
        "rank": st.get("rank"),
        "chips": st.get("chips"),
        "buffer_chips": st.get("buffer_chips"),
        "qualification_protect": st.get("qualification_protect"),
        "first_protect": st.get("first_protect"),
        "replay_chip_delta_sum": chip_delta_sum,
        "replay_chip_delta_n": chip_delta_n,
        "replay_chip_delta_avg": (
            round(chip_delta_sum / chip_delta_n, 2) if chip_delta_n and chip_delta_sum is not None else None
        ),
    }
    path = timeseries_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, separators=(",", ":")) + "\n")
