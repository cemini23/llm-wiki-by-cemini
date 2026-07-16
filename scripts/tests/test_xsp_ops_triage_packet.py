#!/usr/bin/env python3
"""WP3 tests: triage keyword mapping + packet filename/render."""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from intel.core.state import write_json  # noqa: E402

from xsp_ops.enqueue import run_enqueue  # noqa: E402
from xsp_ops.packet import run_packet  # noqa: E402
from xsp_ops.packet_render import packet_filename, render_packet_markdown  # noqa: E402
from xsp_ops.paths import ensure_layout, posts_path  # noqa: E402
from xsp_ops.queue import count_jobs, write_pending  # noqa: E402
from xsp_ops.scale import should_escalate  # noqa: E402
from xsp_ops.triage import run_triage  # noqa: E402
from xsp_ops.triage_rules import triage_post  # noqa: E402


@pytest.fixture
def ops_root(tmp_path: Path) -> Path:
    ensure_layout(tmp_path)
    return tmp_path


def test_triage_high_semis_packet() -> None:
    d = triage_post(
        {
            "title": "Nvidia and TSMC lead SOX",
            "excerpt": "Semiconductor regime still risk-on",
            "regime_tags": ["semis"],
        }
    )
    assert d["action"] == "packet"
    assert d["priority"] == "high"
    assert "nvidia" in d["matched_keywords"] or "tsmc" in d["matched_keywords"]


def test_triage_skip_no_keywords() -> None:
    d = triage_post({"title": "Quiet weekend recap", "excerpt": "No macro moves of note."})
    assert d["action"] == "skip"
    assert d["priority"] == "low"


def test_triage_med_rates() -> None:
    d = triage_post(
        {
            "title": "Yields and the Fed path",
            "excerpt": "Rates markets reprice before FOMC week.",
        }
    )
    assert d["action"] == "packet"
    assert d["priority"] in ("high", "med")  # fomc is high
    assert d["matched_keywords"]


def test_packet_filename() -> None:
    name = packet_filename("sox-semis-regime", day=date(2026, 7, 15))
    assert name == "2026-07-15_sox-semis-regime.md"


def test_render_packet_has_required_sections() -> None:
    md = render_packet_markdown(
        {
            "slug": "sox-semis",
            "title": "SOX Semis",
            "url": "https://example.com/p/x",
            "priority": "high",
            "action": "packet",
            "excerpt": "hello",
            "regime_tags": ["semis"],
            "matched_keywords": ["sox", "nvidia"],
        }
    )
    assert "## Target" in md
    assert "CeminiSuite / xsp-killer" in md
    assert "## Summary" in md
    assert "## Body" in md
    assert "briefs/" in md  # documents human promote only


def test_enqueue_triage_packet_flow(ops_root: Path) -> None:
    slug = "nvda-breadth"
    write_json(
        posts_path(slug, ops_root),
        {
            "slug": slug,
            "title": "NVIDIA breadth and SOX",
            "excerpt": "Semiconductor leadership with risk-on tone",
            "url": "https://www.macrocharts.com/p/nvda-breadth",
            "regime_tags": ["semis", "breadth"],
            "source_path": "/tmp/macro-charts-nvda.md",
        },
    )
    enq = run_enqueue(dry_run=False, root=ops_root)
    assert slug in enq
    assert count_jobs("pending", ops_root) == 1

    results = run_triage(dry_run=False, root=ops_root)
    assert len(results) == 1
    assert results[0]["action"] == "packet"
    assert count_jobs("done", ops_root) == 1
    assert count_jobs("pending", ops_root) == 0

    written = run_packet(dry_run=False, root=ops_root)
    assert len(written) == 1
    assert Path(written[0]).is_file()
    assert "briefs" not in written[0]
    assert str(ops_root / "packets") in written[0] or written[0].endswith(".md")

    # Idempotent second packet pass
    again = run_packet(dry_run=False, root=ops_root)
    assert again == []


def test_scale_threshold(ops_root: Path) -> None:
    for i in range(5):
        write_pending(f"p{i}", ops_root)
    snap = should_escalate(ops_root, threshold=5)
    assert snap["escalate"] is True
    assert "pending_ge_threshold" in snap["reasons"]

    snap2 = should_escalate(ops_root, threshold=10)
    assert snap2["escalate"] is False
