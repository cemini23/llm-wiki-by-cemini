#!/usr/bin/env python3
"""Append inbox triage snapshot to today's daily sweep file (Phase 2).

Called by inbox_notify.sh when files land in `research to be indexed/`.
Creates wiki/sweeps/YYYY-MM-DD-daily.md stub if the morning digest has not run yet.
"""

from __future__ import annotations

import re
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def inbox_files(repo: Path) -> list[Path]:
    inbox = repo / "research to be indexed"
    if not inbox.is_dir():
        return []
    return sorted(p for p in inbox.iterdir() if p.is_file() and not p.name.startswith("."))


def run_preingest(repo: Path) -> str:
    script = repo / "scripts" / "preingest_check.py"
    try:
        proc = subprocess.run(
            [sys.executable, str(script)],
            cwd=str(repo),
            capture_output=True,
            text=True,
            timeout=120,
            check=False,
        )
        return (proc.stdout or proc.stderr or "").strip()
    except (subprocess.TimeoutExpired, OSError) as e:
        return f"(preingest_check failed: {e})"


def render_inbox_section(files: list[Path], preingest: str, ts: str) -> str:
    lines = [
        "## Inbox (`research to be indexed/`)",
        "",
        f"_Updated {ts} by inbox_notify (WatchPaths)._",
        "",
    ]
    if files:
        lines.append(f"**{len(files)} file(s) waiting** — triage before ingest:")
        lines.append("")
        for p in files:
            lines.append(f"- `{p.name}`")
        lines.extend(["", "### preingest_check", "", "```", preingest[:4000], "```", ""])
    else:
        lines.append("_Empty — no manual drops pending._")
        lines.append("")
    return "\n".join(lines)


def replace_section(text: str, section: str) -> str:
    pattern = r"## Inbox \(`research to be indexed/`\)[\s\S]*?(?=\n---\n|\n## |\Z)"
    if re.search(pattern, text):
        return re.sub(pattern, section.rstrip() + "\n\n", text, count=1)
    marker = "---\n\n## Exa candidates"
    if marker in text:
        return text.replace(marker, "---\n\n" + section + "\n---\n\n## Exa candidates", 1)
    return text.rstrip() + "\n\n---\n\n" + section + "\n"


def minimal_daily_stub(today: date) -> str:
    return f"""# Daily Research Digest — {today.isoformat()}

_Inbox-only stub — morning digest not run yet. Run `bash scripts/daily_research_digest.sh` for Exa candidates._

Reference: `@scripts/daily_research_config.yaml`. **Does NOT ingest.**

---

"""


def main() -> int:
    repo = repo_root()
    today = date.today()
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = repo / "wiki" / "sweeps" / f"{today.isoformat()}-daily.md"
    report.parent.mkdir(parents=True, exist_ok=True)

    files = inbox_files(repo)
    preingest = run_preingest(repo) if files else "(inbox empty)"
    section = render_inbox_section(files, preingest, ts)

    if report.is_file():
        text = report.read_text(encoding="utf-8")
    else:
        text = minimal_daily_stub(today)

    report.write_text(replace_section(text, section), encoding="utf-8")
    print(f"Updated inbox section: {report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
