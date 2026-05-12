---
title: "Maggy / claude-bootstrap — AI Engineering Command Center"
type: entity
tags: [tool, agent-framework, tdd-loops, claude-code, k37]
keywords: [claude, bootstrap, maggy, steal-from, three-surface-eval]
related:
  - sources/evaluating-urls-system-integration.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: validated
created: 2026-05-11
updated: 2026-05-11
license_verified: MIT
---

## Relations
- `@sources/evaluating-urls-system-integration.md` — source evaluation brief (URL 5)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `github.com/alinaqi/claude-bootstrap`
- **Tier (per source brief)**: **Steal-from**
- **License** [VERIFIED 2026-05-11]: **MIT** (clean for pattern extraction per Cemini license posture). Maturity: 621★ / last push 2026-05-11 / ~4.5 months old.

## Narrative

Autonomous AI engineering command center built around Claude's LLM ecosystem. Multi-agent workflows run inside isolated Docker containers ("Polyphony"). Enforces TDD-Loops via Stop Hooks — auto-pipes stderr back into LLM context after each shell call.

### Integration vector

Steal-from: extract the **TDD-Loops via Stop Hooks** shell pattern — exit-code capture + stderr-as-LLM-context — and replicate it in local Obsidian / Cemini automation scripts. Do NOT adopt the full framework (P2P mesh networking + Docker autonomy is gross over-engineering for solo dev).

### Risks

Autonomous agents with native shell-exec + Docker-spawn = catastrophic blast radius if exploited.

[Source: Evaluating Urls System Integration.docx, URL 5]
