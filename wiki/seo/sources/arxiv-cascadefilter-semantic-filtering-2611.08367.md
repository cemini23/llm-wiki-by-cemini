---
title: "CascadeFilter — cheap evidence first, full page second, oracle last"
type: source
tags: [source, arxiv, retrieval, filtering, geo-aeo, cost]
keywords: [CascadeFilter, semantic filtering, cascade, threshold selection, passage evidence, chunk view, BM25, reciprocal rank fusion]
related:
  - concepts/passage-evidence-screening-geo.md
  - concepts/retrieval-vs-citation-visibility-geo.md
  - entities/tools/denseon-lateon.md
maturity: draft
read_status: read
created: 2026-11-10
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | CascadeFilter: Cost-Efficient Semantic Filtering with Joint Threshold Selection |
| Author | Yanji He, Tao Zhong, Hongyang Chen, Xiaobo Zhang, Mingyu Yang, Wei Wang |
| Type | arXiv preprint (cs.IR / data systems) |
| arXiv | 2611.08367v1, 5 Nov 2026 |
| Location | `research to be indexed/seo/arxiv-2611.08367-cascadefilter-cost-efficient-semantic-filtering.pdf` |
| Retrieved | 2026-11-10 |
| File | `arxiv-2611.08367-cascadefilter-cost-efficient-semantic-filtering.pdf` |
| Pages | 18 |
| Read status | read (abstract, method, results, appendix I) |

## Narrative

**The question.** A system must decide whether each document in a large set satisfies a natural-language condition. One example: "does this review mention a billing issue?" Running a large model on every document costs a lot. A cheap model saves money but makes more mistakes. A cascade runs the cheap model first and sends uncertain records to an expensive oracle.

**The three stages.** Stage 1 runs a small language model (SLM) on **extracted evidence**. Stage 2 runs the same SLM on the **full document**. Stage 3 sends the remaining records to the **oracle**, a frontier model. [Source: arxiv-2611.08367 p.1]

**The contribution is the threshold search.** Earlier cascade work calibrated thresholds in a fixed sequence after the cascade was assembled. This paper searches the two thresholds **jointly** over a grid that is fixed before calibration. It picks the cheapest configuration that meets an error target. It then certifies the error bound on a sample drawn without replacement. [Source: arxiv-2611.08367 p.1-2]

**Why the first stage is the interesting one for search work.** The authors name three gaps in earlier cascades. The first is **locality**: a chunk view "isolates the deciding signal — a different error mode, not just cheaper". The full-document view dilutes that signal. Their motivating example shows a **28-token** deciding passage against a **430-token** full document. [Source: arxiv-2611.08367 p.3]

**Reported results.** Across 13 evaluation settings the method reports the highest benchmark accuracy in 12 and the highest macro-F1 in 12. Mean accuracy is **0.938** against **0.900** for Task Cascades. Mean macro-F1 is **0.887** against **0.830**. The authors state plainly that these comparisons describe the reported operating points, and that the accuracy guarantee concerns agreement with the oracle, not with ground truth. [Source: arxiv-2611.08367 p.1, p.9]

**Supporting components.** Hybrid lexical (BM25) plus dense retrieval, fused with reciprocal rank fusion. A reranker. A neighbour-agreement term in the routing score. The authors say these components support the threshold design, and are not separate claims of new retrieval algorithms. [Source: arxiv-2611.08367 p.2]

### What this means for GEO

A generative search engine filters the retrieved set before it writes an answer. If a cheap stage reads a short passage first, then **the short passage decides**. A page that states the deciding fact in one compact, self-contained block passes an earlier and cheaper gate. A page that buries the fact in a long page asks the filter to pay for the full document.

This is a mechanism-level argument, not a measured result on a search engine. Tag it accordingly.

## Snippets

> "Chunk view isolates the deciding signal — a different error mode, not just cheaper." [Source: arxiv-2611.08367 p.3]

> "The accuracy guarantee concerns agreement with the oracle." [Source: arxiv-2611.08367 p.1]

> "These components enhance the cascade while leaving its certification interface unchanged." [Source: arxiv-2611.08367 p.1]

## Dead Ends

- **Treating the 0.938 accuracy figure as real-world accuracy.** The paper compares against an oracle, not against ground truth. The authors state this limit themselves.
