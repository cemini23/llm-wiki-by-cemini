---
title: K268 Jev Trading Wave (Sep 2026)
type: concept
tags: [jev, trading, k268, typesafe, harness]
keywords: [System One, RLCD, AgenKit, HFT, market making]
related:
  - concepts/k268-harness-evolution-wave.md
  - concepts/k267-ccc-jev-wave.md
  - sources/jev-trading-research-paper-2026-09-21.md
  - entities/tools/jev-mcp.md
  - entities/tools/jev-trader.md
maturity: draft
created: 2026-09-21
updated: 2026-09-21
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k268-harness-evolution-wave.md
- @concepts/k267-ccc-jev-wave.md
- @sources/jev-trading-research-paper-2026-09-21.md
- @entities/tools/jev-mcp.md
- @entities/tools/jev-trader.md

## Raw Concept

K268 cluster hub for the TypeSafe **Jev Trading Research Paper** (8-page image PDF, vision OCR 2026-09-21).

## Narrative

Vendor field report on **deterministic-probabilistic split** for block-cadence market making: code owns state engine + Avellaneda–Stoikov + hard risk vetoes; **Jev System One** owns a six-question judgment battery (regime, direction, toxic flow, liquidity, quote env, inventory) with **RLCD**-calibrated confidence and fractional Kelly sizing. Build harness cited: **AgenKit** (`agenkit.xyz`).

**Cemini routing — FILE only:**
- **CCC / harness:** steal split-brain pattern (code vs typed judgment), confidence gating, fallback ladder — not AgenKit product Integrate.
- **GuruWatcher:** never auto-arm; vendor latency/cost claims are not GW levels.
- **jev-trader** (paper ref / `jarrodwatts/jev-trader` MIT) = named **live trading demo** — out of scope. No orders. No pm scp.
- **Atto:** unrelated; Transkribus sole HTR.

**0 product Integrate GO.** Live laptop path remains **jev-mcp**. Never `npx github:`.
