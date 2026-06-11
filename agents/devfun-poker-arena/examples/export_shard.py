"""Stable agent partitioning for multi-host Arena export (rate-limit spread)."""
from __future__ import annotations

import hashlib
import os


def shard_index_count(
    shard_index: int | None = None,
    shard_count: int | None = None,
) -> tuple[int, int]:
    """Resolve shard from args or CEMINI_EXPORT_SHARD_INDEX / CEMINI_EXPORT_SHARD_COUNT."""
    if shard_count is None:
        raw = os.environ.get("CEMINI_EXPORT_SHARD_COUNT", "1").strip()
        try:
            shard_count = max(1, int(raw))
        except ValueError:
            shard_count = 1
    if shard_index is None:
        raw = os.environ.get("CEMINI_EXPORT_SHARD_INDEX", "0").strip()
        try:
            shard_index = int(raw)
        except ValueError:
            shard_index = 0
    shard_count = max(1, int(shard_count))
    shard_index = int(shard_index) % shard_count
    return shard_index, shard_count


def agent_shard_bucket(agent_id: str, shard_count: int) -> int:
    digest = hashlib.md5(agent_id.encode("utf-8")).hexdigest()
    return int(digest, 16) % max(1, shard_count)


def agent_in_shard(
    agent_id: str,
    shard_index: int,
    shard_count: int,
) -> bool:
    if shard_count <= 1:
        return True
    if not agent_id:
        return False
    return agent_shard_bucket(str(agent_id), shard_count) == shard_index


def filter_leaderboard_shard(
    lb_rows: list[dict],
    shard_index: int,
    shard_count: int,
) -> list[dict]:
    if shard_count <= 1:
        return lb_rows
    out: list[dict] = []
    for row in lb_rows:
        ag = row.get("agent") or {}
        aid = ag.get("id")
        if aid and agent_in_shard(str(aid), shard_index, shard_count):
            out.append(row)
    return out


def crawl_state_name(shard_index: int, shard_count: int) -> str:
    if shard_count <= 1:
        return "crawl_state.json"
    return f"crawl_state_shard{shard_index}of{shard_count}.json"
