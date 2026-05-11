#!/usr/bin/env python3
"""Static audit of brief / skill / prompt files before they leave the workspace.

Clean-room re-implementation of the MedSkillAudit veto-gate framework
(see @wiki/entities/tools/medskillaudit.md), adapted from medical-research
domain to financial-research / Cemini brief validation.

Two phases:
  STATIC (100% of static score, fully implemented v0.3 — 10 checks):
    1. Required sections present  ── must have ## Target, ## Summary, ## Sources
    2. Cross-link resolution      ── @path/to/page.md must point to a real wiki page
    3. Citation tag well-formedness ── [Source: ...] / [Sources: ...] tags parse
    4. NEEDS VERIFICATION freshness ── tags ≥30 days old surface as warnings
    5. Prose-quality heuristics   ── unauthorized emoji, TODO/FIXME markers
    6. Frontmatter (if present)   ── valid YAML-style front block
    7. Regime-disclosure gate     ── evaluation-comparison claims must disclose regime variables (K33)
    8. Brief completeness         ── risks/phase/go-nogo/verdict/license checklist (K36 academic-paper-skills port)
    9. Risk discipline            ── Risks & mitigations depth: severity column, mitigation column, ≥2 rows (K36)
   10. Phasing                    ── Phase 1 minimum; Phase 2/3 + success criteria earn full credit (K36)

  DYNAMIC (deferred — LLM-as-judge tier; pending _llm_retry.py + DeepSeek budget):
    Requires LLM API call against a sandboxed Conductor / DeepSeek endpoint.
    Tests reproducibility, schema-compliance, hallucinated-citation detection.

Veto gates (any failure ⇒ REJECT, score ignored):
  ● Operational Stability — file parseable, required sections present
  ● Scientific Integrity — every cross-link / citation resolves; no orphans;
                                  evaluation-comparison claims disclose regime variables (K33)

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
SOURCES_SECTION_ALIASES = {"Sources", "Source", "Primary sources", "References", "Cross-references"}

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
            score_weight=0.25,
            score_earned=0.0,
            detail=f"Missing critical section(s): {sorted(missing_critical)}",
            evidence=sorted(missing_critical),
            veto_reason=f"Operational Stability — missing required sections {sorted(missing_critical)}",
        )
    if not has_sources:
        return CheckResult(
            name="required_sections",
            severity="warn",
            score_weight=0.25,
            score_earned=0.17,
            detail=(
                "No Sources/References section found. "
                f"Expected one of: {sorted(SOURCES_SECTION_ALIASES)}"
            ),
            evidence=sections,
        )
    return CheckResult(
        name="required_sections",
        severity="pass",
        score_weight=0.25,
        score_earned=0.25,
        detail=f"All required sections present ({len(sections)} total: {sections})",
    )


def check_crosslinks(text: str) -> CheckResult:
    matches = CROSSLINK_RE.findall(text)
    if not matches:
        return CheckResult(
            name="crosslinks",
            severity="pass",
            score_weight=0.15,
            score_earned=0.15,
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
            score_weight=0.15,
            score_earned=0.0,
            detail=f"{len(dangling)} dangling cross-link(s) of {len(matches)} total",
            evidence=sorted(set(dangling)),
            veto_reason=f"Scientific Integrity — {len(dangling)} cross-link(s) point to non-existent wiki pages",
        )
    return CheckResult(
        name="crosslinks",
        severity="pass",
        score_weight=0.15,
        score_earned=0.15,
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
            score_weight=0.10,
            score_earned=0.10,
            detail="No emoji, no TODO/FIXME markers",
        )
    return CheckResult(
        name="prose_quality",
        severity="warn",
        score_weight=0.10,
        score_earned=0.03 if len(issues) > 1 else 0.05,
        detail="; ".join(issues),
    )


def check_frontmatter(text: str) -> CheckResult:
    """Briefs typically don't have frontmatter, but if they do it must parse."""
    if not text.startswith("---\n"):
        return CheckResult(
            name="frontmatter",
            severity="pass",
            score_weight=0.05,
            score_earned=0.05,
            detail="No frontmatter (typical for briefs)",
        )
    fm_end = text.find("\n---\n", 4)
    if fm_end == -1:
        return CheckResult(
            name="frontmatter",
            severity="warn",
            score_weight=0.05,
            score_earned=0.0,
            detail="Frontmatter opener present but no closing `---`",
        )
    return CheckResult(
        name="frontmatter",
        severity="pass",
        score_weight=0.05,
        score_earned=0.05,
        detail=f"Frontmatter parses ({fm_end - 4} chars)",
    )

# ------------------------------------------------------ regime-disclosure --

REGIME_TRIGGER_PATTERNS = [
    r"\bbeats\b", r"\boutperforms\b", r"\bsurpasses\b",
    r"\bwins on\b", r"\bimproves over\b", r"\bimproved by \d+% over\b",
    r"\bbetter than\b", r"\bsuperior to\b",
    r"\bleading method\b", r"\bbest-performing\b",
    r"\b\d+(\.\d+)?%\s*(vs|against)\s*\w+",  # "X% vs Y" numeric comparisons
]
REGIME_DISCLOSURE_PATTERNS = [
    r"per-regime", r"by regime", r"regime-conditioned",
    r"regime mix", r"\bPRS\b", r"B/\|A\|", r"\bρ\b", r"prior rank correlation",
    r"single-regime", r"during \w+ regime",
]
REGIME_SCOPE_NARROWING = [
    r"\bpreliminary\b", r"\bexploratory\b", r"\bsingle-experiment\b",
    r"\bpilot\b", r"\bproof of concept\b", r"\bcase study\b",
]


def check_regime_disclosure(text: str) -> CheckResult:
    """Scientific Integrity gate: flag evaluation-comparison claims that lack
    regime disclosure (K33 Regime-Conditioned BO discipline).

    Verdicts:
      PASS   — no trigger phrases, OR triggers + disclosure present
      WARN   — triggers found, no disclosure, but scope-narrowing language present
      REJECT — triggers found, no disclosure, no scope-narrowing language
    """
    triggered = any(re.search(p, text, re.IGNORECASE) for p in REGIME_TRIGGER_PATTERNS)
    if not triggered:
        return CheckResult(
            name="regime_disclosure",
            severity="pass",
            score_weight=0.10,
            score_earned=0.10,
            detail="no evaluation-comparison claims detected",
        )
    disclosed = any(re.search(p, text, re.IGNORECASE) for p in REGIME_DISCLOSURE_PATTERNS)
    if disclosed:
        return CheckResult(
            name="regime_disclosure",
            severity="pass",
            score_weight=0.10,
            score_earned=0.10,
            detail="evaluation-comparison claim with regime disclosure",
        )
    narrowed = any(re.search(p, text, re.IGNORECASE) for p in REGIME_SCOPE_NARROWING)
    if narrowed:
        return CheckResult(
            name="regime_disclosure",
            severity="warn",
            score_weight=0.10,
            score_earned=0.05,
            detail="evaluation-comparison claim narrowed but no formal regime disclosure",
        )
    return CheckResult(
        name="regime_disclosure",
        severity="veto",
        score_weight=0.10,
        score_earned=0.0,
        detail="evaluation-comparison claim without regime disclosure (K33 No-Free-Leaderboard)",
        veto_reason="Scientific Integrity — evaluation-comparison claim lacks regime disclosure (B/|A|, ρ, PRS, or per-regime breakdown)",
    )


# -------------------- peer-review framework (K32 academic-paper-skills) ------
# Three new static checks ported from lishix520/academic-paper-skills (MIT)
# final_evaluation.py 7-dimension / completeness-checklist framework, translated
# to the Cemini adoption-brief shape. The three new checks together consume the
# 0.10 weight headroom left by the v0.2 check set.

PHASE_SECTION_RE = re.compile(r"^#{2,3}\s+Phase\s*\d", re.MULTILINE | re.IGNORECASE)
RISK_SECTION_TITLES = (
    "Risks", "Risks & mitigations", "Risks and mitigations", "Risk", "Risk assessment",
    "Risks and gating conditions", "Risks & gating conditions",
)
LICENSE_SECTION_TITLES = ("License", "License posture", "Licensing", "License & IP")
ARCHITECTURE_SECTION_TITLES = ("Architecture", "Design", "System architecture", "Integration architecture")
VERDICT_LINE_RE = re.compile(r"\*\*(GO|NO-GO|CONDITIONAL-?GO)\*\*", re.IGNORECASE)
SUCCESS_CRITERIA_RE = re.compile(
    r"^#{2,3}\s+(Success criteria|Triggers|GO criteria|Acceptance criteria|Promotion criteria|Done when)",
    re.MULTILINE | re.IGNORECASE,
)


def _is_adoption_brief(text: str, target: str) -> bool:
    """Heuristic gate: is this an adoption-decision brief, or an ops/research one?
    Adoption-class new-checks (completeness, risk_discipline, phasing) apply only
    to adoption briefs; ops/research briefs PASS with N/A."""
    name = Path(target).name.lower()
    if "adoption" in name or "prod-adoption" in name:
        return True
    if PHASE_SECTION_RE.search(text):
        return True
    if VERDICT_LINE_RE.search(text):
        return True
    return False


def _section_title_match(sections: list[str], candidates: tuple[str, ...]) -> bool:
    """Match section title by prefix (case-insensitive). 'Phase 1 (init)' matches 'Phase 1'."""
    candidates_lower = tuple(c.lower() for c in candidates)
    for s in sections:
        s_lower = s.lower()
        for c in candidates_lower:
            if s_lower == c or s_lower.startswith(c + " ") or s_lower.startswith(c + "—") or s_lower.startswith(c + " —"):
                return True
    return False


def _section_body(text: str, title_candidates: tuple[str, ...]) -> str | None:
    """Return the body text of the first ## section whose title matches any
    candidate (case-insensitive, exact match on header text). None if absent."""
    pattern = re.compile(
        r"^##\s+(" + "|".join(re.escape(t) for t in title_candidates) + r")\s*$",
        re.MULTILINE | re.IGNORECASE,
    )
    m = pattern.search(text)
    if not m:
        return None
    start = m.end()
    next_section = re.search(r"^##\s+", text[start:], re.MULTILINE)
    end = start + next_section.start() if next_section else len(text)
    return text[start:end]


def check_brief_completeness(text: str, sections: list[str], target: str) -> CheckResult:
    """Completeness-checklist analog (K32 academic-paper-skills final_evaluation).
    Five required structural items for a well-formed adoption brief.
    Weight 0.05; partial credit at 1pt per item. Ops/research briefs skip with full credit."""
    if not _is_adoption_brief(text, target):
        return CheckResult(
            name="brief_completeness",
            severity="pass",
            score_weight=0.05,
            score_earned=0.05,
            detail="N/A — not an adoption-decision brief; ops/research briefs exempt",
        )

    items = {
        "risks_section": _section_title_match(sections, RISK_SECTION_TITLES),
        "phase_section": bool(PHASE_SECTION_RE.search(text)),
        "architecture_section": _section_title_match(sections, ARCHITECTURE_SECTION_TITLES),
        "verdict_line": bool(VERDICT_LINE_RE.search(text)),
        "license_section": _section_title_match(sections, LICENSE_SECTION_TITLES),
    }
    present = sum(items.values())
    missing = sorted(k for k, v in items.items() if not v)
    score_earned = round((present / 5) * 0.05, 3)
    if present == 5:
        return CheckResult(
            name="brief_completeness",
            severity="pass",
            score_weight=0.05,
            score_earned=0.05,
            detail="All 5 completeness items present (risks/phase/architecture/verdict/license)",
        )
    return CheckResult(
        name="brief_completeness",
        severity="warn",
        score_weight=0.05,
        score_earned=score_earned,
        detail=f"{present}/5 completeness items present; missing: {missing}",
        evidence=missing,
    )


def check_risk_discipline(text: str, target: str) -> CheckResult:
    """Methodological-rigor analog (K32 academic-paper-skills, dim 5). For an
    adoption brief, methodological rigor is the depth of the Risks & mitigations
    analysis. Weight 0.03. Ops/research briefs skip with full credit."""
    if not _is_adoption_brief(text, target):
        return CheckResult(
            name="risk_discipline",
            severity="pass",
            score_weight=0.03,
            score_earned=0.03,
            detail="N/A — not an adoption-decision brief; ops/research briefs exempt",
        )

    body = _section_body(text, RISK_SECTION_TITLES)
    if body is None:
        return CheckResult(
            name="risk_discipline",
            severity="warn",
            score_weight=0.03,
            score_earned=0.0,
            detail="No Risks & mitigations section found",
        )

    table_lines = [ln for ln in body.splitlines() if ln.strip().startswith("|") and ln.strip().endswith("|")]
    if len(table_lines) < 3:
        # No table — check for bullet-list format. Top-level bullets with bold prefix
        # like `- **Risk name**:` count as structured risk items (partial credit).
        bullet_re = re.compile(r"^-\s+\*\*[^*]+\*\*\s*[:—\-]", re.MULTILINE)
        bullets = bullet_re.findall(body)
        if len(bullets) >= 2:
            return CheckResult(
                name="risk_discipline",
                severity="warn",
                score_weight=0.03,
                score_earned=0.02,
                detail=f"{len(bullets)} risk bullets (bold-prefix format; table format earns full credit)",
            )
        return CheckResult(
            name="risk_discipline",
            severity="warn",
            score_weight=0.03,
            score_earned=0.01,
            detail=f"Risks section present but no parseable table or structured bullets",
        )

    header = table_lines[0].lower()
    has_severity = "severity" in header
    has_mitigation = "mitigation" in header or "mitigations" in header
    rows = table_lines[2:]  # skip header + separator
    risk_count = len(rows)

    empty_mitigations = 0
    if has_mitigation:
        for r in rows:
            cells = [c.strip() for c in r.strip("|").split("|")]
            if cells and not cells[-1]:
                empty_mitigations += 1

    score = 0.03
    issues = []
    if not has_severity:
        score -= 0.01
        issues.append("no Severity column")
    if not has_mitigation:
        score -= 0.01
        issues.append("no Mitigation column")
    if risk_count < 2:
        score -= 0.005
        issues.append(f"only {risk_count} risk row(s) (expected ≥2)")
    if empty_mitigations > 0:
        score -= 0.005
        issues.append(f"{empty_mitigations} risk row(s) with empty mitigation")
    score = max(0.0, round(score, 3))

    if not issues:
        return CheckResult(
            name="risk_discipline",
            severity="pass",
            score_weight=0.03,
            score_earned=0.03,
            detail=f"{risk_count} risk rows with Severity + Mitigation columns, all populated",
        )
    return CheckResult(
        name="risk_discipline",
        severity="warn",
        score_weight=0.03,
        score_earned=score,
        detail=f"{risk_count} risk rows; issues: {issues}",
        evidence=issues,
    )


def check_phasing(text: str, sections: list[str], target: str) -> CheckResult:
    """Structure/organization analog (K32 academic-paper-skills, dim 6). Brief
    must scope Phase 1 minimum; Phase 2/3 + success criteria earn full credit.
    Weight 0.02. Ops/research briefs skip with full credit."""
    if not _is_adoption_brief(text, target):
        return CheckResult(
            name="phasing",
            severity="pass",
            score_weight=0.02,
            score_earned=0.02,
            detail="N/A — not an adoption-decision brief; ops/research briefs exempt",
        )

    phase_matches = PHASE_SECTION_RE.findall(text)
    phase_count = len(phase_matches)
    has_success_criteria = bool(SUCCESS_CRITERIA_RE.search(text))

    if phase_count == 0:
        return CheckResult(
            name="phasing",
            severity="warn",
            score_weight=0.02,
            score_earned=0.0,
            detail="No Phase 1/2/3 scoping sections found",
        )
    if phase_count >= 2 and has_success_criteria:
        return CheckResult(
            name="phasing",
            severity="pass",
            score_weight=0.02,
            score_earned=0.02,
            detail=f"{phase_count} Phase sections + explicit success/promotion criteria",
        )
    if phase_count >= 2:
        return CheckResult(
            name="phasing",
            severity="pass",
            score_weight=0.02,
            score_earned=0.015,
            detail=f"{phase_count} Phase sections (no explicit success/promotion criteria section)",
        )
    if has_success_criteria:
        return CheckResult(
            name="phasing",
            severity="warn",
            score_weight=0.02,
            score_earned=0.01,
            detail=f"Only {phase_count} Phase section (consider Phase 2/3 scoping)",
        )
    return CheckResult(
        name="phasing",
        severity="warn",
        score_weight=0.02,
        score_earned=0.005,
        detail=f"Only {phase_count} Phase section, no success/promotion criteria",
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
        check_regime_disclosure(text),
        check_brief_completeness(text, sections, target),
        check_risk_discipline(text, target),
        check_phasing(text, sections, target),
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
    lines.append(f"STATIC SCORE: {report.static_score}/100   (10 static checks; LLM-as-judge dynamic phase deferred)")
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
