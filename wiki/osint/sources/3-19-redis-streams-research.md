---
title: Architectural Transition from Ephemeral Messaging to Durable Event Streams in HFT Platforms
type: source
tags: [docx, cemini-internal, infrastructure, redis-streams, redis-pubsub, event-sourcing, durable-messaging, architecture, audit]
clusters: [rl-marl, quant-finance, crypto, prediction-markets, cemini-internal, infrastructure]
related:
  - concepts/rl-marl-research.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26
---

## Relations

- @concepts/rl-marl-research.md — cluster hub for RL/MARL research in the Cemini corpus

## Raw Concept

- **Original title**: Architectural Transition from Ephemeral Messaging to Durable Event Streams in High-Frequency Algorithmic Trading Platforms (subtitle: "and Institutional IP Valuation Analysis")
- **Author(s)**: Unspecified — Cemini-internal research
- **Type**: DOCX
- **Location**: research for cemini/3_19 Redis Streams research.docx
- **Retrieved**: 2026-04-23
- **Read status**: read-skim (DOCX body not re-extracted)
- **Primary cluster**: infrastructure
- **All clusters**: rl-marl, quant-finance, crypto, prediction-markets, cemini-internal, infrastructure

## Narrative

Cemini-internal research on migrating the internal message bus from Redis Pub/Sub to Redis Streams. Preview describes this as a "critical maturation point" for a proprietary financial suite operating across equities, crypto, and (implied) prediction markets. The concrete claim: Pub/Sub is ephemeral (messages disappear if no subscriber is listening), Streams are durable (messages persist with consumer-group semantics and replay). For a trading platform, ephemeral messaging is the root cause of the "execution state amnesia" failure mode called out in 3-10-live-trading-research.

Honest assessment: this is a genuinely substantive architectural topic with a clear correct answer — Redis Streams is the appropriate choice for an algo trading internal bus, and Pub/Sub is not. The "HFT" framing in the title is slightly inflated (Cemini is not HFT by latency standards), but the durability argument applies at any frequency. The IP-valuation subtitle is the usual Cemini-internal marketing overlay; the architectural content is sound regardless.

Relevance: high. Forms a tight triangle with 3-17-git-research (which observes v12.3 uses pub/sub) and 3-10-live-trading-research (which says volatile-state → duplicate orders). This document is the recommended fix.

## Key findings

- Subject: migration from Redis Pub/Sub → Redis Streams for the internal message bus.
- Pub/Sub = ephemeral (messages lost if no consumer); Streams = durable with replay and consumer groups.
- Directly addresses the "execution state amnesia" failure mode identified in 3-10-live-trading-research.
- Closes the loop: 3-17 observes pub/sub in v12.3; 3-10 identifies it as a failure mode; this document prescribes the fix.
- "HFT" title framing is inflated — the durability argument holds at any trading frequency.

## Snippets

- **preview** — "The architectural migration of an algorithmic trading platform's internal message bus from a Redis Publish/Subscribe (Pub/Sub) model to a Redis Streams infrastructure represents a critical maturation point in the system's lifecycle. For a proprietary financial suite operating across diverse asset classes—including equi[...]" — States the migration scope.
