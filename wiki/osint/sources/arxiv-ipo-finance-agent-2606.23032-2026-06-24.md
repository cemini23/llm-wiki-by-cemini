---
title: "IPO Finance Agent — LLM financial analyst eval beyond Finance Agent v2 (arXiv 2606.23032)"
type: source
tags: [source, arxiv, llm-agents, finance, evaluation, k128]
keywords: [2606.23032, IPO Finance Agent, Finance Agent v2, S-1, contextual retrieval, rubric generation, SpaceX SPCX]
related:
  - concepts/ipo-finance-agent-benchmark.md
  - concepts/llm-agent-systems.md
  - concepts/agentified-agent-assessment.md
  - sources/arxiv-agentic-time-machine-2606.21013-2026-06-23.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
maturity: draft
read_status: read
created: 2026-06-24
updated: 2026-06-24
clusters: [llm-agents, quant-finance]
---

## Relations

- @concepts/ipo-finance-agent-benchmark.md — K128 synthesis
- @concepts/llm-agent-systems.md — eval harness cluster
- @concepts/agentified-agent-assessment.md — automated rubric generation pattern

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | IPO Finance Agent: Evaluation of LLM Financial Analysts beyond Finance Agent v2, with Automated Rubric Generation — the Case of the SpaceX (SPCX) IPO |
| **Authors** | Mostapha Benhenda |
| **arXiv** | 2606.23032v2 (Jun 2026) |
| **Repo** | https://github.com/benstaf/ipoagent |
| **sha256** | `b53da4c194cac1c90685e60cf5fffff938fcf50b6852ee86cb46e2d852015565` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.23032-2606.23032v1-ipo-finance-agent-evaluation-of-llm.pdf` |
| **Retrieved** | 2026-06-24 (inbox) |
| **Read status** | read (abstract + method + headline results) |

## Narrative

Extends **Finance Agent v2** (Vals AI SEC 10-K/10-Q benchmark) to **IPO S-1 diligence** — longer documents, pro forma accounting, underwriting-sensitive risk disclosures. Original FABv2 harness **failed on SpaceX S-1 length**; authors add **contextual retrieval** (industry-standard long-doc RAG).

**Dataset:** 1,000 IPO-diligence questions; **70 public** on SpaceX (SPCX) S-1; remainder private anti-contamination split.

**Evaluator-optimizer pipeline:** extract candidate facts from model answers → consolidate draft rubrics → LLM audit for omissions/hallucinations/tier errors/redundancy → human review final rubrics only.

**Headline results [TENTATIVE — paper table]:**

| Model | Accuracy | Cost/query |
|-------|----------|------------|
| Qwen 3.7 Max | 79.4% | $0.30 |
| MiMo-2.5 Pro | 76.8% | $0.05 |
| FABv2 ceiling (Gemini 3.5 Flash) | 57.9% | $2.51 |

**Cemini posture:** **REFERENCE / wiki-only** — steal **automated rubric repair loop** for agent eval (poker multi-axis, PM offline replay), not IPO trading alpha. No cemini-prod brief (legacy MAPPO/equity eval deprioritized).

## Snippets

> "Finance Agent v2 harness basically failed to deliver any output related to the SpaceX S-1 filing, due to document length." [Source: arXiv:2606.23032 §intro (retrieved 2026-06-24)]

> "We introduce an evaluator-optimizer pipeline to automatically generate evaluation rubrics for the benchmark: candidate facts are extracted from model answers, consolidated into draft criteria, then automatically audited for omissions, hallucinations, mistiered items, and redundancy." [Source: arXiv:2606.23032 abstract (retrieved 2026-06-24)]

> "Alibaba Qwen 3.7 Max, reaches 79.4% accuracy at 0.30 USD per query." [Source: arXiv:2606.23032 abstract (retrieved 2026-06-24)]

## Dead Ends

- IPO diligence domain ≠ Polymarket/Kalshi event contracts — no direct pm-kalshi brief.
- SpaceX S-1 case is single-name — generalization to PM resolution research unverified.
