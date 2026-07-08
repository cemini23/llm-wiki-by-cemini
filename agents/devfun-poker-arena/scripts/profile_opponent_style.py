#!/usr/bin/env python3
"""Profile opponent style from export_competition_hands / export_agent_hand_history output.

Usage:
    uv run python scripts/profile_opponent_style.py \\
        --agents reports/exports/.../agents.jsonl \\
        --tables reports/exports/.../tables.jsonl \\
        --handle TEN --hero cemini_wiki_poker
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
_EXAMPLES = ROOT / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from villain_archetype import classify_villain_archetype  # noqa: E402

HERO_DEFAULT = "cemini_wiki_poker"


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not path.is_file():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def _agent_row(agents: list[dict], handle: str) -> dict[str, Any] | None:
    h = handle.lower()
    for row in agents:
        if str(row.get("handle") or "").lower() == h:
            return row
    return None


def _h2h_from_tables(
    tables: list[dict],
    *,
    villain: str,
    hero: str,
) -> dict[str, Any]:
    v_l, h_l = villain.lower(), hero.lower()
    nets: list[int] = []
    uncontested_villain = 0
    uncontested_hero = 0
    for rec in tables:
        seats = rec.get("seats") or []
        hero_seat = villain_seat = None
        for s in seats:
            handle = str(s.get("handle") or "").lower()
            if handle == h_l:
                hero_seat = s
            elif handle == v_l:
                villain_seat = s
        if not hero_seat or not villain_seat:
            continue
        hp = int(hero_seat.get("payout_chips") or 0)
        vp = int(villain_seat.get("payout_chips") or 0)
        nets.append(hp - vp)
        winners = rec.get("winners") or []
        if winners and winners[0].get("hand_name") == "Uncontested":
            wh = str(winners[0].get("handle") or "").lower()
            if wh == v_l and hp == 0:
                uncontested_villain += 1
            elif wh == h_l and vp == 0:
                uncontested_hero += 1
    n = len(nets)
    bb100 = (sum(nets) / n) * (100 / 2) if n else None
    return {
        "tables": n,
        "hero_net_chips": sum(nets),
        "hero_bb_per_100": round(bb100, 2) if bb100 is not None else None,
        "hero_win_rate": round(sum(1 for x in nets if x > 0) / n, 3) if n else None,
        "uncontested_villain_wins": uncontested_villain,
        "uncontested_hero_wins": uncontested_hero,
    }


def profile(
    *,
    agents_path: Path,
    tables_path: Path | None,
    handle: str,
    hero: str,
) -> dict[str, Any]:
    agents = _load_jsonl(agents_path)
    row = _agent_row(agents, handle)
    stats = (row or {}).get("stats") or {}
    archetype_input = {
        "sampleSize": stats.get("sample_size") or (row or {}).get("hands"),
        "vpip": stats.get("vpip"),
        "pfr": stats.get("pfr"),
        "threeBetPct": stats.get("three_bet_pct"),
        "af": stats.get("af"),
        "wtsd": stats.get("wtsd"),
        "wsd": stats.get("wsd"),
        "playingStyle": stats.get("playing_style"),
    }
    archetype = classify_villain_archetype(archetype_input, handle=handle)
    out: dict[str, Any] = {
        "handle": handle,
        "agent_id": (row or {}).get("agent_id"),
        "leaderboard_rank": (row or {}).get("rank"),
        "leaderboard_score": (row or {}).get("chips"),
        "graduate_hands": (row or {}).get("hands"),
        "arena_stats": stats,
        "archetype": archetype,
        "nemesis_recommendation": {
            "add_to_default": True,
            "add_to_linear_aggro": archetype == "linear_aggro",
        },
    }
    if tables_path and tables_path.is_file():
        out["h2h_recent_tables"] = _h2h_from_tables(
            _load_jsonl(tables_path), villain=handle, hero=hero
        )
    return out


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Profile opponent from Arena export JSONL")
    p.add_argument("--agents", type=Path, required=True)
    p.add_argument("--tables", type=Path, default=None)
    p.add_argument("--handle", required=True)
    p.add_argument("--hero", default=HERO_DEFAULT)
    p.add_argument("--json-out", type=Path, default=None)
    args = p.parse_args(argv)

    report = profile(
        agents_path=args.agents,
        tables_path=args.tables,
        handle=args.handle,
        hero=args.hero,
    )
    text = json.dumps(report, indent=2)
    print(text)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(text + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
