---
title: "5_6 links — Architecture and IP Due Diligence Link Evaluation Report (17 URLs)"
type: source
tags: [llm-agents, dev-tooling, knowledge-graph, prompt-engineering, license-compliance, prediction-markets, cemini-internal]
keywords: [tool-evaluation, gemini-deep-research, sift-kg, curl-md, predictparity, obsidian-llm-wiki-local, agentic-trading, deepteam, loki-mode-busl, license-drift]
related:
  - sources/5-5-moarrr-tool-eval.md
  - sources/links-3-5-4-tool-eval.md
  - concepts/cemini-license-posture.md
  - concepts/ip-sale-readiness.md
  - entities/tools/sift-kg.md
  - entities/tools/curl-md.md
  - entities/tools/obsidian-llm-wiki-local.md
  - entities/tools/agentic-trading.md
  - entities/tools/deepteam.md
  - entities/tools/loki-mode.md
  - entities/tools/pybroker.md
  - entities/tools/gitnexus.md
  - entities/tools/codex-startup-pressure-test-skill.md
  - entities/tools/research-paper-writing-skills.md
  - entities/tools/academic-paper-skills.md
  - entities/tools/polymarket-trackers.md
  - entities/tools/git-rewind.md
maturity: draft
read_status: deep-read
created: 2026-05-06
updated: 2026-05-06
---

## Relations

- @sources/5-5-moarrr-tool-eval.md — K31 sister batch (19 tools); this K32 batch reuses identical 8-section per-URL template
- @sources/links-3-5-4-tool-eval.md — K30 batch surfaced Elastic License v2 (mode #9 in catalog); this K32 batch surfaces License Drift (mode #10)
- @concepts/cemini-license-posture.md — license-pattern catalog updated with mode #10 (License Drift, loki-mode BUSL transition + stale aggregator misreport)
- @concepts/ip-sale-readiness.md — license verdicts in this batch operate under softened "monetization-priority 2026" frame: poison-pill auto-rejection relaxed for non-prod-codebase use (laptop dev tools, prompt patterns, reference reading)
- @entities/tools/sift-kg.md — KG-builder eval (Exa-resolved from "UNAVAILABLE"): 453★, KGGen-inspired, OSINT preset domain, high relevance to wiki model — full audit needed
- @entities/tools/curl-md.md — URL→markdown CLI (Exa-resolved): MIT open source, ingest-pipeline candidate
- @entities/tools/obsidian-llm-wiki-local.md — STEAL-FROM tier; highest action-value of the batch (3-tier JSON retry + orphan-normalization → upgrade laptop's `wiki_lint.py`)
- @entities/tools/agentic-trading.md — REFERENCE-ONLY tier; NeurIPS 2025 paper + 4-layer agent protocol (MCP/ACP/A2A/ANP) worth studying for in-house Conductor evolution
- @entities/tools/deepteam.md — DEFER tier; Apache-2.0 LLM red-teaming framework, RAM concern on prod, vendor pull-up axis
- @entities/tools/loki-mode.md — REJECT tier; License Drift exemplar (MIT→BUSL-1.1 transition, third-party aggregators still falsely report MIT)
- @entities/tools/pybroker.md — REJECT tier; Apache-2.0 + Commons Clause poison pill + Polars architectural redundancy
- @entities/tools/gitnexus.md — REJECT-EVALUATE tier; PolyForm-NC 1.0.0 — verdict softened from auto-reject to utility-vs-risk per monetization priority
- @entities/tools/codex-startup-pressure-test-skill.md — STEAL-FROM tier; abandoned project (2 commits, MIT), extract pressure-test/competition-map/mvp-plan prompt patterns
- @entities/tools/research-paper-writing-skills.md — STEAL-FROM tier; abandoned (4 commits, MIT), extract claim-evidence alignment + abstract synthesis patterns
- @entities/tools/academic-paper-skills.md — STEAL-FROM tier; abandoned (2 commits, MIT), 35-point peer-review framework worth porting to wiki_lint.py / brief audit
- @entities/tools/polymarket-trackers.md — Exa-resolved Polymarket-tracker landscape (predictparity/Parity, PredictFolio, PolyWallet) — fits @concepts/prediction-market-historical-analysis.md
- @entities/tools/git-rewind.md — K31 Adopt-tier carry-forward; this batch independently confirms Adopt verdict

## Raw Concept

- Original title: "Architecture and IP Due Diligence Link Evaluation Report"
- Author: Gemini Deep Research
- Type: docx — Cemini-internal architecture evaluation
- Location: cemini-librarian:/opt/cemini-bulk/research/5_6 links.docx (post-ingest move)
- Retrieved: 2026-05-06
- Length: ~55 KB, 17 URLs evaluated using identical 8-section template (Identity / What it is / Scoring / Detailed evaluation / Recommendation tier / Risks / Open questions / Sources)
- Read status: deep-read
- Companion file: laptop `research to be indexed/5_6 links.docx` (sha256 `cd96bebc0b2130dc...`); inbox-cleared post-commit

## Narrative

### Verdict distribution

| Tier | Count | Items |
|------|-------|-------|
| ADOPT | 1 | git-rewind (independent confirm of K31) |
| STEAL-FROM | 4 | codex-startup-pressure-test-skill, Research-Paper-Writing-Skills, academic-paper-skills, obsidian-llm-wiki-local |
| REFERENCE-ONLY | 2 | AgenticTrading (NeurIPS 2025 paper + 4-layer protocol), ISC SANS Edge cleartext-pw advisory |
| DEFER | 1 | deepteam (RAM + vendor-pull axes) |
| REJECT | 6 | pybroker, GitNexus, planet-superres, openreel-video, loki-mode, dflash |
| UNAVAILABLE@eval-time | 3 | sift-kg, curl.md/playground, predictparity.com profile (all three Exa-resolved 2026-05-06 as workspace post-processing — NOT skipped) |

### Exa post-processing of the 3 UNAVAILABLE URLs (added 2026-05-06)

Gemini DR's eval-time HTTP errors prevented evaluation of 3 URLs. Workspace re-resolved via Exa search/crawl. Findings:

1. **sift-kg** (`github.com/juanceresa/sift-kg`) — Python knowledge-graph builder, **453 stars** (sizable maintained project), inspired by KGGen (NeurIPS 2025) by `@stochastic-sisyphus`. Pipeline: documents → text extraction (Kreuzberg + optional OCR) → schema discovery (LLM) → entity/relation extraction (LLM) → NetworkX KG → entity resolution (LLM proposes, human approves) → narrative generation → interactive viewer/exports (GraphML/GEXF/CSV/SQLite). **Has predefined `osint` domain schema.** License [TBV — likely MIT/Apache, requires verification]. Strong fit signal for our librarian/wiki model — see @entities/tools/sift-kg.md for the full audit.

2. **curl.md** (`http://curl.md`) — "URL to markdown for agents" CLI tool. MIT-licensed, open source. Single-line install: `curl -fsSL https://curl.md/install.sh | bash`. Use prefix `curl.md/<URL>` to retrieve any URL as token-optimized markdown. Direct **ingest-pipeline candidate**: replaces `mcp__exa__crawling_exa` for URL→clean-markdown conversion in `## Snippets` extraction step. Cost discipline: open source, no API key required. See @entities/tools/curl-md.md.

3. **predictparity.com profile** (`@amisrael123`) — predictparity.com is now branded "Parity" (login wall). Sister tools surfaced via Exa: **PredictFolio** (predictfolio.com — leaderboard, trader search, community PnL, $5B traded volume across 2.4M traders) and **PolyWallet** (polywallet.app — wallet-tracker w/ live PnL, 30s refresh on premium, leaderboard scout, MIT-style freemium SaaS). All three together form a Polymarket trader-analytics ecosystem. Relevant to @concepts/prediction-market-historical-analysis.md — these are tools that monitor Polymarket trader edge, NOT directly tools Cemini deploys, but candidate data sources for "follow the smart wallets" alpha. See @entities/tools/polymarket-trackers.md.

### License-pattern catalog update (NEW mode #10)

K32 surfaces one new failure mode for the catalog at @concepts/cemini-license-posture.md:

**Mode #10: License Drift** — A repository transitions from a permissive license (MIT) to a restrictive one (BUSL-1.1, Elastic License v2, etc.) at a specific commit, but third-party aggregators (libraries.io, SourceForge mirrors, npm/PyPI mirrors, search-engine snippets) continue to surface the OLD license metadata for weeks or months after the change. **Mitigation**: never trust aggregator metadata; always read the canonical repo's current `LICENSE` file + recent commit log + any `LICENSE-CHANGE-NOTICE.md`. K32 exemplar: **loki-mode** (asklokesh/loki-mode) — repository commits show transition from MIT to BUSL-1.1, but SourceForge mirror + libraries.io still report MIT. Trusting aggregator data here in M&A diligence would be a catastrophic license-posture miss.

This is operationally distinct from K27 mode #1 (NO LICENSE → default copyright) and from mode #5 (Dual-license MIT-vs-GPL ambiguity). The drift mode specifically catches **time-shifted aggregator staleness**.

### Already-known patterns reinforced (no catalog change)

- **Mode #5 (Apache-2.0 + Commons Clause poison pill)** — pybroker (edtechre). Commons Clause forbids commercial use of derivative works; poisons the otherwise-permissive Apache-2.0 base.
- **Mode #5/#9 family (Source-available with non-commercial use restriction)** — GitNexus (PolyForm Noncommercial 1.0.0). Restated: NO production commercial deployment; reference-reading only. Per monetization-priority frame (`monetization_priority_2026.md` memory), laptop-side dev-tool use **may be defensible** if it generates revenue and isn't directly mirrored into prod codebase.
- **Mode (Apache + commercial vendor pull-up)** — deepteam (confident-ai). Apache-2.0 base is fully clean, but the project actively channels users toward the "Confident AI" SaaS platform for advanced features. Not a license-rejection per se, but a cost/lock-in signal worth flagging.

### Key takeaways by category

**1. Wiki/librarian-model upgrades (4 STEAL-FROM candidates)**

The most actionable cluster of the batch. All four are MIT-licensed, mostly-abandoned (2-4 commits), but contain high-value prompt-engineering and Python-linting patterns that directly upgrade Cemini's existing workflow:

- **obsidian-llm-wiki-local** — production-ready Python implementation of `wiki_lint.py`'s expanded feature set: 3-tier JSON-retry-on-malformed-LLM-output, orphan handling with auto-fix (`olw maintain --fix`), bidirectional `[[wikilinks]]` validation, frontmatter normalization. **Not** an MCP server (kb-server retained for serving layer per K30 decision), but the *linting code* is directly portable to laptop.
- **academic-paper-skills** — 35-point peer-review framework across 7 dimensions executed via Python scripts (`gap_analysis.py`, `chapter_quality_check.py`, `final_evaluation.py`). Adapts cleanly to brief-audit workflow: `scripts/skill_audit.py` could borrow the dimension-scoring matrix.
- **codex-startup-pressure-test-skill** — `pressure-test`, `problem-validation`, `competition-map`, `mvp-plan` analytical reasoning modes encoded as Codex skill scripts. Extract prompt content; ignore the JS package.
- **Research-Paper-Writing-Skills** — claim-evidence alignment + abstract-synthesis prompts. Tuned for ML/CV/NLP, requires re-styling for quant-finance domain.

Recommended brief: `briefs/2026-05-06_obsidian-llm-wiki-local-steal-from.md` — wiki_lint.py upgrade plan.

**2. Knowledge-graph alternative (sift-kg)**

This is the most strategically interesting Exa-resolved find. sift-kg builds a NetworkX KG from arbitrary documents using LLM-driven schema discovery + human-in-the-loop entity resolution. Has a built-in `osint` domain schema. **Architectural question**: does this complement or compete with the Karpathy LLM Wiki pattern Cemini already uses? Two possibilities:

- **Complement**: run sift-kg over `wiki/sources/` to generate a structured graph layer (entity tables) on top of the existing prose pages. Use the graph for queries Cemini's current wiki structure can't handle (e.g., "show all sources citing Person X").
- **Compete**: replace the manual frontmatter+`@path` cross-link convention with sift-kg's auto-extracted graph. Risk: lose authorial control over which entities/relations exist.

Phase-0 audit needed before any decision. License [TBV] — must verify before any deeper work.

**3. Agent-orchestration reference (AgenticTrading)**

The Open-Finance-Lab/AgenticTrading repo + its NeurIPS 2025 paper present a 4-layer multi-agent communication protocol: **MCP** (Multi-agent Control), **ACP** (Agent Communication), **A2A** (peer coordination), **ANP** (Agent Network). Couples a DAG Planner Agent with specialized pools (Data, Alpha, Risk, Portfolio, Execution). Reportedly outperforms S&P 500 + Bitcoin in simulation. **Not for production deployment** (Neo4j dependency + 20-agent concurrency exceeds 7GB RAM ceiling), **not for IP-sale codebase** (license unverified per DR), but the protocol stratification is valuable input to in-house Conductor evolution at @concepts/conductor-orchestrator.md.

**4. Polymarket-tracker ecosystem (Exa-resolved)**

predictparity.com / PredictFolio / PolyWallet are wallet-watch / leaderboard-scout services for Polymarket. Relevant signal source for "follow the smart wallets" alpha strategies on top of @entities/tools/polymarket-agents.md. Not adoption candidates (these are SaaS, not libraries), but candidate data feeds — particularly PolyWallet's wallet-state APIs.

**5. Confirmed K31 git-rewind decision**

DR independently reaches "Adopt" verdict with the same reasoning as the K31 sister eval (Apache-or-MIT [TBV in upstream], laptop-only dev tool, OpenAI-API-compatible endpoint flexibility). Two minor discrepancies vs the K31 eval:

- DR claims "the developer should install via Cargo" — actually requires Rust toolchain that Cemini laptop doesn't have. K31 fallback path (manual binary install) is correct.
- DR doesn't mention the `install.sh` checksum bug that K31 surfaced and filed upstream as [issue #1](https://github.com/Chronos778/git-rewind/issues/1).

No action — git-rewind 1.1.4 already adopted K31, in `~/.local/bin/rewind` on laptop.

**6. ISC SANS Edge cleartext-passwords advisory**

Reference-only. Microsoft Edge stores all saved browser passwords in process memory in cleartext, harvestable via Task Manager memory dumps + string-search for `comhttps`. Reportedly classified by Microsoft as "intended behavior". Operational implication: **do NOT store the laptop's API keys (DeepSeek, Polygon, Hetzner, Kalshi, Groq, Gemini, OpenAI) in MS Edge password manager**. Cemini's laptop is macOS so this is mostly moot — but flagged for future Windows-laptop scenarios. No wiki page warranted; recorded here for ingest completeness.

**7. Domain-mismatch rejects with no signal beyond reject (skipped from entity stubs)**

- **planet-superres** — proprietary GAN-upscaled satellite imagery; CV/spatial-DB stack mismatch w/ Cemini text-first architecture
- **openreel-video** — 125k-line React/WebGPU video editor; total domain mismatch
- **dflash** — speculative-decoding optimizer for vLLM/SGLang; GPU-only, not relevant to API-call-based Cemini

These are not getting entity stubs. Recorded here for catalog completeness.

### Cemini stack impact summary

**No prod-side action**: nothing in this batch ships to `cemini-prod:/opt/cemini/` directly. The 9 K28-K31 active prod briefs remain the queue.

**Laptop-side actions** (post-ingest):

1. **STAGE BRIEF**: `briefs/2026-05-06_obsidian-llm-wiki-local-steal-from.md` — port 3-tier JSON retry + orphan/wikilink normalization to `scripts/wiki_lint.py`. Deferred-execution (workspace-side).
2. **AUDIT (Phase-0)**: sift-kg license + maturity audit before any complementarity decision. Defer unless monetization-relevant.
3. **AUDIT-LITE**: curl.md viability vs `mcp__exa__crawling_exa` for ingest-pipeline. Cheap.
4. **PROMPT-LIB**: extract codex-startup-pressure-test-skill + academic-paper-skills + Research-Paper-Writing-Skills prompt content into a `prompt-patterns/` directory or directly into `.claude/skills/` definitions. Deferred until concrete need surfaces.

**Cemini-prod impact**: zero — this batch is workflow/methodology-side.

## Snippets

### License Drift (loki-mode BUSL transition)

> "While earlier versions or community summaries erroneously claim the project operates under MIT, repository commits explicitly demonstrate that the license was changed to BUSL-1.1 (Business Source License). The system context unequivocally states that 'BSL with restrictive terms' resides firmly on the poison-pill reject list. ... The foremost risk is License Drift. The project transitioned from the permissive MIT license to the restrictive BUSL-1.1 recently. However, online aggregators and older documentation still falsely report it as MIT. Trusting third-party aggregators over the actual repository's commit history in an M&A context leads to catastrophic due-diligence failure." [Source: 5_6 links.docx URL 14]

### sift-kg pipeline architecture (Exa-resolved upstream README)

> "Documents (PDF, DOCX, text, HTML, and 75+ formats) → Text Extraction (Kreuzberg, local) — with optional OCR (Tesseract, EasyOCR, PaddleOCR, or Google Cloud Vision) → Schema Discovery (LLM designs entity/relation types from your data — or use a predefined domain) → Entity & Relation Extraction (LLM, using discovered or predefined schema) → Knowledge Graph (NetworkX, JSON) → Entity Resolution (LLM proposes → you review) → Narrative Generation (LLM) → Interactive Viewer (browser) / Export (GraphML, GEXF, CSV, SQLite)" [Source: https://github.com/juanceresa/sift-kg/blob/main/README.md (retrieved 2026-05-06)]

### Obsidian LLM Wiki Local — wiki-maintenance command surface

> "Crucially, it includes robust self-healing maintenance commands (such as olw maintain --fix) designed to programmatically repair broken links, handle orphaned articles, and normalize the wiki structure. To ensure stability when interacting with smaller local models, it employs a sophisticated 3-tier JSON retry system to gracefully handle occasionally malformed LLM outputs." [Source: 5_6 links.docx URL 17]

### AgenticTrading 4-layer agent protocol (DR direct quote)

> "It deploys a Directed Acyclic Graph (DAG) Planner Agent that interprets high-level strategic directives and autonomously orchestrates task execution across specialized agent pools, including Data, Alpha, Risk, Portfolio, and Execution components. The framework consumes live financial data from providers like Polygon.io and Yahoo Finance, routing inter-agent communications through four custom protocol layers: MCP (Multi-agent Control Protocol), ACP, A2A, and ANP." [Source: 5_6 links.docx URL 4]

### Curl.md ingest-pipeline framing (Exa-resolved upstream)

> "URL to markdown for agents. Turn websites into optimized, low token output to supercharge your context. Works with every agent. ... Yes, curl.md is fully open source. The source code is public on GitHub under the MIT License." [Source: http://curl.md/ (retrieved 2026-05-06)]

## Dead Ends

- **DR claim that Cargo is "preferred install" for git-rewind** — wrong for Cemini laptop (no Rust toolchain). K31 manual-binary path stands. Logged for cross-eval-source reconciliation: when two independent DR runs differ on install procedure, prefer the one with verified end-to-end smoke test (K31).
- **DR's "URL UNAVAILABLE" verdict for sift-kg/curl.md/predictparity** — eval-time HTTP errors should NOT default to "skip." Workspace post-processing via Exa rescued 3 high-signal pages from this batch. Lesson: integrate Exa-fallback as a standard step in future Gemini DR ingest workflow when HTTP-error verdicts appear.
