---
title: K284 arXiv Wave — game solving, agent memory, verification (Oct 2026)
type: concept
tags: [k284, arxiv, game-theory, poker, agents, memory, verification, options]
keywords: [k284, cgmy, bluffjax, recursive-game-creator, in-parameter-memory, worldsolver, compaction, verifine, fictitious-play]
related:
  - concepts/k284-eval-wave.md
  - concepts/k284-feeds-wave.md
  - concepts/k283-arxiv-wave.md
  - concepts/agent-tool-use-verification.md
  - entities/tools/bluffjax.md
  - sources/arxiv-2610.07554-bspline-galerkin-cgmy-2026-10-07.md
  - sources/arxiv-2610.07686-bluffjax-2026-10-07.md
  - sources/arxiv-2610.08621-recursive-game-creator-2026-10-07.md
  - sources/arxiv-2610.08630-in-parameter-memory-survey-2026-10-07.md
  - sources/arxiv-2610.08720-worldsolver-2026-10-07.md
  - sources/arxiv-2610.08722-compaction-harm-prediction-2026-10-07.md
  - sources/arxiv-2610.08761-verifine-2026-10-07.md
  - sources/arxiv-2610.08768-slow-fictitious-play-2026-10-07.md
maturity: draft
created: 2026-10-07
updated: 2026-10-07
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k284-eval-wave.md
- @concepts/k283-arxiv-wave.md
- @concepts/agent-tool-use-verification.md
- @sources/arxiv-2610.08761-verifine-2026-10-07.md

## Raw Concept

K284 arXiv cluster hub. **8 papers.** Dual-ID **OSINT K284**. Split: **1 quant**, **2 game theory/poker**, **5 agent tooling/memory/verification**.

## Narrative

### Quant (1)

**`2610.07554` — B-spline Galerkin for CGMY.** A deterministic high-order solver for the tempered-stable CGMY jump process. Cardinal B-spline basis → **exactly Toeplitz** connection matrices → **O(N log N) matvec via FFT**; spatial rate O(h^{p−Y/2}); projected-SOR LCP for American puts. **S&P 500 calibration: IV RMSE 2.47 / 1.97 vp.** An alternative to Monte-Carlo/COS when fat tails matter. **No trade; no scp.**

### Game theory / poker (2)

- **`2610.07686` — BluffJAX (MIT).** JAX-native suite of **10 imperfect-information games** (Kuhn, Leduc, Hold'em, 7-Card Stud, Werewolf, …) with a **JIT-compatible CFR**. Scales to **~2×10⁷ samples/s** at 10,000 parallel envs. The GPU-accelerated poker RL environment the poker lane can build on.
- **`2610.08768` — Arbitrarily slow fictitious play.** Constructs zero-sum games where FP converges at **Θ(t^{−1/k})** for every k — **counterexamples to Karlin's O(t^{−1/2}) conjecture.** No universal convergence exponent. A worst-case lower bound to cite against "fast convergence" claims.

### Agent tooling / memory / verification (5)

- **`2610.08621` — Recursive Game Creator.** Four-role agent harness (Designer / Builder / **Coding-Native Player** / Reviewer) refining a Godot game from prototype to product-level. GameCraft-Bench **72.70 → 77.89**. The reusable trick: **play-test in code, not via GUI rollouts.**
- **`2610.08720` — WorldSolver.** 168 physics-solver-generation tasks. Frontier agents struggle: **GPT-5.6-Sol 48.7%, Claude-Opus-5 46.7%.**
- **`2610.08722` — Compaction harm.** Does history predict when compaction hurts? **A modest, bounded signal** (AUROC 0.66; a wide null on placement). A calibrated negative result.
- **`2610.08761` — VeriFine (NVIDIA).** Co-evolves policy, curriculum, and judge. Driving reasoning **60.56 → 71.61 (+18.2%)**; **judge–human Pearson 0.53 → 0.82.** The judge improves with scale.
- **`2610.08630` — In-Parameter Memory survey.** Gives a taxonomy (placement × acquisition time) and a **scope rule** for what counts as IPM.

### The thread

Four of the five agent papers concern **building trust in agent output** — game feel (Recursive Game Creator), physical plausibility (WorldSolver), compaction safety (trace corpus), and judge calibration (VeriFine). **VeriFine pairs with the K283 CLIFT result** (@sources/arxiv-2610.06829-clift-web-agent-verification-2026-10-06.md): both scale verification separately from the generator.

### Boundary

**FILE only. No install. No clone.** The two game-theory papers are the desk-relevant extracts (poker lane). The agent papers route to CCC/cyber.

### Distribution

- Poker/game-theory (BluffJAX, slow FP) → `../Gambling wiki/briefs/2026-10-07_k284-game-solving.md`
- Agent memory/verification (VeriFine, compaction, IPM, Recursive Game Creator, WorldSolver) → `../Cemini claude code CCC/briefs/2026-10-07_k284-agent-verification-memory.md`
- Game-dev (Recursive Game Creator, WorldSolver) → `../Game Dev wiki/briefs/2026-10-07_k284-agentic-game-generation.md`
