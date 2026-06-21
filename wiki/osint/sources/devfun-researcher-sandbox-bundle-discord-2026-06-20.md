---
title: dev.fun Researcher sandbox — bundle submission Discord (2026-06-20)
type: source
tags: [source, discord, devfun, poker-arena, researcher-track, sandbox, bundle]
keywords: [bundle-submit, submission-interface, heuristic-bot, llm-byok, trueskill, heads-up]
related:
  - concepts/devfun-researcher-track-readiness-2026-06.md
  - concepts/devfun-researcher-pre-submit-recon.md
  - concepts/devfun-poker-agent-challenge-2026.md
  - sources/devfun-poker-researcher-track-email-2026-06-19.md
  - sources/devfun-researcher-track-discord-welcome-2026-06-18.md
  - entities/platforms/devfun-arena.md
maturity: validated
read_status: read
created: 2026-06-20
updated: 2026-06-20
cross-wiki:
  - "@gambling-wiki/sources/devfun-researcher-sandbox-bundle-discord-2026-06-20.md"
---

## Relations

- @gambling-wiki/sources/devfun-researcher-sandbox-bundle-discord-2026-06-20.md — **canonical ingest** (full narrative + snippets)
- @concepts/devfun-researcher-track-readiness-2026-06.md — ops hub
- @concepts/devfun-researcher-pre-submit-recon.md — pre-submit ritual

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Researcher sandbox bundle submission (Discord relay) |
| **Retrieved** | 2026-06-20 |
| **Read status** | read (via @gambling-wiki ingest) |

## Narrative

Canonical page: `@gambling-wiki/sources/devfun-researcher-sandbox-bundle-discord-2026-06-20.md`.

**New vs prior OSINT posture [CONFIRMED Discord 2026-06-20]:**

| Item | Discord says | Prior assumption |
|------|--------------|------------------|
| Submit surface | **Bundle files** → sandbox eval → leaderboard | `pokerkit run` + prod lobby primary |
| Agent types | Heuristic, LLM, weights, solver — **interface-conformant** | Heuristic `decide()` only (still correct lane) |
| LLM BYOK | Encrypted; **per-submission isolated sandbox** | Fixed engine / no runtime LLM [CONFIRMED PR] |
| LLM recommendation | **Not recommended** — poor results + high cost | Already out of scope for Cemini |
| Details | **Submission spec coming soon** | K123 checklist waiting on SDK/Kaggle |

**Cemini action:** hold bundle packaging until interface docs; continue HU gates + trajectory; no `llm_agent.py` path for sandbox.

## Snippets

> "if builders want to submit llm agent, builders' byok are encrypted and injected only into that submission's own isolated sandbox at runtime so will be safe." [Source: dev.fun Discord 2026-06-20 (retrieved 2026-06-20)]
