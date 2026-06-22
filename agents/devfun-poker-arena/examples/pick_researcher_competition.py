#!/usr/bin/env python3
"""Scan Arena API for Researcher / Challenge / HU sandbox competitions.

Usage:
    uv run python examples/pick_researcher_competition.py
    uv run python examples/pick_researcher_competition.py --write-env .env.researcher
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from researcher_comp_recon import (  # noqa: E402
    _is_researcher_candidate,
    _load_api_key,
    _norm_comp_list,
)
from arena_client import ArenaClient, DEFAULT_BASE  # noqa: E402

_AGENT_ROOT = _EXAMPLES.parent

# Pin when Heads-Up PvP S3 is publicly joinable [NEEDS VERIFICATION 2026-06-22].
HEADS_UP_PVP_S3_COMP_ID = "cmqnvili2002gwb82l1qba0gm"


def fetch_candidates(client: ArenaClient) -> list[dict[str, Any]]:
    body = client.get("/competition/list-all")
    comps = _norm_comp_list(body)
    return [c for c in comps if _is_researcher_candidate(c)]


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Pick Researcher sandbox competition id")
    p.add_argument("--write-env", metavar="PATH", help="Append ARENA_RESEARCHER_COMP_ID=…")
    p.add_argument("--json", action="store_true", help="Print JSON only")
    args = p.parse_args(argv)

    key = _load_api_key(_AGENT_ROOT)
    client = ArenaClient(api_key=key, base_url=DEFAULT_BASE)
    candidates = fetch_candidates(client)

    if args.json:
        print(json.dumps(candidates, indent=2))
        return 0

    if not candidates:
        print("No researcher/challenge/sandbox candidates in list-all.")
        print("Run: bash scripts/list_arena_competitions.sh")
        return 1

    def _score(c: dict) -> tuple[int, int, str]:
        blob = f"{c.get('name', '')} {c.get('description', '')}".lower()
        # Prefer live HU PvP sandbox (Researcher track) over legacy beta sandbox ids.
        tier = 0
        if "heads-up pvp" in blob or "heads up pvp" in blob:
            tier = 3
        elif "researcher" in blob:
            tier = 2
        elif "sandbox" in blob and "pvp" in blob:
            tier = 1
        season = int(c.get("seasonNumber") or 0)
        return (tier, season, str(c.get("id") or ""))

    best = max(candidates, key=_score)

    cid = str(best.get("id") or "")
    print(f"candidate_id={cid}")
    print(f"name={best.get('name')}")
    print(f"season={best.get('seasonNumber')}")
    print(f"skillFile={best.get('skillFile')}")
    if "heads-up pvp" in f"{best.get('name', '')} {best.get('description', '')}".lower():
        if cid == HEADS_UP_PVP_S3_COMP_ID:
            print(f"hu_pvp_s3_match={HEADS_UP_PVP_S3_COMP_ID}")
        else:
            print(f"hu_pvp_s3_expected={HEADS_UP_PVP_S3_COMP_ID}")

    if args.write_env and cid:
        path = Path(args.write_env)
        lines = []
        if path.is_file():
            for line in path.read_text(encoding="utf-8").splitlines():
                if not line.startswith("ARENA_RESEARCHER_COMP_ID="):
                    lines.append(line)
        lines.append(f"ARENA_RESEARCHER_COMP_ID={cid}")
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"wrote {path}")

    return 0 if cid else 1


if __name__ == "__main__":
    sys.exit(main())
