---
title: SerpentAI — visual game automation (steal-from)
type: entity
tags: [entity, tool, automation, computer-vision, steal-from]
keywords: [serpentai, visual, pixel, automation, dormant]
related:
  - concepts/tool-evaluation-cross-wiki-batch-2026-06-13.md
  - concepts/ai-game-dev-tool-stack-2026.md
  - entities/tools/godot-stagehand.md
  - entities/tools/airtest.md
  - sources/tool-evaluation-cross-wiki-routing-2026-06-13.md
  - sources/serpent-ai-phase-0-audit-2026-06-13.md
maturity: validated
created: 2026-06-13
updated: 2026-06-13
cross-wiki-primary: @ccc-wiki
---

## Relations

- @ccc-wiki — primary home for lazy-tool / visual assertion integration stub
- @cybersecurity-wiki — defensive analysis of client-side visual automation

## Raw Concept

[`SerpentAI/SerpentAI`](https://github.com/SerpentAI/SerpentAI) — MIT Python framework for **pixel-based game automation** without memory hooks (~7k★ historical).

## Narrative

### What it does [CONFIRMED — repo README + eval]

- Screen capture → visual state parsing → agent actions
- Decoupled from game internals — works on closed-source titles
- Python 3.8+ plugin architecture for game environments

### Maturity [TENTATIVE — gh api 2026-06-13]

| Signal | Value |
|--------|-------|
| Last push | 2022-11-07 |
| Community | Revival attempt ~2020; largely **dormant** |
| License | MIT [CONFIRMED] |

### Posture for game-dev-wiki

| Use | Verdict |
|-----|---------|
| Full install for castle-sim CI | **NO-GO** — dormant deps; prefer @entities/tools/godot-stagehand.md |
| Steal visual-parsing coordination patterns | **GO** — compare with Airtest image-match loop |
| Memory-hook alternative study | **GO** — reference for closed-engine automation theory |

### vs Airtest

Airtest (NetEase, Apache-2.0) is the **active** image-recognition stack — @entities/tools/airtest.md. SerpentAI is historical reference for agent-environment decoupling.

### Phase-0 audit (2026-06-13)

| Check | Result |
|-------|--------|
| License | MIT |
| Last meaningful commit | 2020-05-22 |
| Install | **NO-GO** — dormant; heavy ML/CEF optional deps |
| Steal | Game environment plugin interface only |
| Audit | @sources/serpent-ai-phase-0-audit-2026-06-13.md |

| Verdict | **STEAL-FROM / NO-GO install** |

Steal checklist:

```
[ ] Environment plugin interface (observe → act loop)
[ ] Frame differencing / region-of-interest patterns
[ ] Do NOT copy Python 2/3 legacy env adapters verbatim
```

## Dead Ends

- Production dependency on SerpentAI for W2 — repo inactive; use godot-stagehand + Airtest patterns instead
