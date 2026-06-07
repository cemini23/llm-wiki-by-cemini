#!/usr/bin/env python3
"""Checkpointed full-field submission + stats crawl (slow tier).

Arena has no bulk download. Hourly export covers top-N rivals; this script
walks the full leaderboard in batches and appends deduped JSONL.

State file tracks offset so nightly runs make progress without re-fetching.

Usage:
    uv run python examples/export_field_crawl.py --out-dir reports/exports/playground-s1-live
    uv run python examples/export_field_crawl.py --batch-size 200 --stats-only
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from dotenv import load_dotenv

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from arena_client import ArenaClient, CREDS_PATH, DEFAULT_BASE  # noqa: E402
from export_competition_hands import (  # noqa: E402
    _append_jsonl,
    fetch_agent_stats,
    fetch_agent_submissions,
    fetch_leaderboard,
    fetch_recent_tables,
    normalize_agent_row,
    normalize_submission,
    normalize_table,
)


def _load_creds() -> Optional[str]:
    if CREDS_PATH.exists():
        try:
            return json.loads(CREDS_PATH.read_text()).get("apiKey")
        except Exception:
            pass
    return os.environ.get("ARENA_API_KEY")


def _load_state(path: Path) -> dict[str, Any]:
    if path.is_file():
        try:
            data = json.loads(path.read_text())
        except json.JSONDecodeError:
            data = {}
        # Migrate legacy offset checkpoint → agent-id set (cursor-audit fix).
        if "completed_agent_ids" not in data and data.get("agent_offset"):
            data.setdefault("completed_agent_ids", [])
            data["_migrated_from_offset"] = data.get("agent_offset")
        return data
    return {"completed_agent_ids": [], "cycles": 0, "leaderboard_total": 0}


def _stable_leaderboard(lb_rows: list[dict]) -> list[dict]:
    """Dedupe by agent_id and sort stably (rank re-sort safe)."""
    by_id: dict[str, dict] = {}
    for row in lb_rows:
        ag = row.get("agent") or {}
        aid = ag.get("id")
        if not aid:
            continue
        prev = by_id.get(aid)
        if prev is None or (row.get("rank") or 9999) < (prev.get("rank") or 9999):
            by_id[aid] = row
    return sorted(by_id.values(), key=lambda r: (r.get("agent") or {}).get("id") or "")


def _save_state(path: Path, state: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    state["updated_at"] = datetime.now(timezone.utc).isoformat()
    path.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def crawl_batch(
    client: ArenaClient,
    competition_id: str,
    out_dir: Path,
    *,
    batch_size: int,
    sleep_s: float,
    fetch_submissions: bool,
    fetch_stats: bool,
    fetch_tables: bool,
) -> dict[str, Any]:
    state_path = out_dir / "crawl_state.json"
    state = _load_state(state_path)
    lb_rows = _stable_leaderboard(fetch_leaderboard(client, competition_id))
    total = len(lb_rows)
    state["leaderboard_total"] = total
    completed = set(state.get("completed_agent_ids") or [])
    pending = [r for r in lb_rows if (r.get("agent") or {}).get("id") not in completed]
    batch = pending[:batch_size]
    if not batch and total:
        state["cycles"] = int(state.get("cycles") or 0) + 1
        state["completed_agent_ids"] = []
        _save_state(state_path, state)
        return {"processed": 0, "message": "cycle complete — reset for refresh pass", **state}

    n_subs = 0
    n_stats = 0
    agent_records: list[dict] = []

    for i, row in enumerate(batch):
        ag = row.get("agent") or {}
        aid = ag.get("id")
        handle = ag.get("handle") or ag.get("name") or aid
        if not aid:
            continue
        if fetch_stats:
            stats = fetch_agent_stats(client, aid, competition_id)
            rec = normalize_agent_row(row, stats)
            rec["crawl_index"] = len(completed) + i
            agent_records.append(rec)
            n_stats += 1
        if fetch_submissions:
            subs = fetch_agent_submissions(client, aid, competition_id)
            norm = [normalize_submission(s, competition_id=competition_id) for s in subs]
            n_subs += _append_jsonl(out_dir / "submissions-all.jsonl", norm, "submission_id")
            print(
                f"[crawl] {len(completed) + i + 1}/{total} "
                f"({len(pending) - i - 1} pending) {handle}: {len(subs)} hands",
                file=sys.stderr,
            )
        completed.add(aid)
        if sleep_s:
            time.sleep(sleep_s)

    if agent_records:
        snap = out_dir / "agents-crawl-batch.jsonl"
        snap.write_text(
            "\n".join(json.dumps(r, sort_keys=True) for r in agent_records) + "\n",
            encoding="utf-8",
        )

    n_tables = 0
    if fetch_tables:
        raw = fetch_recent_tables(client, competition_id)
        tables = [normalize_table(t, competition_id=competition_id) for t in raw]
        n_tables = _append_jsonl(out_dir / "tables.jsonl", tables, "table_id")

    state["completed_agent_ids"] = sorted(completed)
    if len(pending) <= batch_size:
        state["cycles"] = int(state.get("cycles") or 0) + 1
    _save_state(state_path, state)

    manifest = {
        "competition_id": competition_id,
        "exported_at": datetime.now(timezone.utc).isoformat(),
        "batch_size": len(batch),
        "completed_agents": len(completed),
        "pending_agents": max(total - len(completed), 0),
        "leaderboard_total": total,
        "new_submissions": n_subs,
        "agents_stats": n_stats,
        "new_tables": n_tables,
        "cycles_complete": state.get("cycles"),
    }
    (out_dir / "crawl_last.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return manifest


def main(argv: Optional[list[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Checkpointed full-field Arena data crawl")
    p.add_argument("--match", default=None, help="competitionId")
    p.add_argument("--out-dir", required=True, help="Export directory (shared with hourly export)")
    p.add_argument("--batch-size", type=int, default=150, help="Agents per run")
    p.add_argument("--sleep", type=float, default=0.06, help="Pause between agents")
    p.add_argument("--stats-only", action="store_true", help="Skip submissions; refresh agent-stats only")
    p.add_argument("--no-tables", action="store_true", help="Skip recent-tables append")
    args = p.parse_args(argv)

    load_dotenv()
    api_key = _load_creds()
    if not api_key:
        print("ERROR: set ARENA_API_KEY or .arena-credentials", file=sys.stderr)
        return 2

    competition_id = (
        args.match
        or os.environ.get("ARENA_LOBBY_COMPETITION_ID")
        or "cmpy2qy65002ud9ej6b7jjq0l"
    )
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    client = ArenaClient(os.environ.get("ARENA_API_BASE", DEFAULT_BASE), api_key=api_key)
    try:
        manifest = crawl_batch(
            client,
            competition_id,
            out_dir,
            batch_size=args.batch_size,
            sleep_s=args.sleep,
            fetch_submissions=not args.stats_only,
            fetch_stats=True,
            fetch_tables=not args.no_tables,
        )
        print(json.dumps(manifest, indent=2))
        return 0
    finally:
        client.close()


if __name__ == "__main__":
    raise SystemExit(main())
