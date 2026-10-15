#!/usr/bin/env python3
"""Static audit of brief / skill / prompt files before they leave the workspace.

Clean-room re-implementation of the MedSkillAudit veto-gate framework
(see @wiki/entities/tools/medskillaudit.md), adapted from medical-research
domain to financial-research / Cemini brief validation.

Two phases:
  STATIC (100% of static score, fully implemented v0.4 — 12 checks):
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
   11. Claim-evidence alignment  ── license/star/version/commit claims must co-locate with verification anchor (K32 research-paper-writing-skills port)
    12. Abstract synthesis        ── ## Summary length + effort estimate + verdict-flavored opener (K32 research-paper-writing-skills port)
    13. Harness dimensions        ── adoption/phase-0 briefs must name ≥4 of 6 system-scaling dimensions (K94)

  DYNAMIC (opt-in via --llm-mode, advisory by default — v0.5):
    Calls DeepSeek (via scripts/_llm_retry.py 3-tier retry) with a combined prompt
    distilled from Kappaemme-git/codex-startup-pressure-test-skill's four modes
    (pressure-test / problem-validation / competition-map / mvp-plan), re-styled
    for tool-adoption brief context. Returns a structured Pydantic verdict:
      verdict ∈ {ship, ship-with-fixes, rework, reject}
      fatal_flaws[]: per-mode severity-ranked findings with disconfirming fast-test
      competition_check: does Cemini already cover this? is displacement justified?
      summary: 2-3 sentence brutal overall read

    Dynamic output is advisory by default (renders alongside static checks but
    does not change the static score). With --strict-dynamic, a "reject" verdict
    upgrades the top-level verdict to REJECT.

Veto gates (any failure ⇒ REJECT, score ignored):
  ● Operational Stability — file parseable, required sections present
  ● Scientific Integrity — every cross-link / citation resolves; no orphans;
                                  evaluation-comparison claims disclose regime variables (K33)

Usage:
  python3 scripts/skill_audit.py briefs/2026-05-04_*.md
  python3 scripts/skill_audit.py --json briefs/some.md     # machine-readable
  python3 scripts/skill_audit.py --strict briefs/some.md   # warnings ⇒ veto
  python3 scripts/skill_audit.py --llm-mode briefs/some.md           # +dynamic (advisory)
  python3 scripts/skill_audit.py --llm-mode --strict-dynamic ...     # +dynamic (veto on reject)

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
import shutil
import subprocess
import sys
from dataclasses import dataclass, field, asdict
from datetime import date, datetime
from pathlib import Path
from typing import Literal

# -------------------------------------------------------------------- paths --

ROOT = Path(__file__).resolve().parent.parent
# Audited briefs are OSINT briefs, so a bare `concepts/x.md` means the osint domain. Before
# the federation merge `ROOT/wiki` was the whole osint wiki; it is now `ROOT/wiki/osint`.
# Cross-wiki `@<alias>/…` references resolve through WIKI_ALIASES, which loads in-tree.
WIKI = Path(os.environ.get("WIKI_DIR", ROOT / "wiki" / "osint"))
TODAY = date.today()


def load_wiki_aliases() -> dict[str, tuple[Path, ...]]:
    """Parse the CLAUDE.md 'Related Wikis' table into alias -> candidate bases.

    Briefs copied into a sibling wiki cite this wiki as `@osint-wiki/<path>`, which
    the alias resolves to this repo's `wiki/`. Some cite files outside `wiki/`
    (`LESSONS.md`, `scripts/...`, `briefs/...`), so each alias yields two ordered
    bases: the wiki directory, then the directory that owns it. Mirrors
    `load_wiki_aliases` in the `vet` package (src/vet/config.py).
    """
    claude_md = ROOT / "CLAUDE.md"
    aliases: dict[str, tuple[Path, ...]] = {}
    if not claude_md.is_file():
        return aliases
    try:
        text = claude_md.read_text(errors="replace")
    except OSError:
        return aliases
    table_re = re.compile(
        r"^\|\s*`([a-z0-9_-]+)`\s*\|\s*`?([^`\n\|]+)`?\s*\|",
        re.MULTILINE,
    )
    for m in table_re.finditer(text):
        alias = m.group(1).strip()
        path_str = m.group(2).strip().rstrip("/")
        if not alias or not path_str:
            continue
        base = (ROOT / path_str).resolve()
        if not base.is_dir() and (base / "wiki").is_dir():
            base = base / "wiki"
        if base.is_dir():
            aliases[alias] = (base, base.parent)
    return aliases


WIKI_ALIASES = load_wiki_aliases()

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
class DynamicFinding:
    mode: str                      # pressure-test | problem-validation | competition-map | mvp-plan
    severity: str                  # high | medium | low
    description: str               # 1-2 sentence flaw
    fast_test: str                 # how to disconfirm in <1 day


@dataclass
class DynamicAudit:
    verdict: str                   # ship | ship-with-fixes | rework | reject
    fatal_flaws: list[DynamicFinding]
    competition_check: str         # what Cemini already does; is displacement justified
    summary: str                   # 2-3 sentence overall read
    model: str                     # which DeepSeek model produced this
    latency_ms: int                # round-trip including retries


@dataclass
class AuditReport:
    target: str
    verdict: Literal["PASS", "WARN", "REJECT", "ERROR"]
    static_score: float           # 0..100
    veto_gates: list[str]         # names of triggered veto gates
    checks: list[CheckResult]
    summary: str
    dynamic: DynamicAudit | None = None  # v0.5: opt-in via --llm-mode

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

# ---- v0.4 patterns: claim-evidence + abstract synthesis (K32 research-paper-writing-skills) ----

# License names that count as a verifiable claim. SPDX-ish identifiers.
LICENSE_CLAIM_RE = re.compile(
    r"\b(MIT|Apache-?2\.0|AGPL-?3\.0|GPL-?3\.0|GPL-?2\.0|BSD-?2|BSD-?3|MPL-?2\.0|"
    r"LGPL|ISC|Unlicense|proprietary|unlicensed)\b",
    re.IGNORECASE,
)
# Maturity claims: star counts, version, commit count, release tags.
STAR_COUNT_RE = re.compile(r"\b\d{1,3}(?:,\d{3})*\s*(?:stars?|★|⭐)\b", re.IGNORECASE)
VERSION_RE = re.compile(r"\bv\d+\.\d+(?:\.\d+)?(?:-[a-z0-9]+)?\b")
COMMITS_RE = re.compile(r"\b\d{1,5}\s+commits?\b", re.IGNORECASE)
RELEASE_DATE_RE = re.compile(r"\blast (?:commit|push|release)\s+\d{4}-\d{2}-\d{2}\b", re.IGNORECASE)

# Verification anchors: signals that a claim has been audited / sourced / dated.
VERIFIED_ANCHOR_RE = re.compile(
    r"\bVERIFIED\s+\d{4}-\d{2}-\d{2}|"
    r"\bPhase-?0 audit|"
    r"\baudit (?:complete|✓|cleared|2\d{3}-\d{2}-\d{2})|"
    r"\b✓\s*COMPLETE|"
    r"\[Source[s]?:|"
    r"\[NEEDS VERIFICATION|"
    r"\[CONFIRMED\]|\[TENTATIVE\]|\[RETRACTED\]",
    re.IGNORECASE,
)

# Abstract synthesis signals (within ## Summary section).
EFFORT_HINT_RE = re.compile(r"\beffort\b|\bestimate\b|\*\*\d+(?:-\d+)?\s*(?:hr|hour|day|week|min)", re.IGNORECASE)
VERDICT_OPENER_RE = re.compile(
    r"^\s*(?:Adopt|Steal-from|Reject|Reference|Defer|Install|GO|NO-?GO|CONDITIONAL-?GO|"
    r"This brief|Adoption recommendation|Recommendation:?)\b",
    re.IGNORECASE | re.MULTILINE,
)

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

    # Three valid forms:
    #   `@concepts/foo.md`            wiki-relative (used inside wiki pages)
    #   `@wiki/concepts/foo.md`       repo-relative (briefs that sit outside wiki/)
    #   `@osint-wiki/concepts/foo.md` cross-wiki alias, one row per entry in the
    #                                 CLAUDE.md 'Related Wikis' table.
    # Resolve aliases against that table; only flag dangling if none resolves.
    dangling = []
    for m in matches:
        if (WIKI / m).is_file() or (ROOT / m).is_file():
            continue
        alias, sep, rest = m.partition("/")
        if sep and rest and any(
            (base / rest).is_file() for base in WIKI_ALIASES.get(alias, ())
        ):
            continue
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
    Accept either: presence of a Sources section OR ≥1 inline citation.
    Weight 0.10 (was 0.15 in v0.3; 0.05 released to claim_evidence in v0.4)."""
    inline_matches = CITATION_RE.findall(text)
    has_sources_section = bool(SOURCES_SECTION_ALIASES & set(sections))

    if has_sources_section and not inline_matches:
        return CheckResult(
            name="citations",
            severity="pass",
            score_weight=0.10,
            score_earned=0.10,
            detail="Sources section present; no inline citations expected",
        )
    if not inline_matches and not has_sources_section:
        return CheckResult(
            name="citations",
            severity="warn",
            score_weight=0.10,
            score_earned=0.03,
            detail="No Sources section AND no inline [Source: ...] tags — claim density too low",
        )
    weak = [c for c in inline_matches if len(c.strip()) < 8]
    if weak:
        return CheckResult(
            name="citations",
            severity="warn",
            score_weight=0.10,
            score_earned=0.05,
            detail=f"{len(weak)} suspiciously short citation(s) of {len(inline_matches)} total",
            evidence=weak[:5],
        )
    return CheckResult(
        name="citations",
        severity="pass",
        score_weight=0.10,
        score_earned=0.10,
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
    # Weight 0.05 (was 0.10 in v0.3; 0.05 released to abstract_synthesis in v0.4).
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
            score_weight=0.05,
            score_earned=0.05,
            detail="No emoji, no TODO/FIXME markers",
        )
    return CheckResult(
        name="prose_quality",
        severity="warn",
        score_weight=0.05,
        score_earned=0.015 if len(issues) > 1 else 0.025,
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


def _claim_has_anchor_nearby(text: str, span: tuple[int, int], radius_chars: int = 240) -> bool:
    """Check whether a verification anchor appears within `radius_chars` of `span`.
    Use char window not line window because adoption briefs commonly use tables;
    same-cell verification (e.g. `| MIT | YES — clean | Verified via Phase-0 audit |`)
    should count as anchored."""
    lo = max(0, span[0] - radius_chars)
    hi = min(len(text), span[1] + radius_chars)
    return bool(VERIFIED_ANCHOR_RE.search(text[lo:hi]))


def check_claim_evidence(text: str, target: str) -> CheckResult:
    """K32 research-paper-writing-skills port: claim-evidence alignment.
    For an adoption brief, license/star/version/commit claims are verifiable
    facts about the target tool. Each such claim should co-locate with a
    verification anchor (Phase-0 audit, citation, VERIFIED tag, NV tag).
    Weight 0.06. Ops/research briefs skip with full credit."""
    if not _is_adoption_brief(text, target):
        return CheckResult(
            name="claim_evidence",
            severity="pass",
            score_weight=0.06,
            score_earned=0.06,
            detail="N/A — not an adoption-decision brief; ops/research briefs exempt",
        )

    # Strip code blocks before scanning — version-like strings inside fenced code
    # are example commands, not claims about the tool itself.
    scan_text = re.sub(r"```[\s\S]*?```", "", text)

    claim_patterns = [
        ("license", LICENSE_CLAIM_RE),
        ("stars", STAR_COUNT_RE),
        ("version", VERSION_RE),
        ("commits", COMMITS_RE),
        ("release", RELEASE_DATE_RE),
    ]
    # Group claim occurrences by (label, canonical-value). A claim is "anchored"
    # if ANY of its occurrences has a verification anchor nearby — once a fact
    # is verified, restating it elsewhere in the brief is fine.
    claims_by_value: dict[tuple[str, str], list[tuple[int, int]]] = {}
    for label, pat in claim_patterns:
        for m in pat.finditer(scan_text):
            canonical = m.group(0).lower().replace(" ", "").replace("-", "")
            claims_by_value.setdefault((label, canonical), []).append(m.span())

    total_claims = len(claims_by_value)
    anchored = 0
    unanchored_samples: list[str] = []
    for (label, canonical), spans in claims_by_value.items():
        if any(_claim_has_anchor_nearby(scan_text, sp) for sp in spans):
            anchored += 1
        else:
            sp0 = spans[0]
            snippet = scan_text[max(0, sp0[0] - 20):sp0[1] + 20].replace("\n", " ").strip()
            unanchored_samples.append(f"{label}: …{snippet}…")

    if total_claims == 0:
        return CheckResult(
            name="claim_evidence",
            severity="pass",
            score_weight=0.06,
            score_earned=0.06,
            detail="No license/star/version/commit claims to verify (rare for adoption briefs; may indicate thin Background)",
        )

    coverage = anchored / total_claims
    if coverage >= 0.90:
        score, sev, glyph = 0.06, "pass", "all"
    elif coverage >= 0.70:
        score, sev, glyph = 0.04, "warn", "most"
    elif coverage >= 0.50:
        score, sev, glyph = 0.02, "warn", "half"
    else:
        score, sev, glyph = 0.0, "warn", "few"

    detail = f"{anchored}/{total_claims} claims anchored ({coverage:.0%}) — {glyph} cover"
    return CheckResult(
        name="claim_evidence",
        severity=sev,
        score_weight=0.06,
        score_earned=score,
        detail=detail,
        evidence=unanchored_samples[:5],
    )


def check_abstract_synthesis(text: str, target: str) -> CheckResult:
    """K32 research-paper-writing-skills port: abstract synthesis quality.
    The ## Summary section is the brief's abstract. Three quality signals:
    (a) length in 50-400 words (not stub, not bleed-over), (b) explicit effort
    estimate, (c) verdict-flavored opening sentence (Adopt/Steal/Reject/GO/etc).
    Weight 0.04. Ops/research briefs skip with full credit."""
    if not _is_adoption_brief(text, target):
        return CheckResult(
            name="abstract_synthesis",
            severity="pass",
            score_weight=0.04,
            score_earned=0.04,
            detail="N/A — not an adoption-decision brief; ops/research briefs exempt",
        )

    summary_body = _section_body(text, {"Summary", "TL;DR", "Tldr", "TLDR"})
    if not summary_body or not summary_body.strip():
        return CheckResult(
            name="abstract_synthesis",
            severity="warn",
            score_weight=0.04,
            score_earned=0.0,
            detail="No ## Summary section body to evaluate",
        )

    # Word count: strip markdown table-cell pipes + bold markers.
    body_clean = re.sub(r"[|*`]", " ", summary_body)
    words = [w for w in re.split(r"\s+", body_clean) if w]
    n_words = len(words)
    in_length_window = 50 <= n_words <= 400

    has_effort = bool(EFFORT_HINT_RE.search(summary_body))
    has_verdict_opener = bool(VERDICT_OPENER_RE.search(summary_body))

    signals_present = sum([in_length_window, has_effort, has_verdict_opener])
    missing = []
    if not in_length_window:
        missing.append(f"length={n_words}w (target 50-400)")
    if not has_effort:
        missing.append("no effort estimate")
    if not has_verdict_opener:
        missing.append("no verdict-flavored opener")

    if signals_present == 3:
        return CheckResult(
            name="abstract_synthesis",
            severity="pass",
            score_weight=0.04,
            score_earned=0.04,
            detail=f"Summary {n_words}w + effort estimate + verdict opener — abstract well-synthesized",
        )
    if signals_present == 2:
        return CheckResult(
            name="abstract_synthesis",
            severity="warn",
            score_weight=0.04,
            score_earned=0.025,
            detail=f"2/3 abstract signals; missing: {missing}",
            evidence=missing,
        )
    if signals_present == 1:
        return CheckResult(
            name="abstract_synthesis",
            severity="warn",
            score_weight=0.04,
            score_earned=0.01,
            detail=f"1/3 abstract signals; missing: {missing}",
            evidence=missing,
        )
    return CheckResult(
        name="abstract_synthesis",
        severity="warn",
        score_weight=0.04,
        score_earned=0.0,
        detail=f"0/3 abstract signals; missing: {missing}",
        evidence=missing,
    )


# --------------------------------------------------------- report generation --


# ============================================================== dynamic check ==
# v0.5 — LLM-as-judge layer. Port of the four codex-startup-pressure-test-skill
# modes (Kappaemme-git/codex-startup-pressure-test-skill, MIT, Phase-0 audited
# 2026-05-11 at /tmp/codex-pressure-test-audit/), re-styled for tool-adoption
# brief context. One combined call returns a flat structured verdict.

_DYNAMIC_SYSTEM_PROMPT = """\
You are a brutal Cemini brief auditor. The user submits a tool-adoption brief
for an OSINT / quant-finance research workspace. Your job: find fatal flaws
before the user spends days installing or integrating the tool.

You evaluate every brief through four lenses:

1. pressure-test — Identify the single most-likely failure mode of the proposed
   adoption. What kills this rollout in production? What core assumption MUST
   be true for the integration to deliver value?

2. problem-validation — Does Cemini actually have the pain this tool claims to
   solve? Is the problem real, frequent, costly? Or is the user adopting because
   the tool is shiny? Treat current-behavior as the bar: would the existing
   Cemini setup (kb-server / DeepSeek / wiki scripts / FastMCP / LangGraph)
   already cover ≥80% of the value?

3. competition-map — What does Cemini already use that overlaps with this tool?
   List the concrete existing components. Is displacement justified? "We have
   no competition" is always wrong — current behavior is competition.

4. mvp-plan — What is the smallest 1-week Phase 1 that proves the tool fits
   before committing to deeper integration? What gets CUT from the brief's
   proposed plan to focus only on the riskiest assumption?

Rules:
- Be specific to this brief. No generic startup advice.
- Rank dangerous flaws first.
- Treat license, maturity (commits/last-push), API-stability claims as testable
  before any line of code is written.
- If the brief claims a tool replaces existing Cemini infrastructure, name the
  specific component it would displace.
- Verdict must be direct; no softening.
- Fast-test must be doable in under a day with what's already in the workspace.
- Do not invent facts not stated in the brief.

Verdict scale:
- ship: no fatal flaws, brief is ready as-is
- ship-with-fixes: minor flaws but adoption can proceed if listed fixes are made
- rework: substantial flaws; brief needs revision before adoption decision
- reject: fatal flaws; do not adopt this tool, or seek a different tool
"""


def _get_dynamic_audit_models():
    """Lazily build the Pydantic v2 schemas. Returns (FatalFlaw, BriefAudit)."""
    from pydantic import BaseModel

    class FatalFlaw(BaseModel):
        mode: Literal["pressure-test", "problem-validation", "competition-map", "mvp-plan"]
        severity: Literal["high", "medium", "low"]
        description: str
        fast_test: str

    class BriefAudit(BaseModel):
        verdict: Literal["ship", "ship-with-fixes", "rework", "reject"]
        fatal_flaws: list[FatalFlaw]
        competition_check: str
        summary: str

    return FatalFlaw, BriefAudit


def run_dynamic_audit(
    text: str,
    *,
    model: str = "deepseek-chat",
    max_retries: int = 2,
    temperature: float = 0.2,
) -> DynamicAudit:
    """Call DeepSeek for the combined 4-mode brief audit. Raises StructuredOutputError on failure."""
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    try:
        from _llm_retry import request_structured  # type: ignore
    except ImportError as e:
        raise RuntimeError(
            f"_llm_retry not importable: {e}. Ensure scripts/_llm_retry.py exists."
        ) from e

    _, BriefAudit = _get_dynamic_audit_models()

    # Truncate brief body to a sane budget (most briefs are <15 KB; tokens ~25K cap).
    # Tail-truncate from middle if needed so frontmatter + verdict line both fit.
    MAX_CHARS = 16000
    if len(text) > MAX_CHARS:
        head = text[: MAX_CHARS // 2]
        tail = text[-(MAX_CHARS // 2) :]
        body = f"{head}\n\n... [middle elided, {len(text) - MAX_CHARS} chars] ...\n\n{tail}"
    else:
        body = text

    prompt = (
        "Audit the following Cemini tool-adoption brief using the four-lens "
        "framework. Return JSON only.\n\n"
        "=== BRIEF START ===\n"
        f"{body}\n"
        "=== BRIEF END ==="
    )

    t0 = datetime.now()
    parsed = request_structured(
        prompt=prompt,
        model_class=BriefAudit,
        system=_DYNAMIC_SYSTEM_PROMPT,
        model=model,
        max_retries=max_retries,
        temperature=temperature,
        stage="skill_audit_llm_mode",
    )
    latency_ms = int((datetime.now() - t0).total_seconds() * 1000)

    findings = [
        DynamicFinding(
            mode=str(f.mode),
            severity=str(f.severity),
            description=f.description,
            fast_test=f.fast_test,
        )
        for f in parsed.fatal_flaws
    ]
    return DynamicAudit(
        verdict=str(parsed.verdict),
        fatal_flaws=findings,
        competition_check=parsed.competition_check,
        summary=parsed.summary,
        model=model,
        latency_ms=latency_ms,
    )


def check_harness_dimensions(text: str, target: str) -> CheckResult:
    """K94 system-scaling steal-from: prod/adoption briefs must address harness subsystems."""
    name = Path(target).name.lower()
    applies = (
        _is_adoption_brief(text, target)
        or "phase0" in name
        or "phase-0" in name
        or "harness" in name
    )
    if not applies:
        return CheckResult(
            name="harness_dimensions",
            severity="pass",
            score_weight=0.03,
            score_earned=0.03,
            detail="N/A — not adoption/phase-0/harness brief",
        )
    dims = (
        "memory",
        "retrieval",
        "tools",
        "orchestration",
        "verification",
        "governance",
    )
    lower = text.lower()
    found = [d for d in dims if d in lower]
    if len(found) >= 4:
        return CheckResult(
            name="harness_dimensions",
            severity="pass",
            score_weight=0.03,
            score_earned=0.03,
            detail=f"Named {len(found)}/6 harness dimensions: {', '.join(found)}",
        )
    missing = [d for d in dims if d not in found]
    return CheckResult(
        name="harness_dimensions",
        severity="warn",
        score_weight=0.03,
        score_earned=0.0,
        detail=f"Only {len(found)}/6 harness dimensions; missing: {', '.join(missing)}",
    )


def assemble_report(
    target: str,
    text: str,
    sections: list[str],
    nv_age_days: int,
    strict: bool,
    dynamic: DynamicAudit | None = None,
    strict_dynamic: bool = False,
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
        check_claim_evidence(text, target),
        check_abstract_synthesis(text, target),
        check_harness_dimensions(text, target),
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

    # Dynamic-mode veto: if --strict-dynamic and DeepSeek returned 'reject',
    # upgrade the top-level verdict. Static-side veto gates still take precedence.
    if dynamic is not None and strict_dynamic and dynamic.verdict == "reject" and not veto_gates:
        verdict = "REJECT"
        summary = (
            f"REJECT (--strict-dynamic) — static {static_score}/100 but dynamic "
            f"audit returned 'reject'. {dynamic.summary}"
        )
        veto_gates = veto_gates + [f"dynamic-audit-reject ({dynamic.model})"]

    return AuditReport(
        target=target,
        verdict=verdict,
        static_score=static_score,
        veto_gates=veto_gates,
        checks=checks,
        summary=summary,
        dynamic=dynamic,
    )


def render_text(report: AuditReport) -> str:
    lines = []
    lines.append("=" * 78)
    lines.append(f"skill_audit  ::  {report.target}")
    lines.append("=" * 78)
    lines.append("")
    lines.append(f"VERDICT: {report.verdict}")
    dyn_note = "" if report.dynamic is None else "  +dynamic (LLM-as-judge active)"
    lines.append(
        f"STATIC SCORE: {report.static_score}/100   "
        f"(12 static checks{dyn_note})"
    )
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
    if report.dynamic is not None:
        d = report.dynamic
        lines.append("=" * 78)
        lines.append(f"DYNAMIC AUDIT (advisory)   model={d.model}   latency={d.latency_ms} ms")
        lines.append("=" * 78)
        lines.append(f"DYNAMIC VERDICT: {d.verdict.upper()}")
        lines.append("")
        lines.append("SUMMARY:")
        lines.append(f"  {d.summary}")
        lines.append("")
        lines.append("COMPETITION CHECK:")
        lines.append(f"  {d.competition_check}")
        lines.append("")
        if d.fatal_flaws:
            lines.append(f"FATAL FLAWS ({len(d.fatal_flaws)}):")
            for i, f in enumerate(d.fatal_flaws, 1):
                lines.append(f"  {i}. [{f.severity.upper():6}] [{f.mode}] {f.description}")
                lines.append(f"     fast-test: {f.fast_test}")
        else:
            lines.append("FATAL FLAWS: none surfaced")
        lines.append("")
    lines.append(f"=> {report.summary}")
    return "\n".join(lines)


def delegate_to_vet(path: Path, args) -> AuditReport | None:
    """Run static checks via the public `vet` CLI when available."""
    if getattr(args, "no_vet", False) or not shutil.which("vet"):
        return None

    cmd = [
        "vet",
        str(path),
        "--profile",
        "brief",
        "--root",
        str(ROOT),
        "--nv-age-days",
        str(args.nv_age_days),
        "--json",
    ]
    if args.strict:
        cmd.append("--strict")

    proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if proc.returncode == 3 or not proc.stdout.strip():
        return None

    try:
        data = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return None

    checks = [
        CheckResult(
            name=c["name"],
            severity=c["severity"],
            score_weight=c["score_weight"],
            score_earned=c["score_earned"],
            detail=c["detail"],
            evidence=c.get("evidence", []),
            veto_reason=c.get("veto_reason"),
        )
        for c in data["checks"]
    ]
    return AuditReport(
        target=data["target"],
        verdict=data["verdict"],
        static_score=data["static_score"],
        veto_gates=data["veto_gates"],
        checks=checks,
        summary=data["summary"] + " (static via vet)",
        dynamic=None,
    )


def merge_dynamic_report(
    report: AuditReport,
    dynamic: DynamicAudit | None,
    *,
    strict_dynamic: bool,
) -> AuditReport:
    if dynamic is None:
        return report

    report.dynamic = dynamic
    if strict_dynamic and dynamic.verdict == "reject" and not report.veto_gates:
        report.verdict = "REJECT"
        report.summary = (
            f"REJECT (--strict-dynamic) — static {report.static_score}/100 but dynamic "
            f"audit returned 'reject'. {dynamic.summary}"
        )
        report.veto_gates = report.veto_gates + [f"dynamic-audit-reject ({dynamic.model})"]
    return report

# ----------------------------------------------------------------- curator mode --

CURATE_STALE_DAYS = 30


def _parse_frontmatter_dates(text: str) -> tuple[str | None, str | None]:
    if not text.startswith("---"):
        return None, None
    end = text.find("\n---", 3)
    if end == -1:
        return None, None
    block = text[3:end]
    created = updated = None
    for line in block.splitlines():
        if line.startswith("created:"):
            created = line.split(":", 1)[1].strip()
        elif line.startswith("updated:"):
            updated = line.split(":", 1)[1].strip()
    return created, updated


def _index_topic_tokens(index_path: Path) -> set[str]:
    if not index_path.exists():
        return set()
    tokens: set[str] = set()
    for line in index_path.read_text(encoding="utf-8", errors="replace").splitlines():
        for word in re.findall(r"[a-z0-9][a-z0-9-]{2,}", line.lower()):
            tokens.add(word)
    return tokens


def curate_skills_and_rules(
    *,
    skills_dir: Path,
    rules_dir: Path,
    report_path: Path,
    stale_days: int = CURATE_STALE_DAYS,
) -> Path:
    """Hermes curator pattern: propose prune/consolidate; never delete."""
    index_tokens = _index_topic_tokens(WIKI / "index.md")
    now = datetime.now()
    rows: list[dict[str, str]] = []

    def scan(path: Path, kind: str) -> None:
        if not path.exists():
            return
        if kind == "skill":
            candidates = sorted(path.glob("*/SKILL.md"))
        else:
            candidates = sorted(path.glob("*.mdc"))
        for fp in candidates:
            rel = fp.relative_to(ROOT)
            text = fp.read_text(encoding="utf-8", errors="replace")
            mtime_age = (now - datetime.fromtimestamp(fp.stat().st_mtime)).days
            _, updated = _parse_frontmatter_dates(text)
            title = fp.parent.name if kind == "skill" else fp.stem
            body_tokens = set(re.findall(r"[a-z0-9][a-z0-9-]{2,}", text.lower()))
            overlap = len(body_tokens & index_tokens)
            reasons: list[str] = []
            if mtime_age >= stale_days:
                reasons.append(f"stale ({mtime_age}d since mtime)")
            if overlap == 0 and len(body_tokens) > 20:
                reasons.append("low wiki/index overlap")
            if kind == "skill" and title in {"goal", "to-issues", "grill-with-docs"}:
                reasons.append("federation canon — KEEP")
            decision = "KEEP" if "federation canon" in " ".join(reasons) else (
                "PRUNE?" if reasons else "KEEP"
            )
            rows.append(
                {
                    "path": str(rel),
                    "kind": kind,
                    "title": title,
                    "updated": updated or "—",
                    "mtime_days": str(mtime_age),
                    "index_overlap": str(overlap),
                    "reasons": "; ".join(reasons) if reasons else "active",
                    "decision": decision,
                }
            )

    scan(skills_dir, "skill")
    scan(rules_dir, "rule")

    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# Skill / rule curator report — {TODAY.isoformat()}",
        "",
        "Hermes curator pattern (K132): **proposal only** — human approves before delete.",
        "",
        "| Decision | Kind | Path | Updated | Mtime(d) | Index overlap | Reasons |",
        "|----------|------|------|---------|----------|---------------|---------|",
    ]
    for r in sorted(rows, key=lambda x: (x["decision"] != "PRUNE?", x["path"])):
        lines.append(
            f"| {r['decision']} | {r['kind']} | `{r['path']}` | {r['updated']} | "
            f"{r['mtime_days']} | {r['index_overlap']} | {r['reasons']} |"
        )
    lines.extend(["", f"Total scanned: {len(rows)}", ""])
    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


# ----------------------------------------------------------------- entrypoint --


def main():
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        "brief",
        nargs="?",
        help="Path to brief / skill / prompt file (omit with --curate)",
    )
    p.add_argument(
        "--curate",
        action="store_true",
        help="Scan .cursor/skills + .cursor/rules; write prune proposal report (no deletes)",
    )
    p.add_argument(
        "--skills-dir",
        type=Path,
        default=ROOT / ".cursor" / "skills",
        help="Skills root for --curate (default: .cursor/skills)",
    )
    p.add_argument(
        "--rules-dir",
        type=Path,
        default=ROOT / ".cursor" / "rules",
        help="Rules dir for --curate (default: .cursor/rules)",
    )
    p.add_argument(
        "--report",
        type=Path,
        default=None,
        help="Report path for --curate (default: .local/reports/skill-curate-YYYY-MM-DD.md)",
    )
    p.add_argument(
        "--curate-stale-days",
        type=int,
        default=CURATE_STALE_DAYS,
        help="Flag skills/rules untouched this many days (default: 30)",
    )
    p.add_argument("--json", action="store_true", help="Emit JSON report instead of text")
    p.add_argument("--strict", action="store_true", help="Treat warnings as veto gates")
    p.add_argument(
        "--nv-age-days",
        type=int,
        default=30,
        help="Flag [NEEDS VERIFICATION] tags older than this (default: 30)",
    )
    p.add_argument(
        "--llm-mode",
        action="store_true",
        help="Run DeepSeek-backed dynamic audit (4-mode pressure-test). Advisory by default.",
    )
    p.add_argument(
        "--strict-dynamic",
        action="store_true",
        help="With --llm-mode: dynamic 'reject' upgrades top-level verdict to REJECT.",
    )
    p.add_argument(
        "--llm-model",
        default="deepseek-chat",
        help="DeepSeek model id for --llm-mode (default: deepseek-chat).",
    )
    p.add_argument(
        "--no-vet",
        action="store_true",
        help="Force inline static checks; do not delegate to `vet` CLI.",
    )
    args = p.parse_args()

    if args.curate:
        report = args.report or (
            ROOT / ".local" / "reports" / f"skill-curate-{TODAY.isoformat()}.md"
        )
        out = curate_skills_and_rules(
            skills_dir=args.skills_dir,
            rules_dir=args.rules_dir,
            report_path=report,
            stale_days=args.curate_stale_days,
        )
        print(f"Curator report written: {out}")
        print(f"Scanned skills under {args.skills_dir} and rules under {args.rules_dir}")
        sys.exit(0)

    if not args.brief:
        p.error("brief path required unless --curate is set")

    path = Path(args.brief)
    if not path.exists():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        sys.exit(3)

    try:
        text, sections = parse_brief(path)
    except (OSError, UnicodeDecodeError) as e:
        print(f"ERROR: could not read {path}: {e}", file=sys.stderr)
        sys.exit(3)

    dynamic = None
    if args.llm_mode:
        try:
            dynamic = run_dynamic_audit(text, model=args.llm_model)
        except Exception as e:
            print(f"WARN: --llm-mode dynamic audit failed: {e}", file=sys.stderr)
            print(
                "  static checks still produced below; dynamic section omitted.",
                file=sys.stderr,
            )

    report = delegate_to_vet(path, args)
    if report is None:
        report = assemble_report(
            target=str(path),
            text=text,
            sections=sections,
            nv_age_days=args.nv_age_days,
            strict=args.strict,
            dynamic=None,
            strict_dynamic=args.strict_dynamic,
        )
    else:
        report = merge_dynamic_report(
            report, dynamic, strict_dynamic=args.strict_dynamic
        )

    if args.json:
        print(json.dumps(asdict(report), indent=2, default=str))
    else:
        print(render_text(report))

    sys.exit({"PASS": 0, "WARN": 1, "REJECT": 2, "ERROR": 3}[report.verdict])


if __name__ == "__main__":
    main()
