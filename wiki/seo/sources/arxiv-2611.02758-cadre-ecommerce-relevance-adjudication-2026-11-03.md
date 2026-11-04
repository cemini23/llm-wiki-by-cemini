---
title: "CADRE — verifier-guided multi-agent adjudication for e-commerce relevance"
type: source
tags: [source, arxiv, relevance, ecommerce, search, distillation]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Learning to Adjudicate: Verifier-Guided Multi-Agent Reasoning for E-Commerce Relevance |
| Authors | Shi Shu, Hao Chen, Baopu Qiu, and others (Tsinghua Shenzhen; Alibaba) |
| arXiv | 2611.02758 |
| Pages | 13 |
| Read status | skimmed (abstract, partially occluded) |

## Narrative

A relevance-judgement system for e-commerce search advertising, deployed and A/B tested.

The method has two layers:

1. **A multi-agent adjudication process guided by a verifier** — several reasoners judge relevance and a verifier arbitrates.
2. **Replay for training** — trajectories that produced correct terminal labels are reused alongside fresh rollouts in later updates.

For serving, **CADRE is distilled into a lightweight student** as an offline teacher, because the multi-agent process is too expensive for online traffic.

Offline evaluation and online A/B tests on an e-commerce advertising platform show improvement in relevance classification and in business and relevance-satisfaction metrics.

### The architecture lesson

**Expensive reasoning offline, cheap inference online.** The adjudication ensemble is a labelling and improvement mechanism, not a serving path. That is the right shape for any relevance or ranking problem where the judgement is expensive and the volume is high: use the expensive process to make labels and to teach a small model, then serve the small model.

It is the same economics as a reference implementation that generates fixtures for a fast one.

**Caveat.** The abstract extract is partially occluded by a copyright block. Only the result description and architecture were captured; no metric values are reproduced here.

## Snippets

> "For efficient online serving, we further use CADRE as an offline teacher to distill its relevance judgments into a lightweight student model. Offline evaluations and online A/B tests on an e-commerce search advertising platform demonstrate that CADRE improves relevance classification and key business and relevance satisfaction metrics." [Source: arxiv-2611.02758 p.1]

## Dead Ends

- **Citing an A/B lift.** The numbers are not in the extracted text.
