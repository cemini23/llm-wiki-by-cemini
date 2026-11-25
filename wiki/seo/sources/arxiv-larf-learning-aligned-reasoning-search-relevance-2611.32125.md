---
title: "LARF: learning-aligned reasoning for search relevance (Tencent Yuanbao)"
type: source
related:
  - concepts/retrieval-vs-citation-visibility-geo.md
  - concepts/generative-engine-optimization.md
  - concepts/scaled-thin-ai-content-risk.md
updated: 2026-11-25
---

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | LARF: Learning-aligned Reasoning Framework for Search Relevance |
| **Author** | Tian Tang, Guo Chen, Reed Li, Hao Wang, Yu Lu, Haijin Liang, Haibo Shi (Tencent Yuanbao Team; Southwest University) |
| **Type** | arXiv preprint (cs.IR) |
| **arXiv ID** | 2611.32125 |
| **Location** | `research to be indexed/seo/arxiv-2611.32125-larf-learning-aligned-reasoning-framework-for-se.pdf` |
| **Retrieved** | 2026-11-25 |
| **Pages** | 16 |
| **Read status** | read |

## Narrative

**Honest relevance: thin, and not actionable for a business.** This is search-relevance engineering inside a large AI-native search product. It has one real link to GEO. The rest is model training.

**The link.** In an AI-native search system, a relevance model decides whether a retrieved document satisfies the user's need. That decision sets ranking quality and the evidence that feeds the generated answer. This is the same gate that @concepts/retrieval-vs-citation-visibility-geo.md describes: a page must first be retrieved, then judged relevant, then cited. LARF makes the middle step explicit and shows that it uses **fine-grained ordinal relevance grades**, not a simple yes or no.

**What the paper builds.** LARF is a three-stage pipeline:

1. Cold-start supervised fine-tuning on selected samples, with chain-of-thought rationales written with multi-agent help.
2. Discriminative GRPO with attribute-wise, list-wise, and rule-consistency rewards, plus a margin loss on the terminal relevance token.
3. Distillation into a dual-head student that keeps classification heads for non-autoregressive inference.

**Why the margin loss matters.** The paper's stated problem is that a trajectory-level reward gives no explicit supervision to the final relevance token. Models then confuse adjacent grades. The fix trains separation between neighbouring labels.

**Results.**

| Metric | Result |
|--------|--------|
| Training / test instances | ~300K train, 16K test, human-annotated web relevance |
| Six-class accuracy (LARF-8B) | +5.78 percentage points |
| NDCG (LARF-8B) | +5.05 points |
| Inference latency, classification-only path | -82.9% |

**What a publisher can take from it.** Very little. The engineering is not transferable to a local business. The one useful inference is directional: AI search engines rank documents in ordered grades and train hard to separate near-ties. Content that is nearly, but not clearly, relevant may lose to a page that is unambiguously on topic. That supports the topical-fit argument on @concepts/scaled-thin-ai-content-risk.md. Mark this as this wiki's inference and `[TENTATIVE]`.

**Limits.** One benchmark, one product. The test set is a human-annotated web relevance set, not a GEO citation corpus. The gains are relative to the paper's own baselines.

## Snippets

> "standard trajectory-level reinforcement learning (RL) objectives do not explicitly enforce margin separation among adjacent ordinal relevance labels." [Source: arxiv-2611.32125-larf-learning-aligned-reasoning-framework-for-se.pdf p.1]
