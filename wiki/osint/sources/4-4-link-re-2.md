---
title: 'CEMINI FINANCIAL SUITE: Technical Intelligence & Competitive Architecture Report'
type: source
tags: [docx, deep-read, agent-governance, cryptographic-evidence, semantic-context, reward-modeling, multi-agent-orchestration, ip-contamination, cemini-internal, link-evaluation, multi-topic]
keywords: [Sovereign-OS, agent URI, TrustScore, cryptographic evidence, SAMEP, OpenViking, AGPL-3.0, DLinear, reward decomposition, recency weighting, TradingAgents, Deer-Flow, IP contamination]
related:
  - concepts/market-microstructure.md
  - concepts/quant-finance.md
  - concepts/rl-marl-research.md
  - concepts/llm-agent-systems.md
  - sources/3-28-links-2.md
  - sources/4-4-link-re.md
  - sources/4-6-links.md
  - concepts/dlinear.md
  - concepts/recency-weighted-fundamental-data.md
  - concepts/algorithmic-stopping-conditions.md
  - concepts/nomotic-ai.md
  - entities/tools/promptfoo.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-04-30
clusters:
  - rl-marl
  - llm-agents
  - market-microstructure
  - quant-finance
  - cemini-internal
  - infrastructure
---

## Relations

- @concepts/market-microstructure.md — Market Microstructure corpus-index hub
- @concepts/quant-finance.md — Quantitative Finance corpus-index hub
- @concepts/rl-marl-research.md — RL/MARL research hub
- @concepts/llm-agent-systems.md — LLM agent-systems hub
- @sources/3-28-links-2.md — sibling K12 doc; agent-infra tool evaluations
- @sources/4-4-link-re.md — sibling K12 doc; academic papers and trading systems
- @sources/4-6-links.md — sibling K12 doc; nvk/llm-wiki + AI governance papers
- @concepts/dlinear.md — DLinear trend-seasonal model concept; Top Steal adoption
- @concepts/recency-weighted-fundamental-data.md — Recency-weighted macro feature engineering; Top Steal adoption

## Raw Concept

- **Original title**: CEMINI FINANCIAL SUITE: Technical Intelligence & Competitive Architecture Report
- **Author(s)**: Cemini internal (link-evaluation audit)
- **Type**: DOCX
- **Location**: cemini-librarian:/opt/cemini-bulk/research/4_4 link re 2.docx
- **Retrieved**: 2026-04-23
- **Read status**: deep-read

## Narrative

This Cemini-internal audit is structured into 7 Target Domains, each evaluating 1–4 primary sources (repos, papers, or frameworks) against the standard 8-section Cemini template. The constraint frame is 128 GB RAM CPU-only Hetzner VPS (now known to be 7 GB — see K11 refresh at @entities/infrastructure/hetzner.md). This doc is notable for two things: (1) its structured domain taxonomy, and (2) explicit IP-contamination warnings for AGPL-3.0 / copyleft-licensed repos.

### Target Domain 1: Agent Governance, Fiscal Discipline & Topology-Independent Routing

**Sovereign-OS** — Declarative agent governance framework. Defines a YAML "Charter" specifying fiscal boundaries (max drawdown, position limits, authorized venues) that agents must obey. Implements asymmetric TrustScore: +5 for compliant actions, −15 for violations — a 3:1 penalty ratio that makes violations cumulatively disqualifying. Relevance: maps to the Nomotic AI "pre-action authorization" pattern in @sources/4-6-links.md. The YAML Charter is a lightweight alternative to hard-coded Pydantic validators for rules that change with market regime.

**Agent URI** — Proposed standard for addressing and discovering AI agents (like URLs for web resources). Relevance: low for a monolithic solo-dev setup. The federated agent-discovery problem doesn't apply to Cemini's single-server architecture.

### Target Domain 2: Cryptographic Evidence Structures

**Constant-size hash tuples** — Cryptographic commitment scheme producing fixed-size proofs regardless of the number of underlying transactions. Relevance: could compress the Cemini cryptographic audit trail's Merkle tree as trade volume scales. [TENTATIVE] — implementation complexity may outweigh benefit at current trade volumes.

**Fuzzy logic guardrails** — Soft constraints using fuzzy membership functions instead of hard binary thresholds. Example: rather than "reject if drawdown > 5%", use a fuzzy rule that increasingly penalizes positions as drawdown approaches 5%. Relevance: smoother risk management than hard Pydantic cutoffs. CPU-cheap (lookup-table evaluation).

### Target Domain 3: Semantic Context Discovery

**SAMEP** — Semantic Asset Mapping and Evaluation Protocol. AGPL-3.0 licensed. **CONTAMINATED — do not integrate.** The conceptual approach (mapping semantic relationships between assets for context-aware trading) is stealable via clean-room reverse engineering. The AGPL-3.0 license is incompatible with Cemini's proprietary stack.

**OpenViking** — Open-source VikingDB-based semantic search layer. AGPL-3.0 licensed. **CONTAMINATED — do not integrate.** Same clean-room constraint as SAMEP. The pattern of semantic context discovery for trading signals is valid; the implementation is legally toxic.

### Target Domain 4: Decomposable Reward Modeling

**DLinear** — **Top Steal.** A ~1,000-parameter linear model that decomposes time series into trend and seasonal components, then applies separate linear layers to each. Despite its simplicity, it beats Transformer-based forecasters on many benchmarks. Relevance: could replace or supplement the LSTM feature extractor in Cemini's MAPPO pipeline. CPU inference cost is negligible (~1K params vs 62K for MAPPO). The trend-seasonal decomposition is inherently interpretable — directly supporting the glass-box IP-sale narrative.

**Legal-action masking** — Constraining RL action spaces to legally permissible trades only (no wash sales, no spoofing, no insider patterns). Relevance: maps to the Nomotic Execution Service. Action masking is implemented as a binary mask over the action space before the policy softmax — computationally free.

**Anti-lookahead semantics** — Preventing the RL agent from using future information during training. Implemented via strict temporal train/test splits and per-timestamp feature freezing. Relevance: the Cemini MAPPO retrain window already enforces temporal splits; this formalizes the constraint.

### Target Domain 5: Hybrid Variable Sets

**Recency weighting** — Assigning decaying weights to fundamental data based on days since publication. Identical to the mechanism in @sources/forex-1-4-4.md (King & Amigó 2025). Cross-document convergence: two independent sources converge on "days since last publication" as the right lightweight mechanism for mixing quarterly macro with daily price data.

**Directional index** — Composite target variable weighting max-profit-path, max-loss-path, and terminal price. Also convergent with @sources/forex-1-4-4.md. Two-source convergence upgrades this from [TENTATIVE] to [CONFIRMED] as a Cemini-adoptable pattern.

### Target Domain 6: Multi-Agent Orchestration

**TradingAgents** — Multi-agent trading system where agents debate trade decisions and a validator agent scores arguments. Relevance: directly validates the Cemini 5-agent LangGraph Devil's Advocate debate protocol. The debate-validation pattern converges with the AI Agency paper in @sources/4-6-links.md (monitored collaborative ensembles, algorithmic stopping conditions).

**Deer-Flow** — Middleware chain for agent orchestration. Composable pipeline: data ingestion → feature engineering → signal generation → risk check → execution. Relevance: maps to the Redis Streams Intel Bus architecture. The middleware-chain pattern was already promoted in @sources/3-26-link-re-3.md (K10).

**Microsoft Agent Framework** — Enterprise multi-agent framework. Overlaps with LangGraph. Snippets-only — the Cemini stack is committed to LangGraph.

**Goose, Hermes-Agent, Promptfoo** — Additional agent frameworks and testing tools. Promptfoo appears across multiple K12 docs (see @sources/3-28-links-2.md) — cross-document convergence strengthens its Promotion case.

### Target Domain 7: Contaminated Intellectual Property

Explicit IP-contamination audit. Three repos flagged as copyleft-poisoned:

- **OpenViking** (AGPL-3.0) — semantic search. Clean-room reverse engineer only.
- **MoneyPrinterV2** (GPL) — automated trading bot. Do not integrate; pattern may be stealable but implementation is toxic.
- **MiroFish** (copyleft) — market data visualization. Do not integrate.

The doc establishes a clear doctrine: **AGPL-3.0, GPL, and strong copyleft licenses are absolute blockers for the Cemini proprietary stack.** MIT, Apache-2.0, and BSD are safe. LGPL requires case-by-case assessment (dynamic linking may be acceptable).

### Promotion candidates

1. **DLinear** — Strongest Promotion candidate. 1,000-parameter trend-seasonal model beating Transformers. CPU-trivial inference. Deserves an entity/concept page as a Cemini-relevant architecture.
2. **Sovereign-OS Charter pattern** — YAML-declarative fiscal discipline with asymmetric TrustScore. Complements the Nomotic AI concept. File under @concepts/llm-agent-systems.md or create a dedicated governance concept page.
3. **IP-contamination doctrine** — The AGPL-3.0 / GPL absolute-blocker rule established here should be recorded in a concept page or added to CLAUDE.md as a constraint.

### Cross-document convergence notes

- Recency weighting + directional index appear in both this doc and @sources/forex-1-4-4.md → [CONFIRMED]
- Promptfoo appears in both this doc and @sources/3-28-links-2.md → strengthens Promotion case
- Deer-Flow middleware chain was already promoted in @sources/3-26-link-re-3.md (K10) → validated, not new
- Nomotic AI / pre-action authorization converges across @sources/4-4-link-re-2.md and @sources/4-6-links.md

## Snippets

> "Sovereign-OS: Declarative agent governance via YAML Charter. Asymmetric TrustScore: +5 for compliant actions, −15 for violations — 3:1 penalty ratio makes violations cumulatively disqualifying." [Source: 4_4 link re 2.docx §Target Domain 1]

> "DLinear: ~1,000-parameter linear model decomposing time series into trend and seasonal components. Despite simplicity, beats Transformer-based forecasters on many benchmarks. CPU inference cost negligible." [Source: 4_4 link re 2.docx §Target Domain 4]

> "AGPL-3.0, GPL, and strong copyleft licenses are absolute blockers for the Cemini proprietary stack. MIT, Apache-2.0, and BSD are safe. LGPL requires case-by-case assessment." [Source: 4_4 link re 2.docx §Target Domain 7]

> "OpenViking (AGPL-3.0): CONTAMINATED — do not integrate. Clean-room reverse engineer only. The pattern of semantic context discovery for trading signals is valid; the implementation is legally toxic." [Source: 4_4 link re 2.docx §Target Domain 3]

> "Recency weighting: assigning decaying weights to fundamental data based on days since publication. Identical mechanism to King & Amigó 2025 forex paper." [Source: 4_4 link re 2.docx §Target Domain 5]

> "Legal-action masking: constraining RL action spaces to legally permissible trades only. Binary mask over action space before policy softmax — computationally free." [Source: 4_4 link re 2.docx §Target Domain 4]
