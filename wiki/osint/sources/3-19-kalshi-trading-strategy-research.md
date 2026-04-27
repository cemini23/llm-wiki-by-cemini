---
title: Advanced Algorithmic Trading Architecture and Microstructure Analysis for Kalshi Prediction Markets
type: source
tags: [docx, rl-marl, llm-agents, market-microstructure, quant-finance, crypto, prediction-markets, cemini-internal]
related:
  - concepts/ensemble-weather-forecasting.md
  - concepts/favorite-longshot-bias.md
  - concepts/ip-sale-readiness.md
  - concepts/macro-weather-regime.md
  - concepts/market-microstructure.md
  - concepts/quant-finance.md
  - entities/components/kelly-cvar-risk-engine.md
  - entities/data-sources/finnhub.md
  - entities/data-sources/fred.md
  - entities/data-sources/gdelt.md
  - entities/data-sources/open-meteo.md
  - entities/frameworks/fastapi.md
  - entities/frameworks/fastmcp.md
  - entities/frameworks/langgraph.md
  - entities/frameworks/pydantic-v2.md
  - entities/infrastructure/polars.md
  - entities/infrastructure/redis.md
  - entities/infrastructure/timescaledb.md
  - entities/observability/grafana.md
  - entities/observability/loki.md
  - entities/observability/prometheus.md
  - entities/observability/tempo.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - sources/3-19-compliance-research.md
  - sources/3-19-ip-sale-research.md
maturity: validated
created: 2026-04-23
updated: 2026-04-24
read_status: deep-read
clusters:
  - rl-marl
  - llm-agents
  - market-microstructure
  - quant-finance
  - crypto
  - prediction-markets
  - cemini-internal
---

## Relations

- @concepts/ensemble-weather-forecasting.md — 31-member Open-Meteo + Gumbel statistical-arbitrage methodology
- @concepts/favorite-longshot-bias.md — primary edge (sell longshots, buy favorites)
- @concepts/ip-sale-readiness.md — top-level synthesis target
- @concepts/macro-weather-regime.md — weather-contract regime detection
- @concepts/market-microstructure.md — Market Microstructure corpus-index hub (Q 2026-04-27)
- @concepts/quant-finance.md — Quantitative Finance corpus-index hub (Q 2026-04-27)
- @entities/components/kelly-cvar-risk-engine.md — Bayesian Modified Kelly + temporal discount + 50% order-book depth cap (Step 55 in Cemini roadmap)
- @entities/data-sources/finnhub.md — institutional consensus comparison feed
- @entities/data-sources/fred.md — macroeconomic consensus arbitrage feed (Fed rates, CPI)
- @entities/data-sources/gdelt.md — adverse-shock signal that triggers BatchCancelOrders inventory withdrawal
- @entities/data-sources/open-meteo.md — 31-member ensemble forecast → Gumbel CDF for weather contracts
- @entities/frameworks/fastapi.md — async REST/WebSocket event loop; Polars offload pattern preserves loop liveness
- @entities/frameworks/fastmcp.md — intelligence server hosting the Kalshi-strategy debate
- @entities/frameworks/langgraph.md — 5-agent Devil's Advocate debate orchestrator
- @entities/frameworks/pydantic-v2.md — pykalshi natively emits Pydantic v2 domain models (alignment justification for SDK adoption)
- @entities/infrastructure/polars.md — vectorized statistical engine (Gumbel fit, ensemble shrinkage, AS in logit space)
- @entities/infrastructure/redis.md — pub/sub blackboard between intelligence layer and execution layer
- @entities/infrastructure/timescaledb.md — Kalshi order book history persistence
- @entities/observability/grafana.md — operator dashboards
- @entities/observability/loki.md — execution log aggregation
- @entities/observability/prometheus.md — request-rate + latency metrics
- @entities/observability/tempo.md — distributed traces across LangGraph → Polars → execution
- @entities/platforms/kalshi.md — the venue
- @entities/platforms/polymarket.md — cross-platform arbitrage explicitly **rejected** (bridge risk, KYC, capital fragmentation outweigh 4–6¢ spreads)
- @sources/3-19-compliance-research.md — companion regulatory/IP source; both anchor on Kalshi DCM compliance under CFTC exclusive federal jurisdiction
- @sources/3-19-ip-sale-research.md — companion deal-economics source; this Kalshi source's first paragraph explicitly frames the strategy stack as an IP-sale-valuation lever (uncorrelated alpha + tail-risk hedge for legacy equity/crypto portfolios)

## Raw Concept

- **Original title**: Advanced Algorithmic Trading Architecture and Microstructure Analysis for Kalshi Prediction Markets
- **Author(s)**: Anonymous Gemini Deep Research-style synthesis; 50 footnoted external sources spanning Kalshi API documentation, Federal Reserve research papers (FEDS 2026010), academic finance papers (Karl Whelan / Becker / arXiv 2510.15205 / Aaltodoc / SFU Swartz et al.), QuantPedia, Substack research blogs (Navnoor Bawa, MoonTowerMeta), CFTC Federal Register notices, M&A advisory (Dentons, Cohen Milstein, Katten), HN/Reddit/r/algotrading discussion threads, and the pykalshi GitHub repository.
- **Type**: DOCX (markdown body extracted via `/tmp/extract_docx.py` to `/tmp/kalshi_strategy_research.txt`)
- **Location**: research for cemini/3_19 Kalshi Trading Strategy Research.docx
- **Retrieved**: 2026-04-23 (filename date reflects download date, not publication)
- **Length**: ~7,200 words; 9 H2 sections; 7 H3 subsections; 3 tables; 50 footnoted citations
- **Read status**: deep-read
- **Primary cluster**: rl-marl
- **All clusters**: rl-marl, llm-agents, market-microstructure, quant-finance, crypto, prediction-markets, cemini-internal

### Section map (H2)
1. Strategic Valuation and Institutional Positioning — IP-sale framing; CPU-only Hetzner constraint forces statistical-supremacy architecture
2. Prediction Market Microstructure and Retail Inefficiencies — favorite-longshot bias + macroeconomic consensus arbitrage
3. Profitable Non-HFT Trading Strategies — weather ensemble stat-arb + calendar spread arbitrage
4. Mathematical Framework for Market Making and Inventory Risk — binary-resolution-induced negative gamma; Avellaneda-Stoikov in logit space
5. Optimal Capital Allocation: The Modified Kelly Criterion — binary-event Kelly + fractional + Bayesian + temporal discount
6. Execution Architecture: REST API and Rate Limit Mechanics — tier table (Basic/Advanced/Premier/Prime) + BatchCreate/BatchCancel weighting asymmetry
7. Real-Time State Management via WebSocket API — RSA-PSS auth, reciprocal-bid order book reconstruction
8. Python SDK Evaluation and Dependency Management — pykalshi recommendation despite <500 stars filter exception
9. Regulatory Landscape and Institutional Viability (2026) — CFTC exclusive federal jurisdiction; Feb 2026 Enforcement Advisory; Cemini-data-source compliance posture
10. Conclusion and Integration Roadmap — full 5-component integration recipe (Intelligence / Pricing / MM / Execution / Compliance)

## Narrative

### Abstract
Non-HFT Kalshi trading architecture for the **CPU-only Hetzner constraint** (no GPU, 128GB RAM ceiling, single VPS, Python 3.12 / FastAPI / Redis / TimescaleDB stack). Core mathematical pivot: **Avellaneda-Stoikov market-making transposed into logit space** (log-odds) because event contracts resolve to $0/$1 — Arrow-Debreu securities incompatible with Black-Scholes Greeks. Strategy stack: favorite-longshot bias passive liquidity provision (sell longshots, buy favorites), weather ensemble statistical arbitrage (31-member Open-Meteo forecasts → Gumbel extreme-value distribution), calendar spread arbitrage, macroeconomic consensus arbitrage (Kalshi 40.1% lower MAE vs Bloomberg consensus, 60% during shocks). Cross-platform Kalshi↔Polymarket arbitrage explicitly **rejected** despite 4–6¢ spreads. Capital allocation via **Bayesian Modified Kelly** (fractional 0.10–0.25x + temporal discount + 50% order-book-depth cap). Execution leverages **BatchCreateOrders/BatchCancelOrders weighting asymmetry** (cancel = 0.2x token weight) for inventory-risk fast-withdrawal. WebSocket order book reconstructed from **bids-only stream** via reciprocal calculation (`P(YES_ask) = 1 − P(NO_bid)`). SDK recommendation: **pykalshi** despite <500-star filter exception (native Pydantic v2 + OrderbookManager + exponential-backoff retries justify the early-stage risk). Regulatory posture: Kalshi as **CFTC-regulated DCM** under exclusive federal jurisdiction (state preemption confirmed via 2024–2025 litigation); Feb 25 2026 CFTC Enforcement Advisory targets MNPI/spoofing/front-running; Cemini's open-data-source posture (Open-Meteo, FRED, SEC EDGAR) yields **zero MNPI risk**.

### Cross-source synthesis — the Cemini-Kalshi triad
This source is the **execution-architecture pillar** of the Cemini IP-sale triad:
- **Regulatory/IP**: @sources/3-19-compliance-research.md — establishes that Kalshi (DCM under CFTC) + the Cemini risk engine + Devil's Advocate audit logs together constitute a "regulatory-compliant execution engine" deal artifact
- **Deal-economics**: @sources/3-19-ip-sale-research.md — quantifies the valuation premium (uncorrelated-alpha multiple uplift; tail-risk hedge for buyer's legacy book)
- **Execution-architecture (this source)**: provides the actual mathematics, API mechanics, and 2026 regulatory framework needed to make the architecture sale-credible

### Key findings (with section anchors)
- **§1 IP-sale framing** — first sentence of source explicitly positions Kalshi integration as IP-sale-valuation lever; "regulated, non-correlated macro and event-driven markets significantly elevates the platform's valuation"; provides "built-in mechanism for hedging tail risks inherent in legacy equity and cryptocurrency portfolios"
- **§1 CPU-only constraint as competitive moat** — Hetzner CPU-only + 128GB RAM ceiling explicitly **mandates the strategic pivot away from HFT** toward "statistical supremacy, advanced probability distributions, and the existing multi-agent FastMCP intelligence server"
- **§2 Event contracts = Arrow-Debreu securities** — fully collateralized binary options resolving to discrete $0/$1 state; standard Black-Scholes Greeks (Delta, Vega) **structurally incompatible**; Gamma becomes aggressively negative as resolution approaches
- **§2 Favorite-longshot bias empirically confirmed** — 300K+ Kalshi-contract dataset 2025/2026: $0.01–$0.10 contracts win <4.18% (vs 1–10% implied → expected return strongly negative −16%+); $0.80–$0.99 contracts win >95.83% (vs 80–99% implied → small positive); rooted in $0.01 minimum tick representing massive relative premium on low-probability contracts (structural, not just behavioral)
- **§2 Macroeconomic consensus arbitrage** — Fed 2026 study (FEDS 2026010): Kalshi has **40.1% lower MAE than Bloomberg consensus** across all regimes; 60% lower during shocks (deviation >0.2pp from consensus); when consensus deviation >0.1pp predicts 81.2% shock rate → 82.4% one day prior to release
- **§3 Weather ensemble statistical arbitrage** — Open-Meteo's 31-member ensemble → Gumbel extreme-value distribution (Gaussian inadequate for temperature extremes) → CDF over Kalshi temperature brackets → **Bayesian shrinkage to climatology** when ensemble variance is high; example: ensemble 74% vs Kalshi $0.45 (45% implied) → massive statistical edge; zero-API-key + zero-rate-limit perfectly aligned with bootstrapped budget
- **§3 Calendar spread arbitrage** — exploits volatility mispricing between correlated events at different resolution dates within a single Kalshi ecosystem (avoids cross-platform fragmentation); 5-agent Devil's Advocate continuously recalculates implied volatility surface across calendar strip; 2σ deviation triggers execution
- **§4 Avellaneda-Stoikov in logit space** — canonical AS model **must be transposed** into log-odds because linear price modeling fails at asymptotic boundaries ($0.01/$0.99); reservation quote `r = μ_logit − γ·q·σ²·τ` (mid-price + inventory penalty); optimal spread `~ γ·σ²·τ + (2/γ)·log(1 + γ/k)` where k = liquidity parameter; inverse sigmoid maps back to $0.01–$0.99 before order submission
- **§5 Modified Kelly** — base binary Kelly `f* = (b·p − q)/b` (b = net odds); full Kelly carries 33% probability of bankroll-halving-before-doubling; mandatory **fractional modifier 0.10–0.25x** + **Bayesian shrinkage** (Swartz et al. SFU; treats `p` as parameter with uncertainty; deferral factor widens when prediction interval is wide) + **temporal discount factor** (capital opportunity cost on long-duration contracts) + **50% order-book-depth cap** to prevent slippage; all wired into Cemini's "Step 55 Kelly/CVaR risk engine"
- **§6 Kalshi API tier mechanics** — Basic 20r/10w; Advanced 30/30; Premier 100/100 (3.75% monthly volume); Prime 400/400 (7.5% monthly volume); write limits apply to create/cancel/amend; tier qualification requires "demonstrating technical competency in API management"
- **§6 Batch endpoint weighting asymmetry** — `BatchCreateOrders` = 1 token/order × 20-order max = 20 tokens; `BatchCancelOrders` = **0.2 tokens/order** × 20-order max = 4 tokens; this asymmetric pricing **enables 100 resting-order clearings per second on Basic tier** when LangGraph detects adverse macro shock via GDELT/FRED → preserves rate limits for re-entry at favorable prices
- **§7 WebSocket reciprocal-bid order book** — Kalshi sends only "Bids" via `orderbook_updates` channel; local manager must reconstruct full Bid/Ask spread by calculating `P(YES_ask) = 1 − P(NO_bid)` (binary invariant `P(YES) + P(NO) = 1`); RSA-PSS signature auth at handshake; subscriptions by `market_ticker` only (UUID `market_id` expressly unsupported); offload reciprocal calculation to Polars to keep FastAPI event loop unblocked
- **§8 pykalshi SDK exception** — `pykalshi` (~56–113 stars, MIT, arshka/pykalshi) **falls below the >500-star filter** but recommended anyway because it provides: native WebSocket streaming, OrderbookManager handling delta-snapshot merging + reciprocal bid/ask, Pydantic v2 domain models (aligns with Cemini contracts), automatic exponential backoff for HTTP 429, direct Pandas/Polars output; rejected: official auto-generated `kalshi_python_sync/_async` (no order-book state management, manual backoff required); kalshi-specific SDKs with >500 stars **do not currently exist**; recommendation: wrap pykalshi in defensive try/except blocks within FastMCP server
- **§9 CFTC exclusive federal jurisdiction** — Kalshi as Designated Contract Market (DCM); CFTC Chairman Michael S. Selig affirmed (2026) that prediction markets trading event contracts are commodity derivatives under CFTC exclusive jurisdiction; state gaming authority injunctions (Massachusetts, Arizona) **preempted** by Commodity Exchange Act (CEA); CFTC has actively intervened in federal courts to assert preemption
- **§9 Feb 25 2026 CFTC Enforcement Advisory** — targets market manipulation: **spoofing, pre-arranged trading, front-running, MNPI exploitation** all prosecutable under CEA; advisory followed Kalshi's internal penalization of users with advance non-public knowledge of event resolution; **Cemini's data sources (Open-Meteo ensemble, FRED, SEC EDGAR) are publicly accessible non-privileged → zero MNPI risk**; alpha generation via "superior statistical processing (Gumbel distributions, Bayesian Kelly sizing, Logit-space AS modeling) rather than insider access" → strict compliance
- **§10 Five-component integration recipe** — Intelligence (FastMCP/LangGraph debates over FRED + Open-Meteo) → Pricing (Polars Gumbel fit + Bayesian Modified Kelly) → Market Making (AS reservation quotes + spreads in logit space) → Execution Bus (Redis pub/sub → audited pykalshi → BatchCreateOrders + BatchCancelOrders) → Compliance (open-data-source posture)

### Drift verified vs prior wiki narrative
The pre-existing wiki Narrative bullet "Kalshi Premier/Prime API mandates rate-limiting + real-time monitoring — Kelly/CVaR governor + Prometheus/Loki/Grafana/Tempo stack satisfies" **conflates two sources**. The Kalshi source documents the **rate-limit mechanics + WebSocket reconstruction** (true) but does **not** mandate "real-time monitoring" as a Premier/Prime tier requirement. The "Prometheus/Loki/Grafana/Tempo to satisfy a real-time monitoring mandate" framing is from @sources/3-19-compliance-research.md (Kalshi as DCM under CFTC has near-real-time monitoring expectations under DCM Core Principle 4). The Kalshi source itself focuses on **technical-competency** as the Premier/Prime qualification ("demonstrating technical competency in API management") + the asymmetric BatchCancel weighting as the actual inventory-risk-management mechanism. Updated key findings above reflect the source's actual mechanics.

### Cemini-stack mappings (architectural component → Kalshi-source justification)
| Cemini component | Kalshi-source justification | Source anchor |
|---|---|---|
| FastAPI async event loop | WebSocket auth + order book updates require non-blocking I/O; Polars offload preserves loop liveness | §7 ¶96 |
| Polars vectorized DataFrames | Reciprocal bid reconstruction; Gumbel CDF over 31-member ensemble; AS reservation quote calculation in logit space | §3 ¶26, §7 ¶96 |
| Redis pub/sub blackboard | Calculated AS quotes passed from intelligence layer to execution module | §10 ¶117 |
| TimescaleDB | Persistent Kalshi order book history for shock-divergence detection | §2 ¶21 |
| LangGraph 5-agent Devil's Advocate | Triggers debate when Kalshi prices diverge from FRED/Open-Meteo consensus by >0.1pp; recalculates implied vol surface across calendar strip | §2 ¶21, §3 ¶33 |
| FastMCP intelligence server | Hosts the Kalshi-strategy debate; wraps pykalshi in defensive try/except | §1 ¶4, §8 ¶102 |
| Kelly/CVaR risk engine ("Step 55") | Bayesian Modified Kelly + temporal discount + 50% order-book-depth cap | §5 ¶63 |
| BatchCancelOrders 0.2x weighting | Adverse-macro-shock liquidity-withdrawal escape valve when GDELT/FRED signal regime change | §6 ¶89 |
| pykalshi (audited, wrapped) | OrderbookManager + Pydantic v2 + exponential backoff justify <500-star filter exception | §8 ¶101 |
| Open-Meteo / FRED / SEC EDGAR | Open public data sources → zero MNPI risk under Feb 2026 CFTC Enforcement Advisory | §9 ¶110 |
| Pydantic v2 model alignment | pykalshi natively emits Pydantic v2 → no contract translation layer | §8 ¶101 |

### Workspace-level retraction notes
- **No DeepSeek-R1-14B or Ollama mentioned in this source** — the LLM-architecture rhetoric is implicit ("multi-agent FastMCP intelligence server", "5-agent Devil's Advocate debate protocol") and routes to whatever LLM actually drives the debate. No re-anchoring needed in this source. Per @entities/infrastructure/deepseek-r1-14b.md, the actual LLM driver is the hosted DeepSeek API — not the local Ollama runtime that prior wiki text referenced.
- **No infrastructure misclaims** — Hetzner CPU-only + 128GB RAM is consistent with the workspace baseline.

## Snippets

### S1 — IP-sale valuation framing (§1 ¶3, opening paragraph)
> "For a proprietary algorithmic trading platform targeting an intellectual property (IP) sale to an institutional buyer, the inclusion of regulated, non-correlated macro and event-driven markets significantly elevates the platform's valuation. It demonstrates a capability to capture uncorrelated alpha and provides the acquiring entity with a built-in mechanism for hedging tail risks inherent in legacy equity and cryptocurrency portfolios."
[Source: 3_19 Kalshi Trading Strategy Research.docx, §1 Strategic Valuation and Institutional Positioning, ¶3]

### S2 — CPU-only constraint as architectural forcing function (§1 ¶4)
> "Operating within a rigid deployment stack—Python 3.12, FastAPI, Redis, and PostgreSQL/TimescaleDB on a CPU-only Hetzner VPS with a 128GB RAM ceiling—requires ruthless optimization. The absence of GPU acceleration and low-latency infrastructure mandates a strategic pivot away from high-frequency trading (HFT) and order book latency arbitrage. Instead, the architecture must leverage statistical supremacy, advanced probability distributions, and the existing multi-agent FastMCP intelligence server to exploit retail behavioral biases and structural microstructure inefficiencies."
[Source: 3_19 Kalshi Trading Strategy Research.docx, §1, ¶4]

### S3 — Favorite-Longshot Bias empirical table (§2.1 ¶8 + Table 1)
> "Academic research, including a comprehensive 2025/2026 study utilizing transaction-level data from over 300,000 Kalshi contracts, confirms a systemic favorite-longshot bias (FLB) in regulated prediction markets. The core finding is that low-probability contracts are systematically overpriced, while high-probability contracts are systematically underpriced."
> | Contract Price Range | Implied Probability | Empirical Win Rate | Expected Return |
> | $0.01 - $0.10 | 1% - 10% | < 4.18% | Strongly Negative (-16%+) |
> | $0.40 - $0.60 | 40% - 60% | ~50% | Neutral |
> | $0.80 - $0.99 | 80% - 99% | > 95.83% | Small Positive |
[Source: 3_19 Kalshi Trading Strategy Research.docx, §2.1 The Favorite-Longshot Bias, ¶8 + Table 1 ¶9-15]

### S4 — FLB structural origin (not just behavioral) (§2.1 ¶17)
> "This inefficiency is not merely a behavioral flaw driven by retail traders seeking lottery-like convexity; it is a structural necessity of the quote-driven market. Liquidity providers (Makers) demand a risk premium to cover their inventory exposure on low-probability events. Because the minimum tick size is $0.01, a single tick on a low-probability contract represents a massive relative premium, skewing the implied probability higher."
[Source: 3_19 Kalshi Trading Strategy Research.docx, §2.1, ¶17]

### S5 — Macroeconomic consensus arbitrage / shock alpha (§2.2 ¶20)
> "The Federal Reserve study demonstrated that Kalshi forecasts exhibit a 40.1% lower Mean Absolute Error (MAE) than consensus forecasts across all market regimes. During major economic shocks—defined as scenarios where actual values deviate from consensus by more than 0.2 percentage points—Kalshi's accuracy advantage increases to 60% lower MAE on the day prior to the data release."
[Source: 3_19 Kalshi Trading Strategy Research.docx, §2.2 Macroeconomic Consensus Arbitrage, ¶20; cites FEDS 2026010 footnote 11]

### S6 — Weather ensemble + Gumbel + Bayesian shrinkage (§3.1 ¶29)
> "If the ensemble model indicates a 74% probability that the daily high will fall within a specific bracket, and the Kalshi order book prices the 'YES' contract at $0.45 (an implied 45% probability), a massive statistical edge exists. Because the Open-Meteo API is free and processing 31 arrays via Polars requires minimal memory overhead, this strategy perfectly aligns with the bootstrapped budget and 128GB RAM CPU-only constraints, requiring zero GPU acceleration and fitting easily within a solo developer's maintenance capacity."
[Source: 3_19 Kalshi Trading Strategy Research.docx, §3.1 Weather Ensemble Statistical Arbitrage, ¶29]

### S7 — Cross-platform arbitrage explicitly rejected (§3.2 ¶31)
> "While cross-platform arbitrage (e.g., simultaneously trading discrepancies between Kalshi and Polymarket) offers consistent 4 to 6 cent spreads, it introduces severe capital fragmentation, smart contract bridge risks, and KYC complexities that decrease the automated elegance of the system. A more capital-efficient approach within Kalshi's single ecosystem is calendar spread arbitrage."
[Source: 3_19 Kalshi Trading Strategy Research.docx, §3.2 Calendar Spread Exploitation, ¶31]

### S8 — Devil's Advocate calendar-strip vol-surface watchdog (§3.2 ¶33)
> "The 5-agent Devil's Advocate debate protocol can utilize the Redis blackboard to continuously recalculate the implied volatility surface across the calendar strip, alerting the execution module when the spread deviates from historical norms by more than two standard deviations."
[Source: 3_19 Kalshi Trading Strategy Research.docx, §3.2, ¶33]

### S9 — Black-Scholes Greeks structurally incompatible (§4 ¶35-36)
> "Because prediction market contracts resolve to exactly $0.00 or $1.00 at a known expiration date, there is no continuous underlying asset price to hedge against, rendering standard Black-Scholes Greeks (like Delta and Vega) structurally incompatible. As the known resolution date approaches, the payoff function becomes discontinuous. Gamma becomes aggressively negative, meaning that maintaining a neutral exposure requires exponential adjustments to position sizing."
[Source: 3_19 Kalshi Trading Strategy Research.docx, §4 Mathematical Framework for Market Making and Inventory Risk, ¶35-36]

### S10 — AS in logit space rationale (§4.1 ¶38)
> "If an algorithm attempts to model probability linearly (e.g., using simple moving averages on contract prices), it will suffer catastrophic execution errors near the asymptotic boundaries ($0.01 or $0.99), as linear adjustments fail to account for the mathematical impossibility of exceeding 100% certainty."
[Source: 3_19 Kalshi Trading Strategy Research.docx, §4.1 Avellaneda-Stoikov in Logit Space, ¶38]

### S11 — Reservation quote in logit units (§4.1 ¶40-46)
> "In this logit framework, the market maker calculates a reservation quote (the theoretical fair value adjusted for current inventory) and an optimal spread. The reservation quote in logit units is defined as: [...] is the current mid-price in logit units. is the current inventory position. is the risk aversion parameter of the market maker. is the instantaneous belief variance (the volatility of the market's consensus). is the remaining time to resolution."
[Source: 3_19 Kalshi Trading Strategy Research.docx, §4.1, ¶40-46; mathematical symbols stripped during docx-to-text extraction — refer to original Word equation editor objects]

### S12 — Inverse sigmoid round-trip + protection from terminal ruin (§4.1 ¶49)
> "By operating entirely within logit space, the trading engine natively comprehends that a price movement from $0.50 to $0.49 represents a minute shift in expected return, whereas a movement from $0.02 to $0.01 represents a 100% relative shift. Once the optimal spread and reservation quotes are calculated in logit units by the Polars engine, the system applies the inverse sigmoid function to map the values back into the $0.01 to $0.99 price boundaries before submitting the limit orders to the Kalshi exchange via the Redis pub/sub bus. This framework mathematically guarantees that inventory skew will dynamically adjust quotes to protect the portfolio from terminal ruin at resolution."
[Source: 3_19 Kalshi Trading Strategy Research.docx, §4.1, ¶49]

### S13 — Full Kelly's catastrophic baseline (§5.2 ¶61)
> "Executing a full Kelly allocation in prediction markets is highly detrimental due to the absolute loss of capital on a failed binary bet. Full Kelly carries a mathematical certainty of a 33% probability of the bankroll halving before it doubles. Furthermore, standard Kelly assumes the proprietary estimate is flawlessly accurate and that execution will occur without slippage."
[Source: 3_19 Kalshi Trading Strategy Research.docx, §5.2 Fractional and Bayesian Modifications, ¶61]

### S14 — Bayesian Modified Kelly + temporal discount + depth cap (§5.2 ¶63-64)
> "A more advanced implementation required for the planned Kelly/CVaR risk engine (Step 55) involves a Bayesian Modified Kelly Criterion. Academic research by Swartz et al. establishes that treating as an unknown parameter with a degree of uncertainty requires adjusting the fraction based on a specified loss function. As the algorithmic engine gathers more historical data on its own forecasting accuracy, it generates a posterior distribution. The deferral factor dynamically adjusts the Kelly fraction down when the prediction interval is wide, and increases it only as the model's historical calibration improves. Additionally, the formula must be modified to account for the 'time to resolution.' Capital locked in a contract expiring in six months incurs a significant opportunity cost compared to capital locked in a daily weather contract. The risk engine applies a temporal discount factor to the Kelly output, severely limiting exposure on long-duration contracts to preserve liquidity for high-frequency daily events. Finally, the total allocation must be capped at a maximum of 50% of the available order book depth at the target price to prevent severe market impact and execution slippage."
[Source: 3_19 Kalshi Trading Strategy Research.docx, §5.2, ¶63-64; cites Swartz et al. SFU footnote 30]

### S15 — Kalshi API tier table (§6.1 Table 2)
> | Tier | Read Limit (per sec) | Write Limit (per sec) | Qualification Metric |
> | Basic | 20 | 10 | Completing signup |
> | Advanced | 30 | 30 | Completing API application |
> | Premier | 100 | 100 | 3.75% of monthly exchange volume |
> | Prime | 400 | 400 | 7.5% of monthly exchange volume |
[Source: 3_19 Kalshi Trading Strategy Research.docx, §6.1 Rate Limits by Access Tier, Table 2 ¶69-75]

### S16 — Batch endpoint weighting asymmetry (§6.2 Table 3 + ¶89)
> | Operation Type | Endpoint | Max Batch Size | Cost Per Order | Total Cost for Full Batch |
> | Create | POST /orders/batched | 20 | 1.0 token | 20 tokens |
> | Cancel | DELETE /orders/batched | 20 | 0.2 tokens | 4 tokens |
>
> "This asymmetric fee structure is critical for inventory risk management. When the LangGraph orchestrator detects an adverse macro shock via GDELT or FRED, the market-making module must rapidly withdraw liquidity to prevent adverse selection. The 0.2x weighting allows the system to clear 100 resting orders per second on the Basic tier, preserving rate limits for subsequent re-entry at more favorable prices."
[Source: 3_19 Kalshi Trading Strategy Research.docx, §6.2 Batch Operations and Transaction Weighting, Table 3 ¶83-87 + ¶89]

### S17 — WebSocket reciprocal-bid order book reconstruction (§7.1 ¶95)
> "A critical implementation nuance is that the Kalshi order book only transmits 'Bids'. Because the contracts are binary invariants where [P(YES)+P(NO)=1], an 'Ask' on the YES side is mathematically identical to a 'Bid' on the NO side. The local order book manager running within the Python environment must dynamically reconstruct the full Bid/Ask spread by calculating the reciprocal values of incoming Bids."
[Source: 3_19 Kalshi Trading Strategy Research.docx, §7.1 The Reciprocal Order Book Mechanism, ¶95]

### S18 — pykalshi SDK exception rationale (§8 ¶101)
> "The most robust community alternative is pykalshi (approx. 56-113 stars, MIT License). Despite falling below the 500-star filter (flagged as early-stage), a technical review indicates it drastically reduces implementation time. It natively supports WebSocket streaming, includes an OrderbookManager that handles the complex delta-snapshot merging and reciprocal bid/ask calculations automatically, and provides Pydantic v2 domain models. This aligns perfectly with the Cemini suite's existing Pydantic data contracts. Furthermore, it features automatic retries with exponential backoff to gracefully handle HTTP 429 rate limit errors, and outputs directly to Pandas/Polars DataFrames."
[Source: 3_19 Kalshi Trading Strategy Research.docx, §8 Python SDK Evaluation, ¶101]

### S19 — CFTC exclusive federal jurisdiction + state preemption (§9 ¶105-106)
> "As of early 2026, Kalshi operates as a Designated Contract Market (DCM) directly overseen by the Commodity Futures Trading Commission (CFTC). Following Kalshi's landmark judicial victories in 2024 and 2025, CFTC Chairman Michael S. Selig definitively affirmed the agency's stance: prediction markets trading event contracts are classified as commodity derivatives, placing them under the exclusive federal jurisdiction of the CFTC. This federal preemption serves as a massive protective moat. While certain state gaming authorities (e.g., in Massachusetts and Arizona) have attempted to issue injunctions characterizing sports and political prediction markets as unlicensed gambling, the CFTC has actively intervened in federal courts, asserting that state laws are preempted by the Commodity Exchange Act (CEA) to prevent regulatory fragmentation."
[Source: 3_19 Kalshi Trading Strategy Research.docx, §9 Regulatory Landscape and Institutional Viability (2026), ¶105-106]

### S20 — Feb 25 2026 CFTC Enforcement Advisory + Cemini compliance posture (§9.1 ¶108-110)
> "On February 25, 2026, the CFTC's Division of Enforcement issued a highly specific Advisory putting prediction market participants on notice regarding market manipulation. The advisory followed Kalshi's internal penalization of users who traded using Material Non-Public Information (MNPI)—specifically instances where individuals possessed advanced, non-public knowledge of an underlying event's resolution before it was broadly disclosed, or where they had the ability to influence the outcome directly. The CFTC emphasized that spoofing, pre-arranged trading, front-running, and exploiting MNPI are direct violations of the CEA and will be prosecuted federally. For the Cemini platform's specific modules (weather, Fed rates, social, BTC), this regulatory framework poses zero risk. Ingesting open-source ensemble weather model data (Open-Meteo) or utilizing macroeconomic calendar releases (FRED, SEC EDGAR) relies entirely on publicly accessible, non-privileged data. By generating alpha through superior statistical processing (Gumbel distributions, Bayesian Kelly sizing, and Logit-space AS modeling) rather than insider access, the system remains strictly compliant."
[Source: 3_19 Kalshi Trading Strategy Research.docx, §9.1 Algorithmic Trading and Bot Restrictions, ¶108-110]

### S21 — Final integration recipe (§10 ¶114-117)
> "Intelligence Layer (FastMCP / LangGraph): Expand the existing 5-agent Devil's Advocate debate protocol to monitor macro events. The system pulls FRED data and Open-Meteo ensembles, triggering a debate on whether a statistical edge exists relative to the Kalshi order book. Pricing Engine (Polars): When a consensus is reached, the Polars engine fits the data to a probability distribution (e.g., Gumbel for weather). It then applies the Bayesian Modified Kelly Criterion, adjusted for time-to-resolution and execution depth, to determine the optimal capital allocation. Market Making Layer: For designated markets, the engine calculates the Avellaneda-Stoikov reservation quotes and optimal spreads entirely within logit space, mitigating the infinite gamma risk of binary resolution. Execution Bus (Redis / FastAPI): The calculated orders are passed via the Redis pub/sub blackboard to the execution module. The module utilizes an audited version of the pykalshi library to manage the WebSocket connection, rebuilding the Bid/Ask spread from the Kalshi Bids-only stream. It routes limit orders via the BatchCreateOrders REST endpoint, leveraging the 0.2x cancellation weight of BatchCancelOrders to dynamically manage inventory, while carefully throttling payload sizes to respect the user tier's write limits."
[Source: 3_19 Kalshi Trading Strategy Research.docx, §10 Conclusion and Integration Roadmap, ¶114-117]
