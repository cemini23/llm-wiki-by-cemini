---
title: ScholarQuest — agentic academic paper search benchmark (CONDITIONAL-GO)
type: entity
tags: [tool, benchmark, agentic-search, literature, k123]
keywords: [ScholarQuest, ScholarBase, arXiv, agentic retrieval]
related:
  - sources/arxiv-scholarquest-agentic-academic-search-2606.20235-2026-06-19.md
  - concepts/federated-daily-research-digest.md
  - concepts/monokern-compounding-research-pipeline.md
  - concepts/cemini-wiki-ingest-workflow.md
maturity: draft
created: 2026-06-19
updated: 2026-06-19
phase_0_verdict: CONDITIONAL-GO
license_verified: false
repo: https://github.com/pty12345/ScholarQuest
cross-wiki-source: "@seo-wiki/sweeps/2026-06-19-daily.md"
---

## Relations

- @sources/arxiv-scholarquest-agentic-academic-search-2606.20235-2026-06-19.md
- @concepts/federated-daily-research-digest.md — eval target for overnight paper fetch quality
- @concepts/monokern-compounding-research-pipeline.md — weekly synthesis literature coverage

## Raw Concept

Phase-0 from K123 SEO digest cross-route — arXiv 2606.20235 + GitHub `pty12345/ScholarQuest`.

## Narrative

### Phase-0 verdict: **CONDITIONAL-GO**

| Check | Result |
|-------|--------|
| License | **None** on GitHub API (2026-06-19) — block adoption until SPDX confirmed |
| Maturity | 0 stars; last push 2026-05-19; paper + code claimed public |
| Failure mode | Reproducibility depends on ScholarBase backend availability |
| Wiki overlap | Federation daily digest uses Exa + preingest_check — ScholarQuest offers structured agentic eval |

**Steal-from:** taxonomy of research intents; citation-expansion answer construction; Recall@k + efficiency + intent-robustness eval dimensions.

**Adopt when:** license verified (likely Apache/MIT — confirm); use to regression-test `daily_research_digest_run.py` paper lane against ScholarQuest query slices.

## Snippets

> "ScholarBase provides unified retrieval, inspection, and citation-expansion interfaces." [Source: arxiv-2606.20235 §1]
