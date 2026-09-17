#!/usr/bin/env python3
"""Consume at most one Tournament sponsored 0.01 MON rebuy ticket.

LIVE: 0.01 MON only. Refuses ≥1 MON. Does not sit a second ticket in this process.

Usage (prod, after rsync; lobby stopped or CEMINI_SPONSORED_TICKET_REBUY=1):

  cd /opt/devfun-poker-arena && ./venv/bin/python scripts/t14_sponsored_rebuy_once.py
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

_AGENT = Path(__file__).resolve().parent.parent
_EXAMPLES = _AGENT / "examples"
sys.path.insert(0, str(_EXAMPLES))

from dotenv import load_dotenv  # noqa: E402

load_dotenv(_AGENT / ".env", override=True)

from arena_client import (  # noqa: E402
    ArenaClient,
    DEFAULT_BASE,
    CREDS_PATH,
    load_state,
    save_state,
)
from run_cemini_lobby import _try_rebuy  # noqa: E402

T14 = "cmt03vxf03y76xjshadwhbcpi"


def _tickets(client: ArenaClient) -> list[dict]:
    body = client.get("/agent/sponsor-tickets")
    raw = body.get("tickets") if isinstance(body, dict) else body
    return [t for t in (raw or []) if isinstance(t, dict)]


def _t14_available(tickets: list[dict]) -> list[dict]:
    out = []
    for t in tickets:
        if str(t.get("status") or "").lower() != "available":
            continue
        if str(t.get("seasonId") or "") == T14 or int(t.get("seasonNumber") or 0) == 14:
            out.append(t)
    return out


def _hero_chips(client: ArenaClient, competition_id: str) -> int | None:
    me = client.get("/agent/me")
    boards = me.get("leaderboard") if isinstance(me, dict) else None
    if not isinstance(boards, list):
        return None
    for row in boards:
        if not isinstance(row, dict):
            continue
        if str(row.get("arenaId") or row.get("competitionId") or "") != competition_id:
            continue
        try:
            return int(row.get("totalScore") or row.get("score") or 0)
        except (TypeError, ValueError):
            return None
    return None


def main() -> int:
    os.environ.setdefault("CEMINI_SPONSORED_TICKET_REBUY", "1")
    os.environ.setdefault("CEMINI_MAX_SPONSORED_REBUYS", "1")
    competition_id = (
        os.environ.get("ARENA_LOBBY_COMPETITION_ID") or T14
    ).strip()
    if competition_id != T14:
        print(
            f"ERROR: lobby comp {competition_id} is not T14 {T14} — refusing",
            file=sys.stderr,
        )
        return 2

    key = os.environ.get("ARENA_API_KEY")
    if not key and Path(CREDS_PATH).is_file():
        key = json.loads(Path(CREDS_PATH).read_text()).get("apiKey")
    client = ArenaClient(os.environ.get("ARENA_API_BASE", DEFAULT_BASE), api_key=key)

    state = load_state()
    used = int(state.get("sponsored_ticket_rebuy_used") or 0)
    chips = _hero_chips(client, competition_id)
    tickets = _tickets(client)
    avail = _t14_available(tickets)
    print(f"t14_available_before={len(avail)} chips={chips} sponsored_used={used}")
    if chips is not None and chips > 0:
        print("already have chips — no-op (will not spend a second ticket)")
        return 0
    if used >= 1:
        print("sponsored_ticket_rebuy_used already set — no-op")
        return 0
    if not avail:
        print("ERROR: no T14 available tickets", file=sys.stderr)
        return 2

    ok = _try_rebuy(client, competition_id, state, save_state)
    tickets2 = _tickets(client)
    avail2 = _t14_available(tickets2)
    chips2 = _hero_chips(client, competition_id)
    print(
        f"rebuy_ok={ok} t14_available_after={len(avail2)} "
        f"chips={chips2} sponsored_used={state.get('sponsored_ticket_rebuy_used')}"
    )
    if ok and chips2 is not None and chips2 > 0:
        return 0
    if ok:
        print("WARN: rebuy reported ok but chips still 0", file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
