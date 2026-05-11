---
title: "TokenSpeed — GPU LLM Inference Engine"
type: entity
tags: [tool, llm-inference, gpu-bound, reject, k38]
keywords: [tokenspeed, reject, three-surface-eval]
related:
  - sources/link-evaluation-brief-trading-stack.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/link-evaluation-brief-trading-stack.md` — source evaluation brief (URL 5)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `github.com/lightseekorg/tokenspeed`
- **Tier (per source brief)**: **Reject**
- **License**: License irrelevant given hardware veto

## Narrative

Ultra-high-performance LLM inference engine. Local-SPMD modeling + C++ control plane + MLA. NVIDIA-datacenter-class hardware. TensorRT-LLM competitor.

### Integration vector

**Reject** — Cemini Hetzner stack is CPU-only; GPU-native inference engine is hardware-impossible. Beyond hardware, requires `--ipc=host --network=host --pid=host --privileged` Docker flags = catastrophic isolation violation.

### Risks

Hardware impossibility + privileged container requirement violates secure multi-tenant principles.

[Source: Link Evaluation Brief Trading Stack.docx, URL 5]
