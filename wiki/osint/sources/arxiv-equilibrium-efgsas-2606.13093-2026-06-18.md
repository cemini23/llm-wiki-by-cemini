---
title: "Equilibrium Computation in Extensive-Form Games with Stochastic Action Sets — arXiv 2606.13093"
type: source
tags: [source, arxiv, game-theory, poker, cfr, k122]
keywords: [2606.13093, EFGSAS, SI-CFR, extensive-form, stochastic action sets, Nash equilibrium, sleeping regret]
related:
  - concepts/extensive-form-games-stochastic-action-sets.md
  - concepts/strategic-resource-acquisition-game-theory.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
maturity: draft
read_status: read
created: 2026-06-18
updated: 2026-06-18
clusters: [quant-finance, llm-agents]
---

## Relations

- @concepts/extensive-form-games-stochastic-action-sets.md — K122 synthesis
- @concepts/strategic-resource-acquisition-game-theory.md — competitive execution overlay sibling
- @concepts/poker-arena-multi-axis-cognitive-profile.md — poker eval cites CFR/equilibrium baselines for mixing axis

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Equilibrium Computation in Extensive-Form Games with Stochastic Action Sets |
| **Authors** | Thomas Schwarz, Ryann Sim, Chun Kai Ling |
| **arXiv** | 2606.13093 (11 Jun 2026) |
| **sha256** | `bf5b7d4fd7be0e9a2e4ff97e300026071fe7710655f51bd7e5f7bbafd1f6c38b` |
| **Repo** | none published |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.13093-equilibrium-computation-in-extensive-form-games.pdf` |
| **Retrieved** | 2026-06-18 (daily digest inbox) |
| **Read status** | read (abstract + contribution summary) |

## Narrative

Standard extensive-form games (EFGs) assume every legal action is always available at each decision node. **EFGSAS** relaxes this: from a base game, actions can be **stochastically restricted** exogenously — modeling realistic settings where the action set itself is random (e.g., liquidity gaps, rule variants, partial menu availability).

**Theory:** naïve expansion to an equivalent standard EFG can require **exponential** strategy representation; under an **independence assumption**, compact polynomial-size strategies exist relative to the base game.

**Algorithm — SI-CFR:** minimizes **sleeping internal regret** and converges to Nash equilibria with high probability in **two-player zero-sum** EFGSAS. A stochastic approximation step recovers compact Nash representations from SI-CFR iterates alone.

**Cemini posture:** **REFERENCE** — no install. Relevant as theoretical backdrop for poker equilibrium literature (Raeth 2606.13815 cites CFR/mixing-axis baselines) and for competitive execution games where action menus are venue- or latency-stochastic. Not directly applicable to frozen-weight LLM poker agents at inference.

## Snippets

> "Given a `base' EFG, we formalize a model that allows for actions to be stochastically restricted, leading to a corresponding Extensive-Form Games with Stochastic Action Sets (EFGSAS)." [Source: arXiv:2606.13093 abstract (retrieved 2026-06-18)]

> "We introduce an algorithm called SI-CFR that minimizes sleeping internal regret, converging to Nash equilibria with high probability in two-player zero-sum EFGSAS." [Source: arXiv:2606.13093 abstract (retrieved 2026-06-18)]

## Dead Ends

- No public code — cannot smoke SI-CFR without reimplementation.
- Multi-player / general-sum convergence not claimed in abstract — do not extrapolate to 6-max NLHE tournament dynamics.
