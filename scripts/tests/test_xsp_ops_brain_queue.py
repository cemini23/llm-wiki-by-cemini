#!/usr/bin/env python3
"""WP1 tests: brain load/save + queue pending→running→done."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from xsp_ops.brain import (  # noqa: E402
    append_pull_log,
    empty_brain,
    load_brain,
    save_brain,
)
from xsp_ops.paths import ensure_layout  # noqa: E402
from xsp_ops.queue import (  # noqa: E402
    count_jobs,
    find_job,
    list_jobs,
    pending_to_running,
    running_to_done,
    write_pending,
)


@pytest.fixture
def ops_root(tmp_path: Path) -> Path:
    ensure_layout(tmp_path)
    return tmp_path


def test_ensure_layout_creates_tree(ops_root: Path) -> None:
    assert (ops_root / "state" / "posts").is_dir()
    assert (ops_root / "queue" / "pending").is_dir()
    assert (ops_root / "queue" / "running").is_dir()
    assert (ops_root / "queue" / "done").is_dir()
    assert (ops_root / "queue" / "failed").is_dir()
    assert (ops_root / "packets").is_dir()
    assert (ops_root / "events").is_dir()


def test_brain_load_save_roundtrip(ops_root: Path) -> None:
    brain = load_brain(ops_root)
    assert brain["pull_log"] == []
    brain["items_seen"] = 3
    brain["last_pull_at"] = "2026-07-15T12:00:00+00:00"
    append_pull_log(brain, {"at": "2026-07-15T12:00:00+00:00", "dry_run": True})
    path = save_brain(brain, ops_root)
    assert path.is_file()
    reloaded = load_brain(ops_root)
    assert reloaded["items_seen"] == 3
    assert len(reloaded["pull_log"]) == 1
    assert reloaded["pull_log"][0]["dry_run"] is True


def test_pull_log_capped_at_20(ops_root: Path) -> None:
    brain = empty_brain()
    for i in range(25):
        append_pull_log(brain, {"n": i})
    save_brain(brain, ops_root)
    reloaded = load_brain(ops_root)
    assert len(reloaded["pull_log"]) == 20
    assert reloaded["pull_log"][0]["n"] == 5
    assert reloaded["pull_log"][-1]["n"] == 24


def test_queue_pending_running_done(ops_root: Path) -> None:
    write_pending("post-alpha", ops_root)
    assert count_jobs("pending", ops_root) == 1
    assert find_job("post-alpha", ops_root)[0] == "pending"

    pending_to_running("post-alpha", ops_root, updates={"note": "working"})
    assert count_jobs("pending", ops_root) == 0
    assert count_jobs("running", ops_root) == 1
    status, job = find_job("post-alpha", ops_root)
    assert status == "running"
    assert job["note"] == "working"

    running_to_done("post-alpha", ops_root, updates={"action": "packet"})
    assert count_jobs("running", ops_root) == 0
    assert count_jobs("done", ops_root) == 1
    status, job = find_job("post-alpha", ops_root)
    assert status == "done"
    assert job["action"] == "packet"
    assert job["status"] == "done"
    assert list_jobs("done", ops_root)[0]["slug"] == "post-alpha"


def test_write_pending_idempotent(ops_root: Path) -> None:
    p1 = write_pending("dup", ops_root)
    p2 = write_pending("dup", ops_root)
    assert p1 == p2
    assert count_jobs("pending", ops_root) == 1
