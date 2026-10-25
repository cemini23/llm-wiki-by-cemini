---
title: "Gemini DR — GitHub sports betting & PM bot landscape (targeted links)"
type: source
read_status: read
tags: [source, gemini-deep-research, github, sports-betting, polymarket, phase-0, k86]
keywords: [open-source, copy-trading, cross-venue, agents, skillnet, ops-hygiene, steal-from]
related:
  - sources/world-cup-github-repo-eval-2026-05-29.md
  - entities/tools/world-cup-bot.md
  - entities/tools/polymarket-agents.md
  - concepts/cross-venue-arbitrage-pattern.md
  - concepts/world-cup-advance-market-bot-v1.md
  - concepts/production-trading-blind-spots.md
  - concepts/cemini-workflow-tooling-audit-2026-05-30.md
  - entities/tools/skillnet.md
  - concepts/gambling-wiki-federation.md
  - entities/tools/sportsbook-api-evangelist.md
  - sources/eval-github-repo-plan-dfs-marl-poker-osint-2026-07-01.md
maturity: validated
created: 2026-05-30
updated: 2026-10-25
---

## Relations

- @sources/world-cup-github-repo-eval-2026-05-29.md — K82 **targeted** 29-repo Phase-0 (WC bot fit); this report is **broader landscape** with PM/agent emphasis
- @entities/tools/polymarket-agents.md — official Polymarket RAG agent framework (report § agents)
- @entities/tools/world-cup-bot.md — primary consumer for steal-from queue
- @concepts/cross-venue-arbitrage-pattern.md — PM×Kalshi + sharp/soft book patterns

## Raw Concept

| Field | Value |
|-------|-------|
| Title | The Convergence of Autonomous AI Agents, ML, and Decentralized Prediction Markets: A Comprehensive Analysis of Open-Source Financial Software |
| Author | Gemini Deep Research (user targeted-links session) |
| Type | docx synthesis report |
| Location | `cemini-librarian:/opt/cemini-bulk/research/GitHub Sports Betting Repositories Evaluation.docx` |
| Retrieved | 2026-05-30 |
| Read status | deep-read (skim on classical ML / computer-vision sections; deep on PM + agents + ops security) |

## Narrative

Broad Gemini survey of **open-source sports betting, arbitrage, DRL trading, Polymarket bots, and LLM agents** — with extensive works-cited URLs. Complements K82's narrow World-Cup-bot Phase-0 batch; use this for **landscape context** and **v2 steal-from candidates**, not as a license to adopt unvetted repos.

### Stack layers (report taxonomy)

| Layer | Examples | WC bot relevance |
|-------|----------|------------------|
| Data ingestion | `roclark/sportsipy`, `bttmly/nba` (schema-driven clients) | Low — we use Gamma + openfootball |
| Classical ML / DFS | `kyleskom/NBA-Machine-Learning-Sports-Betting`, `pydfs-lineup-optimizer` | **Reject** for LP bot (fundamental edge ≠ market making) |
| Fiat book arbitrage | `personal-coding/Live-Sports-Arbitrage-Bet-Finder`, `pretrehr/Sports-betting` (Pinnacle sharp vs Bwin soft) | **Reference** — sharp/soft latency pattern; alert-only analog to PM↔Kalshi |
| DRL / quant finance | `stefan-jansen/machine-learning-for-trading` | Reference for microstructure features; not v1 scope |
| **Polymarket sports** | `GastonDeMichele/Polymarket-Sports-Bot` | **Phase-0 candidate** — PM + SX Bet smart router (TypeScript) |
| PM momentum / HFT | `GastonDeMichele/Polymarket-Momentum-Trading-Bot` | **Reject for LP** — momentum taker ≠ conviction LP |
| Copy-trading | `Polymarket-Copytrading-Bot`, `Dadel-1/Polymarket-CopyTrading` | **Reject** — wallet surveillance; adverse flow amplifier |
| PM×Kalshi niche | `suislanchez/polymarket-kalshi-weather-bot` | **Reference** — cross-venue arb + Kelly sizing pattern |
| Skeptic LP | `sterlingcrispin/nothing-ever-happens` | **Steal-from (ops)** — Polygon RPC, Heroku lifecycle scripts, test coverage — not strategy |
| **Official agents** | `Polymarket/agents` | **Reference** — RAG + Gamma/CLOB split; see @entities/tools/polymarket-agents.md |
| Skill networks | `zjunlp/SkillNet`, `himself65/finance-skills` | Meta — agent tooling; finance-skills already in operator stack |
| AI-for-AI | `sjtu-sai-agents/ML-Master` | Out of scope — self-modifying pipelines |
| Security caution | `ThemeBoy/SportsPress` CVE RFI; `.env` key leaks on `Polymarket/agents` setup | Reinforces TruffleHog + never commit keys [CONFIRMED industry pattern] |

### Phase-0 queue additions (post-K82)

| Repo | Verdict | Rationale |
|------|---------|-----------|
| `GastonDeMichele/Polymarket-Sports-Bot` | **CONDITIONAL-GO audit** | Cross-venue fetch + routing patterns for v2; verify license + no hardcoded geoblock bypass |
| `sterlingcrispin/nothing-ever-happens` | **Steal-from (ops only)** | Deployment scripts, RPC approval flow, CI — not market logic |
| `suislanchez/polymarket-kalshi-weather-bot` | **Reference** | PM×Kalshi polling architecture; weather ≠ WC |
| `Polymarket/agents` | **Reference** | Already evaluated in wiki; RAG/Chroma pattern for research CLI only |
| Copy-trading bots (multiple) | **NO-GO** | Strategy mismatch + toxic flow amplification |

### Sharp vs soft (fiat) → PM×Kalshi analog [TENTATIVE]

Report: Pinnacle as **sharp** reference, Bwin/PMU as **soft** execution targets. Analog: Kalshi regulated lines vs PM CLOB for **alert-only** fade_watch — not autonomous arb without DR-verified pairs (@concepts/cross-venue-arbitrage-pattern.md).

### Finance-skills table (report appendix)

Report cites `himself65/finance-skills` nodes (`yfinance-data`, `options-payoff`, `stock-correlation`, etc.) — confirms operator's installed finance-skills marketplace; no WC-bot code dependency.

## Snippets

> Copy-trading bots cascade when a whale trades — hundreds of bots consume order book liquidity in seconds, amplifying slippage. [Source: GitHub Sports Betting Repositories Evaluation.docx]

> `nothing-ever-happens` operational hygiene: Polygon RPC integrations, Heroku alive/kill/logs scripts, comprehensive test coverage — steal deployment patterns, not "buy No on everything" thesis. [Source: GitHub Sports Betting Repositories Evaluation.docx]

> Accidental `.env` commit with `POLYGON_WALLET_PRIVATE_KEY` remains the most common catastrophic loss vector in open-source PM repos. [Source: GitHub Sports Betting Repositories Evaluation.docx]
