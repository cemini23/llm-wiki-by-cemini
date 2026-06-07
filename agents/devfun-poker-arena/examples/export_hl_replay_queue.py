#!/usr/bin/env python3
"""Fetch replay metadata for HL worst-hand table IDs (Tier-3 capture).

Replays are slow (API cap 50 recent). This script:
  1. Parses table= IDs from an analyze report (or --table-id repeats)
  2. Fetches hero /agent/replays and matches chipDelta + replayUrl
  3. Appends deduped rows to reports/hl-loop/replay_queue.jsonl

Usage:
    uv run python examples/export_hl_replay_queue.py --analyze reports/hl-loop/latest_analyze.txt
    uv run python examples/export_hl_replay_queue.py --table-id cmq48p1c2jtw4jeokfu03r0u4
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from arena_client import ArenaClient, ArenaError, CREDS_PATH, DEFAULT_BASE  # noqa: E402
from export_agent_hand_history import fetch_all_replays  # noqa: E402

_TABLE_RE = re.compile(r"\btable=([a-z0-9]+)\b", re.I)
_WORST_RE = re.compile(r"^\s*#\d+\s+")


def _load_creds() -> tuple[Optional[str], Optional[str]]:
    if CREDS_PATH.exists():
        try:
            c = json.loads(CREDS_PATH.read_text())
            return c.get("apiKey"), c.get("agentId") or c.get("id")
        except Exception:
            pass
    return os.environ.get("ARENA_API_KEY"), os.environ.get("ARENA_AGENT_ID")


def parse_table_ids(analyze_path: Path) -> list[str]:
    ids: list[str] = []
    in_worst = False
    for line in analyze_path.read_text(encoding="utf-8").splitlines():
        if "WORST" in line and "HANDS" in line:
            in_worst = True
            continue
        if in_worst and line.strip().startswith("BEST"):
            break
        if in_worst and _WORST_RE.match(line):
            for m in _TABLE_RE.finditer(line):
                tid = m.group(1)
                if tid != "?" and tid not in ids:
                    ids.append(tid)
    return ids


def _load_seen(path: Path) -> set[str]:
    if not path.is_file():
        return set()
    seen: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        tid = rec.get("table_id")
        if tid:
            seen.add(str(tid))
    return seen


def main(argv: Optional[list[str]] = None) -> int:
    p = argparse.ArgumentParser(description="HL worst-hand replay queue export")
    p.add_argument("--analyze", type=Path, help="Analyze report with table= fields")
    p.add_argument("--table-id", action="append", default=[], help="Explicit table ID")
    p.add_argument(
        "--out",
        type=Path,
        default=Path("reports/hl-loop/replay_queue.jsonl"),
    )
    p.add_argument("--match", default=None, help="competitionId")
    args = p.parse_args(argv)

    table_ids: list[str] = list(args.table_id or [])
    if args.analyze:
        table_ids.extend(parse_table_ids(args.analyze))
    # dedupe preserve order
    seen_in: set[str] = set()
    table_ids = [t for t in table_ids if not (t in seen_in or seen_in.add(t))]

    if not table_ids:
        print("No table IDs — pass --analyze or --table-id", file=sys.stderr)
        return 2

    load_dotenv()
    api_key, agent_id = _load_creds()
    if not api_key or not agent_id:
        print("ERROR: need ARENA_API_KEY + agentId", file=sys.stderr)
        return 2

    competition_id = (
        args.match
        or os.environ.get("ARENA_LOBBY_COMPETITION_ID")
        or "cmpy2qy65002ud9ej6b7jjq0l"
    )
    base = os.environ.get("ARENA_API_BASE", DEFAULT_BASE)
    client = ArenaClient(base, api_key=api_key)

    replay_by_table: dict[str, dict] = {}
    try:
        replays = fetch_all_replays(client, agent_id, competition_id, page_size=50)
        for rec in replays:
            if isinstance(rec, dict):
                tid = rec.get("tableId") or rec.get("handId")
                if tid:
                    replay_by_table[str(tid)] = rec
    except ArenaError as e:
        print(f"WARN: replays fetch failed: {e}", file=sys.stderr)

    out_path = args.out
    out_path.parent.mkdir(parents=True, exist_ok=True)
    seen = _load_seen(out_path)
    added = 0
    ts = datetime.now(timezone.utc).isoformat()

    with out_path.open("a", encoding="utf-8") as fh:
        for tid in table_ids:
            if tid in seen:
                continue
            rep = replay_by_table.get(tid) or {}
            row = {
                "table_id": tid,
                "competition_id": competition_id,
                "chip_delta": rep.get("chipDelta"),
                "replay_url": rep.get("replayUrl")
                or f"https://arena.dev.fun/poker-playground/table/{tid}",
                "winner_handle": rep.get("winnerHandle"),
                "settled_at": rep.get("settledAt"),
                "queued_at": ts,
                "source": "hl_replay_queue",
            }
            fh.write(json.dumps(row, separators=(",", ":"), sort_keys=True))
            fh.write("\n")
            added += 1

    print(f"[replay-queue] table_ids={len(table_ids)} new={added} → {out_path}")
    client.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
