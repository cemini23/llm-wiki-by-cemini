"""Shard partitioning for multi-IP harvest."""
from __future__ import annotations

import sys
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from export_shard import (  # noqa: E402
    agent_in_shard,
    agent_shard_bucket,
    filter_leaderboard_shard,
)


def test_shard_partition_covers_all_agents() -> None:
    ids = [f"agent-{i}" for i in range(300)]
    counts = [0, 0, 0]
    for aid in ids:
        b = agent_shard_bucket(aid, 3)
        counts[b] += 1
    assert sum(counts) == 300
    assert all(c > 0 for c in counts)


def test_filter_leaderboard_shard() -> None:
    rows = [{"agent": {"id": f"a{i}"}} for i in range(9)]
    shard0 = filter_leaderboard_shard(rows, 0, 3)
    shard1 = filter_leaderboard_shard(rows, 1, 3)
    assert len(shard0) + len(shard1) + len(filter_leaderboard_shard(rows, 2, 3)) == 9
    assert not any(
        agent_in_shard((r["agent"]["id"]), 0, 3) for r in shard1
    )
