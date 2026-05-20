---
title: "Phynance — Stochastic calculus + derivative pricing lecture notes (Kakushadze 2014, arXiv:1405.1948v2)"
type: source
tags: [source, arxiv, quant-finance, stochastic-calculus, derivative-pricing, path-integral, lecture-notes, k55]
keywords: [phynance, kakushadze, quantigic, stochastic-calculus, ito-calculus, cameron-martin-girsanov, black-scholes, martingale, binomial-tree, path-integral, brownian-motion, radon-nikodym, hedging, european-options, american-options, lookback, asian, barrier, stony-brook-yitp]
related:
  - concepts/quant-finance.md
  - concepts/stochastic-calculus-foundations.md
  - entities/people/zura-kakushadze.md
  - entities/organizations/quantigic-solutions.md
  - concepts/hiring-quant-talent-philosophy.md
  - concepts/time-series-arima-garch-framework.md
maturity: validated
read_status: skimmed
created: 2026-05-20
updated: 2026-05-20
clusters: [quant-finance, education]
---

## Relations

- @concepts/quant-finance.md — corpus-index home for the foundational quant material
- @concepts/stochastic-calculus-foundations.md — synthesized reference page covering the Itô / Girsanov / Black-Scholes core
- @entities/people/zura-kakushadze.md — author (Quantigic Solutions, UConn Physics)
- @entities/organizations/quantigic-solutions.md — author's firm

## Raw Concept

- **Title**: "Phynance" (a play on physics + finance — derivative-pricing recast in the language of path integrals)
- **Author**: Zura Kakushadze, PhD (Quantigic Solutions LLC; Department of Physics, University of Connecticut)
- **Type**: Ph.D.-level lecture notes (advanced course taught Spring 2002 at the C.N. Yang Institute for Theoretical Physics, Stony Brook)
- **Length**: 111 pages
- **Identifier**: arXiv:1405.1948v2 (q-fin.MF, originally May 2014, v2 4 Mar 2015)
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/1405.1948v2.pdf`
- **Retrieved**: 2026-05-20 (dropped into `research to be indexed/`)
- **Reference text**: course "to a certain extent follows" M. Baxter and A. Rennie, *Financial Calculus: An Introduction to Derivative Pricing*

## Narrative

Foundational quant-finance pedagogical reference covering stochastic calculus and derivative pricing, with the distinctive angle of recasting many derivations in **path-integral** language familiar from theoretical physics (hence "Phynance"). Includes "quiz" problems with solutions drawn from quantitative-finance interview questions from the early-2000s era.

### Coverage (table of contents abstracted)

1. **Introduction: How Does "Bookie the Crookie" Make Money?** — bookmaker arbitrage as motivating example
2. **Bid, Ask and Spread**
3. **Stocks, Bonds and Free Markets**
4. **Arbitrage Pricing**
5. **Binomial Tree Model** — risk-neutral measure; worked example: baseball World Series probability
6. **Martingales** — Tower Law; martingale measure; binomial representation theorem; self-financing hedging
7. **Discrete vs Continuous Models** — Brownian motion intro
8. **Stochastic Calculus** — Itô calculus; Radon-Nikodym process; path integral; continuous Radon-Nikodym; Cameron-Martin-Girsanov theorem
9. **Continuous Martingales** — driftlessness; martingale representation theorem
10. **Continuous Hedging** — change of measure in general one-stock model; terminal value pricing; alternative formulation; heat-kernel method
11. **European Options** — call, put, binary
12. **Plus**: subsequent chapters cover American options, exotic options (lookback, Asian, barrier), interest-rate models, multi-factor models, etc. (continuing to 111p — only ToC fully read in this ingest)

### Pedagogical positioning

- Designed for physics Ph.D.-level audience that already knows Lagrangian/Hamiltonian mechanics, path integrals, and stochastic calculus from a physics lens.
- "Phynance" framing is **substantively useful**, not just cute branding: path-integral formulation gives a different angle on Cameron-Martin-Girsanov (change of measure ↔ change of probability density along paths), Heat-kernel method (Schrödinger-equation correspondence), and exotic option pricing (path-dependent payoffs as path-integral observables).
- Quiz problems = early-2000s interview-style derivations (binomial-tree problems, hedging questions, Black-Scholes-from-first-principles). Useful as a self-test corpus.

### Why this is in the wiki

This is **foundational pedagogical material**, not a strategy or a tool. Two reasons to record it:

1. **Recurring `[NEEDS VERIFICATION]` resolver**: many wiki concept pages cite stochastic-calculus results (Itô's lemma, Girsanov change-of-measure, martingale representation theorem) without a primary source pointer. Phynance is now the in-wiki canonical reference for those; future verification tags can point here.

2. **Hiring-philosophy parallel**: companion to the ssrn-4668072 Simons interview ingested in the same batch — Simons explicitly says he hires mathematicians and physicists, not finance professionals. Kakushadze's Phynance is the kind of material that produces those candidates — a working physicist applying the physics toolkit to derivative pricing, then founding a quant firm (Quantigic). Both sources together motivate the broader concept page on hiring/structure of quant firms.

### Author and venue context

- **Zura Kakushadze**: theoretical physicist (string theory background, Harvard/CERN postdoc lineage) → quantitative-finance practitioner. Founded Quantigic Solutions LLC, Stamford CT. Active publisher on arXiv q-fin (50+ papers across statistical arbitrage, factor models, risk modeling).
- **C.N. Yang Institute for Theoretical Physics, Stony Brook**: founded by C.N. Yang (Nobel 1957, parity violation). Same intellectual lineage — physicists doing applied math — that produced Renaissance Technologies via Jim Simons (Stony Brook math chair before founding RenTech).

## Snippets

> "These are the lecture notes for an advanced Ph.D. level course I taught in Spring'02 at the C.N. Yang Institute for Theoretical Physics at Stony Brook. The course primarily focused on an introduction to stochastic calculus and derivative pricing with various stochastic computations recast in the language of path integral, which is used in theoretical physics, hence 'Phynance'." [Source: 1405.1948v2.pdf p.1]

> Table of Contents (abridged): 1. Introduction: How Does "Bookie the Crookie" Make Money? · 4. Arbitrage Pricing · 5. Binomial Tree Model (incl. Risk-neutral Measure; Baseball World Series) · 6. Martingales (Tower Law; Martingale Measure; Binomial Representation; Self-financing Hedging) · 8. Stochastic Calculus (Itô; Radon-Nikodym; Path Integral; Cameron-Martin-Girsanov) · 9. Continuous Martingales · 10. Continuous Hedging (Heat Kernel Method) · 11. European Options. [Source: 1405.1948v2.pdf pp.2-3]
