---
title: "Gemini Deep Research — Wave 4A: Cemini Stack & Wiki Stack Link Evaluation (30 URLs, 2026-04-29)"
type: source
tags: [docx, librarian-tooling, link-evaluation, decision-record, gemini-dr-wave4, cemini-internal, mcp-servers, trading-tools, license-evaluation]
keywords: [gemini-dr-wave4a, link-evaluation, claudectl, crewai, context7, mem0, last30days-skill, mcp-etherscan, dune-analytics-mcp, polymarket-predictions-mcp, tradingview-mcp, mcp-server-ccxt, vibe-trading-status-change, polymarket-trade-engine, ai-hedge-fund, openbb-reject, kronos, microsoft-qlib, anti-hallucination-spot-check, tos-conflict-pattern, low-maturity-adopt-caveat]
clusters: [librarian-tooling, link-evaluation, decision-record]
related:
  - sources/gemini-dr-link-eval-2026-04-28.md
  - sources/gemini-dr-wave3-link-eval-2026-04-28.md
  - sources/gemini-dr-wave4b-osint-2026-04-29.md
  - sources/gemini-dr-wave5a-cemini-stack-2026-04-30.md
  - sources/shiyu-coder-kronos.md
  - sources/vibe-trading-hkuds.md
  - sources/atomicmemory-llm-wiki-compiler.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/ip-sale-readiness.md
  - concepts/high-signal-paper-patterns.md
  - sources/polymarket-informed-minority-gomezcram-2026.md
  - entities/platforms/polymarket.md
  - concepts/quant-finance.md
  - sources/microsoft-qlib.md
  - sources/dune-analytics-mcp.md
  - sources/polymarket-predictions-mcp.md
  - sources/vibe-trading-hkuds.md
  - sources/atomicmemory-llm-wiki-compiler.md
  - sources/mercurialsolo-claudectl.md
  - sources/upstash-context7.md
  - sources/last30days-skill-mvanhorn.md
  - sources/tradesdontlie-tradingview-mcp.md
  - sources/gemini-dr-wave5b-osint-2026-04-30.md
maturity: validated
read_status: read
created: 2026-04-29
updated: 2026-04-30
---

## Relations

- @sources/gemini-dr-link-eval-2026-04-28.md — Wave 2 (24 URLs) parent of the Gemini DR link-evaluation lineage
- @sources/gemini-dr-wave3-link-eval-2026-04-28.md — Wave 3 (13 URLs) sibling
- @sources/gemini-dr-wave4b-osint-2026-04-29.md — Wave 4B sibling docx (18 URLs OSINT/satellite focus); the "another Link Evaluation" docx of the same date
- @sources/vibe-trading-hkuds.md — URL 22; **status change** Wave 2 Adopt-Cemini → Wave 4 Steal-from (additional context on cross-wave reclassification)
- @sources/atomicmemory-llm-wiki-compiler.md — appears as URL 2 in Wave 4B (reaffirmed Adopt for librarian); not in this 4A brief but relevant cross-wave
- @concepts/wiki-tooling-evaluation.md — wave-evaluation parent for librarian-side findings
- @concepts/ip-sale-readiness.md — license analysis parent; **new finding**: tradingview-mcp surfaces a TOS-conflict-with-automated-trading-via-Chrome-DevTools-Protocol pattern that's adjacent to but distinct from poison-pill family A/B
- @concepts/high-signal-paper-patterns.md — rubric used to score the Adopts; informs which to promote to dedicated source pages
- @sources/polymarket-informed-minority-gomezcram-2026.md — URL 19 polymarket-predictions-mcp pairs operationally with this paper (deployment surface for the "informed-flow analyst" service)
- @entities/platforms/polymarket.md — multiple URLs reference Polymarket (URL 19 mcp + URL 24 trade-engine)

## Raw Concept

- **Original title**: "Cemini Stack & Wiki Stack — Link Evaluation Brief"
- **Source filename**: `4_29 Link Evaluation Brief.docx`
- **Type**: User-authored Gemini Deep Research output (docx, 3.1 MB, 473 paragraphs, 69k characters)
- **Date**: Modified 2026-04-30 (UTC; author dropped 2026-04-29 EDT)
- **URL count**: 30 evaluations
- **Evaluation framework**: 8-section per-URL template (Identity / What it is / Scoring table / Detailed evaluation / Recommendation tier / Risks & caveats / Open questions / Primary sources cited) — same as Wave 2 / Wave 3
- **Evaluation surfaces**: Cemini production stack / Wiki/librarian server stack / Workflow
- **Location after ingest**: cemini-librarian:/opt/cemini-bulk/research/4_29 Link Evaluation Brief.docx
- **Read status**: read (full text extracted to /tmp; URL catalog + recommendation tier per URL captured; Adopt URLs anti-hallucination-spot-checked via Exa)
- **Discovered via**: User manual drop in inbox 2026-04-29 alongside Wave 4B sibling
- **Primary clusters**: librarian-tooling, link-evaluation, decision-record

## Narrative

### Recommendation distribution (30 URLs)

| Tier | Count | URLs |
|---|---|---|
| **Adopt** | 7 | claudectl (9), context7 (14), last30days-skill (16), dune-analytics-mcp (18), polymarket-predictions-mcp (19), tradingview-mcp (20) ⚠️ TOS, qlib (28) |
| **Steal-from** | 7 | crewAI (11), mem0 (15), mcp-etherscan-server (17), mcp-server-ccxt (21), Vibe-Trading (22) [status-change], polymarket-trade-engine (24), ai-hedge-fund (25) |
| **Reference** | 3 | Jon-Becker (5), awesome-claude-code (12), binance-skills-hub (23) |
| **Defer** | 1 | Kronos (27) |
| **Reject** | 3 | quran-database (3), withraven.ai (6), OpenBB (26) |
| **Unavailable** | 8 | autogen (1), nevercast.app (2), api-reviews-by-stripe.vercel.app (4), headroo (7), huggingscience.co (8), conducty (10), claude-mem (13), andrej-karpathy-skills (29), awesome-claude-plugins (30) |
| total | 30 | |

Adopt rate: 7/22 evaluable = **32%** (excluding the 8 Unavailable). Higher than Wave 2 (~22%) and Wave 3 (~13%). The wave heavily favored MCP servers + skills + Cemini-domain-fit tools.

### Anti-hallucination spot-check (Adopts)

Per the Wave 2/Wave 3 protocol, the 5 most Cemini-deployment-relevant Adopts were verified via Exa `web_search_exa` against GitHub primary URLs. Findings:

| URL | Verdict pre-spot-check | Spot-check result |
|---|---|---|
| URL 9 — claudectl | Adopt (Workflow) | License MIT ✅; Rust binary; LOCAL deploy only (laptop). Workflow-only Adopt. |
| URL 14 — context7 (upstash) | Adopt | License MIT ✅; **53,681 stars**; 67 releases; very active; ctx7@0.4.0 latest 2026-04-24. Strongest Adopt by maturity signals. |
| URL 18 — dune-analytics-mcp (kukapay) | Adopt | License MIT ✅; 40 stars / 11 forks; 2 contributors; Python; created 2025-03-16; last push 2025-05-04. **Small project**; functional but bus-factor concern. |
| URL 19 — polymarket-predictions-mcp (kukapay) | Adopt | License MIT ✅; **3 stars / 2 forks / 1 contributor**; created AND last-pushed same day 2025-09-23. **Single-day-development repo**. ⚠️ Severe maturity caveat. |
| URL 20 — tradingview-mcp (tradesdontlie) | Adopt | LICENSE file MIT but GitHub aggregator shows "NOASSERTION" 🚨; 2,362 stars; uses Chrome DevTools Protocol against TradingView Desktop; **README explicitly warns "Performing automated trading or algorithmic decision-making using extracted data" may violate TradingView TOS**. **Material finding: should be Defer or Steal-from for Cemini's automated-trading use case, not Adopt**. |
| URL 28 — qlib (Microsoft) | Adopt | License MIT ✅; **40,300 stars**; v0.9.7 latest Aug 2025; 23 releases; very active; Python. Microsoft-maintained; clean adoption candidate. Strongest Cemini-stack Adopt. |

**Two material findings beyond drift**:
1. **tradingview-mcp TOS-conflict pattern** — Gemini DR's recommendation didn't account for the project's own README warning about TradingView TOS conflict. For Cemini's automated-algorithmic-trading use case, this is a direct liability. **Reclassification: Defer (until TradingView TOS legal review) or Steal-from (extract the Chrome DevTools Protocol pattern only, route through a different data source)**. New IP-sale-readiness pattern: **TOS-conflict-via-data-redistribution** — adjacent to poison-pill family A (copyleft) and family B (vendor-IP-redistribution) but distinct: the LICENSE is clean, the TOS isn't.
2. **polymarket-predictions-mcp single-day-dev** — 3 stars and a single push date is the bus-factor signal the rubric's negative-signals warn about. Adopt verdict can stand IF Cemini is willing to fork-and-maintain rather than rely on upstream. Otherwise reclassify.

### Pre-existing wiki integration

Two URLs evaluated in this wave already have source pages:
- **URL 22 — HKUDS/Vibe-Trading**: Wave 2 ingested as **Adopt-Cemini**. Wave 4 reclassifies as **Steal-from**. Status change reflects deeper analysis on production-readiness gaps. Source page `@sources/vibe-trading-hkuds.md` will be updated with this Wave 4 reassessment (added below).

(URL 2 in Wave 4B — atomicmemory/llm-wiki-compiler — was a Wave 2 Reference; Wave 4B reaffirms Adopt for the librarian server.)

### Per-URL summaries — Adopts (full deep-read targets)

**URL 9: claudectl** (`github.com/mercurialsolo/claudectl`) — MIT, Rust
> Lightweight zero-config Rust binary serving as "mission control" for Claude Code. Manages multiple concurrent agent sessions via SQLite. Local LLM auto-pilot (Ollama, llama.cpp, vLLM) approves safe ops + blocks dangerous ones (force pushes) without cloud API calls. File ownership leases prevent agent collision. **Recommendation: Adopt for Workflow only** (laptop, not librarian/prod). Pairs with the existing `@sources/claude-code-harness-chachamaru.md` (similar guardrail family).

**URL 14: context7 (upstash)** (`github.com/upstash/context7`) — MIT, TypeScript, **53k stars**
> Up-to-date code documentation platform for LLMs and AI code editors. CLI + Skills mode (no MCP) OR MCP server registration. Resolves library names → library IDs → fetches docs. Solves "LLM hallucinates API surface that's been deprecated" failure mode. Highest-maturity Adopt in the wave. **Recommendation: Adopt** for any Cemini development context where DeepSeek-V4-flash is generating code against rapidly-evolving libraries.

**URL 16: last30days-skill** (`github.com/mvanhorn/last30days-skill`) — License pending verification
> Claude Code skill for "what changed in the last 30 days?" workflow. Adopt for Workflow.

**URL 18: dune-analytics-mcp** (`github.com/kukapay/dune-analytics-mcp`) — MIT, Python
> MCP server bridging Dune Analytics (on-chain data) to AI agents. Cemini's crypto pipeline currently consults Coinbase + Polygon for OHLC/trades; Dune is the **on-chain analytics layer** (smart contract events, wallet flows, DeFi metrics). MCP integration means DeepSeek can query Dune directly via tool calls. **40 stars, 2 contributors** — small but functional. Pre-Cemini-deployment: license check + clone+pin pattern (don't rely on upstream maintenance). **Promoted to dedicated source page this session.**

**URL 19: polymarket-predictions-mcp** (`github.com/kukapay/polymarket-predictions-mcp`) — MIT, Python, **3 stars** ⚠️
> MCP server delivering real-time Polymarket odds. **Pairs with `@sources/polymarket-informed-minority-gomezcram-2026.md`**: that paper proposed a "Polymarket informed-flow analyst" service for Cemini; this MCP is exactly the data-access layer that service needs. Bus-factor caveat: 3 stars / 1 contributor / single-day-development. Adoption requires fork + maintain in-house, OR reimplementation. **Promoted to dedicated source page this session.**

**URL 20: tradingview-mcp** (`github.com/tradesdontlie/tradingview-mcp`) — MIT (file-level) / NOASSERTION (GitHub aggregator), 2.4k stars 🚨
> Chrome DevTools Protocol bridge to TradingView Desktop app. AI-assisted chart analysis. **The README itself warns "Performing automated trading or algorithmic decision-making using extracted data" may violate TradingView TOS.** For Cemini's algorithmic-trading use case, this is a direct conflict. **Reclassified Adopt → Defer (TOS legal review) or Steal-from (Chrome DevTools Protocol pattern, different data source).** Material finding to be promoted to `@concepts/ip-sale-readiness.md` as a new pattern.

**URL 28: microsoft/qlib** (`github.com/microsoft/qlib`) — MIT, Python, **40.3k stars**
> Microsoft's AI-oriented quantitative investment platform. Supervised learning + market-dynamics modeling + RL paradigms. Now equipped with R&D-Agent for automated quant R&D. Latest v0.9.7 Aug 2025; 23 releases. Strongest Cemini-stack Adopt by maturity + scope. Direct fit for Cemini's RL-MARL retraining pipelines. **Promoted to dedicated source page this session.**

### Per-URL summaries — Steal-from

**URL 11: crewAI** (`github.com/crewAIInc/crewAI`) — MIT
> Multi-agent collaboration framework. Steal-from pattern: their role-task-process abstractions inform analyst-orchestrator design.

**URL 15: mem0** (`github.com/mem0ai/mem0`) — Apache-2.0
> Long-term memory for LLM agents. Pairs with `@concepts/context-compression-resume-pattern.md` (cpr-pattern); Steal-from informs the cpr Compress phase architecture.

**URL 17: mcp-etherscan-server** (`github.com/crazyrabbitLTC/mcp-etherscan-server`) — License pending
> Etherscan MCP for Ethereum chain data. Pattern only; Cemini may build its own Etherscan-MCP later.

**URL 21: mcp-server-ccxt** (`github.com/doggybee/mcp-server-ccxt`) — License pending
> CCXT (CryptoCurrency eXchange Trading) library wrapped as MCP server. Cemini already integrates CCXT directly via Python; this MCP wrapping adds LLM-tool-call accessibility but at cost of extra layer. Steal-from the wrapper pattern if needed.

**URL 22: HKUDS/Vibe-Trading** — already in wiki at `@sources/vibe-trading-hkuds.md`, **status change** Adopt-Cemini → Steal-from.

**URL 24: polymarket-trade-engine** (`github.com/KaustubhPatange/polymarket-trade-engine`) — License pending
> Polymarket trading engine reference impl. Pattern adjacent to URL 19 MCP server.

**URL 25: ai-hedge-fund** (`github.com/virattt/ai-hedge-fund`) — License pending
> AI-driven hedge fund simulation. Likely educational, not deployable; Steal-from pattern only.

### Per-URL summaries — Reference (3)

- **URL 5: Jon-Becker** — Coinbase senior engineer's GitHub profile. Reference for the trading-systems-engineer hiring/network signal.
- **URL 12: awesome-claude-code** — Curated awesome-list. Reference / browse-only.
- **URL 23: binance-skills-hub** — Binance-ecosystem skills. Reference for Cemini's potential Binance integration path.

### Per-URL summaries — Defer (1)

- **URL 27: Kronos** (`github.com/shiyu-coder/Kronos`) — Time-series foundation model. Defer pending peer-reviewed evaluation; potential future Cemini brain swap candidate alongside Sakana Fugu. **STATUS-CHANGE 2026-04-30**: Wave 5A re-evaluated as **Steal-from** — AAAI 2026 acceptance (Nov 2025) + 22k stars + 20 contributors + MIT confirmed at file + repo level. See `@sources/shiyu-coder-kronos.md` and `@sources/gemini-dr-wave5a-cemini-stack-2026-04-30.md` for full status-upgrade rationale. The "Steal-from-the-tokenizer-not-the-model" pattern applies — extract KronosTokenizer; reject KronosPredictor for production trading.

### Per-URL summaries — Reject (3)

- **URL 3: quran-database** — Domain mismatch (theological). Filter 3 fail.
- **URL 6: withraven.ai** — Closed-source, no API; Filter 1 fail.
- **URL 26: OpenBB** (`github.com/OpenBB-finance/OpenBB`) — License: AGPL-3.0 (the brief flagged this). **Poison-pill family A** per `@concepts/ip-sale-readiness.md`. Reject.

### Cross-wave patterns

1. **Vibe-Trading reclassification**: Wave 2's Adopt-Cemini becomes Wave 4's Steal-from. The downgrade reflects deeper analysis on the bloated React frontend and yfinance-fallback issues that the Wave 2 ingest already noted but didn't gate on. Worth treating as a **Wave-4-as-postmortem** signal — the wiki's prior Adopt verdicts deserve re-review when richer evaluations appear.

2. **MCP server proliferation**: 6 of the 7 Adopts are MCP servers or MCP-compatible (claudectl Workflow exception). The MCP-as-deployment-surface pattern is established for Cemini's stack. New concept candidate: `concepts/mcp-tool-marketplace.md` synthesizing the MCP-server adoption pattern across waves.

3. **Bus-factor caveats** (polymarket-predictions-mcp 3 stars, dune-analytics-mcp 40 stars) suggest a **fork-and-maintain pattern** for small MCP servers — clone, pin a commit hash, accept that upstream may go stale. Different from "Adopt the upstream and follow it" pattern which works for Microsoft qlib (40k stars, 23 releases).

4. **TOS-conflict-via-data-redistribution** (tradingview-mcp) is a new IP-sale-readiness pattern. **Distinct from poison-pill family A (copyleft) and family B (vendor-IP-redistribution-without-authorization)**: the LICENSE is clean MIT, the third-party-data-provider's TOS isn't. Captured as a new section in `@concepts/ip-sale-readiness.md`.

### Open questions / NEEDS VERIFICATION

- **URL 16 last30days-skill license** [NEEDS VERIFICATION 2026-04-29] — license not confirmed via Exa in this session. Pre-adoption gate: verify LICENSE file at `github.com/mvanhorn/last30days-skill/blob/main/LICENSE`.
- **URL 17 mcp-etherscan-server license** [NEEDS VERIFICATION 2026-04-29] — same pre-adoption gate.
- **URL 21 mcp-server-ccxt license** [NEEDS VERIFICATION 2026-04-29] — same pre-adoption gate.
- **URL 24 polymarket-trade-engine license** [NEEDS VERIFICATION 2026-04-29] — same pre-adoption gate.
- **URL 25 ai-hedge-fund license** [NEEDS VERIFICATION 2026-04-29] — same pre-adoption gate.
- **URL 20 tradingview-mcp TOS legal review** [NEEDS VERIFICATION 2026-04-29] — formal legal review of TradingView TOS vs Cemini's automated-trading use case. Currently downgraded to Defer pending review.

## Snippets

> **The wave's headline finding (paraphrased)**: 7 Adopts out of 30 URLs (32% of evaluable), heavily concentrated in MCP servers + Microsoft-maintained projects + Claude Code workflow tooling. Anti-hallucination spot-check surfaced 2 material findings: tradingview-mcp's TOS conflict and polymarket-predictions-mcp's single-day-development bus-factor risk. Both override Gemini DR's recommendation tier.

> **Vibe-Trading status change (URL 22 evaluation excerpt)**:
>
> "Steal-from. While the agentic architecture is impressive, the bloated React frontend (13.1% TS/JS) is a non-starter for Cemini's headless deployment, and the yfinance-fallback data layer creates production-grade reliability risk under the polygon_not_authorized_doctrine. Extract the agent-swarm topology + MCP-tool-decorator pattern; do not deploy the project as-is." [Source: 4_29 Link Evaluation Brief.docx URL 22]

> **claudectl integration vector (URL 9 evaluation excerpt)**:
>
> "The compiled Rust binary would be installed globally on the macOS laptop via Homebrew to wrap existing Claude Code sessions utilized during the 'read paper -> discuss with LLM -> curate wiki' pipeline. By tapping into the local Ollama instance—which is already mapped for semantic embeddings—the auto-pilot module could securely authorize Claude Code to autonomously read Obsidian markdown files and execute wiki_lint.py scripts." [Source: 4_29 Link Evaluation Brief.docx URL 9]

> **qlib integration vector (URL 28 evaluation excerpt)**:
>
> "qlib provides a comprehensive AI-oriented quantitative investment platform supporting supervised learning, market dynamics modeling, and reinforcement learning paradigms. Direct integration target: Cemini's RL-MARL retraining pipeline. The platform's R&D-Agent integration automates the model R&D process — directly applicable to Cemini's MAPPO retrain windows." [Source: 4_29 Link Evaluation Brief.docx URL 28]

> **Anti-hallucination protocol — anchoring quote**:
>
> 5 of 7 Adopt URLs verified via `mcp__exa__web_search_exa`. License MIT confirmed for: claudectl (file-level), context7 (file-level), dune-analytics-mcp (file-level + repo-level), polymarket-predictions-mcp (file-level + repo-level), qlib (file-level + repo-level). License DISPUTE for: tradingview-mcp (file-level MIT, GitHub aggregator NOASSERTION). Star counts: claudectl-not-checked, context7=53,681, dune-analytics-mcp=40, polymarket-predictions-mcp=3, tradingview-mcp=2,362, qlib=40,300. [Per Exa spot-check 2026-04-29]
