---
title: Interactive Brokers (IBKR)
type: entity
tags: [platform, equities, options, futures, broker, institutional, cemini-prescribed]
keywords: [interactive brokers, ibkr, ibkr pro, fix ctci, tws api, web rest api, professional subscriber, lei, large trader, market data fees]
related:
  - sources/fintech-startup-legal-ip-roadmap.md
  - concepts/ip-sale-corporate-structure.md
  - concepts/ip-sale-readiness.md
  - entities/platforms/alpaca.md
  - entities/platforms/oanda.md
maturity: validated
created: 2026-04-27
updated: 2026-04-27
---

## Relations

- @sources/fintech-startup-legal-ip-roadmap.md — K7 deep-read 2026-04-27; paras 62–66 are the canonical IBKR API-tier + LEI + market-data-fee specification. Phase 3 step 9 in the K7 execution roadmap = "Brokerage Integration: Apply for an Interactive Brokers Pro corporate account under the Florida OpCo, utilizing the newly acquired LEI and EIN."
- @concepts/ip-sale-corporate-structure.md — IBKR Pro corporate account is the prescribed institutional brokerage for the Florida OpCo; opening it requires the LEI which itself depends on the OpCo entity formation
- @concepts/ip-sale-readiness.md — parent thesis; IBKR is the prescribed brokerage in the IP-sale-prep institutional-grade infrastructure layer
- @entities/platforms/alpaca.md — developer-tier alternative; K7 lists Alpaca + QuantConnect as appropriate for prototyping but not for institutional liquidity / routing
- @entities/platforms/oanda.md — non-equities sibling broker; OANDA is FX-specific, IBKR is the multi-asset standard

## Raw Concept

Synthesized from @sources/fintech-startup-legal-ip-roadmap.md K7 deep-read 2026-04-27 (paras 62–66). Created as part of K7 promotion. K7 is the only Cemini-corpus source that addresses IBKR specifically; the Cemini-deployed equities path (per @concepts/ip-sale-readiness.md) currently runs through @entities/platforms/alpaca.md, with IBKR as the K7-prescribed institutional-grade upgrade.

## Narrative

**[CONFIRMED — 2026-04-27 K7 deep-read] doc-only.** Prescribed but not deployed. Cemini's current equities execution venue is @entities/platforms/alpaca.md (developer-tier API). The K7 audit prescribes IBKR Pro corporate account under the Florida OpCo as the **institutional-grade upgrade** for the IP-sale-prep window — but the upgrade is gated on Phase 2 step 5 (LEI + EIN acquisition) and Phase 1 (Florida OpCo formation), and the founder has not yet exercised the upgrade pathway.

### What IBKR is

Interactive Brokers (IBKR) is a US-headquartered global broker (NASDAQ: IBKR) operating as a market-maker and broker-dealer across equities, options, futures, FX, fixed income, and prediction markets, with deep liquidity, global multi-asset reach, and institutional-grade algorithmic routing. K7 calls IBKR "the preeminent industry standard for quantitative startups" (para 62) — the sub-institutional-but-serious tier above Alpaca/QuantConnect (developer-friendly APIs, sub-institutional liquidity) and below dedicated prime-brokerage relationships (Goldman Prime, Morgan Stanley Prime, JP Morgan Prime — which require $25M+ AUM minimums).

### API tiers (K7 para 63)

IBKR offers three distinct API tiers suited to different algorithmic demands:

| Tier | Protocol | Use Case | Latency |
|---|---|---|---|
| **Web REST API** | HTTP + WebSockets | Account management, funding, less latency-sensitive trading | High (round-trip via REST) |
| **TWS API** | TCP socket via Trader Workstation | Higher-frequency algorithmic execution; 100+ advanced order types; routing protocols; conditional algorithms; languages: Java, Python, C#, C++ | Medium (TWS desktop gateway) |
| **FIX CTCI** | Financial Information eXchange protocol over leased lines / extranet | Lowest-latency institutional execution; bypasses TWS desktop gateway entirely; routes orders directly to exchange matching engines | Low (direct exchange routing) |

Cemini's prescribed integration tier per K7: **TWS API** for the algorithmic engines (Python compatibility, programmatic order-type control). FIX CTCI is documented as available but its $1,500/month minimum primary-FIX-session commission (K7 para 65) makes it appropriate only for high-frequency or institutional-flow trading patterns that Cemini does not currently run.

### Professional Subscriber classification + market data fees

K7 para 64 surfaces a critical distinction for corporate entities: under exchange regulations, **any corporate entity / trust / LLC is categorically classified as a "Professional Subscriber"** for market data purposes — regardless of whether it trades proprietary capital or manages client funds. Professional Subscribers face substantially higher monthly fees for real-time market data across all global exchanges (NASDAQ, NYSE, ARCA, BATS, AMEX, OPRA, plus international venues).

Operational-cost-model implication: Cemini's recurring market-data overheads will be at Professional rates (typically $50–250/month per exchange feed depending on coverage scope) regardless of trading-volume tier. This is a fixed cost dimension that needs to be factored into the algorithm's after-data-cost economic-viability analysis.

### Minimum thresholds + LEI requirement (K7 paras 65–66)

- **$500 corporate equity balance** to activate market data subscriptions
- **$1,500/month** primary FIX session commission for FIX CTCI routing
- **Active Legal Entity Identifier (LEI)** required for institutional brokerage onboarding — IBKR will not open an LLC or C-Corp account without an active, current LEI

The LEI is the **gating prerequisite** for IBKR Pro corporate account opening. Per K7 Phase 2 step 5, the LEI is acquired immediately after entity formation via the **Global LEI Foundation (GLEIF)**; per K7 Phase 3 step 9, the IBKR account application is then submitted using the LEI + the OpCo's EIN.

### Cemini deployment posture (2026-04-27)

| Component | K7 prescription | Deployed | Gap |
|---|---|---|---|
| IBKR Pro corporate account | Phase 3 step 9 | Not opened | Pending LEI + entity form sequencing |
| TWS API integration | Prescribed for algorithmic execution | Cemini equities path = Alpaca; no IBKR integration | Pending IBKR account |
| FIX CTCI | Documented as available; not prescribed at current scale | Not relevant | n/a |
| LEI registration | Phase 2 step 5 | Not registered | **Required before IBKR onboarding** |
| Market data subscriptions | Professional Subscriber tier | Alpaca IEX free tier currently | Cost-model upgrade pending IBKR |

The current Alpaca-tier deployment is sufficient for paper-trading + small-capital live testing through the IP-sale-prep window. The IBKR upgrade becomes binding only when the institutional-grade execution venue becomes part of the acquirer's deal-time-of-sale operational continuity (i.e., the acquirer expects the platform to run on IBKR or equivalent post-close), or when Cemini's trading volume crosses thresholds (Large Trader 13h-1 = 2M shares OR $20M FMV daily, see @sources/fintech-startup-legal-ip-roadmap.md S8) where Alpaca's developer-tier routing becomes a bottleneck.

## Snippets

### S1 — IBKR API tiers (K7 para 63)
> "Interactive Brokers offers distinct API tiers suited to different algorithmic demands. The Web REST API provides modern websocket streaming for account management, funding, and less latency-sensitive trading. For higher-frequency algorithmic execution, the TWS API (compatible with Java, Python, C#, and C++) allows deep programmatic control over more than 100 advanced order types, routing protocols, and conditional algorithms. For the absolute lowest latency, institutional accounts can utilize the FIX CTCI (Financial Information eXchange) protocol to bypass the desktop gateway software entirely and route orders directly to the exchange matching engines using dedicated leased lines or extranets."
>
> *— @sources/fintech-startup-legal-ip-roadmap.md K7 para 63.*

### S2 — Professional Subscriber classification (K7 para 64)
> "A crucial distinction for corporate entities is market data classification. Under financial exchange regulations, any corporate entity, trust, or LLC—regardless of whether it trades proprietary capital or manages client funds—is categorically classified as a 'Professional Subscriber'. Professional subscribers face substantially higher monthly fees for real-time, non-delayed market data across all global exchanges. A firm must rigorously factor these recurring data overheads into the algorithm's operational cost model."
>
> *— @sources/fintech-startup-legal-ip-roadmap.md K7 para 64. The Professional-Subscriber-classification reframing is the overlooked recurring-cost dimension that surfaces only when transitioning from individual to entity brokerage account.*

### S3 — Minimum thresholds + LEI requirement (K7 paras 65–66)
> "Corporate and institutional accounts at IBKR require a minimum equity balance of $500 to activate market data subscriptions. Furthermore, utilizing advanced routing infrastructure like FIX CTCI incurs severe minimum monthly commission thresholds, generally starting at $1,500 per month for the primary FIX session. To operate in global financial markets, a corporate brokerage account requires a Legal Entity Identifier (LEI). The LEI is a globally recognized, 20-character alphanumeric code that uniquely identifies legally distinct entities participating in financial transactions. Post-2008 regulatory frameworks mandate the LEI for transparent risk tracking across jurisdictions, and institutional brokerages will strictly require an active, current LEI to onboard an LLC or C-Corp and grant trading permissions."
>
> *— @sources/fintech-startup-legal-ip-roadmap.md K7 paras 65–66. The LEI-as-onboarding-blocker framing is the operational-sequencing key in the K7 Phase 2 → Phase 3 transition.*
