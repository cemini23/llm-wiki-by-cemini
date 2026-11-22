---
title: "JointQ quantization for LLMs — no SEO link, recorded for inventory"
type: source
related:
  - concepts/corpus-overflow-out-of-scope.md
updated: 2026-11-22
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | JointQ: Joint Scale-and-Integer Quantization for Large Language Models |
| Authors | Keiji Kimura, Yuma Ichikawa (Fujitsu Limited) |
| arXiv | 2611.20384 |
| Pages | 8 (approx.) |
| File | `arxiv-2611.20384-jointq-joint-scale-and-integer-quantization-for.pdf` |
| Location | `research to be indexed/seo/arxiv-2611.20384-jointq-joint-scale-and-integer-quantization-for.pdf` |
| Retrieved | 2026-11-22 |
| Read status | read |

## Narrative

**No SEO link.** This paper is about model compression. It has no connection to search engines, retrieval, citation, or local ranking. The page exists for inventory honesty and links from @concepts/corpus-overflow-out-of-scope.md.

The authors target a bottleneck in GPTQ, a standard method for post-training quantization of large language models. GPTQ optimizes continuous group scales separately from the choice of discrete integers. JointQ refines the GPTQ result. Each local-search move changes one integer and recomputes that group's optimal scale in closed form, and all scales are re-solved jointly from time to time.

JointQ keeps the GPTQ output format, so it is a drop-in replacement. Across four models and four settings, it improved six-task average zero-shot accuracy over GPTQ in 14 of 16 comparisons and perplexity in 12 of 16. The mean accuracy gain grows from 0.0044 in the W4G128 setting to 0.1559 in W3 per-channel. The authors state the main benefit is downstream accuracy in low-bit and large-group settings. The numbers are single-source claims.

## Snippets

> "JointQ preserves the GPTQ output format and is thus a drop-in replacement." [Source: `arxiv-2611.20384-jointq-joint-scale-and-integer-quantization-for.pdf` p.1 (arXiv 2611.20384), retrieved 2026-11-22]
