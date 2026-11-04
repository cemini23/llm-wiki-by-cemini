---
title: "Vis-Lens — generating preferred images for a neuron, without per-image optimisation"
type: source
tags: [source, arxiv, interpretability, diffusion, vae, fmri, neuroscience]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Structured Visual Landscape: Generating Preferred Representations in Biological and Artificial Neural Networks |
| Authors | Yusong Zhao (University of Illinois Urbana-Champaign), Edgar Y. Walker (University of Washington) |
| arXiv | 2611.03597 |
| Pages | 42 |
| Read status | skimmed (abstract) |

## Narrative

Understanding what makes a neuron fire matters both for interpreting black-box networks and for understanding visual representation in the brain.

The paper proposes a **structured visual representations landscape** and an **activation-based prior** that regularises that landscape with activations from brain regions or network units.

**Vis-Lens** combines a variational autoencoder and a diffusion model into one image-generation framework. It generates natural, realistic **preferred images** by directly modifying activation-regularised latent codes — **without per-image iterative optimisation**.

### Why the "without iterative optimisation" part is the contribution

Prior methods for this generate an image and then optimise it toward a high activation, one image at a time. That is slow, and the result tends to look adversarial — the model's preferred image is often something no eye would call a real object.

Moving the constraint into a prior over the latent space means the preferred image comes out in one pass and stays in the natural image manifold.

Validated on artificial networks and on human visual cortex using fMRI.

**Caveat.** Abstract only. No improvement figure reproduced.

## Snippets

> "It enables the generation of natural, realistic preferred images by directly modifying the activation-regularized latent codes without per-image iterative optimization." [Source: arxiv-2611.03597 p.1]

## Dead Ends

- **Citing the improvement over prior art.** Abstract states it improves; no figure here.
