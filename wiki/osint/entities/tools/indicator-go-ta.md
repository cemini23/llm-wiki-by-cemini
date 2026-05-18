---
title: "indicator (Go technical-analysis library)"
type: entity
tags: [tool, technical-analysis, backtesting, go, quant-finance, reject, agpl-poison-pill, license-drift, k51]
keywords: [indicator, cinar-indicator, go-technical-analysis, macd, bollinger-bands, backtesting-framework, cemini-financial, agpl-3.0, license-drift]
related:
  - sources/multi-wiki-tool-eval-prompt-2026-05-18.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-18
updated: 2026-05-18
---

## Relations

- @sources/multi-wiki-tool-eval-prompt-2026-05-18.md — K51 multi-wiki tool-eval; eval said Defer, license check flipped it to Reject
- @concepts/cemini-license-posture.md — AGPL-3.0 poison pill; this is the posture that terminally blocks it

## Raw Concept

What prompted this page: K51 multi-wiki tool-eval (`@sources/multi-wiki-tool-eval-prompt-2026-05-18.md`) URL 7. Defer, Cemini-financial primary.

## Narrative

`cinar/indicator` — a Go technical-analysis library: 80+ indicators (MACD, Bollinger Bands, and more) plus a strategy backtesting framework, with **zero dependencies**. 852★, frequent recent commits, a deliberate v2 architecture release. Directly relevant to the `/opt/cemini` quant stack — algorithmic-trading indicators + rapid backtesting.

**Verdict: Reject — AGPL-3.0 poison pill.** The K51 eval scored this Defer, flagging the v2 license as unconfirmed. License check 2026-05-18 (GitHub API + `LICENSE.md` inspection) resolves it: `cinar/indicator` is licensed **AGPL-3.0** (`LICENSE.md` = "GNU AFFERO GENERAL PUBLIC LICENSE, Version 3"). This is a **license-drift catch** — the v2.x.x relicense the eval noticed in the commit logs *was* the move to AGPL-3.0. AGPL's network-copyleft would compel open-sourcing any `/opt/cemini` surface that links it. Terminal blocker for the IP-sale-bound trading stack — **hard Reject, not Defer**.

Cemini takeaway: the 80+ indicator formulas (MACD, Bollinger, etc.) are standard public-domain technical-analysis maths — reimplement them directly from their definitions if needed; do **not** lift or link this AGPL implementation. License status verified 2026-05-18 `[CONFIRMED]`.
