---
title: Publisher's exclusion
type: concept
tags: [concept, legal, m-and-a, licensing]
keywords: []
related:
  - sources/3-19-compliance-research.md
  - sources/3-19-ip-sale-research.md
  - concepts/ip-sale-readiness.md
  - entities/data-sources/telethon.md
  - entities/data-sources/finnhub.md
  - entities/platforms/polymarket.md
maturity: validated
created: 2026-04-23
updated: 2026-04-24
disambiguation_pending: true
---

## Relations

- @sources/3-19-compliance-research.md
- @sources/3-19-ip-sale-research.md
- @concepts/ip-sale-readiness.md
- @entities/data-sources/telethon.md
- @entities/data-sources/finnhub.md
- @entities/platforms/polymarket.md

## Raw Concept

Synthesized across 2 source(s) in the Cemini research corpus that reference this concept directly or by equivalent terminology.

## Narrative

**[NEEDS VERIFICATION — 2026-04-24 deep-read of `sources/3-19-compliance-research.md`]** This page's title and content document one meaning of the phrase — the **APA exclusion schedule** mechanic for cherry-picking what gets transferred at acquisition. The 3-19 compliance research source uses the same phrase in a **different, distinct legal sense**: the **Investment Advisers Act §202(a)(11) "publisher's exclusion"** that exempts publishers of bona fide financial publications of general and regular circulation from RIA registration when they don't offer individualized advice (with parallel relief under CFTC Regulation 4.14 for CTA registration). These are two different concepts sharing a name. Decision pending: split into two pages (`apa-exclusion-schedule.md` for current content + a new `iaa-publishers-exclusion.md`), or rename + co-locate. See `wiki/sources/3-19-compliance-research.md` § Snippets S4 for the IAA-sense quote.

**[CONFIRMED — 2026-04-24 Track C audit] doc-only** — APA legal deliverable (exclusion schedule), not software. No engineering milestone. Gap memo: `briefs/track-c-walk-results.md`.

**Publisher's exclusion** _(APA-schedule sense)_ is the Asset Purchase Agreement mechanism by
which specific components of the selling entity's stack can be
**excluded** from the transfer without devaluing the core IP — the
seller either keeps ownership or shuts the feature down pre-close,
and the APA explicitly carves it out.

### Cemini-specific candidates flagged in the 3-19 compliance research
1. **Telegram-channel alt-data** (Telethon pipeline) — reputational
   and user-consent concerns; the acquirer may refuse to inherit.
2. **Finnhub commercial-license-dependent features** — per-entity
   license means the acquirer would re-negotiate, which is
   friction; may be excluded and the feature rebuilt post-close.
3. **Cemini founder's personal Twitter-scraping research notes** —
   clearly personal-IP-adjacent; excluded by default.
4. **Prediction-market execution on Polymarket** — on-chain venue
   with US-retail-access ambiguity; excluded until the acquirer
   decides whether to restructure.

### How it protects deal value
Without publisher's exclusion, any problematic component risks being
used as a price-haircut lever during diligence. Pre-identifying and
carving out lets the core platform be transferred at full value.

## Snippets

*(populate as source stubs are deep-read.)*
