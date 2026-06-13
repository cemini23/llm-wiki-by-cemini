---
title: BigDevSoon — Void Balls AI stack shipped in 10 days (2025)
type: source
tags: [source, case-study, unity, multi-agent, ai-art]
keywords: [void-balls, unity, claude-code, replicate, elevenlabs]
related:
  - concepts/ai-assisted-game-dev-workflows.md
  - concepts/ai-game-dev-tool-stack-2026.md
read_status: read
source_type: blog
source_url: https://bigdevsoon.me/blog/building-games-with-ai-indie-game-dev-workflow/
maturity: tentative
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- @image-gen-wiki — Replicate/Flux art lane cross-ref

## Raw Concept

**Void Balls** 2D roguelite — ~29k LOC C#, 173 scripts, 88 test files, built in **10 days** with multi-agent Claude Code + generative media stack.

## Narrative

### AI toolkit [TENTATIVE — marketing blog]

| Layer | Tool | Role |
|-------|------|------|
| Code | Claude Code Opus — **8 parallel agents** | Architecture, implementation, balance, tests |
| Engine bridge | Unity 6 + **Unity MCP** | Scene inspect, runtime debug, prefabs |
| Art | Replicate (Flux 2D, Recraft) | Sprites, backgrounds — **7-color palette constraint** |
| Audio | ElevenLabs | 9 SFX, 3 music tracks |
| Trailer | CapCut | Marketing |

### Metrics claimed

173 production scripts, 88 test files, 15 power-up cards, 5 enemy types, ~$50/mo AI stack cost.

### Lessons [CONFIRMED narrative]

- AI **amplifies** design vision — does not replace taste
- **Constraints create cohesion** (palette, two-button controls)
- Tests critical when AI refactors at speed
- Stack orchestration is the human skill

### castle-sim relevance

Unity-specific but patterns transfer: parallel agents by domain, MCP for engine visibility, strict visual constraints → route art to @image-gen-wiki.

## Dead Ends

- 10-day claim is studio workflow marketing — treat metrics as [TENTATIVE] until independent verify
