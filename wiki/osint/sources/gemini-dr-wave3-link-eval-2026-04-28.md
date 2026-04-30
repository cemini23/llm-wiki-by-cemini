---
title: Gemini Deep Research — Link Evaluation Wave 3 2026-04-28 (13 URLs)
type: source
tags: [gemini-deep-research, link-evaluation, cemini-stack, librarian-server, ip-sale-readiness, license-audit, anti-hallucination, options-pricing, prompt-optimization]
keywords: [black-scholes-implied-volatility, gepa, build-your-own-openclaw, openclaude, tradingview-api, memoria, machine-learning-for-trading, warp, mesa-filesystem, markdownfs, hidemyemail, schadner-iv-formula, prompt-mutation]
related:
  - sources/gemini-dr-link-eval-2026-04-28.md
  - sources/black-scholes-iv-explicit-schadner-2026.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/librarian-server-architecture.md
  - concepts/ip-sale-readiness.md
  - concepts/scatter-gather-topology.md
  - concepts/ai-organisation-design.md
  - concepts/options-derivatives.md
  - sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md
  - sources/gemini-dr-wave4b-osint-2026-04-29.md
maturity: validated
created: 2026-04-29
updated: 2026-04-30
clusters: [llm-agents, librarian-tooling, decision-record, options-pricing]
---

## Relations

- @sources/gemini-dr-link-eval-2026-04-28.md — Wave 2 canonical (24 URLs, ingested 2026-04-28). Wave 3 follows the same 9-step protocol Wave 2 codified. Bridge link
- @sources/black-scholes-iv-explicit-schadner-2026.md — dedicated source page for the Adopt-tier arxiv paper (URL 12 of this wave); paper-level deep-read warrants its own page
- @concepts/wiki-tooling-evaluation.md — parent decision document; gains a "Wave 3 — Gemini DR findings" section on this same indexing pass
- @concepts/librarian-server-architecture.md — Wave 3 happens AFTER Phase 2 (wiki sync), Phase 3 (compiler stack install), Phase 3.5 (Option C swap to kb-server). Storage migration also landed in this same session. Wave 3 ingestion exercises the new ingest doctrine (raw layer → librarian)
- @concepts/ip-sale-readiness.md — Wave 3 confirms reject-family extension on multiple axes: warp = AGPL-3.0 (confirmed); openclaude = **self-disclosed unauthorized derivative of Anthropic proprietary code** (LICENSE-file-inspected 2026-04-29 — flipped from `HALT-PENDING-LICENSE` to outright `REJECT`); reinforces the IP-sale license-discipline arc with a new poison-pill pattern (vendor-IP-redistribution-without-authorization, distinct from copyleft poison-pills)
- @concepts/scatter-gather-topology.md — `build-your-own-openclaw` Steal-from extracts multi-agent routing and scheduled-cron heartbeat patterns relevant to the LangGraph orchestrator's evolution
- @concepts/ai-organisation-design.md — `Memoria` (Steal-from) introduces "Git for AI" branching/merging memory pattern; complementary to OMC's E²R tree search but at the memory layer rather than the strategy layer
- @concepts/options-derivatives.md — direct relevance: arxiv 2604.24480 explicit Black-Scholes IV closed-form formula is a compute-cycle accelerator for any options-pricing pipeline using this concept

## Raw Concept

- **Original title**: "Cemini Stack & Wiki Stack — Link Evaluation Brief" (continuation; same title as Wave 2)
- **Author/runtime**: Gemini Deep Research (Gemini 2.5 Deep Research mode)
- **Type**: Deep-research report (paste-into-Gemini brief response)
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/Evaluating Code for Trading & Wiki Stacks.docx` (54 KB, 539 lines text-extracted; moved per new ingest doctrine 2026-04-29)
- **Retrieved**: 2026-04-28 (Gemini search date); ingested 2026-04-29
- **Pages / length**: 539 lines / 13 URL evaluations (2 unavailable) + Final Summary Table + 34 works-cited
- **Read status**: deep-read (full ingest 2026-04-29)
- **Upstream prompt**: same brief structure as Wave 2 (`briefs/2026-04-28_gemini-deep-research-link-evaluation-prompt.md`, gitignored)

This source records the third wave of Gemini Deep Research output evaluating 13 candidate URLs against the same three target surfaces (Cemini production stack / Wiki+librarian server / Workflow). Wave 3 was originally checked mid-session for relevance to the Option C decision (which MCP server to serve our nested wiki); the conclusion was that **none of the 13 URLs solved the nested-wiki MCP serving problem**, validating the kb-server adoption decision. Wave 3 then proceeded as its own indexing pass, producing one Adopt-Cemini-Wiki-Workflow finding (the Black-Scholes IV explicit formula paper) and one Adopt-Workflow-pending-license-clarification (`openclaude`) which was subsequently `[REJECTED 2026-04-29]` after manual LICENSE-file inspection revealed self-disclosed unauthorized redistribution of Anthropic proprietary code.

## Narrative

### Why this matters

Wave 3 is smaller (13 URLs vs Wave 2's 24) and lower-yield (1 clean Adopt + 1 license-blocked Adopt vs Wave 2's 2 Adopt-for-Cemini + 6 Adopt-for-Workflow). But it surfaces one **structurally important** Cemini-stack finding — a published 2026 paper claiming a closed-form solution to a 50-year-old problem in option pricing — which is worth a dedicated source page on its own (`@sources/black-scholes-iv-explicit-schadner-2026.md`).

Wave 3 also serves as the first **stress test of the new ingest doctrine** (raw layer migrated to librarian per the same-session storage migration): the docx itself was scp'd to `cemini-librarian:/opt/cemini-bulk/research/` rather than living locally on the laptop.

### Recommendation summary table

| URL | Recommendation tier | Cemini fit | Wiki fit | Workflow fit | License | Source page |
|---|---|---|---|---|---|---|
| google/skills | UNAVAILABLE | — | — | — | — | (this page only) |
| rtunazzz/hidemyemail-generator | Reference-only | ⚠️ | ❌ | ✅ | MIT | (this page only — niche operational utility, last release Apr 2024) |
| gepa-ai/gepa | Steal-from | ⚠️ | ❌ | ✅ | MIT (Exa-verified 3836 ★) | (this page only — extract `dspy.GEPA` methodology, run laptop-only for prompt optimization) |
| czl9707/build-your-own-openclaw | Steal-from | ✅ | ❌ | ✅ | MIT (Exa-verified 1284 ★) | (this page only — extract Phase-3 multi-agent routing + Phase-4 concurrency patterns to LangGraph orchestrator; skip LiteLLM dependency) |
| subramanya1997/markdownfs | **Reject** | ❌ | ⚠️ | ❌ | License unverified (auto-reject), Rust in-memory VFS | (this page only — license + RAM risk + zero-utility) |
| Mesa filesystem | Reference-only | ❌ | ❌ | ✅ | proprietary cloud SaaS | (this page only — read blog for "agent scratchpads as branched filesystems" pattern; do not adopt SDK) |
| warpdotdev/warp | Reference-only | ❌ | ❌ | ✅ | **AGPL-3.0 confirmed (Exa)** | (this page only — laptop-local terminal acceptable; banned from server tier per AGPL reject family) |
| **Gitlawb/openclaude** | **REJECT** `[2026-04-29 — LICENSE-FILE INSPECTED]` | ❌ | ❌ | ❌ | **Unauthorized derivative of Anthropic proprietary code (self-disclosed)** | (this page only — IP-sale poison-pill family confirmed) |
| Mathieu2301/TradingView-API | Steal-from | ❌ | ❌ | ✅ | ISC per Gemini; Exa metadata silent (likely package.json-only) | (this page only — reverse-engineer Python websockets from JS source; TOS-violating, do not deploy) |
| matrixorigin/Memoria | Steal-from | ❌ | ❌ | ✅ | Apache-2.0 (Exa-verified 206 ★) | (this page only — extract `branch_id` + `parent_commit` schema for PostgreSQL; MatrixOne dependency too heavy for our hardware) |
| molab.marimo.io | UNAVAILABLE | — | — | — | — | (this page only) |
| **arxiv 2604.24480 — Schadner IV explicit formula** | **Adopt-Cemini-Wiki-Workflow** | ✅ | ✅ | ✅ | CC BY 4.0 | `@sources/black-scholes-iv-explicit-schadner-2026.md` |
| stefan-jansen/machine-learning-for-trading | Steal-from (with staleness flag) | ✅ | ✅ | ✅ | MIT per Gemini (Apache-2.0 in Exa metadata; needs LICENSE-file inspection); 17061 ★, **last push 2024-08-18** | (this page only — extract `04_alpha_factor_research` + `24_alpha_factor_library` modules; explicit framework-obsolescence flag — pandas 1.0 / TF 2.2 era) |

**Counts (revised 2026-04-29 post-openclaude LICENSE inspection)**: Adopt-Cemini-Wiki-Workflow = 1 (arxiv paper); Steal-from = 5 (gepa, build-your-own-openclaw, TradingView-API, Memoria, ml-for-trading); Reference-only = 3 (hidemyemail, Mesa, warp); **Reject = 2** (markdownfs license-unverified Rust VFS; openclaude unauthorized derivative); Unavailable = 2.

### Anti-hallucination spot-check (Exa `crawling_exa` 2026-04-29)

Per the protocol codified at `@sources/gemini-dr-link-eval-2026-04-28.md`, all Adopt + Steal-from URLs were batched-crawled. **Two material findings beyond simple drift**:

| Repo | Gemini's claim | Exa-confirmed | Verdict |
|---|---|---|---|
| gepa-ai/gepa | MIT, 4.1k ★ | MIT, 3836 ★ (~7% drift) | ✅ |
| czl9707/build-your-own-openclaw | MIT, no count | MIT, 1284 ★ | ✅ |
| **Gitlawb/openclaude** | "NOT FOUND — flag for follow-up", 24.9k ★ | **`Other (NOASSERTION)` — GitHub couldn't auto-detect SPDX**, 24794 ★ (~0.4% drift) | ⚠️ **Adoption HALTED until LICENSE file inspected** |
| Mathieu2301/TradingView-API | ISC (per package.json), 3.3k ★ | License field empty in repo metadata; need package.json for ISC; 3214 ★ | ⚠️ Steal-from-only mitigates the ambiguity |
| matrixorigin/Memoria | Apache-2.0, 212 ★ | Apache-2.0, 206 ★ | ✅ |
| **stefan-jansen/machine-learning-for-trading** | MIT (per code-file inspection), 17.2k ★ | License metadata silent at repo level; 17061 ★, **last push 2024-08-18** (~20 months stale) | ⚠️ Steal-from with framework-obsolescence flag is correct |
| arxiv 2604.24480 | CC BY 4.0, paper exists | Title + abstract verified: "An Explicit Solution to Black-Scholes Implied Volatility" | ✅ Paper exists; license assumption (CC BY 4.0) standard for arxiv |
| warpdotdev/warp | AGPL-3.0 (bulk) + MIT (UI crates) | **AGPL-3.0** (repo-level badge) | ✅ Reject-family confirmed |

**Spot-check verdict**: Gemini's primary-source citations held except for two cases where Exa added material clarity:
- `openclaude` license is genuinely ambiguous (`NOASSERTION`) — confirmed not safe to adopt without manual LICENSE-file inspection
- `machine-learning-for-trading` is significantly stale (~20 months) — Steal-from is right, deploying the codebase verbatim would be a maintenance disaster

### Top-tier finding — **Adopt-Cemini-Wiki-Workflow**

**arxiv 2604.24480 — Schadner Black-Scholes IV explicit formula** (CC BY 4.0, University of Liechtenstein, 27 Apr 2026)

Closed-form solution to Black-Scholes Implied Volatility — claimed to be the first explicit formula in 50 years. Reframes the call price as the survival probability of an inverse Gaussian distribution; inverting the identity yields IV via a single quantile-function call. **Numerical tests in the paper claim 3.4× speedup vs Newton-Raphson / Brent's method** at machine-precision accuracy.

- **Cemini-fit ✅**: replace `scipy.optimize.brentq` calls in `services/quant/volatility_surface.py` with vectorized NumPy/Polars implementation. Frees CPU cycles on the GIL-bound CPU-only Hetzner host. Zero new dependencies.
- **Wiki-fit ✅**: paper itself becomes a permanent source page (`@sources/black-scholes-iv-explicit-schadner-2026.md`) — canonical reference for any future options-pricing concept page.
- **Workflow-fit ✅**: standalone read for the developer's quant-research sessions.
- **Risks**: floating-point precision at extreme boundaries (deep OTM near expiry — inverse Gaussian distributions hit underflow). Comprehensive unit tests required before production swap.
- **Verification gate**: empirical 3.4× speedup against Cemini's specific Polygon options chains under Polars architecture (paper's claim must be reproduced before deploying).

This is the wave's headline finding — see `@sources/black-scholes-iv-explicit-schadner-2026.md` for the dedicated deep-read.

### **REJECT** finding — `[RESOLVED 2026-04-29 — LICENSE-FILE INSPECTED]`

**Gitlawb/openclaude** — outright reject after manual LICENSE-file inspection.

**Background**: 24,794 ★, MCP-native, 200+ model routing. Wave 3 evaluation flagged `license = NOASSERTION` per GitHub's SPDX auto-detector and queued LICENSE-file inspection as the adoption gate.

**Inspection result (2026-04-29 via Exa `crawling_exa` against the raw LICENSE file URL)**: The LICENSE file is **self-disclosed unauthorized derivative work** of Anthropic's proprietary Claude Code source. Verbatim:

> "The original Claude Code source is proprietary software: Copyright (c) Anthropic PBC. All rights reserved. Subject to Anthropic's Commercial Terms of Service. Modifications and additions by OpenClaude contributors are offered under the MIT License where legally permissible: …  **The underlying derived code remains subject to Anthropic's copyright. This project does not have Anthropic's authorization to distribute their proprietary source. Users and contributors should evaluate their own legal position.**"

This is NOT a license-ambiguity problem — it's a copyright-redistribution problem. The repository explicitly admits to redistributing Anthropic's proprietary source without authorization. The MIT-licensed-modifications-only framing is a paper veneer; the underlying base is unauthorized.

**Decision: REJECT**. Do not install on laptop, librarian, or production server. Do not extract patterns. The legal exposure for Cemini's IP-sale-readiness posture is unacceptable — an institutional acquirer's IP-due-diligence team would flag any project that touched openclaude as potentially complicit in copyright infringement of Anthropic's source, even if openclaude itself is the immediate liability bearer.

**New license poison-pill pattern surfaced 2026-04-29**: vendor-IP-redistribution-without-authorization. Distinct from copyleft poison-pills (GPL/AGPL/SSPL/PolyForm-Noncommercial/ELv2 — all of which are LEGITIMATE licenses with viral-or-restrictive terms). This new pattern is a project disclosing its own copyright-infringement exposure in its LICENSE file. Filed as a reject-family addition to `concepts/ip-sale-readiness.md`.

**Lesson**: NOASSERTION + repository-name retaining a trademarked term ("openclaude" → Anthropic's "Claude" trademark) → manual LICENSE inspection mandatory before adoption. Gemini's halt-flag was correct; the spot-check protocol surfaced the issue exactly as designed.

**Continued workflow**: stock Anthropic Claude Code remains the laptop CLI. No vendor-Anthropic-decoupling on the laptop side from this wave.

### Steal-from register (5 entries)

These ship as patterns into Cemini-stack code or laptop-side tooling, no dedicated source pages:

1. **gepa-ai/gepa** (MIT, 3836 ★) — `dspy.GEPA` reflective prompt-mutation framework. **Use case**: laptop-side execution to mathematically pre-compute optimal prompts for LangGraph nodes. Hardcode results into `agents/orchestrator.py`. Production execution rejected (latency + token-budget violations).

2. **czl9707/build-your-own-openclaw** (MIT, 1284 ★) — 18-step tutorial transitioning from synchronous chat → event-driven WebSocket → multi-agent routing → cron-scheduled heartbeats. **Use case**: extract Phase-3 routing + Phase-4 concurrency patterns into Cemini's LangGraph StateGraph; skip the LiteLLM abstraction (Cemini uses DeepSeek directly via OpenAI-compatible).

3. **Mathieu2301/TradingView-API** (ISC, 3214 ★) — JS Node.js client emulating TradingView's WebSocket protocol. **Use case**: reverse-engineer the JS protocol logic; rewrite as Python `websockets`/`httpx` module in `services/ingest/tradingview_websocket.py`. **Caveat**: Active TOS-violation territory — institutional acquirer flag if deployed against TradingView.

4. **matrixorigin/Memoria** (Apache-2.0, 206 ★) — "Git for AI" memory layer with `branch_id`/`parent_commit` semantics over MatrixOne HTAP database. **Use case**: extract the schema concept (add `branch_id` and `parent_commit` columns to LangGraph state-tracking PostgreSQL tables); skip MatrixOne dependency entirely. Cheaper than full adoption; preserves git-style memory branching capability.

5. **stefan-jansen/machine-learning-for-trading** (MIT per file-level inspection, 17061 ★) — Stefan Jansen's textbook codebase, 100+ alpha factors, 150+ Jupyter notebooks. **Use case**: strip-mine `04_alpha_factor_research` and `24_alpha_factor_library` modules; transcribe pandas-1.0 → Polars LazyFrames. **Caveat**: framework-obsolescence is severe — last push 2024-08-18, anchored to TF 2.2 / pandas 1.0. Extract the math, NOT the code.

### Reject — license poison-pill confirmed

- **warpdotdev/warp** (AGPL-3.0) — strict reject-list family confirmed via Exa's repo-level license badge. Laptop-local terminal use is permissible (the laptop is dev infra, not in M&A scope), but any inclusion in the production trading stack or librarian server would trigger AGPL viral provisions. Workflow tier is `Reference-only` — approved for laptop, banned from server.

- **subramanya1997/markdownfs** (license unverified, Rust in-memory VFS for markdown) — auto-rejected on missing LICENSE plus orthogonal architecture (in-memory VFS doesn't solve any wiki-serving problem we have; kb-server already does this).

### Reference-only — laptop or pattern-study only

- **rtunazzz/hidemyemail-generator** (MIT, 451 ★, last release Apr 2024) — niche utility for Apple HideMyEmail burner generation; useful only if vendor email blocking becomes a research-bottleneck. Last release ~2 years stale.
- **Mesa filesystem** (proprietary cloud SaaS, "early access" tier) — read for "branched filesystem for agents" architectural pattern; reject the SaaS dependency.

### Wave 3's effects on the project trajectory

**For Cemini production stack**: 1 high-impact adoption candidate (Schadner IV formula) — high-confidence implementation target with measurable success criteria (3.4× speedup verification). 5 Steal-from patterns add to the implementation backlog.

**For the laptop workflow**: 1 license-blocked adoption candidate (openclaude). 1 Reference-only (warp).

**For the librarian server**: nothing directly. None of the 13 URLs compete with kb-server (already adopted in Option C earlier this session). Memoria is the closest in spirit but is a memory-versioning layer, not a wiki-MCP-server.

**For IP-sale-readiness**: confirms AGPL-3.0 reject extension (warp) and adds a new evaluation pattern (license=NOASSERTION → halt, like openclaude). Reinforces the discipline; doesn't change the policy.

**For the `wiki-tooling-evaluation` concept page**: gains a "Wave 3 — Gemini DR findings" section (this same indexing pass).

### Risks & limitations of this Wave 3 evaluation

1. **Smaller wave; lower yield**. 13 URLs / 1 clean Adopt is materially less productive than Wave 2's 24 URLs / 2 Adopts. Worth tracking whether Gemini DR's effective utility scales linearly or hits diminishing returns at this domain density.
2. **Two URLs unavailable** (google/skills + molab) — same pattern as Wave 2 (~8% unavailable rate).
3. **License ambiguity surfaced for two repos** (`openclaude`, `machine-learning-for-trading`) — Gemini's evaluation flagged both manually; Exa confirmed both. The 9-step protocol caught these correctly.
4. **arxiv paper claim** is unverified empirically. The 3.4× speedup needs reproduction against Cemini's specific Polars + Polygon data before any production swap.
5. **Wave 3 evaluation date 2026-04-28; ingest date 2026-04-29** — note the date discrepancy. Filename + content references use 2026-04-28 (Gemini search date); page frontmatter `created`/`updated` use 2026-04-29 (page-authoring date). Same convention as Wave 2.

## Snippets

> "Adopt — Immediate action is required. Translate the explicit mathematical formula into highly optimized, vectorized NumPy/Polars code and deploy it into the quantitative pipeline to capture the 3.4x compute cycle savings. Simultaneously, process the paper into the Wiki to serve as the new canonical truth for all future options pricing operations." [Source: Gemini DR Wave 3, URL 12 (arxiv 2604.24480)]

> "Steal-from — Do not deploy the evolutionary loop into the production servers. Instead, utilize the dspy.GEPA prompt mutation methodology strictly offline on the developer laptop. Execute the optimization framework during algorithm design phases, extract the resulting high-performance prompts, and hardcode them into the Cemini production codebase." [Source: Gemini DR Wave 3, URL 3 (gepa-ai/gepa)]

> "Steal-from — Do not adopt the underlying repository or attempt to provision its massive database dependency. Instead, extract and implement the abstract software concept: append a 'branch_id' and 'parent_commit' logical column to the existing PostgreSQL tracking tables where the LangGraph orchestrator already persists its intermediate states. This strategic addition grants the Cemini stack 'Git-like memory' capabilities utilizing the highly optimized database engine it already possesses." [Source: Gemini DR Wave 3, URL 10 (matrixorigin/Memoria)]

> "Reference-only — Approved strictly for localized laptop usage to accelerate the developer's operational efficiency. It is entirely banned from deployment anywhere near the Hetzner production or librarian servers." [Source: Gemini DR Wave 3, URL 7 (warp) — AGPL-3.0 license-poison-pill confirmation]

> "Adopt — Install the application exclusively on the developer laptop to unify the local workflow's LLM interaction with the DeepSeek API utilized in production, successfully circumventing Anthropic vendor lock-in. Ensure the tool remains entirely off the Hetzner server infrastructure." [Source: Gemini DR Wave 3, URL 8 (openclaude) — adoption HALT-PENDING-LICENSE-CLARIFICATION 2026-04-29 per Exa license=NOASSERTION confirmation]
