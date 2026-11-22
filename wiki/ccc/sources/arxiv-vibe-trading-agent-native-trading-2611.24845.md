---
title: "Vibe-Trading — provenance, reproducibility and an authority gate for trading agents"
type: source
related:
  - concepts/result-provenance-authority-gate.md
  - entities/tools/vibe-trading.md
updated: 2026-11-22
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Vibe-Trading: Towards Agent-Native Trading |
| Author | Haozhe Wu, Zhonghang Li, Chao Huang (University of Hong Kong) |
| Type | arXiv technical report (cs.AI), 2611.24845 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.24845-vibe-trading-towards-agent-native-trading.pdf` |
| Retrieved | 2026-11-22 |
| Pages | 16 |
| Read status | read |

## Narrative

Vibe-Trading is an agent-native trading framework and workspace: market research, financial data, strategy generation, backtesting, portfolio analysis, paper trading, multi-agent collaboration, and optional broker execution.

The harness contribution is not the trading features. It is the architecture that keeps results, evidence, research history and trading authority connected:

- **Shared evidence grounding.** Each result keeps its source, temporal scope, configuration and producing run, so it can be verified.
- **Versioned research records.** A research trail can be resumed and reproduced.
- **An explicit authority gate.** Strategy research is separated from live execution. Action requires explicit authority.

The paper's motivating problem is state drift. Prices, news, positions and capital change continuously, so a number without its data snapshot and run identity is not reusable.

Cemini note: a separate OSINT repo page already covers the `HKUDS/Vibe-Trading` GitHub project — see `@osint-wiki/sources/vibe-trading-hkuds.md`. This page covers the paper. The OSINT page is owned elsewhere and does not yet link back. [OPEN QUESTION 2026-11-22]

The transferable pattern for CCC is the authority gate, not the trading domain. Any agent that can change external state should keep research and execution behind a gate that an explicit grant opens. [TENTATIVE] single source.

## Snippets

> "Each result retains its source, temporal scope, configuration, and producing run. Shared evidence grounding enables verification, versioned research records support reproducible continuation, and an explicit authority gate separates strategy research from live execution." [Source: arxiv-2611.24845-vibe-trading-towards-agent-native-trading.pdf p.1]
