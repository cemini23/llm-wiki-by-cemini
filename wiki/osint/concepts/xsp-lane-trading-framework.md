---
title: XSP four-lane trading framework (operator playbook)
type: concept
tags: [concept, options, xsp, playbook, lanes, robinhood, k116]
keywords: [xsp, lane-a, lane-b, leaps, overnight-swing, weeklies, robinhood, hyperliquid-shadow]
related:
  - sources/substack-rss-capital-flows-2026-07-15-winner-take-all-ai-race.md
  - sources/substack-rss-moontower-2026-07-15-iron-butterfly.md
  - sources/macro-charts-paid-forward-2026-07-15-sox-cpi-oil-metals.md
  - sources/macro-charts-paid-forward-2026-07-14-sox-oil-yen-bounce.md
  - sources/substack-rss-moontower-2026-07-12-investing-orbits.md
  - sources/macro-charts-paid-forward-2026-07-12-sentiment-capitulation.md
  - concepts/cev-resistance-support-optimal-prediction.md
  - sources/arxiv-cev-resistance-support-prediction-2607.08531-2026-07-13.md
  - sources/substack-rss-moontower-2026-07-08-betting-as-a-tax-on-bullshit.md
  - sources/macro-charts-paid-forward-chat-2026-07-10.md
  - sources/substack-rss-capital-flows-2026-07-10-trading-investing-framework.md
  - concepts/capital-flows-sofr-conviction-framework.md
  - concepts/macro-charts-regime-signals.md
  - concepts/macro-charts-gold-reversal-thesis-2026-06.md
  - concepts/macro-charts-sox-tech-correction-watch-2026-06.md
  - concepts/macro-weather-regime.md
  - concepts/xsp-hedge-fund-core-book-thesis.md
  - concepts/xsp-put-credit-spread-small-account-smb.md
  - concepts/wheel-options-strategy-smb.md
  - concepts/active-project-research-routing.md
  - concepts/reviewer-passive-injection-corpus.md
  - entities/tools/deepspec.md
  - entities/tools/openclaw-mission-control.md
  - entities/tools/fable-advisor.md
  - meta/fable-advisor-prod-touch-gate.md
  - sources/substack-rss-moontower-2026-07-05-vix-and-buy-signals.md
maturity: draft
created: 2026-06-14
updated: 2026-07-15
---

## Relations

- @concepts/xsp-hedge-fund-core-book-thesis.md — **Lane B** implements the institutional core-book idea on XSP
- @concepts/xsp-put-credit-spread-small-account-smb.md — orthogonal SMB selling strategy on same instrument
- @entities/tools/deepspec.md — K137 inference latency Adopt (speculative decoding)
- @entities/tools/openclaw-mission-control.md — K137 fleet audit steal patterns
- @sources/substack-rss-moontower-2026-07-05-vix-and-buy-signals.md — K147 vol regime steal (inverse VIX spike sizing)
- @meta/fable-advisor-prod-touch-gate.md — K159 cross-vendor prod-touch checklist
- @concepts/capital-flows-sofr-conviction-framework.md — K155 SOFR conviction overlay
- @concepts/macro-charts-regime-signals.md — K155 Macro Charts Jul 10 regime reads
- @sources/macro-charts-paid-forward-chat-2026-07-10.md — K155 USDJPY / CPI / SOX chat
- @sources/substack-rss-capital-flows-2026-07-10-trading-investing-framework.md — K155 SOFR framework source

## Raw Concept

Operator discretionary **long-call-only** XSP playbook split into four lanes by tenor and hold style. **Lane B** carries the hedge-fund core-book thesis; **Lane A** is a tactical overnight swing sleeve. Prod automation v1 targets **Lane A exits only** (Robinhood); Hyperliquid SP500 perp is timing shadow only.

## Narrative

### Lane map

| Lane | Tenor / style | Portfolio role | Automation posture (2026-06-14) |
|------|---------------|----------------|-------------------------------|
| **A** | **14–60 DTE**, overnight 1–2 session swing; non-January | Tactical overlay; nimble, risk-averse | **Prod brief shipped** — exit monitor first |
| **B** | **LEAPS** (>180 DTE); accumulate on dips | **Core book** (mentor: 30–50% risk budget conceptually) | **Prod brief shipped** — inventory + hedge alerts; manual entry |
| **C** | Mid-dated; **~10:30 ET** decision rule | Between A and B | Not v1 |
| **D** | **Weeklies** | Smallest structural role; informed-bet tier | Not v1 |

January expiries route to **Lane B** (LEAPS), not Lane A.

### Shared rules (all lanes)

- **Instrument:** XSP long **calls** on **Robinhood** (prod).
- **Direction:** No puts in long-call lanes (puts appear as **hedges** per @concepts/xsp-hedge-fund-core-book-thesis.md, not as short premium sleeve).
- **Regime (lane-specific — not universal GREEN-only):**

| Lane | Entry vs Macro Weather |
|------|------------------------|
| **A** | Tactical swing; regime informs sizing/alerts — **not** GREEN-only |
| **B** | **Accumulate on dips** — entries may target **YELLOW/RED** drawdown windows per dip rubric |
| **C / D** | Lane-specific rules when automated (not v1) |
| **Reviewer** | Hard limits + automation posture only — **must not refuse solely on non-GREEN regime** |

Portfolio-level Macro Weather still gates brain/orchestrator Kelly sizing; XSP dip lanes are an explicit exception. See @concepts/macro-weather-regime.md § XSP lane exception.
- **HL:** SP500 perp on Hyperliquid — **clock/timing shadow only**; no XSP options on HL.

### Lane A — exit rules (v1 defaults)

| Rule | Default |
|------|---------|
| Hard max loss | **-$75** / contract |
| Morning cut | Red past **10:30 ET** → close |
| Open + 30 min | Still red → close |
| Entry | Manual or confirm-card |

Canonical prod handoff: `briefs/2026-06-14_xsp-lane-a-overnight-swing-monitor-cemini-prod.md` (on `cemini-prod:/opt/cemini/briefs/`).

Canonical prod handoff: `briefs/2026-06-14_xsp-lane-b-leaps-hedge-monitor-cemini-prod.md` (on `cemini-prod:/opt/cemini/briefs/`).

### Lane B — hedge rules (v1 defaults)

| Field | v1 default |
|-------|--------------|
| Target delta band | 0.35–0.55 |
| DTE floor | >180d |
| Put hedge | Long protective puts; roll alert DTE <45, call Δ >0.65 |
| Entry | Manual only |
| Scorecard | Delta-adjusted risk return |

Dip entry rubric and per-add size caps — operator fills in prod YAML when ready.

### What not to automate first

- LangGraph brain / equity fair-value path for entries.
- HL perp PnL as proof of XSP edge.
- SMB-style **short** put credit rules in the same YAML.

### Reviewer / lane_id contract (K37 pre-prod)

Automated EMS tools (`place_order`, `close_position`, `cancel_order`) MUST include **`lane_id`** on provisional calls so the K37 reviewer applies the correct rule set. See @concepts/reviewer-passive-injection-corpus.md § Pre-prod gates.

| lane_id | v1 automated EMS |
|---------|------------------|
| `lane_a` | **close_position** only (exit monitor) |
| `lane_b` | alerts; **manual** `place_order` via `lane_id=manual` |
| `lane_c`, `lane_d` | not automated |
| `smb_put_credit` | orthogonal track — not merged with long-call lanes |
| `manual` | operator confirm-card entries |

Reviewer uses **refuse_only** on orders — it must not revise strategy args.

### Operator pre-Lane-A checklist (K155)

Run before discretionary Lane A overnight adds (combine with K147 VIX gate + K150 falsifier field):

| Step | Check | Source |
|------|-------|--------|
| 1 | **Macro Weather** GREEN/YELLOW/RED + comment block current | `@concepts/macro-weather-regime.md` |
| 2 | **SOFR curve read** — rates path coherent with thesis? | `@concepts/capital-flows-sofr-conviction-framework.md` |
| 3 | **CPI Tue Jul 15** — tighten overnight size into print; gold/GDX per MC levels | `@concepts/macro-charts-gold-reversal-thesis-2026-06.md` |
| 4 | **USDJPY 162.25–50** — log yen-strength zone for Lane B macro context (advisory) | `@concepts/macro-weather-regime.md` § External overlay |
| 5 | **Conviction journal** — evidence count + cross-asset confirms logged; **block size-up** on balanced pro/con alone | `@concepts/capital-flows-sofr-conviction-framework.md` |
| 6 | **SOX/KOSPI short** — only on MC target range hit; no front-run | `@concepts/macro-charts-sox-tech-correction-watch-2026-06.md` |
| 7 | **Fundsmith 51% H1 turnover** — sentiment extreme note only; no auto-trade | `@concepts/macro-charts-regime-signals.md` § Jul 10 |

Prod briefs: `briefs/2026-07-10_xsp-macro-weather-usdjpy-cpi-operator.md`, `briefs/2026-07-10_xsp-sofr-conviction-pre-lane-a-checklist.md`.

## Snippets

> "Lane A first for fast exit loop; Lane B is the wealth engine per mentor thesis." [Source: OSINT K116 session synthesis, 2026-06-14]


### K161 — CEV aspiration levels (2026-07-13)

Resistance/support as hidden aspiration levels under **CEV** (2607.08531): positive-drift regimes favor a **stopping band** (not one-sided GBM pivots); elasticity shifts band geometry. Operator mental model for Lane A overnight exits / Lane B LEAPS hedges — see brief `briefs/xsp-2026-07-13_k161-cev-resistance-support-aspiration-steal.md`.
