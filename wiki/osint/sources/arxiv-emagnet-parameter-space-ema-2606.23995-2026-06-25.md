---
title: "EMAgnet — parameter-space EMA self-play regularization (arXiv 2606.23995)"
type: source
tags: [source, arxiv, self-play, game-theory, riot-games, k129]
keywords: [2606.23995, EMAgnet, PPO-EMAg, parameter-space EMA, exploitability, magnet policy]
related:
  - concepts/garip-running-average-self-play.md
  - concepts/multi-agent-fictitious-play-llm.md
  - sources/arxiv-garip-self-play-2606.22688-2026-06-23.md
  - sources/arxiv-mafp-fictitious-play-2606.19308-2026-06-20.md
  - concepts/devfun-poker-agent-challenge-2026.md
maturity: draft
read_status: read
created: 2026-06-25
updated: 2026-06-25
clusters: [rl-marl, llm-agents]
---

## Relations

- @concepts/garip-running-average-self-play.md — K127 running-average magnet cluster
- @sources/arxiv-garip-self-play-2606.22688-2026-06-23.md — complementary last-iterate self-play reference
- @concepts/devfun-poker-agent-challenge-2026.md — poker HU self-play steal target

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | EMAgnet: Parameter-Space EMA Regularization for Policy Gradient Self-Play in Large Games |
| **Authors** | Tristan Maidment, JB Lanier, Chase McDonald, Nathan Tsang (Riot Games); Eugene Vinitsky (NYU); Roy Fox (UCI); Albert Wang; Wesley N. Kerr (Riot Games) |
| **arXiv** | 2606.23995v1 (Jun 2026) |
| **sha256** | `656dc3f1a329395011f438ee8c2d13ca0fed68dbc008ac99a6ae7273bd8a9bf0` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.23995-emagnet-parameter-space-ema-regularization-for-p.pdf` |
| **Retrieved** | 2026-06-25 (inbox) |
| **Read status** | read (abstract + magnet mechanism) |

## Narrative

Regularized **PPO self-play** can match specialized game-theoretic solvers in two-player zero-sum IIGs. **Uniform-magnet** (entropy bonus) regularizes equally toward all actions — wasteful when most strategies are dominated.

**EMAgnet (PPO-EMAg):** maintains **parameter-space EMA** of policy network weights as adaptive regularization target — forgets dominated strategies as policy improves, retains smoothed mixture over relevant self-play cycling strategies [TENTATIVE].

Compared to PPO + uniform magnet (linear / power-law annealing): lower exploitability on standard benchmarks; consistent gains on games with many strictly dominated strategies (e.g. Control Biased RPS navigation forfeit trap) [TENTATIVE].

**Cemini posture:** **Steal-from** for poker-arena HU — EMA magnet vs K127 GARIP running-average policy magnet; Riot production signal elevates priority over independent GARIP (no public repo).

## Snippets

> "EMAgnet, which instead regularizes toward an exponential moving average (EMA) of the last-iterate policy's parameters." [Source: arXiv:2606.23995 abstract (retrieved 2026-06-25)]

> "The uniform target is strategically agnostic as it regularizes equally toward all strategies regardless of whether they are viable or strictly dominated." [Source: arXiv:2606.23995 §1 (retrieved 2026-06-25)]

> "EMAgnet achieves lower exploitability in the majority of tested environments, with consistent performance gains across games containing strictly dominated strategies." [Source: arXiv:2606.23995 abstract (retrieved 2026-06-25)]

## Dead Ends

- Riot internal game benchmarks ≠ NLHE — magnet schedule needs sim validation before dev.fun submission.
