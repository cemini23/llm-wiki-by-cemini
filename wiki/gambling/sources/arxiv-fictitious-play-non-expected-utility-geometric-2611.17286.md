---
title: "Fictitious Play When Agents Are Not Expected-Utility Maximizers: A Geometric Analysis in 2-Action Games"
type: source
tags: [source, arxiv, game-theory, fictitious-play, risk-measures, shelf]
keywords: [nonlinear-fictitious-play, single-crossing-property, finite-crossing, cvar, rho-nash, 2x2-games, 2xn-games]
related:
  - concepts/opponent-modeling-imperfect-info.md
  - sources/arxiv-2610.09244-risk-averse-multi-population-mfg-2026-10-09.md
maturity: draft
created: 2026-11-14
updated: 2026-11-14
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Fictitious Play When Agents Are Not Expected-Utility Maximizers: A Geometric Analysis in 2-Action Games |
| Authors | Hao Liang, Solaleh Mohammadi, Kaiqing Zhang (University of Maryland, College Park) |
| Type | academic paper (arXiv preprint, cs.GT) |
| Location | `research to be indexed/gambling/arxiv-2611.17286-fictitious-play-when-agents-are-not-expected-uti.pdf` |
| arXiv | 2611.17286v1 [cs.GT], 12 November 2026 |
| Retrieved | 2026-11-14 |
| Pages | 79 |
| File | `arxiv-2611.17286-fictitious-play-when-agents-are-not-expected-uti.pdf` |
| Read status | read |

## Narrative

### What the paper is

Fictitious play (FP) is the oldest learning rule in games. Each agent best-responds to the empirical frequency of the opponent's past actions. The standard version assumes both agents maximise **expected** payoff.

This paper drops that assumption. Each action is now scored by a **general, possibly nonlinear functional** of the payoff distribution that the opponent's empirical belief induces. The authors call it **nonlinear fictitious play** (NL-FP). [Source: arxiv-2611.17286 p.1–2]

The functional can be a risk measure. The paper lists coherent and convex risk measures, conditional value-at-risk (CVaR), spectral risk measures, rank-dependent expected utility, and cumulative prospect theory [Source: arxiv-2611.17286 p.2].

### The formal move

Classical FP scores action `a` by `E[r(a, A₋ᵢ)]` under the empirical belief. NL-FP scores it by `ρ(r(a, A₋ᵢ))` for a law-invariant functional `ρ`. Classical FP is the special case `ρ = mean` [Source: arxiv-2611.17286 p.5–6].

The equilibrium notion moves with the functional. A **ρ-Nash equilibrium** requires each player's strategy to be a best response under its own `ρ` [Source: arxiv-2611.17286 p.6].

The analysis then runs on the **advantage function** — the value difference between the two actions — and on its sign changes. In 2×2 games each player's best response is decided by the sign of one scalar function.

### What it proves

| Setting | Condition | Result |
|---------|-----------|--------|
| 2×2 | Strict single crossing | Convergence, continuous and discrete |
| 2×2 | Single crossing | Convergence, continuous and discrete |
| 2×2 | Finite crossing (may fail single crossing) | Convergence, continuous and discrete |
| 2×3 | CVaR row player, risk-neutral column player | **Nonconvergence** — nonconstant periodic orbit |
| 2×n | Finite crossing plus nondegeneracy | Convergence, continuous and discrete |

Two findings carry the weight.

1. **Single crossing preserves the classical geometry.** When the advantage functions cross once, the strategy square keeps the same four best-response regions and the same two patterns as classical FP: coordination-type with a saddle, or spiral-type around an interior equilibrium [Source: arxiv-2611.17286 p.9–10].
2. **The positive result is fragile beyond 2×2.** A 2×3 game with a **CVaR** row player and a risk-neutral column player admits a nonconstant periodic orbit in continuous time [Source: arxiv-2611.17286 p.2–3].

Several functionals common in finance and decision theory **violate** single crossing. The finite-crossing condition is the paper's answer: convergence survives a bounded number of crossings, and the authors give a geometric proof over a finite planar grid [Source: arxiv-2611.17286 p.28].

### Where the betting link is, and how far it goes

There is one real structural connection, and it stops well short of a usable result.

**The connection.** A nonlinear evaluation functional `ρ` assigns one number to a payoff distribution. A staking or selection rule does the same thing. Both collapse a distribution to a decision. The paper's `ρ-Nash` is the equilibrium version of "each side uses its own risk measure, not the mean". The wiki already holds one formal treatment of risk-averse equilibrium learning — see @sources/arxiv-2610.09244-risk-averse-multi-population-mfg-2026-10-09.md — and this paper is the discrete 2-action counterpart.

**Where it stops.**

- The object is a **learning algorithm** in an abstract matrix game. There is no price, no stake, no market, and no empirical data.
- The paper does **not** treat betting. Nothing here sizes a wager, and the word Kelly does not appear in the parts read.
- The result is about **convergence of the iteration**, not about the quality of a decision. Knowing that a CVaR player's best response can cycle in a 2×3 game says nothing about a sportsbook line or a Kalshi contract.
- A betting market is not a 2-action repeated game between two learning agents. The mapping needs a model that the paper does not supply.

**The one caution worth keeping.** If an agent or a model evaluates outcomes by a risk measure instead of expected value, the equilibrium it reaches can differ from the expected-value equilibrium, and in some small games the learning need not settle at all. That is a reason to record which objective a bot uses, not a reason to change a strategy.

### Verdict

**Weak fit. No adopt.** The paper is a theory shelf item, in the same class as the FP convergence pages already on file. It joins @concepts/opponent-modeling-imperfect-info.md as a literacy entry.

**Routing:** wiki-only; no distribution. `wont_wire`.

## Snippets

> "In this work, we study nonlinear fictitious play (NL-FP), in which each pure action is evaluated by a general, possibly nonlinear functional of the payoff distribution induced by the opponent's empirical belief." [Source: arxiv-2611.17286 p.1]

> "We show that the convergence of NL-FP in 2 × n (n ≥ 3) games may fail even for continuous-time NL-FP, when the two-action player uses conditional value-at-risk (CVaR) in a 2 × 3 game." [Source: arxiv-2611.17286 p.1]

> "Our analysis identifies the finite crossing property of advantage functions as a key to convergence." [Source: arxiv-2611.17286 p.28]

## Dead Ends

- **Reading `ρ-Nash` as a betting equilibrium.** The notion is local to a two-player matrix game with a fixed functional per player. A market has many participants and no shared action set of size two.
- **Importing the convergence result into an agent lane.** The result is for abstract 2-action games. The existing arena and bot pages already record the same caution for continuous MFG results.
- **Reading "risk measure" as "fractional Kelly".** The two are both nonlinear maps from a payoff distribution to a number. The paper does not connect them, and does not model staking. The analogy is structural only and is not evidence for any staking rule.
- **Automated results.** The paper discloses that three proofs were AI-assisted, with named model help on the 2×3 counterexample [Source: arxiv-2611.17286 p.28]. Treat the counterexample as reported, not verified here. [TENTATIVE]
