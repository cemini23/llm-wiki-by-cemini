---
title: Stronghold2-MP-AI Phase-0 audit — 2026-06-13
type: source
tags: [source, phase-0, stronghold-2, modding, audit]
keywords: [stronghold-2, multiplayer, ai, patch, signature]
related:
  - entities/tools/stronghold2-mp-ai-patch.md
  - concepts/stronghold-2-github-ecosystem-shelf.md
  - sources/github-stronghold-2-scan-2026-06-13.md
read_status: read
source_type: operator-audit
source_url: https://github.com/Jpnock/Stronghold2-MP-AI
maturity: validated
created: 2026-06-13
updated: 2026-06-16
---

## Raw Concept

Phase-0 audit of **Jpnock/Stronghold2-MP-AI** — MIT external patcher enabling AI opponents in SH2 multiplayer lobbies.

## Narrative

### Method

Clone to `/tmp/phase0-audit/Stronghold2-MP-AI`. Read `main.cpp`, `Signatures.h`, README. Compare fork **Przodownik/Stronghold2-MP-AI-Patch** (Proton offsets variant).

### Checks

| Gate | Result |
|------|--------|
| License | **MIT** [CONFIRMED] |
| Maturity | Last push 2024-10; ~13★; single-purpose tool |
| Mechanism | PID scan → signature match → 12× `0x90` NOP at MP-AI guard |
| Failure modes | Steam EXE update breaks signature; requires admin / `PROCESS_ALL_ACCESS` |
| castle-sim fit | **NO-GO** — retail research QoL only; greenfield AI is JSON-driven |

### Steal value

| Extract | Skip |
|---------|------|
| Version-tolerant byte signature + mask pattern | Shipping patcher in Godot repo |
| MP skirmish vs AI for lord behavior observation | Dependence on patch for sim development |
| Proton offset fork as cross-reference | Expecting Crusader-scale AIV injection |

### Verdict

**CONDITIONAL-GO** — run locally for operator playtest research; verify signature against current Steam EXE before relying. Install: gitignored `briefs/sh2-mp-ai-patch-install.md`.

## Snippets

Fork for Linux/Proton: Przodownik/Stronghold2-MP-AI-Patch — check ProtonDB + fork README before MP skirmish on Linux bottle.
