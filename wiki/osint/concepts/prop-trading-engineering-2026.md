---
title: Prop Trading Engineering 2026 — latency floor, AI differentiator, AI gateway + MCP
type: concept
tags: [concept, trading-eng, prop-trading, infra, k233]
keywords: [optiver, latency, ai-gateway, mcp-hosting, pg-feed, knight-capital]
related:
  - sources/newsletter-pragmatic-engineer-optiver-2026-08-11.md
  - concepts/agent-toolkit-routing-research-backlog.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
---

## Relations

- @sources/newsletter-pragmatic-engineer-optiver-2026-08-11.md
- @concepts/agent-toolkit-routing-research-backlog.md

## Raw Concept

What this page answers: how a modern prop trading firm (Optiver) organizes engineering when latency is the floor and AI models are the differentiator. From the Pragmatic Engineer 2026-08-11 deep-dive.

## Narrative

Key patterns: no external customers (the business is the customer); latency as "enemy #1" with custom FPGAs/hardware, but now **latency is the floor — AI models are the differentiator** ("slow models with a fast trigger, fast models at the network edge"); C++ for low-latency / Python for modeling / **Rust for research tooling + orchestration**; PG Feed (NOTIFY/LISTEN over Postgres WAL) for low-latency high-fanout messaging; AI platform shift with an **AI gateway** (model access) + **MCP hosting platform** (agents reach internal systems) — the closest public analog to Cemini's conductor + MCP tool layer. Knight Capital ($440M bug) as the structural risk-aversion driver.

[Source: Pragmatic Engineer 2026-08-11]
