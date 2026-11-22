---
title: "Typed decision models vs fine-tuned classifiers — no SEO link, recorded for inventory"
type: source
related:
  - concepts/corpus-overflow-out-of-scope.md
updated: 2026-11-22
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Do We Still Need Fine-Tuned Classifiers? Swapping Typed Decision Models into 24 ACL-Venue Papers |
| Authors | Marek Šuppa (Comenius University; Cisco); Jaroslav Kopčan (Kempelen Institute) |
| arXiv | 2611.20191 |
| Pages | 11 (approx.) |
| File | `arxiv-2611.20191-do-we-still-need-fine-tuned-classifiers-swapping.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2611.20191-do-we-still-need-fine-tuned-classifiers-swapping.pdf` |
| Retrieved | 2026-11-22 |
| Read status | read |

## Narrative

**No SEO link.** This paper studies NLP classification methods. It has no connection to search engines, retrieval, citation, or local ranking. The page exists for inventory honesty and links from @concepts/corpus-overflow-out-of-scope.md.

The authors ask how many fine-tuned classifiers a Typed Decision Model can replace under each paper's own evaluation. A Typed Decision Model answers a typed question with a probability for each option and needs no training. The authors swap the predictors of 24 ACL-venue papers for one such model, Jev, and keep each paper's splits, labels, and metric.

With a zero-shot prompt, Jev directly replaced the paper's predictor on 12 of 46 test sets. With 500 training labels and prompt optimization, the method closed a median 72% of the gap to the paper's method, at a median $1.66 per search. LoRA fine-tuning of Qwen3.8-27B closed 97%. The paper's conclusion: fine-tuning is still the most accurate option, but a zero-shot prompt is often enough for plain labels. The percentages are single-source claims.

## Snippets

> "Fine-tuning remains the most accurate option, but a zero-shot prompt is often enough for plain labels, and prompt optimization closes most of the remaining gap." [Source: `arxiv-2611.20191-do-we-still-need-fine-tuned-classifiers-swapping.pdf` p.1 (arXiv 2611.20191), retrieved 2026-11-22]
