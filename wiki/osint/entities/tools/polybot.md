---
title: "polybot — Polymarket Trading & Arbitrage Bot"
type: entity
tags: [tool, polymarket, trading, arbitrage, java, python, market-making]
keywords: [polybot, Polymarket, arbitrage, market-making, replication scoring, ClickHouse, Java]
related:
  - sources/project-link-evaluation-brief-5_10.md
  - sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md
  - entities/tools/polymarket-paper-trader.md
  - concepts/tool-evaluation-framework.md
maturity: draft
created: 2026-05-10
updated: 2026-05-31
---

## Relations
- `@sources/project-link-evaluation-brief-5_10.md` — source evaluation brief (URL 3)
- `@sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md` — K90 v6 Steal-from reaffirmed (MIT)
- `@entities/tools/polymarket-paper-trader.md` — companion Polymarket tool (Adopt tier)

## Raw Concept

Polybot is an open-source Polymarket trading infrastructure and strategy reverse-engineering toolkit. Multi-container architecture with ClickHouse columnar database for real-time market state ingestion.

- **Repo**: `github.com/ent0n29/polybot`
- **License**: MIT
- **Stack**: Java 72.6%, Python 26.5%, Shell 0.9%
- **Requirements**: Amazon Corretto 21 (Java 21+), Maven 3.8+, Docker Compose, Python 3.11+
- **Maturity**: 594 stars

## Narrative

Polybot ingests real-time Polymarket market state and user trade data into ClickHouse, executing automated arbitrage strategies and market-making algorithms. It also provides replication scoring — reverse-engineering profitable trader behaviors for strategy extraction.

### Integration vectors

- **Cemini prod (Steal-from)**: Extract the Python 26.5% of the repo (research scripts, replication scoring, binary arbitrage logic) and rebuild entirely in Polars within the existing Python/LangGraph environment. The Java application and ClickHouse containers must be discarded to stay within the 7 GB RAM ceiling.
- **Workflow (Adopt)**: Claude Code analyzes the Python research scripts to understand Polymarket API interaction patterns, then abstracts and ports the mathematical models.

### Risks

- **Java + ClickHouse overhead**: JVM + ClickHouse violates the 7 GB RAM constraint. The steal-from strategy explicitly discards these components.
- **Commercialization trajectory**: Repository serves as foundation for upcoming "AWARE fund product layer" — the open-source repo may be abandoned or restricted once the commercial product launches.

### Cemini significance

Polybot's replication scoring algorithm — reverse-engineering profitable trader behaviors — is a novel capability not present in the current Polymarket stack. Combined with polymarket-paper-trader (safe forward-testing), it creates a research→validate feedback loop.

[Source: Project Link Evaluation Brief 5_10.docx, URL 3]

### Phase-0 audit (2026-05-28)

Clone: `/tmp/k73-phase0-batch2/polybot`

| Check | Result |
|-------|--------|
| License | **MIT** (`LICENSE` present) |
| Maturity | ~677★, multi-module Java 21 + Docker/ClickHouse stack |
| Fit | Real ingestion/execution architecture, but **Java + ClickHouse** conflict with Cemini 7GB RAM posture |
| Python slice | `research/` scripts exist (~22 py files in shallow tree) for replication scoring |

**Verdict: CONDITIONAL-GO (steal-from only)** — port Python research/replication patterns; **NO** wholesale Java/ClickHouse deploy on cemini-prod.

