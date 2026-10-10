---
title: "Perceptually grounded evaluation for co-speech gesture generation (arXiv 2610.11669)"
type: source
tags: [source, k288, arxiv, video-generation, evaluation, gesture, avatar]
keywords: [co-speech-gesture, benchmark, sgpi, semantic-gesture-preservation, emage, semtalk, gesturelsm, perception]
related:
  - concepts/k288-arxiv-wave.md
maturity: draft
created: 2026-10-10
updated: 2026-10-10
read_status: read
---

## Relations

- @concepts/k288-arxiv-wave.md

## Raw Concept

| Title | Perceptually Grounded and Semantics-Aware Evaluation for Holistic Co-Speech Gesture Generation |
| Authors | Nick Milkin, Lanmiao Liu, Esam Ghaleb, Asli Ozyurek, Zerrin Yumak (MPI Psycholinguistics; Utrecht; Donders) |
| Type | arXiv preprint (cs.CV) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.11669-perceptually-grounded-and-semantics-aware-evalua.pdf` |
| Retrieved | 2026-10-10 |
| arXiv | 2610.11669v1 |
| Site | `holisticgesturebenchmark.github.io` |
| read-status | read |

## Narrative

An evaluation benchmark for **co-speech gesture generation** — the body/hand motion an avatar produces while speaking. Unlike most video-generation evals, this one is **validated against human perception**.

### Method

**13 objective metrics** validated against human ratings, plus a new **semantics-aware** metric — **Semantic Gesture Preservation**:

    SGP_cm = 1 − n(τ̂_cm = beat) / n(E_c)

i.e. **the fraction of annotated semantic-gesture intervals that were NOT collapsed into generic beat gestures** (Gemini 2.5 Pro classifies). Five target-specific **composite OLS predictors** `C_q(xᵢ) = β₀q + βᵀ_q zᵢ` over standardised 13-metric vectors, evaluated by LOOCV.

### Results

**101 valid participants** (49 muted, 52 audio) across five dimensions:

- **SC shows no significant correlation with any perceptual dimension** — a common metric that measures nothing people notice.
- **SGP correlates with speech timing and content match at ρ = 0.39.**
- **Composites beat the best single metric:** content match **ρ 0.7824** (+0.0805 over Coverage), absence of animation errors **0.7065**, speech timing **0.7439**, human-likeness 0.6568, motion diversity 0.5375.
- Four models benchmarked: **EMAGE, SemTalk, GestureLSM, SemConFlow**.

### Why it matters here

Two transferable ideas: (1) **a widely-used metric (SC) that correlates with nothing** — the same "aggregate metric is blind" lesson as PatchBench (K285); (2) **semantics-aware scoring beats motion-plausibility scoring** — "is this a *beat* or a *meaningful* gesture" is the question that tracks human perception. Route: **Image-gen / video** lane. Code and annotations "on acceptance".

## Snippets

> "SC shows no significant correlation with any perceptual dimension." [Source: arxiv-2610.11669-perceptually-grounded-and-semantics-aware-evalua.pdf]

> "SGP_cm = 1 − n(τ̂_cm = beat)/n(E_c)." [Source: arxiv-2610.11669-perceptually-grounded-and-semantics-aware-evalua.pdf]
