---
title: dev.fun Poker Arena — researcher track invite email (2026-06-19)
type: source
tags: [source, email, devfun, poker-arena, researcher-track, heads-up, trueskill]
keywords: [researcher-track, heads-up, trueskill, self-play-sdk, kaggle, tom-dwan, jungleman]
related:
  - concepts/devfun-researcher-track-readiness-2026-06.md
  - concepts/devfun-poker-agent-challenge-2026.md
  - concepts/devfun-researcher-pre-submit-recon.md
  - concepts/devfun-researcher-pro-style-targets-2026-06.md
  - sources/devfun-researcher-track-discord-welcome-2026-06-18.md
  - sources/devfun-researcher-track-hu-format-2026-06-08.md
  - sources/web-pro-villain-profiles-dwan-cates-2026-06-19.md
  - entities/platforms/devfun-arena.md
maturity: validated
read_status: read
created: 2026-06-19
updated: 2026-06-19
cross-wiki:
  - "@gambling-wiki/sources/devfun-poker-researcher-track-email-2026-06-19.md"
---

## Relations

- @gambling-wiki/sources/devfun-poker-researcher-track-email-2026-06-19.md — **canonical ingest** (full narrative + snippets)
- @concepts/devfun-researcher-track-readiness-2026-06.md
- @concepts/devfun-poker-agent-challenge-2026.md
- @entities/platforms/devfun-arena.md

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | dev.fun researcher track invite (devlord → cemini23) |
| **Author** | devlord (dev.fun co-founder) |
| **Type** | Email |
| **Retrieved** | 2026-06-19 |
| **Read status** | read (via @gambling-wiki ingest K121) |

## Narrative

Primary-source confirmation for Researcher track mechanics beyond Discord welcome. **Canonical page:** `@gambling-wiki/sources/devfun-poker-researcher-track-email-2026-06-19.md`.

**New vs prior OSINT posture [CONFIRMED email]:**

| Item | Email says | Prior OSINT assumption |
|------|------------|------------------------|
| Format | **Heads-up** sandbox | HU [CONFIRMED 2026-06-08 relay] — now devlord primary source |
| **Ranking** | **TrueSkill** (pairwise skill) | Chip LB + trajectory / Raeth multi-axis [TENTATIVE] |
| Champion | Top agent = **benchmark bot** field must beat | Aligns with one-pager funnel |
| Pro selection | Dwan + Jungleman pick **style-matched** bots | Finale HU spectacle only |
| Tooling | Self-play SDK, **Kaggle** page, sponsored credits | Arena `pokerkit run` only |
| Submit types | Python bot, weights, fine-tune, LLM + own key | Fixed engine + `decide()` only [PR] |

**Optimization read (Cemini):** TrueSkill rewards **HU win rate vs the sandbox opponent distribution** — not Playground chip rank. Trajectory + M₁–M₉ gates remain **ship discipline** (Discord research contribution + style transparency); they may not be the LB sort key. Add **pro-style overlays** (Dwan/Jungleman villain profiles) as a secondary target for rep selection, not only TrueSkill #1.

Timeline unchanged: **Jun 21** closed beta · **Jun 25** public sandbox.

## Snippets

> "we run it heads-up in a sandbox, ranked by TrueSkill" [Source: @gambling-wiki/sources/devfun-poker-researcher-track-email-2026-06-19.md]

> "the top agent becomes the bot everyone else has to beat" [Source: @gambling-wiki/sources/devfun-poker-researcher-track-email-2026-06-19.md]

> "Tom Dwan and Jungleman … pick the bots that play most like them" [Source: @gambling-wiki/sources/devfun-poker-researcher-track-email-2026-06-19.md]
