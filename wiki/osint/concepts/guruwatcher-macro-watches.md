---
title: GuruWatcher Macro Watches — newsletter-claim price/level alert candidates
type: concept
tags: [concept, guruwatcher, macro, watches, k233]
keywords: [guruwatcher, price-watches, inflation-swaps, factor-rotation, alert-only]
related:
  - sources/newsletter-capital-flows-inflation-risk-2026-08-12.md
  - sources/substack-rss-capital-flows-2026-08-15-bond-market-crash.md
  - concepts/inflation-risk-regime-2026.md
  - sources/substack-rss-glitchspx-2026-08-16-talon-weekly.md
  - sources/substack-rss-moontower-2026-08-16-324-rssb.md
  - concepts/structural-abstention-trusted-kernel.md
  - sources/arxiv-2608.13926-never-the-number-2026-08-17.md
maturity: draft
created: 2026-08-12
updated: 2026-08-17
---

## Relations

- @sources/newsletter-capital-flows-inflation-risk-2026-08-12.md
- @sources/substack-rss-capital-flows-2026-08-15-bond-market-crash.md — K239 30y / 10s30s / SPX-DXY covariance
- @concepts/inflation-risk-regime-2026.md
- @sources/substack-rss-glitchspx-2026-08-16-talon-weekly.md — K240 Talon HITL map
- @sources/substack-rss-moontower-2026-08-16-324-rssb.md — K240 RSSB implied corr
- @concepts/structural-abstention-trusted-kernel.md — never fabricate a watch level
- @sources/arxiv-2608.13926-never-the-number-2026-08-17.md

## Raw Concept

What this page answers: which macro claims from newsletters are watchable as alert-only price/level watches in GuruWatcher.

## Narrative

K233 candidates from Capital Flows (2026-08-12): steels/metals factor (+43% YTD), ags (+16% YTD), and short-end inflation swaps (Japan→UK). Alert-only, no order routing. Watch reconciles most-recent-wins claims vs the armed watches ledger on cemini-prod.

[Source: Capital Flows 2026-08-12]

**K239 (2026-08-15 teaser):** 30y toward ATH; 10s30s bear steepener; ~42 bp terminal hikes through 2027; commodities bid; financials rallying with rates; SPX+30y+DXY lockstep; MMFs at 3% not a safe harbor. **Research-note candidates only** — no `watches.json` arm without operator-supplied symbol + op + level. Brief: `../GuruWatcher/briefs/2026-08-15_k239-guruwatcher-capital-flows-bond-crash-watches.md`.

**K240 (2026-08-17):** Glitch SPX Talon weeklies = HITL sector map (not a directive). Moontower RSSB = implied stock-bond corr awareness. VIVO is **not** a watch unless the operator names a level. Dashboards that print a number consumed as fact must structurally abstain (@concepts/structural-abstention-trusted-kernel.md). Never auto-rewrite `watches.json`.
