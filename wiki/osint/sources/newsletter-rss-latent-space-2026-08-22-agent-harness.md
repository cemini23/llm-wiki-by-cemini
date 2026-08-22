---
title: "Latent Space — The Evolution of the Agent Harness (attention-interface)"
type: source
tags: [newsletter, latent-space, harness, ccc, k245]
keywords: [harness, Harness-Bench, attention-interface, Claude-Code, compaction]
related:
  - concepts/harness-optimization-bench.md
maturity: draft
created: 2026-08-22
updated: 2026-08-22
read_status: read
---

## Relations

- @concepts/harness-optimization-bench.md — Harness-Bench 23.8-pt spread; absorb→shed loop; attention-interface leftover

## Raw Concept

- **title:** The Evolution of the Agent Harness
- **author:** Latent Space
- **type:** Substack essay
- **location:** `cemini-egress-fi:/opt/cemini-bulk/research/osint/newsletter-rss-latent-space-2026-08-22-the-evolution-of-the-agent-harness.md`
- **retrieved:** 2026-08-22
- **read-status:** read
- **sha256:** `9e44ea3399069b8965b3fd91e7060cf4aeea0dd2bc1ac01ef49b9509a1c85662`
- **URL:** https://www.latent.space/p/attention-interface

## Narrative

Thesis: Christmas 2025 agents “started to work” because the **model curve and the harness curve crossed**, not because of a single weight jump. Lukasz Kaiser: harness + a little post-training + new pretrained models — hard to pin down. The next loop is train → absorb into weights → shed scaffold → repeat. Thariq Shihipar: Claude Code recently **deleted 80%** of the system prompt.

**Harness 1.0 (bolt-on):** ReAct on paper (Oct 2022) → AutoGPT/BabyAGI premature autonomy (loop amplifies error; 95%^20 ≈ 36%) → Cursor/Copilot retreat to HITL → o1 overhang late 2024 → Claude Code (Feb 2025) seizes the crossover (bash + files + permission rules; ~$1B ARR in six months).

**Harness 2.0 (co-training):** Harness-Bench, same model / 106 tasks / different harnesses: **52.4 to 76.2 (23.8-pt spread)**. OpenAI ARC-AGI-3: retained reasoning + compaction tripled GPT-5.6 Sol **13.3% → 38.3%**. RL now runs *inside* the harness (codex-1). GPT-5.1-Codex-Max: first model natively trained across multiple context windows via compaction.

**Harness 3.0 (attention-interface):** After the model absorbs tool-use, memory, even multi-agent orchestration, what remains is permissions, identity, trust, legibility — the interface to **scarce human attention**. Prediction: every agentic company ships a human-attention policy surface the way they shipped `AGENTS.md`. New gap = what the agent asks of the human vs what the human can answer.

CCC steal: measure harness spread on the same model; prefer deletion of absorbed scaffold; **do not** swap `/route`. Phase-1 leftover (propose only): an attention-policy surface (when to interrupt, which decisions need approval) — do not edit `.cursor/skills` this session.

## Snippets

> An agent harness is everything besides the model weights that makes the agent work. [Source: https://www.latent.space/p/attention-interface (retrieved 2026-08-22)]

> Harness-Bench ran the same model over the same 106 tasks in different harnesses, and scores ranged from 52.4 to 76.2: a 23.8-point spread with zero change to the model. [Source: https://www.latent.space/p/attention-interface (retrieved 2026-08-22)]

> I predict that within a year, every company building agentic AI will ship a human attention policy surface in the way that every agentic AI company shipped AGENTS.md. [Source: https://www.latent.space/p/attention-interface (retrieved 2026-08-22)]
