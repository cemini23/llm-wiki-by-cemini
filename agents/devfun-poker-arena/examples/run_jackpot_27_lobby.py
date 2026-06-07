#!/usr/bin/env python3
"""Playground lobby loop for S2 jackpot satellite (jackpot_27_decide).

Uses separate credentials — never prod `.arena-credentials`.
"""
from __future__ import annotations

import argparse
import json
import os
import random
import sys
import time
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

import jackpot_27_decide  # noqa: E402
import jackpot_27_safety  # noqa: E402
from agent import _normalize_action_name, _build  # noqa: E402
from arena_client import (  # noqa: E402
    ArenaClient,
    ArenaError,
    DEFAULT_BASE,
    load_or_register,
)
from output_sanitize import maybe_sanitize_action  # noqa: E402

POLL_INTERVAL = 2.0


def _join(client: ArenaClient, competition_id: str) -> dict:
    return client.post("/texas/join", {"competitionId": competition_id})


def _pending(client: ArenaClient, competition_id: str) -> dict:
    return client.get("/texas/pending-actions", params={"competitionId": competition_id})


def run_lobby(args: argparse.Namespace) -> int:
    load_dotenv()
    os.environ.setdefault("ARENA_CREDENTIALS_FILE", ".arena-credentials.jackpot-27")
    client = ArenaClient(
        os.environ.get("ARENA_API_BASE", DEFAULT_BASE),
        api_key=os.environ.get("ARENA_API_KEY") or None,
    )
    competition_id = (
        args.competition_id
        or os.environ.get("JACKPOT_27_COMPETITION_ID")
        or os.environ.get("ARENA_LOBBY_COMPETITION_ID")
        or ""
    )

    if not jackpot_27_safety.join_enabled():
        print(
            "[jackpot-27] JOIN disabled (JACKPOT_27_JOIN_ENABLED=0) — "
            "idle to avoid Playground anti-cheat / collusion flags",
            file=sys.stderr,
        )
        while True:
            time.sleep(3600)

    if not competition_id:
        print("[jackpot-27] ERROR: set --competition-id or JACKPOT_27_COMPETITION_ID", file=sys.stderr)
        return 1

    hands_acted = 0
    rng = random.Random()
    last_join_at = 0.0

    creds = load_or_register(client, args.handle, args.name, args.quote)
    print(f"[jackpot-27] agent={creds.get('agentId')} competition={competition_id}")

    try:
        if not args.skip_join:
            try:
                print(f"[jackpot-27] join: {_join(client, competition_id)}")
                last_join_at = time.time()
            except ArenaError as e:
                print(f"[jackpot-27] initial join: {e.status} {e.body}", file=sys.stderr)

        while True:
            try:
                pending = _pending(client, competition_id)
            except ArenaError as e:
                print(f"[jackpot-27] pending error: {e}", file=sys.stderr)
                time.sleep(POLL_INTERVAL)
                continue

            tables = pending.get("tables") if isinstance(pending, dict) else []
            if not isinstance(tables, list):
                tables = []
            tables = sorted(tables, key=lambda t: (t.get("actionDeadlineAt") or 0))

            if tables:
                table = tables[0]
                if not table.get("competitionId"):
                    table = {**table, "competitionId": competition_id}
                self_agent_id = str(creds.get("agentId") or "")
                if jackpot_27_safety.table_has_blocked_agent(
                    table, self_agent_id=self_agent_id,
                ):
                    siblings = jackpot_27_safety.sibling_seat_labels(
                        table, self_agent_id=self_agent_id,
                    )
                    print(
                        f"[jackpot-27] sibling/qual at table — passive fold only: {siblings}",
                        file=sys.stderr,
                    )
                    allowed = table.get("allowedActions") or {}
                    available = allowed.get("availableActions") or []
                    if allowed.get("canCheck") and "check" in available:
                        action = _build(
                            "check", None, table, allowed, eq=0.0, po=0.0,
                            msg="jp: sibling table — check",
                        )
                    else:
                        action = _build(
                            "fold", None, table, allowed, eq=0.0, po=1.0,
                            msg="jp: sibling table — fold",
                        )
                else:
                    deadline_ms = table.get("actionDeadlineAt") or 0
                    deadline_s = (
                        max(0.0, (deadline_ms / 1000.0) - time.time()) if deadline_ms else 10.0
                    )
                    ctx = jackpot_27_decide.retrieve_solver_context(table)
                    action = jackpot_27_decide.decide(
                        table, deadline_s=deadline_s, research_context=ctx,
                    )
                action = _normalize_action_name(action)
                action = maybe_sanitize_action(action)
                payload = {"tableId": table["tableId"], **action}
                try:
                    client.post("/texas/action", payload)
                    hands_acted += 1
                    print(f"[jackpot-27] action={action.get('action')} total={hands_acted}")
                except ArenaError as e:
                    print(f"[jackpot-27] action error: {e}", file=sys.stderr)

            if args.max_actions and hands_acted >= args.max_actions:
                print(f"[jackpot-27] --max-actions={args.max_actions} done")
                return 0

            if not tables and (time.time() - last_join_at) > 30:
                try:
                    _join(client, competition_id)
                    last_join_at = time.time()
                except ArenaError:
                    pass
            time.sleep(POLL_INTERVAL + rng.uniform(-0.3, 0.3))
    finally:
        client.close()


def main(argv: Optional[list[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Jackpot 27o satellite lobby loop")
    p.add_argument("--competition-id", default=None)
    p.add_argument("--max-actions", type=int, default=0)
    p.add_argument("--skip-join", action="store_true")
    p.add_argument("--handle", default=os.environ.get("JACKPOT_27_HANDLE", "arena_table_probe"))
    p.add_argument("--name", default=os.environ.get("JACKPOT_27_NAME", "Table Probe"))
    p.add_argument("--quote", default=os.environ.get("JACKPOT_27_QUOTE", "fold and observe"))
    return run_lobby(p.parse_args(argv))


if __name__ == "__main__":
    raise SystemExit(main())
