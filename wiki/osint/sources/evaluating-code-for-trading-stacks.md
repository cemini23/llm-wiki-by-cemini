---
title: "Evaluating Code for Trading Stacks — 17-URL Three-Surface Batch"
type: source
tags: [source, evaluation-brief, tooling, three-surface-fit, ip-readiness, license-audit]
keywords: [trading stacks, AI agents, MCP, Go binary, C++ engine, data labeling, license posture, three-surface evaluation]
related:
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - concepts/mcp-tool-marketplace.md
  - concepts/cross-channel-agent-gateway.md
  - concepts/declarative-data-labeling-skills.md
  - entities/tools/picobot.md
  - entities/tools/ctop.md
  - entities/tools/quantmuse.md
  - entities/tools/adala.md
  - entities/tools/mercury-agent.md
  - entities/tools/tmux-orchestrator.md
  - entities/tools/digital-marketing-pro.md
  - entities/tools/llmops-data-processing.md
  - entities/tools/finance-skills.md
  - entities/tools/terax-ai.md
  - entities/tools/data-formulator.md
  - entities/tools/appflowy.md
  - entities/tools/dflash.md
  - entities/tools/floci.md
maturity: validated
read_status: deep-read
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- cross-wiki route → seo-wiki briefs/2026-05-10_digital-marketing-pro-claude-ecosystem.md (URL 10 content; backlinked in brief frontmatter)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied here
- `@concepts/cemini-license-posture.md` — license clean-list enforcement (AGPL/PolyForm rejected)
- `@concepts/mcp-tool-marketplace.md` — picobot is an MCP-native cross-channel gateway candidate
- `@concepts/cross-channel-agent-gateway.md` — pattern extracted from picobot + mercury-agent
- `@concepts/declarative-data-labeling-skills.md` — pattern extracted from Adala + finance-skills

## Raw Concept

- **Title**: Evaluating Code for Trading Stacks
- **Author**: User-prepared analyst memo
- **Type**: docx evaluation brief, 17 URLs scored on three-surface fit matrix
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/Evaluating Code for Trading Stacks.docx`
- **Retrieved**: 2026-05-10
- **sha256**: `726dff6faea3881c…` (preingest verdict: NEW)
- **Pages**: 17 URLs scored — 3 UNAVAILABLE, 14 evaluated
- **Read-status**: deep-read

## Narrative

K36 batch — 17 GitHub/web URLs evaluated against the standard three-surface matrix (Cemini production stack / Wiki librarian server / Workflow laptop). Each URL graded ✅/⚠️/❌ per surface and assigned a recommendation tier: **Adopt**, **Steal-from**, **Reference/Defer**, or **Reject**.

### Tier rollup

| Tier | Count | URLs |
|------|------:|------|
| **Adopt** | 4 | picobot (URL 4), ctop (URL 8), QuantMuse (URL 12), Adala (URL 14) |
| **Steal-from** | 4 | mercury-agent (URL 3), Tmux-Orchestrator (URL 9), digital-marketing-pro (URL 10), LLMops/data-processing (URL 13) |
| **Steal+Adopt split** | 1 | finance-skills (URL 15) — steal for Cemini, adopt for workflow |
| **Reference / Defer** | 2 | terax-ai (URL 2), data-formulator (URL 17) |
| **Reject** | 3 | AppFlowy (URL 7, AGPL-3.0), dflash (URL 11, CUDA-only), floci (URL 16, AWS-emulator domain miss) |
| **UNAVAILABLE** | 3 | URL 1 (HKUDS/AI-Trader), URL 5 (stage-cli), URL 6 (opensourceprojects.dev/post/826eb6ac) |

### High-impact findings

**Cemini production (4 GO adoptions)**:
- **picobot** — 9 MB Go binary, MCP-native, ✅ on all three surfaces. Solves cross-channel (Telegram/Discord/Slack/WhatsApp) communication with <25 MB RAM resident, dropping into existing Docker Compose with `alpine:3.20` base. MIT.
- **QuantMuse** — production-ready quant system with Python factor analysis + C++17 low-latency core engine. Adopt the C++ order-routing core (CMake build inside Alpine container) + VaR/CVaR risk metrics. Strip out LangChain bloat. MIT.
- **Adala** — data-labeling framework with reflection loop; route DeepSeek-compat traffic to Cemini ingest layer for batch sentiment scoring on EDGAR/GDELT. Apache-2.0. **Risk**: 2.5-year release gap (last v0.0.4 Nov 2023).
- **digital-marketing-pro** (Steal): hallucination-detection scripts + `evals.json` schema → port into `agents/orchestrator.py` for pre-trade output validation. MIT.

**Workflow laptop adoptions**:
- **ctop** — htop-style monitor for Claude Code sessions, tracks token utilization across input/output/cache. `npm i -g ctop-claude`. MIT. Solves silent token-burn problem during heavy Obsidian + Claude Code sessions.
- **finance-skills** — `npx plugins add himself65/finance-skills` for yfinance/Funda/Adanos integration during academic-paper back-verification. MIT.
- **data-formulator** (Defer/Reference) — Microsoft Research AI viz tool with DuckDB local backend; useful for Polars→chart pipeline but Alpha-tagged with breaking-change risk.

**Cemini Steal-from patterns**:
- **mercury-agent** (Node.js) — extract permission-hardened shell exec layer + SQLite FTS5 memory schema; transcribe to Python/FastMCP. Don't deploy the Node daemon.
- **Tmux-Orchestrator** — extract `schedule_with_note.sh` + 30-minute auto-commit pattern for hardening long-running local research. Don't adopt full 3-tier hierarchy (10-commit repo, low maturity).
- **LLMops/data-processing** (andysingal) — quarry educational material; extract regex data-cleaning + `LLM-as-judge.md` prompts, port to native Python. Skip ZenML/Ray/Trulens orchestration bloat.

**Rejections — terminal blockers**:
- **AppFlowy** — **AGPL-3.0**, poison-pill family per `@concepts/cemini-license-posture.md`. Closes ASP loophole. IP-sale-disqualifying for any network-adjacent integration.
- **dflash** — CUDA + Apple Silicon MLX hardware lock-in; Cemini is AMD EPYC CPU-only.
- **floci** — AWS emulator (46 services); Cemini explicitly rejected AWS-cloud-native design in favor of Hetzner bare-metal + PostgreSQL/Redis. Solves a problem we don't have.

### Three-surface scoring summary

| Tool | Cemini prod | Wiki server | Workflow | Tier |
|------|:-----------:|:-----------:|:--------:|------|
| picobot | ✅ | ✅ | ⚠️ | **Adopt** |
| ctop | ❌ | ❌ | ✅ | **Adopt (workflow)** |
| QuantMuse | ✅ | — | ⚠️ | **Adopt (prod)** |
| Adala | ✅ | — | ⚠️ | **Adopt (prod ingest)** |
| mercury-agent | ⚠️ | ⚠️ | ✅ | Steal-from |
| Tmux-Orchestrator | ❌ | ❌ | ✅ | Steal-from |
| digital-marketing-pro | ⚠️ | ❌ | ⚠️ | Steal-from |
| LLMops | ⚠️ | — | ✅ | Steal-from |
| finance-skills | ⚠️ | — | ✅ | Steal/Adopt split |
| terax-ai | ❌ | ❌ | ⚠️ | Reference |
| data-formulator | ❌ | ❌ | ✅ | Defer/Reference |
| AppFlowy | ❌ (AGPL) | ❌ | ❌ | **Reject** |
| dflash | ❌ (CUDA) | ❌ | — | **Reject** |
| floci | ❌ (domain) | — | — | **Reject** |

### Cross-cutting concept patterns extracted

1. **Cross-channel agent gateway** — picobot (Adopt) + mercury-agent (Steal) both implement Telegram/Discord/etc. routing on top of MCP. Picobot's pure-Go path is the production-ready instance; mercury's Node.js path is a reference for permission-hardening shell exec. New concept page: `@concepts/cross-channel-agent-gateway.md`.

2. **Declarative data-labeling skills** — Adala + finance-skills both express "label a dataframe row" as a declarative skill the LLM consumes. Pattern unifies SEC filing ingestion + sentiment scoring + factor extraction under one schema. New concept page: `@concepts/declarative-data-labeling-skills.md`.

### Validation methodology cross-check

License claims for the 4 Adopt-tier entries (picobot, ctop, QuantMuse, Adala) plus the 4 Steal-tier MIT entries (mercury, Tmux-Orchestrator, dmp, LLMops) require Phase-0 audit before integration commits. The source brief asserts MIT/Apache-2.0 across all GO items, but Cemini policy requires independent license verification (per `@concepts/cemini-license-posture.md` and post-PageIndex Phase-0 audit pattern).

**Action**: Phase-0 audits queued for picobot, QuantMuse, Adala (Cemini prod integrations). ctop, finance-skills can proceed on laptop-only basis with verification deferred (lower blast radius).

[Source: Evaluating Code for Trading Stacks.docx]
