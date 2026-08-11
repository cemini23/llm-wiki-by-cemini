---
title: "Stagehand (Browserbase) — browser-agent SDK v4"
type: entity
tags: [tool, k231, atto, browser-automation, scraping]
keywords: [stagehand, browserbase, Playwright, CDP, self-healing, Act Observe Extract, Antenati, FamilySearch]
related:
  - sources/eval-url-revenue-opportunity-2026-08-11.md
  - concepts/wiki-tooling-evaluation.md
  - entities/tools/holaos.md
  - sources/eval-project-evaluation-revenue-2026-08-11.md
maturity: draft
created: 2026-08-11
updated: 2026-08-11
phase_0_verdict: "GO Integrate 2026-08-11 (MIT, ~157MB)"
---

## Relations

- @sources/eval-project-evaluation-revenue-2026-08-11.md

- @sources/eval-url-revenue-opportunity-2026-08-11.md — GO Integrate v4
- @concepts/wiki-tooling-evaluation.md
- @entities/tools/holaos.md — combo: Stagehand v4 + holaOS → resilient Atto retrieval

## Raw Concept

- **Repo**: `github.com/browserbase/stagehand` (v4)
- **License**: MIT [gh api override]
- **Tier**: Integrate (v4)
- **Primary fit**: Atto — self-healing portal scraping (Antenati / FamilySearch deep-link extraction)
- **Phase-0**: `.local/adopts/stagehand` ~83MB

## Narrative

Stagehand v4 moves target management, state, and CDP dispatch into a browser extension running adjacent to the page — eliminating remote-execution race conditions. Self-healing `Act` / `Observe` / `Extract` primitives (NL-driven) + hybrid accessibility-tree trimming → 2x faster, ~80% more token-efficient than standard Playwright, and recovers when archival sites change their DOM.

**Constraints:** respect Antenati/FS ToS + rate limits; human-gated truth; no mass scrape; Magika + PII strip unchanged; Transkribus sole HTR; test only against synthetic Rossi / 900-series SSN fixtures — never live PII.
