---
title: "tech-debt-skill — Claude Code Technical Debt Auditor"
type: entity
tags: [tool, code-quality, claude-code, skill, audit, technical-debt]
keywords: [tech-debt, Claude Code skill, code audit, IP-sale readiness, static analysis]
related:
  - sources/evaluating-links-trading-wiki-stacks.md
  - concepts/tool-evaluation-framework.md
maturity: draft
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@sources/evaluating-links-trading-wiki-stacks.md` — source evaluation brief (URL 11)

## Raw Concept

A Claude Code skill triggered via `/tech-debt-audit` that performs comprehensive static analysis across an entire codebase and produces a persistent `TECH_DEBT_AUDIT.md` artifact.

- **Repo**: `github.com/ksimback/tech-debt-skill`
- **License**: MIT
- **Stack**: Claude Code skill (Markdown + subagent dispatch)

## Narrative

The tech-debt-skill consumes the entirety of a local codebase directory and produces a structured audit identifying, quantifying, and providing actionable remediation paths for technical debt. It uses subagent dispatch to parallelize deep static analysis across hundreds of Python modules.

### Integration vectors

- **Workflow (Adopt)**: Install as Claude Code plugin on the macOS environment. Periodically invoke `/tech-debt-audit` targeting the `/opt/cemini/` directory. Results feed into IP-sale readiness preparation by systematically documenting and remediating code quality issues before institutional due diligence.
- **Cemini prod (No)**: Parallel subagent dispatch during active trading would destabilize CPU allocation on the production host.

### Risks

- **API token consumption**: Whole-repository audits spawning parallel subagents generate immense token throughput. Must be run sparingly, not continuously.

### Cemini significance

Directly supports the strategic objective of preparing the Cemini codebase for institutional acquirer scrutiny. A documented, quantified technical debt trail with remediation paths is a due-diligence asset.

[Source: Evaluating Links for Trading and Wiki Stacks.docx, URL 11]
