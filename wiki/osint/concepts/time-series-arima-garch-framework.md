---
title: "Time-series ARIMA + GARCH trading framework — directional forecast × volatility-scaled sizing"
type: concept
tags: [concept, time-series-analysis, arima, garch, unit-root, stationarity, walk-forward, position-sizing, quant-finance, k55, k56]
keywords: [arima, garch, augmented-dickey-fuller, unit-root, spurious-regression, log-returns, volatility-clustering, walk-forward-validation, volatility-scaled-sizing, conditional-expectation, alternative-data, rohonchain, yifan-guo-ssrn-5140015, box-jenkins, engle-1982, hamilton-1994]
related:
  - sources/trading-posts-2-time-series-openhuman-conflict-detector-lp-tactics-2026-05.md
  - sources/phynance-kakushadze-1405-1948v2-stochastic-calculus-2014.md
  - sources/ssrn-5140015-time-series-quant-finance-2025.md
  - sources/posts-prediction-markets-quant-frameworks-2026-05-21.md
  - concepts/markov-regime-switching-models.md
  - concepts/stochastic-calculus-foundations.md
  - concepts/quant-finance.md
  - concepts/event-based-prediction-market-ml.md
  - concepts/monte-carlo-permutation-test-mcpt.md
  - entities/people/rohonchain.md
  - entities/people/yifan-guo.md
  - sources/ai-for-trading-strategies-jevtic-zhaw-2022.md
  - concepts/ols-alpha-signal-framework.md
  - sources/rohonchain-fifa-wc-shock-recovery-strategy-2026-06-02.md
  - sources/trading-posts-compilation-6-2026-06-08.md
maturity: validated
created: 2026-05-20
updated: 2026-06-08
clusters: [quant-finance, time-series]
---

## Relations

- @sources/trading-posts-2-time-series-openhuman-conflict-detector-lp-tactics-2026-05.md — Post 1 (@RohOnChain) primary source for the synthesized framework
- @sources/phynance-kakushadze-1405-1948v2-stochastic-calculus-2014.md — foundational stochastic-calculus reference; complements the empirical framework here with the theoretical underpinnings
- @sources/ssrn-5140015-time-series-quant-finance-2025.md — Yifan Guo's (Jan 2025) survey paper provides the academic anchor for the canonical ARIMA / GARCH / Holt-Winters / ML stack referenced empirically here (K56)
- @concepts/markov-regime-switching-models.md — author's companion piece (K49); time-series + Markov regime detection are designed to be used together
- @concepts/stochastic-calculus-foundations.md — synthesized stochastic-calculus reference page
- @concepts/quant-finance.md — corpus-index home
- @concepts/event-based-prediction-market-ml.md — K56 extension: documents why this equity-style framework fails when ported naively to Polymarket (event-resolution structural breaks)
- @concepts/monte-carlo-permutation-test-mcpt.md — K56 complementary validation framework; MCPT tests whether the backtested edge is real vs data-mining bias
- @entities/people/rohonchain.md — author
- @sources/trading-posts-compilation-6-2026-06-08.md — K106 Post 1 refresh (2008 MBS opener; overlaps K55 body)
- @entities/people/yifan-guo.md — author of the academic-foundation paper (SSRN 5140015)

## Raw Concept

What prompted this page: K55 Posts 2.docx Post 1 — @RohOnChain's "How To Build A Time Series Model To Win Every Single Trade." Third in his quant-framework series (after Markov chains for regime detection and a neural-network signal post). Synthesizes a complete, runnable ARMA-family + GARCH framework with operationally-realistic caveats.

**K56 extension (2026-05-21)**: the Yifan Guo SSRN paper (ssrn-5140015, Jan 2025) was ingested as the academic foundation for the toolkit applied here empirically. Guo's paper anchors the canonical references — Box-Jenkins (1976), Hamilton (1994 *Time Series Analysis*), Engle (1982 ARCH), Breiman (2001 Random Forests) — and provides the structural framing for §§2.1 (ARIMA), 2.2 (GARCH), 2.3 (Holt-Winters), 2.4 (RNN/LSTM), 3.1-3.4 (asset pricing, risk, portfolio optimization, algorithmic trading), and §4 (non-stationarity / multicollinearity / model uncertainty). The empirical and theoretical layers now converge cleanly on this page.

The K56 ingest also surfaced two **complementary validation frameworks**:
- @concepts/event-based-prediction-market-ml.md (@Alexo_0x) — documents why this equity-style framework fails when ported naively to prediction markets
- @concepts/monte-carlo-permutation-test-mcpt.md (@phosphenq) — pre-deployment test for distinguishing real edge from data-mining bias

Together with the Markov-regime page and the LP-rewards-farming page, these form the K55/K56-era quant-finance core of the wiki.

## Narrative

### Why this is in the wiki

@RohOnChain's framework is **standard quantitative finance** — there's nothing novel in ARIMA or GARCH as techniques. The reason this concept page exists:

1. **Operational discipline**, not technique novelty — the post is unusually clear about the *three* most common implementation traps (unit-root spurious regression, in-sample backtesting, ignoring volatility clustering for position sizing). This is the framework's actual value.
2. **Companion to the Markov-regime page**: the author explicitly designed the two posts to compose. The wiki should record both halves and the cross-validation pattern.
3. **Foundational for any future Cemini ML/forecast layer**: any model that takes price data as input has to pass these tests first; documenting the gates here makes them reusable.

### Foundational claim: a forecast is not a prediction

The single most important framing from the post:

> A forecast is the **conditional expectation** — E[X_{t+1} | X_1, ..., X_t] — the single value that minimizes squared error across all possible outcomes. It will essentially never equal the realized value.

The market-maker analogy: quote a bid-ask around an imperfect estimate of the expected price, collect the spread over thousands of trades. The model can be **always slightly wrong** and still profitable if it's directionally right often enough to overcome transaction costs.

**Implication for any Cemini model**: stop chasing high R² or high "accuracy" on directional forecasts. Instead, measure (a) the bias of the conditional expectation, (b) the variance of realized vs forecast, (c) the cost structure that determines what "often enough" means.

### The three time-series tasks

| Task | Uses | Live-trading viable? |
|---|---|---|
| **Filtering** | Past + present data | Yes — every charting indicator is a filter (e.g. moving averages) |
| **Smoothing** | Past + present + *future* data | **No** — requires future information; research-only |
| **Forecasting** | Current + past state → expectation of future | Yes — the trading-decision surface |

Most charting indicators are filters, not forecasters. Confusing the two is a recurring beginner trap.

### The unit-root trap (the most expensive mistake)

Regression of P_{t+1} on P_t for almost any asset gives R² > 0.99. The reader thinks they've discovered a near-perfect predictive relationship. They have **spurious regression**.

A unit root: `X_t = X_{t-1} + ε_t` (random walk). When you regress a random walk against another random walk, even unrelated series produce huge R². The cure:

```python
from statsmodels.tsa.stattools import adfuller

price = df['Close']
returns = df['Close'].pct_change().dropna()

price_test = adfuller(price)         # likely p > 0.05 (has unit root)
returns_test = adfuller(returns)     # likely p < 0.05 (stationary)
```

**Rule**: never build predictive models on raw price levels. Convert to log returns first:
```
r_t = ln(P_t) - ln(P_{t-1})
```
Log returns are *approximately* stationary; they still exhibit volatility clustering + fat tails (addressed by GARCH below).

### The ARMA family

| Model | Form | What it captures |
|---|---|---|
| **AR(p)** | `X_t = Σ φ_i X_{t-i} + ε_t` | Serial dependence on lagged values. φ > 0 = momentum; φ < 0 = mean reversion |
| **MA(q)** | `X_t = ε_t + Σ θ_i ε_{t-i}` | Effect of past surprises on current value (news-event dynamics) |
| **ARMA(p,q)** | Combined | Both effects |
| **ARIMA(p,d,q)** | ARMA after d-th differencing | Same, on non-stationary series |
| **GARCH(p,q)** | `σ²_t = ω + Σ α_i ε²_{t-i} + Σ β_j σ²_{t-j}` | Time-varying volatility (volatility clustering) |

**GARCH is the highest-leverage piece for trading**. The author's specific claim:

> The GARCH-based position sizing is doing more work than the ARIMA forecast direction. Reducing exposure during high volatility regimes is the most reliable edge in the entire system. Directional forecasts at 52-55% accuracy combined with volatility-scaled sizing produces better risk-adjusted returns than 60% accuracy with fixed sizing.

Translation: a mediocre directional forecast plus dynamic position sizing on volatility regime beats a better directional forecast with fixed sizing.

### Reference implementation

```python
import numpy as np
import pandas as pd
import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA
from arch import arch_model
from statsmodels.tsa.stattools import adfuller

class TimeSeriesTradingSystem:
    def __init__(self, ticker, period="5y"):
        self.ticker = ticker
        self.period = period

    def fetch_and_prepare(self):
        data = yf.Ticker(self.ticker).history(period=self.period)
        self.prices = data['Close']
        self.returns = np.log(self.prices / self.prices.shift(1)).dropna() * 100
        return self.returns

    def check_stationarity(self, series):
        result = adfuller(series.dropna())
        return result[1] < 0.05  # True = stationary

    def fit_arima_garch(self, returns, arima_order=(1,0,1), garch_order=(1,1)):
        arima = ARIMA(returns, order=arima_order).fit()
        garch = arch_model(arima.resid, vol='Garch',
                           p=garch_order[0], q=garch_order[1]).fit(disp='off')
        return arima, garch

    def generate_signals(self, returns, lookback=252):
        signals = []
        for i in range(lookback, len(returns)):
            window = returns.iloc[i-lookback:i]
            try:
                arima = ARIMA(window, order=(1,0,1)).fit()
                forecast = arima.forecast(steps=1)[0]
                garch = arch_model(arima.resid, vol='Garch', p=1, q=1).fit(disp='off')
                vol_forecast = np.sqrt(garch.forecast(horizon=1).variance.values[-1][0])
                signal = 1 if forecast > 0 else -1
                position_size = min(1.0, 1.0 / max(vol_forecast, 0.1))
                scaled_signal = signal * position_size
            except:
                scaled_signal = 0
            signals.append({'date': returns.index[i], 'signal': scaled_signal})
        return pd.DataFrame(signals).set_index('date')
```

### Three implementation rules (the operational layer)

1. **GARCH-based position sizing > ARIMA forecast direction**. If you have to pick one, pick GARCH.
2. **Walk-forward is non-negotiable**. At each step, fit the model on history-only and forecast one step ahead. *Never* fit on the full dataset and treat in-sample predictions as a backtest — "that is a curve fit with a label."
3. **Alternative data is the ceiling**; ARMA/GARCH is the floor. ARMA captures patterns *inside* the price series; alt-data (earnings call sentiment, order-flow imbalance, credit spreads, cross-asset regime info) captures information about the underlying process *before* it appears in price. Combine.

### Rolling-window stability gotcha

All ARMA-family models assume stable statistical properties across the estimation window. In real markets this is **continuously violated**. Standard mitigation: rolling 252-trading-day window that discards old data as new data arrives.
- **Shorter window** → adapts faster, parameter estimates noisier.
- **Longer window** → more stable parameters, lags regime changes.
- Optimal window length is **empirical** — must be answered separately per instrument and per strategy.

### The cross-validation with Markov regimes (the genuinely novel insight)

Author's closing question, worth carrying forward:

> A GARCH model tells you that volatility is about to spike based on patterns in the return history alone. A Markov Chain tells you that the market is about to transition from a low-volatility regime to a high-volatility regime based on the current state. **If both signals agree**, that convergence is one of the strongest risk-management signals available. **If they disagree**, that disagreement is itself information about current market conditions.

This is the explicit reason the framework is designed alongside `@concepts/markov-regime-switching-models.md`:
- **Agreement** (both forecast vol-up) → strong risk-management signal → cut exposure aggressively.
- **Disagreement** (GARCH says vol-up, Markov says continue regime) → ambiguous → reduce sizing pending more data; conditions are not as the model assumed.

This pattern generalizes — any two independent forecasting systems with overlapping signal sets can be cross-validated this way. → Adopt as a Cemini multi-model orchestration pattern.

### Cemini fit

- **Foundational reference** — any future Cemini layer that takes price/returns data as input should pass through the unit-root + stationarity gates documented here.
- **GARCH position-sizing layer** is the most directly portable single piece. If Cemini's existing strategies use fixed sizing, retrofitting volatility-scaled sizing is a one-day project with measurable risk-adjusted upside.
- **Walk-forward validator** as a Cemini-wide backtest discipline — never trust an in-sample backtest result.
- **Composes with Markov regime detection** — both already documented; orchestration logic (agree/disagree) is the next step.

## Snippets

> "Every time series can be decomposed into trend, seasonality, and random shock components. The key question is whether these components are stable enough over time to be useful for forecasting." [Source: Posts 2.docx — Post 1, @RohOnChain]

> "A forecast is not a prediction. It is the conditional expectation, the single value that minimizes average squared error across all possible future outcomes. It will essentially never equal the realized value." [Source: Posts 2.docx — Post 1, @RohOnChain]

> "Never build predictive models on raw price levels. Always transform to returns, log returns, or other stationary derived quantities before applying time series models." [Source: Posts 2.docx — Post 1, @RohOnChain]

> "The GARCH-based position sizing is doing more work than the ARIMA forecast direction. Reducing exposure during high volatility regimes is the most reliable edge in the entire system." [Source: Posts 2.docx — Post 1, @RohOnChain]

> "Time series models capture patterns within the price series. Alternative data captures information about the underlying process that drives prices before it appears in the price series." [Source: Posts 2.docx — Post 1, @RohOnChain]
