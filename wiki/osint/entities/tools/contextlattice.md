---
title: "ContextLattice — Long-Horizon Agent Memory Control Plane"
type: entity
tags: [tool, agent-memory, context-orchestration, polyglot, k37]
keywords: [contextlattice, steal-from, three-surface-eval]
related:
  - sources/evaluating-urls-system-integration.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/evaluating-urls-system-integration.md` — source evaluation brief (URL 21)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `github.com/sheawinkler/contextlattice`
- **Tier (per source brief)**: **Steal-from**
- **License**: [NEEDS VERIFICATION 2026-05-11] License needs verification.

## Narrative

Local-first control plane for long-horizon agent memory + context orchestration. Unified write/read API; agents fan out memory across diverse storage tiers (hot/warm/cold). Polyglot: Go ingress + Rust retrieval + Python + TypeScript.

### Integration vector

Steal-from: study as enterprise-grade reference for **long-horizon memory architecture** — high-concurrency Go ingress paired with memory-safe Rust retrieval. Do NOT deploy — polyglot maintenance burden + Hetzner resource limits.

### Risks

Polyglot codebase (Go + Python + TS + Rust) → severe maintenance burden. Resource-heavy.

[Source: Evaluating Urls System Integration.docx, URL 21]
