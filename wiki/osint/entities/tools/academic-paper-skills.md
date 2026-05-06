---
title: academic-paper-skills — 35-Point Peer-Review Framework (MIT)
type: entity
tags: [tool, prompt-engineering, mit-license, steal-from-tier, abandoned-project, peer-review-simulation, brief-audit-upgrade]
keywords: [academic-paper-skills, lishix520, 35-point-peer-review, 7-academic-dimensions, gap-analysis, chapter-quality-check, final-evaluation, brief-audit-upgrade]
related:
  - sources/5-6-links-eval-batch.md
  - concepts/cemini-license-posture.md
  - entities/tools/codex-startup-pressure-test-skill.md
  - entities/tools/research-paper-writing-skills.md
  - entities/tools/obsidian-llm-wiki-local.md
maturity: draft
created: 2026-05-06
updated: 2026-05-06
---

## Relations

- @sources/5-6-links-eval-batch.md — origin source: K32 Gemini DR eval URL 11, **STEAL-FROM** tier
- @concepts/cemini-license-posture.md — MIT-licensed, IP-clean
- @entities/tools/codex-startup-pressure-test-skill.md — sister STEAL-FROM in same K32 batch (pressure-test prompts)
- @entities/tools/research-paper-writing-skills.md — sister STEAL-FROM in same K32 batch (claim-evidence alignment)
- @entities/tools/obsidian-llm-wiki-local.md — sister STEAL-FROM in same K32 batch (wiki maintenance code)

## Raw Concept

lishix520/academic-paper-skills provides a systematic, end-to-end framework for drafting/editing/verifying academic papers via Python scripts and LLM prompts inside Claude Code. Dual-workflow architecture: **Strategist** + **Composer** phases. Includes integrated Python verification scripts (`gap_analysis.py`, `chapter_quality_check.py`, `final_evaluation.py`) that simulate a comprehensive **35-point peer-review assessment across 7 academic dimensions**.

K32 DR verdict: **STEAL-FROM**. Don't install the framework wholesale. Lift the architecture of the **"Reviewer Simulation system"** — specifically the 7-dimension / 35-point assessment matrix — and port these objective evaluation criteria into Cemini's `scripts/skill_audit.py` brief-audit workflow.

This is the most directly-applicable STEAL-FROM in the K32 batch for the brief-audit infrastructure.

## Narrative

- **URL**: `https://github.com/lishix520/academic-paper-skills` ✓ DR-cited
- **License**: MIT — clean, IP-sale safe
- **Stack**: Python verification scripts + LLM prompts; designed for Claude Code execution
- **Maturity**: 2 commits, 0 releases — abandoned per DR. Treat as static prompt+code artifact

### What's actionable for Cemini

Cemini already has `scripts/skill_audit.py` doing **40% of design weight** worth of static checks on briefs (per `CLAUDE.md` schema):

- Required sections (`## Target`, `## Summary`)
- Cross-link `@path` resolution
- Citation tags (Sources section + inline)
- NEEDS VERIFICATION freshness
- Prose quality gates (no emoji, no TODO at ship)
- Frontmatter well-formedness
- Operational Stability + Scientific Integrity veto gates

academic-paper-skills's 35-point / 7-dimension framework would extend this static layer with **LLM-driven semantic evaluation**:

- Are claims supported by cited evidence?
- Is the executive summary aligned with body content?
- Are competing alternatives considered?
- Is the methodology reproducible from text?
- Does the body avoid logical fallacies?

The exact dimensions aren't surfaced in DR, so Phase-1 audit is needed to extract the matrix.

### Action plan

1. Phase 1: clone `github.com/lishix520/academic-paper-skills` to `/tmp/academic-paper-skills-audit/`
2. Phase 2: extract the 7-dimension list + 35-point assessment criteria
3. Phase 3: read the Python verification scripts (`gap_analysis.py`, `chapter_quality_check.py`, `final_evaluation.py`) — adapt the LLM-prompt-driven evaluation pattern to Cemini brief-shape
4. Phase 4: extend `scripts/skill_audit.py` with an `--llm-mode` flag that runs the 7-dimension semantic checks via DeepSeek API; gate behind explicit flag because token cost is non-trivial per brief
5. Phase 5: run on existing briefs at `briefs/` and `cemini-prod:/opt/cemini/briefs/` to validate framework

Estimated effort: 4-6 hours total. Higher than other STEAL-FROM siblings because it includes Python script integration, not just prompt extraction.

### Why this is the highest-priority STEAL-FROM (after obsidian-llm-wiki-local)

Two reasons:

1. **Direct upgrade path to existing infrastructure**: `scripts/skill_audit.py` is real; this extends it with a clear capability axis (semantic LLM evaluation on top of static checks).
2. **Brief quality is the export-control point**: briefs are what ship to claude.ai and CeminiSuite. Higher brief-audit rigor = better information distribution. This has direct revenue impact (per monetization-priority frame).

### Risk

> "The primary indicator of risk is project inactivity. The repository exhibits only 2 total commits and 0 releases, strongly suggesting it represents a static snapshot of a single researcher's personal workflow rather than a continuously improving, community-supported framework. Consequently, any bugs or prompt drift over time will not be addressed by upstream maintainers."

Mitigation: clone, extract, fork-and-maintain. Don't depend on upstream.

### Open questions

- ⚠ Exact 7-dimension list (DR didn't enumerate)
- ⚠ Exact 35-point assessment criteria
- ⚠ Are the Python scripts CLI-callable standalone or assume Claude Code skill context?
- ⚠ DeepSeek API token cost per full 35-point evaluation pass

### Adoption status — STEAL-FROM, NOT INSTALLED

Phase-1 audit pending. Highest-priority STEAL-FROM in K32 after obsidian-llm-wiki-local; bundle into a single brief-audit upgrade sprint.

## Snippets

### 35-point peer-review framework (DR direct quote)

> "This repository provides a systematic, end-to-end framework consisting of Python scripts and LLM prompts explicitly designed to operate inside Claude Code to draft, edit, and rigorously verify academic papers. It features a dual-workflow architecture divided into 'Strategist' and 'Composer' phases. Crucially, the stack includes integrated Python verification scripts (such as gap_analysis.py, chapter_quality_check.py, and final_evaluation.py) that simulate a comprehensive 35-point peer-review assessment across 7 distinct academic dimensions to enforce quality control prior to finalization." [Source: 5_6 links.docx URL 11]

### Why STEAL-FROM (DR direct framing)

> "Steal-from. Do not install the entire framework wholesale, as much of it pertains to academic boilerplate. Instead, lift the architecture of the 'Reviewer Simulation system' — specifically the programmatic execution of the 7 dimensions and 35-point assessment matrix. Port these objective evaluation criteria into the Claude Code prompts and Python linters used when finalizing research briefs for production deployment." [Source: 5_6 links.docx URL 11]
