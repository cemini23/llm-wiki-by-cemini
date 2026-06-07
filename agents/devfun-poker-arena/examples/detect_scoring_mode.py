#!/usr/bin/env python3
"""Detect playground scoring mode (chips vs adjustedBbPer100 / V2/V3)."""
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

from arena_client import ArenaClient, CREDS_PATH, DEFAULT_BASE  # noqa: E402


def detect(client: ArenaClient, competition_id: str) -> dict:
    out: dict = {
        "competition_id": competition_id,
        "scoring_mode": "unknown",
        "adjusted_bb100_visible": False,
        "participant_fields": [],
        "match_fields": [],
        "recommendation": "",
    }
    try:
        body = client.get(f"/texas/benchmark/status?competitionId={competition_id}")
    except Exception as e:
        out["error"] = str(e)
        out["recommendation"] = "Could not reach status API — assume chip rank until verified."
        return out

    participant = body.get("participant") or {}
    match = body.get("match") or {}
    out["participant_fields"] = sorted(participant.keys()) if isinstance(participant, dict) else []
    out["match_fields"] = sorted(match.keys()) if isinstance(match, dict) else []

    for key in ("adjustedBbPer100", "rawChipDelta", "allInEvBbPer100", "aivatBbPer100"):
        if isinstance(match, dict) and key in match:
            out["adjusted_bb100_visible"] = True
            out["scoring_mode"] = "eval_style"
            out[key] = match.get(key)
            break
        if isinstance(participant, dict) and key in participant:
            out["adjusted_bb100_visible"] = True
            out["scoring_mode"] = "eval_style"
            out[key] = participant.get(key)
            break

    if out["scoring_mode"] != "eval_style":
        out["scoring_mode"] = "chip_accumulation"
        out["total_chips"] = participant.get("totalChips")
        out["total_hands"] = participant.get("totalHands")
        out["recommendation"] = (
            "Playground ranks on totalChips — preserve first_protect; "
            "track participant totals; do not trust chip-proxy as EV bb/100."
        )
    else:
        out["recommendation"] = (
            "V2/V3-style metrics visible — optimize for adjustedBbPer100; "
            "run competition_metrics_report after each export."
        )
    return out


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Detect arena scoring mode for a competition")
    p.add_argument("--match", default=None, help="competitionId")
    p.add_argument("--json-out", type=Path, default=None)
    args = p.parse_args(argv)

    load_dotenv()
    api_key = None
    if CREDS_PATH.exists():
        api_key = json.loads(CREDS_PATH.read_text()).get("apiKey")
    api_key = api_key or os.environ.get("ARENA_API_KEY")
    if not api_key:
        print("ERROR: need API key", file=sys.stderr)
        return 2

    competition_id = (
        args.match
        or os.environ.get("ARENA_LOBBY_COMPETITION_ID")
        or "cmpy2qy65002ud9ej6b7jjq0l"
    )
    client = ArenaClient(os.environ.get("ARENA_API_BASE", DEFAULT_BASE), api_key=api_key)
    try:
        report = detect(client, competition_id)
    finally:
        client.close()

    print(json.dumps(report, indent=2, sort_keys=True))
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
