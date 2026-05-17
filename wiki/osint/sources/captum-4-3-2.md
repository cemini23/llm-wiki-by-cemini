---
title: Using Captum to Explain Generative Language Models Vivek Miglani*, Aobo Yang*, Aram H. Markosyan, Diego Garcia-Olano, Narine Kokhlikyan Meta AI
type: source
tags: [pdf, k49, llm-agents]
clusters: [llm-agents]
related:
  - concepts/llm-agent-systems.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-05-17
---

## Relations

- @concepts/llm-agent-systems.md — cluster hub for LLM agent-systems research in the Cemini corpus

## Raw Concept

- **Original title**: Using Captum to Explain Generative Language Models
- **Author(s)**: Vivek Miglani*, Aobo Yang*, Aram H. Markosyan, Diego Garcia-Olano, Narine Kokhlikyan (Meta AI; *equal contribution) — arXiv:2312.05491v1
- **Type**: PDF
- **Location**: research for cemini/Captum 4:3 2.pdf
- **Retrieved**: 2026-04-23 (filename date reflects download date, not publication)
- **Length**: 9p
- **Read status**: deep-read
- **Primary cluster**: llm-agents
- **All clusters**: llm-agents

## Narrative

This Meta AI paper introduces explainability features added in **Captum v0.7** — the open-source PyTorch interpretability library — specifically designed for **generative language models** such as GPT-3-scale LLMs. The motivation: as LLMs spread into critical domains (healthcare, law), it is insufficient to accept a black-box prediction; tooling must help explain *why* a model produced a given output.

The paper surveys the attribution (feature-importance) methods Captum exposes and how they generalize to text generation. An attribution method maps a function and input to a per-feature contribution score, often relative to a **baseline/reference input**. Two families are covered: **perturbation-based methods** — Feature Ablation (substitute each feature with its baseline and measure output change), **Shapley Value Sampling** (game-theoretic, fair-credit allocation estimated via sampled feature permutations), **LIME**, and **KernelSHAP** — which need only black-box access; and **gradient-based methods** — Integrated Gradients, DeepLift, Saliency, and others — which require model weights/gradients. The new generative-model functionality lets practitioners attribute a generated token (or sequence) back to specific input tokens or prompt segments, treating tokens or token groups as the interpretable features and supporting configurable baselines, so users can surface learned associations and spurious dependencies inside generative LLMs.

**Cemini relevance**: a concrete, production-grade toolkit for LLM interpretability/explainability — useful for auditing why an agent or routing model produced a given decision, debugging prompt sensitivity, and adding traceability to model-driven steps in the conductor pipeline.

## Snippets

> "Captum is an open-source model explainability library for PyTorch providing a variety of generic interpretability methods proposed in recent literature such as Integrated Gradients, LIME, DeepLift, TracIn, TCAV and more." [Source: Captum 4:3 2.pdf p.1]

> "These methods can be categorized broadly into (i) perturbation-based methods, which utilize repeated evaluations of a black-box model on perturbed inputs to estimate attribution scores, and (ii) gradient-based methods, which utilize backpropagated gradient information to estimate attribution scores." [Source: Captum 4:3 2.pdf p.1]
