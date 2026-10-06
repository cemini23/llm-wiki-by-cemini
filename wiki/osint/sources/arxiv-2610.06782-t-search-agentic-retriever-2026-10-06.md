---
title: "T-Search: an open agentic retriever and playground for hard multi-step search (arXiv 2610.06782)"
type: source
tags: [source, k283, arxiv, agents, rag, retrieval, eval]
keywords: [t-search, agentic-retriever, gspo, reciprocal-rank-fusion, recall, deep-research]
related:
  - concepts/k283-arxiv-wave.md
  - concepts/agent-tool-use-verification.md
  - entities/tools/t-search.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
read_status: read
---

## Relations

- @concepts/k283-arxiv-wave.md
- @concepts/agent-tool-use-verification.md

## Raw Concept

| Title | T-Search: An Open Agentic Retriever and Playground for Hard Multi-Step Search |
| Authors | Tsymboi, Latypov, Medvedev, Taranets, Stoianov, Gulyakov, Alektorov, Potapov (T-Tech) |
| Type | arXiv preprint (cs.CL) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.06782-t-search-an-open-agentic-retriever-and-playgroun.pdf` |
| Retrieved | 2026-10-06 |
| arXiv | 2610.06782v1 |
| License | **Apache-2.0** (model + harness); benchmarks ODC-BY |
| Artifacts | huggingface.co/collections/t-tech/t-search · github.com/turbo-llm/t-search-harness |
| read-status | read |

## Narrative

An open-weight **agentic retriever**. Base model Qwen3.6-35B-A3B (≈3B active). It runs bounded multi-round search and returns **ranked evidence chunks with reasons — not answers** — so the backend and the answer-generator stay swappable.

### Method

Three tools: `search_corpus`, `save_and_advance`, `finalize_ranking`. Budget: ≤ 5 rounds, 32k-token context per round, search locks at 75% of context, at least 5 searches before advancing. Training: round-sliced SFT, then **GSPO** on a recall reward r = |F ∩ G| / |G|. Three parallel rollouts are fused with **reciprocal rank fusion (RRF)**.

### Results

- **56.0 Recall@10**, single rollout — 14.4 above base.
- **61.3** with three fused rollouts.
- Highest average over seven English/Russian benchmarks, ahead of *larger* open models: GLM-5.1 (54.0), Tongyi DeepResearch (52.6).
- One round ≈ Qwen3.5-397B at **40% latency**.

### Why it matters here

**Apache-2.0** — the licensing is clean, unlike most rows in this batch. The retrieves-chunks-with-reasons design is an alternative to answer-generating deep-research agents. This is a candidate for the RAG/eval lane and for the wiki's own retrieval work. Route to CCC.

## Snippets

> "T-Search returns ranked evidence chunks with reasons rather than answers, so backend and generator are swappable." [Source: arxiv-2610.06782-t-search-an-open-agentic-retriever-and-playgroun.pdf]

> "One round is comparable to Qwen3.5-397B at 40% latency." [Source: arxiv-2610.06782-t-search-an-open-agentic-retriever-and-playgroun.pdf]
