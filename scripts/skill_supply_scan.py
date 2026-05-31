#!/usr/bin/env python3
"""Static supply-chain scan for agent skill trees via NVIDIA SkillSpector.

Always invokes ``skillspector scan`` with ``--no-llm`` (no LLM API keys).
Install first: ``bash scripts/install_skillspector_venv.sh``

Resolution order for the skillspector binary:
  1. ``--skillspector-bin`` CLI flag
  2. ``SKILLSPECTOR_BIN`` environment variable
  3. ``.local/skillspector-venv/bin/skillspector`` (repo-relative)
  4. ``skillspector`` on ``PATH``

Exit codes:
  0 — all targets at or below ``--max-severity`` (default LOW)
  1 — usage / configuration error (skillspector not found)
  2 — one or more targets exceed severity threshold (human review)
  3 — skillspector subprocess failed for at least one target
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parent.parent
DEFAULT_VENV_BIN = REPO / ".local" / "skillspector-venv" / "bin" / "skillspector"
DEFAULT_INBOX = REPO / "research to be indexed"

SEVERITY_RANK = {"LOW": 0, "MEDIUM": 1, "HIGH": 2, "CRITICAL": 3}
DEFAULT_MAX_SEVERITY = "LOW"


@dataclass
class TargetResult:
    path: str
    ok: bool
    severity: str | None = None
    score: int | None = None
    recommendation: str | None = None
    issue_count: int = 0
    error: str | None = None
    raw: dict[str, Any] | None = field(default=None, repr=False)


@dataclass
class ScanReport:
    skillspector_bin: str
    max_severity: str
    results: list[TargetResult] = field(default_factory=list)

    @property
    def worst_severity(self) -> str:
        worst = "LOW"
        for r in self.results:
            if r.severity and SEVERITY_RANK.get(r.severity, 0) > SEVERITY_RANK.get(worst, 0):
                worst = r.severity
        return worst

    @property
    def pass_gate(self) -> bool:
        limit = SEVERITY_RANK.get(self.max_severity, 0)
        for r in self.results:
            if not r.ok:
                return False
            if r.severity and SEVERITY_RANK.get(r.severity, 0) > limit:
                return False
        return True


def resolve_skillspector(explicit: str | None) -> Path | None:
    candidates: list[Path | str] = []
    if explicit:
        candidates.append(explicit)
    env = os.environ.get("SKILLSPECTOR_BIN")
    if env:
        candidates.append(env)
    candidates.append(DEFAULT_VENV_BIN)
    candidates.append("skillspector")
    for c in candidates:
        p = Path(c) if isinstance(c, str) and (c.startswith("/") or c.startswith(".")) else c
        found = shutil.which(str(p)) if not isinstance(p, Path) else (str(p) if Path(p).is_file() else None)
        if found and Path(found).is_file():
            return Path(found)
    return None


def parse_skillspector_json(payload: dict[str, Any]) -> tuple[str, int, str, int]:
    risk = payload.get("risk_assessment") or {}
    severity = str(risk.get("severity") or "LOW").upper()
    score = int(risk.get("score") or 0)
    recommendation = str(risk.get("recommendation") or "")
    issues = payload.get("issues") or []
    return severity, score, recommendation, len(issues)


def run_skillspector(
    bin_path: Path,
    target: Path,
    *,
    timeout: int = 300,
) -> TargetResult:
    target = target.resolve()
    if not target.exists():
        return TargetResult(path=str(target), ok=False, error=f"path not found: {target}")

    cmd = [
        str(bin_path),
        "scan",
        str(target),
        "--no-llm",
        "--format",
        "json",
    ]
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=str(REPO),
        )
    except subprocess.TimeoutExpired:
        return TargetResult(path=str(target), ok=False, error=f"timeout after {timeout}s")
    except OSError as exc:
        return TargetResult(path=str(target), ok=False, error=str(exc))

    stdout = (proc.stdout or "").strip()
    start = stdout.find("{")
    if start >= 0:
        try:
            payload = json.loads(stdout[start:])
            severity, score, recommendation, issue_count = parse_skillspector_json(payload)
            return TargetResult(
                path=str(target),
                ok=True,
                severity=severity,
                score=score,
                recommendation=recommendation,
                issue_count=issue_count,
                raw=payload,
            )
        except json.JSONDecodeError:
            pass

    if proc.returncode != 0:
        err = (proc.stderr or stdout or "").strip()
        return TargetResult(
            path=str(target),
            ok=False,
            error=err[:500] if err else f"skillspector exit {proc.returncode}",
        )

    return TargetResult(path=str(target), ok=False, error="no JSON object in skillspector output")


def discover_skill_roots(base: Path) -> list[Path]:
    """Find skill-like paths under *base* (inbox drops or repo skill dirs)."""
    found: list[Path] = []
    if not base.is_dir():
        return found

    for entry in sorted(base.iterdir()):
        if entry.name.startswith("."):
            continue
        if entry.is_file() and entry.suffix.lower() == ".zip":
            found.append(entry)
            continue
        if not entry.is_dir():
            continue
        if (entry / "SKILL.md").is_file():
            found.append(entry)
            continue
        for child in sorted(entry.iterdir()):
            if child.is_dir() and (child / "SKILL.md").is_file():
                found.append(child)
    return found


def discover_repo_skills() -> list[Path]:
    roots: list[Path] = []
    for rel in (".claude/skills", ".cursor/skills", ".agents/skills"):
        base = REPO / rel
        if not base.is_dir():
            continue
        for p in discover_skill_roots(base):
            roots.append(p)
    return roots


def scan_targets(
    targets: list[Path],
    *,
    bin_path: Path,
    max_severity: str,
    timeout: int = 300,
) -> ScanReport:
    report = ScanReport(skillspector_bin=str(bin_path), max_severity=max_severity)
    for t in targets:
        report.results.append(run_skillspector(bin_path, t, timeout=timeout))
    return report


def print_human(report: ScanReport) -> None:
    print(f"Skill supply scan (SkillSpector static / --no-llm)")
    print(f"  binary:        {report.skillspector_bin}")
    print(f"  max_severity:  {report.max_severity}")
    print()

    for r in report.results:
        name = Path(r.path).name
        if not r.ok:
            print(f"✖ {name}")
            print(f"   error: {r.error}")
        else:
            gate = SEVERITY_RANK.get(r.severity or "LOW", 0) <= SEVERITY_RANK.get(
                report.max_severity, 0
            )
            marker = "✅" if gate else "⚠️"
            print(f"{marker} {name}")
            print(
                f"   severity={r.severity} score={r.score} "
                f"recommendation={r.recommendation} issues={r.issue_count}"
            )
        print()

    print("---")
    if report.pass_gate:
        print(f"PASS — all {len(report.results)} target(s) at or below {report.max_severity}")
    else:
        print(
            f"REVIEW — worst severity {report.worst_severity} "
            f"(limit {report.max_severity}); human review before install/ingest"
        )


def report_to_json(report: ScanReport, *, include_raw: bool = False) -> dict[str, Any]:
    data: dict[str, Any] = {
        "skillspector_bin": report.skillspector_bin,
        "max_severity": report.max_severity,
        "pass": report.pass_gate,
        "worst_severity": report.worst_severity,
        "results": [],
    }
    for r in report.results:
        row = {k: v for k, v in asdict(r).items() if k != "raw"}
        if include_raw and r.raw is not None:
            row["raw"] = r.raw
        data["results"].append(row)
    return data


def exit_code(report: ScanReport) -> int:
    if any(not r.ok for r in report.results):
        return 3
    if not report.pass_gate:
        return 2
    return 0

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        "paths",
        nargs="*",
        help="Skill directory, SKILL.md, or .zip to scan",
    )
    p.add_argument(
        "--inbox",
        action="store_true",
        help=f"Scan skill-like drops in '{DEFAULT_INBOX.name}/' (.zip or dirs with SKILL.md)",
    )
    p.add_argument(
        "--repo-skills",
        action="store_true",
        help="Scan installed skills under .claude/skills, .cursor/skills, .agents/skills",
    )
    p.add_argument(
        "--skillspector-bin",
        default=None,
        help="Path to skillspector executable (else SKILLSPECTOR_BIN / .local venv / PATH)",
    )
    p.add_argument(
        "--max-severity",
        choices=tuple(SEVERITY_RANK),
        default=DEFAULT_MAX_SEVERITY,
        help=f"Fail (exit 2) if any target exceeds this band (default: {DEFAULT_MAX_SEVERITY})",
    )
    p.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON on stdout",
    )
    p.add_argument(
        "--include-raw",
        action="store_true",
        help="With --json, include full skillspector payload per target",
    )
    p.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Write JSON report to this path (always includes summary; --include-raw honored)",
    )
    p.add_argument(
        "--timeout",
        type=int,
        default=300,
        help="Per-target skillspector timeout in seconds (default: 300)",
    )
    return p


def collect_targets(args: argparse.Namespace) -> list[Path]:
    targets: list[Path] = [Path(p) for p in args.paths]
    if args.inbox:
        targets.extend(discover_skill_roots(DEFAULT_INBOX))
    if args.repo_skills:
        targets.extend(discover_repo_skills())
    # dedupe preserve order
    seen: set[str] = set()
    unique: list[Path] = []
    for t in targets:
        key = str(t.resolve()) if t.exists() else str(t)
        if key not in seen:
            seen.add(key)
            unique.append(t)
    return unique


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    bin_path = resolve_skillspector(args.skillspector_bin)
    if bin_path is None:
        print(
            "ERROR: skillspector not found. Run: bash scripts/install_skillspector_venv.sh",
            file=sys.stderr,
        )
        return 1

    targets = collect_targets(args)
    if not targets:
        print(
            "ERROR: no scan targets. Pass paths, or use --inbox / --repo-skills.",
            file=sys.stderr,
        )
        return 1

    report = scan_targets(
        targets,
        bin_path=bin_path,
        max_severity=args.max_severity,
        timeout=args.timeout,
    )

    payload = report_to_json(report, include_raw=args.include_raw)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print_human(report)
        if args.output:
            print(f"Report written: {args.output}")

    return exit_code(report)


if __name__ == "__main__":
    sys.exit(main())
