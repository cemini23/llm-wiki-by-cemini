---
title: "LLMs-from-scratch (Sebastian Raschka)"
type: entity
tags: [tool, educational, llm-fundamentals, pytorch, reference-only, k37]
keywords: [llms, from, scratch, rasbt, reference-only, three-surface-eval]
related:
  - sources/evaluating-urls-system-integration.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/evaluating-urls-system-integration.md` — source evaluation brief (URL 17)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `github.com/rasbt/LLMs-from-scratch`
- **Tier (per source brief)**: **Reference-only**
- **License**: Apache-2.0 (typical for Raschka's repos; verify)

## Narrative

Companion codebase to Build a Large Language Model (From Scratch). Step-by-step coding, pretraining, fine-tuning of a GPT-style autoregressive model using pure PyTorch tensors. Avoids heavy abstractions.

### Integration vector

Reference-only — pedagogical codebase, not deployable. Mandatory deep reading for engineers architecting Cemini's LLM-driven pipelines (tensor mechanics + evaluation benchmark patterns).

### Risks

Multi-epoch training scripts require high-VRAM CUDA/MPS — laptop execution triggers thermal throttling.

[Source: Evaluating Urls System Integration.docx, URL 17]
