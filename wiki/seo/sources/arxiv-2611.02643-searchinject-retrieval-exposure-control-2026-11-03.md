---
title: "SearchInject — controlling which pages reach model context"
type: source
tags: [source, arxiv, prompt-injection, search, rag, defence]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | SearchInject: Retrieval Exposure Control for Indirect Prompt Injection in Language-Model Search |
| Authors | Kainan Zhou, Gangzhen Qian, Janet Sung (Google LLC) |
| arXiv | 2611.02643 |
| Pages | 6 |
| Read status | skimmed (abstract) |

## Narrative

**The most practical paper in this batch for anything that does retrieval-then-generate.**

The premise: an indirect prompt injection can only affect a search-augmented model **after its carrier page reaches model context**. Everything upstream of that moment is irrelevant; everything downstream is too late. So the defence belongs at the **admission decision**.

SearchInject scores candidates on four signals:

1. retrieval relevance,
2. search-abuse cues,
3. instruction likelihood,
4. two relevance interactions.

A **quarantine threshold** is chosen under an empirical constraint — **0.5% clean-candidate false quarantine** on a calibration split — so the filter is tuned to not break legitimate results, rather than to maximise a detection rate.

### Results

Across 1 200 query–family outcomes per retriever, **top-10 target exposure**:

| Retriever | Before | After |
|-----------|--------|-------|
| BM25 | 0.9408 | **0.1583** |
| Normalised hybrid | 0.9158 | **0.1508** |
| LSA | 0.8450 | **0.1375** |

Relative reductions of **83.2–83.7%**, with the largest absolute change in clean nDCG@10 of **0.0018** — essentially no cost to legitimate ranking.

The paper is honest about limits: the frozen threshold yields clean test false-quarantine rates of **0.59–0.65%**, above the 0.5% calibration target. A separate 104-case generation follow-up records **context removal but no confirmed undefended hijacks**, so the generation-level benefit is not demonstrated.

### Why the honest parts matter

Reporting that the threshold missed its calibration constraint on test, and that the generation-level follow-up found no confirmed attack to prevent, is rarer than the headline. It means the mechanism is demonstrated at the retrieval layer and the end-to-end claim is open.

**Relevance.** Any pipeline that fetches web content into a model — newsletter summarisation, comp extraction, link evaluation — has this exact moment. The design lesson is that the filter should be tuned against false positives on clean data, not against a detection rate.

## Snippets

> "An indirect prompt injection can affect a search-augmented large language model only after its carrier page reaches model context. SearchInject controls this admission decision…" [Source: arxiv-2611.02643 p.1]

> "top-10 target exposure falls from 0.9408 to 0.1583 for BM25, from 0.9158 to 0.1508 for a normalized hybrid, and from 0.8450 to 0.1375 for latent semantic analysis." [Source: arxiv-2611.02643 p.1]

## Dead Ends

- **Claiming this prevents injection end to end.** The generation follow-up found no confirmed hijacks to prevent.
