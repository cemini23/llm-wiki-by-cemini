#!/usr/bin/env python3
"""Export full per-agent hand history (submissions + replays + stats).

Used to archive jackpot probe fleet data before pausing / between Playgrounds.

Usage:
    uv run python examples/export_agent_hand_history.py \\
        --match cmpy2qy65002ud9ej6b7jjq0l \\
        --agent cmq014ud2cl3pacxgg8z4p6ho:lib-a \\
        --out-dir reports/jackpot-27-archive/playground-s1
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

from arena_client import ArenaClient, ArenaError, CREDS_PATH, DEFAULT_BASE  # noqa: E402
from export_competition_hands import (  # noqa: E402
    fetch_agent_stats,
    fetch_agent_submissions,
    normalize_agent_row,
    normalize_submission,
)


def fetch_all_replays(
    client: ArenaClient,
    agent_id: str,
    competition_id: str,
    *,
    page_size: int = 50,
) -> list[dict]:
    """Fetch replays — API returns at most one page (offset ignored server-side)."""
    qs = f"?limit={page_size}&competitionId={competition_id}"
    try:
        body = client.get(f"/agent/{agent_id}/replays{qs}")
    except ArenaError:
        return []
    if isinstance(body, list):
        return body
    if isinstance(body, dict) and isinstance(body.get("data"), list):
        return body["data"]
    return []


def _load_creds() -> Optional[str]:
    if CREDS_PATH.exists():
        try:
            return json.loads(CREDS_PATH.read_text()).get("apiKey")
        except Exception:
            pass
    return os.environ.get("ARENA_API_KEY")


def _parse_agent(spec: str) -> tuple[str, str]:
    """agentId or agentId:label"""
    if ":" in spec:
        aid, label = spec.split(":", 1)
        return aid.strip(), label.strip()
    return spec.strip(), spec.strip()


def export_one_agent(
    client: ArenaClient,
    *,
    agent_id: str,
    label: str,
    competition_id: str,
    out_dir: Path,
    include_replays: bool,
) -> dict[str, Any]:
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"[export-agent] {label} ({agent_id})…", file=sys.stderr)

    raw_subs = fetch_agent_submissions(client, agent_id, competition_id)
    subs = [normalize_submission(s, competition_id=competition_id) for s in raw_subs]
    for rec in subs:
        rec["agent_id"] = agent_id
        rec["agent_label"] = label

    stats = fetch_agent_stats(client, agent_id, competition_id)
    agent_row = normalize_agent_row(
        {"agent": {"id": agent_id, "handle": label}, "rank": None, "totalScore": None},
        stats,
    )
    agent_row["agent_label"] = label

    replays: list[dict] = []
    if include_replays:
        replays = fetch_all_replays(client, agent_id, competition_id)
        for rec in replays:
            if isinstance(rec, dict):
                rec.setdefault("agent_id", agent_id)
                rec.setdefault("agent_label", label)

    _write_jsonl(out_dir / "submissions.jsonl", subs)
    (out_dir / "agent-stats.json").write_text(
        json.dumps(agent_row, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    if include_replays:
        _write_jsonl(out_dir / "replays.jsonl", replays)

    summary = {
        "agent_id": agent_id,
        "agent_label": label,
        "competition_id": competition_id,
        "exported_at": datetime.now(timezone.utc).isoformat(),
        "submission_count": len(subs),
        "replay_count": len(replays),
        "stats": agent_row.get("stats"),
    }
    (out_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        f"[export-agent]   {label}: submissions={len(subs)} replays={len(replays)}",
        file=sys.stderr,
    )
    return summary


def _write_jsonl(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as fh:
        for rec in rows:
            fh.write(json.dumps(rec, separators=(",", ":"), sort_keys=True))
            fh.write("\n")


def main(argv: Optional[list[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Export per-agent full hand history.")
    p.add_argument("--match", required=True, help="competitionId")
    p.add_argument(
        "--agent",
        action="append",
        default=[],
        metavar="AGENT_ID[:LABEL]",
        help="Repeatable; export one agent (optional label for output dir)",
    )
    p.add_argument("--out-dir", required=True, help="Archive root directory")
    p.add_argument("--no-replays", action="store_true", help="Skip /agent/replays fetch")
    p.add_argument("--sleep", type=float, default=0.08, help="Pause between agents (seconds)")
    args = p.parse_args(argv)

    load_dotenv()
    api_key = _load_creds()
    if not api_key:
        print("ERROR: set ARENA_API_KEY or .arena-credentials", file=sys.stderr)
        return 2
    if not args.agent:
        print("ERROR: pass at least one --agent", file=sys.stderr)
        return 2

    out_root = Path(args.out_dir)
    out_root.mkdir(parents=True, exist_ok=True)
    client = ArenaClient(os.environ.get("ARENA_API_BASE", DEFAULT_BASE), api_key=api_key)
    summaries: list[dict[str, Any]] = []
    try:
        for spec in args.agent:
            agent_id, label = _parse_agent(spec)
            safe_label = label.replace("/", "-")
            agent_dir = out_root / safe_label
            summaries.append(
                export_one_agent(
                    client,
                    agent_id=agent_id,
                    label=label,
                    competition_id=args.match,
                    out_dir=agent_dir,
                    include_replays=not args.no_replays,
                )
            )
            if args.sleep:
                time.sleep(args.sleep)
    finally:
        client.close()

    manifest = {
        "competition_id": args.match,
        "exported_at": datetime.now(timezone.utc).isoformat(),
        "agents": summaries,
        "notes": (
            "submissions.jsonl is the full per-agent hand history. "
            "replays.jsonl is best-effort (API returns max 50 recent, no offset)."
        ),
    }
    (out_root / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    combined: list[dict] = []
    for spec in args.agent:
        _, label = _parse_agent(spec)
        path = out_root / label.replace("/", "-") / "submissions.jsonl"
        if path.is_file():
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    combined.append(json.loads(line))
    _write_jsonl(out_root / "all-probes-submissions.jsonl", combined)
    total_subs = sum(s["submission_count"] for s in summaries)
    print(f"[export-agent] done → {out_root} ({total_subs} submissions total)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
