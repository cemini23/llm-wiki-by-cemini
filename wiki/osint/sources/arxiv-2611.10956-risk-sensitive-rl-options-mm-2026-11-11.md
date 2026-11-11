---
title: "Risk-sensitive RL for an S&P 500 options market maker — an empirical study"
type: source
tags: [source, arxiv, options, market-making, reinforcement-learning, risk]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-11
updated: 2026-11-11
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Risk-Sensitive Reinforcement Learning for an Options Market Maker: An Empirical Study with Real S&P 500 Options |
| Authors | Jacky Chen, Ing-Haw Cheng, John Hull, Landis Li, Zissis Poulos, Justin Shi, Andreas Veneris, Zeyu Wang (University of Toronto; York University) |
| arXiv | 2611.10956 |
| Pages | 9 |
| Read status | skimmed (abstract) |

## Narrative

An options market maker absorbs client order flow and must **hedge the resulting inventory risk under trading frictions**. The paper studies **risk-sensitive** RL for that problem, on **real S&P 500 options**.

The author list is the credential: John Hull is a standard reference for derivatives theory, and Ing-Haw Cheng for options empirics. A paper from that group on real chains is worth more attention than the usual synthetic-market RL result.

### Why "risk-sensitive" is the right framing

A standard RL objective maximises expected reward. For a market maker, **expected P&L is the wrong objective** — the entire business is collecting premium for bearing a distribution it does not want to be ruined by.

Risk-sensitive RL optimises something closer to a utility over the outcome distribution rather than its mean. That is the correct formalisation of what a market maker actually does, and it is the part of the paper that transfers even if the method does not.

### The standing caution

This is an *empirical study*, not a deployed system. Backtest-to-live gaps in market making are large, and the paper's own framing — an empirical study on real options — is honest about being an evaluation rather than a product.

**Caveat.** Abstract only. No Sharpe, drawdown, or inventory figure reproduced.

## Snippets

> "Options market makers absorb client order flow and must hedge the resulting inventory risk under trading frictions. We study…" [Source: arxiv-2611.10956 p.1]

## Dead Ends

- **Citing a performance number.** Abstract only.
- **Reading this as a deployment.** It is an empirical study.
