#!/usr/bin/env python3
"""One-shot S2 leaderboard rank for cemini_wiki_poker."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "examples"))

from arena_client import ArenaClient, DEFAULT_BASE, load_or_register  # noqa: E402
from export_competition_hands import fetch_leaderboard, leaderboard_adjusted_bb100  # noqa: E402

COMP = "cmr0jmqlt08bi13n8neory9xb"
HERO = "cemini_wiki_poker"


def main() -> int:
    c = ArenaClient(DEFAULT_BASE)
    load_or_register(c, HERO, "c", "q")
    lb = fetch_leaderboard(c, COMP)
    hero_rank = None
    hero_row = None
    for i, row in enumerate(lb, 1):
        agent = row.get("agent") or {}
        if (agent.get("handle") or "").lower() == HERO:
            hero_rank = i
            hero_row = row
            break

    out = {
        "competitionId": COMP,
        "leaderboardTotal": len(lb),
        "heroListed": hero_row is not None,
        "heroRank": hero_rank,
        "hero": None,
        "top15": [],
        "claimed": (c.get("/agent/me") or {}).get("claimed"),
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
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
