---
title: "Readme.skill — Agent Skill for Repo-Stats Auto-Gen"
type: entity
tags: [tool, claude-skill, repo-stats, workflow, adopt, k38]
keywords: [readme, skill, adopt, three-surface-eval]
related:
  - sources/link-evaluation-brief-trading-stack.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/link-evaluation-brief-trading-stack.md` — source evaluation brief (URL 3)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `github.com/study8677/Readme.skill`
- **Tier (per source brief)**: **Adopt**
- **License**: [NEEDS VERIFICATION 2026-05-11] License needs verification; skill format = natural-language instructions (no compiled code), low risk.

## Narrative

Structured agent-skill (natural-language instructions for Claude Code / Codex CLI) that auto-generates repo statistics. Prompts agent to execute git logs, GitHub CLI via GraphQL, parse local SQLite + JSON caches. Outputs structured README/health metrics.

### Integration vector

Adopt locally for workflow — augments existing wiki-curation toolchain with structured repo-stats auto-gen. Drop into `~/.claude/skills/` and invoke during repo audits.

### Risks

Requires `gh` CLI authenticated. Agent drift risk: SKILL.md interpretations shift across model updates.

[Source: Link Evaluation Brief Trading Stack.docx, URL 3]
