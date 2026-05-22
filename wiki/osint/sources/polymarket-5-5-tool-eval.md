---
title: "Polymarket 5_5 — Cemini Stack & Wiki Stack Polymarket-Specific Eval (24 tools)"
type: source
tags: [llm-agents, prediction-markets, polymarket, mcp-server, clob, license-compliance, cemini-internal]
keywords: [tool-evaluation, gemini-deep-research, py-clob-client, python-order-utils, rs-clob-client, polymarket-mcp-server, poly-sdk, polymarket-copy-trading, polybot, octobot-prediction-market]
related:
  - sources/5-5-links-tool-eval.md
  - sources/5-5-links-2-tool-eval.md
  - sources/links-3-5-4-tool-eval.md
  - sources/caiovicentino-polymarket-mcp-server.md
  - concepts/cemini-license-posture.md
  - entities/platforms/polymarket.md
  - entities/tools/polymarket-agents.md
  - entities/tools/polymarket-python-order-utils.md
  - concepts/polymarket-market-making-architectures.md
  - sources/5-5-moarrr-tool-eval.md
  - sources/polymarket-microstructure-anatomy-2604.24366.md
  - sources/tool-eval-50urls-polymarket-kalshi-license-false-negative-2026-05-21.md
maturity: draft
read_status: deep-read
created: 2026-05-05
updated: 2026-05-11
---

## Relations

- @sources/5-5-links-tool-eval.md, @sources/5-5-links-2-tool-eval.md, @sources/links-3-5-4-tool-eval.md — companion Gemini DR eval batches
- @sources/caiovicentino-polymarket-mcp-server.md — earlier Wave 5 Adopt; this batch's URL 19 confirms Adopt-tier verdict
- @entities/platforms/polymarket.md — primary venue
- @entities/tools/polymarket-agents.md — Adopt-tier framework (cross-listed with `links 3 5_4.docx` URL 18)
- @entities/tools/polymarket-python-order-utils.md — Adopt-tier dependency for Polymarket trading
- @concepts/cemini-license-posture.md — applied; URL 16 OctoBot is GPL-3.0 Steal-from (clean-room only)

## Raw Concept

- Original title: "Cemini Stack & Wiki Stack — Link Evaluation Brief" (Gemini Deep Research output, Polymarket-focused)
- Author: Gemini Deep Research
- Type: docx — Cemini-internal architecture evaluation
- Location: cemini-librarian:/opt/cemini-bulk/research/Polymarket 5_5.docx
- Retrieved: 2026-05-05
- Length: ~67 KB, 24 candidates evaluated
- Read status: deep-read

## Narrative

Dedicated Polymarket-ecosystem eval. Goal: compile the canonical Polymarket integration stack from official + community libraries. The four 2026-05-05 / 2026-05-04 batches together (5_5 links + 5_5 links 2 + links 3 5_4 + this) constitute Cemini's **Polymarket-readiness research wave**.

**Recommendation distribution:**

| Tier | Count | Notable |
|------|-------|---------|
| **Adopt** | 2 | URL 5 python-order-utils (MIT — sign-orders dependency), URL 19 caiovicentino/polymarket-mcp-server (MIT — already in Cemini's MCP catalog from Wave 5 — re-confirmed) |
| **Steal-from** | 5 | URL 4 rs-clob-client (MIT — Rust async patterns), URL 10 poly-sdk (MIT — TypeScript abstraction), URL 16 OctoBot-Prediction-Market (GPL-3.0 — clean-room only), URL 17 polymarket-copy-trading-bot (MIT), URL 22 polybot (MIT — enterprise-grade) |
| **Defer** | 2 | License or maturity gating |
| **Reference-only** | 11 | Polymarket-internal: py-clob-client, polymarket-subgraph, clob-client, etc. (referenced for architecture, not direct-adopt) |
| **Reject** | 4 | License or stack mismatch |

### Critical findings

#### 1. The canonical Polymarket integration stack (Adopt-tier carry-forwards)

Combining this batch + `links 3 5_4.docx` Adopts:

| Component | Source | License | Role |
|-----------|--------|---------|------|
| **Polymarket Agents** | `links 3 5_4.docx` URL 18 | MIT | Official-sanctioned framework foundation |
| **python-order-utils** | This URL 5 | MIT | Order signing + cryptographic operations |
| **py-clob-client** (or rs-clob-client) | This URL 4 / Reference URL | MIT | CLOB API wrapping |
| **caiovicentino/polymarket-mcp-server** | This URL 19 | MIT | LLM-readable MCP bridge |

Together this is Cemini's **complete Polymarket stack**. All four are MIT-licensed and IP-sale-clean. Stage as a single Polymarket-readiness brief for prod-side execution.

#### 2. URL 19 polymarket-mcp-server — re-confirmation

> "Highly specialized Model Context Protocol (MCP) server engineered specifically to bridge the Polymarket ecosystem with Large Language Models." [Source: Polymarket 5_5.docx URL 19]

caiovicentino/polymarket-mcp-server was previously documented at `@sources/caiovicentino-polymarket-mcp-server.md` (Wave 5). This 2026-05-05 eval re-confirms the Adopt verdict. No change to existing wiki page; it remains the canonical Polymarket-MCP entity.

#### 3. URL 22 polybot — "enterprise-grade" Steal-from

> "Massive, enterprise-grade, open-source infrastructure suite engineered for Polymarket algorithmic trading and high-fidelity strategy reverse-engineering." [Source: Polymarket 5_5.docx URL 22]

MIT-licensed; Cemini-relevant pattern: high-fidelity strategy reverse-engineering. Lift the strategy-reversing patterns rather than wholesale adoption. Eval recommends "Ignore the J[ava]" parts.

#### 4. URL 16 OctoBot-Prediction-Market — GPL-3.0 (clean-room only)

> "Free, open-source algorithmic trading bot built on top of the generic OctoBot framework. License: GPL-3.0." [Source: Polymarket 5_5.docx URL 16]

GPL-3.0 = pattern #3 in the license catalog (LLM-agent derivative-work risk per K27). Read for architectural inspiration; do NOT feed source to coding agents writing into Cemini.

#### 5. URL 17 polymarket-copy-trading-bot — direct Cemini-relevant pattern

> "Automated Python-based tracking system designed specifically to monitor and replicate the positions of targeted, successful traders on Polymarket." [Source: Polymarket 5_5.docx URL 17]

Smart-money-following is one of Polymarket Trading Bot v3.1's four bundled strategies (per `@sources/links-3-5-4-tool-eval.md` URL 19). Multiple independent implementations of the pattern → high-confidence architectural pattern.

### Architectural patterns worth extracting

- **Polymarket integration stack** (Polymarket Agents + python-order-utils + py-clob-client + polymarket-mcp-server) → wholesale Adopt as a coherent suite
- **rs-clob-client Rust-async patterns** → reference for high-performance CLOB connection patterns (probably Python-equivalent in py-clob-client)
- **polybot enterprise scaffolding** → Steal-from for production-grade infrastructure layout
- **Smart-money-copy-trading** → Steal-from pattern, multi-source architectural confidence

### Cross-batch synthesis (Polymarket 5_5 + links 3 5_4)

These two batches together describe Cemini's complete Polymarket integration plan:
- **Polymarket Agents** (foundation)
- **python-order-utils + py-clob-client** (transport + crypto)
- **polymarket-mcp-server** (LLM bridge)
- **5 different MM implementations** (ref architectures)
- **Cross-venue arbitrage scanner** (Polymarket-Kalshi BTC arb)
- **Smart-money copy trading** (multi-source pattern)

Stage one comprehensive **Polymarket Stack Adoption brief** for the prod-side Claude session. Don't fragment across multiple briefs.

## Snippets

- **Adopt python-order-utils** (URL 5): "A standalone Python utility package designed strictly to generate and cryptographically sign orders for the Polymarket Exchange." [Source: Polymarket 5_5.docx URL 5]

- **Re-confirmed polymarket-mcp-server Adopt** (URL 19): "Highly specialized Model Context Protocol (MCP) server engineered specifically to bridge the Polymarket ecosystem with Large Language Models." [Source: Polymarket 5_5.docx URL 19]

- **rs-clob-client patterns** (URL 4): "Ergonomic, async-first Rust client for the Polymarket CLOB. It utilizes strongly typed request builders, dual authentication flows." [Source: Polymarket 5_5.docx URL 4]

- **Smart-money copy-trading pattern** (URL 17): "Automated Python-based tracking system designed specifically to monitor and replicate the positions of targeted, successful traders on Polymarket." [Source: Polymarket 5_5.docx URL 17]

## Dead Ends

*(none yet — first ingest of this source.)*
