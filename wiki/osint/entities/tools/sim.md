---
title: "Sim — pgvector + agent-state schemas (Steal-from, Apache-2.0)"
type: entity
tags: [tool, pgvector, agent-state, apache-2, steal-from, langgraph-extension, gemini-eval-doc2]
keywords: [sim, simstudioai, pgvector schema, agent state db, next.js, bun, ram budget]
related:
  - sources/evaluating-project-links-systems-2-2026-05-12.md
  - sources/multi-wiki-gemini-eval-prompt-2026-05-12.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-deployment.md
maturity: draft
created: 2026-05-12
updated: 2026-05-12
gemini_eval_doc2_url: 4
phase_0_verdict: STEAL-FROM 2026-05-12 (extract pgvector + agent-state schemas; full Next.js+Bun stack rejected on RAM)
---

## Relations

- `@sources/evaluating-project-links-systems-2-2026-05-12.md` — source eval (URL 4)
- `@concepts/cemini-deployment.md` — Cemini RAM-budget context

## Raw Concept

- **Repo**: `github.com/simstudioai/sim`
- **License**: Apache-2.0
- **Tier**: Steal-from (schemas only)
- **Primary fit**: Cemini financial (LangGraph extension)

## Narrative

Full-stack Next.js + Bun agent platform. Apache-2.0 license clean. Full-stack adoption rejected on Cemini RAM budget; **schema extraction** is the value: pgvector + agent-state DB schemas reusable directly for Cemini LangGraph extension. Steal `agents/orchestrator.py` extension schemas; do not adopt the rest.
