---
title: "What Breaks Under Pruning in Smart Homes (arXiv:2609.17515)"
type: source
tags: [arxiv, source, k263, ccc]
keywords: [k263, pruning, MoE, smart-home, tool-calling]
related:
  - concepts/k263-ccc-harness-wave.md
maturity: draft
created: 2026-09-17
updated: 2026-09-17
read_status: skimmed
---

## Relations

- @concepts/k263-ccc-harness-wave.md

## Raw Concept

| File | `arxiv-2609.17515-what-breaks-under-pruning-in-smart-homes-and-whe.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.17515-what-breaks-under-pruning-in-smart-homes-and-whe.pdf` |
| Retrieved | 2026-09-17 |
| Dual-ID | **OSINT K263** |
| sha256 | `0962fa0c038652d2320aad87f57e3bdae7468d70250110146233110f43471a91` |

## Narrative

Four LLMs; 19.5k instances. MoE tolerates more pruning than dense. Grounded specificity dies before schema intent. Aggressive dense prune → over-refusal. CCC FILE. Tool-calling reliability, not product Integrate.

## Snippets

> Dense models have narrow safe pruning regions followed by sharp degradation, while MoE models tolerate substantially more pruning. Pruning degrades grounded specificity before schema-level intent. [Source: arxiv-2609.17515-what-breaks-under-pruning-in-smart-homes-and-whe.pdf]
