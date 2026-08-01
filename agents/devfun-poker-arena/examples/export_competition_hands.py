#!/usr/bin/env python3
"""Export Playground / competition hand data for training and opponent research.

Arena exposes no single bulk download. This script paginates public API endpoints
and writes training-friendly JSONL plus an optional aggregate summary.

Data sources:
  - GET /texas/recent-tables?competitionId=     all seats, ~200-table rolling window
  - GET /agent/submissions?agentId=&competitionId=   full per-agent history
  - GET /competition/leaderboard?competitionId=      agent roster + ranks
  - GET /texas/agent-stats?agentId=&competitionId=   VPIP/PFR aggregates

Usage:
    uv run python examples/export_competition_hands.py
    uv run python examples/export_competition_hands.py --match cmpy2qy65002ud9ej6b7jjq0l
    uv run python examples/export_competition_hands.py --mode full --top-agents 50
    pokerkit export --match cmpy2qy65002ud9ej6b7jjq0l --out reports/exports/hands.jsonl

Output (default dir reports/exports/<compId>/<timestamp>/):
  tables.jsonl      one record per settled table (all villain hole cards)
  submissions.jsonl hero-perspective rows (--mode full or --top-agents N)
  agents.jsonl      leaderboard + agent-stats snapshot
  summary.json      showdown/win aggregates for strategy review
  manifest.json     export metadata + record counts
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from dotenv import load_dotenv

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from analyze import _fetch_replays  # noqa: E402
from arena_client import ArenaClient, ArenaError, CREDS_PATH, DEFAULT_BASE  # noqa: E402
from export_shard import (  # noqa: E402
    agent_in_shard,
    filter_leaderboard_shard,
    shard_index_count,
)

PAGE_SIZE = 100

_BB100_KEYS = (
    "adjustedBbPer100",
    "adjustedBBPer100",
    "adjusted_bb_per_100",
    "allInEvBbPer100",
    "aivatBbPer100",
)


def leaderboard_adjusted_bb100(lb_row: dict) -> float | None:
    """Extract adjusted bb/100 from a leaderboard row when the UI/API exposes it."""
    for key in _BB100_KEYS:
        val = lb_row.get(key)
        if isinstance(val, (int, float)):
            return float(val)
    return None


def _load_creds() -> tuple[Optional[str], Optional[str]]:
    """Env wins for apiKey on prod (.env via systemd); file supplies agentId fallback."""
    env_key = (os.environ.get("ARENA_API_KEY") or "").strip() or None
    env_agent = (os.environ.get("ARENA_AGENT_ID") or "").strip() or None
    if CREDS_PATH.exists():
        try:
            c = json.loads(CREDS_PATH.read_text())
            key = env_key or c.get("apiKey")
            agent = env_agent or c.get("agentId") or c.get("id")
            return key, agent
        except Exception:
            pass
    return env_key, env_agent


def _paginate(client: ArenaClient, path: str) -> tuple[list[dict], int]:
    """Fetch all pages; return (rows, reported_total)."""
    rows: list[dict] = []
    offset = 0
    total = 0
    while True:
        sep = "&" if "?" in path else "?"
        body = client.get(f"{path}{sep}limit={PAGE_SIZE}&offset={offset}")
        batch = body.get("data") if isinstance(body, dict) else []
        if not isinstance(batch, list):
            batch = body if isinstance(body, list) else []
        if not batch:
            break
        rows.extend(batch)
        total = int(body.get("total") or len(rows)) if isinstance(body, dict) else len(rows)
        offset += len(batch)
        if offset >= total:
            break
    return rows, total


def fetch_recent_tables(client: ArenaClient, competition_id: str) -> list[dict]:
    rows, _ = _paginate(client, f"/texas/recent-tables?competitionId={competition_id}")
    return rows


def fetch_leaderboard(client: ArenaClient, competition_id: str) -> list[dict]:
    rows, _ = _paginate(client, f"/competition/leaderboard?competitionId={competition_id}")
    return rows


def fetch_agent_submissions(
    client: ArenaClient,
    agent_id: str,
    competition_id: str,
) -> list[dict]:
    rows, _ = _paginate(
        client,
        f"/agent/submissions?agentId={agent_id}&competitionId={competition_id}",
    )
    return rows


def fetch_agent_stats(
    client: ArenaClient,
    agent_id: str,
    competition_id: str,
) -> Optional[dict]:
    try:
        return client.get(
            f"/texas/agent-stats?agentId={agent_id}&competitionId={competition_id}"
        )
    except ArenaError:
        return None


def normalize_table(
    table: dict,
    *,
    competition_id: str,
    chip_deltas: Optional[dict[str, dict[str, int]]] = None,
) -> dict:
    chip_deltas = chip_deltas or {}
    table_id = str(table.get("id") or table.get("tableId") or "")
    seat_deltas = chip_deltas.get(table_id) or {}
    seats = []
    for s in table.get("seats") or []:
        agent_id = s.get("agentId")
        seat = {
            "agent_id": agent_id,
            "handle": s.get("agentHandle") or s.get("agentName"),
            "seat": s.get("seatNumber"),
            "hole_cards": list(s.get("holeCards") or []),
            "payout_chips": int(s.get("payoutChips") or 0),
            "stack_chips": int(s.get("stackChips") or 0),
        }
        if agent_id and str(agent_id) in seat_deltas:
            seat["chip_delta"] = seat_deltas[str(agent_id)]
        seats.append(seat)
    winners = []
    for w in table.get("winners") or []:
        winners.append({
            "agent_id": w.get("agentId"),
            "handle": w.get("agentHandle") or w.get("agentName"),
            "seat": w.get("seatNumber"),
            "amount": int(w.get("amount") or w.get("payoutChips") or 0),
            "hand_name": w.get("handName") or "",
        })
    return {
        "record_type": "table",
        "table_id": table.get("id") or table.get("tableId"),
        "competition_id": competition_id,
        "table_number": table.get("tableNumber"),
        "status": table.get("status"),
        "hand_count": int(table.get("handCount") or 1),
        "player_count": int(table.get("playerCount") or len(seats)),
        "board": list(table.get("boardCards") or []),
        "started_at": table.get("startedAt"),
        "ended_at": table.get("endedAt"),
        "seats": seats,
        "winners": winners,
    }


def normalize_submission(
    sub: dict,
    *,
    competition_id: str,
    chip_delta: Optional[int] = None,
) -> dict:
    data = sub.get("data") or {}
    ch = sub.get("challenge") or {}
    result = ch.get("result") or {}
    meta = ch.get("data") or {}
    winners = []
    for w in result.get("winners") or []:
        winners.append({
            "agent_id": w.get("agentId"),
            "handle": w.get("agentName"),
            "seat": w.get("seatNumber"),
            "amount": int(w.get("amount") or 0),
            "hand_name": w.get("handName") or "",
        })
    out = {
        "record_type": "submission",
        "submission_id": sub.get("id"),
        "table_id": ch.get("id"),
        "table_number": meta.get("tableNumber") or ch.get("uniqueId"),
        "competition_id": competition_id,
        "agent_handle": data.get("agentHandle") or data.get("agentName"),
        "seat": data.get("seatNumber"),
        "hole_cards": list(data.get("holeCards") or []),
        "payout_chips": int(data.get("payoutChips") or 0),
        "stack_chips": int(data.get("stackChips") or 0),
        "board": list(result.get("boardCards") or []),
        "winners": winners,
        "settled_at": sub.get("submittedAt") or ch.get("outcomeAt"),
        "score": sub.get("score"),
        "small_blind": meta.get("smallBlindChips"),
        "big_blind": meta.get("bigBlindChips"),
    }
    if chip_delta is not None:
        out["chip_delta"] = int(chip_delta)
    return out


def normalize_agent_row(lb_row: dict, stats: Optional[dict]) -> dict:
    ag = lb_row.get("agent") or {}
    out = {
        "record_type": "agent",
        "agent_id": ag.get("id"),
        "handle": ag.get("handle") or ag.get("name"),
        "name": ag.get("name"),
        "rank": lb_row.get("rank"),
        "chips": lb_row.get("totalScore"),
        "hands": lb_row.get("graduateCount"),
        "wins": lb_row.get("correctCount"),
        "total_submissions": lb_row.get("totalSubmissions"),
        "adjusted_bb100": leaderboard_adjusted_bb100(lb_row),
    }
    if stats:
        out["stats"] = {
            "sample_size": stats.get("sampleSize"),
            "vpip": stats.get("vpip"),
            "pfr": stats.get("pfr"),
            "three_bet_pct": stats.get("threeBetPct"),
            "af": stats.get("af"),
            "wtsd": stats.get("wtsd"),
            "wsd": stats.get("wsd"),
            "playing_style": (stats.get("playingStyle") or {}).get("label"),
        }
    return out


def build_summary(
    tables: list[dict],
    submissions: list[dict],
    agents: list[dict],
) -> dict:
    """Aggregate showdown outcomes for quick strategy review."""
    by_handle: dict[str, dict[str, Any]] = defaultdict(lambda: {
        "showdowns": 0,
        "wins": 0,
        "payout_sum": 0,
        "chip_delta_sum": 0,
        "chip_delta_n": 0,
        "losses": 0,
    })
    for rec in tables:
        winner_ids = {
            (w.get("handle") or w.get("agent_id"))
            for w in rec.get("winners") or []
        }
        for seat in rec.get("seats") or []:
            handle = seat.get("handle") or seat.get("agent_id")
            if not handle:
                continue
            row = by_handle[handle]
            row["showdowns"] += 1
            payout = int(seat.get("payout_chips") or 0)
            row["payout_sum"] += payout
            if handle in winner_ids or payout > 0:
                row["wins"] += 1
            elif payout < 0:
                row["losses"] += 1

    for rec in submissions:
        handle = rec.get("agent_handle")
        if not handle:
            continue
        row = by_handle[handle]
        row["hero_hands"] = row.get("hero_hands", 0) + 1
        payout = int(rec.get("payout_chips") or 0)
        row["hero_payout_sum"] = row.get("hero_payout_sum", 0) + payout
        if rec.get("chip_delta") is not None:
            row["chip_delta_sum"] += int(rec["chip_delta"])
            row["chip_delta_n"] += 1

    hero_chip_delta_sum = None
    hero_chip_delta_n = 0
    hero_bb100_from_delta = None
    for rec in submissions:
        if rec.get("chip_delta") is None:
            continue
        hero_chip_delta_n += 1
        hero_chip_delta_sum = (hero_chip_delta_sum or 0) + int(rec["chip_delta"])
    if hero_chip_delta_n and hero_chip_delta_sum is not None:
        bb_vals = [int(r.get("big_blind") or 0) for r in submissions if r.get("big_blind")]
        bb = max(bb_vals) if bb_vals else 0
        if bb > 0:
            hero_bb100_from_delta = round(
                (hero_chip_delta_sum / bb) * (100 / hero_chip_delta_n), 2
            )

    top_showdown = sorted(
        (
            {"handle": h, **v, "win_rate": round(v["wins"] / max(v["showdowns"], 1), 3)}
            for h, v in by_handle.items()
            if v.get("showdowns", 0) >= 3
        ),
        key=lambda r: r["payout_sum"],
        reverse=True,
    )[:30]

    return {
        "exported_at": datetime.now(timezone.utc).isoformat(),
        "table_records": len(tables),
        "submission_records": len(submissions),
        "agent_records": len(agents),
        "unique_handles_in_tables": len(by_handle),
        "hero_chip_delta_sum": hero_chip_delta_sum,
        "hero_chip_delta_n": hero_chip_delta_n,
        "hero_bb100_from_chip_delta": hero_bb100_from_delta,
        "top_showdown_performers": top_showdown,
        "notes": (
            "recent-tables is a rolling ~200-table window; use --mode full for "
            "per-agent submission history. chip_delta from /agent/replays when "
            "--with-replays; payout_chips is pot won, not chip delta."
        ),
    }


def _write_jsonl(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for rec in records:
            fh.write(json.dumps(rec, separators=(",", ":"), sort_keys=True))
            fh.write("\n")


def _load_existing_ids(path: Path, key: str) -> set[str]:
    index_path = Path(str(path) + ".ids")
    if index_path.is_file():
        return {line.strip() for line in index_path.read_text(encoding="utf-8").splitlines() if line.strip()}
    if not path.is_file():
        return set()
    seen: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        val = rec.get(key)
        if val:
            seen.add(str(val))
    if seen:
        index_path.write_text("\n".join(sorted(seen)) + "\n", encoding="utf-8")
    return seen


def _append_chip_delta_sidecar(out_dir: Path, submissions: list[dict]) -> int:
    """Append chip_delta rows when submissions.jsonl dedupe skips updates."""
    rows: list[dict] = []
    for s in submissions:
        cd = s.get("chip_delta")
        sid = s.get("submission_id")
        if cd is None or not sid:
            continue
        rows.append({
            "record_type": "chip_delta",
            "submission_id": sid,
            "table_id": s.get("table_id"),
            "agent_handle": s.get("agent_handle"),
            "chip_delta": int(cd),
        })
    if not rows:
        return 0
    return _append_jsonl(out_dir / "chip_deltas.jsonl", rows, "submission_id")


def _append_jsonl(path: Path, records: list[dict], dedupe_key: str) -> int:
    seen = _load_existing_ids(path, dedupe_key)
    new_rows = [r for r in records if str(r.get(dedupe_key)) not in seen]
    if not new_rows:
        return 0
    path.parent.mkdir(parents=True, exist_ok=True)
    index_path = Path(str(path) + ".ids")
    lock_path = Path(str(path) + ".lock")
    try:
        import fcntl

        with lock_path.open("a+", encoding="utf-8") as lock_fh:
            fcntl.flock(lock_fh.fileno(), fcntl.LOCK_EX)
            with path.open("a", encoding="utf-8") as fh:
                new_ids: list[str] = []
                for rec in new_rows:
                    rid = str(rec.get(dedupe_key))
                    if rid in seen:
                        continue
                    fh.write(json.dumps(rec, separators=(",", ":"), sort_keys=True))
                    fh.write("\n")
                    seen.add(rid)
                    new_ids.append(rid)
            if new_ids:
                with index_path.open("a", encoding="utf-8") as idx:
                    for rid in new_ids:
                        idx.write(rid + "\n")
            return len(new_ids)
    except ImportError:
        with path.open("a", encoding="utf-8") as fh:
            for rec in new_rows:
                fh.write(json.dumps(rec, separators=(",", ":"), sort_keys=True))
                fh.write("\n")
        return len(new_rows)


def _table_id_by_number(raw_tables: list[dict]) -> dict[int, str]:
    """Map arena tableNumber → recent-tables id (matches /agent/replays tableId)."""
    out: dict[int, str] = {}
    for t in raw_tables:
        num = t.get("tableNumber")
        tid = t.get("id") or t.get("tableId")
        if num is not None and tid:
            out[int(num)] = str(tid)
    return out


def _submission_chip_delta(
    sub: dict,
    agent_replays: dict[str, int],
    table_id_by_number: dict[int, str],
) -> Optional[int]:
    """Join submission to replay chipDelta via table id or tableNumber bridge."""
    ch = sub.get("challenge") or {}
    tid = ch.get("id")
    if tid is not None and str(tid) in agent_replays:
        return agent_replays[str(tid)]
    num = (ch.get("data") or {}).get("tableNumber")
    if num is not None:
        real_tid = table_id_by_number.get(int(num))
        if real_tid and real_tid in agent_replays:
            return agent_replays[real_tid]
    return None


def _replay_deltas_by_agent(
    client: ArenaClient,
    agent_ids: list[str],
    *,
    competition_id: str,
    sleep_s: float = 0.05,
) -> dict[str, dict[str, int]]:
    """{agent_id: {table_id: chipDelta}} — server caps replays at 50 per agent."""
    out: dict[str, dict[str, int]] = {}
    for aid in agent_ids:
        if not aid:
            continue
        deltas = _fetch_replays(client, aid, limit=50, competition_id=competition_id)
        if deltas:
            out[str(aid)] = {str(tid): int(v) for tid, v in deltas.items()}
        if sleep_s:
            time.sleep(sleep_s)
    return out


def _ensure_hero_in_targets(
    lb_rows: list[dict],
    targets: list[dict],
    hero_agent_id: Optional[str],
) -> list[dict]:
    """Always fetch hero submissions even when hero is outside --top-agents slice."""
    if not hero_agent_id:
        return targets
    hero_id = str(hero_agent_id)
    seen = {
        str((row.get("agent") or {}).get("id"))
        for row in targets
        if (row.get("agent") or {}).get("id")
    }
    if hero_id in seen:
        return targets
    for row in lb_rows:
        aid = (row.get("agent") or {}).get("id")
        if aid and str(aid) == hero_id:
            return targets + [row]
    return targets + [{"agent": {"id": hero_id, "handle": "hero"}}]


def export_competition(
    client: ArenaClient,
    competition_id: str,
    *,
    mode: str = "recent",
    top_agents: int = 0,
    fetch_stats: bool = True,
    stats_top: int = 50,
    sleep_s: float = 0.05,
    with_replays: bool = True,
    replays_top_agents: int = 0,
    hero_agent_id: Optional[str] = None,
    shard_index: int | None = None,
    shard_count: int | None = None,
) -> dict[str, Any]:
    """Run export; return dict of record lists keyed by output file stem."""
    shard_index, shard_count = shard_index_count(shard_index, shard_count)
    if shard_count > 1:
        print(
            f"[export] shard {shard_index}/{shard_count} "
            f"(IP-spread worker; tables/agents snapshot on shard 0 only)",
            file=sys.stderr,
        )

    print("[export] fetching leaderboard…", file=sys.stderr)
    lb_rows = fetch_leaderboard(client, competition_id)

    replay_by_agent: dict[str, dict[str, int]] = {}
    replay_agent_ids: list[str] = []
    if with_replays:
        if hero_agent_id and agent_in_shard(str(hero_agent_id), shard_index, shard_count):
            replay_agent_ids.append(str(hero_agent_id))
        if replays_top_agents > 0:
            for row in lb_rows[:replays_top_agents]:
                aid = (row.get("agent") or {}).get("id")
                if not aid or not agent_in_shard(str(aid), shard_index, shard_count):
                    continue
                if str(aid) not in replay_agent_ids:
                    replay_agent_ids.append(str(aid))
        if replay_agent_ids:
            print(
                f"[export] fetching replays for {len(replay_agent_ids)} agents "
                f"(cap 50 tables/agent)…",
                file=sys.stderr,
            )
            replay_by_agent = _replay_deltas_by_agent(
                client,
                replay_agent_ids,
                competition_id=competition_id,
                sleep_s=sleep_s,
            )
    hero_replays = replay_by_agent.get(str(hero_agent_id or ""), {})

    tables: list[dict] = []
    table_id_by_number: dict[int, str] = {}
    if shard_count <= 1 or shard_index == 0:
        print(f"[export] fetching recent-tables for {competition_id}…", file=sys.stderr)
        raw_tables = fetch_recent_tables(client, competition_id)
        table_chip_map: dict[str, dict[str, int]] = {}
        if hero_agent_id and hero_replays:
            table_chip_map = {
                tid: {str(hero_agent_id): delta} for tid, delta in hero_replays.items()
            }
        table_id_by_number = _table_id_by_number(raw_tables)
        tables = [
            normalize_table(t, competition_id=competition_id, chip_deltas=table_chip_map)
            for t in raw_tables
        ]
        print(f"[export] tables={len(tables)}", file=sys.stderr)
    else:
        print("[export] skip recent-tables (non-zero shard)", file=sys.stderr)

    agent_records: list[dict] = []
    if shard_count <= 1 or shard_index == 0:
        for i, row in enumerate(lb_rows):
            ag = row.get("agent") or {}
            aid = ag.get("id")
            stats = None
            if fetch_stats and aid and (i < stats_top or not stats_top):
                stats = fetch_agent_stats(client, aid, competition_id)
                if sleep_s:
                    time.sleep(sleep_s)
            agent_records.append(normalize_agent_row(row, stats))
        print(f"[export] agents={len(agent_records)}", file=sys.stderr)
    else:
        lb_shard = filter_leaderboard_shard(lb_rows, shard_index, shard_count)
        for row in lb_shard:
            ag = row.get("agent") or {}
            aid = ag.get("id")
            if not aid:
                continue
            stats = None
            if fetch_stats:
                stats = fetch_agent_stats(client, aid, competition_id)
                if sleep_s:
                    time.sleep(sleep_s)
            agent_records.append(normalize_agent_row(row, stats))
        print(f"[export] agents-shard={len(agent_records)}", file=sys.stderr)

    submissions: list[dict] = []
    if mode == "full":
        targets = filter_leaderboard_shard(lb_rows, shard_index, shard_count)
        print(f"[export] full mode — submissions for {len(targets)} agents…", file=sys.stderr)
    elif top_agents > 0:
        targets = filter_leaderboard_shard(lb_rows[:top_agents], shard_index, shard_count)
        print(
            f"[export] top-agents={top_agents} shard targets={len(targets)}…",
            file=sys.stderr,
        )
    else:
        targets = []

    targets = _ensure_hero_in_targets(lb_rows, targets, hero_agent_id)

    for i, row in enumerate(targets):
        ag = row.get("agent") or {}
        aid = ag.get("id")
        if not aid:
            continue
        handle = ag.get("handle") or ag.get("name") or aid
        subs = fetch_agent_submissions(client, aid, competition_id)
        agent_replays = replay_by_agent.get(str(aid), {})
        for s in subs:
            cd = _submission_chip_delta(s, agent_replays, table_id_by_number)
            submissions.append(
                normalize_submission(
                    s, competition_id=competition_id, chip_delta=cd
                )
            )
        print(f"[export]   {i + 1}/{len(targets)} {handle}: {len(subs)} hands", file=sys.stderr)
        if sleep_s:
            time.sleep(sleep_s)

    summary = build_summary(tables, submissions, agent_records)
    return {
        "tables": tables,
        "submissions": submissions,
        "agents": agent_records,
        "summary": summary,
    }


def main(argv: Optional[list[str]] = None) -> int:
    p = argparse.ArgumentParser(
        description="Export competition hand data for training and opponent research.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    p.add_argument(
        "--match",
        default=None,
        help="competitionId (default: ARENA_LOBBY_COMPETITION_ID or Playground S1)",
    )
    p.add_argument(
        "--mode",
        choices=("recent", "full"),
        default="recent",
        help="recent=tables+agents only; full=all agent submissions (slow)",
    )
    p.add_argument(
        "--top-agents",
        type=int,
        default=30,
        help="Fetch submissions for top N leaderboard agents (0=skip unless --mode full)",
    )
    p.add_argument(
        "--out-dir",
        default=None,
        help="Output directory (default: reports/exports/<compId>/<timestamp>)",
    )
    p.add_argument(
        "--append",
        action="store_true",
        help="Append to existing JSONL in --out-dir, dedupe by table_id/submission_id",
    )
    p.add_argument(
        "--no-stats",
        action="store_true",
        help="Skip per-agent /texas/agent-stats calls",
    )
    p.add_argument(
        "--stats-top",
        type=int,
        default=50,
        help="Fetch agent-stats for top N leaderboard rows (default 50)",
    )
    p.add_argument(
        "--no-replays",
        action="store_true",
        help="Skip /agent/replays chipDelta merge (payout_chips only)",
    )
    p.add_argument(
        "--replays-top-agents",
        type=int,
        default=0,
        help="Fetch /agent/replays chipDelta for top N leaderboard agents (50 cap/agent)",
    )
    p.add_argument("--shard-index", type=int, default=None, help="Worker shard (0-based)")
    p.add_argument("--shard-count", type=int, default=None, help="Total shards (IP spread)")
    args = p.parse_args(argv)

    load_dotenv()
    api_key, agent_id = _load_creds()
    if not api_key:
        print("ERROR: set ARENA_API_KEY or run pokerkit run once for .arena-credentials",
              file=sys.stderr)
        return 2

    from export_match import resolve_export_competition_id

    competition_id = resolve_export_competition_id(args.match)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = Path(
        args.out_dir or f"reports/exports/{competition_id}/{ts}"
    )

    client = ArenaClient(os.environ.get("ARENA_API_BASE", DEFAULT_BASE), api_key=api_key)
    try:
        top_agents = args.top_agents
        if args.mode == "full":
            top_agents = 0
        elif top_agents <= 0:
            top_agents = 0

        replays_top = max(0, int(args.replays_top_agents))
        if replays_top <= 0:
            raw = os.environ.get("CEMINI_EXPORT_REPLAYS_TOP", "").strip()
            if raw:
                replays_top = max(0, int(raw))

        shard_index, shard_count = shard_index_count(args.shard_index, args.shard_count)

        data = export_competition(
            client,
            competition_id,
            mode=args.mode,
            top_agents=top_agents,
            fetch_stats=not args.no_stats,
            stats_top=args.stats_top,
            with_replays=not args.no_replays,
            replays_top_agents=replays_top,
            hero_agent_id=agent_id,
            shard_index=shard_index,
            shard_count=shard_count,
        )

        if args.append:
            out_dir.mkdir(parents=True, exist_ok=True)
            n_tables = _append_jsonl(out_dir / "tables.jsonl", data["tables"], "table_id")
            n_subs = _append_jsonl(
                out_dir / "submissions.jsonl", data["submissions"], "submission_id"
            )
            n_delta = _append_chip_delta_sidecar(out_dir, data["submissions"])
            if n_delta:
                print(f"[export] chip_deltas sidecar +{n_delta}", file=sys.stderr)
            (out_dir / "agents.jsonl").write_text(
                "\n".join(json.dumps(r, sort_keys=True) for r in data["agents"]) + "\n",
                encoding="utf-8",
            )
            (out_dir / "summary.json").write_text(
                json.dumps(data["summary"], indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            print(f"[export] appended tables={n_tables} submissions={n_subs} → {out_dir}")
        else:
            out_dir.mkdir(parents=True, exist_ok=True)
            _write_jsonl(out_dir / "tables.jsonl", data["tables"])
            _write_jsonl(out_dir / "submissions.jsonl", data["submissions"])
            _write_jsonl(out_dir / "agents.jsonl", data["agents"])
            (out_dir / "summary.json").write_text(
                json.dumps(data["summary"], indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            manifest = {
                "competition_id": competition_id,
                "exported_at": data["summary"]["exported_at"],
                "mode": args.mode,
                "top_agents": top_agents if args.mode != "full" else "all",
                "counts": {
                    "tables": len(data["tables"]),
                    "submissions": len(data["submissions"]),
                    "agents": len(data["agents"]),
                },
                "files": [
                    "tables.jsonl",
                    "submissions.jsonl",
                    "agents.jsonl",
                    "summary.json",
                ],
            }
            (out_dir / "manifest.json").write_text(
                json.dumps(manifest, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            print(f"[export] wrote {out_dir}")
            print(
                f"  tables={len(data['tables'])} "
                f"submissions={len(data['submissions'])} "
                f"agents={len(data['agents'])}"
            )

        return 0
    finally:
        client.close()


if __name__ == "__main__":
    raise SystemExit(main())
