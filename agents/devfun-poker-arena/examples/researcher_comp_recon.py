#!/usr/bin/env python3
"""Pre-submit recon for dev.fun Researcher / Challenge competitions.

Fetches Arena competition metadata, skillFile (when present), introspection
summary, and diffs against Playground S3 template — writes a markdown report
before first submit so optimization target is explicit.

Usage:
    uv run python examples/researcher_comp_recon.py
    uv run python examples/researcher_comp_recon.py --competition-id <id>
    uv run python examples/researcher_comp_recon.py --write-wiki-stub
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional
from urllib.parse import urljoin

from dotenv import load_dotenv

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from arena_client import ArenaClient, DEFAULT_BASE  # noqa: E402

_RESEARCHER_KEYS = (
    "researcher",
    "challenge",
    "sandbox",
    "benchflow",
    "heads-up",
    "head-to",
    "heads up",
)
_PLAYGROUND_TEMPLATE_ID = "cmqf827h30u7dfca3x2aqvzjv"
_SKILLS_BASE = "https://b-arena.dev.fun/skills/"


def _utc_ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _load_api_key(agent_dir: Path) -> str:
    creds = agent_dir / ".arena-credentials"
    if not creds.is_file():
        raise SystemExit(f"ERROR: missing {creds}")
    data = json.loads(creds.read_text(encoding="utf-8"))
    key = data.get("apiKey") or ""
    if not key:
        raise SystemExit("ERROR: .arena-credentials has no apiKey")
    return key


def _norm_comp_list(body: Any) -> list[dict]:
    if isinstance(body, list):
        return [c for c in body if isinstance(c, dict)]
    if isinstance(body, dict):
        data = body.get("data")
        if isinstance(data, list):
            return [c for c in data if isinstance(c, dict)]
    return []


def _is_researcher_candidate(comp: dict) -> bool:
    blob = f"{comp.get('name', '')} {comp.get('description', '')}".lower()
    return any(k in blob for k in _RESEARCHER_KEYS)


def _fetch_text(url: str) -> tuple[str, Optional[str]]:
    try:
        import httpx

        r = httpx.get(url, timeout=30.0, follow_redirects=True)
        if r.status_code != 200:
            return "", f"HTTP {r.status_code}"
        return r.text, None
    except Exception as e:
        return "", str(e)


def _skill_url(comp: dict) -> Optional[str]:
    raw = comp.get("skillFile")
    if not raw:
        return None
    if isinstance(raw, str) and raw.startswith("http"):
        return raw
    if isinstance(raw, str):
        return urljoin(_SKILLS_BASE, raw.lstrip("/"))
    return None


def _diff_fields(template: dict, target: dict) -> list[str]:
    keys = (
        "gameType",
        "description",
        "skillFile",
        "seasonNumber",
        "startAt",
        "endAt",
    )
    lines: list[str] = []
    for k in keys:
        a, b = template.get(k), target.get(k)
        if a != b:
            lines.append(f"- **{k}**: template={a!r} → target={b!r}")
    return lines


def _optimization_matrix(comp: dict, skill_text: str) -> list[str]:
    """Heuristic checklist from comp + skill prose — human confirms."""
    blob = (skill_text or "") + " " + comp.get("description", "")
    low = blob.lower()
    rows: list[str] = []

    def flag(label: str, patterns: tuple[str, ...]) -> str:
        hit = any(p in low for p in patterns)
        return f"| {label} | {'LIKELY' if hit else 'unclear'} | scan skillFile |"

    rows.append("| Signal | Read | Action if confirmed |")
    rows.append("|--------|------|---------------------|")
    rows.append(flag("6-max / multi-way", ("6-max", "6 max", "2-6", "2–6", "six-max")))
    rows.append(flag("Heads-up / HU", ("heads-up", "head to head", "head-to-head", " hu ")))
    rows.append(flag("Trajectory export", ("trajectory", "trace", "action log", "reasoning")))
    rows.append(flag("Multi-axis / cognitive", ("axis", "cognitive", "benchflow", "profile", "rubric")))
    rows.append(flag("Fixed hand block", ("500 hand", "500-hand", "fixed number", "reset stack")))
    rows.append(flag("Multi-day season", ("multi-day", "season", "days", "ongoing")))
    rows.append(flag("Entry fee / buy-in", ("entry fee", "buy-in", "buy in", "chips to enter")))
    return rows


def build_report(
    *,
    client: ArenaClient,
    competition_id: Optional[str],
    out_dir: Path,
) -> Path:
    list_body = client.get("/competition/list-all")
    comps = _norm_comp_list(list_body)
    candidates = [c for c in comps if _is_researcher_candidate(c)]
    active = _norm_comp_list(client.get("/competition/list-active"))

    target: Optional[dict] = None
    if competition_id:
        for c in comps:
            if c.get("id") == competition_id:
                target = c
                break
        if target is None:
            raise SystemExit(f"ERROR: competition id not found: {competition_id}")

    template = next((c for c in comps if c.get("id") == _PLAYGROUND_TEMPLATE_ID), {})

    introspection = client.get("/__introspection")
    intro_path = out_dir / "introspection.json"
    intro_path.write_text(json.dumps(introspection, indent=2) + "\n", encoding="utf-8")

    skill_text = ""
    skill_err: Optional[str] = None
    skill_path: Optional[Path] = None
    if target:
        url = _skill_url(target)
        if url:
            skill_text, skill_err = _fetch_text(url)
            if skill_text:
                skill_path = out_dir / "skillFile.md"
                skill_path.write_text(skill_text, encoding="utf-8")

    ts = _utc_ts()
    report_path = out_dir / f"recon-{ts}.md"
    lines: list[str] = [
        "# Researcher / Challenge competition recon",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        "",
        "## Eval is the gate",
        "",
        "Funnel: **sandbox eval (trajectory + multi-axis)** → top agents **published** "
        "→ challenge lane → stream finale. Optimize for **eval admission**, not Playground "
        "rank or Eval S1 500h bb/100 alone.",
        "",
        "See @wiki/concepts/devfun-researcher-pre-submit-recon.md",
        "",
        "## API snapshot",
        "",
        f"- Active competitions: {len(active)}",
        f"- Researcher/challenge candidates (name/desc filter): {len(candidates)}",
        "",
    ]

    if candidates:
        lines.append("### Candidate competitions")
        lines.append("")
        for c in candidates:
            lines.append(
                f"- `{c.get('id')}` — {c.get('name')} "
                f"(skillFile={c.get('skillFile')!r})"
            )
        lines.append("")
    else:
        lines.append("**No researcher/challenge candidate in list-all yet.** "
                     "Re-run daily until Jun 21.")
        lines.append("")

    if target:
        lines.extend([
            "## Target competition",
            "",
            f"- **id**: `{target.get('id')}`",
            f"- **name**: {target.get('name')}",
            f"- **description**: {target.get('description')}",
            f"- **gameType**: {target.get('gameType')}",
            f"- **skillFile**: {target.get('skillFile')}",
            f"- **seasonNumber**: {target.get('seasonNumber')}",
            "",
        ])
        if template:
            diff = _diff_fields(template, target)
            if diff:
                lines.append("### Diff vs Playground S3 template")
                lines.append("")
                lines.extend(diff)
                lines.append("")
        if skill_path:
            lines.append(f"Skill file saved: `{skill_path.name}`")
        elif skill_err:
            lines.append(f"Skill fetch error: {skill_err}")
        lines.append("")
        lines.extend(_optimization_matrix(target, skill_text))
        lines.append("")
        lines.extend([
            "## Operator decisions (fill before first hand)",
            "",
            "- [ ] **Table format** → set `CEMINI_TABLE_FORMAT=` (6max | hu | auto)",
            "- [ ] **Primary optimization** → trajectory + axis gates (not Playground chase)",
            "- [ ] **Lobby comp** → `ARENA_LOBBY_COMPETITION_ID` + `CEMINI_RESEARCHER_MODE=1`",
            "- [ ] **Sanitize** → `CEMINI_SANITIZE_OUTPUT=0` on Researcher submit path",
            "- [ ] **Match length** → smoke N hands vs full season cadence",
            "- [ ] **Entry economics** → buy-in / rebuy rules from skillFile",
            "- [ ] **Run gate** → `CEMINI_TABLE_FORMAT=<fmt> bash scripts/run_hu_sandbox_gate.sh --hands 500`",
            "",
        ])
    else:
        lines.append("Pass `--competition-id <id>` when Researcher comp appears.")
        lines.append("")

    lines.extend([
        "## Artifacts",
        "",
        f"- `{intro_path.name}` — live API introspection",
    ])
    if skill_path:
        lines.append(f"- `{skill_path.name}` — competition skillFile")

    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    (out_dir / "competition_candidates.json").write_text(
        json.dumps(candidates, indent=2) + "\n", encoding="utf-8",
    )
    if target:
        (out_dir / "target_competition.json").write_text(
            json.dumps(target, indent=2) + "\n", encoding="utf-8",
        )
    return report_path


def main(argv: list[str] | None = None) -> int:
    load_dotenv()
    p = argparse.ArgumentParser(description="Researcher competition pre-submit recon")
    p.add_argument("--competition-id", default=None, help="Pin specific competition id")
    p.add_argument(
        "--out-dir",
        type=Path,
        default=None,
        help="Output directory (default: reports/researcher-round/recon-<ts>)",
    )
    p.add_argument(
        "--write-wiki-stub",
        action="store_true",
        help="Also write wiki/sources stub under OSINT wiki (if path exists)",
    )
    args = p.parse_args(argv)

    agent_dir = _EXAMPLES.parent
    api_key = _load_api_key(agent_dir)
    base = __import__("os").environ.get("ARENA_API_BASE", DEFAULT_BASE)
    client = ArenaClient(base, api_key=api_key)

    ts = _utc_ts()
    out_dir = args.out_dir or Path(f"reports/researcher-round/recon-{ts}")
    out_dir.mkdir(parents=True, exist_ok=True)

    report = build_report(
        client=client,
        competition_id=args.competition_id,
        out_dir=out_dir,
    )
    print(f"[recon] report → {report}")

    if args.write_wiki_stub and report.is_file():
        wiki_root = agent_dir.parent.parent / "wiki" / "sources"
        if wiki_root.is_dir():
            stub = wiki_root / f"devfun-researcher-comp-recon-{ts[:10]}.md"
            body = report.read_text(encoding="utf-8")
            stub.write_text(
                "---\n"
                f"title: dev.fun Researcher comp recon {ts[:10]}\n"
                "type: source\n"
                "tags: [source, devfun, researcher-track]\n"
                "maturity: draft\n"
                f"created: {ts[:10]}\n"
                f"updated: {ts[:10]}\n"
                "---\n\n"
                "## Raw Concept\n\n"
                f"Auto-generated by `researcher_comp_recon.py`. Canonical report: `{report}`\n\n"
                "## Narrative\n\n"
                + body,
                encoding="utf-8",
            )
            print(f"[recon] wiki stub → {stub}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
