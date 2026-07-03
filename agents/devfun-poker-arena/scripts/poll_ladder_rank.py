#!/usr/bin/env python3
"""Leaderboard rank for cemini_wiki_poker on the pinned heads-up ladder comp."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "examples"))

from arena_client import ArenaClient, DEFAULT_BASE, load_or_register  # noqa: E402
from export_competition_hands import fetch_leaderboard, leaderboard_adjusted_bb100  # noqa: E402

PIN_PATH = ROOT / "config" / "researcher_sandbox_submit.pin.json"
HERO = "cemini_wiki_poker"
DEFAULT_COMP = "cmr3n8tft01nilecm1u5jlny7"


def _read_pin() -> dict:
    if not PIN_PATH.is_file():
        return {}
    try:
        return json.loads(PIN_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def _claim_status(client: ArenaClient) -> dict:
    try:
        return client.get("/auth/claim/status") or {}
    except Exception:
        return {}


def main() -> int:
    pin = _read_pin()
    comp = pin.get("competitionId") or DEFAULT_COMP
    active_sub = pin.get("activeSubmissionId")

    c = ArenaClient(DEFAULT_BASE)
    load_or_register(c, HERO, "c", "q")
    lb = fetch_leaderboard(c, comp)
    hero_rank = None
    hero_row = None
    for i, row in enumerate(lb, 1):
        agent = row.get("agent") or {}
        if (agent.get("handle") or "").lower() == HERO:
            hero_rank = i
            hero_row = row
            break

    claim = _claim_status(c)
    out: dict = {
        "competitionId": comp,
        "competitionName": "[poker] heads-up ladder S1",
        "leaderboardTotal": len(lb),
        "heroListed": hero_row is not None,
        "heroRank": hero_rank,
        "hero": None,
        "top15": [],
        "claim": {
            "claimed": claim.get("claimed"),
            "xHandle": claim.get("xHandle"),
            "status": claim.get("status"),
        },
        "activeSubmissionId": active_sub,
        "pvp": None,
    }
    if hero_row:
        a = hero_row.get("agent") or {}
        out["hero"] = {
            "handle": a.get("handle"),
            "trueskillScore": hero_row.get("trueskillScore") or hero_row.get("score"),
            "trueskillMu": hero_row.get("trueskillMu"),
            "trueskillSigma": hero_row.get("trueskillSigma"),
            "adjustedBbPer100": leaderboard_adjusted_bb100(hero_row),
            "completedHands": (
                hero_row.get("completedHands")
                or hero_row.get("graduateCount")
                or hero_row.get("hands")
            ),
            "chips": hero_row.get("chips"),
        }
    for i, row in enumerate(lb[:15], 1):
        a = row.get("agent") or {}
        out["top15"].append(
            {
                "rank": i,
                "handle": a.get("handle"),
                "trueskillScore": row.get("trueskillScore") or row.get("score"),
                "hands": row.get("completedHands") or row.get("graduateCount"),
                "adjustedBbPer100": leaderboard_adjusted_bb100(row),
            }
        )

    if active_sub:
        try:
            from submit_sandbox_pvp import poll_submission  # noqa: WPS433

            polled = poll_submission(active_sub)
            pvp = polled.get("pvp") or {}
            out["pvp"] = {
                "status": pvp.get("status"),
                "completedHands": pvp.get("completedHands"),
                "trueskillScore": pvp.get("trueskillScore"),
                "adjustedBbPer100": pvp.get("adjustedBbPer100"),
                "continuous": pvp.get("continuous"),
            }
        except Exception as exc:
            out["pvp"] = {"error": str(exc)}

    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
