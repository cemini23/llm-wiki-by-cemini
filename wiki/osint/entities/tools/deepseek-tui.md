---
title: "DeepSeek-TUI — DeepSeek-Native Coding Agent (RED-FLAG: aggressive workflow-migration claim)"
type: entity
tags: [tool, coding-agent, deepseek, tui, k39, adopt-tier-flagged, phase-0-pending]
keywords: [deepseek-tui, hmbown, coding agent, claude code alternative, deepseek, mcp tooling, workflow migration]
related:
  - sources/evaluating-project-links-stacks.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - concepts/deepseek-models.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
phase_0_audit: PENDING — Adopt verdict claims full Claude Code → DeepSeek-TUI migration; high mischaracterization risk
---

## Relations
- `@sources/evaluating-project-links-stacks.md` — source evaluation brief (URL 12)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/deepseek-models.md` — DeepSeek-V3/R1 models are Cemini's standardized LLM backbone

## Raw Concept

- **Repo / URL** (per source brief): `github.com/Hmbown/DeepSeek-TUI`
- **Tier (per source brief)**: **Adopt — Workflow only** (eval brief recommends full Claude Code → DeepSeek-TUI migration)
- **Tier downgrade pending**: **NEEDS Phase-0** before any workflow change
- **License** (per source brief): MIT
- **Stack**: Coding agent built on DeepSeek; claims native MCP tooling support

## Narrative — RED FLAG

The eval brief's headline recommendation is the **most aggressive** in the K39 batch:

> "Transition the local Workflow from Claude Code to DeepSeek-TUI. This decision standardizes the entire lifecycle (development and production) on DeepSeek API behavior, eliminating cross-model prompt drift…"

Wholesale Claude Code replacement is a **major workflow change**. Recommending it on a single-dev (Hmbown), apparently-new project (no maturity numbers in the eval brief) is the **exact pattern that produced 6 mischaracterization catches across K28+K30+K36+K38**.

### Integration vector

**Adopt → HOLD pending Phase-0**. Do not migrate workflow until Phase-0 confirms:
1. **Maturity signals** — star count, contributor count, project age, last-push recency
2. **MCP compatibility** — eval claims "native built-in MCP tooling"; verify whether all of Cemini's existing MCP servers (claude-mem, kb-server, conductor, lazy-tool, claude-code-router, etc.) are MCP-spec-compatible and function correctly under DeepSeek-TUI
3. **License file** presence (3rd-occurrence no-LICENSE pattern)
4. **Skill-system compatibility** — Cemini's installed Claude Code skills (finance-skills, claude-mem skills, specify-cli, etc.) must work or migration is a regression
5. **Hooks system compatibility** — Cemini relies on Claude Code hooks (SessionStart, etc.)

### Why a hard pre-migration veto

Even setting aside Phase-0 unknowns: **switching coding agents on a 100% solo-developer team mid-project is high-risk**. Cemini has substantial Claude Code investment (settings.json, hooks, skills, MCP servers, agent definitions). DeepSeek-TUI must demonstrate **strictly-better** behavior across all these axes to justify migration cost — and the eval brief provides no such evidence.

### NEEDS VERIFICATION

- All items in Integration vector
- Cost analysis vs. existing Cemini Claude API spend

### Phase-0 audit status

**PENDING — HIGH PRIORITY**. Workflow migration is a 1-3-day commitment if it works; a much longer rollback if it doesn't. Phase-0 must clear all 5 verification items before any workflow change.

[Source: Evaluating Project Links for Stacks.docx URL 12; retrieved 2026-05-11]
