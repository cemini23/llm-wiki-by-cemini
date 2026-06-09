#!/usr/bin/env python3
"""Build Tournament S1 super-audit pack for 5-model cursor-audit.

Usage:
  uv run python scripts/build_tournament_super_audit_pack.py
  uv run python scripts/build_tournament_super_audit_pack.py --out reports/gap-audit/pack-tournament-s1
"""
from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPT = ROOT / "prompts" / "tournament_s1_super_audit.md"
HL = ROOT / "reports" / "hl-loop"
DEFAULT_OUT = ROOT / "reports" / "gap-audit" / "pack-tournament-s1"


def _read_tail(path: Path, max_chars: int = 12000) -> str:
    if not path.is_file():
        return f"(missing: {path})"
    text = path.read_text(encoding="utf-8", errors="replace")
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + f"\n\n… truncated {len(text) - max_chars} chars …"


def _git_oneline_decide(n: int = 25) -> str:
    try:
        out = subprocess.check_output(
            ["git", "log", "--oneline", f"-{n}", "--", "examples/cemini_decide.py"],
            cwd=ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        )
        return out.strip()
    except Exception as e:
        return f"(git log failed: {e})"


def _playground_status() -> str:
    script = ROOT / "scripts" / "cemini_playground_status.sh"
    if not script.is_file():
        return "(no status script)"
    try:
        return subprocess.check_output(
            ["bash", str(script)],
            cwd=ROOT,
            text=True,
            stderr=subprocess.STDOUT,
            timeout=60,
        )
    except Exception as e:
        return f"(status failed: {e})"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = p.parse_args()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)

    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # Copy / summarize artifacts
    artifacts: dict[str, str] = {
        "state.json": _read_tail(HL / "state.json", 4000),
        "deploys.jsonl": _read_tail(HL / "deploys.jsonl", 15000),
        "eval_timeseries.jsonl": _read_tail(HL / "eval_timeseries.jsonl", 8000),
        "preflight_metrics.json": _read_tail(HL / "preflight_metrics.json", 4000),
        "latest_analyze.txt": _read_tail(HL / "latest_analyze.txt", 8000),
        "tournament_candidate.json": _read_tail(HL / "tournament_candidate.json", 4000),
        "playground_timeseries.jsonl": _read_tail(HL / "playground_timeseries.jsonl", 8000),
        "bb100_hero_analysis.md": _read_tail(
            ROOT / "reports/gap-audit/pack-s2-prep/bb100_hero_analysis.md", 4000
        ),
        "s2_heavy_audit_prompt_excerpt.md": _read_tail(
            ROOT / "reports/gap-audit/pack-s2-heavy/audit_prompt.md", 20000
        ),
        "git_decide_log.txt": _git_oneline_decide(30),
        "playground_status.txt": _playground_status(),
    }

    for name, body in artifacts.items():
        (out / name).write_text(body, encoding="utf-8")

    # Index for auditors
    index_lines = [
        f"# Tournament S1 super-audit pack — built {ts}",
        "",
        f"Root: `{ROOT}`",
        "",
        "## Read order",
        "",
    ]
    for name in artifacts:
        index_lines.append(f"- `{out / name}`")
    index_lines.extend(
        [
            "",
            "## Code paths (absolute)",
            f"- `{ROOT / 'examples/cemini_decide.py'}`",
            f"- `{ROOT / 'examples/run_cemini_lobby.py'}`",
            f"- `{ROOT / 'examples/qualification_guard.py'}`",
            f"- `{ROOT / 'examples/deploy_registry.py'}`",
            f"- `{ROOT / 'tests/fixtures/regression_spots.py'}`",
            f"- `{ROOT / 'docs/tournament-version-tracking.md'}`",
            "",
            "## Briefs",
            f"- `{ROOT / 'briefs/2026-06-08_s2-heavy-audit-synthesis-v2.md'}`",
            f"- `{ROOT / 'briefs/2026-06-06_s1a-premium-retrospective-synthesis.md'}`",
            f"- `{ROOT / 'briefs/2026-06-06_discord-meta-tournament-foundation.md'}`",
        ]
    )
    index_path = out / "PACK_INDEX.md"
    index_path.write_text("\n".join(index_lines), encoding="utf-8")

    if not PROMPT.is_file():
        print(f"Missing {PROMPT}", file=__import__("sys").stderr)
        return 1

    template = PROMPT.read_text(encoding="utf-8")
    audit_prompt = template.replace("{pack_index}", index_path.read_text(encoding="utf-8"))
    prompt_path = out / "audit_prompt.md"
    prompt_path.write_text(audit_prompt, encoding="utf-8")

    meta = {
        "built": ts,
        "out": str(out),
        "prompt_chars": len(audit_prompt),
        "artifacts": list(artifacts.keys()),
    }
    (out / "meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(meta, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
