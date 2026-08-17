---
title: "Moontower #324 + RSSB implied stock-bond correlation (folded)"
type: source
tags: [source, substack, rss, xsp, k240]
keywords: [RSSB, stock-bond, Fisher-z, implied-correlation, Moontower-324]
related:
  - concepts/xsp-lane-trading-framework.md
  - concepts/guruwatcher-macro-watches.md
  - concepts/high-iv-collar-shopping.md
maturity: draft
created: 2026-08-17
updated: 2026-08-17
read_status: read
---

## Relations

- @concepts/xsp-lane-trading-framework.md — RSSB IV as hedge-regime awareness
- @concepts/guruwatcher-macro-watches.md — HITL watch only if a level is named
- @concepts/high-iv-collar-shopping.md — prior Moontower hedge vocabulary

## Raw Concept

| Field | Value |
|-------|--------|
| Folded | Moontower #324 + stock-bond / RSSB options |
| sha256 (#324) | `b4a29d959a3c810e095136521217b953c226fa3f249171e1194664e22159a2aa` |
| sha256 (stock-bond) | `51feaf4e1361c0cfb913642d1e51db6d020d67e347ef85be5290e6c95a7d21e2` |
| URLs | https://moontowermeta.com/moontower-324/ · https://moontowermeta.com/stock-bond-correlation/ |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/` (both filenames) |
| Dual-ID | **OSINT K240**. xsp awareness + GW if a level is named. No auto-arm. |

## Narrative

#324 is mostly a book/showdown note plus pointers into the stock-bond companion. The steal is the companion: **RSSB** (Return Stacked — $1 global equities + $1 Treasuries on $1 capital) listed options. Implied vol on RSSB lets you back out an **implied stock-bond correlation** because the leg vols are known. Risk-parity books are structurally short that correlation and are the natural buyers of RSSB vol if the market exists.

Realized (VTI/IEF): 30-day **+0.43**, 1-year **+0.28**. Fisher-z CI on N=22 for r=0.43 is roughly **[+0.02, +0.72]** — you cannot distinguish 0.43 from 0.20 or 0.60. 1Y N=251 is tighter **[+0.16, +0.39]**. Error bars are lopsided because correlation is bounded; transform, interval, invert.

**Steal:** xsp awareness of implied stock-bond corr via RSSB IV. GuruWatcher only if the operator names a level. Never auto-rewrite `watches.json`.

## Snippets

> "its implied vol allows you to back out an implied stock-bond correlation since we know the vol of the legs." [Source: moontowermeta.com/stock-bond-correlation]

> "The 95% confidence interval on a correlation of +0.43 with N=22 is roughly [+0.02, +0.72] — wide." [Source: same]
