---
title: Polymarket_data (SII-WANGZJ) — on-chain PM dataset pipeline
type: entity
tags: [tool, polymarket, dataset, osint, adopt, k103]
keywords: [polymarket-data, sii-wangzj, on-chain, historical-trades]
related:
  - sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md
  - entities/tools/warproxxx-poly-data.md
  - concepts/polymarket-wallet-alpha-pipeline.md
maturity: draft
created: 2026-06-07
updated: 2026-06-07
phase_0_verdict: "CONDITIONAL-GO 2026-06-07 — MIT verified; 107GB+ workflow — sample subset on laptop only; prod via brief"
---

## Relations

- @sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md — K103 Adopt
- @entities/tools/warproxxx-poly-data.md — sibling PM data tooling
- @concepts/polymarket-wallet-alpha-pipeline.md — downstream OSINT use

## Raw Concept

- **URL:** https://github.com/SII-WANGZJ/Polymarket_data
- **Tier:** Adopt (OSINT-wiki)
- **License:** MIT [CONFIRMED 2026-06-07]
- **Stars / push:** ~625★ / 2026-01-01

## Narrative

Open pipeline for fetching and storing Polymarket on-chain trade history at scale. Relative `data/` + `logs/` layout; no hardcoded absolute paths in core scripts.

**Phase-0:** CONDITIONAL-GO — disk-heavy; ingest sample to librarian research only. Overlaps ArcticDB market dataset paths — coordinate before full mirror.

**Not** a Cemini prod execution component.

## Snippets

> "Route wallet activity into OSINT financial profiling directory." [Source: Tool Evaluation and Wiki Fit.docx URL for Polymarket_data; paraphrase K103 eval]
