---
title: "Trading posts compilation (Posts.docx K88) — 42 X long-forms"
type: source
tags: [source, trading-posts, polymarket, hyperliquid, agent-harness, k88]
keywords: [karpathy, myttle, dankoweb3, fabianosolana, functionspace, betashop, cyrilXBT, polydao, ruflo]
related:
  - sources/trading-posts-compilation-k84-2026-05-30.md
  - sources/trading-posts-compilation-38-2026-05-26.md
  - concepts/polymarket-bot-architecture.md
  - concepts/polymarket-negative-filter-trading.md
  - concepts/polymarket-updown-indicator-stack.md
  - concepts/polymarket-lp-rewards-farming.md
  - concepts/hyperliquid-agent-trading.md
  - entities/platforms/hyperliquid.md
  - entities/tools/finance-skills.md
  - entities/tools/hermes-agent.md
  - "@seo-wiki/concepts/x-account-voice-and-format.md"
  - "@ccc-wiki/sources/trading-posts-compilation-42-2026-05-31.md"
  - "@ccc-wiki/concepts/karpathy-agent-infrastructure-basics.md"
  - "@ccc-wiki/concepts/claude-code-subagent-templates.md"
  - "@ccc-wiki/concepts/claude-harness-dynamic-workflows-k88.md"
  - "@ccc-wiki/entities/tools/ruflo.md"
maturity: draft
read_status: read
created: 2026-05-31
updated: 2026-05-31
clusters: [polymarket, hyperliquid, agent-harness, obsidian-ccc]
---

## Relations

- @sources/trading-posts-compilation-k84-2026-05-30.md — prior batch (different sha256)
- @concepts/polymarket-bot-architecture.md — operator taxonomy extended by K88 PM posts
- @seo-wiki/concepts/x-account-voice-and-format.md — K88 style pass

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | `Posts.docx` K88 — 42 posts (`Next Post:` delimiter) |
| **Type** | X long-form compilation |
| **sha256** | `5449697ba75686e885fd8bffafcdd8c2168c0d1b704014b0b6e1660f05483c9f` |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/trading-posts-compilation-42-2026-05-31.docx` |
| **Retrieved** | 2026-05-31 |
| **Read status** | read (PM/HL clusters deep-read; agent-harness cluster skimmed → CCC routing) |

**Not** K84 (`43198b3e…`) or K69/K67 — same filename, verify hash.

## Narrative

Largest post count since K73/K67. **~60% agent-harness / Obsidian / Claude Code** (CCC-wiki territory). **OSINT-high-signal PM/HL cluster (~5 posts)** below. Remainder: macro (ecoinometrics), LinkedIn funnels, Venice tokenomics — low OSINT priority.

### P0 — Polymarket / prediction markets

| Post | Author | Thesis | Wiki action |
|------|--------|--------|-------------|
| 10 | @myttle_web3 | **Negative filter** — bot finds what *not* to trade before speed optimization | `@concepts/polymarket-negative-filter-trading.md` |
| 18 | @DankoWeb3 | 10 indicators for PM UP/DOWN crypto markets | `@concepts/polymarket-updown-indicator-stack.md` |
| 22 | @functionspaceHQ | "Beyond the Odds" — FOMC dot plot vs PM; weather/Kalshi framing | extend `@concepts/polymarket-weather-trading-strategy.md` stub note |
| 36 | @FabianoSolana | Consolidated PM beginner guide (LP, spreads, discipline) | backlink `@concepts/polymarket-lp-rewards-farming.md` |
| 4 | @polydao | Claude Skills ecosystem map (GitHub links) | overlaps K88 tool eval; CCC cross-ref |

### P1 — Hyperliquid / perps

| Post | Author | Thesis | Wiki action |
|------|--------|--------|-------------|
| 39 | @betashop | HL agent dropped 16pts in 48h then self fine-tuned | `@concepts/hyperliquid-agent-trading.md` stub |

### P2 — Quant / ML (reference)

| Post | Author | Note |
|------|--------|------|
| 25 | @RohOnChain | Neural nets "win every trade" — promotional; overlaps `@sources/trading-posts-2-time-series-openhuman-conflict-detector-lp-tactics-2026-05.md` |
| 1 | @TheSuperEng | ML metrics primer — textbook, no trading edge |

### P3 — CCC / workflow (cross-wiki, not OSINT concept pages)

Karpathy 7 tips (@ScottyBeamIO), Cyril Hermes course (06), Obsidian purge (07), Khairallah Obsidian×Claude (09, 30), Claude harness posts (27–29, 32–34, 38), Ruflo swarm (@Damir_Akaza 41), subagent template (@0x_rody 02). **Route:** `Cemini claude code CCC/briefs/2026-05-31_k88-ccc-workflows-and-tool-eval-from-osint.md`

### SEO style-pass

Ran seo-wiki `prompts/posts-docx-style-pass.md` — Karpathy number-led framework + Cyril course-format posts added to exemplar table.

## Snippets

> "I wanted a Polymarket bot to trade faster. then i looked at my own trades and realized speed was not the first problem." [Source: Posts.docx K88 Post 10, @myttle_web3]

> "10 indicators that have stood the test of time and proven their edge … especially on Polymarket UP/DOWN." [Source: Posts.docx K88 Post 18, @DankoWeb3]

> "The Top Hyperliquid Agent Dropped 16 Points in 48 Hours. Then It Fine-Tuned Itself." [Source: Posts.docx K88 Post 39, @betashop]

## Dead Ends

- **@RohOnChain Post 25** — "win every trade" framing is marketing; keep as `[TENTATIVE]` counterexample, not a strategy adopt.
