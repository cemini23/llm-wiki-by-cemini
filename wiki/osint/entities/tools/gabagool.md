---
title: "gabagool — Polymarket Arbitrage Bot (NO-GO 2026-05-12: no LICENSE + pattern-duplicates CloddsBot)"
type: entity
tags: [tool, polymarket, prediction-markets, arbitrage, trading-bot, python, k39, no-go, no-license-file, cloddsbot-duplicate]
keywords: [gabagool, polymarket, arbitrage, kalshi-adapter, risk-manager, yes-threshold, max-concurrent-arbitrages]
related:
  - sources/evaluating-project-links-stacks.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - entities/tools/cloddsbot.md
maturity: validated
created: 2026-05-11
updated: 2026-05-12
phase_0_audit: NO-GO 2026-05-12 — no LICENSE file (6th occurrence pattern) + risk/arb math duplicates CloddsBot
license_verified: NONE (README claims MIT; `gh api license.spdx_id` = null)
---

## Relations
- `@sources/evaluating-project-links-stacks.md` — source evaluation brief (URL 8)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@entities/tools/cloddsbot.md` — K38 Polymarket arbitrage bot pattern peer; together they form the **2nd-and-3rd Polymarket arb reference architecture** for Cemini's planned Kalshi adapter

## Raw Concept

- **Repo / URL** (per source brief): `github.com/strongca22-cpu/gabagool`
- **Tier (per source brief)**: **Steal-from**
- **License** (per source brief): MIT — pending Phase-0 verification (3rd-occurrence pattern: K36 finance-skills + K38 AI-Trader + K38 Readme.skill all had missing LICENSE files despite README claims)
- **Stack**: Python; Polymarket-specific API + wallet integration

## Narrative

Polymarket arbitrage bot — single-developer project. Eval brief recommends pattern extraction (not deployment) into Cemini's planned Kalshi ingestion + execution layer.

### Patterns to lift

1. **Python Risk Manager schemas** — extract structure, port to Kalshi adapter
2. **`.env` threshold parameters**: `yes_threshold`, `max_concurrent_arbitrages` — operational thresholds for arbitrage gating
3. **Arbitrage mathematical models** — core spread / mispricing detection logic (verify against CloddsBot's existing equivalents)

### Why not deploy

- Too tightly coupled to Polymarket API + wallet (Solana DeFi adapter pattern from CloddsBot, K38, is more generalizable)
- Single-dev maintenance bus-factor
- Cemini's strategic direction is **Kalshi-first** (regulated CFTC venue), not Polymarket — adapter logic must port across venues

### NEEDS VERIFICATION

- LICENSE file actually present in repo (per 3rd-occurrence pattern caution)
- Star count, contributor count, recency of last push
- Whether arbitrage math is novel or reproduces published Kelly-criterion / spread-arbitrage literature

### Phase-0 audit status

**NO-GO 2026-05-12** — no LICENSE file + math duplicates K38-confirmed CloddsBot.

## Phase-0 audit findings (2026-05-12)

**Repo verified**: `github.com/strongca22-cpu/gabagool` — 180★ / Polymarket-coupled / last push 2026-01-27 / **LICENSE file ABSENT** (`gh api license.spdx_id` = null) despite README claiming MIT. **6th occurrence of no-LICENSE pattern** (after K36 finance-skills + K38 Readme.skill + K38 AI-Trader + K39 meridian + K39 mac-code).

**Cross-reference vs CloddsBot (K38, MIT-confirmed, 254★, `alsk1992/CloddsBot`)**:

| Pattern | gabagool location | CloddsBot location | Novelty |
|---------|-------------------|-------------------|---------|
| Position-count + exposure caps + profit-margin checks | `src/risk_manager.py:110-165` (`max_concurrent_arbitrages`, `max_total_exposure`, `min_profit_margin`) | `src/opportunity/risk.ts:381-410` | **DUPLICATE** |
| Circuit breakers | `src/risk_manager.py:196-230` (`check_circuit_breakers()`, static thresholds) | `src/opportunity/risk.ts:410-438` (integrated risk-adjusted return + recommendations loop) | CloddsBot **STRICTLY-BETTER** |
| Risk decomposition | static thresholds only | 5-factor weighted aggregation (`src/opportunity/risk.ts:374-387` — execution, timing, platform, liquidity, correlation) | CloddsBot **STRICTLY-BETTER** |
| Opportunity detection | `strategies/gabagool_strategy.py:205` (`combined_cost = yes_price + no_price < threshold`) | `src/arbitrage/index.ts:287-302` (cross-platform `spread = sellPrice - buyPrice`) | CloddsBot **STRICTLY-BETTER** (multi-venue, gabagool is single-venue YES/NO pair) |
| Profit-margin formula | `strategies/gabagool_strategy.py:210` (`profit_margin = 1.0 - combined_cost`) | identical math in CloddsBot ~L300 | **IDENTICAL** |
| Platform-specific risk scores | not present | `src/opportunity/risk.ts:141-160` (`PLATFORM_RISK_SCORES` — Kalshi 15, Polymarket 20) | CloddsBot **STRICTLY-BETTER** (already Kalshi-aware) |
| Execution flow | sync wrapped in `asyncio.to_thread()` | event-driven fetching | different impl, same goal |

**Kalshi-portability**: gabagool's risk/arb math is Polymarket-coupled at the API/order-book layer (`src/gamma_client.py` GammaClient, `src/bot.py` order execution). CloddsBot is **already pre-architected for cross-venue portability** with platform-specific risk scoring including Kalshi. The math layer of both is venue-neutral (YES/NO binary), but CloddsBot's abstractions are cleaner.

### Verdict

**NO-GO 2026-05-12 — DEFER-INDEFINITELY**. Two independent blockers:

1. **No LICENSE file** = legal ambiguity = extraction prohibited under Cemini's no-LICENSE posture (`@concepts/cemini-license-posture.md` mode #1, now 8th occurrence).
2. **Pattern duplication** = even with license fixed, gabagool's risk/arb logic is a subset re-implementation of CloddsBot. CloddsBot is K38-certified MIT, has 5-factor risk decomposition vs gabagool's static checks, and already includes Kalshi risk scoring. **Kalshi adapter should extract from CloddsBot, skip gabagool**.

Activation trigger: only reconsider if (a) repo adds clean LICENSE file AND (b) gabagool ships novel Polymarket-specific patterns CloddsBot doesn't cover. Neither is on the roadmap.

K39 batch closure: gabagool is the **3rd Steal-from NO-GO** in K39 alongside the eval-brief Adopt mischaracterizations. Pattern aggregate now: 7 mischaracterization catches + 8th no-LICENSE occurrence + 1 GO (nvidia-openshell).

[Source: Evaluating Project Links for Stacks.docx URL 8; retrieved 2026-05-11; Phase-0 audit 2026-05-12]
