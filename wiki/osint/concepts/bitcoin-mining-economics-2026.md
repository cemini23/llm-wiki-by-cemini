---
title: Bitcoin mining economics 2026 — a subsidy-only business with one squeeze point
type: concept
related:
  - sources/substack-rss-wublock-2026-11-12-global-crypto-mining-news-in-october-binance-poo.md
  - sources/substack-rss-wublock-2026-11-13-wublockchain-weekly-goldman-citi-launch-joint-us.md
  - concepts/osint-inbox-wave-2026-11-14.md
updated: 2026-11-14
---

## Raw Concept

What decided a Bitcoin miner's P&L in late 2026? This page collects the recurring metrics from the WuBlockchain mining coverage: hashprice, fee share, per-coin electricity cost, hashrate distribution and the miner-to-AI pivot.

Sources: @sources/substack-rss-wublock-2026-11-12-global-crypto-mining-news-in-october-binance-poo.md and @sources/substack-rss-wublock-2026-11-13-wublockchain-weekly-goldman-citi-launch-joint-us.md.

## Narrative

### The structure

A miner's revenue is block subsidy plus transaction fees. In late 2026 the second term collapsed.

| Metric | Value | Date |
|---|---|---|
| Fees as share of block rewards | 0.31% | 11 Oct 2026 |
| Fees, 30-day average | 0.64% of revenue | late Oct |
| Consecutive days below 1% | 51 | through mid-Oct |
| Lowest daily reading in dataset (from Jul 2016) | 0.30% | 15 Feb 2026 |
| Share of the ten lowest days in 2026 | 8 of 10 | — |

Revenue is therefore a function of subsidy and coin price, and nothing else. Ordinal-style fee demand is not back.

### The squeeze point

Hashprice is daily revenue per unit of hashrate. At about **$33 per PH/s**:

| Item | Value per PH/s per day |
|---|---|
| Gross revenue | $33.35 |
| After 2% pool fee | $32.68 |
| Electricity cost, 25 J/TH at $0.06/kWh | $36.00 |
| Gross margin | negative |

The rig loses money before hosting and maintenance. Per-coin costs make the fleet split visible:

| Rig | Electricity cost per BTC at $0.05/kWh |
|---|---|
| Antminer S19 | about $86,700 |
| Antminer S21 | about $44,300 |

The S19 is underwater against spot. The S21 holds a cushion. Fleets therefore sort into two populations by hardware vintage, and the hashprice level decides how fast the old fleet retires.

### The two miner cohorts

| Cohort | 2026 output |
|---|---|
| IREN, Core Scientific, Bitfarms, TeraWulf, Cipher | 7,075 BTC, down about 47% from 13,263 |
| MARA, CleanSpark, Riot, HIVE, American Bitcoin | up 16% year on year |

The falling cohort is the group that redirected capacity to AI and HPC hosting. The split is a business-model choice, not an operating failure: a miner that converts a data centre to AI hosting stops producing coins.

The cost curves explain why conversion is attractive. Bitcoin mining is about **40% capex and 45.9% electricity**. AI inference is about **76% capex and 4.8% electricity**. Power is the binding input in mining and capital goods are the binding input in inference.

### Balance-sheet behaviour

- Fourteen listed companies sold about **108,247 BTC** worth **$8.08bn** in 2026. MARA sold 40,581 and Riot 20,264.
- Miner holdings were **1,192,622 BTC**, up 379 BTC week on week.
- The Puell Multiple was **0.99**, just below its 365-day average.

Miners sold into the year and still added to holdings. That is consistent with a refinancing and equipment cycle, not distress. [TENTATIVE: one vendor's aggregate]

### Network and geography

| Region | Estimated hashrate | Share |
|---|---|---|
| United States | about 335 EH/s | 35.6% |
| Russia | about 170 EH/s | 18.1% |
| China | — | about 11.7% |
| Ethiopia | about 15 EH/s | falling, down about 35% |

US share slipped 1.1 points and Russia gained. Pool concentration over 30 days: AntPool 21.0%, Foundry USA 25.3%, F2Pool 16.4%, together 62.7%.

### The structural items

- **Binance Pool shut down** on 10 November 2026, closing a major hashrate marketplace. Migrating miners must re-point rigs and re-price their fee arrangements.
- **CleanSpark moved to quarterly reporting.** Monthly operational updates had been the highest-frequency disclosure in the sector. Less disclosure means a slower price signal.
- **Zcash became the marginal miner story.** ZEC rose about 3,000% since mid-2025, and two backers each target about 20% of network hashrate. Concentration near 40% is a governance risk.

### What to monitor

1. Fee share back above 1%. That is the only sign that on-chain activity is contributing again.
2. Hashprice against the S21 electricity line. That is the fleet-retirement threshold.
3. The capex-to-electricity split of any miner announcing an AI conversion.

## Snippets

> "At an electricity price of $0.05 per kWh, the electricity cost of mining 1 BTC with a Bitmain Antminer S19 is approximately $86,700, above Bitcoin's current market price." [Source: substack-rss-wublock-2026-11-12-global-crypto-mining-news-in-october-binance-poo.md]

> "The hashrate recovery reflects an increase in computing power dedicated to the Bitcoin network, but does not directly imply a corresponding improvement in miners' profitability." [Source: substack-rss-wublock-2026-11-12-global-crypto-mining-news-in-october-binance-poo.md]
