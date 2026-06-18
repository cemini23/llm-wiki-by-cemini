---
title: "dev.fun Poker Agent Challenge — operator one-pager (2026-06)"
type: source
tags: [source, devfun, poker-arena, tournament, heads-up, researcher-track]
keywords: [poker agent challenge, dev.fun, heads-up, Tom Dwan, Jungleman, BenchFlow, Daytona, $30K]
related:
  - concepts/devfun-poker-agent-challenge-2026.md
  - concepts/active-project-research-routing.md
  - sources/arxiv-poker-arena-multi-axis-2606-13815-2026-06-18.md
  - entities/platforms/devfun-arena.md
maturity: validated
read_status: read
created: 2026-06-18
updated: 2026-06-18
clusters: [prediction-markets, llm-agents]
---

## Relations

- @concepts/devfun-poker-agent-challenge-2026.md — synthesis + optimization posture for Cemini
- @entities/platforms/devfun-arena.md — platform entity
- @sources/arxiv-poker-arena-multi-axis-2606-13815-2026-06-18.md — academic eval framing (Raeth / IIT Roorkee)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | dev.fun · The Poker Agent Challenge |
| **Author** | dev.fun (operator collateral) |
| **Type** | PDF one-pager |
| **Location** | `research to be indexed/poker-arena-onepager.pdf` → archive after ingest |
| **Retrieved** | 2026-06-18 |
| **Read status** | read (full 3 pages) |
| **sha256** | `19d6f0cda8f4746e164363ead6a4f6fa0ba92674274e3d914d66cd5edd2259bf` |

## Narrative

Invited **researcher track** collateral for the **Poker Agent Challenge** — distinct from ongoing Playground/Tournament **6-max** seasons but same dev.fun Arena stack.

**Prize pool ($30K total):** leaderboard payouts + **researcher pool** (shared across leaderboard) + **sponsored credits** for future Arena seasons for top agents.

**Game format:** **Heads-up** NLHE — build agent → **submit to sandbox** → **score** on one public leaderboard → top agents **published** as challengeable bots under operator name.

**Schedule [CONFIRMED from one-pager]:**

| Date | Event |
|------|--------|
| **Jun 21, 2026** | Closed beta launch — invited researcher community |
| **Jun 25, 2026** | Public launch |
| **Early July 2026** | Finale — championship; top LB agents play **Tom Dwan & Jungleman** head-to-head live on stream |

**Partners (rails):** Monad (agentic payment), OpenRouter (inference), Daytona (sandbox), BenchFlow (eval).

**Why compete (operator framing):** win pool share; seat vs pros on stream; live as **the bot to beat** on platform.

## Snippets

- "Build an AI agent that plays **heads-up** poker, submit it to our **sandbox**, and climb the leaderboard for the prize pool."
- "Top agents go live on as **champion agents** that everyone else can come and challenge."
- "REGISTER TO COMPETE" / Discord for researcher community (links on one-pager; not extracted to plain text).

## Dead Ends

- One-pager does not specify sandbox API, competition ID, or whether HU eval uses same `arena.dev.fun` `/texas/` lobby as 6-max — confirm via Discord / docs before prod pivot.
