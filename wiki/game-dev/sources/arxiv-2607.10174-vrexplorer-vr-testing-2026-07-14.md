---
title: arXiv 2607.10174 — VRExplorer model-based VR scene testing — 2026-07-14
type: source
tags: [source, arxiv, playtest, unity, vr, automation, phase-0]
keywords: [vrexplorer, eat-framework, navmesh, pfsm, ase-2025]
related:
  - sources/vrexplorer-phase-0-audit-2026-07-14.md
  - entities/tools/vrexplorer.md
  - entities/tools/godot-ai-playtest.md
  - entities/tools/godot-stagehand.md
  - concepts/ai-game-dev-tool-stack-2026.md
  - concepts/godot-stagehand-ci-smoke-plan.md
  - sources/inbox-arxiv-reject-batch-2026-07-14.md
  - meta/cross-wiki-routing.md
read_status: read
source_type: research-paper
source_url: https://arxiv.org/abs/2607.10174
maturity: validated
created: 2026-07-14
updated: 2026-07-14
---

## Raw Concept

**VRExplorer** (ASE 2025) — model-based semi-automated testing for **Unity VR** scenes. **EAT** (Entity / Action / Task) interaction model + agent that explores via Unity **NavMesh** pathfinding and executes interactions through a **Probabilistic Finite State Machine (PFSM)**. Eval on 11 VR projects; beats VRGuide on ELOC/method coverage. Repo: `TsingPig/VRExplorer` (~11★, ~272 MB shallow clone). Package install via `VRExplorer_Release` git URL.

## Narrative

### Architecture [CONFIRMED — abstract + README]

| Component | Role |
|-----------|------|
| **EAT framework** | Generic VR interaction model (entity + action + task) |
| **NavMesh explorer** | Locomotion through reachable 3D scene after Navigation Static bake |
| **PFSM** | Probabilistic action selection for object interactions |
| **Unity package** | Prefab agent + interface hooks under `Package/EAT Framework` |

### castle-sim / W2 mapping (STEAL-FROM — research shelf)

| Extract | Skip |
|---------|------|
| **EAT-style interaction inventory** for playtest coverage (what can the agent touch?) | Unity VR package adoption |
| **Model-based scene exploration** contrast vs Stagehand / godot-ai-playtest TCP control | Replacing Godot CI with Unity NavMesh |
| PFSM as optional policy for non-deterministic smoke (explore breadth) | Shipping VR headset test harness |

Cross-ref: @entities/tools/godot-stagehand.md, @entities/tools/godot-ai-playtest.md, @concepts/godot-stagehand-ci-smoke-plan.md.

**Verdict:** **STEAL-FROM (research)** — see Phase-0 @sources/vrexplorer-phase-0-audit-2026-07-14.md (**NO-GO adopt**). Brief: gitignored `briefs/research/vrexplorer-model-based-playtest-shelf.md`.

## Dead Ends

- Adopting VRExplorer into castle-sim — wrong engine (Unity), wrong domain (VR), **no SPDX license** on GitHub
- Treating NavMesh VR exploration as substitute for Godot Stagehand L0/L1 smoke on `game_3d.tscn`
