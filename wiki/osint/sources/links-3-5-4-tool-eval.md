---
title: "links 3 5_4 — Cemini Stack & Wiki Stack Eval (24 tools, Polymarket-heavy)"
type: source
tags: [llm-agents, prediction-markets, polymarket, market-making, algorithmic-trading, license-compliance, cemini-internal]
keywords: [tool-evaluation, gemini-deep-research, polymarket-agents, poly-market-maker, polybot, polymarket-trading-bot, claude-code-obsidian-graphify, context-mode-elv2]
related:
  - sources/5-5-links-tool-eval.md
  - sources/5-5-links-2-tool-eval.md
  - sources/polymarket-5-5-tool-eval.md
  - sources/5-4-links-tool-eval.md
  - sources/links-2-5-4-tool-eval.md
  - concepts/cemini-license-posture.md
  - entities/platforms/polymarket.md
  - entities/tools/polymarket-agents.md
maturity: draft
read_status: deep-read
created: 2026-05-05
updated: 2026-05-05
---

## Relations

- @sources/5-5-links-tool-eval.md, @sources/5-5-links-2-tool-eval.md, @sources/polymarket-5-5-tool-eval.md — companion 2026-05-04 / 2026-05-05 Gemini DR eval batches
- @entities/platforms/polymarket.md — primary venue affected by this batch
- @entities/tools/polymarket-agents.md — Adopt-tier carry-forward; Polymarket's official sanctioned developer framework
- @concepts/cemini-license-posture.md — adds **Elastic License v2 (ELv2)** as a license to scrutinize (URL 3 Context Mode)

## Raw Concept

- Original title: "Link Evaluation Brief: Cemini Stack & Wiki Stack" (Gemini Deep Research output)
- Author: Gemini Deep Research
- Type: docx — Cemini-internal architecture evaluation
- Location: cemini-librarian:/opt/cemini-bulk/research/links 3 5_4.docx
- Retrieved: 2026-05-04
- Length: ~74 KB, 24 candidates evaluated
- Read status: deep-read

## Narrative

Heavy Polymarket-market-making focus. Five different MM implementations (poly-market-maker, poly-maker, polymarket-market-maker, Polymarket Trading Bot v3.1, Polymarket-BTC-15-Minute-Trading-Bot) — all Steal-from-tier — give a panoramic view of Polymarket's automated-MM ecosystem.

**Recommendation distribution:**

| Tier | Count | Notable |
|------|-------|---------|
| **Adopt** | 2 | URL 4 Claude Code + Obsidian + Graphify (MIT — Claude-Code persistent-memory pattern via Obsidian vault), URL 18 Polymarket Agents (MIT — official sanctioned framework) |
| **Steal-from** | 7 | 5 Polymarket MM/trading bots, plus URL 3 Context Mode (ELv2!), URL 17 Polymarket-Kalshi BTC Arbitrage (cross-doc duplicate w/ 5_5 links 2 URL 8) |
| **Defer** | 1 | License or maturity gate |
| **Reference-only** | 4 | Documentation / educational |
| **Reject** | 5 | License or stack mismatch |
| **Unavailable** | 5 | URL retrieval failed |

### Critical findings

#### 1. Polymarket Agents (URL 18) — official-framework Adopt

> "Officially sanctioned developer framework and comprehensive utility suite constructed to empower users to build and deploy autonomous AI." [Source: links 3 5_4.docx URL 18]

This is the **canonical Polymarket Adopt** for Cemini's eventual Polymarket integration. MIT-licensed, official-sanctioned (rare combo for prediction-market platforms). Pairs with the K30 Polymarket 5_5 batch's URL 5 (`python-order-utils`) + URL 19 (`polymarket-mcp-server`) to form a coherent integration stack.

#### 2. Five Polymarket MM implementations — runtime architecture comparison

| URL | Project | Distinguishing trait |
|-----|---------|----------------------|
| URL 11 | poly-market-maker | "AMM 'keeper' for Polymarket CLOB" — minimal automated-keeper pattern |
| URL 12 | poly-maker | "Comprehensive automated market-making solution" — full two-sided liquidity |
| URL 14 | polymarket-market-maker | "Risk-aware MM infrastructure" — explicitly risk-controls-first |
| URL 19 | Polymarket Trading Bot v3.1 - Enhanced Risk Management | TypeScript, four strategies bundled (Arbitrage, DipArb, Smart Money copy, ...) |
| URL 20 | Polymarket-BTC-15-Minute-Trading-Bot | Specific high-frequency niche on BTC 15-min markets |

All MIT. Cemini's eventual Polymarket MM strategy can pick one of these as a starting reference and lift the risk-control + order-keeping patterns. **No single one is wholesale-adopt** — they're complementary references for different angles.

#### 3. URL 3 Context Mode — Elastic License v2 (new license to scrutinize)

> "License: ELv2 (Elastic License v2)." [Source: links 3 5_4.docx URL 3]

ELv2 is a non-permissive source-available license. Imposes use restrictions (cannot host as a service, cannot circumvent license checks). For Cemini's IP-sale readiness, ELv2 is a **9th license-pattern** to add to the catalog: source-available with use-restrictions. Treat as Defer/Reject for any production integration; OK as architectural-reference reading.

Update `@concepts/cemini-license-posture.md` to include ELv2 in the catalog.

#### 4. Claude Code + Obsidian + Graphify (URL 4) — persistent-memory Adopt

> "Configuration pipeline designed to furnish Claude Code with persistent, long-term memory utilizing an Obsidian vault." [Source: links 3 5_4.docx URL 4]

Adjacent to:
- `@sources/agriciDaniel-claude-obsidian.md` (Wave 5B claude-obsidian Adopt)
- K28's `coleam00/claude-memory-compiler` (Defer due to NO LICENSE)
- This batch's claude-OSINT (5_5 links URL 6)

Cemini's existing Claude Code config already uses memory files at `~/.claude/projects/.../memory/`. Whether this Obsidian-Graphify setup adds value beyond what's deployed is the Phase-0 question. Probably already-covered by `@sources/agriciDaniel-claude-obsidian.md`.

#### 5. Cross-doc duplicate (Polymarket-Kalshi BTC Arbitrage Bot)

URL 17 of this docx = URL 8 of 5_5 links 2.docx. **Cross-doc duplicates are high-signal** (per K8/K9 discipline). Two independent evals reach Steal-from verdict for this arbitrage scanner — pattern is the load-bearing extract.

### Architectural patterns worth extracting

- **Polymarket Agents wholesale adoption** for Polymarket integration foundation
- **Risk-aware MM scaffolding** (polymarket-market-maker) → defines structure for Cemini's eventual Polymarket MM
- **Cross-venue arbitrage scanner** (BTC arb, cross-doc duplicate) → reference architecture
- **Persistent-memory Obsidian-Graphify** → compare against existing Cemini config; likely no-op
- **Context Mode** (ELv2 — read-only) → token-efficiency patterns; do NOT integrate

## Snippets

- **Polymarket Agents official-framework framing** (URL 18): "Officially sanctioned developer framework and comprehensive utility suite constructed to empower users to build and deploy autonomous AI." [Source: links 3 5_4.docx URL 18]

- **ELv2 license caveat** (URL 3): "License: ELv2 (Elastic License v2)" — source-available with use-restrictions (no SaaS hosting, no license-check circumvention). [Source: links 3 5_4.docx URL 3]

- **Cross-doc duplicate signal** (URL 17 = 5_5 links 2.docx URL 8): real-time BTC arbitrage scanner; second independent Steal-from verdict.

## Dead Ends

*(none yet — first ingest of this source.)*
