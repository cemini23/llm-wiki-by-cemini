---
title: "Trading posts compilation (Posts.docx K107) — 17 X long-forms"
type: source
tags: [source, trading-posts, polymarket, agent-harness, quant-framework, poker, k107]
keywords: [dynamic-workflows, claude-skills, lp-farming, ols-alpha, open-spot-preflop, notebooklm, fear-index, weather-markets, kaiynne-org]
related:
  - sources/trading-posts-compilation-6-2026-06-08.md
  - concepts/polymarket-lp-rewards-farming.md
  - concepts/ols-alpha-signal-framework.md
  - concepts/agent-team-five-gate-decision-memo.md
  - concepts/polymarket-weather-trading-strategy.md
  - sources/arxiv-aarri-research-intern-bench-2606-07462-2026-06-09.md
  - "@ccc-wiki/briefs/2026-06-09_k107-ccc-dynamic-workflows-skills-from-osint.md"
  - "@seo-wiki/concepts/x-account-voice-and-format.md"
maturity: draft
read_status: read
created: 2026-06-09
updated: 2026-06-09
clusters: [polymarket-quant, agent-harness, market-making, poker]
---

## Relations

- @sources/trading-posts-compilation-6-2026-06-08.md — prior batch (K106)
- @concepts/polymarket-lp-rewards-farming.md — Post 14 LP window tactics
- @concepts/ols-alpha-signal-framework.md — Post 15 OLS alpha pipeline
- @concepts/agent-team-five-gate-decision-memo.md — Post 7 org layers (extends K98)
- @concepts/polymarket-weather-trading-strategy.md — Post 6 weather WR claim
- @sources/arxiv-aarri-research-intern-bench-2606-07462-2026-06-09.md — Post 5 adjacent (self-repair harness)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | `Posts.docx` K107 — 17 posts (16 `Next Post:` delimiters + opener) |
| **Type** | X long-form compilation |
| **sha256** | `5b174d74b929c918679111c41c21de7c405e96f5237ae79c76435b0438062877` |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/trading-posts-compilation-7-2026-06-09.docx` |
| **Retrieved** | 2026-06-09 |
| **Read status** | read (all 17 skimmed; prod/CC/poker routes assigned) |

Preingest: **LIKELY** filename collision with older Hermes compilation location field — hash distinct from K106 (`76b26ee5…`) and all prior batches.

## Narrative

K107 full inbox + daily digest arXiv batch. **~25% agent harness** (Posts 0–5, 8, 13) → CCC brief. **~20% PM ops** (Posts 9–11, 14) → prod + LP concept update. **~15% quant** (Post 15) → OLS concept. **~10% org** (Post 7) → five-gate memo update. **~10% weather** (Post 6) → weather strategy xref. **~10% poker** (Post 16) → arena preflop bug brief. **~10% SEO/tooling** (Posts 2–4, 12) → SEO style pass + source index only.

### Post index

| # | Author | Theme | Route |
|---|--------|-------|-------|
| 0 | @PawelHuryn | Claude dynamic workflows — orchestrator off-model (113 agents, ultracode) | CCC brief |
| 1 | @cyrilXBT | Claude Skills full course (Hermes/Claude Code layout) | CCC brief |
| 2 | @Zephyr_hg | Gmail/Calendar/Drive → Claude in 30 min | SEO style pass |
| 3 | @TimJayas | Codex tokens 245M→28M/day (caching, scope) | CCC brief |
| 4 | @0xDepressionn | $336K ARR Claude Code startup stack | CCC xref |
| 5 | @akshay_pachaar | Self-repairing agent harness (observability gap) | CCC + AARRI xref |
| 6 | @Emotion_web3 | Weather markets 86% WR narrative | weather strategy xref |
| 7 | @kaiynne | Four org layers (research/plan/exec/growth) for agentic teams | five-gate memo update |
| 8 | @0xwhrrari | Claude Projects setup discipline | CCC brief |
| 9 | @0x_Punisher | PM fear index — cluster repricing speed | PM concept stub (digest) |
| 10 | @igor_mikerin | Polymarket beginner mistakes (referral promo) | PM architecture xref |
| 11 | @maqxbt | AI agents trading PM (Polystrat/Olas promo) | REFERENCE only |
| 12 | @vorty279 | 100 OSS AI repos by niche | source index; no Phase-0 farm |
| 13 | @xanaxmontanaonx | NotebookLM industry research notebook | OSINT/CCC xref |
| 14 | @0xbobaaa | LP farm ~$1M/day fees — 21–24h window, unfilled orders goal | prod + LP concept |
| 15 | @RohOnChain | OLS alpha / IC / OOS / Newey-West gauntlet | `ols-alpha-signal-framework` |
| 16 | @3d64r_89 | Arena PFR bug — `call_chips==0` vs open spot | poker agent brief |

## Snippets

> "The orchestrator moved off the model and into code. The agents do the work; the code that coordinates them spends zero model tokens." [Source: Posts.docx K107, @PawelHuryn Post 0]

> "The goal of LP farming is to place an order that never gets filled… find a market resolving in 21–24 hours." [Source: Posts.docx K107, @0xbobaaa Post 14]

> "detect open spots with current_bet <= big_blind instead" of `call_chips == 0`. [Source: Posts.docx K107, @3d64r_89 Post 16]
