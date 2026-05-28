---
title: agent-skills (instructa) — Claude Code skill structural schema (Adopt-tier)
type: entity
tags: [tool, claude-code, skills, plugin, adopt-tier, workflow, schema]
keywords: [agent-skills, instructa, claude code skills, SKILL.md, package-security-check, security-auditor]
related:
  - sources/evaluating-urls-cemini-project-2026-05-13.md
  - concepts/tool-evaluation-framework.md
  - entities/tools/agent-skills-eval.md
maturity: draft
created: 2026-05-13
updated: 2026-05-28
---

## Relations

- `@sources/evaluating-urls-cemini-project-2026-05-13.md` — origin source (Doc 1, K42), Adopt-tier
- `@concepts/tool-evaluation-framework.md` — methodology
- `@entities/tools/agent-skills-eval.md` — prior eval framework page

## Raw Concept

Stub from Doc 1 K42 eval (2026-05-13). Adopt-tier; cross-routed to Workflow (primary) + Cybersec (security-auditor + browser_debugger personas).

## Narrative

- **Eval claim**: `.agents/skills/` structural schema for Claude Code plugin integration; package-security-check + security-auditor skill definitions.
- **URL**: `https://github.com/instructa/agent-skills/blob/main/skills/package-security-check/SKILL.md` (eval reported UNAVAILABLE during fetch but referenced extensively in cross-routing).
- **Cemini use case**: embed the structural schema into Cemini's local automation templates; inject security-auditor persona into defensive ops.

### Phase-0 audit (2026-05-28)

Repo: `instructa/agent-skills` — reachable; **no root LICENSE** (`gh api` = NONE). Individual sub-skills include their own licenses (e.g. `skills/search-context/LICENSE` = MIT).

**Verdict: CONDITIONAL-GO (steal-from per-skill)** — cherry-pick specific skills (e.g. `package-security-check`, `secleak-check`) only after per-folder license verification; do not bulk-adopt the monorepo.

[Source: Evaluating URLs for Cemini Project.docx (retrieved 2026-05-13)]
