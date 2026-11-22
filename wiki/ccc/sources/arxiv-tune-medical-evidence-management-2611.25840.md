---
title: "TUNE — medical VLM agents and evidence management after tool use"
type: source
related:
  - concepts/evidence-management-tool-use.md
  - concepts/harness-attribution-multimodal-eval.md
  - concepts/lossless-visual-memory-harness.md
updated: 2026-11-22
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Harnessing Medical Visual-Language Models with Agentic Evidence Management |
| Author | Huang Qiming, Hanze Dong, Jipeng Zhang et al. (NUS, Microsoft) |
| Type | arXiv paper (cs.CV), 2611.25840 |
| Location | `research to be indexed/ccc/arxiv-2611.25840-harnessing-medical-visual-language-models-with-a.pdf` |
| Retrieved | 2026-11-22 |
| Pages | 22 |
| Read status | read |

## Narrative

The paper asks a question that generalises past medicine: once a tool returns the right evidence, does the agent use it well? Most work on tool-augmented medical agents stops at mask acquisition. This work builds a benchmark that separates evidence **use** from segmentation **quality**.

**Mask-Evidence MedVQA** has 2.5K examples across four image types. Each question has an answer-relevant ground-truth mask and several renderings of that mask. Two findings follow:

- **Presentation matters.** Different renderings of the same fixed mask change model behaviour.
- **Masks trade off.** Highlighting a region can expose evidence the model missed, and can also induce wrong associations. A ground-truth mask can correct some answers and break initially correct ones.

The authors then introduce **TUNE** (Tool Use is Not Enough), an evidence-management harness. It decides what evidence to acquire, how to present it, and whether to accept the answer update. Full TUNE beats direct tool use by 9.1 points on average across seven benchmarks, and lifts a fine-tuned Qwen3.5-9B backbone by 4.0 points.

The transferable rule: a harness must manage evidence after acquisition, not only acquire it. This applies to any tool that returns an artifact — a grep result, a search snippet, a diff. Presentation and an accept/ reject decision belong in the harness. [TENTATIVE] single source.

## Snippets

> "Acquiring the right mask is not enough; an agent must also decide how to present the evidence and whether it should change the answer." [Source: arxiv-2611.25840-harnessing-medical-visual-language-models-with-a.pdf p.1]

> "Full TUNE improves over direct tool use by 9.1 points on average across seven benchmarks." [Source: arxiv-2611.25840-harnessing-medical-visual-language-models-with-a.pdf p.1]
