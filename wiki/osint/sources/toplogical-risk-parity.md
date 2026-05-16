---
title: Topological Risk Parity (TRP) — Nayar, Ainasse & Kulkarni (FMI Technologies)
type: source
tags: [pdf, portfolio-strategy, risk-parity, graph-methods, long-short]
keywords: [Topological Risk Parity, TRP, minimum spanning tree, MST, Hierarchical Risk Parity, HRP, correlation distance, Mantegna distance, long-short, market-neutral, factor hierarchy, signal propagation]
related:
  - concepts/portfolio-strategy.md
  - entities/tools/riskfolio-lib.md
  - entities/components/kelly-cvar-risk-engine.md
maturity: validated
read_status: deep-read
created: 2026-04-27
updated: 2026-05-16
---

## Relations

- @concepts/portfolio-strategy.md — Portfolio Strategy corpus-index hub; TRP is a risk-parity / allocation method
- @entities/tools/riskfolio-lib.md — Riskfolio-Lib implements classical HRP; TRP is positioned as a non-binary, long/short-capable alternative to HRP
- @entities/components/kelly-cvar-risk-engine.md — Cemini's portfolio-risk module; TRP is a candidate topology-aware weighting layer upstream of Kelly/CVaR sizing

## Raw Concept

- **Original title**: Topological Risk Parity
- **Author(s)**: Revant Nayar, El Mehdi Ainasse, Dnyanesh Kulkarni (FMI Technologies LLC)
- **Type**: PDF — arXiv:2604.16773v1 [q-fin.PM], 18 Apr 2026; dated April 21, 2026
- **Location**: research for cemini/toplogical risk parity.pdf
- **Retrieved**: 2026-04-27
- **Length**: 15p
- **Read status**: deep-read
- **Cluster**: portfolio-strategy

## Narrative

**Topological Risk Parity (TRP)** is a tree-based portfolio-construction method designed for **signed cross-sectional signals** and **long/short, market-neutral, factor-aware** books — a deliberate departure from classical Hierarchical Risk Parity (HRP), which is binary-dendrogram-based, long-only, and propagates cluster-variance risk budgets. The motivating intuition: passive/factor flows impose a tree-like correlation structure on markets (formalized via a three-level nested-flow return model `rᵢ = θ_M z_M + θ_S z_{s(i)} + θ_B z_{b(i)} + εᵢ`, which yields strictly ordered covariance tiers basket > sector > market). A correlation-distance graph (Mantegna distance `Dᵢⱼ = √((1−ρᵢⱼ)/2)`) is reduced to a sparse **minimum spanning tree** backbone of `n−1` edges; the MST is then rooted and used to attenuate/redistribute signed signals.

The core object is the **topological factor** `gᵥ`, the product along the root-to-node path of `αᵤ(ρ) = (1−ρ) + ρ/b(u)`, where `b(u)` is a node's branching number and `ρ ∈ [0,1]` is a smooth control parameter. Final weights are `wᵥ = L · sᵥ·gᵥ / ‖x‖₁` (L = target gross leverage). `ρ = 0` recovers normalized raw-signal allocation; `ρ = 1` gives conservative equal-split. A key theoretical result is **deliberate local non-conservation**: branching expands aggregate descendant factor mass by `(b(u)−1)(1−ρ)`, letting topology shape exposure while attenuating conviction along any single path. TRP **preserves signal sign** (so long/short intent survives), needs **no covariance inversion and no cluster-variance recursion**, and admits a conditional `L¹`-Lipschitz stability bound.

Two variants: **TRP-MST** (generic rooted MST, root chosen by hub-degree / max-signal / fixed-index) and **Semi-Supervised TRP (TRP-SPY/XL)**, which imposes an economic prior — a dummy SPY market root with the 11 sector ETFs forced as depth-one children — enabling explicit market/sector/factor neutrality. Acknowledged caveats: root choice and MST instability under small correlation changes both materially move allocations, and the sector-anchored DFS is order-dependent for non-sector names. Relevance to Cemini: TRP is a covariance-inversion-free, interpretable weighting layer well-suited to L/S equity stat-arb and factor-neutral books — a natural complement (or alternative) to Riskfolio-Lib's HRP, sitting upstream of the Kelly/CVaR risk engine.

## Snippets

- "Relative to classical Hierarchical Risk Parity (HRP), TRP is non-binary and designed for signed cross-sectional signals and hedged long-short portfolios: it preserves signal direction while using return-dependence geometry to shape exposures." [Source: toplogical risk parity.pdf p.1]

- "For each internal node u with b(u) ≥ 1, define αᵤ(ρ) := (1 − ρ) + ρ/b(u). This is the key propagation coefficient." [Source: toplogical risk parity.pdf p.5]

- "The exact local deviation from conservative splitting is βᵤ(ρ) − 1 = (b(u) − 1)(1 − ρ). Equivalently, whenever ρ < 1 and b(u) > 1, branching expands total descendant factor mass relative to the conservative benchmark." [Source: toplogical risk parity.pdf p.8]
