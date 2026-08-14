---
title: "Wu Blockchain — Weekly 2026-08-14 (Li Lin UMX, Wintermute $1B HFT/AI, Strategy BTC floor)"
type: source
tags: [newsletter, crypto, perps, quant, k237, wublock]
keywords: [UMX, Wintermute, Strategy, STRC, BTC floor, Fidelity ETH ETF, MARA, GSR, DeFi TVL, SEC tokenization]
related:
  - concepts/crypto-derivatives-volume-2026.md
  - concepts/crypto-venue-website-traffic.md
  - concepts/prediction-market-regulation-2026.md
  - concepts/xsp-lane-trading-framework.md
  - sources/substack-rss-wublock-2026-08-13-july-2026-exchange-website-traffic-report-total.md
maturity: draft
created: 2026-08-14
updated: 2026-08-14
read_status: read
---

## Relations

- @concepts/crypto-derivatives-volume-2026.md — K233 derivatives-volume umbrella
- @concepts/crypto-venue-website-traffic.md — K236 venue-traffic umbrella
- @concepts/prediction-market-regulation-2026.md — SEC tokenization delay + Clarity Act
- @concepts/xsp-lane-trading-framework.md — venue/flow context
- @sources/substack-rss-wublock-2026-08-13-july-2026-exchange-website-traffic-report-total.md — K236 WuBlock sibling

## Raw Concept

| Field | Value |
|-------|--------|
| Title | WuBlockchain Weekly: Li Lin Launches Crypto-Friendly Broker, Bitcoin Miners Shift Fast to AI and Russia Opens Crypto for Retail Investors |
| Publisher | Wu Blockchain (Substack RSS) |
| URL | https://wublock.substack.com/p/wublockchain-weekly-li-lin-launches |
| Retrieved | 2026-08-14 |
| File | `substack-rss-wublock-2026-08-14-wublockchain-weekly-li-lin-launches-cryptofriend.md` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/` |

## Narrative

Weekly crypto market roundup. Key items for the OSINT wiki:

### Venue / flow structural

- **UMX (Unified Market Exchange)** — Li Lin-backed Avenir Group, invitation-only public beta. Positions as a "crypto-friendly securities platform": unified-account system integrating brokerage, crypto exchange, and cross-market capital management in one account (US stocks, ETFs, options, crypto, cross-asset transfers, crypto-stock conversion). Structural bet on cross-market capital efficiency — the "one account for everything" venue pattern.
- **Wintermute $1B / 5yr** HFT + AI data-center investment; expanding into equities, commodities, FX, and **prediction markets**; ~10% non-crypto revenue today → >50% by end-2027; US affiliate broker-dealer + authorized participant. Macro-market-maker expansion into PM = flow-concentration signal for PM LPs.

### Balance-sheet / on-chain datapoints

- **Strategy (MSTR/STRC)**: sold 1,690 BTC @ $64,262 (Aug 3–9) → ~$108.6M, all used for STRC repurchases; raised ~$653M selling 6.59M MSTR shares. Holds 840,447 BTC, avg $75,385. BTC Credit model: STRC floor $16,184 (implied BTC risk 8.84%, credit spread 115bp); combined debt+preferred $21.952B → BTC floor $20,587. Plans to resume accumulation within the year (YTD bought ~175k BTC vs ~7k sold).
- **Bitcoin miners**: fee-revenue share 0.69% (near 10-yr low 0.52% April); hashrate 861 EH/s (−33% from Oct 2025 peak 1.3 ZH/s); est. production cost $78,254/BTC (~23% above spot). Anthropic–Riot $9.1B/20yr cloud-computing deal (191MW Rockdale); MARA $750M loans (18,750 BTC collateral @ ~$1.2B).
- **Fidelity ETH ETF (FETH)**: staking up to 100% of held ETH, 85/15 reward split (fund keeps 85%), quarterly cash distributions, may sell ETH for distributions.
- **DeFi TVL halved** ($167B Oct 2025 → $75B): Andre Cronje — "pure DeFi no longer exists," evolved into "onchain finance" with circuit-breakers/emergency controls/curators.

### Macro / regulatory

- SEC tokenization "innovation exemption" further delayed (Clarity Act §10505 negotiations); public meeting later; cloture motion filed (mid-Sept procedural vote).
- Bank of Russia draft: non-qualified investors up to 300k RUB/yr (~$3,645) in BTC/ETH/USDT through each broker, with screening (market cap, ADTV, 5-yr price history); risk test required; comments until Aug 24.
- GSR (Spencer Hallarn): crypto sluggish due to AI capital rotation; bull return needs AI investment cool-off + Fed rate cuts; tokenization opportunity is in repairing settlement pipelines, not wrapping assets.

### Routing

- **Wiki-only** in OSINT (venue/market context). No GuruWatcher price watches (no concrete trigger levels beyond Strategy floor model, which is issuer-specific). No xsp/pm scp — no implementable venue/flow signal this week (UMX/Wintermute are structural context; Strategy floor model is single-name credit, not a cross-venue signal). Contrast K236 WuBlock traffic brief which had two-series confirmation worth scp'ing.
- **Poker/GW**: skip.

## Snippets

> UMX functions more as a unified-account system integrating brokerage, crypto exchange and cross-market capital-management capabilities, rather than merely offering crypto-asset and US-stock trading side-by-side.
>
> The BTC floor price for STRC is $16,184... its implied BTC risk stands at 8.84% with a credit spread of 115 basis points. The combined notional size of the company's debt and preferred stock amounts to $21.952 billion, yielding an overall BTC floor price of $20,587.
>
> Crypto market-maker Wintermute plans to invest approximately $1 billion over the next five years in high-frequency trading and AI data-center infrastructure... expanding into equities, commodities, foreign exchange and prediction-market businesses.
