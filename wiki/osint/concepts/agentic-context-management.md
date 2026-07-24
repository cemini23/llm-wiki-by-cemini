---
title: Agentic Context Management (ACM)
type: concept
tags: [concept, agent-memory, harness, k193]
keywords: [context lifecycle, compaction, Maximem Synap, scoping]
related:
  - sources/arxiv-2607.21503-agentic-context-management.md
  - concepts/hierarchical-bounded-agent-memory.md
  - concepts/context-compression-resume-pattern.md
  - entities/tools/openforgerl.md
  - sources/arxiv-2607.21557-openforgerl.md
maturity: draft
created: 2026-07-24
updated: 2026-07-24
---

## Relations

- @sources/arxiv-2607.21503-agentic-context-management.md
- @concepts/hierarchical-bounded-agent-memory.md
- @concepts/context-compression-resume-pattern.md
- @entities/tools/openforgerl.md
- @sources/arxiv-2607.21557-openforgerl.md

## Raw Concept

Manage what an agent holds in mind as a **lifecycle** (architect → ingest → scope → anticipate → compact/consolidate), not as infinite RAG store.

## Narrative

Naive context concat → quadratic token cost; crude summarization → accuracy cliff; validated compaction aims for linear cost with fidelity. Complements Ensemble QSP hierarchical memory and CPR. Production steal: explicit eviction + provenance + org/user scope tiers in poker decide() / CCC harness sessions. Maximem Synap is a commercial reference — **no local adopt** this batch.
