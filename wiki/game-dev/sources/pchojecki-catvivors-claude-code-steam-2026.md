---
title: Przemek Chojecki — Catvivors solo dev with Claude Code (2026)
type: source
tags: [source, case-study, claude-code, godot, steam]
keywords: [catvivors, claude-code, solo-dev, steam, vampire-survivors]
related:
  - concepts/ai-assisted-game-dev-workflows.md
  - entities/engines/godot-4.md
read_status: read
source_type: blog
source_url: https://pchojecki.medium.com/ai-helped-me-solo-dev-a-game-on-steam-f84a2425be10
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Raw Concept

AI researcher ships **Catvivors** (Vampire Survivors-like roguelite) to Steam Early Access using **Claude Code** + **Godot**.

## Narrative

### Stack [CONFIRMED]

- Engine: Godot (open source)
- AI: Claude Code in terminal (~$20/mo vs local 32GB+ models)
- Blueprint: `readme.md` with mechanics, engine, tools

### Phases & timing

| Phase | Duration | Notes |
|-------|----------|-------|
| First prototype | Days | "Trash" — not fun, placeholder art |
| First **fun** level | **~2 weeks** | Hardest part — balance, movement, glitches |
| Content expansion | ~1 week | Levels, weapons, shop — fast after loop locked |
| Steam release prep | **~3 weeks** | Win/Mac/Linux builds, store page, waiting |

### Human-only responsibilities [CONFIRMED]

- **Playtesting for fun** — AI cannot judge engagement or frustration
- Complex art — basic AI sprites OK; premium art needs humans/asset packs

### Quote

> "AI is an incredibly powerful assistant, but it won't solve all your problems."

## Snippets

Workflow: markdown blueprint → iterate in engine with Claude Code → human playtest loop.
