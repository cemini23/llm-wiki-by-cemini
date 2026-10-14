---
title: Evrey SHC_AIV — Phase-0 audit — 2026-06-19
type: source
tags: [source, phase-0, stronghold, crusader, modding, audit]
keywords: [aiv, evrey, crusader, skirmish]
related:
  - entities/tools/evrey-shc-aiv.md
  - entities/tools/unofficial-crusader-patch2.md
  - concepts/stronghold-crusader-ai-modding-shelf.md
  - concepts/stronghold-modding-ecosystem-shelf.md
  - sources/stronghold-franchise-research-pass2-2026-06-18.md
  - sources/krarilotus-efficient-ai-phase-0-audit-2026-06-19.md
read_status: read
source_type: operator-audit
source_url: https://github.com/Evrey/SHC_AIV
maturity: validated
created: 2026-06-19
updated: 2026-06-19
---

## Raw Concept

Phase-0 audit of **Evrey/SHC_AIV** — community replacement set for all 128 Crusader **`.aiv`** castle layouts (skirmish + history packs).

## Narrative

### Method

GitHub README + repo layout (2026-06-19). No clone required for audit — distribution is binary AIV files + docs.

### Checks

| Gate | Result |
|------|--------|
| License | **None declared** on repo — study layouts only; do not redistribute AIV in castle-sim |
| Maturity | Long-running community standard; skirmish + history packs; `firefly_fixed/` bugfix variant |
| Mechanism | Replace `Stronghold Crusader Extreme/aiv/` files (128 slots, 8 per lord × 16 lords) |
| castle-sim fit | **STEAL-FROM (layout)** — transcribe build-order patterns → `castle_templates/*.json` |
| UCP synergy | Works with UCP2 balance; pair with Krarilotus AIC for behaviour |

### Steal value

| Extract | Skip |
|---------|------|
| Per-lord castle diversity (8 layouts) | Shipping `.aiv` binaries |
| Economic building early-order (granary/hovel priority) | Runtime Crusader dependency |
| History vs skirmish pack split | Expecting 1:1 SH2 `.s2m` format |

### Verdict

**STEAL-FROM (design)** — gold-standard AIV quality bar for lord castle templates. Operator brief: `briefs/research/crusader-aiv-study-loop.md`.

## Dead Ends

- Phase-0 clone for SPDX — none; audit is distribution + README only
