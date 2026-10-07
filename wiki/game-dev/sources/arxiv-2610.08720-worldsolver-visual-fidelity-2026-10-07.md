---
title: WorldSolver — visual fidelity as a verification signal for generated code (2026-10-07)
type: source
tags: [source, arxiv, harness, agents, benchmark, verification]
keywords: [worldsolver, solver-generation, visual-fidelity, physical-plausibility, scaffold-tasks]
related:
  - concepts/agent-harness-castle-project.md
  - sources/arxiv-2610.08215-learn2play-bench-experience-2026-10-07.md
  - entities/tools/gamedevbench.md
  - sources/arxiv-2609.40324-cogentic-proof-harness-2026-10-03.md
  - sources/inbox-arxiv-reject-batch-2026-10-07.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2610.08720
maturity: validated
created: 2026-10-07
updated: 2026-10-07
---

## Raw Concept

**arXiv:2610.08720** — **WorldSolver** [CONFIRMED], from NLPR & MAIS (CASIA), Peking University, and Huawei Noah's Ark Lab. A benchmark of **168 simulation tasks** [CONFIRMED] derived from physical phenomena in **61 classic computer graphics papers**, spanning **7 physical domains** [CONFIRMED]. Physics simulation is a testbed for LLM agents because it needs physical understanding, mathematical reasoning, and software engineering [CONFIRMED]. Each task ships a **code scaffold** that fixes the simulation environment, leaving the **solver implementation** for the agent to complete [CONFIRMED].

## Narrative

### Three evaluation dimensions [CONFIRMED]

The bench scores each solver on **Execution Checks** (does it run), **Visual Fidelity** (does the rendered simulation reproduce the intended dynamic behaviour), and **Physical Plausibility** (physics-grounded verification of the generated dynamics). Visual Fidelity uses a VLM judge over four criteria: event sequence, interaction response, signature phenomenon, and temporal coherence. Physical Plausibility runs hidden violation calculators over the state trajectory.

Headline results [CONFIRMED]. GPT-5.6-Sol leads at 48.7% overall, and Claude-Opus-5 follows at 46.7%. Gemini-3.7-Flash reaches 29.3%. DeepSeek-V4.1-Flash, GLM-5.3, Qwen-3.8-Max, and Kimi-K2.7-Code score 24.6%, 23.6%, 22.7%, and 17.1%. Producing an executable solver is hard. Satisfying visual and physical correctness is harder.

### What this wiki should take from it [CONFIRMED]

This page is here for the **evaluation design**, not the physics domain. Two transferable pieces.

1. **The scaffold-plus-completion task shape.** The bench hands the agent a fixed environment and a well-defined gap to fill. This is the story-brief shape the castle-sim W2 harness uses: fixed repo, one subsystem, one acceptance test.
2. **Visual fidelity as a verification dimension.** The agent-bench ladder here covers task completion (GameDevBench), tick-level logic asserts (GameLogicBench), deterministic UE checks (CraftBench-UE), and decision simulation (EnterpriseBench) — see @concepts/agent-harness-castle-project.md. None of them verifies that rendered output looks right. For a 3D castle sim, "does the scene render as intended" is a real acceptance axis, and a VLM or image-diff judge is the cheap way to automate it.

Cross-link @entities/tools/gamedevbench.md and @sources/arxiv-2610.08215-learn2play-bench-experience-2026-10-07.md.

### Caveat [TENTATIVE]

The domain is scientific and graphics-research simulation, not game development. The physics content does not transfer. Only the evaluation design does.

## Dead Ends

- Adopting this bench for castle-sim. The physics domain differs from game development.
- Assuming a passing execution check means correct behaviour. The paper shows solvers that run yet violate physical laws.
- Trusting visual fidelity alone. The paper shows visually correct solvers with wrong physics, and the reverse.
