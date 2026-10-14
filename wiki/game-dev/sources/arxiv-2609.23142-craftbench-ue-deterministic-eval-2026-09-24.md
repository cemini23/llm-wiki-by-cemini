---
title: CraftBench-UE — deterministic UE agent eval harness (2026-09-24)
type: source
tags: [source, arxiv, benchmark, unreal, harness, steal-from]
keywords: [craftbench-ue, unreal-engine, deterministic-eval, coding-agents]
related:
  - entities/tools/craftbench-ue.md
  - sources/arxiv-2607.03525-gameenginebench-harness-2026-08-15.md
  - entities/tools/gamedevbench.md
  - concepts/agent-harness-castle-project.md
  - sources/inbox-arxiv-reject-batch-2026-09-24.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2609.23142
maturity: validated
created: 2026-09-24
updated: 2026-09-24
---

## Raw Concept

**arXiv:2609.23142** — CraftBench-UE runs agents in isolated **Unreal Engine** projects, reconstructs submissions, applies **deterministic** build/asset/runtime checks (no LLM judge). **70 tasks** spanning C++, Blueprints, assets. Repo: [ramenvr/craftbench-ue](https://github.com/ramenvr/craftbench-ue) — **MIT**.

## Narrative

### Steal (Godot / castle-sim) [CONFIRMED]

Fork B is Godot — do **not** adopt UE harness. Steal:

- Fresh-project reconstruction of agent patches
- Deterministic compile + runtime checks without LLM judge
- Task taxonomy spanning code **and** serialized assets (contrast @sources/arxiv-2609.27585-unity-insight-code-asset-index-2026-09-24.md for Unity)

### Phase-0 (2026-09-24)

| Check | Result |
|-------|--------|
| License | **MIT** [CONFIRMED — gh api] |
| Engine | UE only |
| Verdict | **CONDITIONAL-GO (reference clone)** — extract-only for harness design; **NO-GO** wire into castle-sim runtime |

## Dead Ends

- Running CraftBench-UE against castle-sim Godot repo
- Treating MIT UE bench as substitute for GameDevBench Godot tasks
