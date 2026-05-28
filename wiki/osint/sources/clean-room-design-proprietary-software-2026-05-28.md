---
title: Clean-Room Design for Proprietary Software — Legal and Technical Isolation
type: source
tags: [source, legal, clean-room, gpl, pmxt, discountifu, k77]
keywords: [clean-room, GPL, AGPL, pmxt, discountifu, reverse-engineering, trade-secret]
related:
  - concepts/clean-room-software-design.md
  - entities/tools/discountifu-polymarket-trading-bot.md
  - concepts/polymarket-bot-architecture.md
maturity: draft
created: 2026-05-28
updated: 2026-05-28
---

## Relations

- @concepts/clean-room-software-design.md
- @entities/tools/discountifu-polymarket-trading-bot.md — R11 target
- @concepts/polymarket-bot-architecture.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Clean-Room Design for Proprietary Software |
| Type | docx |
| Location | `cemini-librarian:/opt/cemini-bulk/research/Clean-Room Design for Proprietary Software.docx` |
| Retrieved | 2026-05-28 |
| Read-status | deep-read |

## Narrative

Clean-room isolates **specification** (what) from **implementation** (how) to avoid GPL/AGPL contamination when building proprietary trading stacks adjacent to open-source (pmxt, discountifu, py-clob-client).

Three layers: (1) legal firewall — no dev reads both proprietary + OSS code; (2) functional spec from black-box observation only; (3) independent implementation with audit trail.

AI-assisted coding weakens traditional clean-room — generated code may embed training-data patterns. Cemini posture: **read OSS for API contracts only**; implement in `cemini/` with separate authors; document R11 as behavioral diff not line copy.

## Snippets

> Clean-room success requires provable separation between those who understand the problem and those who have seen the reference implementation. [Source: Clean-Room Design for Proprietary Software.docx — paraphrase]
