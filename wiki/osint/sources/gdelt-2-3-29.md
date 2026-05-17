---
title: "CoreEval: Automatically Building Contamination-Resilient Datasets with Real-World Knowledge toward Reliable LLM Evaluation"
type: source
tags: [pdf, k49, llm-agents]
clusters: [llm-agents]
related:
  - concepts/llm-agent-systems.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-05-16
---

## Relations

- @concepts/llm-agent-systems.md — cluster hub for LLM agent-systems research in the Cemini corpus

## Raw Concept

- **Original title**: CoreEval: Automatically Building Contamination-Resilient Datasets with Real-World Knowledge toward Reliable LLM Evaluation
- **Author(s)**: Jingqian Zhao, Bingbing Wang, Geng Tu, Yice Zhang, Qianlong Wang, Bin Liang, Jing Li, Ruifeng Xu (Harbin Institute of Technology Shenzhen; Peng Cheng Laboratory; CUHK; Hong Kong PolyU). arXiv:2511.18889v1, Nov 2025.
- **Type**: PDF
- **Location**: research for cemini/gdelt 2 3:29.pdf
- **Retrieved**: 2026-04-23 (filename date reflects download date, not publication)
- **Length**: 23p
- **Read status**: deep-read
- **Primary cluster**: llm-agents
- **All clusters**: llm-agents

## Narrative

CoreEval tackles **data contamination** in LLM benchmarking — the problem that public, static evaluation datasets may have leaked into model training corpora, artificially inflating measured performance. Reported contamination rates run 1%–45% across six QA benchmarks, and the paper notes simple paraphrasing can let even a 13B model overfit a benchmark to GPT-4-comparable scores. Two existing mitigations fall short: **data rewriting** (LLM edits existing data, risking label drift and re-introducing contaminated content from model priors) and **data generation** (LLM creates fresh data, losing the original's semantic complexity).

CoreEval is a three-stage pipeline framed on Bruner's cognitive learning theory: (1) **Real-World Knowledge Attainment** — extract entity relationships from the original data and query the **GDELT** Global Knowledge Graph for relevant up-to-date real-world knowledge; (2) **Knowledge Recontextualization** — integrate the retrieved knowledge with the original data, refining and restructuring it to keep semantic coherence and task alignment; (3) a **Data Reflection** mechanism that iteratively verifies and refines labels to enforce consistency between the updated and original datasets. Because the injected knowledge post-dates training cutoffs, the resulting datasets resist contamination while preserving the source's difficulty and structure. Experiments across multiple NLP tasks (sentiment, stance, emotion) and several LLMs show CoreEval reliably reduces performance overestimation versus rewriting/generation baselines.

**Cemini relevance**: a news-RAG and LLM-evaluation methodology for the librarian — GDELT-grounded dataset refresh is a template for contamination-resilient evaluation of any model that consumes the wiki, and the entity-extraction + reflection loop mirrors ingest-pipeline quality control.

## Snippets

> "Data contamination poses a significant challenge to the fairness of LLM evaluations ... To address these limitations, we propose CoreEval, a Contamination-resilient Evaluation strategy for automatically updating data with real-world knowledge." [Source: gdelt 2 3:29.pdf p.1]

> "Li et al. (2024c) reported contamination rates from 1% to 45% across six Question Answering (QA) benchmarks ... Simple test variations, such as paraphrasing, can bypass these methods, allowing even a 13B model to overfit benchmarks and perform comparably to GPT-4." [Source: gdelt 2 3:29.pdf p.2]
