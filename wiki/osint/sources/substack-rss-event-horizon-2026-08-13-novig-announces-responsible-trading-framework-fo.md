---
title: "Event Horizon — Novig 'Responsible Trading Framework' + CFTC incentive advisory + NYC council probe"
type: source
tags: [newsletter, event-horizon, prediction-markets, k236, kalshi]
keywords: [novig, responsible-trading, cftc, self-certification, incentive-programs, nyc-council, baltimore, kalshi, polymarket]
related:
  - concepts/prediction-market-regulation-2026.md
  - sources/newsletter-event-horizon-wildfires-2026-08-12.md
  - concepts/kalshi-retail-lp.md
  - concepts/polymarket-bot-architecture.md
maturity: draft
created: 2026-08-13
updated: 2026-08-13
read_status: read
---

## Relations

- @concepts/prediction-market-regulation-2026.md — extends the CFTC/NY/Baltimore regulatory-state map
- @sources/newsletter-event-horizon-wildfires-2026-08-12.md — prior EH issue (K233): NY AG, CFTC emergency authority
- @concepts/kalshi-retail-lp.md — retail LP posture under incentive-program scrutiny
- @concepts/polymarket-bot-architecture.md — venue ops posture

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Event Horizon — Novig Announces 'Responsible Trading Framework' For Its Prediction Market, Including Minimum Age Of 21 |
| URL | https://nexteventhorizon.substack.com/p/novig-announces-responsible-trading-framework |
| sha256 | `3501ac6061e35ba403c7d90d5b2c0efde4fc5538b6cf0dbca6673dcd84c50114` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-event-horizon-2026-08-13-novig-announces-responsible-trading-framework-fo.md` |
| retrieved | 2026-08-13 |

## Narrative

**Novig's responsible trading framework** (Chapter 14 of the Ludlow Exchange rulebook; Jacob Fortinsky, co-founder/CEO) — affirmative exchange-side obligations across the product lifecycle:

- **21+ nationwide age standard** with identity verification, re-verification, suspension on credible underage/identity-misuse indication. Industry standard is 18+ (Polymarket, Kalshi); decision driven by NCAA lobbying + "broader reckoning coming with the younger traders."
- **Member controls**: deposit/loss/exposure limits, elapsed-time reminders, cooling-off periods, self-exclusion (incl. indefinite), delays before limit increases take effect.
- **Responsible marketing**: no "risk-free" claims, no under-21-directed marketing, no promotions tied to recent losses / financial hardship.
- **Restrictions on trading incentives** (loss-chasing, escalating deposits, holding losing positions).
- **Responsible platform design**: clear disclosure of amounts at risk / max loss / settlement terms; review features that obscure risk or encourage impulsivity.
- **Responsible contract review** before listing + enhanced disclosures / tighter limits as warranted.
- **Risk-based monitoring**: rapid deposit/activity increases, repeated deposits after losses, attempts to raise limits or remove exclusions, apparent loss-chasing → educational prompts to temporary/permanent restrictions.
- **CFTC accountability**: metrics, recordkeeping, periodic review, information to CFTC on request.

**CFTC DMO advisory on incentive programs** (self-certifications under Reg 40.5/40.6): staff concerns over deficient incentive-program filings for event contracts. Explicitly flagged as problematic: payments exceeding what's reasonably necessary, unlimited rebates / "risk-free" trades / market-maker stipends (Rule 1.56 prohibition on guarantees), hidden one-off/preferential arrangements, secret discount codes, non-cash prizes, VIP/early access without disclosure, retention bonuses, sweepstakes-like rewards based on chance (Core Principle 2 non-discrimination). Directly touches Kalshi's chance-based bonus offer (prior EH coverage `pm-kalshi-bonus-odds-event-horizon-2026-07-29`).

**NYC Council investigation** (Speaker Julie Menin) — deceptive/predatory marketing by prediction platforms; letters to **Kalshi, Polymarket, Coinbase, Gemini Titan**; focus on influencer marketing, undisclosed sponsorships, fabricated profitable-wager depictions; can subpoena; WSJ first. **Baltimore** filed consumer-protection suits against **Kalshi + Polymarket** (illegal unlicensed sports betting + misleading legality claims).

**Other signals:** Kalshi raise talk — Sequoia, Wellington at **$40B valuation** (The Information); Kalshi volume Aug 11 **$1.27B** (sports+parlays 78.6%, crypto 18%); CFTC directed Kalshi to keep operating in NY despite a court order (Matt Levine + Better Markets commentary); Kalshi referred **32 insider-trading cases** to CFTC in Q (NYT); **Jeff Bandman** back as CEO of Kalshi Prime (FCM); Kalshi market data now on **DoubleZero Edge** multicast.

**For pm-bot ops:** regulatory pressure on retail-facing incentive programs (CFTC advisory + NYC/Baltimore actions) is regime risk for the Kalshi lane — awareness only, no concrete code steal this issue. Seasonal venue-liquidity lull continues.

**Route:** wiki + `briefs/pm-k236-novig-responsible-trading.md` (no scp — awareness posture, no retail-bot code change mandated).

[Source: Event Horizon 2026-08-13 (retrieved 2026-08-13)]
