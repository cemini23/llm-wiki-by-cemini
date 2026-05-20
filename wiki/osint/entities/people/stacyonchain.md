---
title: "@stacyonchain — Sports-prediction consensus agent author / CentPRO promoter"
type: entity
tags: [entity, person, polymarket-creator, sports-trading, claude-agent, firecrawl, centpro-promoter, k55]
keywords: [stacyonchain, sports-consensus-agent, firecrawl-claude, centpro-bot-promoter, polymarket-sports-trading, world-cup-test]
related:
  - sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md
  - concepts/sports-prediction-consensus-agent.md
  - entities/tools/centpro.md
  - entities/tools/firecrawl.md
  - entities/platforms/polymarket.md
maturity: draft
created: 2026-05-20
updated: 2026-05-20
---

## Relations

- @sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md — Post 4 source
- @concepts/sports-prediction-consensus-agent.md — synthesized concept
- @entities/tools/centpro.md — the closed-source Windows bot the author promotes (K55 tool eval Reject)
- @entities/tools/firecrawl.md — the scraper used in the open architecture

## Raw Concept

Pseudonymous Polymarket sports-trading creator publishing a detailed architecture for a multi-source consensus agent — paired with a paid commercial product (`centpro.bot`). The architecture is open and useful; the productized form is closed-source and Rejected from the Cemini stack.

## Narrative

### Handle

X / Twitter: **@stacyonchain**

### Product

- `centpro.bot` — closed-source Windows binary, $49/month or $120 lifetime, delivered as a compressed archive via automated Telegram system. K55 tool-eval URL 4. **Rejected** for Cemini integration (see `@entities/tools/centpro.md`).

### Open architecture (the useful part)

Multi-source consensus-as-signal agent for sports predictions on Polymarket. Synthesized in `@concepts/sports-prediction-consensus-agent.md`:
- Firecrawl scrapes tier-weighted analytics sources (Opta, FBref, Understat, WhoScored, SofaScore).
- Claude Sonnet 4.5 extracts per-article signals (extraction-only; no inference).
- Claude synthesizes cross-source consensus (strength + weighted probability + dissent count).
- Entry gates: signal quality, ≥7pp edge over Polymarket price, Kelly × 0.12-0.20 fraction × 6% hard cap.

Reported results: strong signals on ~15-20% of matches; consensus *strength* predicts better than direction; runs at <$30/month in API costs.

### Author / product separation

- The **open architecture** is genuinely useful and adoptable as a Cemini concept page.
- The **closed product** (CentPRO) is not adoptable for Cemini — Windows binary, no source code, Telegram-archive distribution, $49/mo subscription, opaque execution logic. Treat the recipe as adoptable; the bot as a Reject.

### Why Cemini cares

- **Sports markets are a major Polymarket category not yet covered in Cemini's stack**. The @stacyonchain architecture is the cleanest single description of how to approach them programmatically.
- Author has clearly thought through gating + sizing carefully (the 6% hard-cap discipline, the consensus-strength-not-direction insight).

### Caveats

- Promotional content: explicit "Only 15/50 spots left" / "Like + bookmark for setup" framing. Marketing pattern.
- The product-vs-recipe conflict-of-interest is real but the recipe is described in enough technical detail that someone with the patience can reproduce it from the post alone.
- Reported "15-20% strong signal rate" is single-source [TENTATIVE].
