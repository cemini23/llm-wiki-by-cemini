---
title: "GARIP — running-average reference for zero-sum self-play (arXiv 2606.22688)"
type: source
tags: [source, arxiv, game-theory, self-play, poker, marl, k127]
keywords: [2606.22688, GARIP, running average, last-iterate convergence, DeepNash, R-NaD, MMD, magnet policy, exploitability]
related:
  - concepts/garip-running-average-self-play.md
  - concepts/multi-agent-fictitious-play-llm.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/devfun-poker-agent-challenge-2026.md
  - sources/arxiv-mafp-fictitious-play-2606.19308-2026-06-20.md
  - sources/arxiv-agentic-time-machine-2606.21013-2026-06-23.md
  - concepts/emagnet-parameter-space-ema-self-play.md
  - sources/arxiv-emagnet-parameter-space-ema-2606.23995-2026-06-25.md
  - sources/arxiv-irumai-indian-rummy-ppo-2606.21975-2026-06-25.md
maturity: draft
read_status: read
created: 2026-06-23
updated: 2026-10-25
clusters: [rl-marl, llm-agents]
---

## Relations

- @concepts/garip-running-average-self-play.md — K127 synthesis
- @concepts/multi-agent-fictitious-play-llm.md — complementary equilibrium-learning cluster (MAFP vs gradient self-play)
- @concepts/poker-arena-multi-axis-cognitive-profile.md — exploitability axis target

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | GARIP: A Running-Average Moving Reference for Last-Iterate Self-Play in Two-Player Zero-Sum Games |
| **Authors** | Can Savcı (Independent Researcher, İzmir) |
| **arXiv** | 2606.22688 (Jun 2026) |
| **sha256** | `731040ae03e1fa01d2667eb91b5707d9c88c9a205acb0255e11af5b80ef0c9fc` |
| **Repo** | none public at ingest |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.22688-pdf-garip-a-running-average-moving-reference-for.pdf` |
| **Retrieved** | 2026-06-23 (inbox) |
| **Read status** | read (abstract + method ablation grid) |

## Narrative

Naive gradient ascent self-play in two-player zero-sum games **cycles** — last iterate orbits equilibrium. Modern fixes regularize toward a **reference policy**:

| Method | Reference | Limitation |
|--------|-----------|------------|
| MMD | Fixed distribution | Converges to **regularized** equilibrium only |
| R-NaD (DeepNash) | Periodic snapshot | Peak lag from stale snapshot |
| **GARIP** | **Running average (Polyak magnet)** | Minimizes peak lag among causal convex averages |

**Central mechanism:** collapse tracks **peak lag** of the reference; running average (flat profile, peak = mean) uniquely minimizes peak lag vs snapshot magnets.

**Deep-RL form:** PPO self-play + λ KL(πθ ∥ π_mag) where π_mag is running-average policy; opponent is average opponent. 2×2 ablation (opponent × magnet) at λ=0.5, K=200, ρ=10⁻², 10 seeds — GARIP (avg+moving) reports lowest exploit return among grid [TENTATIVE — paper table truncated in extract].

**Cemini posture:** **REFERENCE / steal-from** — poker HU chart refinement via running-average villain mixture anchor (complements K124 MAFP fictitious play + K125 trajectory verifier). No code → offline pattern brief only.

## Snippets

> "Self-play with naive gradient ascent cycles in two-player zero-sum games: the last iterate orbits the equilibrium." [Source: arXiv:2606.22688 abstract (retrieved 2026-06-23)]

> "Among causal convex averages of a fixed mean lag the running average (flat profile, peak = mean) uniquely minimizes that peak, while a snapshot's peak lag exceeds its mean." [Source: arXiv:2606.22688 abstract (retrieved 2026-06-23)]

> "PPO self-play with a λ KL(πθ ∥ πmag) term, where the magnet πmag is the running-average (Polyak) policy and the opponent is the average opponent." [Source: arXiv:2606.22688 §intro (retrieved 2026-06-23)]

## Dead Ends

- Tabular/game-theoretic proof setting ≠ NLHE action space — steal is **reference-update schedule**, not literal PPO install without sim validation.
- Independent researcher, no OSS — cannot Adopt until repo ships.
