---
title: vercel-labs/skills — cross-tool SKILL.md installer
type: entity
tags: [tools, skills, claude-code, cursor, dev-tooling]
keywords: [vercel-skills, npx-skills, skill-md, symlink, cursor, claude-code, codex]
related:
  - sources/eval-url-revenue-opportunity-2026-10-13.md
  - concepts/k290-eval-wave.md
  - entities/tools/agent-skill-manager.md
maturity: draft
created: 2026-10-13
updated: 2026-10-13
wire_status: deferred
---

## Relations

- @sources/eval-url-revenue-opportunity-2026-10-13.md
- @concepts/k290-eval-wave.md
- @entities/tools/agent-skill-manager.md

## Raw Concept

**What prompted this page:** K290 tool eval (2026-10-13), entry 4 — **Integrate tier**. `github.com/vercel-labs/skills`.

## Narrative

An **`npx skills`** CLI that **installs, symlinks and updates `SKILL.md`** directories across **Cursor, Claude Code and Codex**. The value is **one skill source, many agent runtimes** — it removes per-runtime copies of the same skill.

**License:** **MIT** — `[CONFIRMED]`. **Docx star count was wrong** (16.2k claimed; **34.3k actual**).

**Docx tier: Integrate** (high value, now) — *"standardize agent procedures, raise engineering velocity."*

**Overlap:** `@entities/tools/agent-skill-manager.md` and `@entities/tools/agent-skills.md` already cover skill packaging in this wiki. `vercel-labs/skills` is the **distribution/symlink** layer rather than the authoring layer.

**Caution that applies here:** this workspace's rule is that **unsolicited third-party skill/MCP repositories are treated as hostile until allowlisted** (AgentBaiting). A symlink installer makes it **easier to point every runtime at one source** — which is exactly the supply-chain shape to review before adopting. **Phase-0 ran 2026-10-13** — MIT confirmed by `gh api`; cloned to `.local/adopts/k290/skills` (1.9 MB). The allowlist caution above still applies before adoption.

## Snippets

> npx skills — install/symlink/update SKILL.md across Cursor/Claude Code/Codex. [Source: Repository Revenue Opportunity Analysis.docx — entry 4]
