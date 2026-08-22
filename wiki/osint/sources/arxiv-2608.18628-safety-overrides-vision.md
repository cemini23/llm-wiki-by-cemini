---
title: When safety overrides vision — VLMs refuse while still seeing
type: source
tags: [vlm, safety, interpretability, image-gen, alignment]
keywords: [refusal-direction, visual-grounding, late-layer-steering, Gupta, Chakraborty, IIT-Delhi]
related:
  - concepts/agent-safety-executable-evaluation.md
  - concepts/inadvertent-context-leakage.md
maturity: draft
created: 2026-08-21
updated: 2026-08-21
read_status: skimmed
---

## Relations
- @concepts/agent-safety-executable-evaluation.md
- @concepts/inadvertent-context-leakage.md

## Raw Concept
- **title:** When Safety Overrides Vision: Exploring Dynamics between Vision Influence and Safety Alignment in Vision-Language Models
- **author:** Mehak Gupta, Tanmoy Chakraborty (Yardi School of AI, IIT Delhi)
- **type:** arXiv paper
- **location:** `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.18628-when-safety-overrides-vision-exploring-dynamics.pdf`
- **retrieved:** 2026-08-21
- **pages:** arXiv HTML (RQ framing, vision-influence, refusal dir, late-layer interventions)
- **read-status:** skimmed

## Narrative
Paired eval: same image + question; only the instruction changes (default vs safety-constrained “abstain if uncertain”). Qwen3-VL-8B, LLaVA-v1.6-Vicuna-7B, Phi-3-Vision on VQAv2 / GQA / POPE. Safety instruction spikes abstention (e.g. Qwen3-VL POPE 0%→56%) on items the model *already answered correctly* under default instruction.

Layer-wise vision-influence (clean vs corrupted-image logit of the first generated token) stays up during abstention — the model still sees. Refusal direction r_ℓ = μ_abstain − μ_answer; safety instruction steers late-layer hidden states toward it. Geometry is architecture-dependent (Qwen separable, Phi entangled) but the causal role is shared: subtracting the refusal direction at late layers restores grounded answers without retraining or changing the image; adding it increases refusal. Hallucination rise is modest vs abstention drop.

OSINT keeps the interpretability steal: **refusal direction vs grounding** — a model can know/see and still refuse to speak. Pointer only to Image-gen wiki (brief). Skip clone; no runtime wire, no activation-steering recipe in this wiki.

Pairs with inadvertent-context-leakage: both are gaps between internal state and expressed text (leakage encodes secrets in benign text; this suppresses answers while vision remains).

## Snippets
> Under safety-constrained instruction, models frequently abstain from answering questions that remain correctly answerable under default instruction despite receiving identical image-question inputs. [Source: https://arxiv.org/abs/2608.18628 (retrieved 2026-08-21)]

> Abstained generations remain consistently influenced by visual evidence throughout decoding … suppressing refusal-related representations reliably restores grounded answering behavior … without retraining or modifying visual inputs. [Source: arxiv-2608.18628-safety-overrides-vision.pdf abstract]

> Safety-aligned VLMs reveal [a] gap between what a model internally understands and what it ultimately expresses: a model may know, see, and yet still refuse to speak. [Source: arxiv-2608.18628-safety-overrides-vision.pdf §1]
