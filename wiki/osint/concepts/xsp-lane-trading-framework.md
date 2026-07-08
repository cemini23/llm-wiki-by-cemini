---
title: XSP four-lane trading framework (operator playbook)
type: concept
tags: [concept, options, xsp, playbook, lanes, robinhood, k116]
keywords: [xsp, lane-a, lane-b, leaps, overnight-swing, weeklies, robinhood, hyperliquid-shadow]
related:
  - sources/substack-rss-moontower-2026-07-08-betting-as-a-tax-on-bullshit.md
  - concepts/xsp-hedge-fund-core-book-thesis.md
  - concepts/xsp-put-credit-spread-small-account-smb.md
  - concepts/wheel-options-strategy-smb.md
  - concepts/active-project-research-routing.md
  - entities/tools/deepspec.md
  - entities/tools/openclaw-mission-control.md
  - sources/substack-rss-moontower-2026-07-05-vix-and-buy-signals.md
maturity: draft
created: 2026-06-14
updated: 2026-07-08
---

## Relations

- @concepts/xsp-hedge-fund-core-book-thesis.md — **Lane B** implements the institutional core-book idea on XSP
- @concepts/xsp-put-credit-spread-small-account-smb.md — orthogonal SMB selling strategy on same instrument
- @entities/tools/deepspec.md — K137 inference latency Adopt (speculative decoding)
- @entities/tools/openclaw-mission-control.md — K137 fleet audit steal patterns
- @sources/substack-rss-moontower-2026-07-05-vix-and-buy-signals.md — K147 vol regime steal (inverse VIX spike sizing)
- @sources/substack-rss-moontower-2026-07-08-betting-as-a-tax-on-bullshit.md — K150 falsifier / calibration steal

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
- **Regime:** New risk only on **GREEN** `intel:playbook_snapshot` (SPY gate).
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

## Snippets

> "Lane A first for fast exit loop; Lane B is the wealth engine per mentor thesis." [Source: OSINT K116 session synthesis, 2026-06-14]
