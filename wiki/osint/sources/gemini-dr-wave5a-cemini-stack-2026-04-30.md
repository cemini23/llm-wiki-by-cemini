---
title: "Gemini Deep Research — Wave 5A: Cemini Stack & Wiki Stack Link Evaluation (6 URLs, 2026-04-30)"
type: source
tags: [docx, librarian-tooling, link-evaluation, decision-record, gemini-dr-wave5, cemini-internal, mcp-servers, trading-tools, license-evaluation]
keywords: [gemini-dr-wave5a, link-evaluation, firnflow, the-well, kronos, zeroboot, stash, worldseed, kronos-status-change, lancedb-columnar-format, foyer-hybrid-cache, polymathic-ai, vm-sandboxes, mcp-memory-layer, multi-agent-simulation, anti-hallucination-spot-check, fork-and-maintain-pattern]
clusters: [librarian-tooling, link-evaluation, decision-record]
related:
  - sources/gemini-dr-link-eval-2026-04-28.md
  - sources/gemini-dr-wave3-link-eval-2026-04-28.md
  - sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md
  - sources/gemini-dr-wave4b-osint-2026-04-29.md
  - sources/alash3al-stash.md
  - sources/shiyu-coder-kronos.md
  - sources/microsoft-qlib.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/ip-sale-readiness.md
  - concepts/high-signal-paper-patterns.md
  - entities/infrastructure/pgvector.md
  - entities/infrastructure/hetzner.md
  - entities/infrastructure/deepseek-api.md
  - sources/gemini-dr-wave5b-osint-2026-04-30.md
maturity: validated
read_status: read
created: 2026-04-30
updated: 2026-05-17
---

## Relations

- @sources/gemini-dr-link-eval-2026-04-28.md — Wave 2 (24 URLs) parent of the Gemini DR link-evaluation lineage
- @sources/gemini-dr-wave3-link-eval-2026-04-28.md — Wave 3 (13 URLs) earlier sibling
- @sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md — Wave 4A (30 URLs) immediate predecessor; **Kronos status change**: Wave 4A Defer → Wave 5A Steal-from after deeper evaluation
- @sources/gemini-dr-wave4b-osint-2026-04-29.md — Wave 4B sibling
- @sources/alash3al-stash.md — URL 5 dedicated source page (Adopt tier)
- @sources/shiyu-coder-kronos.md — URL 3 dedicated source page (Steal-from tier; was Defer in Wave 4A)
- @sources/microsoft-qlib.md — Wave 4A Adopt that pairs with Kronos (qlib is the data-prep + backtest harness; Kronos is the foundation-model layer)
- @concepts/wiki-tooling-evaluation.md — wave-evaluation parent for librarian-side findings
- @concepts/ip-sale-readiness.md — license analysis parent; **Apache-2.0 transitive-dependency caveat** surfaces for stash (go.mod) and firnflow (Cargo.lock)
- @concepts/high-signal-paper-patterns.md — rubric used to score the Adopts; informs which to promote to dedicated source pages
- @entities/infrastructure/pgvector.md — stash uses pgvector; current Cemini pgvector deployment is the integration touch-point
- @entities/infrastructure/hetzner.md — CPX21 footprint is the deployment surface for stash on the Wiki/Librarian stack
- @entities/infrastructure/deepseek-api.md — stash MCP integration sits between Cemini's brain (DeepSeek-V4-Flash) and persistent memory

## Raw Concept

- **Original title**: "Cemini Stack & Wiki Stack — Link Evaluation Brief"
- **Source filename**: `Codebase Evaluation for Trading & Wiki 4_30.docx`
- **Type**: User-authored Gemini Deep Research output (docx, 158 paragraphs)
- **Date**: 2026-04-30 EDT (user-authored same day)
- **URL count**: 6 evaluations (smaller, deeper than Wave 4A's 30)
- **Evaluation framework**: 8-section per-URL template (Identity / What it is / Scoring table / Detailed evaluation / Recommendation tier / Risks & caveats / Open questions / Primary sources cited) — consistent with Waves 2/3/4
- **Evaluation surfaces**: Cemini production stack / Wiki/librarian server stack / Workflow
- **Location after ingest**: cemini-librarian:/opt/cemini-bulk/research/Codebase Evaluation for Trading & Wiki 4_30.docx
- **Read status**: read (full text extracted; URL catalog + recommendation tier per URL captured; Adopt + Steal-from URLs anti-hallucination-spot-checked via Exa `crawling_exa`)
- **Discovered via**: User manual drop in inbox 2026-04-30 alongside Wave 5B sibling (Polymarket-cluster focus)
- **Primary clusters**: librarian-tooling, link-evaluation, decision-record

## Narrative

### Recommendation distribution (6 URLs)

| Tier | Count | URLs |
|---|---|---|
| **Adopt** | 1 | stash (5) |
| **Steal-from** | 1 | Kronos (3) [status-change vs Wave 4A Defer] |
| **Reference-only** | 2 | firnflow (1), zeroboot (4) |
| **Reject** | 2 | the_well (2), WorldSeed (6) |
| **Unavailable** | 0 | — |
| total | 6 | |

Adopt rate: 1/6 = **16.7%**. Steal-from rate: 1/6 = **16.7%**. Combined operational adoption (Adopt + Steal-from) = 33% — comparable to Wave 4A's 47% (14/30). The wave was deliberately narrow: only 6 URLs, but each evaluated more deeply than the Wave 4A averages.

### Anti-hallucination spot-check (Adopt + Steal-from)

Per the Wave 2/3/4 protocol, the 2 operationally-relevant URLs were verified via Exa `crawling_exa` against GitHub primary URLs:

| URL | Verdict pre-spot-check | Spot-check result |
|---|---|---|
| URL 5 — alash3al/stash | Adopt | License Apache-2.0 ✅ confirmed file-level + repo-level; **407 stars / 1 contributor**; primary language Go (81.5%); created 2026-04-24, latest release v0.2.6 on 2026-04-26; PostgreSQL+pgvector dependency confirmed; MCP server confirmed; 8-stage consolidation pipeline (episodes → facts → relationships → causal links → confidence decay) confirmed. **Bus-factor: 1 contributor on a 6-day-old repo is the maturity caveat** — fork-and-maintain pattern applies. |
| URL 3 — shiyu-coder/Kronos | Steal-from (Wave 4A Defer) | License MIT ✅ confirmed file-level + repo-level; **22,172 stars / 3,908 forks / 20 contributors**; **AAAI 2026 acceptance** (Nov 2025); arXiv:2508.02739 (Aug 2025); Kronos-mini 4.1M / Kronos-small 24.7M / Kronos-base 102.3M / Kronos-large 499.2M (large not open-source). Decoder-only foundation model on K-line/OHLCV with two-stage tokenizer architecture confirmed. **Major status upgrade vs Wave 4A**: AAAI 2026 acceptance + 22k stars retroactively justify Steal-from over Defer. |

**One material finding beyond drift**:

1. **stash bus-factor + immaturity** — the docx's Adopt verdict is sound IF Cemini commits to the **fork-and-maintain pattern** (clone, pin a commit hash, accept upstream may go stale). 6-day-old repo with 1 contributor is the textbook bus-factor signal. The ~150-200 MB PostgreSQL footprint plus ~50-100 MB Go binary fits within CPX21's 4 GB envelope, but the operational risk is upstream evaporation. Mitigation: pin v0.2.6 (latest), fork to a Cemini-controlled GitHub org, treat as inhouse code from day 1.

2. **Kronos status change rationale** — Wave 4A's Defer was based on "pending peer-reviewed evaluation" + bus-factor concerns. Wave 5A's Steal-from is justified by:
   - **AAAI 2026 acceptance** (Nov 2025; high-prestige peer-reviewed signal)
   - **20 contributors** + **22k stars** (no longer bus-factor)
   - **MIT license repo-level confirmed** (clean for IP-sale readiness target)
   - **Kronos-mini 4.1M params** fits CPU inference on CPX21 if needed (alternative deployment surface)
   - **The tokenizer pattern (continuous OHLCV → discrete tokens)** is the steal-from extract — *not* the Transformer model itself, which the project itself disclaims as "simplified example, not production-ready"
   
   This is a textbook **status-upgrade-on-deeper-evaluation** pattern, mirroring (in opposite direction) the Wave 4A Vibe-Trading downgrade Adopt-Cemini → Steal-from.

### Pre-existing wiki integration

- **URL 3 — Kronos**: Wave 4A indexed as **Defer**. Wave 5A reclassifies as **Steal-from** with deeper analysis. The Wave 4A `gemini-dr-wave4a-cemini-stack-2026-04-29.md` page is updated with this Wave 5 status change (cross-wave reclassification follows the Vibe-Trading pattern from Wave 4A).
- All other URLs are first-evaluation in this session.

### Per-URL summaries — Adopt (1)

**URL 5: alash3al/stash** (`github.com/alash3al/stash`) — Apache-2.0, Go, 407 stars
> Persistent memory layer for AI agents — episodes, facts, working context stored in Postgres+pgvector. Single binary, MCP server included, no cloud required. 8-stage consolidation pipeline: facts → relationships → causal links → goal tracking → failure patterns → hypothesis verification → confidence decay. Each stage processes only new data since last run. **Adopt for Wiki/Librarian server**: deploy as Dockerized systemd service on CPX21, bridge between static llm-wiki-compiler and dynamic Claude Code reasoning. **Partial-fit Cemini production**: replaces simple linear memory in agents/orchestrator.py — but the 8-stage LLM-call pipeline introduces token-cost risk that needs profiling before prod adoption. Workflow Yes-fit: solo-dev Claude Code can connect remotely to CPX21-hosted Stash via MCP. Bus-factor caveat: 6-day-old repo, 1 contributor — **fork-and-maintain pattern strongly recommended**. **Promoted to dedicated source page this session.**

### Per-URL summaries — Steal-from (1)

**URL 3: shiyu-coder/Kronos** (`github.com/shiyu-coder/Kronos`) — MIT, Python, 22k stars, AAAI 2026 [STATUS-CHANGE Defer→Steal-from]
> First open-source foundation model for financial K-line/OHLCV data. Decoder-only Transformer pre-trained on 45+ global exchanges. Two-stage tokenizer architecture: hierarchical discrete tokens via continuous-OHLCV-to-token quantization (Binary Spherical Quantization claimed by docx; tokenizer architecture confirmed by repo). Kronos-mini 4.1M / Kronos-small 24.7M / Kronos-base 102.3M / Kronos-large 499.2M (large not open). **Steal-from extract**: the **KronosTokenizer** pattern (continuous → discrete tokens for financial data). The Transformer itself is disclaimed as "simplified example, not production-ready" by authors; deployment of the model into Cemini's execution path violates the "stability and predictability requirements" of trading. Direct fit: pair Kronos tokenization architecture with Cemini's existing OHLCV pipeline as an experimental signal source, not a primary brain. **Promoted to dedicated source page this session.**

### Per-URL summaries — Reference-only (2)

**URL 1: gordonmurray/firnflow** — Apache-2.0, Rust
> High-performance multi-tenant vector + full-text search engine over object storage (S3, MinIO, R2, Tigris). Foyer hybrid cache for tiered RAM-NVMe-S3 paging. **Cemini production stack Partial-fit**: could replace pgvector in PostgreSQL but requires standing up MinIO/R2 stack. **Wiki/Librarian No-fit**: 4 GB RAM + 80 GB NVMe envelope of CPX21 cannot host the prerequisite S3-compat object store. **Workflow Yes-fit**: architectural blueprint for tiered Rust caching + LanceDB columnar format. **Reference-only**: deploy nothing; study the foyer cache pattern. Open: Cargo.lock audit for transitive AGPL/SSPL via cargo-deny [NEEDS VERIFICATION 2026-04-30].

**URL 4: zerobootdev/zeroboot** — Rust, sub-millisecond VM sandboxes
> Firecracker-snapshot-based mmap'd VM engine for untrusted AI agent code. **Fatal blocker for Cemini**: zero internal networking — agents cannot make API calls. **Wiki/Librarian No-fit**: no dynamic execution surface on CPX21. **Workflow Yes-fit**: educational Rust source on memory snapshot mapping + CSPRNG fork-state hazard pattern. **Reference-only**. Managed API service [RETRACTED 2026-05-17 — the "egress networking on the roadmap" framing was wrong: the managed API (`api.zeroboot.dev`, early-access signup at tally.so/r/aQGkpb) is live, but per zeroboot's own README + docs/ARCHITECTURE.md the no-networking constraint is architectural — forks communicate via 16550 UART serial I/O only, with no outbound network access in either self-hosted or managed mode. The managed service removes infra-management burden, not the networking limitation. Cemini's "agents cannot make API calls" blocker stands.]

### Per-URL summaries — Reject (2)

**URL 2: PolymathicAI/the_well** — 15 TB physics-simulation dataset (numerical physical systems)
> Domain mismatch absolute — financial trading + OSINT vs. spatiotemporal physics. **All three surfaces No-fit**. CPX21's 80 GB NVMe physically cannot host 15 TB. Reject without further verification.

**URL 6: AIScientists-Dev/WorldSeed** — Multi-agent emergent-social-simulation engine, YAML configs
> Non-deterministic architecture conflicts with trading determinism requirements. 12 commits, zero releases — extreme immaturity. WebSockets + uv + multi-process stack incompatible with CPX21's tight envelope. **All three surfaces No-fit**. Reject.

### Cross-wave patterns

1. **Status-upgrade-on-deeper-evaluation** (Kronos Defer → Steal-from) mirrors the Wave 4A Vibe-Trading status-downgrade pattern in opposite direction. **Together they establish**: wave evaluations are not stationary — peer-review acceptance, star-growth, and contributor-base shifts within 1-2 weeks legitimately re-rank tier. Worth treating as a **rolling-re-evaluation policy**: any project whose tier was set with maturity caveats should auto-re-eval on next wave touch.

2. **The fork-and-maintain pattern** continues to apply (stash 1-contributor / 6-day-old). New refinement: even within the Adopt tier, **a maturity-stratified Adopt** distinguishes "Adopt-and-follow-upstream" (qlib 40k stars, Microsoft maintained) from "Adopt-but-fork-and-pin" (stash, polymarket-predictions-mcp from Wave 4A). This stratification belongs in `@concepts/wiki-tooling-evaluation.md`.

3. **License-clean-but-deployment-blocked** (firnflow Apache-2.0 but requires S3 stack; zeroboot networking-blocked) is a recurring "Reference-only" recipe: clean license + sound architecture + missing infra-prerequisite = study, don't deploy. Distinct from poison-pill rejection (LICENSE conflict) and TOS-conflict pattern (Wave 4A tradingview-mcp). New IP-sale-readiness sub-pattern: **infrastructure-prerequisite-block**.

4. **Steal-from-the-tokenizer-not-the-model** (Kronos): the high-value architectural pattern is the OHLCV→discrete-token quantizer, not the Transformer prediction head. This generalizes to a wider Steal-from pattern: when an Adopt candidate has a "production-ready disclaimer" from the authors themselves, the rich extract is usually the upstream component (data preprocessing / tokenization / feature engineering), not the downstream component (the predictor / decision-maker). Fits as a refinement to `@concepts/wiki-tooling-evaluation.md`.

### Open questions / NEEDS VERIFICATION

- **URL 1 firnflow Cargo.lock audit** **`[TENTATIVE 2026-05-29]`** — spot-check of `gordonmurray/firnflow` Cargo.lock (705 crates): no `AGPL`/`GPL`/`SSPL` license fields in lockfile; root Apache-2.0. Full `cargo-deny` sweep still recommended before Workflow extract; Reference-only posture unchanged (S3 prereq block).
- **URL 1 firnflow RAM footprint under load** **`[TENTATIVE 2026-05-29]`** — upstream README benchmarks query latency (S3→72µs warm), not RAM under 130-FastMCP concurrent load; **Reference-only** (S3 prereq) unchanged; soak = internal benchmark.
- **URL 3 Kronos-small CPU latency** **`[TENTATIVE 2026-05-29]`** — Kronos-small **24.7M** params; public demo = 24h BTC forecast, not sub-second execution; **Steal tokenizer only** — CPU P99 trading-path latency unbenchmarked.
- **URL 3 Kronos pyqlib transitive license audit** **`[CONFIRMED 2026-05-29]`** — no `qlib` dependency in `requirements.txt`; GitHub code search returns 0 hits. Default install path is MIT-only (torch/pandas/huggingface); pyqlib gate **closed**.
- **URL 4 zeroboot egress networking roadmap** [RETRACTED 2026-05-17] — there is no egress-networking roadmap item. Zeroboot's no-networking is an architectural property of the CoW-fork model (serial-I/O-only sandboxes); the managed API at `api.zeroboot.dev` does not change it. Verified via zeroboot README + docs/ARCHITECTURE.md (Exa 2026-05-17).
- **URL 5 stash go.mod transitive license sweep** **`[TENTATIVE 2026-05-29]`** — root **Apache-2.0**; direct deps `jackc/pgx` **MIT**, `mark3labs/mcp-go` **MIT** (GitHub API). Formal `go-licenses` sweep still advised before prod pin; Adopt posture for librarian MCP memory unchanged.
- **URL 5 stash token-cost ratio** **`[TENTATIVE 2026-05-29]`** — `consolidate.go` confirms **8 stages** (7 LLM + 1 pure-SQL decay) with `LLMCalls` counter; per-1k-input token ratio still needs Cemini workload measurement.

## Snippets

> **The wave's headline finding (paraphrased)**: 1 Adopt + 1 Steal-from out of 6 evaluable URLs (33% combined operational adoption rate). Anti-hallucination spot-check confirmed both: stash Apache-2.0 + 407 stars + 1 contributor (fork-and-maintain warranted); Kronos MIT + 22k stars + 20 contributors + AAAI 2026 acceptance (status-upgrade Defer → Steal-from since Wave 4A). The wave's signature pattern: deeper evaluation per URL than Wave 4A averages (6 URLs × ~25 paragraphs each).

> **Kronos status-change rationale (URL 3 evaluation excerpt)**:
>
> "Steal-from — Extract the continuous-to-discrete OHLCV tokenization architecture and the PyTorch implementation of the KronosTokenizer. Deploying the actual Transformer model into the production execution stack violates the stability and predictability requirements of the trading platform; the authors explicitly state within the repository documentation that the provided fine-tuning pipeline is a 'simplified example and not a production-ready quantitative trading system.'" [Source: Codebase Evaluation for Trading & Wiki 4_30.docx URL 3]

> **stash adoption rationale (URL 5 evaluation excerpt)**:
>
> "Adopt — Integrate Stash directly into the CPX21 Wiki/Librarian server. Use it to supercharge the solo-developer research workflow via the MCP protocol, while keeping it strictly isolated from the high-frequency Cemini production trading stack. The 8-stage consolidation pipeline (extracting facts, relationships, causal links) bridges the gap between the static llm-wiki-compiler and dynamic Claude Code reasoning." [Source: Codebase Evaluation for Trading & Wiki 4_30.docx URL 5]

> **firnflow architecture (URL 1 evaluation excerpt — explains the Reference-only verdict)**:
>
> "Firnflow's memory profile is highly configurable due to its reliance on the foyer hybrid cache, which intelligently pages data to the NVMe disk and ultimately to S3 to minimize resident RAM. … The prerequisite of standing up an S3-compatible object store (MinIO) on the same Hetzner CPX21 server creates an infrastructure overhead inconsistent with the 'simple, persistent compounding artifact' philosophy of the wiki." [Source: Codebase Evaluation for Trading & Wiki 4_30.docx URL 1]

> **Anti-hallucination protocol — anchoring quote**:
>
> Both Adopt + Steal-from URLs verified via `mcp__exa__crawling_exa`. License confirmed at file + repo level: stash=Apache-2.0, Kronos=MIT. Star counts: stash=407, Kronos=22,172. Contributor counts: stash=1, Kronos=20. Conference acceptance for Kronos: AAAI 2026 (Nov 2025). [Per Exa spot-check 2026-04-30]
