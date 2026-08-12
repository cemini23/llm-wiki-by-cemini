---
title: "Pragmatic Engineer — Software Engineering at a Proprietary Trading Company (Optiver)"
type: source
tags: [newsletter, k233, trading-eng, ccc, infra]
keywords: [pragmatic-engineer, optiver, prop-trading, latency, ai-gateway, mcp, knight-capital]
related:
  - concepts/prop-trading-engineering-2026.md
  - concepts/agent-toolkit-routing-research-backlog.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
read_status: read
---

## Relations

- @concepts/prop-trading-engineering-2026.md
- @concepts/agent-toolkit-routing-research-backlog.md — AI gateway + MCP hosting platform pattern

## Raw Concept

| Field | Value |
|-------|--------|
| Title | "Software engineering at a proprietary trading company: Optiver" |
| URL | https://newsletter.pragmaticengineer.com/p/optiver |
| sha256 | `70ef6a369209c91ca85145363e4a15d7a248124177cf9d7477dec4097c132788` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/newsletter-rss-pragmatic-engineer-2026-08-11-software-engineering-at-a-proprietary-trading-co.md` |
| retrieved | 2026-08-12 |

## Narrative

Deep-dive on engineering at Optiver (Amsterdam HQ, ~950 engineers, 30–40% on platform). Key mental models for the trading industry:

- **No external customers** — the business is the customer; no external deadlines, personal motivation to improve is highly valued.
- **Latency is "enemy number one"** — nearly every major decision minimizes latency; Optiver manufactures its own hardware (custom FPGAs, AMD hardware partnership, dedicated fiber/wavelength leasing, colocation).
- **Latency is now the floor; AI models are the differentiator** — "slow models with a fast trigger sending signals to execute trades, and fast models running at the edge of the network making trade decisions realtime." Invest more in better models than in lowering latencies further.
- **Knight Capital cautionary tale** — a single HFT bug → $440M loss; risk-aversion is structural.
- **Three-layer stack**: C++ for low-latency, Python for modeling/prototyping/internal tooling, **Rust increasingly in research tooling + service orchestration** (not replacing C++).
- **PG Feed** — internal NOTIFY/LISTEN over Postgres WAL for high-fanout latency-sensitive messages (pricing/config data) instead of Kafka (avoids extra disk read/write latency).
- **Ultra-low-latency loop** — market-making paths memoized/precomputed and burned into FPGA/ASIC.

**AI platform shift** (most relevant to Cemini): the platform team is "beginning to reimagine itself as built for AI." Users are both humans and automated systems; goal is to decompose work into workstreams and orchestrate agents. Two projects launched this year:
- **AI gateway** — gives Optiver engineers access to models.
- **MCP hosting platform** — makes it easy for engineers to access internal systems/tools via agents.

Risk management: human oversight (traders tweak strategy parameters) + automated monitoring that checks apps output orders within expected parameters regardless of algorithm intent.

Route: **wiki-only** (no GuruWatcher price watches; no poker/Atto steal). The AI gateway + MCP-hosting pattern is the closest public-industry analog to Cemini's conductor + MCP tool layer → filed to `@concepts/agent-toolkit-routing-research-backlog.md` and CCC awareness.

[Source: Pragmatic Engineer 2026-08-11 (retrieved 2026-08-12)]
