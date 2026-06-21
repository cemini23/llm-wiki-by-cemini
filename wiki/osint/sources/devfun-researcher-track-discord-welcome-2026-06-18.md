---
title: dev.fun researcher-track Discord welcome — Researcher Round (2026-06)
type: source
tags: [source, devfun, poker-arena, researcher-track, discord]
keywords: [researcher round, sandbox benchmark, trajectory data, 50 seats, closed beta]
related:
  - concepts/devfun-poker-agent-challenge-2026.md
  - concepts/devfun-researcher-track-readiness-2026-06.md
  - concepts/devfun-researcher-pre-submit-recon.md
  - sources/devfun-poker-agent-challenge-onepager-2026-06-18.md
  - sources/devfun-poker-researcher-track-email-2026-06-19.md
  - sources/devfun-researcher-sandbox-bundle-discord-2026-06-20.md
  - sources/devfun-researcher-track-hu-format-2026-06-08.md
  - sources/arxiv-poker-arena-multi-axis-2606-13815-2026-06-18.md
  - entities/platforms/devfun-arena.md
maturity: validated
read_status: read
created: 2026-06-18
updated: 2026-06-08
clusters: [prediction-markets, llm-agents]
---

## Relations

- @concepts/devfun-poker-agent-challenge-2026.md
- @sources/devfun-poker-agent-challenge-onepager-2026-06-18.md
- @entities/platforms/devfun-arena.md
- @concepts/devfun-poker-competitor-github-recon-2026-06.md — public competitor repos (gin/poker-bot, kecodot, system7)
- @sources/devfun-researcher-track-hu-format-2026-06-08.md — **HU format confirmed** for Researcher sandbox (supersedes 6-max assumption below)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | researcher-track channel welcome post |
| **Author** | dev.fun (Discord operator) |
| **Type** | Discord message (operator relay) |
| **Location** | Discord `#researcher-track` |
| **Retrieved** | 2026-06-18 |
| **Read status** | read |

## Narrative

Official welcome in the **researcher-track** Discord channel for invited researchers. Names the next phase **Researcher Round** — distinct wording from one-pager “Poker Agent Challenge” but same Jun 21 closed beta gate.

**Confirmed facts [CONFIRMED]:**

| Item | Detail |
|------|--------|
| Prize pool | **$30,000** |
| Capacity | **50 seats** — invited researcher community only |
| Closed beta | **June 21** launch |
| Eval goal | Sandbox benchmark studying **how** agents play, not only whether they win |
| Workflow | Submit agent → run in arena → **pull full trajectory data** |
| Meta | Participants help shape **next version of agent evaluation** |
| Follow-up | More details promised in channel; questions welcome |

One-pager shared again in-channel (see `@sources/devfun-poker-agent-challenge-onepager-2026-06-18.md`).

**Operator assumptions (2026-06-18)** — partially superseded:

| Item | Working assumption | Status |
|------|-------------------|--------|
| Table size | ~~**6-max**~~ | [RETRACTED] — **HU** [CONFIRMED 2026-06-08] `@sources/devfun-researcher-track-hu-format-2026-06-08.md` |
| Match length | **Multi-day** continuous season (like Playground/Tournament) — **not** Eval 500h; official params not posted | [TENTATIVE] |
| Submit cadence | Same arena loop as existing poker comps until skill contradicts | [TENTATIVE] |
| Fixed engine + LLM | Accept PR wording [CONFIRMED per PR] until sandbox skill contradicts | [CONFIRMED] |

## Snippets

- "We're opening the next important round of Poker Arena: the **Researcher Round**, with a **$30,000** prize pool."
- "This round is limited to **50 seats** and is open to the invited researcher community."
- "The **Closed Beta Launch starts on June 21**."
- "This track is designed as a **sandbox benchmark** for studying how poker agents actually play, not just whether they win."
- "You'll be able to submit an agent, run it through the arena, **pull full trajectory data**, and help shape what the next version of agent evaluation should look like."
