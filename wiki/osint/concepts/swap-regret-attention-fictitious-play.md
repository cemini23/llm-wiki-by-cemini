---

title: Swap-regret attention ≈ fictitious play (poker steal)
type: concept
tags: [concept, poker, game-theory, regret, k198]
keywords: [swap regret, smoothed fictitious play, CCE, CE, decide]
related:
  - sources/arxiv-2607.23333-swap-regret-attention.md
  - concepts/code-as-agent-harness.md
  - concepts/verifier-deployment-gap.md
  - sources/arxiv-2607.27035-correlated-chance-sampling-mccfr-2026-07-30.md
maturity: draft
created: 2026-07-28
updated: 2026-07-30
---

## Relations

- @sources/arxiv-2607.27035-correlated-chance-sampling-mccfr-2026-07-30.md — CCS-MCCFR

- @sources/arxiv-2607.23333-swap-regret-attention.md
- @concepts/code-as-agent-harness.md
- @concepts/verifier-deployment-gap.md

## Raw Concept

Can a minimal attention net implement no-regret / no-swap-regret updates for HU poker decide()?

## Narrative

arXiv 2607.23333 shows single-layer attention + regret (or swap-regret) loss can realize smoothed fictitious play / Blum–Mansour-style updates, inducing CCE vs CE asymptotics. For Poker Arena: useful as a **theory steal** for MAFP / regret-matching lanes — not a drop-in model. Pair with external yardsticks (play-adequacy, verifier–deployment gap) so self-trained regret losses cannot self-grade promotions.
