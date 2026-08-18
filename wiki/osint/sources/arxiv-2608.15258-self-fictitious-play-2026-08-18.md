---
title: "Self-fictitious-play for potential monotone ergodic MFG (arXiv 2608.15258)"
type: source
tags: [arxiv, poker, mafp, mfg, k241]
keywords: [self-fictitious-play, mean-field-games, Lasry-Lions, occupation-measure]
related:
  - concepts/multi-agent-fictitious-play-llm.md
  - sources/arxiv-mafp-fictitious-play-2606.19308-2026-06-20.md
  - concepts/swap-regret-attention-fictitious-play.md
  - sources/arxiv-2607.08861-fictitious-play-fbsde-stochastic-games-2026-07-16.md
  - concepts/devfun-researcher-track-readiness-2026-06.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
read_status: read
---

## Relations

- @concepts/multi-agent-fictitious-play-llm.md — MAFP family; SFP is a single-trajectory belief variant
- @sources/arxiv-mafp-fictitious-play-2606.19308-2026-06-20.md — LLM MAFP primary
- @concepts/swap-regret-attention-fictitious-play.md — poker FP steal
- @sources/arxiv-2607.08861-fictitious-play-fbsde-stochastic-games-2026-07-16.md — FBSDE fictitious play
- @concepts/devfun-researcher-track-readiness-2026-06.md — Arena researcher track

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.15258, "Self-fictitious-play for Potential Monotone Ergodic Mean-field Games" |
| Authors | Yupeng Bai, Mathieu Laurière, Zhenjie Ren, Songbo Wang (Evry / NYU Shanghai / Côte d'Azur) |
| Retrieved | 2026-08-18 |
| File | `arxiv-2608.15258-self-fictitious-play-for-potential-monotone-ergo.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.15258-self-fictitious-play-for-potential-monotone-ergo.pdf` |
| Type | math.OC preprint |
| Dual-ID | **OSINT K241**. Poker Arena brief if MAFP steal is real (it is). |

## Narrative

Long-horizon learning in **ergodic, potential, monotone** mean-field games via a self-fictitious-play (SFP) dynamics. The state follows the optimal feedback for the current belief; the belief is updated from the **player's own empirical occupation measure**, not the population distribution. On the torus, SFP is contractive and has a unique invariant law. That invariant law sits within Wasserstein error of order **square-root of the belief-update rate** of the MFG Nash equilibrium. The proof uses uniform-in-time regularity of the ergodic HJB plus a Lasry–Lions energy. A linear-quadratic example shows the rate is sharp.

**Steal for Poker Arena `[TENTATIVE]`:** when you cannot observe the population (HU sandbox, opponent is a black box), update the fictitious-play belief from **your own occupation measure** and keep the belief-update rate small — error scales like √ε. This is a MAFP-family variant, not a replacement for Shen et al. stance-entangled MAFP. Do not drop it into live betting; researcher-track brief only.

## Snippets

> "the belief is updated using the player's own empirical occupation measure rather than the population distribution." [Source: arxiv-2608.15258 p.1]

> invariant law "quantitatively close to the MFG Nash equilibrium, with an error of order equal to the square root of the belief-update rate." [Source: arxiv-2608.15258 abstract]
