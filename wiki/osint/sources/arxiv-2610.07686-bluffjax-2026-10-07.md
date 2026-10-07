---
title: "BluffJAX: Adversarial Imperfect Information Games in JAX (arXiv 2610.07686)"
type: source
tags: [source, k284, arxiv, poker, game-theory, rl, cfr]
keywords: [bluffjax, jax, cfr, poker, kuhn, leduc, exploitability, imperfect-information]
related:
  - concepts/k284-arxiv-wave.md
  - entities/tools/bluffjax.md
maturity: draft
created: 2026-10-07
updated: 2026-10-07
read_status: read
---

## Relations

- @concepts/k284-arxiv-wave.md
- @entities/tools/bluffjax.md

## Raw Concept

| Title | BluffJAX: Adversarial Imperfect Information Games in JAX |
| Authors | Aryaman Reddi, Jan Peters (TU Darmstadt / Hessian.ai / DFKI), Carlo D'Eramo (Univ. Würzburg) |
| Type | arXiv preprint (cs.AI) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.07686-bluffjax-adversarial-imperfect-information-games.pdf` |
| Retrieved | 2026-10-07 |
| arXiv | 2610.07686v1 |
| License | **MIT** |
| Code | `github.com/bluffjax/bluffjax` |
| read-status | read |

## Narrative

The first open-source, **hardware-accelerated JAX suite for adversarial imperfect-information games** — deception and hidden information.

### What is in it

**10 JAX-native games:** Kuhn Poker, Leduc, Texas Hold'Em Limit/No-Limit, 5 Card Draw, 7 Card Stud, Goofspiel, Werewolf, Bluff, Kemps. Performance comes from `jax.vmap` (parallel environments), `jax.jit` (XLA), and `jax.lax.scan`. It ships a **fully JIT-compatible Counterfactual Regret Minimization (CFR)** and exploitability metrics for Kuhn/Leduc.

### Results

- Scales to **hundreds of millions of samples/s**; at 10,000 parallel environments even the slowest game (Seven Card Stud) still produces ~**2×10⁷ samples/s**.
- Uniform-random exploitability: Kuhn **0.4583**, Leduc **2.3736** — matches OpenSpiel / Kawamura et al.

### Why it matters here

**MIT** and directly usable. This is the GPU-accelerated **poker/imperfect-information RL environment** the gambling/poker lane can build on — CFR baselines at millions of samples/s on one accelerator. Route to the Gambling wiki and the poker-arena thread.

## Snippets

> "At 10,000 parallel environments the slowest game (Seven Card Stud) still generates ~2e7 samples/s." [Source: arxiv-2610.07686-bluffjax-adversarial-imperfect-information-games.pdf]

> "Uniform-random exploitability: Kuhn 0.4583, Leduc 2.3736." [Source: arxiv-2610.07686-bluffjax-adversarial-imperfect-information-games.pdf]
