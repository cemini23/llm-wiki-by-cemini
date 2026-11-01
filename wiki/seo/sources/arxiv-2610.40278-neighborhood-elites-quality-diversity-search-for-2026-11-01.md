---
title: "Neighborhood Elites: quality-diversity search for QA uncertainty"
type: source
tags: [source, arxiv, uncertainty-quantification, quality-diversity, question-answering]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Neighborhood Elites: Quality-Diversity Search for Uncertainty Quantification in Question Answering |
| Authors | Mesut Ceylan et al., ETH Zurich (Elgar Fleisch also University of St.Gallen) |
| arXiv | 2610.40278 |
| File | `arxiv-2610.40278-neighborhood-elites-quality-diversity-search-for.pdf` |
| Retrieved | 2026-11-01 |
| URL | https://arxiv.org/abs/2610.40278 |
| Read status | skimmed (abstract + intro) |

## Narrative

Large language models produce wrong answers that look the same as correct answers. In question answering, that error moves into later tasks with no notice. Perturbation-based uncertainty quantification probes the model on a set of input rewrites. It reads uncertainty from how much the predictions change.

Usual rewrite sets come from free paraphrasing, token-level perturbation, or adversarial search. Those rewrites leave two things uncontrolled. The first is the kind of change made to the context. The second is how explicitly the context supports the answer. When neither is controlled, the generator sets the mix, and the estimate inherits that mix.

Quality-diversity search is built to cover a predefined exploration space. The authors recast input perturbation as a quality-diversity problem. They propose neighborhood elites, a neighborhood constructor. Neighborhood elites spreads answer-preserving rewrites across two axes: the kind of edit, and the explicitness of support.

The paper compares neighborhood elites with three other neighborhood constructors. It holds the editor, the question-answering model, the uncertainty measure, and the search objective fixed. It also compares neighborhood elites with three scores read from the original context. The test uses five extractive question-answering datasets and five instruction-tuned large language models.

The paper reports that neighborhood elites improves failure detection against every other constructor in at least 24 of the 25 dataset-model pairs. It reports that neighborhood elites reaches 0.726 AUROC and 0.211 AUPRC lift over the base rate. It also reports a gain over semantic entropy computed over decoder samples, of 0.074 AUROC and 0.062 AUPRC lift, and that this advantage widens as the neighborhood grows. Each of these numbers is a single-source claim from this preprint.

A local-SEO and digital-marketing practitioner who reuses a model answer in a later asset faces the risk the abstract names: a wrong answer can pass downstream unnoticed. Neighborhood elites is the paper's reported constructor for detecting that failure on extractive question answering. The reported test covers those five datasets and five models.

## Snippets

> "Large language models (LLMs) are increasingly capable, yet they produce wrong answers indistinguishable from correct ones. In question answering (QA), such an error propagates unnoticed into downstream tasks." [Source: `arxiv-2610.40278-neighborhood-elites-quality-diversity-search-for.pdf` p.1 (arXiv 2610.40278), retrieved 2026-11-01]
