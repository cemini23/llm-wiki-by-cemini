---
title: "CentPRO — Closed-source Polymarket trading bot (Reject, K55)"
type: entity
tags: [entity, tool, polymarket, closed-source, commercial-binary, reject, supply-chain-risk, k55]
keywords: [centpro, centpro-bot, closed-source-windows-binary, polymarket-bot-commercial, $49-month-subscription, telegram-archive-distribution, no-license-found, stacyonchain-promotion]
related:
  - sources/multi-wiki-tool-eval-19url-2026-05-20.md
  - sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md
  - concepts/cemini-license-posture.md
  - concepts/sports-prediction-consensus-agent.md
  - entities/people/stacyonchain.md
  - entities/platforms/polymarket.md
maturity: draft
created: 2026-05-20
updated: 2026-05-20
---

## Relations

- @sources/multi-wiki-tool-eval-19url-2026-05-20.md — K55 tool eval URL 4, **Reject**
- @sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md — K55 Posts.docx Post 4 promoted CentPRO alongside the open architecture
- @concepts/cemini-license-posture.md — license-posture exemplar (commercial closed-source binary)
- @concepts/sports-prediction-consensus-agent.md — the open recipe @stacyonchain describes; CentPRO is the gated implementation
- @entities/people/stacyonchain.md — the author/operator promoting CentPRO

## Raw Concept

- **URL**: `https://centpro.bot/`
- **License**: NO LICENSE FOUND (proprietary commercial software)
- **Stack**: Windows Application (closed-source binary)
- **Distribution**: compressed archive via automated Telegram system
- **Pricing**: $49/month subscription or $120 lifetime
- **K55 verdict**: **Reject** — Cemini-financial fit: ❌. All other surfaces: ❌. No cross-wiki routing.

## Narrative

Phase-0 NO-GO recorded. CentPRO is the productized form of the open sports-prediction-consensus architecture described in `@concepts/sports-prediction-consensus-agent.md`. The architecture is useful and recordable; the bot itself is not adoptable into the Cemini stack.

### Why Reject (verbatim summary of K55 eval reasoning)

1. **Closed-source binary**: no source code access, no audit path, no modification path.
2. **Proprietary distribution**: compressed-archive delivery via Telegram bot. No reproducible build chain.
3. **Subscription pricing**: $49/month or $120 lifetime. Recurring vendor cost + vendor lock-in.
4. **Wrong execution surface**: Windows binary. Cemini is Linux (Hetzner servers + macOS laptop). Would require Wine/VM emulation that defeats latency requirements.
5. **Wrong stack language**: not programmable in Python; cannot integrate with the LangGraph orchestrators at `/opt/cemini`.
6. **IP-sale readiness conflict**: integrating closed-source third-party binaries creates supply-chain audit gaps and contaminates the proprietary-IP boundary.

### Cross-link to the @stacyonchain promotion

The K55 Posts.docx Post 4 by @stacyonchain (`@entities/people/stacyonchain.md`) **explicitly promotes centpro.bot**: "Access the bot we built: https://centpro.bot/ Only 15/50 spots left (I am running it daily for 5m crypto markets) Once it's closed - it's closed."

This is the canonical **author-product conflict-of-interest pattern**: the author writes a detailed architectural post (which is genuinely useful and educational) while gating the productized form behind a paid subscription. The Cemini posture is:
- **Lift the architecture** as a concept page (`@concepts/sports-prediction-consensus-agent.md`).
- **Reject the bot** for adoption (this page).

### Cemini fit

- **None**. Phase-0 NO-GO.
- The K55 evaluation makes the case clearly. No follow-up actions needed.

### License risk

> "Proprietary commercial software entirely devoid of an open-source license, strictly barring any form of codebase integration, modification, or deployment within the infrastructure." [Source: Multi-Wiki Tool Eval Prompt — URL 4 license risk]

### NEEDS VERIFICATION

None. The proprietary closed-source Windows-binary format definitively disqualifies the asset from Linux-based production pipelines. The K55 eval phrased this conclusively.
