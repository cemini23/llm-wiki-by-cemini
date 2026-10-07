---
title: "monid — runtime API discovery + metering for agent tools"
type: entity
tags: [tool, agent-tooling, metering, guruwatcher, mit, k284]
keywords: [monid, openrouter-for-agent-tools, metering, api-discovery, guruwatcher, spend-ceiling, k284]
related:
  - sources/eval-url-revenue-opportunity-2026-10-07.md
  - concepts/k284-eval-wave.md
maturity: draft
created: 2026-10-07
updated: 2026-10-07
---

## Relations

- @sources/eval-url-revenue-opportunity-2026-10-07.md — K284 eval (tier: **Extract**, route: GuruWatcher)
- @concepts/k284-eval-wave.md — K284 cluster hub

## Raw Concept

- **Repo:** `github.com/monid-ai/monid`
- **Tier (K284):** **Extract** (route: GuruWatcher)
- **License:** **MIT** (verified 2026-10-07)
- **Stars:** 2,462 (verified)
- **Description:** "Monid - OpenRouter for agent tools"

## Narrative

A registry/router that does **runtime API discovery and metering** for agent tools. The K284 eval routes it to **GuruWatcher** for its **runtime connector + metering architecture**.

### Why it matters here

GuruWatcher calls external endpoints (newsletters, market data). A **metering layer** with spend ceilings prevents an agent from overrunning a pay-per-call budget. Note: `monid` and `treg` are near-identical in positioning ("OpenRouter for agent tools") — compare before picking one.

### Boundary

FILE only. **Enforce spend ceilings.** GuruWatcher stays **alert-only**: no trade routing, no `watches.json` clobber.

## Snippets

> "monid (GuruWatcher runtime API discovery and metering connector architecture)." [Source: eval-url-revenue-opportunity-2026-10-07.md]
