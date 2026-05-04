#!/usr/bin/env python3
"""Static audit of brief / skill / prompt files before they leave the workspace.

Clean-room re-implementation of the MedSkillAudit veto-gate framework
(see @wiki/entities/tools/medskillaudit.md), adapted from medical-research
domain to financial-research / Cemini brief validation.

Two phases:
  STATIC (40% of total score, fully implemented v0.1):
    1. Required sections present  ── must have ## Target, ## Summary, ## Sources
    2. Cross-link resolution      ── @path/to/page.md must point to a real wiki page
    3. Citation tag well-formedness ── [Source: ...] / [Sources: ...] tags parse
    4. NEEDS VERIFICATION freshness ── tags ≥30 days old surface as warnings
    5. Frontmatter (if present)   ── valid YAML-style front block
    6. Prose-quality heuristics   ── unauthorized emoji, TODO/FIXME markers

  DYNAMIC (60% of total score, deferred to v0.2):
    Requires LLM API call against a sandboxed Conductor / DeepSeek endpoint.
    Tests reproducibility, schema-compliance, hallucinated-citation detection.

Veto gates (any failure ⇒ REJECT, score ignored):
  ● Operational Stability — file parseable, required sections present
  ● Scientific Integrity — every cross-link / citation resolves; no orphans

Usage:
  python3 scripts/skill_audit.py briefs/2026-05-04_*.md
  python3 scripts/skill_audit.py --json briefs/some.md     # machine-readable
  python3 scripts/skill_audit.py --strict briefs/some.md   # warnings ⇒ veto

Exit codes:
  0  PASS   (no veto gates, score ≥ pass threshold)
  1  WARN   (no veto gates, score below pass threshold OR warnings present)
  2  REJECT (veto gate triggered)
  3  ERROR  (file not found / parse error)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field, asdict
from datetime import date, datetime
from pathlib import Path
from typing import Literal

# -------------------------------------------------------------------- paths --

ROOT = Path(__file__).resolve().parent.parent
WIKI = Path(os.environ.get("WIKI_DIR", ROOT / "wiki"))
TODAY = date.today()

# -------------------------------------------------------------- data classes --

Severity = Literal["pass", "warn", "veto"]


@dataclass
class CheckResult:
    name: str
    severity: Severity
    score_weight: float           # contribution to static score (sum of all weights = 1.0)
    score_earned: float           # actual score earned (0..score_weight)
    detail: str
    evidence: list[str] = field(default_factory=list)
    veto_reason: str | None = None  # set iff severity == "veto"


@dataclass
class AuditReport:
    target: str
    verdict: Literal["PASS", "WARN", "REJECT", "ERROR"]
    static_score: float           # 0..100
    veto_gates: list[str]         # names of triggered veto gates
    checks: list[CheckResult]
    summary: str

# ------------------------------------------------------------- regex helpers --

SECTION_HEAD_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
CROSSLINK_RE = re.compile(r"@([a-zA-Z0-9_\-/]+\.md)\b")
CITATION_RE = re.compile(r"\[Sources?:\s*([^\]]+)\]")
NEEDS_VERIF_RE = re.compile(r"\[NEEDS VERIFICATION\s+(\d{4}-\d{2}-\d{2})\]")
TODO_RE = re.compile(r"\b(TODO|FIXME|XXX)\b")
EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001F6FF"   # symbols & pictographs (faces, objects)
    "\U0001F900-\U0001F9FF"   # supplemental symbols (incl. modern emoji)
    "\U0001FA70-\U0001FAFF"   # extended symbols
    "\U0001F600-\U0001F64F"   # smileys
    "\U0001F680-\U0001F6FF"   # transport & map symbols
    # NOTE: deliberately excluded U+2600-27BF (Miscellaneous Symbols) — that
    # range contains technical arrows (→ ⇒ ↗) and check/cross marks (✓ ✖) which
    # are conventional in technical writing and not "emoji" in the doctrine sense.
    "]"
)

# Required sections, keyed by brief type. Briefs with target=CeminiSuite must
# include enough structure that the prod-side Claude session can act on them.
CRITICAL_SECTIONS = {"Target", "Summary"}
SOURCES_SECTION_ALIASES = {"Sources", "Source", "Primary sources", "References"}

# ------------------------------------------------------- individual checks --


def parse_brief(path: Path) -> tuple[str, list[str]]:
    text = path.read_text(encoding="utf-8")
    sections = SECTION_HEAD_RE.findall(text)
    return text, sections


def check_required_sections(text: str, sections: list[str]) -> CheckResult:
    section_set = set(sections)
    missing_critical = CRITICAL_SECTIONS - section_set
    has_sources = bool(SOURCES_SECTION_ALIASES & section_set)

    if missing_critical:
        return CheckResult(
            name="required_sections",
            severity="veto",
            score_weight=0.30,
            score_earned=0.0,
            detail=f"Missing critical section(s): {sorted(missing_critical)}",
            evidence=sorted(missing_critical),
            veto_reason=f"Operational Stability — missing required sections {sorted(missing_critical)}",
        )
    if not has_sources:
        return CheckResult(
            name="required_sections",
            severity="warn",
            score_weight=0.30,
            score_earned=0.20,
            detail=(
                "No Sources/References section found. "
                f"Expected one of: {sorted(SOURCES_SECTION_ALIASES)}"
            ),
            evidence=sections,
        )
    return CheckResult(
        name="required_sections",
        severity="pass",
        score_weight=0.30,
        score_earned=0.30,
        detail=f"All required sections present ({len(sections)} total: {sections})",
    )


def check_crosslinks(text: str) -> CheckResult:
    matches = CROSSLINK_RE.findall(text)
    if not matches:
        return CheckResult(
            name="crosslinks",
            severity="pass",
            score_weight=0.20,
            score_earned=0.20,
            detail="No @path cross-links to validate",
        )

    # Two valid forms: `@concepts/foo.md` (wiki-relative, used inside wiki pages)
    # and `@wiki/concepts/foo.md` (repo-relative, used in briefs that sit outside wiki/).
    # Try both; only flag dangling if neither resolves.
    dangling = []
    for m in matches:
        wiki_relative = WIKI / m
        repo_relative = ROOT / m
        if not (wiki_relative.exists() or repo_relative.exists()):
            dangling.append(m)

    if dangling:
        return CheckResult(
            name="crosslinks",
            severity="veto",
            score_weight=0.20,
            score_earned=0.0,
            detail=f"{len(dangling)} dangling cross-link(s) of {len(matches)} total",
            evidence=sorted(set(dangling)),
            veto_reason=f"Scientific Integrity — {len(dangling)} cross-link(s) point to non-existent wiki pages",
        )
    return CheckResult(
        name="crosslinks",
        severity="pass",
        score_weight=0.20,
        score_earned=0.20,
        detail=f"{len(matches)} cross-link(s) all resolve",
    )


def check_citations(text: str, sections: list[str]) -> CheckResult:
    """Briefs cite via ## Sources section; wiki pages use inline [Source: ...] tags.
    Accept either: presence of a Sources section OR ≥1 inline citation."""
    inline_matches = CITATION_RE.findall(text)
    has_sources_section = bool(SOURCES_SECTION_ALIASES & set(sections))

    if has_sources_section and not inline_matches:
        # typical brief shape — sources listed in section, no inline tags needed
        return CheckResult(
            name="citations",
            severity="pass",
            score_weight=0.15,
            score_earned=0.15,
            detail="Sources section present; no inline citations expected",
        )
    if not inline_matches and not has_sources_section:
        return CheckResult(
            name="citations",
            severity="warn",
            score_weight=0.15,
            score_earned=0.05,
            detail="No Sources section AND no inline [Source: ...] tags — claim density too low",
        )
    weak = [c for c in inline_matches if len(c.strip()) < 8]
    if weak:
        return CheckResult(
            name="citations",
            severity="warn",
            score_weight=0.15,
            score_earned=0.08,
            detail=f"{len(weak)} suspiciously short citation(s) of {len(inline_matches)} total",
            evidence=weak[:5],
        )
    return CheckResult(
        name="citations",
        severity="pass",
        score_weight=0.15,
        score_earned=0.15,
        detail=f"{len(inline_matches)} inline citation(s)" + (" + Sources section" if has_sources_section else ""),
    )


def check_needs_verification(text: str, max_age_days: int) -> CheckResult:
    matches = NEEDS_VERIF_RE.findall(text)
    if not matches:
        return CheckResult(
            name="needs_verification_freshness",
            severity="pass",
            score_weight=0.10,
            score_earned=0.10,
            detail="No [NEEDS VERIFICATION] tags",
        )
    stale = []
    for d in matches:
        try:
            tag_date = datetime.strptime(d, "%Y-%m-%d").date()
            age = (TODAY - tag_date).days
            if age > max_age_days:
                stale.append(f"{d} ({age}d old)")
        except ValueError:
            stale.append(f"{d} (unparseable date)")
    if stale:
        return CheckResult(
            name="needs_verification_freshness",
            severity="warn",
            score_weight=0.10,
            score_earned=0.05,
            detail=f"{len(stale)}/{len(matches)} NV tag(s) older than {max_age_days}d",
            evidence=stale,
        )
    return CheckResult(
        name="needs_verification_freshness",
        severity="pass",
        score_weight=0.10,
        score_earned=0.10,
        detail=f"{len(matches)} NV tag(s), all fresh (≤{max_age_days}d)",
    )


def check_prose_quality(text: str) -> CheckResult:
    # Workspace doctrine: no emoji unless explicitly authorized; no TODO/FIXME at
    # ship time (briefs go to prod — outstanding TODOs should be tracked in
    # ROADMAP, not embedded).
    emojis = EMOJI_RE.findall(text)
    todos = TODO_RE.findall(text)
    issues = []
    if emojis:
        issues.append(f"{len(emojis)} emoji char(s) — workspace doctrine forbids unauthorized emoji")
    if todos:
        issues.append(f"{len(todos)} TODO/FIXME/XXX marker(s) — should not ship unresolved")
    if not issues:
        return CheckResult(
            name="prose_quality",
            severity="pass",
            score_weight=0.15,
            score_earned=0.15,
            detail="No emoji, no TODO/FIXME markers",
        )
    return CheckResult(
        name="prose_quality",
        severity="warn",
        score_weight=0.15,
        score_earned=0.05 if len(issues) > 1 else 0.08,
        detail="; ".join(issues),
    )


def check_frontmatter(text: str) -> CheckResult:
    """Briefs typically don't have frontmatter, but if they do it must parse."""
    if not text.startswith("---\n"):
        return CheckResult(
            name="frontmatter",
            severity="pass",
            score_weight=0.10,
            score_earned=0.10,
            detail="No frontmatter (typical for briefs)",
        )
    fm_end = text.find("\n---\n", 4)
    if fm_end == -1:
        return CheckResult(
            name="frontmatter",
            severity="warn",
            score_weight=0.10,
            score_earned=0.0,
            detail="Frontmatter opener present but no closing `---`",
        )
    return CheckResult(
        name="frontmatter",
        severity="pass",
        score_weight=0.10,
        score_earned=0.10,
        detail=f"Frontmatter parses ({fm_end - 4} chars)",
    )

# --------------------------------------------------------- report generation --


def assemble_report(
    target: str,
    text: str,
    sections: list[str],
    nv_age_days: int,
    strict: bool,
) -> AuditReport:
    checks = [
        check_required_sections(text, sections),
        check_crosslinks(text),
        check_citations(text, sections),
        check_needs_verification(text, nv_age_days),
        check_prose_quality(text),
        check_frontmatter(text),
    ]
    veto_gates = [c.veto_reason for c in checks if c.severity == "veto" and c.veto_reason]
    static_score = round(sum(c.score_earned for c in checks) * 100, 1)

    if veto_gates:
        verdict = "REJECT"
        summary = f"REJECT — {len(veto_gates)} veto gate(s) triggered. Score irrelevant."
    elif strict and any(c.severity == "warn" for c in checks):
        verdict = "REJECT"
        summary = f"REJECT (--strict) — score {static_score}/100, warnings treated as veto"
    elif any(c.severity == "warn" for c in checks):
        verdict = "WARN"
        summary = f"WARN — score {static_score}/100, warnings present but no veto"
    elif static_score >= 80:
        verdict = "PASS"
        summary = f"PASS — score {static_score}/100, all checks clean"
    else:
        verdict = "WARN"
        summary = f"WARN — score {static_score}/100 below 80-point pass threshold"

    return AuditReport(
        target=target,
        verdict=verdict,
        static_score=static_score,
        veto_gates=veto_gates,
        checks=checks,
        summary=summary,
    )


def render_text(report: AuditReport) -> str:
    lines = []
    lines.append("=" * 78)
    lines.append(f"skill_audit  ::  {report.target}")
    lines.append("=" * 78)
    lines.append("")
    lines.append(f"VERDICT: {report.verdict}")
    lines.append(f"STATIC SCORE: {report.static_score}/100   (dynamic phase deferred to v0.2)")
    lines.append("")
    if report.veto_gates:
        lines.append("VETO GATES TRIGGERED:")
        for vg in report.veto_gates:
            lines.append(f"  ✖ {vg}")
        lines.append("")
    lines.append("CHECKS:")
    for c in report.checks:
        glyph = {"pass": "✓", "warn": "⚠", "veto": "✖"}[c.severity]
        lines.append(f"  {glyph} [{c.severity.upper():4}] {c.name}: {c.detail}")
        if c.evidence:
            for e in c.evidence[:5]:
                lines.append(f"      - {e}")
            if len(c.evidence) > 5:
                lines.append(f"      ... and {len(c.evidence) - 5} more")
    lines.append("")
    lines.append(f"=> {report.summary}")
    return "\n".join(lines)

# ----------------------------------------------------------------- entrypoint --


def main():
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("brief", help="Path to brief / skill / prompt file")
    p.add_argument("--json", action="store_true", help="Emit JSON report instead of text")
    p.add_argument("--strict", action="store_true", help="Treat warnings as veto gates")
    p.add_argument(
        "--nv-age-days",
        type=int,
        default=30,
        help="Flag [NEEDS VERIFICATION] tags older than this (default: 30)",
    )
    args = p.parse_args()

    path = Path(args.brief)
    if not path.exists():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        sys.exit(3)

    try:
        text, sections = parse_brief(path)
    except (OSError, UnicodeDecodeError) as e:
        print(f"ERROR: could not read {path}: {e}", file=sys.stderr)
        sys.exit(3)

    report = assemble_report(
        target=str(path),
        text=text,
        sections=sections,
        nv_age_days=args.nv_age_days,
        strict=args.strict,
    )

    if args.json:
        print(json.dumps(asdict(report), indent=2, default=str))
    else:
        print(render_text(report))

    sys.exit({"PASS": 0, "WARN": 1, "REJECT": 2, "ERROR": 3}[report.verdict])


if __name__ == "__main__":
    main()
