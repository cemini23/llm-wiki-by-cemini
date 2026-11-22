"""Tests for scripts/preingest_check.py — REVIEW vs DUPLICATE verdicts.

Run the CLI through subprocess so the module-level argparse block executes
exactly as it does for an operator.
"""

import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RUN = [sys.executable, str(REPO / "scripts" / "preingest_check.py")]

REPO_PAGE = """---
title: Example Harness repository documentation
type: source
updated: 2026-11-22
---

## Raw Concept
- **Title**: Example Harness
- **Type**: repository docs
- **URL**: https://github.com/example/harness

## Narrative
This page documents the harness repository.
"""

PAPER_PAGE = """---
title: Harness scaling laws paper
type: source
updated: 2026-11-22
---

## Raw Concept
- **Title**: Harness scaling laws
- **arXiv ID**: 2611.24845
- **URL**: https://arxiv.org/abs/2611.24845

## Narrative
This page documents the paper.
"""


def _make_tree(tmp_path: Path, wiki_pages: dict[str, str], inbox_files: dict[str, str]):
    sources = tmp_path / "wiki" / "osint" / "sources"
    sources.mkdir(parents=True, exist_ok=True)
    for name, body in wiki_pages.items():
        (sources / name).write_text(body, encoding="utf-8")

    inbox = tmp_path / "inbox" / "osint"
    inbox.mkdir(parents=True, exist_ok=True)
    for name, body in inbox_files.items():
        (inbox / name).write_text(body, encoding="utf-8")


def _run(tmp_path: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [
            *RUN,
            "--inbox",
            str(tmp_path / "inbox"),
            "--wiki",
            str(tmp_path / "wiki"),
        ],
        cwd=str(REPO),
        capture_output=True,
        text=True,
        check=False,
    )


def _verdict_line(stdout: str) -> str:
    for line in stdout.splitlines():
        if line.strip().startswith("verdict:"):
            return line
    raise AssertionError(f"no verdict line in stdout:\n{stdout}")


def test_paper_vs_repo_doc_returns_review(tmp_path):
    """A paper that cites a repo is not the page documenting that repo."""
    _make_tree(
        tmp_path,
        {"harness.md": REPO_PAGE},
        {
            "harness-paper.md": (
                "# Harness paper\n\n"
                "arXiv: 2611.24845\n\n"
                "Code: https://github.com/example/harness\n"
            )
        },
    )
    proc = _run(tmp_path)
    assert proc.returncode == 0, proc.stderr
    assert "REVIEW" in proc.stdout
    line = _verdict_line(proc.stdout)
    assert "DUPLICATE" not in line, line


def test_same_type_url_stays_duplicate(tmp_path):
    """Two repo docs that share a repo URL are the same artifact class."""
    _make_tree(
        tmp_path,
        {"harness.md": REPO_PAGE},
        {
            "harness-notes.md": (
                "# Harness repository notes\n\n"
                "Source: https://github.com/example/harness\n"
            )
        },
    )
    proc = _run(tmp_path)
    assert proc.returncode == 0, proc.stderr
    assert "DUPLICATE" in _verdict_line(proc.stdout)


def test_arxiv_match_still_duplicate(tmp_path):
    """An exact arXiv ID is an identity match, whatever the URL mix."""
    _make_tree(
        tmp_path,
        {"harness-paper.md": PAPER_PAGE},
        {
            "harness-study.md": (
                "# Harness scaling study\n\n"
                "- arXiv: 2611.24845\n"
                "- Code: https://github.com/other/harness-code\n"
            )
        },
    )
    proc = _run(tmp_path)
    assert proc.returncode == 0, proc.stderr
    assert "DUPLICATE" in _verdict_line(proc.stdout)
