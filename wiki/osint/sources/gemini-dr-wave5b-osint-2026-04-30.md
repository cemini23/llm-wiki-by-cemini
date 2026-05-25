---
title: "Gemini Deep Research — Wave 5B: Cemini Stack & Wiki Stack Deep Integration Evaluation (18 URLs incl. Polymarket cluster, 2026-04-30)"
type: source
tags: [docx, librarian-tooling, link-evaluation, decision-record, gemini-dr-wave5, cemini-internal, mcp-servers, polymarket-cluster, license-evaluation, prompt-extraction]
keywords: [gemini-dr-wave5b, link-evaluation, claude-obsidian, agency-agents, claude-code-system-prompts, system_prompts_leaks, openagi, bridgeward, poly-maker, polymarket-btc-15min-bot, polymarket-orderbook-substreams, polymarket-mcp-server, polymarket-analyzer, poly_data, prediction-market-backtesting, gpl-3-0-rejection, mit-vs-gpl-license-discrepancy, karpathy-pattern-adjacent, prompt-extraction-pattern, fork-and-maintain-pattern]
clusters: [librarian-tooling, link-evaluation, decision-record, polymarket]
related:
  - sources/gemini-dr-link-eval-2026-04-28.md
  - sources/gemini-dr-wave3-link-eval-2026-04-28.md
  - sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md
  - sources/gemini-dr-wave4b-osint-2026-04-29.md
  - sources/gemini-dr-wave5a-cemini-stack-2026-04-30.md
  - sources/caiovicentino-polymarket-mcp-server.md
  - sources/agriciDaniel-claude-obsidian.md
  - sources/piebald-claude-code-system-prompts.md
  - sources/atomicmemory-llm-wiki-compiler.md
  - sources/polymarket-predictions-mcp.md
  - sources/polymarket-informed-minority-gomezcram-2026.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/ip-sale-readiness.md
  - concepts/high-signal-paper-patterns.md
  - concepts/mcp-tool-marketplace.md
  - entities/tools/warproxxx-poly-data.md
  - entities/platforms/polymarket.md
  - entities/infrastructure/deepseek-api.md
  - sources/dune-analytics-mcp.md
  - sources/upstash-context7.md
maturity: validated
read_status: read
created: 2026-04-30
updated: 2026-05-17
---

## Relations

- @sources/gemini-dr-link-eval-2026-04-28.md — Wave 2 (24 URLs) parent of the Gemini DR link-evaluation lineage
- @sources/gemini-dr-wave3-link-eval-2026-04-28.md — Wave 3 (13 URLs) earlier sibling
- @sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md — Wave 4A (30 URLs) predecessor
- @sources/gemini-dr-wave4b-osint-2026-04-29.md — Wave 4B (18 URLs OSINT focus) — most direct sibling: same paragraph count + similar URL evaluation depth
- @sources/gemini-dr-wave5a-cemini-stack-2026-04-30.md — Wave 5A canonical sibling (6 URLs, Cemini-stack focus); Wave 5B is the deeper (18-URL) Polymarket-cluster + workflow-tooling pass authored same day
- @sources/caiovicentino-polymarket-mcp-server.md — URL 14 dedicated source page (Adopt tier; the wave's only Adopt)
- @sources/agriciDaniel-claude-obsidian.md — URL 2 dedicated source page (Steal-from tier; Karpathy LLM Wiki pattern adjacent — promoted given direct relevance to the librarian)
- @sources/piebald-claude-code-system-prompts.md — URL 6 dedicated source page (Steal-from tier; 9.6k stars + 114 releases + tracks Claude Code v2.1.123)
- @sources/atomicmemory-llm-wiki-compiler.md — Wave 4B Adopt; pairs operationally with claude-obsidian (URL 2) — both implement Karpathy LLM Wiki pattern; atomicmemory is for headless server, claude-obsidian is for visual workstation
- @sources/polymarket-predictions-mcp.md — Wave 4A URL 19 (kukapay's MCP); pairs adjacently with the Wave 5B Polymarket cluster
- @sources/polymarket-informed-minority-gomezcram-2026.md — paper that motivated the Polymarket cluster evaluation; the Wave 5B Polymarket cluster gives Cemini the deployment-surface options
- @concepts/wiki-tooling-evaluation.md — wave-evaluation parent for librarian-side findings
- @concepts/ip-sale-readiness.md — license analysis parent; **major finding**: 2 GPL-3.0 / LGPL-3.0 rejections in this wave (poly_data URL 16, prediction-market-backtesting URL 17). License-discrepancy pattern (poly_data: GPL-3.0 repo-level vs MIT pyproject.toml metadata) verified — repo-level GPL-3.0 stands.
- @concepts/high-signal-paper-patterns.md — rubric used to score the Adopts
- @concepts/mcp-tool-marketplace.md — MCP server proliferation pattern continues; polymarket-mcp-server is the wave's MCP-Adopt, joining context7 + dune-analytics-mcp + polymarket-predictions-mcp from Wave 4A
- @entities/platforms/polymarket.md — 7 of the 18 URLs target Polymarket directly (the Polymarket cluster of this wave)
- @entities/infrastructure/deepseek-api.md — Cemini's brain integration target; polymarket-mcp-server's "45 tools" gives DeepSeek-V4-Flash direct prediction-market trading capability via MCP

## Raw Concept

- **Original title**: "Cemini Stack and Wiki Stack Deep Integration Evaluation"
- **Source filename**: `another Evaluating Code for Trading & Wiki Stacks 4_30.docx`
- **Type**: User-authored Gemini Deep Research output (docx, 270 paragraphs)
- **Date**: 2026-04-30 EDT (user-authored same day as Wave 5A)
- **URL count**: 18 evaluations (5 Unavailable; 13 evaluable)
- **Evaluation framework**: 8-section per-URL template (Identity / What it is / Scoring table / Detailed evaluation / Recommendation tier / Risks & caveats / Open questions / Primary sources cited) — consistent with all prior waves
- **Evaluation surfaces**: Cemini production stack / Wiki/librarian server stack / Workflow
- **Location after ingest**: cemini-librarian:/opt/cemini-bulk/research/another Evaluating Code for Trading & Wiki Stacks 4_30.docx
- **Read status**: read (full text extracted; URL catalog + tier per URL captured; Adopt + most-relevant Steal-from URLs anti-hallucination-spot-checked via Exa `crawling_exa`)
- **Discovered via**: User manual drop in inbox 2026-04-30 alongside Wave 5A sibling
- **Primary clusters**: librarian-tooling, link-evaluation, decision-record, polymarket

## Narrative

### Recommendation distribution (18 URLs)

| Tier | Count | URLs |
|---|---|---|
| **Adopt** | 1 | polymarket-mcp-server (14) |
| **Steal-from** | 5 | claude-obsidian (2), claude-code-system-prompts (6), BridgeWard (9), poly-maker (11), Polymarket-BTC-15-Min-Bot (12) |
| **Reference-only** | 4 | agency-agents (3), system_prompts_leaks (7), polymarket-orderbook-substreams (13), polymarket-analyzer (15) |
| **Reject** | 3 | openagi (8), poly_data (16) GPL-3.0, prediction-market-backtesting (17) GPL-3.0+LGPL-3.0 |
| **Unavailable** | 5 | Ling-2.6-1T (1), CoMeT-CC (4), claude-opus-4.7-prompt-optimizer (5), patrickelmore.com (10), kruschdev/pg-git-mcp (18) |
| total | 18 | |

Adopt rate: 1/13 evaluable = **7.7%**. Combined operational adoption (Adopt + Steal-from) = 6/13 = **46%**. The wave heavily favored prompt-extraction-pattern Steal-froms and Polymarket-cluster code; only 1 clean Adopt because most Polymarket projects either fail license (GPL-3.0) or fail framework-compatibility (NautilusTrader-locked).

### Anti-hallucination spot-check (Adopt + key Steal-froms + license-discrepancy Reject)

Per the Wave 2/3/4/5A protocol, 4 URLs were verified via Exa `crawling_exa` against GitHub primary URLs:

| URL | Verdict pre-spot-check | Spot-check result |
|---|---|---|
| URL 14 — caiovicentino/polymarket-mcp-server | Adopt | License MIT ✅ confirmed file + repo level; **395 stars / 90 forks**; Python (80.7%); 45 tools; created 2025-11-11, last push 2026-04-03; **Contributors: 1** (bus-factor — fork-and-maintain warranted); Latest release v0.1.0 (only 1 release total). |
| URL 2 — AgriciDaniel/claude-obsidian | Steal-from | License MIT ✅ confirmed file + repo level; **3,581 stars / 416 forks** — high signal; 6 releases through v1.6.0; Python (69%) + Shell (29%); created 2026-04-07, last push 2026-04-24 (23 days old at evaluation, very fresh); **Contributors: 1** (bus-factor); Karpathy LLM Wiki pattern in repo description. **Promoted to dedicated source page**. |
| URL 6 — Piebald-AI/claude-code-system-prompts | Steal-from | License MIT ✅ confirmed; **9,684 stars** — strongest star signal in the wave; 4 contributors; **114 releases** (one per Claude Code version), latest v2.1.123 on 2026-04-29 (literal day-before-evaluation); JavaScript-only; tracks Claude Code's prompt content per-version. **Promoted to dedicated source page**. |
| URL 16 — warproxxx/poly_data | Reject (GPL-3.0) | License confirmed: **GNU General Public License v3.0 (GPL-3.0)** at repo level (Exa-confirmed). The docx noted a `pyproject.toml License: MIT` discrepancy as [NEEDS VERIFICATION 2026-04-30]; repo-level GPL-3.0 stands. Reject stands. 1,578 stars / 4 contributors. |

**Three material findings beyond drift**:

1. **polymarket-mcp-server bus-factor** — Adopt verdict is sound IF Cemini commits to fork-and-maintain. 1-contributor, 1-release repo at 2.5 months old. Mitigation: pin to v0.1.0 commit hash, fork to Cemini-controlled GitHub org. Same playbook as Wave 4A polymarket-predictions-mcp (kukapay's, 3 stars at the time).

2. **claude-obsidian Karpathy-pattern adjacency** — The repo's description ("Persistent, compounding wiki vault based on Karpathy's LLM Wiki pattern. /wiki /save /autoresearch") makes it directly adjacent to the workspace's own implementation philosophy. The /autoresearch slash command is the most operationally interesting extract — a multi-round research-loop pattern that could augment the workspace's existing Tier-2 sweep workflow. **Promoted to dedicated source page**.

3. **poly_data license-discrepancy resolution** — The docx flagged a real conflict: the GitHub repo-level license shows GPL-3.0 but the pyproject.toml metadata reads `License: MIT`. **Authoritative resolution**: GitHub's repo-level license detection (which inspects LICENSE file content) is canonical for IP-sale-readiness purposes. The pyproject.toml metadata field is informational and can drift; legal counsel evaluating the codebase will look at the LICENSE file. **Reject stands**. New IP-sale-readiness sub-pattern: **license-metadata-discrepancy** — when project metadata disagrees with LICENSE file, the LICENSE file is canonical.

### Pre-existing wiki integration

- All Wave 5B URLs are first-evaluation in this session.
- Wave 4A URL 19 (kukapay/polymarket-predictions-mcp) and Wave 5B URL 14 (caiovicentino/polymarket-mcp-server) form a **dual-MCP-Polymarket-server pattern**: kukapay's is a *predictions-data MCP* (read-only odds delivery); caiovicentino's is a *trading MCP* (45 tools incl. autonomous trading). Together they cover the full Polymarket integration surface for Cemini.

### Per-URL summaries — Adopt (1)

**URL 14: caiovicentino/polymarket-mcp-server** — MIT, Python, 395 stars
> Production-ready MCP server for Polymarket prediction markets. **45 comprehensive tools** across 5 categories: Market Discovery (8), Market Analysis (10), Trading, Position Management, Real-time Monitoring. Enterprise-grade safety features. Direct integration with FastMCP container via docker-compose. **Adopt for Cemini production**: deploy as isolated service block, gives DeepSeek-V4-Flash direct Polymarket trading capability via MCP protocol — no custom integration code. Pairs with Wave 4A's polymarket-predictions-mcp (kukapay) for full read+write coverage. **Bus-factor caveat**: 1 contributor, 1 release — fork-and-maintain pattern applies. Key security risk: requires `.env`-injected POLYMARKET_PASSPHRASE private keys; secret-management hardening required pre-prod. **Promoted to dedicated source page this session.**

### Per-URL summaries — Steal-from (5)

**URL 2: AgriciDaniel/claude-obsidian** — MIT, Python, 3.6k stars [STEAL-FROM]
> Claude+Obsidian persistent knowledge engine, **Karpathy LLM Wiki pattern** explicit in repo description. /wiki /save /autoresearch slash commands. Maps directly to the workspace's existing librarian methodology. **Steal-from extract**: the `/autoresearch` multi-round research loop pattern + the `wiki-lint.py` implementation specifics + the `wiki/hot.md` session-memory caching schema. Direct workflow boost for the solo-dev curation cycle. **Cemini production no-fit**: requires Obsidian Local REST API + visual environment. **Wiki/Librarian no-fit (full deploy)**: too tied to Obsidian for headless CPX21. Steal the patterns, not the runtime. **Promoted to dedicated source page.**

**URL 6: Piebald-AI/claude-code-system-prompts** — MIT, JavaScript, **9.7k stars**, **114 releases tracking Claude Code v2.1.123** [STEAL-FROM]
> Systematic extraction of Claude Code's internal system prompts, 24 builtin tool descriptions, sub-agent prompts (Plan/Explore/Task), utility prompts (CLAUDE.md, compact, statusline, magic docs, WebFetch, Bash cmd, security review, agent creation). Released per Claude Code version. **Steal-from extract**: the prompt structures themselves — formatting syntax, parameter descriptions for the 24 builtin tools — directly applicable to Cemini's ~130 custom FastMCP tool decorators. Lift the schemas, structurally adapt to FastMCP, gain consistency. **Risk**: extreme upstream volatility (Claude Code beta, v2.1.124 today is v2.1.130 next month). Adoption requires fork+pin, periodic re-sync. **Pre-prod gate**: confirm DeepSeek-V4-Pro-Think strict adherence to heavy-XML-tagging structures (Claude-specific) before committing schemas. **Promoted to dedicated source page.**

**URL 9: BridgeWard (bridge-mind)** — License pending verification [STEAL-FROM]
> Prompt-injection defense skill for AI agents. "Trust nothing, ship safely" paradigm. Skeptical-reading patterns + read-only injection auditor concept. **Steal-from extract**: regex patterns + textual refusal templates + the auditor concept (append to wiki_lint.py tail to gate external PDF/paper summaries). Native bash-shell-only invocation forces extraction-not-deployment. **Risk**: false-positive refusals on legitimate data ops. **Workflow Yes-fit; Cemini production partial-fit pending Python rewrite.**

**URL 11: poly-maker (warproxxx)** — License pending verification ⚠️ [STEAL-FROM]
> Polymarket automated market-maker bot. Liquidity layers via dynamic order placement. **Steal-from extract**: the order-placement state machine + the Python `trading.py`/`poly_data` modules. **Reject as-deployed**: native architecture uses Node.js for `poly_merger` logic + external Google Sheets as control plane (incompatible with Cemini). **Critical caveat**: README explicitly states the bot will **actively lose money in current environments** — do not deploy default spread logic. Steal the structural patterns, write Cemini-native trading logic. NOTE: warproxxx also authors poly_data (URL 16, GPL-3.0 Reject) — verify poly-maker's license independently.

**URL 12: Polymarket-BTC-15-Minute-Trading-Bot (aulekator)** — License pending verification [STEAL-FROM]
> 7-phase architecture for 15-minute Bitcoin price prediction markets on Polymarket. NautilusTrader-based execution engine. **Steal-from extract**: (a) custom hardened Polymarket API wrapper (`polymarket_client.py`); (b) Signal Processors (price divergence + Fear & Greed Index mappings); (c) Risk Management algorithms (30% stop-loss, 20% take-profit constraints). **Reject as-deployed**: NautilusTrader replacement of Cemini's LangGraph would be unacceptable foundational rewrite. Adopt the components selectively into Cemini's existing orchestrator.

### Per-URL summaries — Reference-only (4)

- **URL 3: msitarzewski/agency-agents** — Static AI agent personality library, .md+frontmatter. 144 specialized agents. Shell-script `convert.sh` ingestion utility. **Reference-only**: load decorum content into Claude Code via convert.sh; do not deploy as Cemini agents. Risk: context-limit pollution from overly-detailed personas degrades model instruction-following.
- **URL 7: asgeirtj/system_prompts_leaks** — Crowdsourced static collection of leaked commercial-AI system prompts (Anthropic, OpenAI, xAI). MIT wrapper, but underlying prompt text is corporate IP. **Reference-only**: educational reading; never copy-paste into Cemini production prompts (copyright contamination risk).
- **URL 13: PaulieB14/polymarket-orderbook-substreams** — StreamingFast Substreams for high-fidelity Polymarket CLOB v2 data extraction from Polygon blockchain. Rust-binary + Substreams runtime — completely outside Cemini's Python/Polars/FastMCP stack. **Reference-only**: proves what specialized infrastructure is needed for CLOB-level data; Cemini sticks with official API webhooks.
- **URL 15: mneves75/polymarket-analyzer** — Bun+TypeScript Blessed-TUI live Polymarket dashboard. **Reference-only**: extract `rateLimiter.ts` Token Bucket logic; do not deploy TUI itself.

### Per-URL summaries — Reject (3)

- **URL 8: aiplanethub/openagi** — Multi-agent framework w/ Admin/Worker hierarchies + LTM. **Reject**: solves problems Cemini's LangGraph+FastMCP already solves; Jupyter Notebooks (51.6%) workflow incompatibility; potential heavy local vector DB (ChromaDB/FAISS) blowing CPX21 budget.
- **URL 16: warproxxx/poly_data** — **GPL-3.0 (verified Exa repo-level)**. Comprehensive Polymarket data pipeline. **Reject**: license-metadata-discrepancy (GPL-3.0 LICENSE vs MIT pyproject.toml metadata; LICENSE file is canonical). 1,578 stars don't override license fact. Poison-pill family A (copyleft).
- **URL 17: evan-kolberg/prediction-market-backtesting** — **GPL-3.0 + LGPL-3.0** (mixed copyleft). Advanced backtesting on NautilusTrader for Kalshi/Polymarket. **Reject**: poison-pill family A. Plus: massive local Hive-partitioned full-book Parquet mirrors footprint blowing any local hardware budget.

### Per-URL summaries — Unavailable (5)

- URL 1: huggingface.co/inclusionAI/Ling-2.6-1T — network/access blocked
- URL 4: Dirac-Robot/CoMeT-CC — connection error
- URL 5: CheswickDEV/claude-opus-4.7-prompt-optimizer — connection error
- URL 10: patrickelmore.com context-pollution-debris-not-capacity blog post — connection error
- URL 18: kruschdev/pg-git-mcp — connection error

These are reasonable Tier-2 gap-fill targets for a future workflow re-evaluation pass.

### Cross-wave patterns

1. **License-metadata-discrepancy resolution** (poly_data URL 16): when `pyproject.toml` License field contradicts the repo-root `LICENSE` file, the LICENSE file is canonical for IP-sale-readiness assessment. Confirmed via Exa repo-level license detection. New sub-pattern under `@concepts/ip-sale-readiness.md`.

2. **The "Reject-by-license + popular" recipe** (poly_data 1.6k stars, prediction-market-backtesting). High-star copyleft projects are a recurring trap: stars + community ≠ adoption signal when the license precludes inclusion. Confirms the Wave-2 pattern that license rules trump popularity for IP-sale-readiness.

3. **The dual-MCP-Polymarket pattern** (Wave 4A URL 19 kukapay/polymarket-predictions-mcp + Wave 5B URL 14 caiovicentino/polymarket-mcp-server). One MCP for read-only odds; the other for autonomous trading. Together they form the complete Polymarket-integration MCP layer for Cemini's brain. **Both 1-contributor, fork-and-maintain pattern.**

4. **Karpathy-pattern adjacency** (Wave 5B URL 2 claude-obsidian) joins atomicmemory/llm-wiki-compiler (Wave 4B Adopt) and wastedcode/memex (earlier wiki) as the third Karpathy-pattern implementation in the corpus. Three distinct flavors emerge: (a) headless server (atomicmemory), (b) visual workstation (claude-obsidian), (c) filesystem-only minimal (wastedcode/memex). Each has a niche; Cemini's workspace is closest to claude-obsidian conceptually.

5. **Prompt-extraction-pattern** (Wave 5B URL 6 claude-code-system-prompts; Wave 5B URL 7 system_prompts_leaks) is a new content-vs-runtime pattern: the **content** (prompt text + tool descriptions + structures) is the high-value extract; the **runtime** (JavaScript scrapers) is irrelevant. Mirrors the Wave 5A "Steal-from-the-tokenizer-not-the-model" pattern (Kronos): the upstream component is what's worth keeping.

6. **NautilusTrader-as-rejection-trigger** (URL 12 BTC-15-Min-Bot Steal-from-only because of NautilusTrader rewrite blocker; URL 17 Reject in part because NautilusTrader infrastructure overhead). When a Polymarket project is built on NautilusTrader, **the NautilusTrader dependency is itself a Cemini-stack incompatibility flag**, separate from license. Document under `@concepts/wiki-tooling-evaluation.md`.

### Open questions / NEEDS VERIFICATION

- **URL 9 BridgeWard license** [CONFIRMED 2026-05-17] — `github.com/bridge-mind/bridgeward` repo-level LICENSE = **MIT** (confirmed via Exa crawl + ClaudePluginHub listing). Clean for IP-sale-readiness. Steal-from verdict's license footing holds. Note: this is `bridge-mind/bridgeward` (BridgeMind suite, sole contributor matthewmiller2925, 24★, created 2026-04-30) — not to be confused with unrelated CC-BY-SA-4.0 skills in the same prompt-injection space.
- **URL 9 BridgeWard runtime** [CONFIRMED 2026-05-17] — verified local-only: the README's "What BridgeWard Is Not" section states explicitly "Not a classifier model. **No ML inference, no API calls.** Pure reasoning discipline encoded as instructions." The `injection-auditor` is a read-only subagent (cannot write/edit/execute, cannot follow instructions in audited content). No external API — the good outcome; the Steal-from extract (regex red-flag patterns + refusal templates + auditor concept) is sound.
- **URL 11 poly-maker license** [CONFIRMED 2026-05-17] — `github.com/warproxxx/poly-maker` repo-level LICENSE = **MIT** (Exa crawl confirmed: "License: MIT"). Despite warproxxx also authoring GPL-3.0 poly_data (URL 16), poly-maker itself is cleanly MIT-licensed. Steal-from verdict's license footing holds. Caveat unchanged: `poly_merger` is built on open-source Polymarket code and has a Node.js dependency.
- **URL 11 poly-maker JS-to-Python conversion** [NEEDS VERIFICATION 2026-04-30] — feasibility of rewriting `poly_merger` Node.js logic to Python natively.
- **URL 12 Polymarket-BTC-15-Min-Bot Python 3.14+ feature dependency** [NEEDS VERIFICATION 2026-04-30] — which exclusive Python 3.14+ features (asyncio task groups, advanced typing) are mandated by code.
- **URL 13 polymarket-orderbook-substreams remote subscription** [NEEDS VERIFICATION 2026-04-30] — feasibility of consuming via The Graph or Pinax-managed infrastructure (avoids local Substreams indexer overhead).
- **URL 14 polymarket-mcp-server rate-limiter under load** [NEEDS VERIFICATION 2026-04-30] — token-bucket algorithm under concurrent FastMCP load.
- **URL 14 polymarket-mcp-server secret management** [NEEDS VERIFICATION 2026-04-30] — `.env`-injected POLYMARKET_PASSPHRASE in Docker is acceptable for solo-dev but needs hardening for prod.
- **URL 17 prediction-market-backtesting subset salvage** [NEEDS VERIFICATION 2026-04-30] — corporate legal review for extractable non-GPL subset (charting / mathematical helpers).
- **5 Unavailable URLs** [NEEDS VERIFICATION 2026-04-30] — re-fetch Ling-2.6-1T, CoMeT-CC, claude-opus-4.7-prompt-optimizer, patrickelmore.com, kruschdev/pg-git-mcp.

## Snippets

> **The wave's headline finding (paraphrased)**: 1 Adopt + 5 Steal-from out of 13 evaluable URLs (46% combined operational adoption). Anti-hallucination spot-check confirmed: polymarket-mcp-server (MIT, 395★, 1 contributor — fork-and-maintain), claude-obsidian (MIT, 3.6k★, Karpathy LLM Wiki pattern explicit), claude-code-system-prompts (MIT, 9.7k★, 114 releases tracking Claude Code v2.1.123), and the **license-metadata-discrepancy** in poly_data resolved via repo-level GPL-3.0. The wave's signature pattern: heavy Polymarket cluster (7/18 URLs) of which 1 Adopt + 2 Steal-from extracts pieces + 2 GPL-3.0 Rejects.

> **polymarket-mcp-server adoption rationale (URL 14 evaluation excerpt)**:
>
> "Adopt. This project elegantly and comprehensively solves the exact Polymarket integration and execution requirements mandated for the Cemini ingest layer. Because it is pre-packaged flawlessly as a compliant MCP server, deploying the logic strictly involves adding a new, isolated service block to the existing Cemini docker-compose.yml stack." [Source: another Evaluating Code for Trading & Wiki Stacks 4_30.docx URL 14]

> **claude-obsidian Karpathy-pattern relevance (URL 2 evaluation excerpt)**:
>
> "The repository provides a persistent knowledge engine that intertwines Anthropic's Claude with the Obsidian note-taking application, directly architected around Andrej Karpathy's LLM Wiki pattern. … Steal-from. While the full installation relies heavily on a visual Obsidian environment unsuited for the CPX21 headless transition, the overarching architectural logic embedded inside the agents/wiki-lint.md definitions and the hot.md caching schema are highly valuable." [Source: another Evaluating Code for Trading & Wiki Stacks 4_30.docx URL 2]

> **The license-discrepancy resolution rationale (URL 16 evaluation excerpt)**:
>
> "Although the repository evaluation explicitly identified the primary license as GPL-3.0, a subsequent inspection of the pyproject.toml configuration file metadata surprisingly revealed the tag License: MIT." [Source: another Evaluating Code for Trading & Wiki Stacks 4_30.docx URL 16]
>
> Cemini-resolution: GitHub repo-level license detection (LICENSE file content) is canonical for IP-sale-readiness purposes; pyproject.toml metadata is informational. Reject stands.

> **Anti-hallucination protocol — anchoring quote**:
>
> 4 URLs verified via `mcp__exa__crawling_exa` 2026-04-30. License confirmed at file + repo level: polymarket-mcp-server=MIT, claude-obsidian=MIT, claude-code-system-prompts=MIT, poly_data=GPL-3.0 (Reject confirmed). Star counts: polymarket-mcp-server=395, claude-obsidian=3,581, claude-code-system-prompts=9,684, poly_data=1,578. Contributor counts: polymarket-mcp-server=1 (bus-factor), claude-obsidian=1 (bus-factor), claude-code-system-prompts=4, poly_data=4. Releases: polymarket-mcp-server=1, claude-obsidian=6, claude-code-system-prompts=114 (per-Claude-Code-version), poly_data=N/A. [Per Exa spot-check 2026-04-30]
