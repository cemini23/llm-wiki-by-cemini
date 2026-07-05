---
title: arXiv 2606.29932 — SAGA CivRealm long-horizon strategy agents — 2026-07-05
type: source
tags: [source, arxiv, llm, strategy, multi-agent, civrealm]
keywords: [saga, scene-graph, tool-augmented-planner, dual-horizon-feedback, freeciv]
related:
  - concepts/stronghold-2-ai-lords.md
  - concepts/rts-siege-ai-reference.md
  - concepts/game-ai-rl-augmentation-shelf.md
  - concepts/llm-npc-runtime-ai-shelf.md
  - concepts/agent-harness-castle-project.md
  - concepts/scope-tiers.md
  - sources/arxiv-2606.30092-starcraft-hrl-influence-maps-2026-06-30.md
  - sources/arxiv-2606.20210-augmenting-game-ai-drl-2026-06-20.md
  - sources/protocolbench-llm-multiagent-protocol-shelf-2026-06-24.md
  - sources/inbox-arxiv-reject-batch-2026-07-05.md
  - meta/cross-wiki-routing.md
read_status: read
source_type: research-paper
source_url: https://arxiv.org/abs/2606.29932
maturity: validated
created: 2026-07-05
updated: 2026-07-05
---

## Raw Concept

**SAGA** — LLM multi-agent framework for **long-horizon multi-domain strategy** on CivRealm/FreeCiv: (i) Map-Semantic **Scene Graph** for spatial grounding without global token dump; (ii) **Tool-Augmented Planner** with per-domain specialist controllers; (iii) **Dual-Horizon Feedback Loop** (within-game goals + cross-game causal post-mortem). SOTA mean civilization score vs five LLM baselines; −27% output tokens vs strongest baseline.

## Narrative

### Architecture [CONFIRMED — abstract]

| Mechanism | Problem addressed | castle-sim analog (Tier 3+ / Phase E+) |
|-----------|-------------------|----------------------------------------|
| **Map-Semantic Scene Graph** | Raw tile coords → scene blindness | Typed relations among estates, walls, armies → per-lord local NL context |
| **Tool-Augmented Planner** | Monolithic 15k+ token state dumps | Pull economy/military/siege state on demand; dispatch to specialist submodules |
| **Dual-Horizon Feedback** | Sparse end-game reward only | In-match sub-goals (harass cadence, breach prep) + cross-match lord profile tuning |

### castle-sim mapping (STEAL-FROM — research shelf)

| Extract | Skip |
|---------|------|
| **Specialist controller decomposition** parallels `LordAIDirector` economy / harass / siege phases | Running FreeCiv/CivRealm benchmark harness |
| **Scene graph** pattern for spatial grounding in lord prompts (estates, breach points) | Replacing JSON `lord_profiles.json` with cloud LLM at Tier 2 |
| **Cross-episode strategic prior** as design doc for lord personality evolution (Tier 3+) | Training or API spend on hobby vertical slice |

**Verdict:** **STEAL-FROM (research shelf)** — gitignored `briefs/research/saga-civrealm-strategy-agent-shelf.md`. v0–v2: hand-coded SH2 lord cycles; Tier 3+ optional LLM lord director research only.

**Cross-wiki:** Multi-agent orchestration primitives → @ccc-wiki stub if harness patterns extracted later (@sources/protocolbench-llm-multiagent-protocol-shelf-2026-06-24.md).

**Repo:** `KazeCloud/SAGA-Civrealm` (~1★, no LICENSE listed 2026-07-05) — reference implementation only; no Phase-0.

## Dead Ends

- Porting SAGA to Godot for Kingmaker — API cost + non-determinism vs SH2 scripted lord authenticity target
- Conflating scene graph with influence maps — SAGA is NL relational grounding; @sources/arxiv-2606.30092-starcraft-hrl-influence-maps-2026-06-30.md is grid hashing for micro
