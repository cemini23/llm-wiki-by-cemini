---
title: 'Targeted Extraction Audit: Cemini Financial Suite — FinRL-X, Zero-Shot LLM Aggregation, Agentic Screening'
type: source
tags: [docx, rl-marl, llm-agents, portfolio-strategy, options-derivatives, prediction-markets, cemini-internal, finrl-x, weight-centric-interface, logistic-meta-classifier, ledoit-wolf, finbert]
related:
  - concepts/options-derivatives.md
  - concepts/portfolio-strategy.md
  - concepts/rl-marl-research.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26
clusters:
  - rl-marl
  - llm-agents
  - portfolio-strategy
  - options-derivatives
  - prediction-markets
  - cemini-internal
---

## Relations

- @concepts/options-derivatives.md — Options & Derivatives corpus-index hub (Q 2026-04-27)
- @concepts/portfolio-strategy.md — Portfolio Strategy corpus-index hub (Q 2026-04-27)
- @concepts/rl-marl-research.md — cluster hub for RL/MARL research in the Cemini corpus

## Raw Concept

- **Original title**: Targeted Extraction Audit: Cemini Financial Suite Architecture (FinRL-X / Zero-Shot LLM Aggregation / Agentic AI Screening batch)
- **Author(s)**: Cemini internal research (no attributed author)
- **Type**: DOCX (internal extraction audit)
- **Location**: research for cemini/3_26 blog re 2.docx
- **Length**: ~5639 words, 106 paragraphs
- **Retrieved**: 2026-04-23 (filename date 2026-03-26)
- **Read status**: read-skim
- **Primary cluster**: cemini-internal (partition-assigned `options-derivatives` is misclustered — none of the sources covered are about options, see flags)
- **All clusters**: rl-marl, llm-agents, portfolio-strategy, options-derivatives, prediction-markets, cemini-internal

## Narrative

Third-batch targeted-extraction audit (sibling to `3-29-research-3.md` and `3-29-research-5.md`), dissecting three external arXiv preprints against the Cemini CPU-only / LangGraph / MAPPO / Hetzner-128GB stack using the same seven-slot template.

**Source 1: arXiv:2603.21330 — FinRL-X (Apache 2.0).** The most portable pattern: a **weight-centric interface** as the sole immutable contract between strategy and execution — π_total = π_risk ∘ π_timing ∘ π_alloc ∘ π_select. Strategy layer emits a target-weight vector θ to `intel:weights:target` Redis Stream; an isolated FastAPI execution service diffs against live PostgreSQL state and executes, abstracting Kalshi vs Alpaca vs Robinhood. Disaggregate pipeline into LangGraph StateGraph nodes (select_assets, allocate_base_weights, apply_timing_signals, apply_risk_overlay). **Deterministic risk overlay** (VIXVolatilityScaler-style) compresses weights toward cash when implied vol breaches thresholds, *overriding* the RL agent — chosen explicitly because MAPPO is sample-inefficient for macro-tail events. Training pipeline must query the same TimescaleDB materialized views as live services (no offline CSV/memory arrays) — ~8-12h of DBmate migration refactoring. Rejects `bt` backtesting library as conflicting with TorchRL/PettingZoo native vectorized backtests.

**Source 2: arXiv:2603.20965 — Aggregating Zero-Shot LLM Agents for corporate-disclosure classification.** Replace the LangGraph final consensus LLM call with a **frozen-LLM meta-classifier**: flatten the 5 agents' labels (+1/0/-1), confidence floats, and pairwise-agreement booleans into a structured vector; run L2-regularized logistic regression (liblinear) on it for final decision. Microseconds on CPU, removes the last non-deterministic step. Enforce deterministic-inference constraints on LLM calls (Temperature=0, Top-p=1, fixed seed). Pydantic v2 schema-violation → single retry → auto-neutral-label-zero-confidence fallback. Confidence extraction: geometric mean of token log-probabilities if available; else parse-from-JSON with clipping to [0,1] and `@field_validator` sanitization. **Reject** running 72B-parameter models locally (Qwen2.5-72B-Instruct cited) — use external APIs only for large models. Role-isolated system prompts: Performance / Guidance / Risk personas, disagreement-magnitude vectorized via pgvector and fed to the 28-dim MAPPO observation.

**Source 3: arXiv:2603.23300 — Agentic AI-Based Screening.** Two-frequency agent architecture: slow LLM-Strategy Agent on book-to-market / firm fundamentals (annual/quarterly cadence, TimescaleDB hypertable); fast FinBERT-sentiment agent on news (daily/minute, Redis Stream + materialized view). Intersection-based consensus: stock enters the optimization pool only on 2-of-3 agent agreement — this is a *CPU-efficient pre-filter* that reduces dimensionality before Markowitz/covariance inversion (O(N³) → manageable). Portfolio layer uses **Ledoit-Wolf nonlinear shrinkage** (`sklearn.covariance.LedoitWolf`) for covariance estimation — singular-sample-covariance problem solved in one line of Python, no neural-net approximators needed. POET (Fan et al.) cited as alternative.

Relevant to Cemini as one of the highest-density prescriptive docs in the internal corpus — weight-centric interface and logistic meta-classifier are both immediately actionable, low-risk wins. Honest limits: (a) consulting/IP-sale register same as sibling audits — every section ends on "satisfies institutional due-diligence" framing; (b) effort estimates (8-12h, "few hours") ungrounded; (c) three source papers are only abstract-read, so the specific `bt`-library conflict, 72B-model footnote, and Ledoit-Wolf applicability claims are taken from the summarizer not verified against primary texts; (d) "two-frequency agent processing" is a sensible pattern but no empirical speedup numbers are reported.

## Key findings

- **FLAG: MISCLUSTERED** — home cluster `options-derivatives` wrong; none of the three source papers is about options. Correct home is `cemini-internal` or `portfolio-strategy`.
- **Weight-centric interface (FinRL-X)** — target-weight vector θ to `intel:weights:target` Redis Stream; isolated FastAPI execution service handles broker diffs. Decouples strategy from Kalshi/Alpaca/Robinhood execution entirely.
- Pipeline as LangGraph StateGraph: select_assets → allocate_base_weights → apply_timing_signals → apply_risk_overlay, Polars DataFrames at each node.
- Deterministic VIX-scaled risk overlay OVERRIDES MAPPO during macro-tail events — chosen because RL is sample-inefficient for rare crashes.
- Training pipeline queries same TimescaleDB materialized views as live services — eliminates sim-to-live data-semantics drift.
- **Frozen-LLM meta-classifier** replaces LangGraph final consensus LLM: L2-regularized logistic regression over flattened (label, confidence, pairwise-agreement) vector.
- Deterministic LLM-inference constraints: Temperature=0, Top-p=1, fixed seed; Pydantic `@field_validator` intercepts malformed confidence scores.
- Graceful-degradation fallback: schema violation → single retry → neutral-label-zero-confidence; prevents cascade failure in 24/7 loop.
- Two-frequency agent split: slow fundamentals (annual/quarterly) vs fast sentiment (daily/minute) into separate TimescaleDB tiers.
- Intersection-based consensus (2-of-3 agreement) as CPU-efficient pre-filter before O(N³) covariance inversion.
- **Ledoit-Wolf nonlinear shrinkage** (`sklearn.covariance.LedoitWolf`) for covariance estimation — single line of Python replaces neural-net approximators.
- Reject running 72B-parameter models locally on 128GB Hetzner; external API only.

## Snippets

- **FinRL-X weight-centric interface** — "π_total = π_risk ∘ π_timing ∘ π_alloc ∘ π_select… the TorchRL agent or the LangGraph orchestrator purely calculates the desired target state and publishes this [θ] vector to a Redis Stream, specifically a channel named intel:weights:target. A completely isolated FastAPI execution service then consumes this stream."
- **Risk overlay override** — "Expecting a TorchRL MAPPO agent to accurately learn and remember extreme macro-tail risks (like a flash crash) within a limited 28-feature observation space on a CPU is sample-inefficient… the risk overlay mathematically compresses the target weights toward cash, overriding the RL agent's allocations."
- **Meta-classifier** — "the final node in the LangGraph orchestrator should not be an LLM call. It should be a purely numerical execution utilizing a scikit-learn model trained with L2-regularized logistic regression."
- **Confidence extraction** — "defined mathematically as the geometric mean of the token probabilities for the generated label string… for models that do not expose log-probabilities, the numerical confidence value must be parsed directly from the constrained JSON output and mathematically clipped."
- **Intersection consensus** — "A stock is included in the final optimization pool only if multiple independent agents agree on the directional signal… the orchestrator acts as a highly efficient pre-filter."
- **Ledoit-Wolf** — "the sklearn.covariance.LedoitWolf module can compute this robust covariance matrix in a single line of Python code. Integrating this robust mathematical formulation directly into the Polars weight calculation pipeline provides institutional-grade portfolio optimization."
