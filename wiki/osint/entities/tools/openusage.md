---
title: "openusage — Local Token Economics Dashboard"
type: entity
tags: [dev-tooling, token-economics, api-cost-tracking, go, mit, adopted-tier, laptop-only]
keywords: [openusage, token-tracking, api-spend, cost-monitoring, gemini-api, quota-management]
related:
  - sources/multi-wiki-tool-evaluation-v3.md
maturity: draft
created: 2026-05-14
updated: 2026-05-14
---

## Relations
- @ccc-wiki/entities/openusage.md  (cross-wiki stub)

- @sources/multi-wiki-tool-evaluation-v3.md — v3 batch eval: Adopt tier, CCC wiki primary fit

## Raw Concept

From the Cemini Multi-Wiki Link Evaluation Report v3 (May 2026). MIT-licensed v0.10.5, Go-based background telemetry daemon for tracking API token consumption and financial spend across local developer environments.

## Narrative

OpenUsage provides local-first token economics tracking by passively intercepting `~/.gemini` auth directories and monitoring `GEMINI_API_KEY` executions. Supports 15+ visual themes and requires zero configuration.

**Tier: Adopt** — MIT license, safe for IP perimeter. Directly satisfies CCC wiki's token-economics tracking mandate. Cross-wiki routing: configure the telemetry daemon to isolate and track API billing rates for heavy OSINT investigative queries (OSINT wiki stub).

**NEEDS VERIFICATION:** Compatibility with EDR-monitored corporate endpoint environments.
