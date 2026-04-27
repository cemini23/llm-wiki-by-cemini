---
title: 'Strategic Architecture and Algorithmic Development Report: Cemini Financial Suite Project State Summary'
type: source
tags: [docx, cemini-internal, rl-marl, llm-agents, portfolio-strategy, market-microstructure, quant-finance, prediction-markets, audit-security, infrastructure, data-engineering]
related:
  - concepts/market-microstructure.md
  - concepts/milestone-ledger.md
  - concepts/portfolio-strategy.md
  - concepts/quant-finance.md
  - entities/infrastructure/hetzner.md
  - entities/infrastructure/pgvector.md
  - entities/infrastructure/redis.md
  - entities/infrastructure/timescaledb.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26
read_status: validated
clusters:
  - rl-marl
  - llm-agents
  - portfolio-strategy
  - market-microstructure
  - quant-finance
  - prediction-markets
  - cemini-internal
  - audit-security
  - infrastructure
  - data-engineering
---

## Relations

- @concepts/market-microstructure.md — Market Microstructure corpus-index hub (Q 2026-04-27)
- @concepts/milestone-ledger.md — sibling page; K5 upgrades its `[RETRACTED 2026-04-24 Track C]` to `[RESOLVED 2026-04-26 K5 deep-read]` with the source-grounded reframe
- @concepts/portfolio-strategy.md — Portfolio Strategy corpus-index hub (Q 2026-04-27)
- @concepts/quant-finance.md — Quantitative Finance corpus-index hub (Q 2026-04-27)
- @entities/infrastructure/hetzner.md
- @entities/infrastructure/pgvector.md
- @entities/infrastructure/redis.md
- @entities/infrastructure/timescaledb.md
- @entities/platforms/kalshi.md
- @entities/platforms/polymarket.md

## Raw Concept

- Original title: Strategic Architecture and Algorithmic Development Report — Cemini Financial Suite Project State Summary (v11.0)
- Authors: Cemini internal authoring team (unsigned)
- Affiliation: Cemini Financial Suite (internal)
- Type: DOCX, internal project-state strategic document
- Location: research for cemini/3_9 pm research.docx
- Length: 172-paragraph DOCX
- Retrieved: 2026-04-23
- Publication date: 2026-03-08 (v11.0; document explicitly stamps "documented March 8, 2026")
- Read status: validated (deep-read 2026-04-26 — K5)
- Primary cluster: cemini-internal
- All clusters: rl-marl, llm-agents, portfolio-strategy, market-microstructure, quant-finance, prediction-markets, cemini-internal, audit-security, infrastructure, data-engineering
- Flag: **cemini-internal / strategic** — written for IP-sale narrative; v11.0 baseline is six-plus weeks stale as of 2026-04-26

## Narrative

### Abstract
v11.0 project-state document combining (a) **inventory of "currently deployed" Cemini state as of 2026-03-08** with (b) **comprehensive gap analysis + prescribed tech-stack upgrades** for IP-acquisition readiness. The document organizes into four prescriptive phases (Phase 1 Foundation Hardening, Phase 2 Agent Orchestration + Cryptographic Logging, Phase 3 RL Engine + Deterministic Execution, Phase 4 Hardware Verification + Final Packaging) culminating in the M&A pitch. Headline claim: **18 of 42 strategic roadmap milestones complete**.

### Prescribed-vs-deployed gap (2026-04-26 K5 deep-read)

K5 is the **stale-snapshot K-series reframe** — different from J/K/K2/K3/K4 prescribed-vs-deployed-collapse pattern. The source was written 2026-03-08; many of its "Recommended Tech Stack Upgrades" have shipped in the seven weeks since, while several of its "currently deployed" claims are stale or never had artifact backing in the first place. Server probe (`ssh root@hetzner` 2026-04-26):

**Source's "currently deployed" claims — accurate:**
- TimescaleDB + pgvector + password-protected Redis pub/sub ✓
- Pydantic v2 data contracts ✓
- GitHub Actions CI/CD ✓
- Kalshi engine live (autonomous, WebSockets, RSA-PSS) ✓
- Trivy + Semgrep dependency auditing ✓ (`/opt/cemini/.github/workflows/deploy.yml`)
- "263 automated tests" — server runs **528** (sourced under-count; deployment exceeded)
- IntelPublisher / IntelReader design pattern ✓ — `IntelPublisher`/`IntelReader` confirmed in 6+ files (`/opt/cemini/rl_training/integration.py`, `/opt/cemini/services/conviction_aggregator.py`, etc.)
- `intel:*` namespace ✓ — **30+ channels enumerated in deployed code**: `intel:agent_weights`, `intel:bar`, `intel:btc_sentiment`, `intel:btc_spy_corr`, `intel:btc_volume_spike`, `intel:capability_manifest_hash`, `intel:conflict_events`, `intel:conviction_composite`, `intel:debate_rubric`, `intel:debate_verdict`, `intel:earnings_calendar`, `intel:edgar_alert`, `intel:ensemble_signal`, `intel:fed_bias`, `intel:fred_credit_spread`, `intel:fred_fed_policy`, `intel:fred_labor`, `intel:fred_yield_curve`, `intel:fuzzy_scalar`, `intel:fx:calendar`, `intel:fx:carry`, `intel:fx:tick:*`, `intel:geopolitical_risk`, `intel:kalshi_liquidity_spike`, `intel:kalshi_oi`, `intel:kalshi_orderbook_summary`, `intel:llm_signal:*`, `intel:logit_assessments`, plus more truncated. **This is the strongest as-built confirmation in K5** — and it directly **contradicts the K4 finding** (`intel:orderbook` / `intel:sentiment` weren't real). The K4 finding was correct as scoped (no `intel:orderbook` specifically), but the broader `intel:*` *family* is heavily deployed in different channel names.

**Source's "currently deployed" claims — stale or wrong:**
- "approximately 18 Docker containers" → actually **40** (consistent with K4 finding; container count nearly doubled in seven weeks)
- "active migration pathway toward Docker Swarm" → `docker info | grep Swarm` returns **`Swarm: inactive`**. Single-node Hetzner VPS, not Swarm-orchestrated. The "active migration" claim was either aspirational or has been deferred.
- "5-tab Streamlit performance dashboard has been deployed" → `streamlit>=1.32.2` is in `/opt/cemini/requirements.txt` and `ui/replay_helpers.py`/`ui/performance.py` exist; **but no Streamlit container is running** in the 40-container snapshot. The deployed observability stack is Grafana + Loki + Prometheus + Tempo + Alertmanager + cAdvisor + Alloy — a **completely different paradigm** than the source's Streamlit framing. Streamlit may launch ad-hoc against the data layer, but it's not the production-monitoring story.
- "GDELT BigQuery ... 15-minute indexing delay" → server runs `gdelt_harvester` container (different mechanism than direct BigQuery query). The 15-min-delay criticism the source uses to motivate the OpenFang + Playwright-skill upgrade may be partially obsolete; the deployed harvester is its own pipeline.
- "milestone ledger" → **doesn't exist as a cryptographically-anchored artifact** per @concepts/milestone-ledger.md `[RETRACTED 2026-04-24 Track C]` (now upgraded to `[RESOLVED 2026-04-26 K5 deep-read]`). What exists is `/opt/cemini/docs/ROADMAP.md` — a markdown step-list. So "18 of 42 milestones complete" is at best a self-reported count against that markdown, at worst arbitrary. **Critical implication for IP-sale framing:** the document's headline self-assessment metric is unverifiable.

**Source's "Recommended Tech Stack Upgrades" — actually shipped (between 2026-03-08 and 2026-04-26):**
- **Polars** (replacing Pandas) → `polars>=0.20.15` in `/opt/cemini/requirements.txt`; **186 references** in code. ✓ shipped.
- **Pydantic AI** → `pydantic-ai>=0.0.15` in `requirements.txt`; pulled into `docker/Dockerfile.brain`. ✓ shipped (note: Pydantic-DeepAgents pattern + DeepAgents is **not** shipped — the AI library is, the multi-agent framework on top of it is not).
- **NautilusTrader** (Rust event-driven engine) → `nautilus-trader>=1.190.0` in `requirements.txt`. ✓ shipped (note: the source frames Nautilus as "currently the execution layer" but lists the PettingZoo wrapper as a Phase 3 upgrade — wrapper still TBD).
- **PettingZoo + ParallelEnv wrapper around NautilusTrader BacktestEngine** → `pettingzoo` in `rl_training/environment.py`, `tests/test_step8_backtesting.py`. Test exists for Step 8 backtesting; wrapper appears to be at least scaffolded. ✓ partially shipped.
- **Schemathesis + Hypothesis + mutmut** → all three in `requirements.txt` (`schemathesis>=4.12.0`, `hypothesis>=6.100.0`, `mutmut>=3.0.0`); 1691 hypothesis refs in code. ✓ shipped (the prescribed CI integration in deploy.yml is a separate question — needs spot-check).
- **Streamlit dashboard** → in deps + `ui/` code (per stale-claims section above; deployed but not as a container).

**Source's "Recommended Tech Stack Upgrades" — still NOT shipped:**
- **OpenFang** (Rust agent OS) → 0 refs in `/opt/cemini/` proper (1 ref in some doc; not in code)
- **DeepAgents pattern** (TodoToolset, SubAgentToolset) → 0 refs
- **TorchRL** → only in `briefs/track-c-walk-results.md` and `briefs/2026-04-24_track-c-milestone-ledger-walk.md` — these are **briefs**, not code. So the prescribed RL training loop wrapper is still unbuilt. The source's "TorchRL combined with PettingZoo Parallel API" Phase 3 prescription is unstarted on the TorchRL leg, scaffolded on the PettingZoo leg.
- **OpenBB Platform** → 0 refs
- **dbmate** (declarative schema migrations) → only in `.worktrees/` (speculative branches), `LESSONS.md`, and `research_wiki/`. Not in main `/opt/cemini/` code. The source claimed "integration of a declarative schema migration framework utilizing dbmate" — **this claim is wrong on the main branch**; it lives only in worktrees that haven't merged.
- **VeritasChain Protocol (VCP)** → already `[RETRACTED 2026-04-24 Track C]` per @concepts/cryptographic-audit-trail.md (J pass) — `veritaschain` 0 refs, `eqty` 0 refs. The "VCP" string itself appears in `cemini_mcp/server.py` and `ui/replay_helpers.py` + `ui/performance.py` + `tests/test_audit_trail.py` + `tests/test_property_based.py`, but disambiguating these from the protocol references requires per-file inspection — likely refers to the *concept* of VCP (e.g., test scaffolding for what would be VCP integration) rather than the deployed SDK.
- **Zero-Knowledge Compliance Audit (zkCA) / zkSNARK** → 0 refs
- **EQTY Lab Verifiable Compute SDK** → 0 refs (despite `eqty` zero-check)
- **SafeOR-Gym CMDP Action-Shield** → 0 refs

### What this means for the wiki

**The source is the canonical Cemini-state inventory document, but its baseline is now stale by ~7 weeks.** The wiki has been treating its "18 of 42 milestones complete" framing as the authoritative count, but:

1. The **milestone count is unverifiable** because the milestone ledger as an artifact doesn't exist (Track C). Any number cited in this document should carry `[STALE — 2026-03-08 baseline]` with an explicit note about the artifact gap.
2. The **deployed-state claims need a re-check** for the seven-week diff — at minimum: 18→40 containers, Swarm-inactive, the full observability stack (Grafana/Loki/Prometheus/Tempo/Alertmanager/cAdvisor/Alloy) that the source omits entirely.
3. The **"Recommended Tech Stack Upgrades" section is now partially obsolete** — Polars, Pydantic-AI, NautilusTrader, PettingZoo, Schemathesis, Hypothesis, mutmut, Streamlit have all shipped. Only OpenFang, DeepAgents, TorchRL (still), OpenBB, dbmate (in main), VCP/zkCA/EQTY/SafeOR-Gym are genuinely outstanding.
4. The **dual nature of the document** (engineering inventory + IP-sale narrative) means tone-checking matters: pull the inventory facts and discount the strategic framing.

This is the **opposite finding pattern from K3** (which found "the wiki claims more than is built"): K5 finds **"the source under-counts what's been built post-snapshot, but over-claims artifact backing for the milestone ledger itself."** Both directions of staleness are present in the same document.

### Entities referenced
Hetzner, Docker Swarm, TimescaleDB, pgvector, Redis, IntelPublisher/IntelReader, Kalshi, Polymarket, GitHub Actions, Pydantic v2, dbmate, Trivy, Semgrep, Streamlit, GDELT BigQuery, NautilusTrader, OpenFang, Pydantic AI, Pydantic-DeepAgents, TorchRL, PettingZoo, MAPPO, MASAC, Polars, Playwright-skill, OpenBB Platform, Schemathesis, Hypothesis, mutmut, VeritasChain Protocol (VCP), zkSNARK / zkCA, EQTY Lab Verifiable Compute SDK, SafeOR-Gym

### Concepts covered
"Intelligence-in, ticker-out" paradigm, Opportunity Discovery Engine, Strangler Fig migration pattern, Domain-Driven Design (DDD), Multi-Agent Reinforcement Learning (MARL), Constrained Markov Decision Process (CMDP), Multi-Agent Proximal Policy Optimization (MAPPO), Multi-Agent Soft Actor-Critic (MASAC), differential Sharpe ratio reward shaping, Devil's Advocate protocol (Bull/Bear/Risk-Assessor agents), Agentic Context Engineering (ACE), reward hacking, research-to-production gap, IP HoldCo / OpCo dual-structure, Trader Tax Status (Section 475(f) Mark-to-Market election)

## Snippets

> As of the current development phase (v11.0, documented March 8, 2026), the platform has successfully executed 18 of its 42 strategic roadmap milestones.
>
> *— para 2 (Project State Summary). The headline self-assessment. The "18 of 42" count cannot be verified against an artifact because the milestone ledger as a cryptographically-anchored ledger doesn't exist (per @concepts/milestone-ledger.md Track C retraction). What exists is `docs/ROADMAP.md` — a markdown step-list. Numbers count what step the markdown is at; they don't prove milestones shipped per their stated acceptance criteria.*

> The physical infrastructure currently operates on a single Hetzner Virtual Private Server (VPS), deploying approximately 18 Docker containers, with an active migration pathway toward Docker Swarm for resilient, multi-node orchestration.
>
> *— para 2. **Container count is now 40, not 18** (consistent with K4 finding). **`docker info | grep Swarm` returns `Swarm: inactive`** — single-node, no active Swarm migration. The "active migration pathway" framing was either aspirational on 2026-03-08 or has been deferred.*

> Cross-system intelligence and inter-process communication are orchestrated via a password-protected Redis pub/sub message broker, which utilizes a strict IntelPublisher and IntelReader design pattern to broadcast signals across a standardized intel:* namespace.
>
> *— para 2. **Confirmed deployed.** `IntelPublisher` and `IntelReader` patterns appear in 6+ files (rl_training, services, cemini_mcp). The `intel:*` namespace has 30+ channel names enumerated in code: `intel:agent_weights`, `intel:btc_sentiment`, `intel:conviction_composite`, `intel:debate_verdict`, `intel:fred_yield_curve`, `intel:fx:tick:*`, `intel:llm_signal:*`, etc. **This is the strongest as-built confirmation in K5** — and contradicts a narrower K4 finding that `intel:orderbook` / `intel:sentiment` channels don't exist (those specific names don't, but the family does heavily).*

> Furthermore, the system boasts a robust suite of over 263 automated tests, encompassing linting, vulnerability scanning with Trivy and Semgrep, and dependency auditing.
>
> *— para 3. **Server runs 528 tests** (source under-count by 2x — 7-week test growth). Trivy + Semgrep confirmed in `/opt/cemini/.github/workflows/deploy.yml`. The "263" figure is stale; updating to the live count would strengthen the IP-sale narrative not weaken it.*

> The integration of the GDELT BigQuery database for the extraction of geopolitical intelligence signals suffers from a hardcoded 15-minute indexing delay. In modern quantitative finance, where market microstructures and automated market makers (AMMs) react to macroeconomic catalysts in milliseconds, a 15-minute delay on sentiment data renders the resulting signals statistically obsolete and introduces unacceptable adverse selection risks to the trading models.
>
> *— para 6 (Architectural Concurrency and Latency Limitations). **Mechanism shift**: server runs a `gdelt_harvester` container, not a direct BigQuery query path. The 15-min delay criticism the source uses to motivate the OpenFang + Playwright-skill upgrade is at least partially obsolete — the deployed harvester is its own pipeline. The latency claim is unverified post-mechanism-shift; needs spot-measurement.*

> The roadmap indicates an eventual shift toward multi-agent consensus frameworks (Step 31), but relying on traditional Python-based agent orchestrators like LangGraph, AutoGen, or CrewAI introduces severe scalability and infrastructure costs… Scaling this to a society of 40 to 50 concurrent research, analytical, and execution agents would result in multi-gigabyte memory footprints before any useful mathematical computation begins. This overhead renders the current Hetzner CPU-only VPS deployment entirely inadequate and would force a costly migration to distributed managed Kubernetes clusters.
>
> *— para 8 (Multi-Agent Orchestration and Memory Bloat). The argument the source uses to motivate the **OpenFang Rust agent OS** prescription. **OpenFang is not deployed** (zero refs in `/opt/cemini/`). The "40-50 concurrent agents" hypothetical never materialized in the way the source predicted — what the server actually runs is the deployed multi-LLM-analyst pattern in `services/llm_analyst/main.py` plus the LangGraph-style (single shared DeepSeek-API) pattern documented in K's reframe of @concepts/scatter-gather-topology.md. The K series has separately corrected the K + K3 + K4 narrative to reflect that the actual deployed LLM layer is far simpler than the source's "40-50 concurrent Python agents" foil.*

> The execution layer utilizes NautilusTrader, a highly performant, event-driven engine written in Rust that is capable of processing up to 5 million rows per second and modeling L2/L3 order book fills.
>
> *— para 9 (Reinforcement Learning and Execution Paradigm Mismatch). **Confirmed in deps** — `nautilus-trader>=1.190.0` in `/opt/cemini/requirements.txt`. The source's framing as "currently the execution layer" is more accurate than the parallel framing of `ems_executor` as the execution container — Nautilus is the execution **engine library**, while `ems_executor` is the **deployment container** that may or may not wrap it. The PettingZoo ParallelEnv wrapper around NautilusTrader BacktestEngine that Phase 3 prescribes appears to be at least scaffolded — `tests/test_step8_backtesting.py` exists.*

> Currently, the Cemini Suite relies on internal PostgreSQL databases and flat JSONL files for trade logging and performance dashboards. In the context of institutional M&A due diligence, these internal records are fundamentally trust-based and tamper-prone. They cannot mathematically prove to a skeptical buyer that the backtest results were not retroactively altered, selectively omitted, or cherry-picked to hide catastrophic maximum drawdowns.
>
> *— para 10 (Cryptographic Trust and Acquisition Due Diligence Gaps). The motivation for the VCP / zkCA / EQTY prescription. All three remain unbuilt (per server probe; consistent with @concepts/cryptographic-audit-trail.md `[RETRACTED 2026-04-24 Track C]`). The motivation paragraph remains valid as a real gap — buyer-side trust deficit on internal-PG/JSONL trade logs is a real haircut driver.*

> The platform will integrate the VeritasChain Protocol (VCP), an open standard specification for recording algorithmic trading decisions and execution results in an immutable, cryptographically verifiable format.
>
> *— para 22 (Security & Verification Tools). **Will integrate** — explicit forward-looking framing. K's J-pass for @concepts/cryptographic-audit-trail.md correctly identified VCP as prescribed-not-built; this paragraph is the source-side confirmation that the Cemini-internal v11.0 doc itself uses **prescription voice**, not deployment voice, on VCP — the wiki's collapse into present-tense was the synthesis error.*

> To fully insulate the intellectual property during the paper-trading validation phase, the overarching corporate entity should adopt a dual-structure framework: an IP HoldCo (registered in Wyoming or Delaware) that exclusively owns the source code and neural network weights, granting a limited operational license to a trading OpCo (e.g., a Florida LLC). The trading entity must execute a Section 475(f) Mark-to-Market election to achieve "Trader Tax Status," exempting the firm from capital loss limitations and wash sale accounting burdens during high-frequency validation.
>
> *— para 124 (Acquisition Readiness and Valuation Strategy). **Corporate-structure prescription** — out of scope of the technical-deployment probe but worth flagging as an item the wiki has no other coverage of. Worth a future stub at `concepts/ip-sale-corporate-structure.md` if the IP HoldCo / OpCo split becomes operative.*
