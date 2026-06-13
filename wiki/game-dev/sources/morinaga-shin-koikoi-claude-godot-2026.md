---
title: morinaga — Shin KoiKoi shipped in 2 days with Claude + Godot (2026)
type: source
tags: [source, case-study, godot, claude, indie]
keywords: [hanafuda, godot, claude, itch-io, csharp]
related:
  - concepts/ai-assisted-game-dev-workflows.md
  - entities/engines/godot-4.md
read_status: read
source_type: blog
source_url: https://dev.to/morinaga/i-shipped-a-polished-hanafuda-card-game-in-2-days-with-claude-and-godot-5a7j
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Raw Concept

Solo dev ships polished **Shin KoiKoi** (Hanafuda) to itch.io — honest timeline breakdown.

## Narrative

### Stack [CONFIRMED]

| Area | Choice |
|------|--------|
| Engine | Godot 4.6.2 .NET (C#) |
| AI | Anthropic Claude (~70% UI scaffolding) |
| Art | Gemini / Midjourney — no characters (IP-safe) |
| Tests | 184 unit tests |
| Distribution | itch.io Mac/Win/Linux |

### Honest timeline

- **~3 weeks** pre-work: design notes, scope (Koi-Koi only, single-player)
- **2 days** active implementation
- **1 day** store polish, screenshots, i18n

### Collaboration model [CONFIRMED]

"Principal engineer with junior pair" — Claude needed direction at every architecture decision; typing/boilerplate near-instant.

### Gotchas documented

1. macOS universal export requires `import_etc2_astc=true` in project.godot
2. Font fallback order for CJK + Devanagari
3. Automated screenshot tour via C# state machine + `--screenshots` CLI flag
4. Oracle Cloud Always Free — deferred online multiplayer

### Accessibility

Shipped colorblind mode, UI scale, reduced motion, 6 languages, GDPR consent — cheaper upfront than retrofit.

## Snippets

Godot chosen over Unity: OSS, smaller binary, faster script-reload loop.
