"""Periodic playground metrics log — chipDelta from replays + leaderboard snapshot."""
from __future__ import annotations

import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

_EXAMPLES = Path(__file__).resolve().parent
_AGENT_ROOT = _EXAMPLES.parent
_DEFAULT_PATH = _AGENT_ROOT / "reports" / "hl-loop" / "playground_timeseries.jsonl"
_STATE_PATH = _AGENT_ROOT / "reports" / "hl-loop" / "state.json"


def _git_commit_short() -> str | None:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=_AGENT_ROOT,
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
    except Exception:
        return None


def _hl_state_fields() -> dict[str, Any]:
    out: dict[str, Any] = {}
    if not _STATE_PATH.is_file():
        return out
    try:
        data = json.loads(_STATE_PATH.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            if data.get("round") is not None:
                out["hl_round"] = data["round"]
            if data.get("commit"):
                out["commit"] = data["commit"]
    except Exception:
        pass
    return out


def _deploy_grace_active() -> bool | None:
    try:
        from hl_runtime_config import deploy_grace_status

        st = deploy_grace_status()
        return bool(st.get("active"))
    except Exception:
        return None


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
    commit = _git_commit_short()
    grace = _deploy_grace_active()
    row: dict[str, Any] = {
        "schema": "devfun.playground_timeseries.v1",
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
        "deploy_grace_active": grace,
    }
    row.update(_hl_state_fields())
    if commit and "commit" not in row:
        row["commit"] = commit
    agent_version = os.environ.get("AGENT_VERSION", "").strip()
    if agent_version:
        row["agent_version"] = agent_version
    path = timeseries_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, separators=(",", ":")) + "\n")
