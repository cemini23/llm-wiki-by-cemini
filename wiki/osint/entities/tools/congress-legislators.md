---
title: congress-legislators (unitedstates)
type: entity
tags: [tool, data, entity-resolution, politics, kalshi, k149]
keywords: [bioguide, ICPSR, legislator YAML, CC0, prediction-markets]
related:
  - sources/eval-url-revenue-plan-20url-2026-07-08.md
  - entities/platforms/kalshi.md
  - concepts/dcm-state-preemption.md
maturity: draft
created: 2026-07-08
updated: 2026-07-08
---

## Relations

- @sources/eval-url-revenue-plan-20url-2026-07-08.md — K149 Extract
- @entities/platforms/kalshi.md — political event-contract entity keys

## Raw Concept

Structured US Congress legislator database — YAML/JSON with Bioguide, ICPSR, official vs preferred names.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `unitedstates/congress-legislators` |
| **License** | **CC0-1.0** (`gh api` 2026-07-08) |
| **Stars / pushed** | ~2.4k★; pushed 2026-06-15 |
| **Verdict** | **Extract** — canonical IDs for PM/Kalshi political entity resolution |
| **Brief** | `briefs/pm-2026-07-08_k149-congress-legislators-entity-resolve.md` |

Use as offline lookup table before NLP alias matching on committee / member event markets. Sync cadence needs verification (YAML lag on resignations).

## Snippets

> "Integrating this highly structured metadata directly into the PM/Kalshi bot infrastructure guarantees perfect entity resolution" [Source: eval docx URL 17 — [TENTATIVE] on perfect]
