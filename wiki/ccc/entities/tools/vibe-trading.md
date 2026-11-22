---
title: vibe-trading — agent-native trading workspace (HKUDS)
type: entity
related:
  - sources/arxiv-vibe-trading-agent-native-trading-2611.24845.md
  - concepts/result-provenance-authority-gate.md
maturity: draft
updated: 2026-11-22
---

## Raw Concept

Entity page for the `HKUDS/Vibe-Trading` project. Prompted by the paper ingest `@sources/arxiv-vibe-trading-agent-native-trading-2611.24845.md`. A separate OSINT source page covers the repo: `@osint-wiki/sources/vibe-trading-hkuds.md` (owned by the OSINT wiki).

## Narrative

- **Repo:** https://github.com/HKUDS/Vibe-Trading
- **Authors:** Haozhe Wu, Zhonghang Li, Chao Huang (University of Hong Kong)
- **Scope:** market research, financial data, strategy generation, backtesting, portfolio analysis, paper trading, multi-agent collaboration, optional broker execution.

The architecture, not the trading features, is the reason this page exists in CCC. Results keep source, temporal scope, configuration and producing run. Research records are versioned. An explicit authority gate separates strategy research from live execution. See `@concepts/result-provenance-authority-gate.md`.

### Fit for Cemini

Trading-specific use belongs to the OSINT wiki and CeminiSuite. The harness pattern — provenance plus an authority gate — is reusable. Do not adopt the trading stack here.

[OPEN QUESTION 2026-11-22] The OSINT page does not yet link back to this page. Add the reciprocal edge when the OSINT owner next edits it.
