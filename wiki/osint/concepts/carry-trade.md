---
title: Carry trade
type: concept
tags: [concept, forex, strategy, risk-management]
keywords: [carry-trade, interest-rate-differential, forward-premium-puzzle, funding-currency, unwind-risk, negative-skew]
related:
  - entities/platforms/oanda.md
  - concepts/macro-weather-regime.md
  - concepts/perps-dex-funding-carry-strategy.md
maturity: validated
created: 2026-04-23
updated: 2026-05-20
---

## Relations

- @entities/platforms/oanda.md — OANDA is the primary FX execution venue for Cemini's carry-trade variants.
- @concepts/macro-weather-regime.md — Macro Weather regime gates carry-trade sizing: disabled in RED, half-sized in YELLOW, full-sized in GREEN.
- @concepts/perps-dex-funding-carry-strategy.md — K55 instantiation in crypto perpetual-futures: same edge (interest-rate-differential capture) on a different asset class

## Raw Concept

Stub created during Phase 3 lint to close dangling ref from an entity page. Expand on deep-read.

## Narrative

A **carry trade** borrows in a low-interest-rate currency ("funding
currency") and invests in a higher-yielding one ("target currency"),
harvesting the interest-rate differential (the "carry"). In forex
markets, this is executed by holding a long position in the
high-yield currency against the low-yield one, collecting positive
swap rates over time as long as the exchange rate remains stable.

### The forward premium puzzle

Standard economic theory (Uncovered Interest Rate Parity) predicts that
high-interest currencies should depreciate against low-interest ones by
roughly the rate differential — which would cancel out any carry profit.
Empirically, this does not hold: high-yield currencies often depreciate
less than theory predicts, and sometimes appreciate, giving carry
traders a double gain (interest spread + FX appreciation). This
persistent anomaly — the "forward premium puzzle" or "forward bias" —
is the economic basis for carry trade profitability. [Source:
https://www.investopedia.com/carry-trade-definition-4682656 (retrieved
2026-05-02)]

### Risk dynamics: "up the stairs, down the elevator"

Carry trades produce steady, small gains during calm markets but
catastrophic losses during risk-off events. The mechanism:

1. Risk-off shock triggers flight to safety
2. Funding currencies (JPY, CHF) strengthen rapidly as positions unwind
3. High-yield target currencies plummet
4. Leveraged positions face margin calls, forcing further selling
5. A vicious liquidation cycle accelerates

This creates **negative skew** in returns — long periods of small gains
punctuated by sudden, deep drawdowns. The carry trader is effectively
selling crash insurance: collecting small premiums (the rate
differential) in exchange for occasionally paying out a large claim
(market panic losses). [Source:
https://fxempire.com/education/article/fx-carry-trades-explained-strategies-blowups-and-risk-management-tips-1541780
(retrieved 2026-05-02)]

### Historical unwinds

- **2008 GFC**: Yen surged against carry-trade target currencies as
  Lehman collapsed; positions that had been profitable for years
  unwound in weeks.
- **2024 Yen carry trade unwind**: Bank of Japan raised rates while
  the Fed held steady, narrowing the rate differential and triggering
  a sharp yen appreciation that cascaded through global equity and FX
  markets. [Source: Investopedia (retrieved 2026-05-02)]

### Risk management

- **Carry-to-vol ratio**: Evaluate interest rate spread relative to
  implied volatility (a Sharpe-like ratio for carry). A 4% yield in
  a stable currency may be preferable to 8% in a volatile one.
- **Basket funding**: Diversify funding across multiple low-yield
  currencies rather than concentrating in JPY or CHF alone.
- **Sentiment monitoring**: VIX spikes, equity drawdowns, and
  geopolitical shocks signal elevated unwind risk. [Source:
  https://fxempire.com/education/article/fx-carry-trades-explained-strategies-blowups-and-risk-management-tips-1541780
  (retrieved 2026-05-02)]

### Cemini integration

In Cemini's FX stack, carry-trade variants on G10 crosses (notably
EUR/USD, AUD/JPY, NZD/JPY) are gated by the Macro Weather regime:
disabled in RED, half-sized in YELLOW, full-sized in GREEN. The
Kelly/CVaR risk engine enforces per-pair position limits, and the
OANDA v20 REST API provides execution. See @sources/forex-research-3-18.md
for specific pair-level parameterization.

## Snippets

- "At its core, an FX carry trade is embarrassingly simple: you borrow money in a low-interest currency and invest it in a higher-interest one." — [Source: https://fxempire.com/education/article/fx-carry-trades-explained-strategies-blowups-and-risk-management-tips-1541780 (retrieved 2026-05-02)]
- "Carry trades 'go up by the stairs and down by the elevator.'" — [Source: FXEmpire (retrieved 2026-05-02)]
- "The carry trader is effectively selling crash insurance. You collect small premiums (the interest differential) but occasionally have to pay out a massive claim (during market panics)." — [Source: FXEmpire (retrieved 2026-05-02)]
- "Currencies with higher interest rates tend to appreciate against currencies with lower interest rates, contrary to the predictions of interest rate parity. The phenomenon suggests that forward exchange rates are not neutral predictors of future spot rates." — [Source: https://www.investopedia.com/carry-trade-definition-4682656 (retrieved 2026-05-02)]
