---
title: "Trading posts compilation (Posts.docx K97) — 17 X long-forms"
type: source
tags: [source, trading-posts, agent-harness, polymarket, world-cup-2026, quant-framework, k97]
keywords: [horizon-trade, claude-code-cheat-sheet, dynamic-workflows, deflated-sharpe, rohonchain, gustafssonkotte, hermes-goal, rubrics-agents, codex-course]
related:
  - sources/trading-posts-compilation-12-2026-06-01.md
  - concepts/monokern-compounding-research-pipeline.md
  - entities/people/damidefi.md
  - sources/rohonchain-fifa-wc-shock-recovery-strategy-2026-06-02.md
  - concepts/polymarket-marginal-polytope-arbitrage.md
  - concepts/polymarket-football-shock-recovery-trading.md
  - concepts/regime-conditioned-evaluation.md
  - concepts/claude-code-skills-md-workflow.md
  - entities/people/rohonchain.md
  - entities/people/gustafssonkotte.md
  - entities/tools/hermes-agent.md
  - entities/tools/world-cup-bot.md
  - "@seo-wiki/concepts/x-account-voice-and-format.md"
  - "@ccc-wiki/briefs/2026-06-03_k97-ccc-agent-harness-from-osint.md"
  - "@ccc-wiki/sources/trading-posts-compilation-17-2026-06-03.md"
maturity: draft
read_status: read
created: 2026-06-03
updated: 2026-06-03
clusters: [agent-harness, polymarket-quant, seo-funnel]
---

## Relations

- @sources/trading-posts-compilation-12-2026-06-01.md — prior batch (different sha256)
- @sources/rohonchain-fifa-wc-shock-recovery-strategy-2026-06-02.md — Post 17 ≈ same FIFA shock article (K94 deep-read)
- @entities/tools/world-cup-bot.md — Module 8 implements shock path (not Dome)
- @ccc-wiki/briefs/2026-06-03_k97-ccc-agent-harness-from-osint.md — harness cluster handoff
- @seo-wiki/concepts/x-account-voice-and-format.md — K97 style pass

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | `Posts.docx` K97 — 17 posts (`Next Post:` delimiter) |
| **Type** | X long-form compilation |
| **sha256** | `bf5682b3cdc56cee8c8aad39f1afd47288002f03aed37096406a1ae8ea16e4e1` |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/trading-posts-compilation-17-2026-06-03.docx` |
| **Retrieved** | 2026-06-03 |
| **Read status** | read (skim all 17; harness → CCC; Roh FIFA → K94 canon) |

**Not** K92 (`cc168e87…`) or K93 (`…31 posts`) — same filename; hash discipline required. Preingest: **LIKELY** filename collision with older Posts drops — this hash is distinct.

## Narrative

K97 full ingest. **~55% agent-harness / Claude Code / Codex / Hermes / NotebookLM** → **CCC-wiki** (brief + source stub). **~25% Polymarket quant** (@RohOnChain Posts 15–17, marginal polytope + WC shock) → OSINT concepts (Post 17 duplicate of K94 source). **~10% discretionary TA** (@KoroushAK ZCT) → thin reference only. **~10% product funnels** (Horizon closed beta, startup-for-agents) → SEO voice pass; no prod adopt.

### Post index

| # | Author | Theme | Route |
|---|--------|-------|-------|
| 1 | @horizon_trade_x | Deflated Sharpe + four desk questions; Horizon plain-English backtest beta | OSINT `regime-conditioned-evaluation` + SEO |
| 2 | @0x_rody | Claude Code cheat sheet (70+ commands) | CCC |
| 3 | @0xCodez | Dynamic workflows (Anthropic engineer patterns) | CCC |
| 4 | @ericzakariasson | Runtime context vs agent guessing | CCC |
| 5 | @0xDepressionn | Prompt cost cut $7.8k→$129 | CCC |
| 6 | @sydneyrunkle | Rubrics — agents self-evaluate/correct | CCC |
| 7 | @KoroushAK | ZCT price action masterclass | skip (discretionary TA) |
| 8 | @zaimiri | Hermes `/goal` full guide | CCC + `hermes-agent` |
| 9 | @startupideaspod | Build startups for agents | SEO / skip |
| 10 | @0xCodez | Codex 30-min course | CCC |
| 11 | @Zephyr_hg | Claude setup for solo consultants ($4k/mo research team) | CCC + SEO |
| 12 | @Gustafssonkotte | Live bot interim — 12 trades, fast vs slow market WR | OSINT `gustafssonkotte` |
| 13 | @eng_khairallah1 | Claude Cowork full-day automation course | CCC |
| 14 | @zeuuss_01 | Claude + NotebookLM + Obsidian 6 min pipeline | CCC + `monokern` |
| 15 | @RohOnChain | PM math roadmap — marginal polytope, Bregman, ILP | OSINT `polymarket-marginal-polytope-arbitrage` |
| 16 | @DamiDefi | Opus + Kimi agent swarm — 50 YC startups | CCC + `damidefi` |
| 17 | @RohOnChain | FIFA quant WC strategy (shock recovery) | **K94 duplicate** — backlink only |

### Prod / WC notes

- Post 17 still references **Dome API** for historical tapes — OSINT canon: Dome EOL 2026-04-28; use Polymarket Data API + live WS per `@projects/world-cup-bot/Architecture - match_shock_v1.md`.
- Post 12 public timestamp: **fast tape → wins, slow tape → losses** — reinforces K62/K93 tape-speed discipline before WC **14:00 UTC storm window** [TENTATIVE single-day n=12].

## Snippets

> "They called it the Deflated Sharpe Ratio." [Source: Posts.docx K97 Post 1, @horizon_trade_x]

> "Claude Code has 70+ commands, 12 keyboard shortcuts, and 30+ CLI flags. Most people use about 5 of them." [Source: Posts.docx K97 Post 2, @0x_rody]

> "12 trades · 10 wins, 2 losses · WR 83% … 2 losses came on a slow market · 10 wins on a fast one" [Source: Posts.docx K97 Post 12, @Gustafssonkotte]

> "Sophisticated traders extracted $40 million in guaranteed arbitrage profits from Polymarket in one year." [Source: Posts.docx K97 Post 15, @RohOnChain — aligns with arXiv 2508.03474 via @robrtcode K67]

> "will those overreactions get larger because of all the inexperienced money, or will they get smaller because of all the new liquidity?" [Source: Posts.docx K97 Post 17, @RohOnChain — WC sizing hypothesis for shock module]
