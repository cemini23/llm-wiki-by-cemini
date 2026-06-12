---
title: all-agentic-architectures — 35 agent pattern compendium
type: entity
tags: [tool, agent-patterns, steal-from, k113]
keywords: [fareedkhan, agentic-rag, deterministic-picker, jupyter]
related:
  - sources/multi-wiki-tool-eval-v5-k113-2026-06-12.md
  - concepts/tool-evaluation-framework.md
  - concepts/conductor-orchestrator.md
  - "@ccc-wiki/entities/tools/all-agentic-architectures.md"
maturity: draft
created: 2026-06-12
updated: 2026-06-12
license_verified: MIT
---

## Relations

- @sources/multi-wiki-tool-eval-v5-k113-2026-06-12.md — K113 Steal-from
- @concepts/conductor-orchestrator.md — routing pattern extraction target

## Raw Concept

- **Repo:** `github.com/FareedKhan-dev/all-agentic-architectures`
- **Tier:** **Steal-from** — MIT; 3,600★ eval (~verify at adopt)
- **License:** MIT `[CONFIRMED]` 2026-06-12

## Narrative

Jupyter compendium of 35 multi-agent paradigms. Eval highlights **deterministic-picker** pattern to avoid LLM scorer degradation in deep eval loops.

**Integration:** extract routing diagrams into conductor/lazy-tool docs — **do not** import full notebook dependency tree.

**NO-GO:** prod install of entire repo; pattern library only.
