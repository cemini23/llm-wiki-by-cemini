---
title: "Repair risk in crypto option surfaces — admissible repairs disagree downstream"
type: source
tags: [source, arxiv, options, crypto, surface-fitting, greeks, risk]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Quantifying Repair Risk in Crypto Option Surfaces |
| Author | Tenghan Zhong (University of Southern California) |
| arXiv | 2611.00958 |
| Pages | 9 |
| Read status | skimmed (abstract) |

## Narrative

**A short paper that names a real and usually invisible problem.**

Option desks adjust raw crypto quotes into a price surface that stays inside bid–ask intervals and satisfies no-arbitrage across strikes, before computing Greeks, hedge quantities, or risk measures.

For the same quote panel, those constraints **admit multiple valid surfaces**. The paper calls them **admissible repairs**, and the variation in downstream outputs **repair risk**.

### The mechanism

The dispersion comes from **finite-difference amplification**: two admissible repairs within price distance ε can differ in local normalised-strike curvature by **4ε/h²**, where h is the local strike spacing.

That expression explains why the effect is worse than intuition suggests. Curvature is a second difference, so a second difference over a small h amplifies any first-order disagreement by h⁻². Tight strike spacing makes the amplification larger, not smaller.

### Why it matters for this workspace

Anything that computes Greeks, hedge ratios, or risk measures from a fitted surface inherits this. Two desks can hold identical quotes, both produce arbitrage-free surfaces, and both get different deltas.

The mitigation is not a better fit. It is **reporting the dispersion**: run the admissible repair more than once, or over a range of admissible fits, and show the spread in the output rather than a single number.

The paper proposes **repair-risk validation** as a matched framework for exactly that.

**Caveat.** Abstract only. No empirical magnitude is reproduced here.

## Snippets

> "For the same quote panel, however, these constraints may admit multiple such surfaces, which we call admissible repairs, with different downstream outputs… the mechanism is finite-difference amplification: two admissible repairs within price distance ε can differ in local normalized-strike curvature by 4ε/h²." [Source: arxiv-2611.00958 p.1]

## Dead Ends

- **Treating one arbitrage-free surface as the answer.** The constraints admit several, and they disagree downstream.
