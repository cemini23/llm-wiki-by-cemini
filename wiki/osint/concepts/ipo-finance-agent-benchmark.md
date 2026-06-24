---
title: IPO Finance Agent — automated rubric eval for long-document financial agents
type: concept
tags: [concept, llm-agents, evaluation, finance, k128]
keywords: [IPO Finance Agent, Finance Agent v2, S-1, contextual retrieval, rubric generation, evaluator-optimizer]
related:
  - sources/arxiv-ipo-finance-agent-2606.23032-2026-06-24.md
  - concepts/llm-agent-systems.md
  - concepts/agentified-agent-assessment.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - sources/arxiv-agentic-time-machine-2606.21013-2026-06-23.md
maturity: draft
created: 2026-06-24
updated: 2026-06-24
---

## Relations

- @sources/arxiv-ipo-finance-agent-2606.23032-2026-06-24.md — K128 primary source
- @concepts/llm-agent-systems.md — eval harness hub
- @concepts/poker-arena-multi-axis-cognitive-profile.md — multi-axis rubric sibling

## Raw Concept

How do you evaluate LLM financial agents on **long IPO filings** when naive chunk retrieval fails, and how can rubrics be generated without full human authorship?

## Narrative

**Finance Agent v2 gap:** periodic 10-K/10-Q tasks with naive chunk RAG; **S-1 IPO** docs are longer and structurally different (pro forma, governance, underwriting risks).

**IPO Finance Agent extensions:**

1. **Contextual retrieval** — industry-standard long-doc RAG replacing naive chunks (required for SpaceX S-1).
2. **Evaluator-optimizer rubric pipeline** — extract facts from answers → draft criteria → LLM audit (omissions, hallucinations, tier errors, redundancy) → human review finals only.
3. **Private held-out split** — 930/1000 questions private anti-contamination.

**Steal matrix (REFERENCE — wiki-only):**

| Component | Poker Arena | PM offline eval |
|-----------|-------------|-----------------|
| Automated rubric repair | Extend nine-axis eval criteria generation | Resolution replay grading |
| Contextual retrieval | N/A (short action contexts) | Long market research memos |
| Cost-accuracy Pareto | Model pick for decide() | Eval batch model tier |

No cemini-prod brief — equity/IPO domain is legacy-deprioritized per `active_project_brief_targets.yaml`.

## Snippets

> "Human experts only review final rubrics before deployment." [Source: arXiv:2606.23032 abstract (retrieved 2026-06-24)]

## Dead Ends

- IPO accuracy leaderboard ≠ trading PnL — do not promote to `core` without Cemini-specific replication.
