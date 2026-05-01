---
title: "DiffMAS: Learning to Communicate — Differentiable Multi-Agent Systems via KV-Cache Latent Communication"
type: source
tags: [multi-agent-systems, differentiable-communication, KV-cache, LoRA, agent-training, reasoning]
keywords: [DiffMAS, KV-cache communication, latent communication, differentiable agents, multi-agent training, LoRA fine-tuning, AIME24, GPQA]
clusters: [llm-agents]
related: []
maturity: validated
read_status: deep-read
created: 2026-04-30
updated: 2026-04-30
---

## Relations
- @concepts/llm-agent-systems.md — corpus hub; DiffMAS adds the "learnable communication" dimension to the agent-design taxonomy

## Raw Concept
- Original title: Learning to Communicate: Differentiable Multi-Agent Systems via KV-Cache Latent Communication (DiffMAS)
- Type: arXiv preprint (arXiv:2604.21794)
- Retrieved: 2026-04-30 (Tier-2 sweep, via Exa crawling)
- Read status: deep-read (abstract + §1-3 via Exa)

## Narrative

DiffMAS addresses a fundamental limitation in current multi-agent LLM systems: communication happens through discrete natural-language messages, which creates optimization boundaries between agents. The internal representations used during reasoning are continuous, but inter-agent exchange forces them through a discrete bottleneck. DiffMAS makes communication **learnable** by treating KV-caches as a differentiable latent communication channel.

**Architecture — Two-stage training**:

**Stage I (KV Trace Construction)**: Agents 1 through K−1 sequentially construct a shared KV trace. Each agent prefillls the existing cache and appends newly generated KV segments. No gradient updates occur in this stage — the focus is on building the latent communication medium.

**Stage II (Differentiable Decoding)**: The final agent performs autoregressive decoding on the prefilled KV cache. Cross-attention over the accumulated KV trace produces hidden states, which are projected through the LM head to generate tokens. Supervised fine-tuning is applied via cross-entropy loss. **Gradients backpropagate only through LoRA parameters of the final agent** — the backbone model remains frozen. [Source: arXiv:2604.21794 §1, Fig.1]

**Results**:
- AIME24: **+26.7%** over baselines
- GPQA-Diamond: **+20.2%**
- Consistent gains across mathematical reasoning, scientific QA, code generation, and commonsense benchmarks
- Outperforms: single-agent inference, text-based multi-agent systems, and prior latent communication methods
- Parameter-efficient: only LoRA parameters trained, backbone frozen [Source: arXiv:2604.21794 Abstract]

**Why this matters**: Current multi-agent systems (including Cemini's planned orchestrator) are modular compositions of individually-optimized components. DiffMAS shows that the interactions *between* agents can themselves be optimized through learning. The KV-cache-as-communication-channel pattern is architecture-agnostic — any transformer-based agent pipeline can adopt it.

**Relevance to Cemini**: The differentiable communication paradigm maps to Cemini's multi-agent trading pipeline (analyst → researcher → trader → risk manager chains from TradingAgents). If Cemini's analyst-team outputs (structured reports) were transmitted as KV-cache traces rather than discrete text, downstream agents could learn to attend to the most relevant latent features. The LoRA-only training constraint fits Cemini's API-only deployment (no full-model fine-tuning). The +26.7% gain on AIME24 suggests the communication bottleneck is real and large.

## Snippets

"Discrete message passing creates optimization boundaries between agents. This limitation is particularly restrictive as the performance of the system depends critically on how well intermediate reasoning results are preserved and interpreted across agents." [Source: arXiv:2604.21794 §1]

"KV caches provide a natural mechanism for enabling differentiable communication. As continuous internal representations produced by transformer attention layers, KV states can be directly reused by downstream agents without requiring discrete decoding or re-encoding." [Source: arXiv:2604.21794 §1]

"DiffMAS consistently improves reasoning accuracy and decoding stability over single-agent inference, text-based multi-agent systems, and prior latent communication methods, achieving +26.7% on AIME24, +20.2% on GPQA-Diamond." [Source: arXiv:2604.21794 Abstract]
