---
title: 'ESGLens: An LLM-Based RAG Framework for Interactive ESG Report Analysis and Score Prediction'
type: source
tags: [pdf, llm-agents, k49]
keywords: [ESGLens, LLM, RAG, ESG, report analysis, score prediction, GRI, LSEG, embeddings]
related:
  - concepts/llm-agent-systems.md
clusters: [llm-agents]
maturity: validated
read_status: deep-read
created: 2026-04-27
updated: 2026-05-16
---

## Relations

- @concepts/llm-agent-systems.md — cluster hub for LLM agent systems in the Cemini corpus

## Raw Concept

- **Original title**: ESGLens: An LLM-Based RAG Framework for Interactive ESG Report Analysis and Score Prediction
- **Author(s)**: Tsung-Yu Yang, Meng-Chi Chen (Massachusetts Institute of Technology)
- **Type**: PDF (arXiv 2604.19779)
- **Location**: cemini-librarian:/opt/cemini-bulk/research/ESGLens- .pdf
- **Retrieved**: 2026-04-27
- **Length**: 20p
- **Read status**: deep-read
- **Cluster**: llm-agents

## Narrative

Yang & Chen present ESGLens, a proof-of-concept LLM-RAG framework for analyzing corporate ESG (Environmental, Social, Governance) reports — documents central to investment decision-making but costly to analyze manually because they are long, heterogeneous, and lack a standardized template. ESGLens automates three tasks: (1) structured information extraction guided by Global Reporting Initiative (GRI) standards, (2) interactive question-answering with source traceability, and (3) ESG score prediction via regression on LLM-generated embeddings.

The pipeline is purpose-built: a report-processing module segments heterogeneous PDF content into typed chunks (text, tables, charts); a GRI-guided extraction module retrieves and synthesizes information aligned to specific standards; and a scoring module embeds extracted summaries and feeds them to a regression model trained against London Stock Exchange Group (LSEG) reference scores. The framework is evaluated on ~300 reports from QQQ, S&P 500, and Russell 1000 constituents (FY2022). Among three embedding methods (ChatGPT, BERT, RoBERTa) and two regressors (Neural Network, LightGBM), ChatGPT embeddings with a Neural Network achieve a Pearson correlation of 0.48 (R² ≈ 0.23) against LSEG ground-truth scores — a modest but statistically meaningful signal given the small training set and restriction to the environmental pillar. A traceability audit found 8 of 10 extracted claims verify against the source document, the two failures attributable to few-shot example leakage. The authors are explicit that this is a minimum-viable prototype, limited by dataset size and environmental-only coverage.

**Cemini relevance**: an LLM-RAG framework that turns unstructured corporate disclosures into structured, scored investment signals — a directly transferable pattern for any Cemini effort that ingests filings or sustainability reports into the trading-stack knowledge base.

## Snippets

> "We present ESGLens, a proof-of-concept framework combining retrieval-augmented generation (RAG) with prompt-engineered extraction to automate three tasks: (1) structured information extraction guided by Global Reporting Initiative (GRI) standards, (2) interactive question-answering with source traceability, and (3) ESG score prediction via regression on LLM-generated embeddings." [Source: ESGLens- .pdf p.1]

> "ChatGPT embeddings with a Neural Network achieve a Pearson correlation of 0.48 (R2 ≈ 0.23) against LSEG ground-truth scores – a modest but statistically meaningful signal given the ∼300-report training set and restriction to the environmental pillar." [Source: ESGLens- .pdf p.1]

> "A traceability audit shows that 8 of 10 extracted claims verify against the source document, with two failures attributable to few-shot example leakage." [Source: ESGLens- .pdf p.1]
