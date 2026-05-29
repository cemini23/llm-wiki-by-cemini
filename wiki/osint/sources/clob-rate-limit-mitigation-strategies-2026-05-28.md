---
title: CLOB Rate Limit Mitigation — Backoff, Batching, WebSocket-First Architecture
type: source
tags: [source, execution, polymarket, kalshi, hyperliquid, rate-limits, k77]
keywords: [429, websocket, exponential-backoff, batch-orders, TCP_NODELAY, kalshi, polymarket]
related:
  - concepts/clob-rate-limit-mitigation-strategies.md
  - concepts/shadow-to-live-transition-engineering.md
  - entities/tools/discountifu-polymarket-trading-bot.md
maturity: draft
read_status: read
created: 2026-05-28
updated: 2026-05-28
---

## Relations

- @concepts/clob-rate-limit-mitigation-strategies.md
- @concepts/shadow-to-live-transition-engineering.md — 429 preflight
- @entities/tools/discountifu-polymarket-trading-bot.md — R11 WS diff

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Architectural Strategies for Mitigating API Rate Limits in CLOBs |
| Type | docx |
| Location | `cemini-librarian:/opt/cemini-bulk/research/CLOB Rate Limit Mitigation Strategies.docx` |
| Retrieved | 2026-05-28 |
| Read-status | deep-read |

## Narrative

Compares three mitigation strategies for HTTP 429 / venue throttling:

| Strategy | Use | Avoid for |
|----------|-----|-----------|
| Exponential backoff | IP-ban prevention, catastrophic fallback | Primary taker / cancel path — loses queue position → adverse selection |
| Order batching | MM quote refresh (Paradex 50× weight; HL partial) | Latency arb; Kalshi charges per-order in batch |
| **WebSocket-first** | Live order + book path | — |

Network tuning: **TCP_NODELAY**, QUICKACK, monitor TCP zero-window backpressure; disconnect + resync on stale buffer flood.

Venue notes: Polymarket advises backoff; Kalshi **read/write token buckets** (100 write/s base); Hyperliquid address + IP limits, 100 in-flight posts cap.

## Snippets

> "Exponential backoff cannot be utilized as a primary capacity management tool for latency-sensitive trading algorithms." [Source: CLOB Rate Limit Mitigation Strategies.docx]
