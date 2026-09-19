---
title: Long-Lived Characters, Local Inference — incremental NPC memory (2026-09-19)
type: source
tags: [source, arxiv, npc, llm, local-inference, memory]
keywords: [long-lived-characters, incremental-memory, qwen, kv-cache, local-npc, game-rules]
related:
  - concepts/llm-npc-runtime-ai-shelf.md
  - concepts/agentic-npc-design-guardrails.md
  - concepts/scope-tiers.md
  - sources/inbox-arxiv-reject-batch-2026-09-19.md
  - sources/nvidia-ace-qwen3-on-device-npc-2025.md
  - sources/morganpage-local-npc-dialogue-2026.md
  - sources/ixie-agentic-npc-balance-2026.md
  - entities/projects/castle-sim.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2609.18935
maturity: validated
created: 2026-09-19
updated: 2026-09-19
---

## Raw Concept

**arXiv:2609.18935** — Incremental memory maintenance for **locally deployed** LLM game NPCs. Problem: revising a few memories invalidates a long reusable KV prefix; full replay competes with foreground dialogue and other characters. Wrong fluent dialogue about item ownership or transfer state can corrupt **deterministic game rules**. Runtime on quantized **Qwen hybrid recurrent-attention** model: remove superseded KV entries, compute replacement records at true sequence tail, preserve recurrent state + unchanged KV.

## Narrative

### Problem framing [CONFIRMED]

| Issue | castle-sim relevance (Tier 3+) |
|-------|-------------------------------|
| Prefix invalidation on memory edit | Peasant/lord with 50+ conversation turns cannot full-refill before every bark |
| Multi-character maintenance cost | Kingmaker with 12 AI lords + scripted peasants — serial replay impractical on laptop |
| Dialogue → rules coupling | SH2 economy flags (granary stock, ownership, crime state) must stay **authoritative** over LLM fluency |

Aligns with @concepts/agentic-npc-design-guardrails.md **curated memory** + **hard walls** — this paper adds **inference-state** maintenance, not just text summaries.

### Technical approach [CONFIRMED]

- **True-tail updates** — replacement KV at actual sequence tail vs slot-preserving alternatives
- **Recurrent state preserved** — hybrid RNN-attention; not disposable "latest memory text" encoding
- **Eval** — multi-update dialogue replays, fixed-input placement ablations, attention diagnostics
- **Findings** — independent block composition weakens query-conditioned memory selection; slot-preserving alternatives repeat double-subtraction errors; attention-distribution proximity alone does not explain semantic recovery

### Phase-0 posture [TENTATIVE]

| Check | Result |
|-------|--------|
| License / repo | Paper-only ingest — no pin until public code + SPDX |
| Godot bridge | **None** — research shelf |
| castle-sim v0–v2 | **DEFER** — scripted barks only (@concepts/vertical-slice-v0.md) |
| Verdict | **STEAL-FROM (pattern)** — incremental KV maintenance for local SLM NPCs at Tier 3+ |

### Design steal for castle-sim (Phase E+)

1. **Separate inference state from displayed memory text** — treat character KV/recurrent state as maintained resource
2. **True-tail memory patches** — when quest flag or ownership changes, patch at tail; do not replay full life log
3. **Rules fence** — LLM proposes dialogue; **Godot authoritative** for granary counts, crime flags, lord honour (matches iXie "systems not content")
4. **Regression harness** — scripted maintenance rounds (paper uses 8) before any Tier 3 NPC pilot

### Cross-wiki

- Dev-time harness patterns → @ccc-wiki (validate-before-act, replay gates)
- On-device SLM stack contrast → @sources/nvidia-ace-qwen3-on-device-npc-2025.md (AAA middleware vs hobby local Qwen)

## Snippets

```
Abstract lead: "A game character should not have to reread its entire life before every conversation."
Model family: quantized Qwen hybrid recurrent-attention (local inference)
Key eval: true-tail updates recover full-refill quantity in 3 reconstructions vs slot-preserving double-subtraction error
```

## Dead Ends

- Installing full local Qwen hybrid stack for M0–M2 castle-sim (scope + laptop cost)
- Letting LLM dialogue directly mutate economy/crime state without deterministic validator
- Equating attention-distribution similarity with semantic memory correctness
