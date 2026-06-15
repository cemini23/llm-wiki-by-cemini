---
title: Stronghold2-MP-AI — multiplayer AI patch (MIT)
type: entity
tags: [entity, tool, stronghold-2, modding, steal-from]
keywords: [stronghold-2, multiplayer, ai, patch, mit]
related:
  - concepts/stronghold-2-github-ecosystem-shelf.md
  - concepts/stronghold-2-systems-inventory.md
  - concepts/operator-vision-sh2-personal-clone.md
  - sources/github-stronghold-2-scan-2026-06-13.md
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- @concepts/stronghold-2-github-ecosystem-shelf.md — sibling SH2 tools

## Raw Concept

[`Jpnock/Stronghold2-MP-AI`](https://github.com/Jpnock/Stronghold2-MP-AI) — external C++ tool that **NOP-patches** Stronghold 2 at runtime to enable **AI opponents in multiplayer** lobbies. MIT license.

## Narrative

### Mechanism [CONFIRMED — main.cpp + Signatures.h]

1. Operator provides `Stronghold2.exe` PID
2. Scans main module for byte signature (`szMPAIFuncSig` / mask)
3. Writes **12 NOP bytes** (`0x90`) at match — disables “AI off in MP” guard
4. Requires admin / `PROCESS_ALL_ACCESS`

Fork: [Przodownik/Stronghold2-MP-AI-Patch](https://github.com/Przodownik/Stronghold2-MP-AI-Patch) (also MIT).

### Value for operator / clone research

| Use | Notes |
|-----|-------|
| **Play MP skirmish vs AI** while taking playtest notes | Primary operator QoL |
| Pattern-scan patching | Version-tolerant vs hardcoded offsets |
| AI behavior observation | Observe SH2 lord AI in skirmish — informs Phase D `@concepts/rts-siege-ai-reference` |

### castle-sim boundary

- **Do not** ship patcher inside Godot repo
- **Do not** depend on patch for sim development — greenfield AI is JSON-driven
- OK to document install steps in gitignored `briefs/` for local retail setup

### Phase-0 verdict

**CONDITIONAL-GO** — run locally for research; verify signature still matches current Steam EXE before relying on it.

## Snippets

```
Stars: ~13 | Language: C++ | License: MIT
```

## Dead Ends

- Expecting Crusader-grade AIV injection — this only **unlocks** built-in MP AI flag
