---
title: DeepSearch-World — verifiable self-evolution for tool-use agents
type: concept
tags: [concept, web-agents, self-distillation, harness, k161]
keywords: [DeepSearch-Evolve, verifiable environment, trajectory filtering, BrowseComp]
related:
  - sources/arxiv-deepsearch-world-2607.07820-2026-07-13.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/generator-verifier-inference-time-steering.md
maturity: draft
created: 2026-07-13
updated: 2026-07-15
---

## Relations

- @sources/arxiv-deepsearch-world-2607.07820-2026-07-13.md — primary
- @concepts/continual-harness-online-self-improvement.md — online self-improve family
- @concepts/generator-verifier-inference-time-steering.md — process verification adjacency

- @seo-wiki/concepts/process-verified-agentic-search-geo.md — SEO GEO entity-hit playbook (K139)
- @seo-wiki/sources/arxiv-geng-2026-deepsearch-world-self-distillation-2607.07820-2026-07-15.md

## Raw Concept

Self-improving tool-use agents need a **deterministic verifiable environment** so trajectory filter/mix can supervise intermediate tool decisions — not only sparse final rewards or teacher imitation.

## Narrative

DeepSearch-Evolve loop: generate → filter → mix → SFT, without stronger-model distillation. Cognitive behaviors to preserve: progress verification, grounded reflection, failure recovery / rollback.

**Poker:** map to sandbox trajectory triage — keep verified failure recoveries and progress checks; drop ungrounded reflection noise.
**CCC:** Watch for open release of env + 420K pool before any Adopt.

## Snippets

- 31.2% BrowseComp / 61.5% GAIA / 93.4% HotpotQA without teacher distill [Source: 2607.07820]
