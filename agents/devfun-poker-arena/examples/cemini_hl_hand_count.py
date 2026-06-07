#!/usr/bin/env python3
"""Qual bot settled-hand count for HL loop rerun bookkeeping.

Uses leaderboard graduateCount (fast) with /agent/submissions fallback.

Usage:
    uv run python examples/cemini_hl_hand_count.py
    uv run python examples/cemini_hl_hand_count.py --json
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parent
_AGENT_DIR = _EXAMPLES.parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from arena_client import ArenaClient, ArenaError, CREDS_PATH, DEFAULT_BASE  # noqa: E402

try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv(_path: Path) -> bool:  # type: ignore[misc]
        return False

_EXPORT_AGENTS = _AGENT_DIR / "reports" / "exports" / "playground-s1-live" / "agents.jsonl"


def _load_api_key() -> str | None:
    load_dotenv(_AGENT_DIR / ".env")
    raw = os.environ.get("ARENA_API_KEY")
    if raw and raw.strip():
        return raw.strip()
    if CREDS_PATH.is_file():
        data = json.loads(CREDS_PATH.read_text(encoding="utf-8"))
        return data.get("apiKey")
    prod = _AGENT_DIR / ".arena-credentials"
    if prod.is_file():
        data = json.loads(prod.read_text(encoding="utf-8"))
        return data.get("apiKey")
    return None


def _load_agent_id() -> str | None:
    for path in (CREDS_PATH, _AGENT_DIR / ".arena-credentials"):
        if path.is_file():
            data = json.loads(path.read_text(encoding="utf-8"))
            if data.get("agentId"):
                return data["agentId"]
    return None


def _hands_from_export_snapshot(
    *,
    handle: str,
    agent_id: str | None,
) -> dict | None:
    """Read latest export timer snapshot when live leaderboard lookup fails."""
    if not _EXPORT_AGENTS.is_file():
        return None
    try:
        for line in reversed(_EXPORT_AGENTS.read_text(encoding="utf-8").splitlines()):
            if not line.strip():
                continue
            row = json.loads(line)
            if row.get("record_type") != "agent":
                continue
            if agent_id and row.get("agent_id") == agent_id:
                hands = int(row.get("hands") or row.get("total_submissions") or 0)
                return {
                    "hands": hands,
                    "source": "export_snapshot",
                    "rank": row.get("rank"),
                    "chips": row.get("chips"),
                    "agent_id": row.get("agent_id"),
                    "handle": row.get("handle"),
                }
            if row.get("handle") == handle:
                hands = int(row.get("hands") or row.get("total_submissions") or 0)
                return {
                    "hands": hands,
                    "source": "export_snapshot",
                    "rank": row.get("rank"),
                    "chips": row.get("chips"),
                    "agent_id": row.get("agent_id"),
                    "handle": row.get("handle"),
                }
    except Exception:
        return None
    return None


def fetch_hand_count(
    client: ArenaClient,
    competition_id: str,
    *,
    agent_id: str | None = None,
    handle: str | None = None,
    allow_slow: bool = False,
) -> dict:
    handle = handle or os.environ.get("CEMINI_AGENT_HANDLE", "cemini_wiki_poker")
    agent_id = agent_id or _load_agent_id()

    row: dict | None = None
    try:
        from export_competition_hands import fetch_leaderboard  # noqa: WPS433

        for candidate in fetch_leaderboard(client, competition_id):
            ag = candidate.get("agent") or {}
            if agent_id and ag.get("id") == agent_id:
                row = candidate
                break
            if ag.get("handle") == handle:
                row = candidate
                break
    except ArenaError:
        row = None

    if row is None:
        for offset in range(0, 4000, 50):
            try:
                page = client.get(
                    f"/competition/leaderboard?competitionId={competition_id}"
                    f"&limit=50&offset={offset}"
                )
            except ArenaError:
                break
            for candidate in page.get("data") or []:
                ag = candidate.get("agent") or {}
                if agent_id and ag.get("id") == agent_id:
                    row = candidate
                    break
                if ag.get("handle") == handle:
                    row = candidate
                    break
            if row:
                break

    if row:
        hands = int(row.get("graduateCount") or row.get("totalSubmissions") or 0)
        return {
            "hands": hands,
            "source": "leaderboard",
            "rank": row.get("rank"),
            "chips": row.get("totalScore"),
            "agent_id": (row.get("agent") or {}).get("id"),
            "handle": (row.get("agent") or {}).get("handle"),
        }

    snap = _hands_from_export_snapshot(handle=handle, agent_id=agent_id)
    if snap:
        return snap

    if not allow_slow or not agent_id:
        return {"hands": 0, "source": "none", "agent_id": agent_id, "handle": handle}

    from export_competition_hands import fetch_agent_submissions  # noqa: WPS433

    subs = fetch_agent_submissions(client, agent_id, competition_id)
    return {
        "hands": len(subs),
        "source": "submissions",
        "agent_id": agent_id,
        "handle": handle,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Qual bot hand count for HL loop")
    parser.add_argument(
        "--match",
        default=os.environ.get("ARENA_LOBBY_COMPETITION_ID", "cmpy2qy65002ud9ej6b7jjq0l"),
    )
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--slow", action="store_true", help="Fallback to full submissions API")
    args = parser.parse_args()

    key = _load_api_key()
    load_dotenv(_AGENT_DIR / ".env")
    base = os.environ.get("ARENA_API_BASE", DEFAULT_BASE)

    info: dict
    if key:
        client = ArenaClient(base, api_key=key)
        info = fetch_hand_count(client, args.match, allow_slow=args.slow)
        client.close()
    else:
        handle = os.environ.get("CEMINI_AGENT_HANDLE", "cemini_wiki_poker")
        agent_id = _load_agent_id()
        info = _hands_from_export_snapshot(handle=handle, agent_id=agent_id) or {
            "hands": 0,
            "source": "none",
            "agent_id": agent_id,
            "handle": handle,
        }

    if args.json:
        print(json.dumps(info))
    else:
        print(info["hands"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
