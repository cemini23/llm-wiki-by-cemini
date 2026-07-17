---
title: "Cemini — PM LP vs copy capital decision (K165 synthesis)"
type: concept
tags: [concept, polymarket, capital-allocation, lp-rewards, copy-trading, hyperliquid, k165]
keywords: [capital-decision, kill-switch, empirical-kill, daleep, hlp-conflict]
related:
  - sources/gemini-dr-pm-lp-vs-copy-trading-2026-07-14.md
  - sources/gemini-dr-pm-trading-strategies-capital-2026-07-14.md
  - sources/gemini-dr-pm-hl-strategies-2026-07-14.md
  - concepts/polymarket-copy-trading-strategy.md
  - concepts/polymarket-lp-rewards-farming.md
  - concepts/polymarket-lp-bot-phase0-spec.md
  - concepts/polymarket-lp-comprehensive-backtest.md
  - concepts/hyperliquid-hlp-vs-user-vaults.md
  - entities/tools/oracle3.md
  - entities/tools/cryptuon-polybot.md
  - entities/tools/oddpool.md
  - entities/tools/polymarket-quotebot.md
maturity: draft
created: 2026-07-14
updated: 2026-07-16
clusters: [polymarket]
---

## Relations

- @sources/gemini-dr-pm-lp-vs-copy-trading-2026-07-14.md
- @sources/gemini-dr-pm-trading-strategies-capital-2026-07-14.md
- @sources/gemini-dr-pm-hl-strategies-2026-07-14.md
- @concepts/polymarket-copy-trading-strategy.md
- @concepts/polymarket-lp-rewards-farming.md
- @concepts/polymarket-lp-bot-phase0-spec.md
- @concepts/polymarket-lp-comprehensive-backtest.md — v2 backtest is the restart gate
- @concepts/hyperliquid-hlp-vs-user-vaults.md
- @entities/tools/oracle3.md — Phase-0 pending INTEGRATE stub
- @entities/tools/cryptuon-polybot.md — ≠ ent0n29/polybot
- @entities/tools/oddpool.md — selective-LP filter candidate
- @entities/tools/polymarket-quotebot.md — external measurement patterns

## Raw Concept

Operator capital question after Cemini `pm_lp_rewards` kill (2026-06-13) + three Gemini DRs (2026-07-14). Synthesizes wiki prior + DR catalogs without treating retail LP anecdotes as Cemini PnL.

## Narrative

### Empirical prior (Cemini — prod, file into wiki)

| Fact | Status |
|------|--------|
| `pm_lp_rewards` attributed ~**+$0.94** / ~23 events (snapshot ~2026-06-11) | Operator/prod |
| Sleeve **KILLED** 2026-06-13 — “Defer; no capital spend”; `PM_LP_LIVE_POST=false` | `pivot_posture.yaml` |
| June pivot active prove-edge: **kalshi_weather** | Prod |

Do **not** use K55/K56 “$50→$18 in 48h” as Cemini evidence.

### DR consensus (all three)

1. **Blind PM/HL copy = structural negative EV** (Daleep/Deleep whale-edge inverse; latency; hedge-leg; fee drag). Aligns with `@concepts/polymarket-copy-trading-strategy.md` + `@gambling-wiki/concepts/pm-copy-trading-retail-risks.md`.
2. **$500 default → Neither (D)** — cannot clear LP $1/day floor without concentration risk.
3. **OpenClaw / Telegram key bots → AVOID** for any live path.
4. **DIY HL fill-mirror → skip** (Binance lead-lag + min notional + funding asymmetry).

### Open conflicts `[NEEDS VERIFICATION 2026-07-14]`

| Conflict | Report A (LP vs copy) | Report B (strategies) | Report C (PM+HL) |
|----------|----------------------|----------------------|------------------|
| $10k PM LP restart | **Yes (A)** | Selective A or HLP | **Skip PM LP** |
| HLP vs User Vaults | HLP OK / DIY no | **HLP OK; skip User Vaults** | **User Vaults &gt; HLP** if HL |

### Working operator posture (until conflicts clear)

1. **No capital to blind copy** (B) — wallets as **negative/filter signal** only.
2. **No auto-restart of `pm_lp_rewards`** without new markout-positive paper + WC/post–Jul-19 reward re-baseline — empirical kill stands.
3. **HL:** paper-only DIY forbidden; if any HL capital, require resolved HLP vs User Vault ADR + canary ≤$1k + DD kills (see vault concept).
4. **Prefer prove-edge sleeves** already in pivot (Kalshi weather / XSP) over either pure LP or copy.

### Shared kill metrics worth adopting

- Net markout (rewards − adverse fills) &lt; 0 for **3 consecutive days** → halt
- Detection/cancel lag &gt; **200ms** on live sports LP → halt
- Canary DD &gt; **8–10%** → halt

## Snippets

> Wiki architecture preferred LP over copy; Cemini ledger showed LP never cleared meaningful payout. Capital choice is not “resume LP nostalgia vs ship Telegram copy.”
