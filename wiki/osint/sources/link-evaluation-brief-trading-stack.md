---
title: "K38 — Link Evaluation Brief for Trading Stack (29-URL Three-Surface Batch)"
type: source
tags: [source, evaluation-brief, tooling, three-surface-fit, trading, prediction-markets, agents, mcp, k38]
keywords: [URL eval, trading stack, MCP servers, agent skills, weather prediction markets, kalshi, polymarket, telegram osint, license audit]
related:
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - concepts/mcp-tool-marketplace.md
  - entities/tools/notoriouslab-vault-search.md
  - entities/tools/google-research-monorepo.md
  - entities/tools/readme-skill.md
  - entities/tools/agent-skills-eval.md
  - entities/tools/tokenspeed.md
  - entities/tools/ai-ml-roadmap.md
  - entities/tools/perplexity-mcp.md
  - entities/tools/medusa-pantheon.md
  - entities/tools/cloddsbot.md
  - entities/tools/ai-trader-hkuds.md
  - entities/tools/tropicaltidbits.md
  - entities/tools/climatereanalyzer.md
  - entities/tools/windy-com.md
  - entities/tools/google-colab-vscode.md
  - entities/tools/9router.md
  - entities/tools/megamemory.md
  - entities/tools/guild-mcp.md
  - entities/tools/opencode-ai.md
  - entities/tools/d3ext-wef.md
  - entities/tools/hackers-arise-telegram.md
  - entities/tools/metatron-recon.md
  - entities/tools/liquid4all-cookbook.md
  - entities/tools/ssh-keys-manager-stmol.md
  - entities/tools/wethr-net.md
  - entities/tools/bettingonweather.md
maturity: validated
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@concepts/tool-evaluation-framework.md` — three-surface methodology
- `@concepts/cemini-license-posture.md` — IP-sale-readiness license clean-list enforcement
- `@concepts/mcp-tool-marketplace.md` — many URLs are MCP-native or MCP-adjacent

## Raw Concept

- **Title**: Cemini Stack & Wiki Stack — Link Evaluation Brief
- **Author**: User-prepared analyst memo (commissioned eval brief)
- **Type**: docx evaluation brief, 29 URLs scored on three-surface fit matrix
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/Link Evaluation Brief for Trading Stack.docx`
- **Retrieved**: 2026-05-11
- **sha256**: `84915db2356e3461…` (preingest verdict: NEW)
- **Pages**: 29 URLs scored — 4 UNAVAILABLE/unclear, 25 evaluated
- **Read-status**: deep-read

## Narrative

K38 batch — 29 URLs evaluated against the three-surface fit matrix. Heavy bias toward trading-stack + agent-tooling. Notable inclusion of 5 weather/prediction-market URLs (Polymarket/Kalshi-relevant) and 2 OSINT-tooling tutorials.

### Tier rollup

| Tier | Count | URLs |
|------|------:|------|
| **Adopt** | 6 | Readme.skill (URL 3), Perplexity MCP (URL 7), Google Colab VSCode ext (URL 14), 9router (URL 15), guild MCP (URL 18), wethr.net (URL 28) |
| **Steal-from** | 6 | google-research (URL 2), CloddsBot (URL 9), AI-Trader (URL 10), MegaMemory (URL 16), hackers-arise Telegram OSINT (URL 22), METATRON (URL 23) |
| **Reference-only** | 5 | vault-search (URL 1), AI-ML roadmap (URL 6), climatereanalyzer (URL 12), Liquid4All cookbook (URL 26), bettingonweather (URL 29) |
| **Defer** | 3 | agent-skills-eval (URL 4), windy.com (URL 13), opencode.ai (URL 19) |
| **Reject** | 5 | TokenSpeed (URL 5), Medusa Pantheon Security (URL 8), tropicaltidbits (URL 11), D3Ext/WEF (URL 21), ssh-keys-manager-stmol (URL 27) |
| **UNAVAILABLE / unclear** | 4 | URLs 17, 20, 24, 25 |

### Domain clustering

- **Weather / prediction markets** (URLs 11-13, 28-29): wethr.net is the singular Adopt — explicitly built for Kalshi/Polymarket weather probability modeling, programmable API. windy.com deferred on €990/yr subscription gate. bettingonweather is required strategy reading. tropicaltidbits rejected (copyright, no API). climatereanalyzer reference-only.
- **Trading bots** (URLs 9, 10): CloddsBot (Node.js, Anthropic + 8 providers, 4 agents, Solana DeFi + Hyperliquid) — Steal-from for multi-agent routing logic, risk-engine math, prediction-market integrations, MCP tool schemas. AI-Trader (FastAPI + React) — Steal-from for IBKR integration logic + background-worker isolation pattern.
- **Agent frameworks / skills** (URLs 3, 4): Readme.skill (Adopt — agent skill format for repo-stats auto-gen, fits workflow). agent-skills-eval (Defer — formal SKILL.md validator; valuable but priority infrastructure migration comes first).
- **MCP servers / proxies** (URLs 7, 15, 18): Perplexity MCP (Adopt — live web search gap closer, TypeScript service worth Docker-isolating). 9router (Adopt — token-compressing LLM proxy, claims ~65% token reduction, OpenAI-compatible drop-in). guild MCP (Adopt — Go binary, BM25 + int8 ONNX hybrid retrieval with Reciprocal-Rank Fusion, potential Ollama replacement on Hetzner CPX21).
- **Memory / context** (URL 16): MegaMemory — Steal-from for two-way merge engine (`src/merge.ts`) handling embedded knowledge across git branches, port to wiki_lint.py merge-conflict resolution.
- **Coding agents / tooling** (URLs 14, 17, 19): Google Colab VS Code ext (Adopt — local IDE + remote GPU). opencode.ai (Defer — alternative coding agent, requires migration off Claude Code).
- **Security / OSINT** (URLs 8, 21, 22, 23): Medusa rejected (AGPL-3.0). D3Ext/WEF rejected (Wi-Fi offensive, domain mismatch). hackers-arise Telegram OSINT tutorial — Steal-from for member enumeration + scraping patterns (TOS-violation risk noted). METATRON — Steal-from purely for `search.py` DuckDuckGo scraper (free real-time web context).
- **Educational / archival** (URLs 2, 6, 17, 26): google-research monorepo — Steal-from for specific feature-engineering + learning-rate tuning algorithms. LLMs-from-scratch / AI-ML roadmap / Liquid4All cookbook → reference-only.
- **Workflow tools** (URLs 1, 27): vault-search (Obsidian-tied, license missing, reference-only). ssh-keys-manager-stmol rejected (unverified GUI, sensitive-credential exposure, security anti-pattern).
- **Cross-domain reject**: TokenSpeed (URL 5) — GPU-only, --privileged Docker, fundamental hardware + security mismatch.

### Cross-wiki routing

No URLs in K38 are strong cross-wiki candidates. Weather/prediction-market URLs are Cemini-OSINT-specific. Trading bots are explicitly trading-stack. The 2 OSINT tutorials (Telegram, METATRON) are pure OSINT-wiki content. The MCP / agent / memory tools are all general infrastructure that **architecturally** could benefit other wikis but practically benefit only the OSINT librarian server.

### License posture warnings (gate before any Phase-0 audit promotion)

- **Medusa**: **AGPL-3.0** — hard reject per Cemini license clean-list (already filed)
- **TokenSpeed**: license + hardware gate, hard reject
- **vault-search**: license missing, reference-only stance is correct
- **Liquid4All cookbook**: license not located in brief, reference-only until verified
- **opencode.ai**: license ambiguity flagged — could be BSL/PolyForm masquerading as OSS; audit before deeper adoption
- **Readme.skill**: skill format only (no executable code), license risk low
- **MegaMemory**: license check pending — only `src/merge.ts` pattern to be lifted, low-risk
- **CloddsBot, AI-Trader, METATRON, hackers-arise tutorial**: license check pending — only patterns/algorithms to be lifted, low-risk

### Reading method

- 25 reachable URLs read in full
- 4 UNAVAILABLE (URLs 17, 20, 24, 25) flagged for Exa-resolution

[Source: Link Evaluation Brief for Trading Stack.docx, retrieved 2026-05-11]
