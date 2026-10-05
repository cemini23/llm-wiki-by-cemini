---
title: Game AI — RL augmentation shelf (deferred Phase E+)
type: concept
tags: [concept, game-ai, reinforcement-learning, deferred, reference]
keywords: [rl, behavior-tree, goap, fsm, lord-ai, ea]
related:
  - sources/arxiv-2606.20210-augmenting-game-ai-drl-2026-06-20.md
  - concepts/rts-siege-ai-reference.md
  - concepts/stronghold-2-ai-lords.md
  - concepts/stronghold-crusader-ai-modding-shelf.md
  - concepts/agent-harness-castle-project.md
  - concepts/scope-tiers.md
  - entities/projects/castle-sim.md
  - sources/inbox-arxiv-reject-batch-2026-06-29.md
  - sources/arxiv-2606.30092-starcraft-hrl-influence-maps-2026-06-30.md
  - sources/arxiv-2606.29932-saga-civrealm-strategy-agents-2026-07-05.md
  - sources/arxiv-2609.29228-bt-fsm-llm-conversion-2026-09-30.md
  - sources/arxiv-2609.34214-glyphbench-rl-playground-2026-09-30.md
  - sources/arxiv-2609.34342-sage-strategic-reasoning-2026-09-30.md
  - sources/arxiv-2609.37658-enterprisebench-strategic-agents-2026-09-30.md
  - sources/arxiv-2610.03695-queen-chess-explains-moves-2026-10-05.md
maturity: validated
created: 2026-06-20
updated: 2026-06-30
---

## Relations

- @sources/arxiv-2606.20210-augmenting-game-ai-drl-2026-06-20.md — EA production vision (2026)
- @concepts/stronghold-2-ai-lords.md — hand-coded lord personalities today

## Raw Concept

Shelf for **modular RL-augmented game AI** — RL replaces specific BT/FSM **leaves**, not whole lord brains. Deferred until castle-sim Phase E lord director is stable on JSON/GOAP-style weights.

## Narrative

### Architecture pattern [CONFIRMED — EA paper]

```
Hand-coded director (FSM/BT/GOAP)
  ├── harass raid (scripted weights)     ← castle-sim Phase E v1
  ├── siege composition (tables)         ← Phase E v1
  └── locomotion / micro leaf (RL?)      ← Phase E+ optional
```

**Rule:** Authenticity > superhuman. Kingmaker clone targets believable harass, not optimal StarCraft micro.

### castle-sim mapping

| EA lesson | Godot target |
|-----------|--------------|
| Modular leaf policies | `LordAIDirector` submodules per phase |
| Reward = designer language | `lord_profiles.json` tunable weights (no NN) |
| Occupancy vs navmesh | Flow-field / navmesh hybrid already planned |
| Overnight retrain | **Skip** — JSON hot-reload instead |
| µs inference budget | Pure GDScript director for slice |

### When to revisit RL

- After Phase E JSON lords pass playtest parity
- If operator wants **learned siege targeting** on fixed scenario set
- If `@ccc-wiki` harness adds automated scenario RL loop (Trainee-to-Trainer defer)

### Related hand-coded north stars

| Reference | Use |
|-----------|-----|
| Crusader `.aic` + UCP | Weight categories for director |
| SH2 Fandom lord tables | `@concepts/stronghold-2-ai-lords.md` |
| TW GDC siege roles | `@concepts/rts-siege-ai-reference.md` |

### Expert-plus-explainer split (2026-10-05) [TENTATIVE]

QUEEN pairs a **silent expert encoder** (a chess network) with a language model trained only to interpret the expert's state and explain it — reaching grandmaster play and fluent explanations with a 4B model. The transferable shape for castle-sim is the **split**: the hand-coded director stays the decision-maker, and any language model is an explainer over the director's state. That gives readable play plus readable reasons without handing decisions to an LLM.

The prerequisite is a strong expert to interpret, which the JSON lord director is not yet. Phase E+ note, not a W2 action. See @sources/arxiv-2610.03695-queen-chess-explains-moves-2026-10-05.md.

## Dead Ends

- Replacing `lord_profiles.json` with end-to-end RL before hand-coded baseline ships
- Behavioral cloning from retail SH2 replays — no dataset pipeline
