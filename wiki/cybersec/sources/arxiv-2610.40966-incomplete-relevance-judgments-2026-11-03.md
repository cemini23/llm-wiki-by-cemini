---
title: "Better retrievers, worse labels — incomplete relevance judgments distort abstention scores"
type: source
tags: [source, arxiv, rag, evaluation, abstention, benchmark-bias]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Better Retrievers, Worse Labels: How Incomplete Relevance Judgments Distort Abstention Evaluation in Conversational RAG |
| Authors | Ivan Kochergin (Letovo School), Vasily Konovalov (AXXX) |
| arXiv | 2610.40966 |
| Pages | 11 |
| Read status | skimmed (abstract) |

## Narrative

A measurement-bias paper, and a sharp one.

Conversational RAG benchmarks score abstention by reading sufficiency off relevance judgments: a retrieved context with no gold document is treated as unanswerable. The authors test that shortcut on RECOR with four retrievers (nDCG@10 from .18 to .59) and three Qwen3 readers.

### The finding

**The better the retriever, the worse the shortcut.**

| Retriever strength | Share of no-gold contexts that actually contain the answer |
|---|---|
| Weakest | 28% |
| Strongest | **72%** |

And the shortcut's precision falls accordingly: **.68 → .10**, or **.70 → .21** under blind audit.

A reader confirms it: Qwen3-4B answers **62–67%** of these "false misses" correctly, against 23–30% of contexts judged insufficient and 1% with no documents at all.

Where the answers come from: hard negatives mined for the same question, another turn's gold, or a neighbouring chunk of the gold page.

On MTRAG, with human judgments, precision still drops from .72 to .50.

### Why this is a general lesson

The benchmark's negative labels are **derived from an incomplete annotation process**, and improving retrieval moves the system into regions the annotation never covered. So a better system scores worse against a label set that was built for a weaker one.

That is a reusable warning for any evaluation built on "no positive found" as a negative: **absence of evidence in the annotation is being scored as evidence of absence.**

**Caveat.** Abstract only; exact per-retriever figures are given as ranges above.

## Snippets

> "The stronger the retriever, the larger the share of no-gold contexts that still contain the answer (28% to 72%) and the lower the shortcut's precision (.68 to .10; .70 to .21 under the audit)." [Source: arxiv-2610.40966 p.1]

## Dead Ends

- **Scoring abstention off relevance judgments.** That is the shortcut the paper breaks.
