---
title: "T-Search — open agentic retriever (Apache-2.0)"
type: entity
tags: [tool, retrieval, agent, rag, apache-2.0, k283]
keywords: [t-search, agentic-retriever, gspo, reciprocal-rank-fusion, recall, t-tech, k283]
related:
  - sources/arxiv-2610.06782-t-search-agentic-retriever-2026-10-06.md
  - concepts/k283-arxiv-wave.md
  - concepts/agent-tool-use-verification.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
---

## Relations

- @sources/arxiv-2610.06782-t-search-agentic-retriever-2026-10-06.md — arXiv 2610.06782
- @concepts/k283-arxiv-wave.md — K283 arXiv hub
- @concepts/agent-tool-use-verification.md — agent verification thread

## Raw Concept

- **Repo:** `github.com/turbo-llm/t-search-harness`
- **Model/collection:** `huggingface.co/collections/t-tech/t-search`
- **License:** **Apache-2.0** (model + harness); benchmarks ODC-BY
- **Paper:** arXiv 2610.06782 (T-Tech)
- **Base:** Qwen3.6-35B-A3B (~3B active)

## Narrative

An open-weight **agentic retriever**. It runs bounded multi-round search and returns **ranked evidence chunks with reasons — not answers** — so the corpus backend and the answer-generator stay swappable.

### Results

56.0 Recall@10 single-rollout (14.4 above base); **61.3** with three RRF-fused rollouts. Highest average across seven English/Russian benchmarks — ahead of larger open models (GLM-5.1 54.0, Tongyi DeepResearch 52.6). One round ≈ Qwen3.5-397B at 40% latency.

### Why it matters here

**Apache-2.0** is the rare clean license in this batch. The retrieves-chunks design is an alternative to answer-generating deep-research agents. Candidate for the wiki's retrieval/routing lane. Route: CCC.

## Snippets

> "T-Search returns ranked evidence chunks with reasons rather than answers, so backend and generator are swappable." [Source: arxiv-2610.06782-t-search-an-open-agentic-retriever-and-playgroun.pdf]
