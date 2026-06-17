#!/usr/bin/env python3
"""Tournament vs playground priority — prod guard helper."""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from arena_client import ArenaClient, DEFAULT_BASE, load_or_register  # noqa: E402


def _load_env() -> None:
    load_dotenv(_EXAMPLES.parent / ".env")


def competition_status(client: ArenaClient, competition_id: str) -> str:
    body = client.get("/competition/list-all")
    for row in body.get("data") or []:
        if row.get("id") == competition_id:
            return str(row.get("status") or "").strip()
    return ""


def participant_chip_state(client: ArenaClient, competition_id: str) -> dict:
    try:
        st = client.get(f"/texas/benchmark/status?competitionId={competition_id}")
        p = st.get("participant") or {}
        return {
            "chip_state": str(p.get("chipState") or ""),
            "total_chips": int(p.get("totalChips") or 0),
            "total_hands": int(p.get("totalHands") or 0),
        }
    except Exception:
        return {"chip_state": "", "total_chips": 0, "total_hands": 0}


def main() -> int:
    _load_env()
    p = argparse.ArgumentParser(description="Tournament priority guard status")
    p.add_argument("--tournament-comp", default=os.environ.get("S2_TOURNAMENT_COMP", "cmqggiv9k37am11ydmppz466e"))
    p.add_argument("--playground-comp", default=os.environ.get("S3_PLAYGROUND_COMP", "cmqf827h30u7dfca3x2aqvzjv"))
    p.add_argument("--json", action="store_true")
    args = p.parse_args()

    client = ArenaClient(os.environ.get("ARENA_API_BASE", DEFAULT_BASE))
    load_or_register(client, "cemini_wiki_poker", "c", "q")
    try:
        t_status = competition_status(client, args.tournament_comp)
        p_status = competition_status(client, args.playground_comp)
        t_part = participant_chip_state(client, args.tournament_comp)
        t_live = t_status == "Active"
        t_busted = t_part.get("chip_state") == "busted"
        out = {
            "tournament_comp": args.tournament_comp,
            "tournament_status": t_status,
            "tournament_participant": t_part,
            "playground_comp": args.playground_comp,
            "playground_status": p_status,
            "pause_playground": t_live and not t_busted,
            "resume_playground": p_status == "Active" and (
                not t_live or t_busted or t_status == "Ended"
            ),
        }
        if args.json:
            print(json.dumps(out))
        else:
            print(
                f"tournament={args.tournament_comp} status={t_status} "
                f"chips={t_part.get('total_chips')} state={t_part.get('chip_state')}"
            )
            print(f"playground={args.playground_comp} status={p_status}")
            print(f"pause_playground={out['pause_playground']} resume_playground={out['resume_playground']}")
        return 0
    finally:
        client.close()


if __name__ == "__main__":
    raise SystemExit(main())
