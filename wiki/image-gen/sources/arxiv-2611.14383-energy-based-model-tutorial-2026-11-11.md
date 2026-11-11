---
title: "An energy-based lens on all of machine learning (78-page tutorial)"
type: source
tags: [source, arxiv, tutorial, energy-based-models, foundations]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-11
updated: 2026-11-11
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | An Energy-Based Perspective on Machine Learning |
| Authors | Bo Dai (Georgia Tech), Yilun Du (Harvard) |
| arXiv | 2611.14383 |
| Pages | 78 |
| Read status | skimmed (abstract) |

## Narrative

A tutorial, and the framing is the contribution. Energy-based models are usually presented as one family among many — `p(x) ∝ exp(−E(x))`. This uses them as **a single lens that connects the different aspects of machine learning.**

The organising claim: **any EBM is specified by three choices.**

| Choice | What it determines |
|-------|--------------------|
| **The energy** | What the model represents |
| **The inference procedure** | How you sample from or optimise it |
| **The learning method** | How the energy is fit to data |

That decomposition is what makes it a lens rather than a technique. Almost every model has an implicit energy, an implicit inference procedure, and an implicit learning rule; naming them makes the differences between model families structural rather than historical.

The tutorial develops the components — sampling, variational inference, maximum likelihood, noise contrastive estimation, pseudolikelihood.

### Why it is filed here

It is a reference text, not a result. Its value in this wiki is that it gives one vocabulary for the diffusion work already catalogued: a diffusion model's score is a gradient of an energy, sampling is inference, training is fitting. Pages that describe these as separate techniques can be read as one thing.

**Caveat.** Abstract and title page only. No chapter-level summary here.

## Snippets

> "Any EBM is specified by three choices: the energy, which determines what the model represents; the inference procedure, which samples from or optimizes the energy; and the learning method, which fits the energy to data." [Source: arxiv-2611.14383 p.1]

## Dead Ends

- **Citing a specific formulation.** Title page only; read the chapter before quoting.
