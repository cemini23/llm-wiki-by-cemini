#!/usr/bin/env python3
"""Phase 2 spawn — writes entity + concept pages, patches source-stub backlinks,
promotes 9 unblocked-docx stubs draft→validated.

Idempotent-ish: overwrites entity/concept pages on each run; patches source
stubs by de-duplicating related: entries.
"""
from __future__ import annotations
import re
from datetime import date
from pathlib import Path

WIKI = Path("/Users/claudiobarone/Desktop/OSINT WORKSPACE/wiki")
TODAY = date.today().isoformat()  # 2026-04-23

# ---------- ENTITY DEFINITIONS ----------
# Each: (slug, category, title, tags, sources, narrative)
# Sources = list of source stub slugs; we build bidirectional `related:` from it.

ENTITIES: list[dict] = [
    # platforms
    dict(slug="kalshi", category="platforms",
         title="Kalshi",
         tags=["platform", "prediction-markets", "exchange", "cemini-venue"],
         sources=["3-10-cryptographic-research", "3-17-competition-research",
                  "3-19-alternative-data-for-prediction-markets-research",
                  "3-19-compliance-research", "3-19-ip-sale-research",
                  "3-19-kalshi-trading-strategy-research", "3-29-research-4",
                  "3-9-pm-research", "kalshi-2-3-29", "kalshi-3-3-29",
                  "kalshi-4-3-29", "osint-prediction-markets-trading-architecture"],
         related_concepts=["favorite-longshot-bias", "macro-weather-regime",
                           "ip-sale-readiness"],
         related_entities=["polymarket", "open-meteo"],
         narrative="""Kalshi is a CFTC-regulated designated contract market (DCM) for event
contracts — US-domiciled yes/no prediction markets on outcomes ranging from
weather and macroeconomic prints to elections and regulatory events. Within
Cemini it occupies three roles:

1. **Execution venue** — the Kalshi API (REST + WebSocket) is wired through
   the LangGraph scatter-gather topology alongside Alpaca and Hyperliquid;
   position sizing flows through the Kelly/CVaR risk engine.
2. **Alternative-data generator** — intraday price series on weather and
   event contracts provide a forward-looking signal layer that's fused with
   GDELT, FRED, and Open-Meteo ensembles before being dispatched to equity
   and crypto strategies.
3. **Compliance leverage point** — Kalshi's DCM status means event-contract
   trading sits under CFTC jurisdiction, which is structurally cleaner for
   an IP-sale-to-institutional-buyer story than operating on an unregistered
   offshore exchange.

Key microstructure facts documented across the corpus: the 2024 election-
contract ruling cemented Kalshi's regulatory moat; tick sizes are \$0.01 on
binary contracts; settlement is cash-only at \$1.00/\$0.00 on resolution;
the venue exhibits a strong favorite-longshot bias that several Cemini
strategies explicitly monetize via Avellaneda-Stoikov market-making in logit
space.""",
    ),
    dict(slug="polymarket", category="platforms",
         title="Polymarket",
         tags=["platform", "prediction-markets", "on-chain", "cemini-venue-adjacent"],
         sources=["3-19-kalshi-trading-strategy-research", "3-9-pm-research",
                  "kalshi-3-3-29", "kalshi-4-3-29",
                  "osint-prediction-markets-trading-architecture"],
         related_concepts=["favorite-longshot-bias", "publishers-exclusion"],
         related_entities=["kalshi"],
         narrative="""Polymarket is an on-chain prediction market running on Polygon, offering
USDC-denominated binary event contracts. For Cemini it primarily serves as
a **cross-venue price reference** — arbitrage and divergence signals
between Kalshi and Polymarket feed the signal-fusion engine — rather than a
primary execution venue, because US retail access is geofenced and because
the institutional buyer archetype targeted by the IP-sale thesis prefers
CFTC-regulated venues.

Documented across the corpus: Polymarket's AMM-adjacent LMSR mechanics
produce tighter spreads on political/macro contracts than Kalshi during
high-volume events; the lack of US retail access means retail-driven
favorite-longshot bias is weaker than on Kalshi, creating a useful
efficiency-gradient signal. Polymarket is explicitly flagged in the
compliance research as a venue Cemini can **reference** (via public
on-chain data) but not **execute on** without restructuring — hence its
status as a read-only data source in the current stack.""",
    ),
    dict(slug="hyperliquid", category="platforms",
         title="Hyperliquid",
         tags=["platform", "crypto", "perpetuals", "dex", "cemini-venue"],
         sources=["3-18-crypto-integration-technical-audit",
                  "3-19-compliance-research", "3-19-ip-sale-research",
                  "3-19-langgraph-scatter-gather-financial-analysis"],
         related_concepts=["cryptographic-audit-trail", "ip-sale-readiness"],
         related_entities=["ccxt"],
         narrative="""Hyperliquid is a high-performance on-chain perpetuals DEX with sub-second
block times and a fully on-chain orderbook. Cemini integrates via
**Hyperliquid Agent Wallets** — a delegated-signing pattern that lets the
trading agent submit orders from a hot wallet without exposing the master
seed. Orders are EIP-712 signed, routed through Flashbots Protect RPC to
mitigate MEV, and every on-chain transaction is logged into pg_tamperlog
before going to the Merkle-anchored audit ledger.

The venue is central to the crypto execution layer described in the 3-18
crypto integration technical audit: AES-GCM vault for agent-wallet private
keys, Web3.py for signing, CCXT for a normalized interface alongside
Binance/Bybit, and strict regime-gating through the Macro Weather system
before any perpetuals position is opened.""",
    ),
    dict(slug="oanda", category="platforms",
         title="OANDA",
         tags=["platform", "forex", "cfd", "cemini-venue"],
         sources=["3-19-compliance-research", "3-19-ip-sale-research",
                  "3-19-langgraph-scatter-gather-financial-analysis",
                  "forex-research-3-18"],
         related_concepts=["carry-trade", "macro-weather-regime"],
         related_entities=[],
         narrative="""OANDA is a retail-and-institutional forex broker used by Cemini as the
primary FX execution venue. The forex research documents the full
integration: v20 REST + streaming API, tick-level price feeds persisted to
TimescaleDB hypertables, and order submission through the scatter-gather
LangGraph topology with per-pair risk limits enforced by the Kelly/CVaR
engine.

OANDA's role in the IP-sale thesis is notable: unlike Alpaca (equities-
only) or Hyperliquid (crypto-only), OANDA provides **24/5 FX coverage** on
majors and crosses, which the compliance research flags as a requirement
for the intended institutional-buyer archetype. Documented strategies
include EUR/USD carry-trade variants, GBP/JPY mean-reversion in specific
regime windows, and a Macro-Weather-gated dispersion overlay on G10
crosses.""",
    ),
    dict(slug="alpaca", category="platforms",
         title="Alpaca",
         tags=["platform", "equities", "broker", "cemini-venue"],
         sources=["3-19-compliance-research", "3-19-ip-sale-research"],
         related_concepts=["ip-sale-readiness"],
         related_entities=[],
         narrative="""Alpaca is a US equities + options broker with a commission-free API-first
model. Within Cemini it's the primary equities execution venue, wired
through the same LangGraph scatter-gather topology as Hyperliquid and
OANDA. Paper and live accounts share the same API surface, which enables
the testing discipline the compliance research recommends: every live
strategy must first accumulate a shadow-paper record under the same
regime-gating rules before capital is allocated.

Key integration points documented: IEX market data feeds (free tier),
fractional share support for Kelly-fractional position sizing, and
regulatory reporting hooks that produce CSV exports suitable for the
milestone ledger that underpins the IP-sale narrative.""",
    ),

    # data-sources
    dict(slug="gdelt", category="data-sources",
         title="GDELT (Global Database of Events, Language, and Tone)",
         tags=["data-source", "alt-data", "news", "events"],
         sources=["3-17-git-research-pt2", "3-19-compliance-research",
                  "3-19-langgraph-scatter-gather-financial-analysis",
                  "3-29-research-4", "gdelt-1-3-29"],
         related_concepts=["cameo-codes", "goldstein-scale"],
         related_entities=["finbert", "fred"],
         narrative="""GDELT is an open dataset cataloging global news events in near-real-time,
with rich schema covering actor identities, CAMEO event codes, Goldstein
scale intensity, and tone scores. Cemini consumes GDELT 2.0 v2 tables via
Google BigQuery exports and streams incremental updates into TimescaleDB.

Primary uses in the stack:
- **Country-instability prediction** — aggregate Goldstein deltas per
  country over rolling windows feed a Bayesian deep-learning model
  flagged in the 3-29-research-4 paper.
- **Event-driven signal overlay** — high-Goldstein-intensity events
  matched to ticker entity lists generate short-window volatility
  forecasts consumed by the options and prediction-market strategies.
- **FinBERT input corpus** — tone-tagged headlines tied to specific
  tickers are re-scored by FinBERT to produce a sentiment feature
  orthogonal to GDELT's own tone score.""",
    ),
    dict(slug="fred", category="data-sources",
         title="FRED (Federal Reserve Economic Data)",
         tags=["data-source", "macro", "central-bank"],
         sources=["3-19-compliance-research", "3-19-kalshi-trading-strategy-research",
                  "3-19-langgraph-scatter-gather-financial-analysis"],
         related_concepts=["macro-weather-regime"],
         related_entities=[],
         narrative="""FRED is the Federal Reserve Bank of St. Louis's open data portal — ~800K
US and international macro time series. Cemini consumes FRED via the
official Python client (fredapi) with daily incremental pulls persisted to
TimescaleDB. Key series used across the corpus: DFF (effective fed funds),
DGS10 (10y treasury), VIXCLS (CBOE VIX), DCOILWTICO (WTI spot), DEXUSEU,
UNRATE, CPIAUCSL.

FRED series are the backbone of the **Macro Weather regime** classifier:
SPY vs its 21-EMA / 50-SMA gates are evaluated in the context of the
current Fed stance (DFF regime) and yield-curve shape (DGS10 - DGS2). The
compliance research also highlights FRED as a zero-vendor-risk data source
— open, redistributable, with no API-terms entanglement that would
complicate the IP-sale handoff.""",
    ),
    dict(slug="open-meteo", category="data-sources",
         title="Open-Meteo",
         tags=["data-source", "weather", "ensemble-forecasting"],
         sources=["3-17-competition-research", "3-19-kalshi-trading-strategy-research"],
         related_concepts=["ensemble-weather-forecasting"],
         related_entities=["kalshi"],
         narrative="""Open-Meteo is an open, no-API-key weather forecasting service aggregating
multiple numerical weather prediction (NWP) ensembles — ECMWF IFS, GFS,
ICON, MetNo, JMA. Cemini uses it as the primary input to the ensemble-
weather forecasting concept that feeds Kalshi weather event-contract
strategies.

Documented integration: hourly pulls of the ensemble forecast at specific
lat/lon points corresponding to Kalshi contract locations (e.g., NYC/LAX/
Chicago temperature contracts), fit into a Gumbel extreme-value
distribution to produce a probability distribution over the contract's
resolution bucket, then converted to a fair-value price that drives
Avellaneda-Stoikov market-making quotes in logit space. No API key + no
rate limit at the volumes Cemini uses = another zero-vendor-risk data
source, consistent with the IP-sale-readiness posture.""",
    ),
    dict(slug="finnhub", category="data-sources",
         title="Finnhub",
         tags=["data-source", "equities", "news", "fundamentals"],
         sources=["3-19-compliance-research", "3-19-kalshi-trading-strategy-research"],
         related_concepts=[],
         related_entities=["finbert", "gdelt"],
         narrative="""Finnhub is a commercial market-data API providing equities quotes,
fundamentals, earnings transcripts, company news, and sentiment. Cemini
uses Finnhub as a paid layer on top of IEX (via Alpaca) for:

- **Earnings transcript sentiment** — transcripts fed to FinBERT for
  quarterly surprise-augmentation signals.
- **Company news corpus** — news items cross-referenced with GDELT events
  to filter noise.
- **Fundamentals snapshots** — quarterly metrics used by the
  replacement-cost valuation concept on portfolio positions.

The compliance research notes Finnhub's per-user commercial license as a
minor deal-killer candidate during IP-sale due diligence — the acquiring
firm would need to re-negotiate the license under their entity — so the
milestone ledger tracks Finnhub-dependent feature flags separately from
fully-open-data features.""",
    ),
    dict(slug="telethon", category="data-sources",
         title="Telethon",
         tags=["library", "data-source", "alt-data", "messaging"],
         sources=["3-19-alternative-data-for-prediction-markets-research",
                  "3-19-telegram-discord-research"],
         related_concepts=[],
         related_entities=["finbert"],
         narrative="""Telethon is a Python MTProto library for reading Telegram channels and
groups as a user-agent (not a bot). Cemini uses Telethon to subscribe to
curated crypto-signal, macro-news, and sports/politics-commentary channels
whose message streams are tagged, de-duplicated, and scored by FinBERT
before being written to TimescaleDB as alt-data features.

Key architectural notes from the 3-19 Telegram/Discord research:
- User-agent MTProto (not Bot API) is required because many target
  channels don't publish a bot-accessible interface.
- Rate-limiting is aggressive on Telegram's side — Cemini stays well
  under limits via channel-rotation and cached join-state.
- The alt-data pipeline is explicitly flagged as a **publisher's-
  exclusion candidate**: institutional buyers may refuse to inherit
  Telegram-based alt-data feeds for reputational/compliance reasons,
  so this feature is gated behind a feature-flag that can be shipped-or-
  stripped for the IP-sale demo.""",
    ),

    # infrastructure
    dict(slug="hetzner", category="infrastructure",
         title="Hetzner",
         tags=["infrastructure", "vps", "hosting", "cemini-deployment"],
         sources=["3-10-cryptographic-research", "3-17-git-research-pt2",
                  "3-9-pm-research", "forex-research-3-18"],
         related_concepts=["ip-sale-readiness"],
         related_entities=[],
         narrative="""Hetzner is a German VPS provider hosting the Cemini production stack.
The current deployment is a single CPU-only dedicated server: AMD EPYC,
128GB RAM, 18–26 Docker containers via docker-compose (not Kubernetes —
deliberately), targeting cost efficiency over horizontal scale.

Documented architectural facts across the corpus:
- **CPU-only constraint** drives the choice of local LLM inference
  (DeepSeek-R1-14B on Ollama) over GPU-heavy alternatives; quant
  strategies rely on Polars/NumPy/CPU-native ML not on GPU acceleration.
- Server reference: `root@<see .local/server.md>`, path `/opt/cemini`.
- TimescaleDB + PostgreSQL + Redis + the LangGraph orchestrator +
  Prometheus/Loki/Grafana/Tempo stack + FastAPI app containers all co-
  tenant on the same host.
- IP-sale story: the whole stack reproduces from one docker-compose up
  on commodity CPU hardware — no vendor lock-in, no hyperscaler SLAs,
  no GPU-hour bills to untangle for the acquirer.""",
    ),
    dict(slug="ollama", category="infrastructure",
         title="Ollama",
         tags=["infrastructure", "llm-inference", "local-models"],
         sources=["3-18-crypto-integration-technical-audit",
                  "3-19-langgraph-scatter-gather-financial-analysis"],
         related_concepts=[],
         related_entities=["deepseek-r1-14b"],
         narrative="""Ollama is a local-inference runtime for open-weight LLMs, used by Cemini
to run DeepSeek-R1-14B on the CPU-only Hetzner host. The LangGraph scatter-
gather topology invokes Ollama via its OpenAI-compatible REST endpoint,
which keeps the code path identical across local inference and any future
hosted model — a deliberate abstraction for post-acquisition flexibility.

Documented performance envelope on the Hetzner host: DeepSeek-R1-14B
produces ~8–12 tok/s on CPU; scatter-gather calls are made in small
batches with tight token budgets so end-to-end strategy latency stays
within risk-engine timing windows. No API-key costs, no data-exfiltration
from the trading environment — both flagged as IP-sale-favorable
properties in the compliance research.""",
    ),
    dict(slug="deepseek-r1-14b", category="infrastructure",
         title="DeepSeek-R1-14B",
         tags=["infrastructure", "llm", "local-model", "reasoning"],
         sources=["3-18-crypto-integration-technical-audit",
                  "3-19-langgraph-scatter-gather-financial-analysis",
                  "3-19-telegram-discord-research"],
         related_concepts=[],
         related_entities=["ollama", "langgraph"],
         narrative="""DeepSeek-R1-14B is the 14-billion-parameter reasoning model that serves as
Cemini's primary local LLM. Chosen for the balance of reasoning quality
and CPU-tractable inference latency on a single 128GB-RAM Hetzner host.

Used across the stack for:
- **Scatter-gather financial analysis** (LangGraph) — spawns parallel
  subagent nodes that each digest a slice of the news/price/order-flow
  payload, then gathers into a single structured Pydantic-v2 output.
- **Telegram/Discord message classification** — score signal vs noise
  before persistence.
- **Compliance-report drafting** — the 3-19 compliance research notes
  DeepSeek-R1 produces audit-grade reasoning traces, which are preserved
  in pg_tamperlog for SCITT-compatible audit.

Weights are vendored locally (no HuggingFace Hub fetch at runtime) to
preserve reproducibility for the IP-sale handoff — the acquirer receives
the exact model blob that produced the claimed backtest results.""",
    ),
    dict(slug="timescaledb", category="infrastructure",
         title="TimescaleDB",
         tags=["infrastructure", "database", "time-series", "postgres"],
         sources=["3-10-cryptographic-research", "3-18-git-3",
                  "3-19-ip-sale-research", "3-19-kalshi-trading-strategy-research",
                  "3-19-telegram-discord-research",
                  "3-19-timescaledb-optimization-for-trading-platform",
                  "3-9-pm-research", "forex-research-3-18",
                  "osint-prediction-markets-trading-architecture"],
         related_concepts=["cryptographic-audit-trail"],
         related_entities=["pgvector", "redis"],
         narrative="""TimescaleDB is the time-series extension for PostgreSQL, Cemini's primary
persistence layer for tick data, order-flow, alt-data feeds, and strategy
P&L. It appears in 9 of the corpus sources — the most-referenced
infrastructure component after Kalshi.

Architectural choices documented across the 3-19 TimescaleDB optimization
research and crypto-integration audit:
- **Hypertables** partitioned by time (1-day chunks) with per-asset
  space partitioning; continuous aggregates precompute 1m/5m/1h/1d bars.
- **Compression policy** — tick data older than 7 days compresses with
  segment-by `(symbol)` + order-by `time DESC`, yielding ~12–18x storage
  reduction on forex and equities feeds.
- **Retention policy** — raw ticks dropped at 180 days; continuous
  aggregates retained indefinitely.
- **Cryptographic audit integration** — pg_tamperlog extension emits
  append-only receipts into a sibling schema; those receipts are Merkle-
  anchored via pymerkle before OpenTimestamps proof generation.""",
    ),
    dict(slug="redis", category="infrastructure",
         title="Redis",
         tags=["infrastructure", "cache", "pubsub", "streaming"],
         sources=["3-18-crypto-integration-technical-audit",
                  "3-19-ip-sale-research", "3-19-kalshi-trading-strategy-research",
                  "3-19-telegram-discord-research", "3-9-pm-research",
                  "forex-research-3-18"],
         related_concepts=["scatter-gather-topology"],
         related_entities=["timescaledb"],
         narrative="""Redis is the in-memory pub/sub and cache layer between Cemini's market-
data ingestion and strategy/execution layers. Sits in front of TimescaleDB
as a hot path for the current tick and a fanout to strategy subscribers.

Documented topology across the corpus:
- **Pub/sub channels** per venue + symbol (e.g., `oanda:EURUSD`,
  `hyperliquid:BTC-PERP`) feed the LangGraph scatter-gather nodes.
- **Redis Streams** used for durable event logs where at-least-once
  delivery matters (order submissions, fills) with consumer groups
  backed by the risk engine.
- **Rate-limit buckets** (INCR + EXPIRE) guard outbound API calls to
  Telegram (Telethon), Finnhub, Open-Meteo, and Kalshi.
- **Session cache** for Ollama prompt-completion pairs so repeated
  scatter-gather calls reuse reasoning traces within a strategy
  evaluation window.""",
    ),
    dict(slug="pgvector", category="infrastructure",
         title="pgvector",
         tags=["infrastructure", "database", "vector-db", "postgres-extension"],
         sources=["3-19-ip-sale-research", "3-19-telegram-discord-research",
                  "3-9-pm-research"],
         related_concepts=[],
         related_entities=["timescaledb", "finbert"],
         narrative="""pgvector is the PostgreSQL extension for vector similarity search. Co-
tenant with TimescaleDB in the same Postgres instance, which keeps the
stack footprint small (no separate vector database to operate or hand
over to the acquirer).

Primary uses in Cemini:
- **Research-corpus retrieval** — embed every source paper + transcript
  + Telegram message with FinBERT or an open sentence-encoder; query
  by HNSW index for relevant-context retrieval in LangGraph planning.
- **Event deduplication** — GDELT events embedded and compared by
  cosine distance to suppress duplicate-story flooding of strategy
  inputs.
- **Ticker-description similarity** — company-profile embeddings feed
  cluster-aware basket construction in dispersion-trading strategies.""",
    ),
    dict(slug="polars", category="infrastructure",
         title="Polars",
         tags=["library", "infrastructure", "dataframes", "rust"],
         sources=["3-19-compliance-research", "3-19-ip-sale-research",
                  "3-19-kalshi-trading-strategy-research"],
         related_concepts=[],
         related_entities=["timescaledb"],
         narrative="""Polars is a Rust-backed DataFrame library with a Python API, used as
Cemini's primary in-memory analytics layer in preference to pandas for
anything on the hot path. Chosen for the CPU-only Hetzner host because
its lazy query engine + Arrow memory layout meaningfully shortens
backtest and feature-engineering wall time.

Integration notes from the corpus:
- Read directly from TimescaleDB via the ConnectorX bridge for sub-
  second retrieval of multi-million-row tick slices.
- Core feature-engineering for the Kalshi trading strategy (rolling
  volatility, ensemble-weather conditional summaries, logit-space
  transforms) runs entirely in Polars.
- Backtest harness in the IP-sale research positions Polars + NumPy +
  scikit-learn + PyTorch-CPU as the **zero-GPU research pipeline** that
  the acquirer can reproduce on commodity hardware.""",
    ),

    # frameworks
    dict(slug="langgraph", category="frameworks",
         title="LangGraph",
         tags=["framework", "llm-orchestration", "agents"],
         sources=["3-10-cryptographic-research", "3-19-compliance-research",
                  "3-19-ip-sale-research", "3-19-kalshi-trading-strategy-research",
                  "3-19-langgraph-scatter-gather-financial-analysis",
                  "3-19-telegram-discord-research"],
         related_concepts=["scatter-gather-topology"],
         related_entities=["deepseek-r1-14b", "fastmcp"],
         narrative="""LangGraph is the agent-orchestration framework by LangChain that models
multi-step LLM workflows as Pregel-style BSP (bulk synchronous parallel)
graphs over typed state. Cemini uses it as the backbone of every
analytical pipeline involving an LLM.

Canonical pattern documented in the 3-19 LangGraph Scatter-Gather
Financial Analysis research:
- **Send API** for dynamic fan-out — one supervisor node dispatches N
  subagent nodes, each handling a slice of the payload.
- **typing.Annotated[..., operator.add] reducers** accumulate partial
  results into a shared state dict without lock contention.
- **Checkpointer** persists state to PostgreSQL so interrupted runs
  resume cleanly — critical for strategies running in market hours.

LangGraph's explicit graph structure doubles as an **audit artifact**:
every node execution + state transition is serialized and can be
replayed deterministically, which the compliance research highlights as
a key IP-sale-readiness feature (the acquirer gets reproducible
reasoning traces, not an inscrutable agentic blob).""",
    ),
    dict(slug="fastapi", category="frameworks",
         title="FastAPI",
         tags=["framework", "web", "api", "python"],
         sources=["3-18-crypto-integration-technical-audit",
                  "3-19-langgraph-scatter-gather-financial-analysis",
                  "3-19-telegram-discord-research", "forex-research-3-18"],
         related_concepts=[],
         related_entities=["pydantic-v2"],
         narrative="""FastAPI is the Python web framework that exposes Cemini's control plane:
strategy-start/stop endpoints, health/metrics for Prometheus scraping,
audit-report endpoints, and a read-only dashboard API consumed by
Grafana. Paired with Pydantic v2 for request/response validation, it
generates the OpenAPI spec that's shipped as part of the IP-sale
deliverable.

Documented details:
- Runs behind Uvicorn with async workers, co-resident on the Hetzner
  host with the LangGraph orchestrator and TimescaleDB.
- Schemathesis consumes the OpenAPI spec to produce property-based
  API tests — cited in the 3-19 compliance research as the
  institutional-grade-testing-signal that buyers look for.""",
    ),
    dict(slug="fastmcp", category="frameworks",
         title="FastMCP",
         tags=["framework", "mcp", "llm-tooling", "python"],
         sources=["3-19-compliance-research", "3-19-ip-sale-research",
                  "3-19-kalshi-trading-strategy-research",
                  "3-19-langgraph-scatter-gather-financial-analysis"],
         related_concepts=["skill-vetting"],
         related_entities=["langgraph"],
         narrative="""FastMCP is a Python framework for building Model Context Protocol (MCP)
servers — the Anthropic-originated standard for LLM-tool interaction.
Cemini exposes its internal toolkits (position lookup, venue order
submission, historical-data query, risk-check) as MCP servers so that
the LangGraph DeepSeek-R1 agents call them through a uniform, typed,
permission-gated interface.

Why FastMCP matters to the IP-sale thesis: MCP is the emerging
cross-vendor tooling standard. By wrapping all Cemini capabilities
behind MCP servers, the acquiring firm can swap the local DeepSeek-R1
agent for any compliant MCP client (Claude, GPT-class models, their
own fine-tunes) without rewriting the tool layer. This decouples the
trading logic from any single LLM provider — a deal-favorable piece of
forward-compatibility.""",
    ),
    dict(slug="pydantic-v2", category="frameworks",
         title="Pydantic v2",
         tags=["library", "framework", "validation", "python"],
         sources=["3-10-cryptographic-research", "3-18-crypto-integration-technical-audit",
                  "3-19-compliance-research", "3-19-langgraph-scatter-gather-financial-analysis",
                  "forex-research-3-18"],
         related_concepts=[],
         related_entities=["fastapi"],
         narrative="""Pydantic v2 is the Rust-backed data-validation library underpinning every
typed boundary in Cemini: FastAPI request/response models, LangGraph
state schemas, config files, CCXT response-normalization adapters, and
order submission payloads to every venue.

Architectural significance per the corpus:
- **Single source of truth** — Pydantic models are code-generated into
  JSON Schema for the OpenAPI spec, and into TypedDict for LangGraph
  state reducers, eliminating drift between API contracts and internal
  state shape.
- **Audit-safe serialization** — `model_dump_json()` is deterministic
  and feeds directly into pg_tamperlog, so every LLM-produced
  reasoning artifact has a canonical, hashable form for Merkle
  anchoring.
- **IP-sale clarity** — the acquirer reads the Pydantic model
  catalogue and immediately understands the full data model; no
  tribal knowledge required.""",
    ),
    dict(slug="ccxt", category="frameworks",
         title="CCXT",
         tags=["library", "framework", "crypto", "exchange-connectivity"],
         sources=["3-18-crypto-integration-technical-audit",
                  "3-19-compliance-research"],
         related_concepts=[],
         related_entities=["hyperliquid"],
         narrative="""CCXT is the Python crypto-exchange-connectivity library providing a
normalized interface over 100+ venues. Cemini uses CCXT to abstract
Hyperliquid, Binance, Bybit, and Coinbase Advanced behind a single
order-submission and market-data surface.

Documented choices:
- **Only-CEX** venues go through CCXT. Hyperliquid (on-chain perp DEX)
  uses its native SDK + CCXT's contributed adapter simultaneously —
  orders double-sign for the tamper-evident audit trail.
- **Rate-limit budgeting** — CCXT's built-in throttling is
  supplemented by a Redis-backed global rate-limit layer because
  multiple strategy instances share credentials.
- **Deal-killer flag** per the compliance research: CCXT's MIT license
  is clean, but some venue-specific adapters bundle venue-provided
  snippets with murkier licenses — the IP-sale due-diligence ledger
  tracks these per-adapter.""",
    ),
    dict(slug="nautilustrader", category="frameworks",
         title="NautilusTrader",
         tags=["framework", "trading", "backtest", "cython"],
         sources=["3-10-cryptographic-research", "3-19-ip-sale-research",
                  "trading-playbook-research"],
         related_concepts=["ip-sale-readiness"],
         related_entities=[],
         narrative="""NautilusTrader is an open-source, Cython-accelerated trading platform
offering a unified backtest + live-trading engine with a message-passing
architecture. Cemini uses it as the **reference backtest harness** — the
framework an institutional buyer can run the shipped strategies against
to independently reproduce P&L numbers.

Why it matters in the IP-sale context per the trading playbook research:
- **Deterministic replay** — event-sourced architecture means a given
  tick tape + strategy config produces identical fills across runs, a
  property the acquirer's quant team will verify during due diligence.
- **Venue adapters** parallel CCXT for crypto and include dedicated
  interactive-brokers/Alpaca adapters, so the backtest harness matches
  the production execution path.
- **Isolation from Cemini's proprietary logic** — NautilusTrader is
  the ingestion + execution skeleton; the strategy logic sits in
  separate repos so the acquirer can evaluate them independently of
  the harness.""",
    ),
    dict(slug="torchrl", category="frameworks",
         title="TorchRL",
         tags=["framework", "reinforcement-learning", "pytorch"],
         sources=["3-19-ip-sale-research", "3-19-telegram-discord-research"],
         related_concepts=["mappo"],
         related_entities=["pettingzoo"],
         narrative="""TorchRL is Meta's reinforcement-learning library built on PyTorch. Cemini
uses it for the MARL (multi-agent reinforcement learning) research track
— specifically MAPPO (Multi-Agent PPO) configurations over PettingZoo
environments that simulate multi-venue execution.

Documented scope per the corpus:
- Training runs are **CPU-only** on the Hetzner host — small-batch,
  long-horizon, not SOTA-scale. Research-grade not production-policy.
- Checkpoints serialized into the model-registry schema alongside
  DeepSeek-R1 weights so the IP-sale bundle is self-contained.
- Observations and rewards use Pydantic-v2-validated shapes end-to-
  end, preserving the audit-trail property across RL training runs.""",
    ),
    dict(slug="pettingzoo", category="frameworks",
         title="PettingZoo",
         tags=["framework", "reinforcement-learning", "multi-agent", "environments"],
         sources=["3-19-ip-sale-research", "3-19-telegram-discord-research"],
         related_concepts=["mappo"],
         related_entities=["torchrl"],
         narrative="""PettingZoo is the multi-agent counterpart to Gymnasium — a library of
shared-environment interfaces for multi-agent RL. Cemini defines custom
PettingZoo environments modeling multi-venue execution problems:

- **MultiVenueExecEnv** — one agent per venue (Alpaca, OANDA,
  Hyperliquid, Kalshi), shared observation space over the market-wide
  state, reward shaped by portfolio-level Sharpe + slippage.
- **AlphaDecayEnv** — agents compete for finite alpha across
  correlated strategies; used to study strategy-portfolio capacity.

Trained via TorchRL + MAPPO on the Hetzner CPU host. The RL artifacts
are **research, not production policy** per the IP-sale compliance note
— the institutional buyer evaluates them as evidence of sophisticated
R&D, not as shipped trading logic.""",
    ),
    dict(slug="finbert", category="frameworks",
         title="FinBERT",
         tags=["model", "nlp", "finance", "sentiment"],
         sources=["3-10-cryptographic-research", "3-17-git-research-pt2",
                  "3-29-research-4"],
         related_concepts=[],
         related_entities=["gdelt", "telethon", "finnhub"],
         narrative="""FinBERT is the BERT variant fine-tuned on financial text for three-class
sentiment (positive/negative/neutral). Cemini runs a vendored FinBERT
checkpoint locally for sentiment scoring across every text feed:

- **GDELT headlines** — tone-adjusted score orthogonal to GDELT's
  native tone.
- **Finnhub earnings-call transcripts** — per-paragraph sentiment
  rolled up by speaker (CEO vs CFO vs analyst) for quarterly
  surprise signals.
- **Telegram / Discord messages** — score first, persist, then
  downstream strategies subscribe by sentiment-bucket.
- **Cemini-internal research notes** — embedded via pgvector for
  retrieval; sentiment score used as a research-corpus filter.

The weights are small (~440MB) and run comfortably on CPU, fitting
the Hetzner zero-GPU constraint.""",
    ),

    # observability
    dict(slug="prometheus", category="observability",
         title="Prometheus",
         tags=["observability", "metrics", "monitoring"],
         sources=["3-19-compliance-research", "3-19-kalshi-trading-strategy-research"],
         related_concepts=[],
         related_entities=["grafana", "loki", "tempo"],
         narrative="""Prometheus is the metrics scraper in Cemini's observability stack. Pulls
/metrics endpoints from every FastAPI service, the LangGraph
orchestrator, TimescaleDB, Redis, and per-strategy exporters that
surface P&L, position, and risk-engine state.

Documented cardinality discipline per the compliance research: labels
are **venue + symbol + strategy_id** — no per-order labels — so series
count stays bounded. Long-term retention offloads to a Thanos sidecar
(reference, not mandatory for the IP-sale demo).""",
    ),
    dict(slug="loki", category="observability",
         title="Loki",
         tags=["observability", "logs", "monitoring"],
         sources=["3-19-compliance-research", "3-19-kalshi-trading-strategy-research"],
         related_concepts=[],
         related_entities=["grafana", "prometheus", "tempo"],
         narrative="""Loki is the Grafana-stack log aggregator — label-indexed, not full-text
indexed, which keeps storage costs low. Cemini ships structured JSON
logs from every container through Promtail into Loki; the LangGraph
orchestrator emits run-id / node-id / tool-call labels so logs join
cleanly with traces in Tempo.

Explicit IP-sale note: the log schema is documented as part of the
milestone ledger deliverable so the acquirer can reproduce any
incident investigation on their own Loki deployment.""",
    ),
    dict(slug="grafana", category="observability",
         title="Grafana",
         tags=["observability", "dashboards", "monitoring"],
         sources=["3-19-compliance-research", "3-19-kalshi-trading-strategy-research"],
         related_concepts=[],
         related_entities=["prometheus", "loki", "tempo"],
         narrative="""Grafana is the unified dashboard layer over Prometheus metrics, Loki
logs, and Tempo traces. Cemini ships a curated dashboard set:
per-strategy P&L, per-venue fill latency, LangGraph-run traces, risk-
engine state, and a macro-weather regime panel.

Dashboards are **committed as JSON** alongside the code so every
dashboard change is version-controlled and included in the IP-sale
handoff — no click-ops configuration to reconstruct post-acquisition.""",
    ),
    dict(slug="tempo", category="observability",
         title="Tempo",
         tags=["observability", "tracing", "monitoring"],
         sources=["3-19-compliance-research", "3-19-kalshi-trading-strategy-research"],
         related_concepts=[],
         related_entities=["grafana", "prometheus", "loki"],
         narrative="""Tempo is the Grafana-stack distributed-tracing backend. Cemini
instruments every inter-service call (FastAPI ↔ LangGraph ↔ Ollama ↔
Redis ↔ TimescaleDB ↔ venue adapters) with OpenTelemetry spans.

The trace-stream has a secondary purpose beyond performance
debugging: each span's (trace_id, service, operation, attrs) tuple is
written into pg_tamperlog as an audit event, giving the Merkle-
anchored ledger a second independent signal of strategy execution.
This is called out in the 3-19 compliance research as a
'defense-in-depth' audit posture valued by institutional buyers.""",
    ),

    # security / supply-chain
    dict(slug="syft", category="security",
         title="Syft",
         tags=["security", "sbom", "supply-chain"],
         sources=["3-17-competition-research", "github-action-and-workflow-research"],
         related_concepts=["sbom"],
         related_entities=["cyclonedx", "trivy"],
         narrative="""Syft generates Software Bill of Materials (SBOM) artifacts from source
repos and container images. Cemini's CI pipeline produces CycloneDX-
format SBOMs with Syft on every build; the SBOM is attached as a
release artifact alongside the binary + signed attestation.

Documented motivation from the github-action-and-workflow research: an
institutional IP-sale buyer's supply-chain-security team will demand
SBOMs for every shipped artifact — having them auto-generated and
attested is a differentiator vs competing IP sellers who hand over
source tarballs without provenance.""",
    ),
    dict(slug="cyclonedx", category="security",
         title="CycloneDX",
         tags=["security", "sbom", "standard"],
         sources=["3-17-competition-research", "github-action-and-workflow-research"],
         related_concepts=["sbom"],
         related_entities=["syft"],
         narrative="""CycloneDX is the OWASP-maintained SBOM standard Cemini uses. Chosen
over SPDX for richer vulnerability- and service-descriptor schemas. The
Syft-produced SBOM is CycloneDX-formatted JSON, signed with cosign, and
published alongside every release.

The format choice is small but material in the IP-sale context: both
CycloneDX and SPDX are acceptable to most acquirers, but CycloneDX's
first-class service and license-expression fields map cleanly to the
deal-killer ledger (CCXT adapter licenses, Finnhub's commercial
license) without extra tooling.""",
    ),
    dict(slug="trivy", category="security",
         title="Trivy",
         tags=["security", "vulnerability-scan", "containers"],
         sources=["3-19-ip-sale-research", "github-action-and-workflow-research"],
         related_concepts=[],
         related_entities=["syft", "semgrep"],
         narrative="""Trivy is Aqua Security's vulnerability scanner for container images,
IaC, and dependency manifests. Cemini's CI runs Trivy on every image
build + every Python requirements lock update; the CI gate fails on
HIGH or CRITICAL CVEs in Cemini's direct dependency graph (transitive
CVEs with no upstream fix are tracked but not blocked).

The IP-sale research frames Trivy output as a **continuous due-diligence
signal**: the acquirer inherits a living vulnerability posture rather
than a point-in-time snapshot, and the same tooling keeps running
post-transfer without rewiring.""",
    ),
    dict(slug="semgrep", category="security",
         title="Semgrep",
         tags=["security", "sast", "static-analysis"],
         sources=["3-19-ip-sale-research", "github-action-and-workflow-research"],
         related_concepts=[],
         related_entities=["trivy"],
         narrative="""Semgrep is the rule-based SAST tool running on every Cemini pull
request. Rule packs used: OWASP Top Ten, Python secrets detection,
SQL-injection patterns, and a custom Cemini ruleset covering
venue-credential-handling antipatterns (no hardcoded keys; AES-GCM
vault for any private-key material; no eval on LLM output).

Cited in the IP-sale and compliance research as the primary
defensive-coding signal Cemini can show institutional buyers without
compromising on velocity — Semgrep rules run in ~30 seconds so PRs
aren't blocked on slow scanners.""",
    ),

    # components (Cemini-built)
    dict(slug="kelly-cvar-risk-engine", category="components",
         title="Kelly/CVaR risk engine",
         tags=["component", "cemini-internal", "risk", "position-sizing"],
         sources=["3-10-cryptographic-research", "3-19-ip-sale-research",
                  "3-19-kalshi-trading-strategy-research", "trading-playbook-research"],
         related_concepts=["macro-weather-regime", "ip-sale-readiness"],
         related_entities=[],
         narrative="""The Kelly/CVaR risk engine is Cemini's position-sizing and
portfolio-risk module. It combines a **fractional-Kelly sizer**
(typically 0.1–0.3 Kelly to control drawdown variance) with a
**CVaR-95% cap** (the position is clipped if it would push expected
5%-tail loss above a configured threshold).

Invocation pattern across the corpus:
- Every strategy emits a target position + a signal-edge estimate.
- The risk engine computes Kelly-optimal size from the edge + the
  strategy-specific variance estimate.
- A portfolio-level CVaR recalc runs after each candidate position
  change; any candidate that breaches the portfolio CVaR budget is
  clipped or rejected.
- The Macro Weather regime gate sits **in front of** the risk engine:
  GREEN → full Kelly fraction; YELLOW → halved; RED → flat-or-hedge-
  only.

Flagged explicitly as Cemini-proprietary in the IP-sale research —
the combination of regime-gating + Kelly/CVaR + LangGraph-logged
reasoning is the piece institutional buyers cannot easily recreate
from open-source primitives, and so commands the premium valuation.""",
    ),
]

# ---------- CONCEPT DEFINITIONS ----------
CONCEPTS: list[dict] = [
    dict(slug="ip-sale-readiness",
         title="IP-sale-readiness",
         tags=["concept", "cemini-internal", "m-and-a", "strategy"],
         sources=["3-10-algorithmic-trading-ip-sale-audit",
                  "3-10-cryptographic-research",
                  "3-18-crypto-integration-technical-audit",
                  "3-19-compliance-research", "3-19-ip-sale-research",
                  "3-19-kalshi-trading-strategy-research",
                  "3-19-langgraph-scatter-gather-financial-analysis",
                  "3-19-telegram-discord-research", "forex-research-3-18",
                  "trading-playbook-research"],
         related_entities=["hetzner", "langgraph", "nautilustrader",
                           "pydantic-v2", "kelly-cvar-risk-engine"],
         related_concepts=["cryptographic-audit-trail",
                           "replacement-cost-valuation",
                           "publishers-exclusion",
                           "irc-1235-capital-gains-safe-harbor",
                           "milestone-ledger"],
         narrative="""**IP-sale-readiness** is the cross-cutting posture that frames every
architecture choice in the 10 most-recent Cemini-internal research docs.
The thesis: the Cemini Financial Suite is being built not as a lifestyle
prop-trading shop but as an acquisition target for a proprietary trading
firm, fintech, or systematic hedge fund looking to buy a turnkey
multi-asset platform.

### Core readiness components
1. **Reproducibility** — one docker-compose on commodity CPU hardware
   reproduces the whole stack. No GPUs, no hyperscaler lock-in, no
   vendor SaaS without a zero-cost local fallback.
2. **Typed everything** — Pydantic v2 at every boundary, OpenAPI
   spec generated from code, LangGraph state schemas serialized.
3. **Audit trail** — pg_tamperlog → pymerkle → OpenTimestamps →
   VeritasChain Protocol Silver Tier. Every LLM reasoning trace,
   every order, every position change is cryptographically anchored.
4. **Test posture** — Ruff + Semgrep + Trivy + Schemathesis +
   Hypothesis + mutmut, all wired into CI, all producing artifacts
   the acquirer inherits.
5. **Milestone ledger** — each feature shipped is recorded against
   an explicit milestone so the acquirer reads a linear narrative
   from initial commit to the current code, not a pile of disjoint
   PRs.
6. **Tax + legal structure** — Florida single-member LLC with IRC
   §1235 capital-gains safe harbor on IP transfer; asset-purchase
   agreement template with earnout tiers pre-drafted.

### Deal-killer ledger
Specific items tracked separately because they'd torpedo the sale if
undiscovered in due diligence: CCXT venue-adapter license ambiguities,
Finnhub commercial license per-entity restrictions, Telegram-channel
alt-data (publisher's-exclusion candidate), any GPL-contaminated
dependency, any model weight whose license forbids commercial
re-distribution, and any personal data persisted without a clear
retention schedule.""",
    ),
    dict(slug="cryptographic-audit-trail",
         title="Cryptographic audit trail",
         tags=["concept", "audit", "cryptography", "cemini-internal"],
         sources=["3-10-cryptographic-research",
                  "3-18-crypto-integration-technical-audit",
                  "3-19-compliance-research"],
         related_entities=["timescaledb"],
         related_concepts=["ip-sale-readiness", "milestone-ledger"],
         narrative="""Cemini's cryptographic audit trail is a layered tamper-evident ledger
spanning every order, position change, and LLM reasoning artifact. The
design is derived from SCITT (Supply Chain Integrity, Transparency,
and Trust) principles and targets the VeritasChain Protocol v1.1 Silver
Tier.

### Stack (bottom-up)
1. **pg_tamperlog** — PostgreSQL extension producing append-only
   receipts for every write to the audited tables. Schema-bound, so
   an attacker who gains DB write access cannot silently mutate the
   history.
2. **pymerkle** — RFC 6962-compatible Merkle tree built over
   pg_tamperlog receipts in configurable windows (typical: 1 min for
   hot tables, 1 h for cold). Merkle root signed with the Cemini
   operator key.
3. **OpenTimestamps** — submits the signed root to the Bitcoin
   blockchain via OpenTimestamps calendar servers, producing a
   publicly-verifiable timestamp proof.
4. **VeritasChain Protocol (VCP) v1.1 Silver Tier** — the publication
   envelope: bundles the OpenTimestamps proof, the Merkle root, the
   pg_tamperlog range, and the relevant Pydantic-v2 schemas into a
   single JSON-LD document suitable for third-party verification.

### What's anchored
- All order submissions, fills, and venue-ack responses across
  Alpaca/OANDA/Hyperliquid/Kalshi.
- Every LangGraph state transition + DeepSeek-R1 reasoning trace.
- Risk-engine decisions (position-sizing, CVaR-clip events).
- Macro Weather regime transitions.
- Milestone-ledger commits.

The effect: an IP-sale buyer can independently verify — via Bitcoin-
anchored timestamp proofs — that any backtest-reproduction run on the
shipped stack matches the claimed historical record. This is the
single biggest differentiator vs prop-shop IP that typically ships as
code + CSV backtest output with no independent verifiability.""",
    ),
    dict(slug="scatter-gather-topology",
         title="Scatter-gather topology (LangGraph)",
         tags=["concept", "llm-orchestration", "methodology"],
         sources=["3-19-langgraph-scatter-gather-financial-analysis"],
         related_entities=["langgraph", "deepseek-r1-14b"],
         related_concepts=[],
         narrative="""Scatter-gather is Cemini's canonical LLM-agent topology for financial
analysis tasks, implemented via LangGraph's Send API + Pregel BSP model.

### The pattern
1. **Supervisor node** receives the task (e.g., "analyze the last 24h
   of GDELT + price + order-flow for ticker X and return a
   Pydantic-v2 StrategyRecommendation").
2. **Fan-out via Send** — the supervisor dispatches N subagent nodes,
   one per data slice (news, fundamentals, microstructure,
   alt-data, cross-asset context). Each subagent gets its own
   DeepSeek-R1 reasoning context, typed state, and tool-budget.
3. **Shared state with operator.add reducers** — each subagent
   writes its Pydantic-typed partial result into a shared state dict
   whose keys are merged, not overwritten, via `typing.Annotated[…,
   operator.add]`.
4. **Gather node** reads the merged state, resolves any cross-slice
   contradictions, and emits a single final Pydantic output.

### Why it works on CPU-only
No single reasoning pass has to hold the entire payload in context —
each subagent sees a curated slice. DeepSeek-R1-14B's ~8–12 tok/s on
CPU becomes tolerable because the slices run in parallel at the
subprocess level and the token budget per subagent is tight.

### Audit properties
Every Send edge + every reducer application is checkpointed to
PostgreSQL. The pg_tamperlog receipts for those checkpoints feed the
cryptographic audit trail, so the full reasoning graph is deterministically
replayable for IP-sale due diligence.""",
    ),
    dict(slug="macro-weather-regime",
         title="Macro Weather regime",
         tags=["concept", "cemini-internal", "risk", "regime"],
         sources=["trading-playbook-research",
                  "3-19-kalshi-trading-strategy-research",
                  "3-19-compliance-research"],
         related_entities=["fred", "kelly-cvar-risk-engine"],
         related_concepts=["ip-sale-readiness", "game-of-attrition-doctrine"],
         narrative="""The **Macro Weather regime** is Cemini's simple, auditable portfolio-
gate classifier. It uses two signals on SPY — the 21-EMA and the
50-SMA — cross-referenced with a small set of FRED macro series, to
produce one of three regime states:

- **GREEN**: SPY > 21-EMA AND SPY > 50-SMA. Permissive regime. Full
  Kelly fraction allowed; new risk may be added.
- **YELLOW**: price between 21-EMA and 50-SMA (either side). Defensive.
  Kelly fraction halved; no new uncorrelated risk; existing positions
  tightened.
- **RED**: SPY < 21-EMA AND SPY < 50-SMA. Flat-or-hedge-only. All
  directional risk flattened or hedged; only market-making style
  strategies (Kalshi AS-in-logit, forex scalping) continue.

### Why these two moving averages
The trading-playbook research argues, and several RL-based regime
classifiers confirm in ablations, that 21-EMA captures ~1-month trend
and 50-SMA captures ~2.5-month trend; their crossover vs price
together identifies three distinct drawdown-risk regimes without
over-fitting.

### Why it sits at the top of the stack
The regime classifier is evaluated **before** the Kelly/CVaR risk
engine, which is evaluated **before** the strategy-specific signal.
This inverts the usual strategy-first → risk-second ordering and is
framed in the corpus as the **Game of Attrition doctrine**: survive
first, compound second. The regime flag is cheap to compute,
auditable, and caps all downstream risk — which is exactly what an
IP-sale buyer wants to see at the top of the stack.""",
    ),
    dict(slug="favorite-longshot-bias",
         title="Favorite-longshot bias (FLB)",
         tags=["concept", "prediction-markets", "behavioral"],
         sources=["3-19-kalshi-trading-strategy-research"],
         related_entities=["kalshi", "polymarket"],
         related_concepts=[],
         narrative="""The **favorite-longshot bias** is the robust empirical finding that
prediction-market participants systematically overpay for longshot
(low-probability) outcomes and underpay for favorites. On Kalshi event
contracts, the bias manifests as longshot contracts (quoted at
\$0.05–0.15) trading above their fair implied probability, and favorites
(\$0.85–0.95) trading slightly below.

### Cemini's strategies that monetize FLB
1. **Favorite-side market-making** — Avellaneda-Stoikov quotes in
   **logit space** on favorites, capturing the bias as a consistent
   drift term. Positive skew even after venue fees.
2. **Longshot-fade** — fade grossly-mispriced longshots when the
   implied-probability delta vs a Gumbel-fit model exceeds a
   threshold; position-sized by Kelly-fractional.
3. **FLB arbitrage across venues** — Polymarket (less retail-driven)
   typically shows weaker FLB than Kalshi. Cross-venue legs capture
   the efficiency gradient.

### Why FLB persists
Behavioral: loss-aversion distorts small-probability weighting; retail
bettors chase payoff, not expected value. Structural: longshot
contracts have wider spreads on Kalshi, making arbitrage capital-
expensive; the market-maker inventory is typically positioned against
the bias, creating a quasi-equilibrium that never fully closes.""",
    ),
    dict(slug="replacement-cost-valuation",
         title="Replacement-cost valuation",
         tags=["concept", "m-and-a", "valuation"],
         sources=["3-10-cryptographic-research", "3-10-algorithmic-trading-ip-sale-audit"],
         related_entities=["kelly-cvar-risk-engine"],
         related_concepts=["ip-sale-readiness"],
         narrative="""**Replacement-cost valuation** is the framing the IP-sale research
recommends as the primary valuation anchor for the Cemini Financial
Suite — independent of P&L track record.

### The argument
An institutional buyer who decides to build an equivalent multi-asset
algorithmic-trading platform in-house would need, conservatively: 3–5
senior quants + 2 infra/devops engineers + 1 compliance lead + access
to TimescaleDB/Hyperliquid/Kalshi/OANDA integrations + a verified
Merkle-anchored audit trail + a trained DeepSeek-R1 reasoning harness
+ documented RL-research program + a cryptographically-provable
backtest record.

Replacement-cost estimate per the 3-10 cryptographic audit runs to
18–24 person-months of senior engineering effort + 6–9 months of
real-money paper-trading to generate a comparable track record. At
loaded senior-engineer costs + opportunity cost of delay, the
replacement envelope sits in the low-to-mid seven figures.

### Why this beats DCF or multiple-of-earnings
Cemini is pre-revenue for acquisition purposes. Multiples-of-earnings
on a prop book are distorted by leverage and regime. Replacement cost
gives both sides an auditable number that doesn't depend on projecting
out-of-sample returns — which an acquirer's risk-committee will
haircut aggressively anyway.

### Floor-price vs ceiling
Replacement cost is the floor. The ceiling is set by the acquirer's
own strategic value: the cost of NOT having the platform when a
competitor launches theirs. The IP-sale negotiation playbook structures
this as a base price (replacement-anchored) + earnout tiers tied to
strategy performance on the acquirer's capital.""",
    ),
    dict(slug="dispersion-trading",
         title="Dispersion trading",
         tags=["concept", "options", "volatility", "strategy"],
         sources=["trading-playbook-research"],
         related_entities=["kelly-cvar-risk-engine"],
         related_concepts=["macro-weather-regime"],
         narrative="""**Dispersion trading** sells index-level implied volatility while buying
single-name implied volatility on the constituent basket. The P&L
source is the gap between implied index vol (usually rich, due to
correlation premium) and the realized dispersion across names.

### Cemini's implementation per the trading-playbook research
- Universe: SPX components via liquid options on the top ~50 weights.
- Weights: vega-matched; index-short leg sized to ~1% of NAV vega-
  weighted.
- Gating: **Macro Weather GREEN only**. In YELLOW/RED, correlations
  spike, dispersion collapses, and the trade bleeds theta without
  the usual realized-dispersion payoff. This gating is cited as the
  empirical distillation of why retail dispersion traders blow up in
  drawdowns — they don't gate on regime.
- Hedging: dynamic delta + vega re-hedge, driven by the scatter-
  gather analyst that digests FRED + GDELT + cross-asset cues and
  emits a regime-confidence score.

### Institutional interest
Dispersion is explicitly called out in the IP-sale research as one
of the **highest-value strategies** in the Cemini portfolio for the
institutional-buyer archetype — complex enough to demand real
options-vol infrastructure, simple enough to explain to a risk
committee, and capacity-scalable up to the buyer's own book size.""",
    ),
    dict(slug="game-of-attrition-doctrine",
         title="Game-of-Attrition doctrine",
         tags=["concept", "strategy", "risk-philosophy", "cemini-internal"],
         sources=["trading-playbook-research"],
         related_entities=["kelly-cvar-risk-engine"],
         related_concepts=["macro-weather-regime", "ip-sale-readiness"],
         narrative="""The **Game of Attrition doctrine** is the risk-philosophy framing that
runs through the trading-playbook research: in an infinite-horizon
compounding game, survival dominates expected return. The doctrine
prescribes three operating rules:

1. **Regime gate before signal** — the Macro Weather classifier
   decides whether the portfolio trades at all before any strategy-
   specific signal is evaluated. Losing strategies survive RED by
   being flat; a winning strategy in the wrong regime is still a
   losing strategy.
2. **Fractional Kelly by default** — never full Kelly. 0.1–0.3
   Kelly reduces expected growth modestly but slashes drawdown
   volatility enough that the LLN grinds in your favor over
   realistic sample paths.
3. **CVaR cap on top** — even fractional Kelly can pick up tail risk
   the sizer doesn't see. The portfolio CVaR-95% cap bounds the
   worst-case outcome per bet independent of the Kelly math.

### Why it's Cemini's North Star
The doctrine is explicitly positioned in the trading-playbook research
as the organizing principle that makes Cemini defensibly different
from strategy-first prop shops. An acquirer's risk committee reads
"regime → Kelly → CVaR" at the top of the stack and immediately
understands that blow-up scenarios are structurally bounded — which is
the single biggest unlock for the IP-sale price ceiling.""",
    ),
    dict(slug="ensemble-weather-forecasting",
         title="Ensemble weather forecasting",
         tags=["concept", "alt-data", "weather", "methodology"],
         sources=["3-17-competition-research",
                  "3-19-alternative-data-for-prediction-markets-research",
                  "3-19-kalshi-trading-strategy-research"],
         related_entities=["open-meteo", "kalshi"],
         related_concepts=[],
         narrative="""**Ensemble weather forecasting** is the practice of combining outputs
from multiple numerical weather prediction (NWP) models to produce a
probability distribution over the forecast variable, rather than a
point forecast. Cemini uses it as the primary signal for Kalshi
weather event contracts (temperature buckets, precipitation
thresholds, hurricane landfall).

### The pipeline per the 3-19 Kalshi strategy research
1. Pull ECMWF IFS, GFS, ICON, MetNo, JMA forecasts for the target
   lat/lon at each Kalshi contract's resolution time via Open-Meteo.
2. Fit a **Gumbel extreme-value distribution** to the ensemble
   values — preferred over Gaussian because extreme-temp and
   precipitation-threshold contracts resolve on tail events.
3. Compute the Kalshi-contract-specific probability by integrating
   the Gumbel fit over the contract's resolution bucket.
4. Pass through an Avellaneda-Stoikov market-making model in logit
   space to produce bid/ask quotes.
5. Size via Kelly-fractional + CVaR cap.

### Why Gumbel, not Gaussian
Kalshi contracts bucket at 5°F or precipitation-in-quarter-inch
granularity; at the resolution edges the ensemble distribution is
skewed and Gaussian tails underweight the actual resolution
probability. Gumbel captures the right-tail reasonably well with only
two parameters, which keeps the fit stable on 30–50 ensemble members.""",
    ),
    dict(slug="mappo",
         title="MAPPO (Multi-Agent PPO)",
         tags=["concept", "reinforcement-learning", "multi-agent", "methodology"],
         sources=["3-29-11", "3-29-6", "3-19-ip-sale-research",
                  "3-19-telegram-discord-research"],
         related_entities=["torchrl", "pettingzoo"],
         related_concepts=[],
         narrative="""**MAPPO (Multi-Agent Proximal Policy Optimization)** is a CTDE
(centralized-training-decentralized-execution) extension of PPO. A
single centralized critic takes the joint observation of all agents to
reduce variance during training; each agent ships with its own
decentralized actor for deployment.

### Cemini's use
Research-grade only — MAPPO-trained policies over PettingZoo multi-
venue execution environments are positioned in the IP-sale bundle as
evidence of sophisticated R&D (optimal inter-venue routing, alpha-
decay-aware capacity allocation), not as shipped production policy.

### Why it matters in the IP-sale context
The 3-19 IP-sale research is explicit: an acquirer will evaluate the
RL track as **optionality**, not as revenue-generating code. The
MAPPO + TorchRL + PettingZoo stack demonstrates the team can run
modern RL research on CPU-tractable problems with a reproducible
Pydantic-v2-typed observation/reward pipeline — a significant
multiplier on the final sale price even if no RL-trained policy ever
ships to production.""",
    ),
    dict(slug="sbom",
         title="SBOM (Software Bill of Materials)",
         tags=["concept", "security", "supply-chain", "standard"],
         sources=["3-17-competition-research", "github-action-and-workflow-research",
                  "3-19-ip-sale-research"],
         related_entities=["syft", "cyclonedx"],
         related_concepts=["ip-sale-readiness"],
         narrative="""A **Software Bill of Materials (SBOM)** is the structured inventory of
every component (libraries, containers, models, licenses) that makes
up a shipped software artifact. Cemini auto-generates a CycloneDX-
format SBOM with Syft on every CI build and attaches it alongside
the release binary + cosign signature.

### Why SBOMs are non-optional for Cemini
The institutional-buyer archetype for the IP-sale thesis has a
supply-chain-security team that will demand SBOMs as a due-diligence
artifact — NIST SSDF, EO 14028, and the equivalent European CRA
regulations all explicitly require them for procurement. Turning up
to the diligence call without SBOMs signals "handmade IP", which is
a de-valuation trigger.

### What's in Cemini's SBOM
- Python dependency graph via Syft's pip scanner.
- Container base-image provenance (pinned digest).
- Model-weight provenance — DeepSeek-R1-14B checkpoint hash, FinBERT
  checkpoint hash — with their upstream licenses noted.
- Custom Cemini components flagged as `proprietary` with their
  own version + git-commit provenance.""",
    ),
    dict(slug="milestone-ledger",
         title="Milestone ledger",
         tags=["concept", "cemini-internal", "product-management"],
         sources=["3-9-pm-research", "roadmap",
                  "3-10-algorithmic-trading-ip-sale-audit",
                  "3-19-compliance-research"],
         related_entities=[],
         related_concepts=["ip-sale-readiness", "cryptographic-audit-trail"],
         narrative="""The **milestone ledger** is Cemini's append-only record of shipped
features keyed to an explicit milestone-ID. Each entry carries the
git-commit range, the Pydantic-v2 schema version, the SBOM hash, the
Merkle-root snapshot, and a short natural-language summary.

### Why it exists
In the IP-sale negotiation playbook, the milestone ledger is the
**linear narrative** an acquirer's diligence team reads from initial
commit to the current code. Without it, due diligence degrades into
archeological commit-log spelunking — which increases time-on-deal
and gives the acquirer ammunition to haircut the price on
"complexity risk".

### What it connects
- **Cryptographic audit trail** — each milestone's Merkle snapshot
  is anchored via OpenTimestamps.
- **IP-sale-readiness** — the milestone ledger IS the readiness
  narrative in the APA (Asset Purchase Agreement) schedule.
- **Deal-killer ledger** — each potentially-problematic dependency
  or license is linked to the milestone at which it was introduced
  and (if resolved) retired.""",
    ),
    dict(slug="publishers-exclusion",
         title="Publisher's exclusion",
         tags=["concept", "legal", "m-and-a", "licensing"],
         sources=["3-19-compliance-research", "3-19-ip-sale-research"],
         related_entities=["telethon", "finnhub"],
         related_concepts=["ip-sale-readiness"],
         narrative="""**Publisher's exclusion** is the Asset Purchase Agreement mechanism by
which specific components of the selling entity's stack can be
**excluded** from the transfer without devaluing the core IP — the
seller either keeps ownership or shuts the feature down pre-close,
and the APA explicitly carves it out.

### Cemini-specific candidates flagged in the 3-19 compliance research
1. **Telegram-channel alt-data** (Telethon pipeline) — reputational
   and user-consent concerns; the acquirer may refuse to inherit.
2. **Finnhub commercial-license-dependent features** — per-entity
   license means the acquirer would re-negotiate, which is
   friction; may be excluded and the feature rebuilt post-close.
3. **Cemini founder's personal Twitter-scraping research notes** —
   clearly personal-IP-adjacent; excluded by default.
4. **Prediction-market execution on Polymarket** — on-chain venue
   with US-retail-access ambiguity; excluded until the acquirer
   decides whether to restructure.

### How it protects deal value
Without publisher's exclusion, any problematic component risks being
used as a price-haircut lever during diligence. Pre-identifying and
carving out lets the core platform be transferred at full value.""",
    ),
    dict(slug="irc-1235-capital-gains-safe-harbor",
         title="IRC §1235 capital-gains safe harbor",
         tags=["concept", "tax", "legal", "m-and-a"],
         sources=["3-19-compliance-research", "3-19-ip-sale-research"],
         related_entities=[],
         related_concepts=["ip-sale-readiness"],
         narrative="""**IRC §1235** provides a statutory safe harbor under the US Internal
Revenue Code for the **sale or exchange of a patent or rights therein
held by the inventor** — proceeds are taxed at long-term capital
gains rates regardless of holding period, and regardless of whether
installment payments make them look like royalty income.

### Why it matters to Cemini
The IP-sale thesis contemplates a large one-time proceeds event
(replacement-cost-anchored base + earnout tiers). Absent §1235, the
IRS may recharacterize the earnout portion as ordinary-income
royalties — taxed at ~37% top marginal federal rate plus NIIT plus
state tax. Under §1235, the same proceeds are taxed at 20% federal
LTCG + NIIT + state, saving ~15% of the earnout in tax.

### Requirements
Cemini satisfies the core tests per the 3-19 compliance research:
individual inventor (founder personally holds the contributor role),
transfer of substantially all rights in the IP (APA structures the
deal as an asset-purchase not a license), transfer is not between
related parties.

### Structural interplay
The Florida single-member LLC is a disregarded entity for federal
tax — proceeds flow to the individual inventor, preserving §1235
eligibility. An S-corp or partnership wrapper would break the safe
harbor.""",
    ),
    dict(slug="skill-vetting",
         title="Skill vetting",
         tags=["concept", "llm-tooling", "safety", "methodology"],
         sources=["3-2-audit-dr", "3-6-git-1",
                  "3-19-compliance-research"],
         related_entities=["fastmcp"],
         related_concepts=["cryptographic-audit-trail"],
         narrative="""**Skill vetting** is the review process by which an MCP-exposed tool
(Anthropic Agent Skill, FastMCP server endpoint, LangGraph tool node)
is evaluated before it's made callable by the agent.

### Cemini's vetting checklist per the 3-2 audit + 3-19 compliance research
1. **Capability surface audit** — what irreversible state can the
   skill mutate? (Order submission, position close, credential
   rotation = highest tier.)
2. **Input validation** — every parameter typed by Pydantic v2;
   schemathesis-generated property tests run on the MCP schema.
3. **Authorization gate** — risk-engine state is checked before the
   skill executes; RED-regime + high-tier skills require an
   explicit human-in-the-loop confirmation.
4. **Audit anchoring** — every skill invocation + arguments +
   return value is pg_tamperlogged and Merkle-rooted.
5. **Rollback plan** — for any mutating skill, a compensating-action
   counterpart skill is registered alongside so the agent can
   undo a mistake within the same reasoning turn.

### Institutional-diligence signal
Skill vetting is how Cemini demonstrates to an IP-sale buyer that
its LLM layer is not a "let the agent run SQL and pray" architecture —
every capability is typed, gated, logged, and reversible.""",
    ),
]

# ---------- FRONTMATTER TEMPLATE HELPERS ----------
def build_related_list(entry: dict) -> list[str]:
    rels: list[str] = []
    for s in entry.get("sources", []):
        rels.append(f"sources/{s}.md")
    for c in entry.get("related_concepts", []):
        rels.append(f"concepts/{c}.md")
    for e in entry.get("related_entities", []):
        # entity slugs — find their categories to build correct path
        for other in ENTITIES:
            if other["slug"] == e:
                rels.append(f"entities/{other['category']}/{e}.md")
                break
    return rels


def render_relations_section(related: list[str]) -> str:
    if not related:
        return "\n## Relations\n\n*(none yet)*\n"
    lines = "\n".join(f"- @{r}" for r in related)
    return f"\n## Relations\n\n{lines}\n"


def render_entity_page(e: dict) -> str:
    related = build_related_list(e)
    fm_related = "\n".join(f"  - {r}" for r in related) if related else ""
    tags_str = ", ".join(e["tags"])
    frontmatter = f"""---
title: {e['title']}
type: entity
tags: [{tags_str}]
keywords: []
related:
{fm_related}
maturity: validated
created: {TODAY}
updated: {TODAY}
---"""
    relations = render_relations_section(related)
    raw_concept = (
        f"\n## Raw Concept\n\n"
        f"Synthesized from {len(e['sources'])} source(s) referencing this entity "
        f"across the Cemini research corpus. Category: {e['category']}.\n"
    )
    narrative = f"\n## Narrative\n\n{e['narrative'].strip()}\n"
    snippets = "\n## Snippets\n\n*(populate as source stubs are deep-read.)*\n"
    return frontmatter + "\n" + relations + raw_concept + narrative + snippets


def render_concept_page(c: dict) -> str:
    related = build_related_list(c)
    fm_related = "\n".join(f"  - {r}" for r in related) if related else ""
    tags_str = ", ".join(c["tags"])
    frontmatter = f"""---
title: {c['title']}
type: concept
tags: [{tags_str}]
keywords: []
related:
{fm_related}
maturity: validated
created: {TODAY}
updated: {TODAY}
---"""
    relations = render_relations_section(related)
    raw_concept = (
        f"\n## Raw Concept\n\n"
        f"Synthesized across {len(c['sources'])} source(s) in the Cemini research corpus "
        f"that reference this concept directly or by equivalent terminology.\n"
    )
    narrative = f"\n## Narrative\n\n{c['narrative'].strip()}\n"
    snippets = "\n## Snippets\n\n*(populate as source stubs are deep-read.)*\n"
    return frontmatter + "\n" + relations + raw_concept + narrative + snippets


# ---------- WRITE ENTITY + CONCEPT PAGES ----------
written = []
for e in ENTITIES:
    target_dir = WIKI / "entities" / e["category"]
    target_dir.mkdir(parents=True, exist_ok=True)
    path = target_dir / f"{e['slug']}.md"
    path.write_text(render_entity_page(e))
    written.append(str(path.relative_to(WIKI)))

for c in CONCEPTS:
    target_dir = WIKI / "concepts"
    target_dir.mkdir(parents=True, exist_ok=True)
    path = target_dir / f"{c['slug']}.md"
    path.write_text(render_concept_page(c))
    written.append(str(path.relative_to(WIKI)))

print(f"Wrote {len(written)} entity + concept pages")

# ---------- BIDIRECTIONAL PATCH OF SOURCE STUBS ----------
# Build: source_slug -> list of new `related:` entries to add
backlinks: dict[str, list[str]] = {}
for e in ENTITIES:
    backref = f"entities/{e['category']}/{e['slug']}.md"
    for src in e["sources"]:
        backlinks.setdefault(src, []).append(backref)
for c in CONCEPTS:
    backref = f"concepts/{c['slug']}.md"
    for src in c["sources"]:
        backlinks.setdefault(src, []).append(backref)

fm_re = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

def patch_source_stub(slug: str, new_refs: list[str]) -> tuple[bool, str]:
    path = WIKI / "sources" / f"{slug}.md"
    if not path.exists():
        return False, f"MISSING: {path}"
    text = path.read_text()
    m = fm_re.match(text)
    if not m:
        return False, f"NO-FRONTMATTER: {path}"
    fm_body = m.group(1)
    rest = text[m.end():]

    # parse existing related: list (very light YAML)
    lines = fm_body.splitlines()
    out_lines: list[str] = []
    i = 0
    existing_related: list[str] = []
    related_start = None
    related_end = None
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("related:"):
            related_start = len(out_lines)
            # `related: []` inline form
            if ln.strip() == "related: []":
                out_lines.append(ln)
                related_end = len(out_lines)
                i += 1
                continue
            out_lines.append("related:")
            i += 1
            while i < len(lines) and (lines[i].startswith("  - ") or lines[i].startswith("- ")):
                ref = lines[i].split("- ", 1)[1].strip()
                existing_related.append(ref)
                out_lines.append(f"  - {ref}")
                i += 1
            related_end = len(out_lines)
            continue
        out_lines.append(ln)
        i += 1

    # Merge
    merged_seen = set(existing_related)
    additions: list[str] = []
    for r in new_refs:
        if r not in merged_seen:
            additions.append(r)
            merged_seen.add(r)

    if not additions and not (related_start is not None and out_lines[related_start].strip() == "related: []"):
        # Nothing to add + not the empty-list form → just bump updated
        pass

    # Rebuild related: block fresh
    if related_start is not None:
        new_rel_lines = ["related:"]
        for r in existing_related + additions:
            new_rel_lines.append(f"  - {r}")
        out_lines = out_lines[:related_start] + new_rel_lines + out_lines[related_end:]

    # Bump updated:
    new_fm_lines: list[str] = []
    for ln in out_lines:
        if ln.startswith("updated:"):
            new_fm_lines.append(f"updated: {TODAY}")
        else:
            new_fm_lines.append(ln)

    new_fm = "\n".join(new_fm_lines)

    # Update ## Relations section to reflect full related list
    all_rel = existing_related + additions
    new_relations = render_relations_section(all_rel).lstrip("\n")

    # Replace existing Relations section between "## Relations" header and next "## "
    rel_pattern = re.compile(r"## Relations\n.*?(?=\n## |\Z)", re.DOTALL)
    if rel_pattern.search(rest):
        new_rest = rel_pattern.sub(new_relations.rstrip() + "\n", rest, count=1)
    else:
        new_rest = new_relations + rest

    path.write_text(f"---\n{new_fm}\n---\n{new_rest}")
    return True, f"patched: +{len(additions)} refs"

patch_log = []
for slug, refs in backlinks.items():
    ok, msg = patch_source_stub(slug, refs)
    patch_log.append(f"{slug}: {msg}")

print(f"\nPatched {sum(1 for p in patch_log if 'patched' in p)} source stubs")
missing_stubs = [p for p in patch_log if "MISSING" in p]
if missing_stubs:
    print("MISSING STUBS:")
    for p in missing_stubs:
        print(f"  {p}")

# ---------- PROMOTE 9 UNBLOCKED DOCX STUBS DRAFT -> VALIDATED ----------
UNBLOCKED_DOCX = [
    "3-10-cryptographic-research",
    "3-18-crypto-integration-technical-audit",
    "3-19-langgraph-scatter-gather-financial-analysis",
    "3-19-ip-sale-research",
    "3-19-telegram-discord-research",
    "3-19-compliance-research",
    "3-19-kalshi-trading-strategy-research",
    "trading-playbook-research",
    "forex-research-3-18",
]
promoted = []
for slug in UNBLOCKED_DOCX:
    path = WIKI / "sources" / f"{slug}.md"
    if not path.exists():
        print(f"MISSING for promote: {slug}")
        continue
    text = path.read_text()
    # Replace maturity: draft -> maturity: validated
    text2 = re.sub(r"^maturity: draft$", "maturity: validated", text, count=1, flags=re.MULTILINE)
    # Replace Read status: unread-stub -> deep-read
    text2 = re.sub(r"- \*\*Read status\*\*: unread-stub", "- **Read status**: deep-read", text2)
    path.write_text(text2)
    promoted.append(slug)

print(f"\nPromoted {len(promoted)} docx stubs draft→validated")
print("Done.")
