---
title: "Project Link Evaluation Brief 5/10 — 15-Tool Polymarket, Chaos Engineering & Feature Flag Audit"
type: source
tags: [tool-evaluation, polymarket, chaos-engineering, feature-flags, architecture, licensing]
keywords: [polymarket-paper-trader, polybot, chaosblade, growthbook, flagsmith, goose, harness, posthog, kubescape, litmus, kusionstack, rig, prediction-market-backtesting]
related:
  - concepts/tool-evaluation-framework.md
  - entities/tools/polymarket-paper-trader.md
  - entities/tools/polybot.md
  - entities/tools/chaosblade.md
  - entities/tools/growthbook.md
  - entities/tools/flagsmith.md
  - entities/tools/goose-aaif.md
  - entities/tools/prediction-market-backtesting.md
maturity: validated
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@entities/tools/polymarket-paper-trader.md` — Adopt: MCP-based Polymarket paper trading simulator
- `@entities/tools/polybot.md` — Steal-from: Polymarket arbitrage/replication algorithms
- `@entities/tools/chaosblade.md` — Adopt: chaos engineering for Docker Compose resilience testing
- `@entities/tools/growthbook.md` — Steal-from: MCP feature flag methodology for LLM orchestration
- `@entities/tools/flagsmith.md` — Defer: license gated
- `@entities/tools/goose-aaif.md` — Reference-only: MCP/ACP protocol patterns
- `@entities/tools/prediction-market-backtesting.md` — Reference-only: TPE sampling methodology
- `@concepts/tool-evaluation-framework.md` — shared methodology

## Raw Concept
- **Title**: Cemini Stack and Wiki Stack Integration and Applicability Analysis
- **Type**: Commissioned evaluation brief
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/Project Link Evaluation Brief 5_10.docx`
- **Retrieved**: 2026-05-10
- **Format**: .docx, 60KB, 400 paragraphs
- **Read status**: deep-read

## Narrative

Third evaluation brief in the May 10 batch. Evaluates 15 tools with emphasis on Polymarket trading infrastructure, chaos engineering for resilience testing, and feature flag platforms for LLM orchestration control. Same three-surface methodology as the companion briefs.

### Summary verdicts

| Tier | Count | Tools |
|------|-------|-------|
| **Adopt** | 2 | polymarket-paper-trader, chaosblade |
| **Steal-from** | 2 | polybot, GrowthBook |
| **Defer** | 1 | Flagsmith |
| **Reference-only** | 2 | prediction-market-backtesting, Goose |
| **Reject** | 7 | Harness, PostHog, Chaos Mesh, Kubescape, Litmus, KusionStack, Rig |
| **Unavailable** | 1 | weatherbot |

### Rejection patterns

- **Kubernetes dependency** (4): Chaos Mesh, Kubescape, Litmus, KusionStack — all require K8s, Cemini uses Docker Compose exclusively
- **Hardware/resource violation** (2): PostHog (min 16GB RAM, ClickHouse+Kafka), Harness (3GB+Java/Go)
- **Archived/abandoned** (1): Rig (archived March 2025)
- **License** (1): Harness (PolyForm Shield, additionally)

### Polymarket cluster

Three Polymarket-adjacent tools evaluated in this brief:
- **polymarket-paper-trader** (Adopt): 26 MCP tools, MIT license, Python 100%, v0.1.6. Sidecar container for safe LLM strategy forward-testing
- **polybot** (Steal-from): Java+Python Polymarket bot with arbitrage and replication scoring. Extract Python research scripts and algorithmic logic; discard JVM+ClickHouse
- **prediction-market-backtesting** (Reference-only): Nautilus Trader extension with Optuna TPE sampling. Mixed GPL-3.0/LGPL-3.0/MIT licensing blocks adoption, but methodology is valuable

### Chaos engineering: Chaosblade over Kubernetes-native alternatives

Four chaos tools evaluated. Only Chaosblade (Apache-2.0, Go binary, no K8s dependency) passes all gates. The other three (Chaos Mesh, Litmus, KusionStack) hard-require Kubernetes. Chaosblade's `blade` CLI can target Docker containers directly via OS-level fault injection (CPU/memory/network).

## Snippets

> "The repository should be cloned, and its MCP server instantiated as a sidecar container within the Cemini docker-compose.yml to facilitate safe, hallucination-resistant forward-testing of LLM trading strategies." (polymarket-paper-trader, Adopt)

> "The underlying algorithmic logic, Polymarket API interaction patterns, and Python research scripts must be extracted and translated into the native Python/LangGraph environment. The overarching Java application and ClickHouse execution containers must be discarded." (polybot, Steal-from)

> "The CLI binary should be integrated into the Cemini testing pipeline to execute scheduled chaos experiments against the Docker Compose stack during non-critical market hours." (chaosblade, Adopt)

[Source: Project Link Evaluation Brief 5_10.docx]
