---
title: "Evaluating Links for Trading and Wiki Stacks — 27-Tool Infrastructure & Integration Audit"
type: source
tags: [tool-evaluation, trading, wiki, architecture, licensing, cemini-stack]
keywords: [pandas-ta, spec-kit, tradingview-mcp, tech-debt, claude-mem, revpdf, codeboarding, deepteam, browserbase, agentskillos, vectorbt, tracecat, karpathy-wiki, polybot, spj]
related:
  - concepts/tool-evaluation-framework.md
  - entities/tools/pandas-ta-classic.md
  - entities/tools/github-spec-kit.md
  - entities/tools/tradingview-mcp.md
  - entities/tools/tech-debt-skill.md
  - entities/tools/claude-mem.md
  - entities/tools/revpdf.md
  - entities/tools/codeboarding.md
  - entities/tools/deepteam.md
  - entities/tools/browserbase-skills.md
  - entities/tools/agentskillos.md
  - entities/tools/stirling-pdf.md
  - entities/tools/llmfit.md
  - entities/tools/claude-managed-agents.md
  - entities/tools/public-apis-list.md
  - concepts/split-panel-jackknife-spj.md
  - sources/ssrn-4943355.md
maturity: validated
read_status: deep-read
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@entities/tools/pandas-ta-classic.md` — Adopt: 252 technical indicators, Pandas-native
- `@entities/tools/github-spec-kit.md` — Adopt: spec-driven development for wiki→code bridge
- `@entities/tools/tradingview-mcp.md` — Adopt: MCP server for TradingView data
- `@entities/tools/tech-debt-skill.md` — Adopt: Claude Code skill for codebase audit
- `@entities/tools/claude-mem.md` — Adopt: persistent context across sessions
- `@entities/tools/revpdf.md` — Adopt: lightweight offline PDF editor
- `@entities/tools/codeboarding.md` — Adopt: automated architecture diagramming
- `@entities/tools/deepteam.md` — Steal-from: LLM guardrail classifiers
- `@entities/tools/browserbase-skills.md` — Steal-from: Playwright-based browser automation patterns
- `@entities/tools/agentskillos.md` — Steal-from: skill retrieval algorithm
- `@concepts/split-panel-jackknife-spj.md` — Steal-from: SPJ econometric method from URL 27
- `@entities/tools/stirling-pdf.md` — Defer: license verification pending
- `@concepts/tool-evaluation-framework.md` — shared methodology

## Raw Concept
- **Title**: Cemini Stack & Wiki Stack: Comprehensive Infrastructure and Integration Evaluation
- **Type**: Commissioned evaluation brief
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/Evaluating Links for Trading and Wiki Stacks.docx`
- **Retrieved**: 2026-05-10
- **Format**: .docx, ~3.1MB, 525 paragraphs
- **Read status**: deep-read

## Narrative

Comprehensive evaluation of 27 software repositories, platforms, and design patterns against the three Cemini deployment surfaces. Each evaluated on: concrete integration vector, license compatibility with IP-sale readiness, RAM/disk/compute footprint, and architectural fit.

### Summary verdicts

| Tier | Count | Tools |
|------|-------|-------|
| **Adopt** | 7 | pandas-ta-classic, GitHub Spec-Kit, tradingview-mcp, tech-debt-skill, claude-mem, RevPDF, CodeBoarding |
| **Steal-from** | 4 | DeepTeam, Browserbase Skills, AgentSkillOS, SPJ algorithm (from SSRN 4943355) |
| **Defer** | 1 | Stirling PDF |
| **Reference-only** | 5 | LLM-Wiki pattern, llmfit, AI Engineering from Scratch, public-apis, Claude Managed Agents |
| **Reject** | 7 | Telegram-Drive, Tracecat, MasterDnsVPN, Arkon, vectorbt, Coralflavor, Hermes Desktop |
| **Unavailable** | 3 | codeg, remindb, agents-remember-md |

### Rejection patterns

- **License poison pill** (3): Tracecat (AGPL-3.0 + PolyForm Shield), Arkon (PolyForm Noncommercial), vectorbt (Apache 2.0 + Commons Clause)
- **Architectural mismatch** (3): Telegram-Drive (Telegram API as storage), MasterDnsVPN (DNS tunneling → latency), Hermes Desktop (Electron bloat)
- **Consumer/novelty** (1): Coralflavor ("uncensored AI chat")

### License-driven rejections are institutional memory

Tracecat, Arkon, and vectorbt all failed on licensing grounds despite strong technical fits. These rejections reinforce the IP-sale-readiness license posture documented in `@concepts/cemini-license-posture.md`. The Commons Clause (vectorbt) and PolyForm family (Arkon, Tracecat) are on the explicit reject list.

### Notable adopt recommendations

- **tradingview-mcp**: Deploy as Docker sidecar, map 130+ MCP tools into orchestrator. High-value for real-time technical analysis.
- **pandas-ta-classic**: 252 indicators, but requires Pandas↔Polars bridging. Must profile latency penalty.
- **GitHub Spec-Kit**: Bridges the 380-page wiki → deterministic Python code gap via spec-driven development.
- **claude-mem**: Solves context amnesia across multi-day dev cycles. Token efficiency paradox flagged as risk.

## Snippets

> "The mathematical fidelity of the 252 unique tools provides an immediate upgrade to the existing scikit-learn and NumPy calculation pipelines." (pandas-ta-classic, Adopt rationale)

> "The philosophy of executable specifications provides the exact bridge required to systematically translate the 380 hand-curated markdown pages into deterministic, test-driven Python code." (Spec-Kit, Adopt rationale)

> "This constitutes an immediate and total licensing failure, overriding all technical merits." (vectorbt, Reject rationale — Commons Clause)

[Source: Evaluating Links for Trading and Wiki Stacks.docx]
