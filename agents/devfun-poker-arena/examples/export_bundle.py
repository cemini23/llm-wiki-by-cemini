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
        aid = a.get("agent_id") or a.get("handle")
        if not aid:
            continue
        prev = by_id.get(str(aid))
        if prev is None or (a.get("rank") or 9999) < (prev.get("rank") or 9999):
            by_id[str(aid)] = a
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


def _norm_handle(handle: str | None) -> str:
    return (handle or "").strip().lower()


def load_bb100_snapshot(export_dir: Path) -> dict:
    """Load UI/manual bb/100 snapshot if present in export dir."""
    for name in ("bb100_ui_snapshot.json", "bb100_snapshot.json"):
        path = export_dir / name
        if path.is_file():
            try:
                return json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                continue
    return {}


def bb100_snapshot_index(snapshot: dict) -> dict[str, float]:
    """handle (normalized) and display_name → adjusted_bb100."""
    out: dict[str, float] = {}
    for row in snapshot.get("agents") or []:
        bb = row.get("adjusted_bb100")
        if not isinstance(bb, (int, float)):
            continue
        for key in ("handle", "display_name"):
            h = row.get(key)
            if h:
                out[_norm_handle(str(h))] = float(bb)
                out[_norm_handle(str(h).replace(" ", "_"))] = float(bb)
    return out


def apply_bb100_snapshot(export_dir: Path, snapshot: dict | None = None) -> list[dict]:
    """Merge snapshot bb/100 into agent rows; write agents_bb100_enriched.jsonl."""
    snapshot = snapshot if snapshot is not None else load_bb100_snapshot(export_dir)
    agents = load_export_agents(export_dir)
    if not snapshot:
        return agents
    idx = bb100_snapshot_index(snapshot)
    enriched: list[dict] = []
    for a in agents:
        row = dict(a)
        h = _norm_handle(row.get("handle"))
        name = _norm_handle(str(row.get("name") or ""))
        if row.get("adjusted_bb100") is None:
            row["adjusted_bb100"] = idx.get(h) or idx.get(name)
        if row.get("adjusted_bb100") is not None:
            row["adjusted_bb100_source"] = row.get("adjusted_bb100_source") or "ui_snapshot"
        enriched.append(row)
    # Snapshot-only rows not in export (partial field)
    seen = {_norm_handle(a.get("handle")) for a in enriched}
    for srow in snapshot.get("agents") or []:
        bb = srow.get("adjusted_bb100")
        h = _norm_handle(srow.get("handle"))
        if not h or h in seen or not isinstance(bb, (int, float)):
            continue
        enriched.append({
            "record_type": "agent",
            "handle": srow.get("handle") or h,
            "name": srow.get("display_name"),
            "rank": srow.get("chip_rank"),
            "chips": srow.get("chips"),
            "hands": srow.get("hands"),
            "adjusted_bb100": float(bb),
            "adjusted_bb100_source": "ui_snapshot_only",
        })
        seen.add(h)
    enriched.sort(key=lambda x: x.get("rank") or 9999)
    out_path = export_dir / "agents_bb100_enriched.jsonl"
    out_path.write_text(
        "\n".join(json.dumps(r, sort_keys=True) for r in enriched) + "\n",
        encoding="utf-8",
    )
    return enriched


def load_export_agents_with_bb100(export_dir: Path) -> list[dict]:
    """Agents from export + UI snapshot overlay when API lacks bb/100."""
    enriched_path = export_dir / "agents_bb100_enriched.jsonl"
    if enriched_path.is_file():
        return dedupe_agents(load_jsonl(enriched_path))
    snapshot = load_bb100_snapshot(export_dir)
    if snapshot:
        return apply_bb100_snapshot(export_dir, snapshot)
    return load_export_agents(export_dir)
