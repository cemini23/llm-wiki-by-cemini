---
title: Non-Markov belief-state benchmarks (RNG-Bench pattern)
type: concept
tags: [concept, benchmark, memory, mllm, k125]
keywords: [RNG-Bench, Memory Gap, non-Markov, belief state, hidden state, Matching Pairs]
related:
  - sources/arxiv-rng-bench-non-markov-mllm-2606.19338-2026-06-21.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/agentic-navigation-memory-strategy.md
  - sources/arxiv-qwen-robotnav-2606.18112-2026-06-20.md
  - concepts/generator-verifier-inference-time-steering.md
  - concepts/devfun-poker-agent-challenge-2026.md
  - concepts/llm-agent-systems.md
maturity: draft
created: 2026-06-21
updated: 2026-06-21
---

## Relations

- @sources/arxiv-rng-bench-non-markov-mllm-2606.19338-2026-06-21.md — RNG-Bench paper (K125)
- @concepts/poker-arena-multi-axis-cognitive-profile.md — Raeth memory ablation + F6 session store
- @concepts/agentic-navigation-memory-strategy.md — spatial hidden-state (K124 RobotNav)

## Raw Concept

K125 ingest of arXiv **2606.19338**. Benchmark design pattern for **closed-loop** agents where the visible observation is **insufficient** — models must reconstruct hidden state from history. **Memory Gap** decomposes failure into **forgetting** vs **wrong action given correct belief**.

## Narrative

### RNG-Bench harness axes

| Axis | Role |
|------|------|
| Scale | Latent state size (board / maze grid) |
| Pattern | Visual distractors |
| Modality | Text vs 2D vs 3D egocentric views |

**Matching Pairs** — card identities briefly shown, later matched from memory. **3D Maze** — integrate egocentric views into traversable map. **Duel protocol** — paired instances control variance.

### Memory Gap diagnostic

Compare agent score vs **oracle-with-perfect-memory** policy on same instance. Gap ≈ forgetting; remainder ≈ decision error given belief. Paper reports most frontier MLLM error is **gap-dominated**.

### Cemini mappings [TENTATIVE]

| Domain | Non-Markov trigger | Memory Gap analog |
|--------|-------------------|-------------------|
| Poker HU/6-max | Opponent line from two streets ago; session notes | Export trajectory → tag spots where F6 memory off caused wrong action vs where action wrong despite memory |
| Castle-sim playtest | Fog-of-war resource locations after camera pan | Stagehand replay: compare peasant path with/without minimap scratchpad |
| Verifier stack (K123/K125) | Belief about villain range | Verifier accepts action but **range state** stale → gap in exploitability bound |

**Posture:** REFERENCE rubric — do not install RNG-Bench MLLM weights on Researcher track (no runtime LLM).

## Snippets

> "Existing benchmarks … test recall only after an episode has ended." [Source: arXiv:2606.19338 abstract (retrieved 2026-06-21)]

## Dead Ends

- Long-context text benchmarks (LongBench) — recall without closed-loop causal observation chain.
- Raeth chip leaderboard — scalar outcome hides forgetting vs mis-play decomposition.
