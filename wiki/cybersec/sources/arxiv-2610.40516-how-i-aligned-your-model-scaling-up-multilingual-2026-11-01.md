---
title: "Template Pipeline for Multilingual LLM Safety Data"
type: source
tags: [source, arxiv, multilingual-safety, llm-alignment, safety-data]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | How I Aligned Your Model: Scaling Up Multilingual Safety Training with Templates |
| Authors | Max Neuwinger et al., ETH Zurich |
| arXiv | 2610.40516 |
| File | `arxiv-2610.40516-how-i-aligned-your-model-scaling-up-multilingual.pdf` |
| Retrieved | 2026-11-01 |
| URL | https://arxiv.org/abs/2610.40516 |
| Read status | skimmed (abstract + intro) |

## Narrative

Safety alignment for large language models focuses on English. The abstract says this focus gives limited multilingual coverage and harms low-resource language performance. Open training datasets are often small. Many of them do not cover region-local harmful topics.

The authors propose a template pipeline. The pipeline extracts safe templates from harmful prompts. It translates the templates. It fills the slots with culturally authentic entities. Those entities are harmful or benign. The output is large multilingual refusal corpora and benign corpora.

The authors release MSAFETEMP. The abstract calls it a validated corpus for multilingual safety alignment and evaluation. Single source: this abstract states that the corpus spans 60 languages. The abstract gives no other counts, success rates, or score deltas.

The abstract says English-only evaluation misjudges multilingual safety. For several models, attacks that fail in English succeed after translation. Culturally local variants expose further failures that translation alone misses. The abstract also says template augmentation raises diversity and alignment quality, and that safety performance improves beyond English.

The introduction says red-teaming is much more effective in non-English languages than in English, and that open multilingual safety data remains scarce. It says an English prompt that a model refuses can draw a compliant answer after translation and a culture-local rewrite, while the harmful intent stays the same. It lists four collection blocks: native-speaker cost, thin low-resource red-team coverage, translation that lacks local context, and generator refusals that block synthetic harmful text. It says users of low-resource languages are the least protected, and that those languages open an easy attack path. The preprint aims the corpus and the pipeline at research on safer models for less-represented cultures.

## Snippets

> "Using the dataset, we show that English-only evaluation misjudges multilingual safety: for several models, attacks that fail in English succeed once translated, while culturally localized variants expose further failures that translation alone misses." [Source: `arxiv-2610.40516-how-i-aligned-your-model-scaling-up-multilingual.pdf` p.1 (arXiv 2610.40516), retrieved 2026-11-01]
