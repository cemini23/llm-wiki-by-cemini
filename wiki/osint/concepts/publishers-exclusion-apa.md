---
title: "Publisher's exclusion (APA exclusion-schedule sense)"
type: concept
tags: [concept, legal, m-and-a, licensing]
keywords: []
related:
  - sources/3-19-compliance-research.md
  - sources/3-19-ip-sale-research.md
  - concepts/ip-sale-readiness.md
  - concepts/ip-sale-corporate-structure.md
  - concepts/publishers-exclusion.md
  - concepts/publishers-exclusion-iaa.md
  - entities/data-sources/telethon.md
  - entities/data-sources/finnhub.md
  - entities/platforms/polymarket.md
maturity: validated
created: 2026-04-23
updated: 2026-04-27
---

## Relations

- @sources/3-19-compliance-research.md — flags this APA-sense as one of two senses sharing the phrase; canonical statutory citation for the IAA-sense lives in S4
- @sources/3-19-ip-sale-research.md — APA architecture+goodwill framing implicitly requires careful APA exclusion design
- @concepts/ip-sale-readiness.md — top-level acquisition-readiness synthesis where APA carve-out logic matters as deal-value protection
- @concepts/ip-sale-corporate-structure.md — K6 2026-04-27 — the dual-entity (HoldCo / OpCo) structure is what makes APA carve-out **operable** at deal time; the OpCo can shed problematic features pre-close because the IP-bearing HoldCo is a separate entity not contaminated by the OpCo's operational scope
- @concepts/publishers-exclusion.md — disambiguation landing page (the original slug, now a stub)
- @concepts/publishers-exclusion-iaa.md — the other concept sharing the phrase; IAA §202(a)(11) bona-fide-publication registration exemption (distinct legal context)
- @entities/data-sources/telethon.md
- @entities/data-sources/finnhub.md
- @entities/platforms/polymarket.md

## Raw Concept

Page renamed from `publishers-exclusion.md` → `publishers-exclusion-apa.md` via `git mv` 2026-04-25 (history preserved). The original slug now hosts the disambiguation landing page. Synthesized across 2 source(s) in the Cemini research corpus that reference this concept directly.

## Narrative

**[RESOLVED — 2026-04-25]** This page documents the **APA exclusion schedule** sense of "publisher's exclusion" — the M&A Asset Purchase Agreement mechanic for cherry-picking what gets transferred at acquisition. The IAA §202(a)(11) bona-fide-publication sense referenced in `@sources/3-19-compliance-research.md` S4 lives on a separate page at `@concepts/publishers-exclusion-iaa.md`. The disambiguation landing page (which routes between the two senses) is at `@concepts/publishers-exclusion.md`.

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
