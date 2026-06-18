---
title: arXiv 2606.13815 — Poker Arena multi-axis evaluation (Raeth)
type: source
tags: [source, arxiv, poker, devfun, evaluation, k122]
keywords: [multi-axis, trajectory, memory ablation, Raeth, poker arena, nine-axis]
related:
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/devfun-poker-agent-challenge-2026.md
  - entities/platforms/devfun-arena.md
  - sources/devfun-poker-agent-challenge-onepager-2026-06-18.md
  - sources/devfun-researcher-track-discord-welcome-2026-06-18.md
maturity: validated
read_status: deep-read
created: 2026-06-18
updated: 2026-06-18
clusters: [prediction-markets, llm-agents]
---

## Relations

- @concepts/poker-arena-multi-axis-cognitive-profile.md — K122 nine-axis synthesis
- @concepts/devfun-poker-agent-challenge-2026.md — Cemini Researcher Round target
- @entities/platforms/devfun-arena.md
- @sources/devfun-poker-agent-challenge-onepager-2026-06-18.md
- @sources/devfun-researcher-track-discord-welcome-2026-06-18.md

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Poker Arena: Multi-Axis Profiling of Strategic Reasoning and Memory in LLMs |
| **Authors** | Pratham Singla, Shivank Garg (IIT Roorkee); Vihan Singh (Raeth AI) |
| **arXiv** | 2606.13815 (Jun 2026) |
| **sha256** | `aec0c504a655e5fd07943f2c84a5429b959a7ee381b81ea8429c93f9600e8822` |
| **Product** | https://poker.raeth.ai/ · https://www.raeth.ai/benchmarks |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.13815-poker-arena-multi-axis-profiling-of-strategic-re.pdf` |
| **Retrieved** | 2026-06-18 |
| **Read status** | deep-read (abstract, §2–4, Table 1–2, ablation) |

## Narrative

Raeth **Poker Arena** evaluates **seven frontier LLMs** in **50 seven-player NLHE tournaments** (20 hands/session, 1,000 hands total, 9,115 actions). Combines deterministic engine (side pots, MC equity, escalating blinds) with **three-layer memory** and **nine-axis cognitive profile**.

**Headline misrank:** Claude Opus 4.6 **#1 chips** (+$15,730, 14 firsts) but **#5 mean axis** (0.5754); Grok **#1 mean axis** (0.6137), **#2 chips**. Spearman ρ=+0.571 (p=0.18, n=7) — rankings correlate weakly.

**Memory ablation (600 hands):** seeding prior session into L2 helps GPT (+114.6/session), hurts Kimi (−109.4), slightly hurts Claude (−42.5) — none p<0.05 at n=10 but directions stable.

**Engine details:** $1,000 start stacks; blinds escalate every 5 hands ($5/$10 → $50/$100); anonymized opponent aliases in L1; L2 16K char agent-written notebook with conditional UPDATE gate.

**Cemini posture:** **Steal axis definitions + memory ablation discipline** for dev.fun Researcher Round (`@concepts/devfun-poker-agent-challenge-2026.md`). Raeth platform is parallel benchmark, not submission target.

## Snippets

> "Scalar leaderboards misrank competence and that memory effects are model-dependent." [Source: arXiv:2606.13815 §5 Conclusion (retrieved 2026-06-18)]

> "Claude is the only model that pairs above-median VPIP (28.6%) with above-median AF (2.46)." [Source: arXiv:2606.13815 §4.2 (retrieved 2026-06-18)]

> "Layer 2 is a session-scoped memory … written and maintained by the agent itself … maximum size of 16K characters." [Source: arXiv:2606.13815 §2.2 (retrieved 2026-06-18)]

## Dead Ends

- Paper panel = 7-max; dev.fun Researcher assumed 6-max — seat geometry differs.
- Judge-scored axes (M₂ bluffing, M₃ opponent reading) require non-contestant LLM panels — not replicated in Cemini CI without API budget.
