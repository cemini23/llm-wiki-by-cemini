---
title: "DeepSeek-TUI — DeepSeek-Native Coding Agent (NO-GO 2026-05-12: eval-brief scope mischaracterization)"
type: entity
tags: [tool, coding-agent, deepseek, tui, k39, no-go, eval-brief-mischaracterization]
keywords: [deepseek-tui, hmbown, coding agent, claude code alternative, deepseek, mcp tooling, workflow migration]
related:
  - sources/evaluating-project-links-stacks.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - concepts/deepseek-models.md
maturity: validated
created: 2026-05-11
updated: 2026-05-12
phase_0_audit: NO-GO 2026-05-12 — eval-brief mischaracterizes scope; recommends wholesale Claude Code replacement without justification
license_verified: MIT (gh api confirmed)
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

**NO-GO 2026-05-12** — wholesale workflow replacement unjustified on demonstrated-mature single-LLM project.

## Phase-0 audit findings (2026-05-12)

**Repo verified**: `github.com/Hmbown/DeepSeek-TUI` — 26,403★ / 2,214 forks / 369 open issues / MIT confirmed / last push 2026-05-12 (active). Tool itself is **legitimately mature** — not mischaracterization on the tool, mischaracterization on the **adoption recommendation**.

**The mischaracterization is in the eval brief, not the tool**: brief frames DeepSeek-TUI as a Claude Code drop-in replacement ("This decision standardizes the entire lifecycle…"). DeepSeek-TUI is a *DeepSeek-API-only* terminal coding agent; Cemini's stack is multi-model (Claude Max + DeepSeek API + qwen research agents) with Claude Code-specific infrastructure investment:

- **Skills system**: finance-skills + claude-mem + specify-cli + tech-debt-audit are Claude 4.7-tuned. DeepSeek-V4 parity on financial-reasoning workloads is unverified.
- **Hooks system**: `SessionStart` + post-tool hooks are Claude Code primitives.
- **MCP server stack**: claude-mem, kb-server, conductor, lazy-tool, claude-code-router — all assume Claude Code's MCP harness.

**Cemini-coverage check**: switching coding agents on a 100% solo-developer team mid-project = workflow regression cost vastly exceeds any "standardization" benefit. Migration would be 1-3 days work + months of skill-system re-tuning + permanent loss of Claude 4.7-tier reasoning on the bulk of curation/research work.

### Verdict

**NO-GO 2026-05-12**. Tool is fine for someone who wants a DeepSeek-only TUI; Cemini is not that user. Activation trigger: only reconsider if (a) head-to-head benchmark shows DeepSeek-V4 ≥ Claude 4.7 on Cemini's actual research-curation + financial-reasoning workloads (unlikely at K-series cadence), AND (b) Cemini's MCP stack adds DeepSeek-TUI compatibility shims. Neither is on the roadmap.

[Source: Evaluating Project Links for Stacks.docx URL 12; retrieved 2026-05-11; Phase-0 audit 2026-05-12]
