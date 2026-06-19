---
title: "Pan et al. 2026 — ScholarQuest agentic academic paper search (arXiv 2606.20235)"
type: source
tags: [source, arxiv, benchmark, agentic-search, literature, k123]
keywords: [2606.20235, ScholarQuest, ScholarBase, agentic search, academic paper retrieval]
related:
  - entities/tools/scholarquest.md
  - concepts/federated-daily-research-digest.md
  - concepts/monokern-compounding-research-pipeline.md
  - concepts/cemini-wiki-ingest-workflow.md
maturity: validated
read_status: read
created: 2026-06-19
updated: 2026-06-19
cross-wiki-source: "@seo-wiki/sweeps/2026-06-19-daily.md"
---

## Relations

- @entities/tools/scholarquest.md — benchmark + ScholarBase backend
- @concepts/federated-daily-research-digest.md — daily digest paper-discovery eval steal
- @concepts/monokern-compounding-research-pipeline.md — weekly deep-research quality bar
- @concepts/cemini-wiki-ingest-workflow.md — ingest pipeline literature discovery

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | ScholarQuest: A Taxonomy-Guided Benchmark for Agentic Academic Paper Search in Open Literature Environments |
| **Authors** | Tingyue Pan et al. (USTC) |
| **arXiv** | 2606.20235v1 |
| **Repo** | https://github.com/pty12345/ScholarQuest |
| **Retrieved** | 2026-06-19 |
| **Read status** | read (design, benchmark scope, baseline results) |

## Narrative

**ScholarQuest** — large-scale benchmark for **agentic** academic paper search vs single-shot retrieval. **1,000+ CS topics**, **four query intents** (method-oriented, setting-anchored, comparison-based, scope-controlled). **ScholarBase** million-scale arXiv testbed with unified retrieval + citation-expansion APIs.

Best agent: **Recall@100 = 0.314**, **Recall@All = 0.355** — substantial headroom. Agentic methods beat single-shot baselines; failures often **off-target exploration** not insufficient effort.

**OSINT steal:** taxonomy-guided query generation for evaluating federation **daily digest** paper-discovery agents; citation expansion mirrors wiki ingest literature fan-out.

**Phase-0:** GitHub 0 stars, **no LICENSE** filed — **CONDITIONAL-GO** pending license verification.

## Snippets

> "Agentic methods outperform single-shot retrieval baselines, yet the best-performing agent only achieves 0.314 Recall@100." [Source: arxiv-2606.20235 §Abstract]
