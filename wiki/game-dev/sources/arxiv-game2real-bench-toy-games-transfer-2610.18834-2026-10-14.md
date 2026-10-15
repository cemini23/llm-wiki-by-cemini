---
title: "Game2Real-Bench — Do Toy Games Reveal and Transfer to Real-World Visual Reasoning?"
type: source
tags: [arxiv, benchmark, visual-reasoning, vlm, transfer]
keywords: [procedural games, real-world transfer, in-context learning, constraint reasoning, fine-grained perception]
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

Title: Game2Real-Bench — Do Toy Games Reveal and Transfer to Real-World Visual Reasoning?
Authors: Qingan Liu, Juntong Feng, Yue Zhu et al. (Dalian University of Technology, NTU)
Type: arXiv preprint (2610.18834)
Location: `research to be indexed/game-dev/arxiv-2610.18834-game2real-bench-do-toy-games-reveal-and-transfer.pdf`
Retrieved: 2026-10-14
Read status: read

## Narrative

**The question:** do abilities measured in procedurally generated toy games correspond to real-world visual reasoning, and do game examples help solve real-world tasks?

**The design:** 1,000 independently generated game samples with **programmatically verified** answers, plus 400 real-world samples, connected by **shared reasoning requirements** — visual evidence, spatial operations, constraints, state transitions — **not visual similarity**. Four capability groups: fine-grained perception, spatial reasoning, constraint reasoning, sequential planning. 25 VLMs evaluated.

**The result:** game and real-world performance track closely — **Pearson 0.935, Spearman 0.935**. One-shot in-context transfer is **capability-dependent**: **constraint reasoning improves** for several models, while **fine-grained perception consistently declines**.

**Why it is filed here:** the **capability-level** finding matters more than the headline correlation. A single aggregate "games transfer" verdict is not supported; the sign of transfer depends on which capability is measured.

## Snippets

> "Performance on game and real-world tasks shows consistent cross-setting trends, with a Pearson correlation of 0.935 and a Spearman correlation of 0.935." [Source: arxiv-2610.18834 p.1]

> "Constraint reasoning shows positive gains for several models, while fine-grained perception consistently declines with gam[e] ..." [Source: arxiv-2610.18834 p.1]

## Dead Ends

- Reading 0.935 as "toy games are a valid proxy". The correlation is between *scores*; the transfer experiment shows the effect differs by capability and is negative for perception.
