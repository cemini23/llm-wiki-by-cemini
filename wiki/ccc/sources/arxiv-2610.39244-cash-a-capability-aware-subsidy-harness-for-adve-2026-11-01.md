---
title: "CASH: capability licences that govern an LLM-plus-model agent harness"
type: source
tags: [source, arxiv, llm-agents, harness-design, allocation]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | CASH: A Capability-Aware Subsidy Harness for Advertiser Subsidy Allocation |
| Authors | Minmao Wang (Fudan University), Huihuang Lin, Likun Wu (Tianjin University), Hongke Zhao, Shijie Yi, Fei Pan (Kuaishou Technology) |
| arXiv | 2610.39244 |
| File | `arxiv-2610.39244-cash-a-capability-aware-subsidy-harness-for-adve.pdf` |
| Retrieved | 2026-11-01 |
| URL | https://arxiv.org/abs/2610.39244 |
| Read status | skimmed (abstract + intro) |

## Narrative

The task is Advertiser Subsidy Allocation. A platform gives billing discounts to
advertisers. It must pick a subsidy level for every account. It must maximise total
discounted revenue under a platform-wide cap on the subsidy rate.

Operators set these subsidies today from business rules, advertiser tiers and operating
goals. The paper says tier-level policy breaks as the advertiser base grows. A tier cannot
say how one account responds to each subsidy level, and it cannot spend a shared budget
account by account.

CASH pairs a knowledge-guided LLM with a data-driven numerical response model. It learns
from realised outcomes where each source is locally reliable across accounts and subsidy
levels. It then turns that reliability into **capability licences**. The licences govern
three things: which source answers, the agent review step, and the budget allocation.

An **Expected Policy Coverage Gain** signal directs a limited feedback budget toward the
evidence most likely to widen high-value reliable coverage. The new feedback improves the
numerical model and updates the capability estimates.

The online result is one month on a large advertising platform, with CASH serving 60% of
traffic. Revenue per account rose **15.35%** and ADVV rose **19.86%** over control, at an
essentially unchanged subsidy rate. The authors also report gains in revenue quality, LTV
and retention. These are single-source claims from this abstract.

For a harness designer the transferable idea is the licence layer. A controller states
which component is trusted for which region, and routes work by that estimate rather than
by a fixed rule. The paper applies it to subsidy allocation. The pattern is general.

## Snippets

> "CASH pairs a knowledge-guided large language model (LLM) with a data-driven numerical response model, learns from realized outcomes where each is locally reliable across accounts and subsidy levels, and turns this reliability into explicit capability licenses that govern source selection, agent review and budget allocation." [Source: `arxiv-2610.39244-cash-a-capability-aware-subsidy-harness-for-adve.pdf` p.1 (arXiv 2610.39244), retrieved 2026-11-01]
