---
title: "ETAMem: multi-view memory for long-term conversational agents"
type: source
tags: [source, arxiv, long-term-memory, conversational-agents, personalization]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | ETAMem: Decoupling and Aligning Heterogeneous Memory for Long-Term Conversational Agents |
| Authors | Xinying Qian et al., Nankai University (co-authors at Tiangong University and the University of Edinburgh) |
| arXiv | 2610.37443 |
| File | `arxiv-2610.37443-etamem-decoupling-and-aligning-heterogeneous-mem.pdf` |
| Retrieved | 2026-11-01 |
| URL | https://arxiv.org/abs/2610.37443 |
| Read status | skimmed (abstract + intro) |

## Narrative

Long-term memory lets a large language model keep a coherent and personalized exchange across a long conversation. The paper names two failures in current memory systems. Information Entanglement mixes different information inside one coarse memory unit. Organizational Mismatch orders memory mainly by semantic similarity and can miss other associations.

ETAMem is a multi-view memory framework. It separates mixed conversational information. It then aligns each memory representation and each organization with the character of that information. Heterogeneous information parsing extracts atomic memory units and identifies affective information. View-specific memory structuring places those units in three complementary hierarchical views: Event, Affect, and Time. ETAMem maintains the structures as the conversation grows. It uses adaptively calibrated thresholds.

Retrieval is entropy-based. The method assigns a query-specific budget across the views. It then runs a hierarchical search inside each view.

The reported tests are LoCoMo and LongMemEval-S. The paper says ETAMem beats state-of-the-art baselines. The relative accuracy improvement is 12.46% on LoCoMo and 7.96% on LongMemEval-S. Both figures are single-source claims from this abstract. The paper also says token efficiency stays competitive. A further analysis in the paper says the memory views complement one another.

The stated task is personalization and question answering over long conversations. That task matches a local-SEO or digital-marketing chat that must stay coherent for one person across many turns. The paper claims two causes of failure: mixed information inside coarse memory units, and memory organized mainly by semantic similarity. ETAMem claims three hierarchical views (Event, Affect, and Time) and entropy-based retrieval with a query-specific budget. The 12.46% and 7.96% figures are single-source claims from this abstract.

## Snippets

> "To address these challenges, we propose ETAMem, a multi-view memory framework that decouples heterogeneous conversational information and aligns memory representations and organization with its distinct characteristics. Experiments on LoCoMo and LongMemEval-S demonstrate that ETAMem outperforms state-of-the-art baselines, achieving relative accuracy improvements of 12.46% and 7.96%, respectively, while maintaining competitive token efficiency." [Source: `arxiv-2610.37443-etamem-decoupling-and-aligning-heterogeneous-mem.pdf` p.1 (arXiv 2610.37443), retrieved 2026-11-01]
