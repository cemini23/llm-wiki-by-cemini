---
title: Hierarchical bounded agent memory (Ensemble QSP pattern)
type: concept
tags: [concept, agent-memory, multi-agent, harness, k161]
keywords: [three-layer memory, project-state JSON, eviction, PI oversight, context bound]
related:
  - sources/arxiv-2607.29600-ham-vln-2026-08-03.md
  - concepts/agentic-context-management.md
  - sources/arxiv-2607.21503-agentic-context-management.md
  - sources/arxiv-2607.10814-belief-conditioned-llm-agents-werewolf-audit-2026-07-15.md
  - concepts/belief-conditioned-agent-audit-hidden-info.md
  - sources/arxiv-hierarchical-memory-ensemble-qsp-2607.07666-2026-07-13.md
  - concepts/agent-memory-critique.md
  - concepts/context-compression-resume-pattern.md
  - concepts/autosci-research-lifecycle-memory.md
maturity: draft
created: 2026-07-13
updated: 2026-08-03
---

## Relations

- @sources/arxiv-2607.29600-ham-vln-2026-08-03.md — K219 HAM-VLN decision-coupled world graph
- @concepts/agentic-context-management.md — K193 lifecycle framing
- @sources/arxiv-2607.21503-agentic-context-management.md
- @sources/arxiv-hierarchical-memory-ensemble-qsp-2607.07666-2026-07-13.md — primary
- @concepts/agent-memory-critique.md — eviction = active forgetting
- @concepts/context-compression-resume-pattern.md — mid-term state vs CPR serialize

## Raw Concept

Long-horizon multi-agent work needs **capped hierarchical memory** with explicit eviction — not full-history concat and not cold-start each turn.

## Narrative

Steal from Ensemble QSP (2607.07666):

1. **Short-term** — live turn window + scratchpad facts that survive truncation
2. **Mid-term** — structured project-state JSON; inject only task-relevant slices; auto-summarize decision log
3. **Long-term** — domain handbook + physics/checklists (stable across sessions)

Empirical claim: mid-term inject stays ~**300 tokens median** across 100+ runs when caps + eviction hold.

**K219 HAM-VLN (2607.29600):** decision-coupled agent-authored memory — recent waypoints verbatim in a bounded window; older history re-enters via relevance/recency/salience retrieval + one-hop topology; **>65% context cut** with SR gains on VLN-CE / ObjectNav. Steal for poker/CCC: same call writes action + reflective failure notes; no extra LLM round-trip for memory authoring.

**Poker Arena:** session summaries + last-N hands + decision log — not full trajectory dump into `decide()` context.
**CCC:** PI-style oversight agent + specialist workers with bounded mid-term state.

## Snippets

- Mid-term median 301 tokens / max 4,050 across 104 runs [Source: 2607.07666]
- HAM-VLN: >65% context reduction; 61.0% SR VLN-CER2R (training-free) [Source: 2607.29600]
