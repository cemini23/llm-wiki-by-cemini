---
title: "Revisiting over-refusal in safety-aligned LLMs"
type: source
tags: [source, arxiv, over-refusal, safety-alignment, representation]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Revisiting Over-refusal in Safety-aligned Large Language Models: A Representation and Optimization Perspective |
| Authors | Chao Chen et al., Hefei University of Technology (Pengyang Shao and Fei Shen, National University of Singapore) |
| arXiv | 2610.39802 |
| File | `arxiv-2610.39802-revisiting-over-refusal-in-safety-aligned-large.pdf` |
| Retrieved | 2026-11-01 |
| URL | https://arxiv.org/abs/2610.39802 |
| Read status | skimmed (abstract + intro) |

## Narrative

Over-refusal is a side effect of safety alignment in large language models. The model rejects harmless queries that look risky on the surface. The authors say existing mitigation methods can work. They also say the field still does not explain why a safety-aligned model rejects harmless queries when the safety supervision is correct.

The paper studies over-refusal through representation and optimization. It uses three sample types. Harmful samples are unsafe queries that the model must refuse. Benign samples are clearly harmless queries. Over-refusal samples are harmless queries that the model is likely to reject by mistake.

The authors report two observations. Representations of harmful samples and over-refusal samples look separable at some intermediate layers, then overlap more in deeper layers. Harmful-sample gradients show high similarity inside the class and sit in a low-rank subspace. Those gradients align more strongly with refusal-target gradients than with the correct helpful-target gradients on over-refusal prompts. The authors say this imbalanced gradient coupling can push over-refusal samples toward refusal. They also say the weaker separation in deeper layers can make a clear boundary harder to keep.

The method is GOAL (Gradient Orthogonalization with contrAstive Learning). It is a safety-alignment framework with two parts. The first part orthogonalizes over-refusal gradients against the low-rank refusal subspace taken from harmful gradients. The aim is to stop imbalanced gradient coupling from biasing over-refusal optimization toward refusal. The second part adds a contrastive learning objective so harmful representations and over-refusal representations separate more clearly.

The abstract says experiments on multiple models and benchmarks show that GOAL mitigates over-refusal and preserves safety performance and general capabilities. The supplied abstract states no measured scores. That effectiveness claim is single-source. The text points to code at an anonymous repository. The introduction names two earlier lines: DCR reshapes the refusal boundary before safety alignment, and SCANS steers safety-critical layer activations. For a defensive security and AI-safety reader, the paper is about the refusal boundary. The model must still refuse harmful queries, and it should answer harmless queries that only look risky.

## Snippets

> "Over-refusal is a critical side effect of safety alignment in large language models (LLMs), causing harmless but superficially risky queries to be mistakenly rejected. Despite the effectiveness of existing mitigation methods, why safety-aligned LLMs may still reject harmless queries under correct safety supervision remains insufficiently understood." [Source: `arxiv-2610.39802-revisiting-over-refusal-in-safety-aligned-large.pdf` p.1 (arXiv 2610.39802), retrieved 2026-11-01]
