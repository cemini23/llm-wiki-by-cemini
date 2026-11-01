---
title: "When visual evidence is insufficient: what shapes MLLM refusal"
type: source
tags: [source, arxiv, multimodal-refusal, post-training, activation-intervention]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | When Visual Evidence Is Insufficient: How Instructions, Post-Training, and Internal Activations Shape Refusal in Multimodal Language Models |
| Authors | Ananth K Suresh et al., Indian Institute of Technology Hyderabad |
| arXiv | 2610.37430 |
| File | `arxiv-2610.37430-when-visual-evidence-is-insufficient-how-instruc.pdf` |
| Retrieved | 2026-11-01 |
| URL | https://arxiv.org/abs/2610.37430 |
| Read status | skimmed (abstract + intro) |

## Narrative

Multimodal large language models (MLLMs) should recognize when an image gives insufficient evidence for a question. They should withhold an unsupported answer. The paper says refusal alone does not show that recognition. A model may refuse because of unrelated safety constraints. A model may also refuse without identifying the missing evidence.

The authors study refusal on visually unanswerable questions. They test three controls: inference-time instructions, post-training, and internal activation interventions. The study uses three MLLMs on the MoHoBench benchmark. The authors change the meaning and the placement of refusal instructions. They compare supervised post-training with preference-based post-training. They intervene on a refusal-related activation direction. They derive that direction from naturally answered examples and refused examples.

The abstract states no numeric rates. These comparisons are single-source claims from this abstract. Refusal is highly sensitive to the meaning and the placement of instructions. Sample-level changes differ by model. Aggregate refusal rates hide those changes. Evidence-aware refusal instructions and general refusal instructions have stronger effects than an intentionally mismatched safety instruction. Post-training produces larger increases in refusal. Post-training can also induce responses that combine refusal language with attempted answers. Activation intervention produces smaller changes. Those changes transfer across prompt conditions. The authors report no evidence of indiscriminate refusal on the visually answerable samples they tested.

A defensive security and AI-safety reader can treat a refusal string as a behavior, not as proof of evidence recognition. Instruction meaning and instruction placement can change which samples a model refuses. Post-training can raise refusal and still leave an attempted answer in the same response. Activation intervention changes refusal less in this study, and the change holds across prompt conditions. The paper says refusal is jointly shaped by external instructions, post-training, and internal representations. It calls for work that separates evidence recognition from a learned propensity to refuse.

## Snippets

> "For reliable deployment, multimodal large language models (MLLMs) should recognize when an image provides insufficient evidence to answer a question and withhold unsupported answers. Yet refusal alone is not necessarily evidence of such recognition: models may refuse because of unrelated safety constraints or without identifying the missing evidence." [Source: `arxiv-2610.37430-when-visual-evidence-is-insufficient-how-instruc.pdf` p.1 (arXiv 2610.37430), retrieved 2026-11-01]
