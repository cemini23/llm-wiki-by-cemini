#!/usr/bin/env python3
"""Fold/check all pending actions for a competition — leave old playground tables."""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
sys.path.insert(0, str(_EXAMPLES))

from agent import _build, _normalize_action_name  # noqa: E402
from arena_client import ArenaClient, ArenaError, CREDS_PATH, DEFAULT_BASE  # noqa: E402


def _load_agent_id() -> str:
    if CREDS_PATH.exists():
        c = json.loads(CREDS_PATH.read_text())
        return str(c.get("agentId") or c.get("id") or "")
    return os.environ.get("ARENA_AGENT_ID", "")


def drain(client: ArenaClient, competition_id: str, *, max_rounds: int = 50) -> int:
    acted = 0
    for _ in range(max_rounds):
        try:
            pending = client.get(
                "/texas/pending-actions",
                params={"competitionId": competition_id},
            )
        except ArenaError as e:
            print(f"[drain] pending failed {competition_id}: {e.status}", file=sys.stderr)
            break
        tables = pending.get("tables") if isinstance(pending, dict) else []
        if not tables:
            break
        for table in tables:
            allowed = table.get("allowedActions") or {}
            available = allowed.get("availableActions") or []
            if allowed.get("canCheck") and "check" in available:
                action = _build("check", None, table, allowed, eq=0.0, po=0.0,
                                msg="drain old comp — check")
            else:
                action = _build("fold", None, table, allowed, eq=0.0, po=1.0,
                                msg="drain old comp — fold")
            action = _normalize_action_name(action)
            try:
                client.post("/texas/action", {"tableId": table["tableId"], **action})
                acted += 1
                print(f"[drain] {competition_id} table={table['tableId']} {action.get('action')}")
            except ArenaError as e:
                print(f"[drain] action error: {e.status}", file=sys.stderr)
    return acted


def main() -> int:
    load_dotenv()
    p = argparse.ArgumentParser(description="Drain pending hands in old competition(s)")
    p.add_argument("competition_ids", nargs="+", help="Competition IDs to drain")
    p.add_argument("--max-rounds", type=int, default=50)
    args = p.parse_args()

    client = ArenaClient(
        os.environ.get("ARENA_API_BASE", DEFAULT_BASE),
        api_key=os.environ.get("ARENA_API_KEY") or None,
    )
    agent_id = _load_agent_id()
    print(f"[drain] agent={agent_id}")
    total = 0
    try:
        for cid in args.competition_ids:
            n = drain(client, cid, max_rounds=args.max_rounds)
            print(f"[drain] {cid}: {n} actions")
            total += n
    finally:
        client.close()
    print(f"[drain] done total={total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
