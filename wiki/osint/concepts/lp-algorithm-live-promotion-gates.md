---
title: LP algorithm live promotion gates — DSR, markout, shadow, kill switch
type: concept
tags: [concept, liquidity-provision, validation, polymarket, cemini-internal, k76]
keywords: [LP-promotion, DSR, markout, MCPT, shadow-incubation, kill-switch, pm_lp_rewards]
related:
  - sources/quant-bot-lp-live-promotion-criteria-2026-05-28.md
  - concepts/brier-score-model-promotion-framework.md
  - concepts/monte-carlo-permutation-test-mcpt.md
  - concepts/regime-conditioned-evaluation.md
  - concepts/polymarket-lp-rewards-farming.md
  - concepts/shadow-to-live-transition-engineering.md
  - concepts/shadow-trading-telemetry-accumulation.md
  - concepts/pnl-attribution-versioning.md
  - concepts/polymarket-lp-bot-phase0-spec.md
  - sources/algorithmic-trading-model-benchmarking-framework-2026-05-28.md
  - sources/shadow-trading-data-accumulation-strategies-2026-05-28.md
maturity: validated
created: 2026-05-28
updated: 2026-05-29
---

## Relations

- @sources/quant-bot-lp-live-promotion-criteria-2026-05-28.md — primary source
- @concepts/brier-score-model-promotion-framework.md — Brier/BSS + calibration pillar (K77)
- @concepts/monte-carlo-permutation-test-mcpt.md — MCPT pillar
- @concepts/shadow-trading-telemetry-accumulation.md — dual-track shadow data (K77)
- @concepts/regime-conditioned-evaluation.md — DSR / multiple-testing overlap
- @concepts/polymarket-lp-rewards-farming.md — Cemini LP workstream
- @concepts/shadow-to-live-transition-engineering.md — shadow incubation mechanics
- @concepts/pnl-attribution-versioning.md — `pm_lp_rewards` version bump at promotion
- @concepts/polymarket-lp-bot-phase0-spec.md — Phase-0 spec alignment

## Raw Concept

Checklist for promoting **liquidity provision** bots (especially Cemini `pm_lp_rewards`) from research/hold → shadow → live. Synthesized from K76 quant LP promotion source + existing MCPT concept.

## Narrative

### GO gate stack (all required)

| Gate | What | Cemini artifact |
|------|------|-----------------|
| **1. DSR** | Deflated Sharpe after N trials / non-normality | Research notebook + trial count logged |
| **2. MCPT** | Permutation p-value on true vs shuffled paths | @concepts/monte-carlo-permutation-test-mcpt.md |
| **3. Markout** | Short (10–50ms) + mid (1–5s) realized spread | Shadow fill analytics |
| **4. Shadow PnL floor** | Net positive after fees + infra cost model | Shadow window report |
| **5. MDD / ES** | Peak-to-trough + tail loss bound | Risk governor limits |
| **6. Kill switch** | Out-of-loop halt tested | `risk_governor` / panic paths |
| **7. Brier / calibration** | BSS > 0 OOS; reliability bins within tolerance | @concepts/brier-score-model-promotion-framework.md |

`[NEEDS VERIFICATION 2026-05-28]` Exact numeric DSR/markout thresholds in source DOCX were truncated in extract — **define operator thresholds in prod config**, do not copy placeholder numbers from synthesis doc.

### Shadow incubation

- Live ticks, suppressed or sim-matched orders.
- Minimum hours/days + must include high-volatility session.
- Incumbent vs candidate comparison before capital switch.

### Live cutover

1. Bump `pm_lp_*` in strategy registry (K75 SOP).
2. Start at reduced size cap.
3. Monitor markout + message-rate kill switch for first 24h.

## Snippets

> "Positive shadow PnL is necessary but entirely insufficient for promotion." [Source: quant-bot-lp-live-promotion-criteria-2026-05-28.docx]

> "Kill switch must operate entirely outside of the strategy's core logic loop." [Source: quant-bot-lp-live-promotion-criteria-2026-05-28.docx]
