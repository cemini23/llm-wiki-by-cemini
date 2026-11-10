---
title: Genealogical reinforcement — local family structure as a growth predictor
type: concept
related:
  - sources/arxiv-genealogical-reinforcement-2611.08548.md
  - concepts/computational-genealogy-archival-automation.md
  - concepts/long-memory-phase-transition-correlated-bernoulli.md
updated: 2026-11-10
---

## Raw Concept

Can a node's growth be predicted from the density and quality of its local neighbourhood in a tree? Prompted by arXiv 2611.08548.

## Narrative

### The model

A discrete-time branching process where offspring probability depends on the local family tree:

```
ξ(v) ~ Binomial(K=2, p(v))
p(v) = 1 / (1 + exp(-β0 - β1 G(v)))
G(v) = Σ_{u living, d(u,v) ≤ 2D} e^(-θ d(u,v))
```

- `β0` is the baseline reproduction rate. `β0 < 0` is a harsh environment where reinforcement is needed to avoid extinction.
- `β1 > 0` sets the strength of reinforcement. `β1 = 0` gives an ordinary Galton–Watson process.
- `θ` sets how fast influence decays with genealogical distance.
- `D` is the truncation depth.

[Source: arxiv-2611.08548-genealogical-reinforcement-in-branching-processe.pdf pp.2-3]

### The three statistical results

1. **Identifiability needs depth.** With `D ≥ 2`, the three parameters are globally structurally identifiable when the sample has at least two distinct non-zero genealogical distances and linearly independent relative counts. With `D = 1` the parameters are degenerate. [Source: arxiv-2611.08548-genealogical-reinforcement-in-branching-processe.pdf p.4]
2. **The null must be simulated.** `β1` sits on the parameter boundary and `θ` is unidentifiable under the null. Wilks' theorem does not apply. The paper simulates the null: 95% thresholds are **11.11** at `D = 3` and **12.11** at `D = 5`. [Source: arxiv-2611.08548-genealogical-reinforcement-in-branching-processe.pdf p.6]
3. **Depth buys power.** Detection power rises sharply from `D = 3` to `D = 5`. Observing deeper relationships detects weaker reinforcement.

### The representation theorem

The process is a **tree-valued multitype branching process** on a finite type space. A tree of depth `D` is the reproductive object. The number of types follows `ρ_D = (ρ_{D-1}+1)(ρ_{D-1}+2)/2`.

### What is transferable

The transferable structure is **local density as a feature in a growth model**. Any graph where a node's outcome depends on nearby nodes can use the same shape:

- a weighted sum of neighbour counts, with exponential decay by distance;
- a logistic link to the outcome;
- a truncation depth chosen to keep the state space finite;
- an identifiability check before fitting.

Candidate settings include entity resolution (does a candidate match gain support from nearby matches), referral and co-authorship growth, and cluster growth in a marketplace.

### What is not transferable

The paper is a toy model for one mechanism. It is not a social model, and it says so. The biological setting supplies the interpretation; the mathematics only supplies the shape.

## Snippets

> "A large family structure at short genealogical distances is most likely to beget a locally large family. We refer to this concept as genealogical reinforcement." [Source: arxiv-2611.08548-genealogical-reinforcement-in-branching-processe.pdf p.1]

> "Given a model with a parameter on the boundary of the space, Chernoff's theorem dictates that the null distribution follows a mixture ... However, as our model incorporates a nuisance parameter that is unidentifiable under the null hypothesis, we must instead directly simulate the null distribution." [Source: arxiv-2611.08548-genealogical-reinforcement-in-branching-processe.pdf p.5]

## Dead Ends

- **Using this as a genealogy-record method.** It has no archive content.
- **Fitting `D = 1` and reporting three parameters.** They are not identifiable at that depth.
