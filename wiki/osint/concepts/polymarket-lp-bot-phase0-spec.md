---
title: "Polymarket LP bot — Phase-0 specification (design only)"
type: concept
tags: [concept, polymarket, lp-rewards, market-making, phase-0, cemini-prod, specification]
keywords: [lp-bot, phase-0, polymarket-clob, participation-forecaster, two-sided-liquidity, adverse-selection, copy-trading-adversary, k56-live-test, paper-trade-gate]
related:
  - concepts/polymarket-lp-rewards-farming.md
  - concepts/polymarket-copy-trading-strategy.md
  - concepts/polymarket-bot-architecture.md
  - concepts/polymarket-microstructure-findings.md
  - concepts/monte-carlo-permutation-test-mcpt.md
  - concepts/kelly-sizing-quarter.md
  - entities/tools/polymarket-clob-api.md
  - entities/tools/polymarket-gamma-api.md
  - entities/platforms/polymarket.md
  - sources/posts-prediction-markets-quant-frameworks-2026-05-21.md
  - sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md
  - sources/trading-posts-2-time-series-openhuman-conflict-detector-lp-tactics-2026-05.md
  - concepts/polymarket-lp-weather-market-discovery.md
  - concepts/polymarket-lp-weather-guard.md
  - concepts/cemini-backtest-report-kit.md
  - meta/pm-lp-backtest-cadence.md
  - concepts/lp-algorithm-live-promotion-gates.md
  - concepts/world-cup-advance-market-bot-v1.md
  - concepts/polymarket-sports-lp-operating-rules.md
  - sources/gemini-polymarket-lp-rewards-world-cup-2026-05-29.md
maturity: draft
created: 2026-05-21
updated: 2026-05-29
clusters: [polymarket, market-making, phase-0]
---

## Relations

- @concepts/polymarket-lp-rewards-farming.md — strategy + tactics + K56 live-test numbers this spec operationalizes
- @concepts/polymarket-copy-trading-strategy.md — adversary model (copy-traders consume flow before our fills matter)
- @concepts/polymarket-bot-architecture.md — shared bot plumbing lessons (reconciler, failed-open, infrastructure-first)
- @concepts/polymarket-microstructure-findings.md — depth, spread, trade-direction constraints on scanner filters
- @concepts/monte-carlo-permutation-test-mcpt.md — pre-live statistical gate for any strategy claiming edge
- @entities/tools/polymarket-clob-api.md, @entities/tools/polymarket-gamma-api.md — required APIs
- @concepts/polymarket-lp-weather-market-discovery.md — prod weather LP discover pass (orthogonal to this Phase-0 politics/geopolitics spec)
- @concepts/polymarket-lp-weather-guard.md — pre-resolution exit when weather pass enabled
- @concepts/cemini-backtest-report-kit.md — laptop LP spread sweep + HTML report before shadow-live
- @meta/pm-lp-backtest-cadence.md — quarterly re-run ritual
- @concepts/world-cup-advance-market-bot-v1.md — K82 sports/WC vertical implementing this architecture for FIFA advance markets
- @concepts/polymarket-sports-lp-operating-rules.md — sports-specific cancel/fill invariants (6–10h pre-kickoff)

## Raw Concept

Phase-0 design document for a **maker-side** Polymarket LP-rewards bot on CeminiSuite. Prompted by K55 user interest + K56 live-test confirmation ($50 → $18 in 48h, Top ~15% LP rank). **No production code in this workspace** — spec only; implementation is server-Claude scope after brief review.

## Narrative

### Phase-0 verdict target

**CONDITIONAL-GO** for a **paper-trade / shadow-live** Phase-1 build if:

1. Reward-eligible market scanner reproduces published participation math on ≥3 historical markets.
2. Simulated two-sided quotes stay inside 3–4¢ of mid without violating per-market capital caps.
3. Adverse-fill P&L in shadow mode stays below LP-reward accrual over a 7-day window at $200 notional.

**NO-GO** if Polymarket removes or materially changes LP scoring before Phase-1 starts, or if shadow mode shows reward income &lt; adverse-selection loss at all tested capital tiers.

### Scope boundary

| In scope (Phase-0 → Phase-1 design) | Out of scope |
|-------------------------------------|--------------|
| USDC LP rewards on reward-eligible CLOB markets | Directional taker bots, weather, Up/Down 5m |
| Two-sided resting limits near midpoint | $POLY airdrop optimization (upside only) |
| Gamma scanner + CLOB place/cancel/reconcile | Telegram copy-trading (NO-AUDIT tools) |
| Capital tiers $50 / $200 / $500 paper-live | Autonomous treasury via Bridge API |
| Operator alerts + daily P&L ledger | Multi-wallet airdrop farming |

Deploy host: **cemini-prod** or dedicated egress stack — decision deferred to server brief; spec assumes same CLOB credentials pattern as existing Polymarket workstreams.

### Capital tiers (from K56 + K55)

| Tier | Markets | Per-market cap | Expected outcome (7–10d) | Evidence |
|------|---------|----------------|-------------------------|----------|
| **Pilot** | 3–5 | 15% of float | Clear $1/day floor; learn fills | K56: $50 → $18 / 48h, Top 15% |
| **Standard** | 5–7 | 15% bot / 35% manual | ~$40 rewards / 10d at Top 6–7% | K55 @MatiasScalbi [TENTATIVE] |
| **Scale** | 7–12 | 15% cap | Diminishing share in deep books | Extrapolation — needs shadow data |

**Do not** size on $POLY FDV estimates. Rewards-only breakeven is the gate.

### System architecture

```
┌─────────────────────────────────────────────────────────────┐
│ 1. MARKET SCANNER (Gamma + rewards eligibility API/page)    │
│    Hard filters: vol≥$40k, resolution≥14d, mid 40–60¢,      │
│    reward pool ≥ $300/day OR boosted new-market flag        │
└───────────────────────────┬─────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. PARTICIPATION FORECASTER                                 │
│    est_share = f(order_size, visible_depth, two_sided=true) │
│    daily_usd = est_share × pool_daily                       │
│    REJECT if est_share < 0.5% OR daily_usd < $1.00          │
└───────────────────────────┬─────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. QUOTE ENGINE                                             │
│    YES bid + NO bid symmetric around mid ± spread_cents      │
│    spread_cents: 3–4 default, 2 for pilot tight mode        │
│    size = min(per_market_cap, market_min_shares)            │
│    Place at 00:00 UTC bucket when possible (daily calc)     │
└───────────────────────────┬─────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. FILL HANDLER (WS user channel)                           │
│    On fill → post limit exit (never market sell)            │
│    Track adverse_selection_usd per market                   │
│    Orphan / dust cleanup on every cycle                     │
└───────────────────────────┬─────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ 5. ROTATION CONTROLLER (every 4–6h + event-driven)          │
│    participation < 1% → pull market                         │
│    mid moved ≥ 2¢ → cancel/replace (resets TWOI — pay cost) │
│    else hold quotes (preserve time-in-book)                 │
└───────────────────────────┬─────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ 6. REWARD ACCOUNTANT                                        │
│    Track claimed vs accrued rewards; $1/day floor alarm     │
│    Daily report: rewards, adverse fills, net, rank proxy    │
└─────────────────────────────────────────────────────────────┘
```

**80% of engineering** is modules 4–6 (plumbing), per @MatiasScalbi — not the quote formula.

### Module acceptance criteria (Phase-1 build gates)

| Module | Phase-1 done when |
|--------|-------------------|
| Scanner | Emits ≥5 eligible markets/day; zero false positives on resolved-in-&lt;14d markets in backtest log |
| Forecaster | Within 2× of actual participation on 3 markets where we have ground-truth reward statements |
| Quote engine | Never posts one-sided-only quotes; respects 15% cap; logs mid/spread at place time |
| Fill handler | 100% fills get limit exit within 60s; zero orphan orders &gt;1h |
| Rotation | No market held with &lt;0.3% participation for &gt;24h without alert |
| Accountant | Daily email/Slack: gross rewards, adverse P&L, net, open exposure |

### Adversary and microstructure constraints

From @concepts/polymarket-copy-trading-strategy.md and @concepts/polymarket-microstructure-findings.md:

- **Copy-traders** (~100ms wallet mirroring) are not competitors for LP *rewards* but are competitors for *fills* — getting picked off on one side raises adverse-selection cost.
- **Public trade-direction feed** is ~59% reliable vs on-chain truth — do not use WS trade sign alone for adverse-selection attribution; reconcile to fills.
- **Near-resolution** markets: hard exclude &lt;14 days — 20–30% swings documented in tactics layer.

### Risk register

| Risk | Severity | Mitigation |
|------|----------|------------|
| Adverse fill on news spike | High | Mid 40–60¢ only; 4–6h human/bot monitor; theme diversification |
| Reward formula change | Medium | Daily diff on Polymarket rewards docs; kill switch |
| Participation share collapse | Medium | Rotation at &lt;1%; forecaster recheck before re-entry |
| Geofence / account | Medium | Keep withdrawable buffer; no full float |
| Copy-trader front-run on fill exit | Low–Med | Limit exits only; accept slower unwind |
| Boosted-reward market churn | Low | Scanner flags new markets; cap exposure per boosted market |

### Statistical gate before live USDC

Run **MCPT** (@concepts/monte-carlo-permutation-test-mcpt.md) on 7-day shadow **net** series (rewards − adverse fills). Phase-1 live requires p-value below team threshold (recommend p &lt; 0.05 on mean net &gt; 0). No MCPT → no live capital beyond pilot tier.

### Phase-0 deliverables (this document + next steps)

| Deliverable | Owner | Status |
|-------------|-------|--------|
| This spec | OSINT wiki | **Done** |
| cemini-prod brief (implementation handoff) | OSINT `briefs/` → scp | **Shipped 2026-05-21** (`/opt/cemini/briefs/2026-05-21_polymarket-lp-bot-phase0-spec.md`) |
| Shadow-mode PRD on server | server-Claude | Not started |
| Phase-0 audit vs existing MM code | server-Claude | Not started |

### Phase-1 handoff checklist (for server-Claude)

1. Confirm CLOB + Gamma client reuse from existing Polymarket modules (no parallel auth).
2. Implement scanner + forecaster with unit tests on 3 frozen market snapshots.
3. Paper-trade 7 days at **$50 pilot** tier only.
4. MCPT on net series; present results in brief.
5. If GO: raise to **$200 standard** tier; operator review at day 14.

### Open decisions (need user / prod input)

1. **Host process** — new service vs module inside existing Polymarket runner?
2. **Alert channel** — reuse Cemini operator notify or new?
3. **Boosted markets** — auto-prioritize Neymar-style 94¢ / tight-spread setups or manual whitelist only?
4. **Concurrent workstreams** — LP bot runs alongside weather/taker bots; shared wallet or sub-account?

### K82 extension — World Cup advance markets (2026-05-29)

See @concepts/world-cup-advance-market-bot-v1.md for the full vertical spec. Delta vs this Phase-0 politics/geopolitics template:

| Parameter | Phase-0 default | WC sports override |
|-----------|-----------------|-------------------|
| Mid band filter | 40–60¢ priority | 20–80¢ conviction + 90¢+ bilateral mode |
| Resolution horizon | ≥14 days | Group-stage calendar; **hard exclude** if kickoff &lt;10h |
| Rotation trigger | 4–6h + mid move 2¢ | **Match calendar guard** T-6h cancel all |
| Fill handler | Limit exit 60s | Same + **queue depletion** ($300) + draw awareness |
| Forecaster pool floor | $300/day | $300–600/day per team (Apr 2026 sports boost) |
| Capital sweet spot | $200 tier | **$2–3K** per Gemini + live-test synthesis |

WC bot is the **first Phase-1 implementation candidate** for this spec — public OSS + Cemini module, prices from Gamma/CLOB at runtime (no hardcoded mids).

## Snippets

> "$50 deployed, sitting top 15% of all LP providers on the platform and the window is still open." [Source: K56 Posts.docx Post 1]

> "For bot: the edge is in the plumbing, not the algorithm." [Source: Posts 2.docx Post 4, @MatiasScalbi]

> "If participation drops below 1%, pull capital and rotate." [Source: @concepts/polymarket-lp-rewards-farming.md tactical table]
