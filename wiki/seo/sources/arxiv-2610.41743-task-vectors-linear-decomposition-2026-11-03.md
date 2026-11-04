---
title: "Task vectors decompose into task-recognition and task-learning components"
type: source
tags: [source, arxiv, task-vectors, interpretability, steering, control]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Task Vectors Can Be Linearly Decomposed into Interpretable and Controllable Components |
| Authors | Yukiya Horiba (Keio), Hakaze Cho (RIKEN, Tohoku), Takahiro Yakoh (Keio) |
| arXiv | 2610.41743 |
| Pages | 13 |
| Read status | skimmed (abstract) |

## Narrative

Task vectors are a compact way to steer a model, but they are treated as **atomised directions** extracted from hidden states — with no account of their internal structure.

Prior work decomposed in-context learning into **Task Recognition (TR)** and **Task Learning (TL)**. This paper asks whether a single task vector decomposes the same way.

It formulates a TR/TL decomposition from candidate-label unembeddings, splitting each vector into TR, TL, and residual components, then optimises the TR and TL coefficients with Bayesian optimisation.

### Results

- TR/TL-based optimisation finds intervention directions that **outperform the original task vectors**.
- Optimising over random directions also helps — but TR/TL search gives **more reliable** gains, particularly for instruction-based vectors.
- Isolated interventions on the components produce distinct logit-level effects **consistent with their intended roles**.

### Why "random also helps" is the honest part

The paper reports that random-direction optimisation improves performance too. That admission matters: it means some of the gain is generic, not structural. What TR/TL buys is reliability, not the effect itself.

That is the right way to report an ablation — the baseline that would embarrass the method is included and explained rather than omitted.

**Relevance.** Steering vectors are how a model's behaviour gets adjusted without retraining. Knowing that a vector carries both "which task is this" and "how to do it" means those can be adjusted separately.

**Caveat.** Abstract only, no figures.

## Snippets

> "Although optimization over random directions can also improve performance, TR/TL-based search yields more reliable gains, particularly for instruction-based TVs." [Source: arxiv-2610.41743 p.1]

## Dead Ends

- **Citing an accuracy delta.** Abstract only.
