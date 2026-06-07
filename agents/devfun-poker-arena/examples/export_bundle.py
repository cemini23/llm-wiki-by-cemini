"""Load merged export data from Tier-1 + Tier-2 crawl artifacts."""
from __future__ import annotations

import json
from pathlib import Path


def load_jsonl(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    out: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            out.append(json.loads(line))
    return out


def dedupe_agents(rows: list[dict]) -> list[dict]:
    by_id: dict[str, dict] = {}
    for a in rows:
        aid = a.get("agent_id")
        if not aid:
            continue
        prev = by_id.get(aid)
        if prev is None or (a.get("rank") or 9999) < (prev.get("rank") or 9999):
            by_id[aid] = a
    return sorted(by_id.values(), key=lambda x: x.get("rank") or 9999)


def load_export_agents(export_dir: Path) -> list[dict]:
    rows: list[dict] = []
    for name in ("agents.jsonl", "agents-all.jsonl"):
        rows.extend(load_jsonl(export_dir / name))
    for batch in sorted(export_dir.glob("agents-crawl-batch*.jsonl")):
        rows.extend(load_jsonl(batch))
    return dedupe_agents(rows)


def load_export_submissions(export_dir: Path) -> list[dict]:
    rows: list[dict] = []
    for name in ("submissions-all.jsonl", "submissions.jsonl"):
        rows.extend(load_jsonl(export_dir / name))
    seen: set[str] = set()
    out: list[dict] = []
    for r in rows:
        sid = r.get("submission_id")
        if sid and sid in seen:
            continue
        if sid:
            seen.add(sid)
        out.append(r)
    return out


def crawl_progress(export_dir: Path) -> dict:
    path = export_dir / "crawl_state.json"
    if not path.is_file():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
