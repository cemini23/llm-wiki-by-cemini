---
title: "BluffJAX — GPU-accelerated imperfect-information game suite (MIT)"
type: entity
tags: [tool, poker, game-theory, jax, cfr, mit, k284]
keywords: [bluffjax, jax, cfr, poker, kuhn, leduc, holdem, exploitability, k284]
related:
  - sources/arxiv-2610.07686-bluffjax-2026-10-07.md
  - concepts/k284-arxiv-wave.md
maturity: draft
created: 2026-10-07
updated: 2026-10-07
---

## Relations

- @sources/arxiv-2610.07686-bluffjax-2026-10-07.md — arXiv 2610.07686
- @concepts/k284-arxiv-wave.md — K284 arXiv hub

## Raw Concept

- **Repo:** `github.com/bluffjax/bluffjax`
- **License:** **MIT**
- **Paper:** arXiv 2610.07686 (Reddi, Peters, D'Eramo)
- **Stack:** JAX (`vmap`, `jit`, `lax.scan`)

## Narrative

The first open-source, **hardware-accelerated JAX suite for adversarial imperfect-information games**. Ten JAX-native games: Kuhn, Leduc, Texas Hold'Em (Limit/No-Limit), 5 Card Draw, 7 Card Stud, Goofspiel, Werewolf, Bluff, Kemps. Ships a **fully JIT-compatible CFR** plus exploitability metrics.

### Results

**~2×10⁷ samples/s** at 10,000 parallel envs on the slowest game. Uniform-random exploitability Kuhn **0.4583**, Leduc **2.3736** (matches OpenSpiel).

### Why it matters here

The **GPU-accelerated poker/imperfect-information RL environment** the poker lane can build on — CFR baselines at millions of samples/s on one accelerator, MIT, no licence friction. Route: Gambling wiki + the poker-arena thread.

## Snippets

> "At 10,000 parallel environments the slowest game (Seven Card Stud) still generates ~2e7 samples/s." [Source: arxiv-2610.07686-bluffjax-2026-10-07.md]
