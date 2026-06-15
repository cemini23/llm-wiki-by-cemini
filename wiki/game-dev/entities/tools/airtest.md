---
title: Airtest — image-based UI automation (Adopt → CCC)
type: entity
tags: [entity, tool, automation, testing, cross-wiki]
keywords: [airtest, netease, image-recognition, ui-test]
related:
  - concepts/tool-evaluation-cross-wiki-batch-2026-06-13.md
  - concepts/ai-game-dev-tool-stack-2026.md
  - entities/tools/godot-stagehand.md
  - entities/tools/serpent-ai.md
  - sources/tool-evaluation-cross-wiki-routing-2026-06-13.md
  - sources/airtest-phase-0-audit-2026-06-13.md
maturity: validated
created: 2026-06-13
updated: 2026-06-13
cross-wiki-primary: @ccc-wiki
---

## Relations

- @ccc-wiki — **primary install surface** (lazy-tool / playwright-fallback complement)
- @cybersecurity-wiki/concepts/mcp-security-posture.md — before wiring into agent loops

## Raw Concept

[`AirtestProject/Airtest`](https://github.com/AirtestProject/Airtest) — Apache-2.0 Python UI automation via **image recognition** (NetEase Games ecosystem).

## Narrative

### What it does [CONFIRMED — eval]

- Locate UI elements by template matching / OCR
- Cross-platform scripted interaction without engine hooks
- Pairs with Poco for hierarchy when available

### Eval verdict (2026-06-13 batch)

| Surface | Tier |
|---------|------|
| @ccc-wiki | **Adopt** — fill visual UI gap for non-DOM apps |
| game-dev-wiki | **Stub** — reference for Godot/Unity Phase-0 UI audit methodology |

### vs castle-sim W2 stack

| Tool | Mechanism | Default |
|------|-----------|---------|
| godot-stagehand | Godot-native external driver | **Preferred** for castle-sim CI |
| Airtest | Screen template matching | Fallback for editor chrome / non-Godot UIs |
| SerpentAI | Legacy pixel agent env | Steal patterns only |

### Adoption bar

1. Phase-0 complete — @sources/airtest-phase-0-audit-2026-06-13.md
2. Sandbox project on @ccc-wiki — not castle-sim default
3. Document image template maintenance cost (brittle on res changes)

### Phase-0 audit (2026-06-13)

| Check | Result |
|-------|--------|
| License | Apache-2.0 |
| Activity | Active (v1.4.3 area, Dec 2025) |
| castle-sim | **NO-GO primary** — use godot-stagehand for in-engine CI |
| @ccc-wiki | **CONDITIONAL-GO** |

| Verdict | **CONDITIONAL-GO** (CCC) / stub here |

## Snippets

Use case sketch for engine eval:

```
# Pseudocode — not production
touch(Template("play_button.png"))
assert_exists(Template("fps_overlay.png"))
```

## Dead Ends

- Replacing godot-stagehand for in-engine regression — wrong layer; Airtest is screen-space
