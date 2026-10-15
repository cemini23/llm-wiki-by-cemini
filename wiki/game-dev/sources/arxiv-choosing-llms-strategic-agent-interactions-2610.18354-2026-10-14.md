---
title: "Choosing LLMs for Strategic Agent Interactions"
type: source
tags: [arxiv, game-theory, model-selection, evaluation]
keywords: [strategic selection, meta game, bandit selector, opponent adaptation, seed runs]
related:
  - concepts/k291-game-dev-wave.md
maturity: draft
read_status: read
created: 2026-10-14
updated: 2026-10-14
---

## Relations

- @concepts/k291-game-dev-wave.md — K291 game-dev wave hub

## Raw Concept

Title: Choosing LLMs for Strategic Agent Interactions
Authors: Arastun Mammadli, Herbert Woisetschläger, Jawad Fayaz, Shiqiang Wang (University of Exeter, IBM Research)
Type: arXiv preprint (2610.18354)
Location: `research to be indexed/game-dev/arxiv-2610.18354-choosing-llms-for-strategic-agent-interactions.pdf`
Retrieved: 2026-10-14
Read status: read

## Narrative

Reframes model selection as a **meta game layered on the base game**: a selector fields one model per round from a portfolio, against a payoff matrix that is **latent and learned online**.

**Three findings:**
- The evaluation signal is **game-specific** — competence varies with game setup **and opponent**.
- A reliable signal needs **far more seed runs** than conventional benchmarking.
- **Embedding-based and self-reflection selectors fail** to capture the strategic signal consistently. A lightweight **multi-armed bandit** is more reliable, though still below the best fixed model. Non-stationary and adversarial bandit variants **did not beat a stationary bandit**.

Evaluated across **5 games and 10 LLMs**.

## Snippets

> "We find that the evaluation signal is game-specific, and that extracting a reliable signal requires a much higher number of seed runs N compared to traditional benchmarking setups." [Source: arxiv-2610.18354 p.1]

> "simple non-stationary and adversarial bandit variants fail to outperform a stationary bandit baseline, pointing to a gap in how current methods handle a shifting opponent." [Source: arxiv-2610.18354 p.1]

## Dead Ends

- Picking a model by benchmark score. Strategic competence is per-game and per-opponent; a single ranking does not transfer.
