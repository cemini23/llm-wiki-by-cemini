---
title: Ideal-State Artifact (ISA) verification — deterministic close gates
type: concept
tags: [concept, agent-harness, verification, k229, lifeos]
keywords: [ISA, CloseGate, LifeOS, state-machine, harness]
related:
  - entities/tools/lifeos.md
  - entities/tools/pi-rlm.md
  - concepts/code-as-agent-harness.md
  - concepts/agentic-code-quality-gates.md
  - sources/eval-github-revenue-opportunity-2026-08-09.md
maturity: draft
created: 2026-08-09
updated: 2026-08-09
---

## Relations

- @entities/tools/lifeos.md
- @entities/tools/pi-rlm.md
- @concepts/code-as-agent-harness.md
- @concepts/agentic-code-quality-gates.md
- @sources/eval-github-revenue-opportunity-2026-08-09.md

## Raw Concept

Pattern extracted from danielmiessler/LifeOS (MIT) during K229 Phase-0.

## Narrative

Force agents through a **Current State → Ideal State** artifact with gates that **block completion claims** when outputs are stale or unverified (ISA / CloseGate class). Pairs with:

- persistent code namespace (`pi-rlm` Bun `execute`) for stateful intermediate results
- Osmani agentic quality gates (prefer harness constraints over review volume)

Cemini use: CCC harness + Atto Italian civil-record kit — reduce hallucinated "done" before human-gated `truth.ged` / vault writes.

[Source: LifeOS README + K229 eval]
