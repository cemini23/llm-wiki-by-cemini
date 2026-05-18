---
title: "indicator (Go technical-analysis library)"
type: entity
tags: [tool, technical-analysis, backtesting, go, quant-finance, defer, k51]
keywords: [indicator, cinar-indicator, go-technical-analysis, macd, bollinger-bands, backtesting-framework, cemini-financial]
related:
  - sources/multi-wiki-tool-eval-prompt-2026-05-18.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-18
updated: 2026-05-18
---

## Relations

- @sources/multi-wiki-tool-eval-prompt-2026-05-18.md — K51 multi-wiki tool-eval; Defer verdict, Cemini-financial primary fit
- @concepts/cemini-license-posture.md — license-unverified → Defer pending audit

## Raw Concept

What prompted this page: K51 multi-wiki tool-eval (`@sources/multi-wiki-tool-eval-prompt-2026-05-18.md`) URL 7. Defer, Cemini-financial primary.

## Narrative

`cinar/indicator` — a Go technical-analysis library: 80+ indicators (MACD, Bollinger Bands, and more) plus a strategy backtesting framework, with **zero dependencies**. 852★, frequent recent commits, a deliberate v2 architecture release. Directly relevant to the `/opt/cemini` quant stack — algorithmic-trading indicators + rapid backtesting.

**Verdict: Defer.** The library is mature and well-maintained, but the eval flags the **v2 license text as unconfirmed** (commit logs note a license update for "v2.x.x and above" but the actual terms were not retrieved). Integrating an unverified-license library into the core `/opt/cemini` data pipeline is a fatal IP-sale risk. Defer pending a license audit of the v2 terms — a clean MIT/Apache result would make this a candidate for the trading stack.

`[NEEDS VERIFICATION 2026-05-18]` — audit the exact license text applied to `cinar/indicator` v2.x.x.
