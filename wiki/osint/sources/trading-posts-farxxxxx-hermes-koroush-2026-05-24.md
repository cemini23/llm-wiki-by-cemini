---
title: "Trading posts (posts.docx K64) — @farxxxxx1 Polymarket stack, Hermes use cases, @KoroushAK altcoin screener"
type: source
tags: [source, trading-posts, polymarket, hermes-agent, altcoin-screener, k64]
keywords: [farxxxxx1, poly_data, polymarket-cli, polymarket-agents, wallet-screening, kelly, volume-exit, shruti_0810, hermes-agent, koroushak, orion-terminal]
related:
  - entities/tools/warproxxx-poly-data.md
  - entities/tools/polymarket-agents.md
  - entities/tools/hermes-agent.md
  - entities/people/farxxxxx1-polymarket.md
  - entities/people/koroushak.md
  - concepts/polymarket-wallet-alpha-pipeline.md
  - concepts/polymarket-bot-architecture.md
  - concepts/altcoin-screener-orion-workflow.md
  - sources/trading-posts-ai-workflow-polymarket-markov-2026-05.md
  - sources/x-posts-quant-oss-polymarket-bots-2026-05.md
  - concepts/polymarket-copy-trading-strategy.md
  - concepts/prediction-market-historical-analysis.md
  - entities/platforms/polymarket.md
maturity: validated
read_status: deep-read
created: 2026-05-24
updated: 2026-05-24
clusters: [polymarket, trading-posts]
---

## Relations

- @entities/tools/warproxxx-poly-data.md — Post 1 data layer (GPL-3.0; pattern-only)
- @entities/tools/polymarket-agents.md — Post 1 official agent framework (K30 + K64)
- @entities/tools/hermes-agent.md — Post 2 community use-case catalog
- @entities/people/farxxxxx1-polymarket.md — Post 1 author
- @entities/people/koroushak.md — Post 3 author
- @concepts/polymarket-wallet-alpha-pipeline.md — Post 1 synthesized stack
- @concepts/polymarket-bot-architecture.md — Post 1 corroborates exit / backtest lessons
- @concepts/altcoin-screener-orion-workflow.md — Post 3 Orion screener workflow
- @sources/trading-posts-ai-workflow-polymarket-markov-2026-05.md — prior `posts.docx` ingest (different 3 posts; same filename)
- @sources/x-posts-quant-oss-polymarket-bots-2026-05.md — Hermes weather path (K52)

## Raw Concept

- **Title**: `posts.docx` (K64 batch — not the K49 Markov/Morin/bored2boar compilation)
- **Type**: three X long-form posts separated by `Next Post:`
- **Location**: `research to be indexed/posts.docx` → `cemini-librarian:/opt/cemini-bulk/research/posts.docx`
- **Retrieved**: 2026-05-24
- **Read status**: deep-read

## Narrative

### Post 1 — @farxxxxx1: Polymarket bot “every line of code” ($10k / 19 days) [TENTATIVE stats]

**Claimed economics:** ~$11.4k cumulative over 19 days, 214 trades, 74% WR, Sharpe 2.31; infra **$25/mo** (Claude API $20 + Hetzner $5). Treat all PnL as **[TENTATIVE]** promotional.

**Stack (public repos):**

| Layer | Repo | Role |
|-------|------|------|
| Data | `warproxxx/poly_data` (~1.9k★, **GPL-3.0**) | 86M trades; Polars wallet screen → top wallets by PnL + WR |
| Scan | `Polymarket/polymarket-cli` | Agent-oriented CLI: markets list, CLOB book/midpoint, no API key read-only |
| Brain | `Polymarket/agents` (**MIT**, ~3.6k★) | Official agent framework; 4-check Claude loop (base rate, news, whale, crowd bias) |
| Execution | `dylanpersonguy/Polymarket-Trading-Bot` | Claimed 53k LOC TS; 3-agent consensus filter [NEEDS VERIFICATION 2026-05-24 — repo 404 on `gh api`] |

**Mechanisms worth extracting (license-clean-room where GPL blocks import):**

1. **Wallet alpha screen** — `group_by(maker)` → ≥100 trades, WR>70%, rank PnL → `targets.json` (author: top 20 wallets dominate).
2. **Market pre-filter** — gap vs Claude estimate, depth, hours-to-resolution window (drops ~93% of markets).
3. **Quarter-Kelly cap** — `f*` band 0.05–0.15 cited as Sharpe sweet spot.
4. **Consensus entry** — ≥2/3 agents agree BUY; 1/3 → half size.
5. **Exit before resolution** — target at 85% of expected gap; **volume spike** (10m vol > 3× avg); stale thesis 24h; author claims 91% of top-wallet exits pre-resolution, ~73% of max profit.

**Failures reported:** sports (52% WR), low-volume markets, holding to settlement, running all 7 strategies at once.

→ @concepts/polymarket-wallet-alpha-pipeline.md

### Post 2 — @Shruti_0810: 276 Hermes Agent use cases [TENTATIVE catalog]

Community roundup positioning Hermes as **persistent autonomous infrastructure** (not chatbot): dev swarms, messaging integrations (Telegram, Slack, Gmail, …), business ops, content pipelines, research briefings, K8s enterprise deployments.

No new trading edge — **updates** @entities/tools/hermes-agent.md with K64 deployment taxonomy. Overlaps K52 @0xMovez weather deploy path.

### Post 3 — @KoroushAK: Altcoin discovery via Orion Terminal screener

Discretionary **crypto alt** workflow (not Polymarket): five-column Orion layout — Symbol, TRD (5M), Change % (5M/1D), Volume (5M). Rules: TRD sort → top 10 → drop if Volume (5M) <$500k → narrow to 5–6 names via extreme 5M/1D movers. Market-regime heuristics: high TRD + clean direction = breakout day; low TRD + mixed = reversal day. Price-action follow-on: staircases vs spike reversals.

Promotional CTAs (paid video, Orion affiliate). Methodology is **[TENTATIVE]** single-source but structurally sound for liquidity/attention filtering.

→ @concepts/altcoin-screener-orion-workflow.md

### Duplicate filename note

`preingest_check.py` flagged **LIKELY** duplicate of @sources/trading-posts-ai-workflow-polymarket-markov-2026-05.md (same `posts.docx` name). **Content is disjoint** — proceed as K64; librarian canonical file is this drop (2026-05-24).

## Snippets

> "91% of exits happen before resolution. Average capture: 73% of max potential profit. Primary trigger: volume spike." [Source: posts.docx Post 1, @farxxxxx1, 2026-05-24]

> "The repos are free… The only question: will you build it this weekend" [Source: same]

> "2026: People started building AI systems that work instead of them." [Source: posts.docx Post 2, @Shruti_0810]
