---
title: Augmenting Game AI with Deep RL (EA vision paper) — 2026-06-20
type: source
tags: [source, arxiv, game-ai, reinforcement-learning, ea]
keywords: [rl, game-ai, behavior-tree, goap, fsm, production]
related:
  - concepts/game-ai-rl-augmentation-shelf.md
  - concepts/rts-siege-ai-reference.md
  - concepts/stronghold-2-ai-lords.md
  - concepts/stronghold-crusader-ai-modding-shelf.md
  - meta/cross-wiki-routing.md
  - concepts/agent-harness-castle-project.md
  - sources/inbox-arxiv-reject-batch-2026-06-20.md
  - entities/projects/castle-sim.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2606.20210
maturity: validated
created: 2026-06-20
updated: 2026-06-20
---

## Raw Concept

**arXiv:2606.20210** — EA Stockholm vision paper (IEEE CoG 2026 proceedings id). Argues RL should **augment** hand-coded game AI (FSM/BT/GOAP), not replace it. Case studies: EA SPORTS FC 25 goalkeeper positioning (SAC); Battlefield 6 infantry locomotion (PPO + occupancy maps).

## Narrative

### Production requirements (Section I) [CONFIRMED]

| Requirement | Meaning for castle-sim |
|-------------|----------------------|
| Short training time | Overnight retrain when sim changes — impractical for hobby solo; **defer RL** |
| Controllability | Designers need qualitative behavior control — **LordProfile JSON + BT director** |
| Modularity | RL as **leaf node** in BT/GOAP, not end-to-end — matches `LordAIDirector` stub |
| Maintainability | Hand-coded core survives patches — JSON lord profiles editable |
| Bug detection/fixing | Fine-tune sub-policies in hours post-ship — N/A hobby |
| Authenticity | **Human-like > superhuman** — Kingmaker PvE, not AlphaStar |
| Runtime inference | µs budgets on console — Godot Phase E must stay lightweight |

### Hand-coded baseline (Section II) [CONFIRMED]

- **FSM** — SH2 lord phases (natural / siege / defence) map cleanly
- **BT** — modular selectors; Crusader AIC study target
- **GOAP** — planner cost grows with action count; castle-sim uses **weighted director** instead

### EA case takeaways [CONFIRMED]

**Goalkeeper (FC 25):** SAC on real game sim; 4-day → 12h training via offline data + scenario training; **170µs** MLP inference; +10% save rate vs FSM; designers tune via **reward function** not state graph edits.

**Battlefield locomotion:** PPO; occupancy map beats 24-raycasts (2× faster obs); RL leaf in BT won 11/20 vs hand-coded; **authenticity** over raw win rate.

### Research gaps cited [TENTATIVE — shelf for Phase E+]

- Designers-in-the-loop reward authoring
- Small networks for real-time inference
- Fine-tuning without catastrophic forgetting
- Efficient 3D perception (occupancy vs navmesh)
- Behavior evaluation frameworks for black-box policies

### castle-sim verdict

**STEAL-FROM (architecture)** — Phase E LordAI: keep **JSON + FSM/BT director**; optional future RL **leaf** for locomotion or siege targeting only. **NO-GO** on shipping neural inference in vertical slice.

Cross-ref: @concepts/stronghold-crusader-ai-modding-shelf.md (`.aic` weights as design reference, not runtime).

## Snippets

```
feast_honour unrelated — paper focus is modular RL augmentation of BT/FSM/GOAP
Authenticity requirement: "goalkeeper should behave like a human professional"
```

## Dead Ends

- End-to-end RL lord (AlphaStar-style) — conflicts with controllability + solo dev scope
- Training in full Godot sim overnight — harness cost exceeds hobby ROI before Phase E ships
