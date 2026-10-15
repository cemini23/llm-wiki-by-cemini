---
title: "LongHisDoc — A Benchmark for Chinese Long Historical Document Understanding"
type: source
tags: [arxiv, benchmark, document-ai, retrieval, ocr]
keywords: [long document, historical documents, LVLM, RAG, benchmark, QA]
related:
  - concepts/k291-osint-wave.md
maturity: draft
read_status: skimmed
created: 2026-10-14
updated: 2026-10-14
---

## Relations

- @concepts/k291-osint-wave.md — K291 osint wave hub

## Raw Concept

Title: LongHisDoc — A Comprehensive Benchmark for Chinese Long Historical Document Understanding
Authors: Zeyu Shan, Yongxin Shi, Shihang Wu, Peirong Zhang, Yuanyuan Fang, Zhaopeng Wang, Lianwen Jin (SCUT, Sichuan University)
Type: arXiv preprint (2610.14531)
Location: `research to be indexed/osint/arxiv-2610.14531-longhisdoc-a-comprehensive-benchmark-for-chinese.pdf`
Retrieved: 2026-10-14
Read status: skimmed

## Narrative

**The first benchmark for long (full-book) historical document understanding.** 1,012 expert-annotated QA pairs from 101 PDFs, averaging **85.1 pages and 42,776 tokens per document**, across 10 categories and four QA types: single-page, cross-page, multi-hop, and **unanswerable**.

**Headline result — frontier models are far from solving this.** Best LVLM reaches **62.9%**; best LLM **69.9%**. Answers need multimodal evidence from text, layout, *and* visual elements together. The paper also benchmarks modal retrievers and end-to-end RAG.

**Why it matters here:** the **unanswerable** QA class and the 85-page document length are the two design choices worth noting. Both address failure modes that a shorter, always-answerable benchmark cannot expose.

## Snippets

> "Our evaluation reveals that the top-performing LVLM and LLM achieve only 62.9% and 69.9% accuracy, respectively, highlighting a substantial performance gap." [Source: arxiv-2610.14531 p.1]

## Dead Ends

- Reading 62.9% as a near-solved task. The benchmark includes unanswerable questions, so a naive always-answer strategy is penalised.
