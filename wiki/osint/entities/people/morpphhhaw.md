---
title: "@morpphhhaw — Perps DEX market-neutral funding-carry bot operator"
type: entity
tags: [entity, person, perps-trader, funding-carry, dex-perps, k55]
keywords: [morpphhhaw, perps-dex-funding-bot, market-neutral-carry, cross-venue-perp-hedge, semi-automated-allocator, telegram-morph-tg]
related:
  - sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md
  - sources/trading-posts-oil-polymarket-html-dex-sniping-2026-05-21.md
  - concepts/perps-dex-funding-carry-strategy.md
maturity: draft
created: 2026-05-20
updated: 2026-05-21
---

## Relations

- @sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md — Post 1 canonical source
- @sources/trading-posts-oil-polymarket-html-dex-sniping-2026-05-21.md — K55-2 redistribution (Post 1 duplicated; reference-only, no new content)
- @concepts/perps-dex-funding-carry-strategy.md — synthesized concept

## Raw Concept

Pseudonymous perpetual-futures DEX trader publishing operational details of a market-neutral funding-carry bot. K55 ingest source (Posts.docx Post 1). Documents the architectural failure modes of cross-venue hedged perps strategies, useful as a portable lesson library for any future Cemini market-neutral workstream.

## Narrative

### Handle

X / Twitter: **@morpphhhaw**

### Stated background

- Telegram channel: `t.me/morph_tg` (referenced in the post; commercial monetization layer).
- Focus: perpetual-futures DEX trading; specifically **cross-venue market-neutral funding-carry strategies**.

### Bot description (from K55 ingest)

- **Strategy class**: volatility-adjusted funding carry (long on one venue + short on another, capturing funding spread, hedged on direction).
- **Cycle**: 15-minute allocator cycle.
- **Safety architecture**: 8 explicit safety gates (live-confirm phrase, reduce-only closes, leverage cap, min balance, min hold, local-DB position state, event log, emergency flatten).
- **Live test results** (small dollar size, ~17.2 position-hours, 4 closed positions): funding PnL +$0.057, price PnL +$0.002 — funding dominated as designed. Run-rate ~19% APR [TENTATIVE — point estimate from n=4].

### Why Cemini cares

- **Out of scope today** — Cemini has no perp-DEX adapters.
- **In scope as a portable failure-mode catalog** — every reconciliation pattern, every safety gate, and every "one leg opened, the other didn't" lesson generalizes to any future Cemini cross-venue strategy.
- **Conditional-future relevance** — if/when Cemini adds Hyperliquid / GMX / dYdX integration, the strategy template synthesized in `@concepts/perps-dex-funding-carry-strategy.md` is the build blueprint.

### Caveats

- Self-published; PnL screenshots only. Treat methodology as plausible, specific numbers as `[TENTATIVE]`.
- Telegram-link affiliate funnel.
- 4-position sample is far too small to validate the strategy's expected return; the author is explicit about this.
