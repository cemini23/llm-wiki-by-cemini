#!/usr/bin/env python3
"""WP2 tests: parse markdown signals + land posts."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from xsp_ops.brain import load_brain  # noqa: E402
from xsp_ops.land import run_land  # noqa: E402
from xsp_ops.parse_post import (  # noqa: E402
    parse_markdown_file,
    run_parse,
    slug_from_filename,
)
from xsp_ops.paths import ensure_layout, posts_path  # noqa: E402
from xsp_ops.sensor import run_sensor  # noqa: E402

FIXTURE_MD = """---
title: SOX and Semis — Regime Watch
url: https://www.macrocharts.com/p/sox-semis-regime
published: 2026-07-14
---

# SOX and Semis — Regime Watch

Markets dig into semiconductor breadth while yields drift.

Nvidia and TSMC sit at the center of the risk-on tape. CPI print next week.
"""


@pytest.fixture
def ops_root(tmp_path: Path) -> Path:
    ensure_layout(tmp_path)
    return tmp_path


@pytest.fixture
def inbox(tmp_path: Path) -> Path:
    d = tmp_path / "inbox"
    d.mkdir()
    path = d / "macro-charts-2026-07-14-sox-semis-regime.md"
    path.write_text(FIXTURE_MD, encoding="utf-8")
    return d


def test_slug_from_filename() -> None:
    assert slug_from_filename(Path("macro-charts-2026-07-14-foo-bar.md")) == "2026-07-14-foo-bar"
    assert "macrocharts" not in slug_from_filename(
        Path("substack-rss-macrocharts-2026-01-01-baz.md")
    ) or "2026" in slug_from_filename(Path("substack-rss-macrocharts-2026-01-01-baz.md"))


def test_parse_markdown_file_extracts_fields(tmp_path: Path) -> None:
    path = tmp_path / "macro-charts-2026-07-14-sox-semis-regime.md"
    path.write_text(FIXTURE_MD, encoding="utf-8")
    signal = parse_markdown_file(path)
    assert signal["title"] == "SOX and Semis — Regime Watch"
    assert "macrocharts.com" in signal["url"]
    assert signal["published"] == "2026-07-14"
    assert "semis" in signal["regime_tags"] or "rates" in signal["regime_tags"] or signal["regime_tags"]
    assert len(signal["excerpt"]) <= 500
    assert "semiconductor" in signal["excerpt"].lower() or "Nvidia" in signal["excerpt"]


def test_run_parse_and_land(ops_root: Path, inbox: Path) -> None:
    signals = run_parse(dry_run=False, root=ops_root, inbox=inbox)
    assert len(signals) == 1
    assert signals[0]["slug"]

    landed = run_land(dry_run=False, root=ops_root, signals=signals)
    assert len(landed) == 1
    slug = landed[0]
    post_file = posts_path(slug, ops_root)
    assert post_file.is_file()
    brain = load_brain(ops_root)
    assert slug in brain["post_ids"]
    assert any("macro-charts" in p for p in brain["known_paths"])


def test_parse_dry_run_no_brain_mark(ops_root: Path, inbox: Path) -> None:
    signals = run_parse(dry_run=True, root=ops_root, inbox=inbox)
    assert len(signals) == 1
    brain = load_brain(ops_root)
    assert signals[0]["slug"] not in (brain.get("parsed_slugs") or [])


def test_sensor_dry_run_appends_pull_log(ops_root: Path) -> None:
    out = run_sensor(dry_run=True, root=ops_root)
    assert out["dry_run"] is True
    brain = load_brain(ops_root)
    assert brain["last_pull_at"]
    assert brain["pull_log"]
    assert brain["pull_log"][-1]["dry_run"] is True
