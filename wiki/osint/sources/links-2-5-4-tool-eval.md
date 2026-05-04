---
title: "links 2 5_4 — Primary Software Repositories Evaluation (14 candidates)"
type: source
tags: [llm-agents, dev-tooling, financial-research, audit-security, license-compliance, autoresearch, cemini-internal]
keywords: [tool-evaluation, license-posture, autoresearch-loop, sharpe-as-loss, codegraph, riskfolio-lib, financetoolkit, dual-license-ambiguity, lumibot, mit-vs-gpl]
related:
  - sources/5-4-links-tool-eval.md
  - sources/gemini-sci-research-2602-03837.md
  - sources/more-links-5-2-arch-eval.md
  - sources/links-5-2-tool-eval.md
  - concepts/cemini-license-posture.md
  - concepts/autoresearch-loop-pattern.md
  - entities/tools/codegraph.md
  - entities/tools/leaf.md
  - entities/tools/riskfolio-lib.md
  - entities/tools/financetoolkit.md
  - entities/tools/atlas-gic-autoresearch.md
  - entities/tools/agentic-soc-platform.md
  - entities/infrastructure/yfinance.md
maturity: draft
read_status: deep-read
created: 2026-05-04
updated: 2026-05-04
---

## Relations

- @sources/5-4-links-tool-eval.md — companion 19-tool eval batch ingested same day; together form a 33-tool sweep
- @sources/gemini-sci-research-2602-03837.md — co-ingested methodology paper; Section 2.6 (Agentic Tool-Use & Automated Feedback) is the theoretical analog of atlas-gic's autoresearch loop in this batch
- @sources/more-links-5-2-arch-eval.md — K27 architecture eval; identical 8-section template
- @sources/links-5-2-tool-eval.md — K27 companion 19-tool batch
- @concepts/cemini-license-posture.md — adds **dual-license ambiguity pattern** (Lumibot: README claims MIT, core files labeled GPL-3.0); fifth license-failure mode after K27's three + 5_4-links's CC-BY-NC-data contamination
- @concepts/autoresearch-loop-pattern.md — atlas-gic's Sharpe-as-loss + 25-agent Darwinian debate is the canonical financial-domain instantiation
- @entities/tools/codegraph.md — Adopt-tier; token-efficient AST indexer for Claude Code
- @entities/tools/leaf.md — Adopt-tier; Rust terminal markdown viewer for wiki authoring UX
- @entities/tools/riskfolio-lib.md — Adopt-tier; BSD-3-Clause portfolio optimization for Cemini FastMCP integration
- @entities/tools/financetoolkit.md — Adopt-tier; MIT 150-metric financial library for Cemini FastMCP integration
- @entities/tools/atlas-gic-autoresearch.md — Steal-from-tier; autoresearch loop pattern (NO LICENSE blocks deployment)
- @entities/tools/agentic-soc-platform.md — Steal-from-tier; Redis Stream + LangGraph patterns
- @entities/infrastructure/yfinance.md — already-existing entity page; this batch reaffirms the polygon-doctrine fallback positioning

## Raw Concept

- Original title: "Evaluation of Primary Software Repositories for Cemini, Wiki, and Workflow Architectures" (Gemini Deep Research output)
- Author: Gemini Deep Research (one-shot evaluation of 14 user-supplied URLs)
- Type: docx (Cemini-internal architecture evaluation)
- Location: cemini-librarian:/opt/cemini-bulk/research/links 2 5_4.docx
- Retrieved: 2026-05-04
- Length: ~3.0 MB, 14 candidates evaluated using identical 8-section template
- Read status: deep-read

## Narrative

Companion to `@sources/5-4-links-tool-eval.md` ingested same day. Skewed toward financial-research libraries (Riskfolio-Lib, FinanceToolkit, Lumibot, backtrader, QuantConnect/Lean, yfinance, atlas-gic) and developer-workflow tooling (codegraph, leaf, repowise, shannon). Six of fourteen target the Cemini production stack directly; the eight others target the workflow layer.

**Prediction-market scope** (added 2026-05-04 per user note): the financial libraries here (Riskfolio-Lib for HRP/Kelly, FinanceToolkit for 150 metrics) generalize directly to prediction-market position-sizing and risk modeling (Kalshi + Polymarket support sports, healthcare/biotech, politics, weather, economic indicators). atlas-gic's autoresearch loop is explicitly trading-oriented and applies as cleanly to prediction markets as to equities — Sharpe-as-loss is venue-agnostic. probablyprofit (in 5_4-links companion) is already prediction-market-native (Polymarket).

**Recommendation distribution:**

| Tier | Count | Items |
|------|-------|-------|
| **Adopt** | 4 | colbymchenry/codegraph (MIT — Node + SQLite + tree-sitter, 19+ language AST indexer for Claude Code token efficiency), RivoLink/leaf (MIT — Rust terminal markdown viewer with watch mode, LaTeX + YAML rendering), dcajasn/Riskfolio-Lib (BSD-3-Clause — C++/Fortran/Python convex optimization with 24 risk measures incl. Kelly + HRP), JerBouma/FinanceToolkit (MIT — 150 metrics incl. Extended DuPont, GARCH, VaR, Ulcer Index) |
| **Steal-from** | 2 | FunnyWolf/agentic-soc-platform (MIT — Redis Stream + LangGraph multi-agent pattern, security domain mismatch but architectural-fit identical), chrisworsey55/atlas-gic (NO LICENSE — autoresearch loop with rolling Sharpe ratio as objective, 25-agent Darwinian debate, git-tracked prompt evolution) |
| **Reference-only** | 3 | KeygraphHQ/shannon (AGPL-3.0 + proprietary tier — Claude Agent SDK parallel-orchestration reference, no execution allowed), repowise-dev/repowise (AGPL-3.0 + dual-license — Tree-sitter + Leiden + PageRank for code intelligence, methodology only), QuantConnect/Lean (Apache-2.0 — C# event-driven engine, 13k+ commits institutional reference, stack mismatch) |
| **Defer** | 2 | Lumiwealth/lumibot (DUAL-LICENSE AMBIGUITY MIT vs GPL-3.0 — perfect Cemini structural match but legally fraught), ranaroussi/yfinance (Apache-2.0 — already in use as polygon-doctrine fallback, scraping fragility blocks production primary use) |
| **Reject** | 3 | webxos/phalanx (NO LICENSE + opaque + obscure 1-week-old project), zakirkun/deep-eye (MIT but abandoned at 14 commits + offensive-security domain irrelevance), mementum/backtrader (GPL-3.0 + legacy pandas/matplotlib, modern Polars supersedes) |

**Critical findings:**

### 1. atlas-gic autoresearch loop is the highest-leverage architectural pattern in this batch

`chrisworsey55/atlas-gic` implements an end-to-end autoresearch loop: 25 LLM agents stratified across 4 hierarchical layers, each representing a distinct investment psychology, debating live trades. The system:

1. Identifies the worst-performing agent based on rolling Sharpe ratio
2. Prompts a meta-LLM to rewrite that agent's system instructions
3. Git-tracks the rewrite as a commit
4. If subsequent live performance degrades, automatically reverts via `git reset`
5. If improved, weights the agent's vote more heavily on subsequent decisions

This is a **financial-domain instantiation of the Gemini paper's Section 2.6 (Agentic Tool-Use & Automated Feedback)** — both have an LLM proposing, an objective function judging, and automated state mutation/rollback. The Gemini paper validates the pattern in mathematical proof construction (numerical traceback as feedback); atlas-gic validates it in trading (Sharpe ratio as feedback).

**Direct relevance to Conductor**: Conductor v0.1.1 currently uses A/B taxonomy-routing with manual `--build-priors`. The atlas-gic pattern suggests a future evolution where agent selection itself is autoresearch-driven rather than human-tuned. See `@concepts/autoresearch-loop-pattern.md` for synthesis.

**Blocker**: NO LICENSE on the atlas-gic repo. Per `@concepts/cemini-license-posture.md` audit rule, this is REJECT for code reuse. The pattern can be re-implemented from scratch (clean-room) inspired by the architecture description in the Gemini DR eval, but no atlas-gic code itself can land in Cemini.

### 2. Lumibot introduces a fifth license-failure pattern (dual-license ambiguity)

`Lumiwealth/lumibot` README aggressively advertises MIT licensing (likely positioning against GPL-3.0 backtrader), but specific core repository files explicitly carry GPL-3.0 headers. This **dual-license ambiguity** is a new failure mode beyond K27's three + the CC-BY-NC-data-contamination pattern from 5_4-links:

| # | Pattern | First seen | Mitigation |
|---|---------|------------|------------|
| 1 | NO LICENSE → default copyright | K27 (multiple) | Audit rule: REJECT until upstream LICENSE clarified |
| 2 | AGPL network-clause Docker-defeat | K27 (SocratiCode) | Reject for any networked deployment; allow only as static reference reading |
| 3 | GPL-3.0 LLM-agent derivative-work | K27 (freqtrade, qb-core) | Quarantine agents — never feed GPL source to coding agents writing into Cemini |
| 4 | CC-BY-NC training-data contamination | 5_4-links (tennis_atp + tennis_match_prediction) | Extract algorithm only; retrain against commercially-licensed data |
| 5 | **Dual-license MIT-vs-GPL ambiguity** | **links-2-5_4 (Lumibot)** | **File-by-file legal audit before any import; default-Reject pending clarification** |

Update `@concepts/cemini-license-posture.md` accordingly.

### 3. Riskfolio-Lib + FinanceToolkit are immediate Cemini-FastMCP integration candidates

Both libraries are pure-Python (or C++/Fortran-bound via Python), permissively licensed (BSD-3-Clause + MIT), and architecturally orthogonal:

- **Riskfolio-Lib**: 24 convex risk measures (HRP, Black-Litterman, Kelly), CVXPY-based, integrates as `@mcp.tool` for the DeepSeek brain to query position-sizing math at decision time. Caveat: LICENSE-XL.txt file flagged as "presence noted" — needs verification before commit.
- **FinanceToolkit**: 150 financial metrics standardized across data vendors. Integrates as `@mcp.tool` for fundamental analysis — Extended DuPont, GARCH volatility, VaR, Ulcer Index. Caveat: native Yahoo Finance integration must be force-replaced with Alpaca/FMP feeds per polygon-doctrine.

**Action item**: stage briefs for both as `briefs/2026-05-04_*-fastmcp-integration.md` for the prod-server-side Claude session.

### 4. codegraph + leaf are workflow-layer wins for the laptop side

- **codegraph** (MIT, Node + SQLite + tree-sitter): pre-indexes the local Cemini codebase (Python, TypeScript, etc.) and exposes call-graph structure to Claude Code, eliminating blind file scans. Direct token-efficiency win for `services/llm_analyst/` development sessions. Install via `npm install -g`. .gitignore the SQLite indices.
- **leaf** (MIT, Rust): terminal markdown viewer with watch mode, renders LaTeX + YAML frontmatter live. Runs alongside Claude Code while editing wiki pages — instant visual feedback for cross-link integrity and equation rendering before invoking `wiki_lint.py`.

Both are laptop-only tools; neither belongs on the librarian or production hosts.

### 5. yfinance positioning reaffirmed

This batch's evaluation of yfinance independently arrives at the **polygon-doctrine** position recorded in user memory: yfinance is acceptable as a research-side fallback (laptop, ad-hoc backtesting), explicitly **not** acceptable as production primary ingestion (Yahoo's undocumented API + scraping fragility + IP rate-limiting risk). No change to current usage required.

### Architectural patterns worth extracting

- **atlas-gic autoresearch loop with Sharpe-as-loss** → Conductor evolution candidate (clean-room re-implementation given NO LICENSE)
- **agentic-soc-platform Redis Stream + LangGraph patterns** → harden Cemini's `agents/orchestrator.py` queue handling
- **shannon parallel-orchestration patterns** (AGPL — read-only) → reference for multi-agent state management
- **repowise PageRank + Leiden community detection** (AGPL — read-only) → reference for code-intelligence scoring algorithms
- **codegraph SQLite + tree-sitter pattern** → already adopted; clean architectural prototype

## Snippets

- **atlas-gic autoresearch mechanics**: "iteratively refine live trading strategies... a continuous 'autoresearch' loop... isolating the worst-performing agent based strictly on real-world market outcomes—specifically measured by the rolling Sharpe ratio—and prompting the overarching LLM to fundamentally rewrite that agent's internal system instructions... a git-tracked evolutionary history where successful prompt modifications are permanently committed, and failures are automatically reverted via git reset, leveraging Darwinian scoring methodologies to shift capital weighting dynamically across the artificial swarm." [Source: links 2 5_4.docx URL 9]

- **Lumibot license ambiguity**: "Highly ambiguous and conflicting. Documentation prominently advertises License: MIT, but the core repository files (like the README) are explicitly labeled with License: GPL-3.0." [Source: links 2 5_4.docx URL 7]

- **codegraph token-efficiency claim**: "fundamentally eliminates the need for agents to blindly scan files, drastically reducing token consumption and accelerating architectural exploration." [Source: links 2 5_4.docx URL 3]

- **leaf rendering scope**: "successfully rendering LaTeX mathematical formulations, YAML frontmatter data, multi-tiered tables, and syntax-highlighted code blocks directly into the terminal." [Source: links 2 5_4.docx URL 4]

- **agentic-soc-platform stack alignment**: "The integration of a purely Python environment, LangGraph orchestration, and a Redis message queue perfectly mirrors the exact infrastructure Cemini utilizes for processing high-velocity, 24/7 cryptocurrency market intelligence." [Source: links 2 5_4.docx URL 5]

- **Riskfolio-Lib scope**: "24 distinct convex risk measures, ranging from basic standard deviation and Maximum Drawdown to highly advanced concepts like the Kelly Criterion and Hierarchical Risk Parity (HRP)... commercial-grade and open-source solvers (e.g., MOSEK, CLARABEL, CVXPY)." [Source: links 2 5_4.docx URL 12]

- **FinanceToolkit scope**: "highly transparent, standardized calculations for over 150 unique financial metrics, fundamental ratios, and complex risk indicators... Extended DuPont Analysis... Value at Risk, GARCH volatility modeling, Ulcer Index." [Source: links 2 5_4.docx URL 14]

- **repowise token-reduction claim**: "a benchmarked 209x mean reduction in required tokens when analyzing complex repositories" via Tree-sitter + Leiden + PageRank — but AGPL-3.0 + dual-licensing target enterprise SaaS. Reference-only. [Source: links 2 5_4.docx URL 6]

- **shannon scale signal**: "approximately 41.2k stars and a documented history of 235 commits" — extremely high signal but AGPL-3.0 (Lite) + proprietary (Pro) blocks deployment. [Source: links 2 5_4.docx URL 2]

## Dead Ends

*(none yet — first ingest of this source.)*
