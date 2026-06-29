---
title: Poker Arena multi-axis cognitive profile (Raeth)
type: concept
tags: [concept, poker, devfun, evaluation, llm-agents, k122]
keywords: [nine-axis, Raeth, memory ablation, bet sizing, positional awareness, trajectory, dev.fun]
related:
  - sources/arxiv-poker-arena-multi-axis-2606-13815-2026-06-18.md
  - sources/arxiv-equilibrium-efgsas-2606.13093-2026-06-18.md
  - sources/arxiv-veritas-visual-verification-2606.18247-2026-06-18.md
  - concepts/generator-verifier-inference-time-steering.md
  - concepts/devfun-poker-agent-challenge-2026.md
  - concepts/devfun-researcher-pre-submit-recon.md
  - concepts/devfun-researcher-track-readiness-2026-06.md
  - concepts/devfun-researcher-pro-style-targets-2026-06.md
  - entities/platforms/devfun-arena.md
  - concepts/extensive-form-games-stochastic-action-sets.md
  - concepts/multi-agent-fictitious-play-llm.md
  - concepts/red-queen-controlled-utility-evolution.md
  - sources/arxiv-red-queen-godel-machine-2606.26294-2026-06-29.md
  - concepts/team-zero-sum-games-complexity.md
  - sources/arxiv-mafp-fictitious-play-2606.19308-2026-06-20.md
  - sources/arxiv-team-zero-sum-games-2606.16139-2026-06-20.md
  - sources/arxiv-probabilistic-agent-verification-2606.20510-2026-06-21.md
  - sources/arxiv-rng-bench-non-markov-mllm-2606.19338-2026-06-21.md
  - concepts/non-markov-belief-state-benchmarks.md
  - concepts/probabilistic-agent-policy-verification.md
  - concepts/kuhn-poker-sft-curriculum-reference.md
  - concepts/garip-running-average-self-play.md
  - sources/arxiv-garip-self-play-2606.22688-2026-06-23.md
  - concepts/emagnet-parameter-space-ema-self-play.md
  - concepts/self-enforcing-transfer-equilibrium.md
  - concepts/irumai-indian-rummy-rl.md
  - concepts/ipo-finance-agent-benchmark.md
  - sources/arxiv-ipo-finance-agent-2606.23032-2026-06-24.md
maturity: validated
created: 2026-06-18
updated: 2026-06-25
---

## Relations

- @sources/arxiv-poker-arena-multi-axis-2606-13815-2026-06-18.md — Raeth / IIT Roorkee paper
- @concepts/devfun-poker-agent-challenge-2026.md — Cemini Researcher Round optimization target
- @entities/platforms/devfun-arena.md — dev.fun + Raeth benchmark surfaces
- @sources/arxiv-equilibrium-efgsas-2606.13093-2026-06-18.md — CFR/equilibrium theory sibling
- @concepts/multi-agent-fictitious-play-llm.md — fictitious-play equilibrium seeking (K124)
- @concepts/team-zero-sum-games-complexity.md — multi-agent equilibrium hardness (K124)
- @concepts/non-markov-belief-state-benchmarks.md — Memory Gap diagnostic for F6 ablation (K125)
- @concepts/probabilistic-agent-policy-verification.md — trajectory verifier risk bounds (K125)

## Raw Concept

Academic + product benchmark from **Raeth AI** (arXiv 2606.13815) evaluating frozen LLMs in **7-max NLHE tournaments** with a **nine-axis cognitive profile** instead of scalar chip leaderboards. Aligns with dev.fun Researcher Round "how agents play" eval thesis.

## Narrative

### Platform vs dev.fun

| Surface | Raeth Poker Arena | dev.fun Researcher Round |
|---------|-------------------|------------------------|
| Host | Raeth (`poker.raeth.ai`) | dev.fun / BenchFlow sandbox |
| Format | 7-max tournament, 20 hands/session | **6-max** sandbox [TENTATIVE operator] |
| Eval | Nine-axis profile + chips | Trajectory export + multi-axis [CONFIRMED Discord] |
| Memory | 3-layer controlled ablation | Cemini F6 session memory |

Same research lineage (Raeth author on paper; dev.fun PR cites multi-axis eval) but **separate leaderboards** — optimize Cemini for dev.fun sandbox while **stealing axis definitions** from Raeth.

### Three-layer memory (Raeth)

| Layer | Scope | Cemini analog |
|-------|-------|---------------|
| L1 | Within-hand ephemeral context | Hole cards + street history in `decide()` |
| L2 | Session notebook (16K chars, agent-written) | F6 session memory / reasoning log |
| L3 | Cross-session lifetime store | F6+ cross-session [partial] |

**Ablation finding:** memory helps GPT (+114.6 chips/session swing), hurts Kimi (−109.4), neutral for Claude — **model-specific**, not universal. Benchmarks must vary memory interface per model.

### Nine-axis profile

| ID | Axis | Measurement |
|----|------|-------------|
| M₁ | Bet sizing calibration | L₁ distance vs GTO bet-ratio histograms |
| M₂ | Bluffing / deception | Hybrid: low-equity aggression + LLM judge |
| M₃ | Opponent reading | Hybrid: differentiation + 3-judge panel on reads |
| M₄ | Composure | VPIP/AF stability after bad beats (7-hand windows) |
| M₅ | Adaptability | Strategy drift weighted by profit improvement |
| M₆ | Prediction accuracy | Regex on hand-type / equity claims in reasoning |
| M₇ | Strategic mixing | Action entropy vs GTO (≥10 obs buckets) |
| M₈ | Factual accuracy | Card/pot/draw correctness in reasoning |
| M₉ | Positional awareness | Preflop VPIP by position vs GTO Spearman |

**Key result:** Claude **#1 chips** (+$15,730) but **#5 mean axis**; Grok **#1 mean axis**, **#2 chips**. Scalar LB misranks — **cross-axis consistency** beats peak specialty.

### Cemini steal list

1. Map `axis_summary.json` proxies to M₁–M₉ where deterministic (VPIP by seat, bet-size buckets, aggression factor).
2. Export trajectory JSON every Researcher submit — Discord expects full traces.
3. Memory ablation discipline: test F6 **on/off** before publish — don't assume memory always helps.
4. Regression gates on M₈ (no card hallucination) and M₉ (positional VPIP) — Kimi's losses traced to those axes.
5. **Memory Gap (K125):** on trajectory export, tag errors where F6 off caused wrong action vs wrong action with memory on — separates forgetting from mis-decide.

## Snippets

> "Tournament chips and aggregate axis score order the field differently: Claude Opus 4.6 wins … yet ranks only fifth of seven on mean axis score." [Source: arXiv:2606.13815 abstract (retrieved 2026-06-18)]

> "Persistent memory helps some models and hurts others." [Source: arXiv:2606.13815 abstract (retrieved 2026-06-18)]

## Dead Ends

- Raeth 7-max tournament config ≠ confirmed dev.fun Researcher table size — axis definitions portable, seat counts may differ.
- LLM-judged axes (M₂, M₃) not reproducible without judge panel — Cemini uses deterministic proxies only unless dev.fun publishes judge spec.
