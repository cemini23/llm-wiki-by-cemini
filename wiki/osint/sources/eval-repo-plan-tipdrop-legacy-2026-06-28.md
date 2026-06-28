---
title: "Repo Evaluation Plan 2.docx — TipDrop legacy alerts audit (2026-06-28)"
type: source
tags: [tool-evaluation, tipdrop, compliance, k133]
keywords: [stocktips, tipdrop, uwb-localization, cftc-4-41, gemini-deep-research-v9]
related:
  - concepts/wiki-tooling-evaluation.md
  - concepts/cemini-license-posture.md
  - sources/eval-multi-wiki-discord-link-2026-06-28.md
maturity: draft
read_status: read
created: 2026-06-28
updated: 2026-06-28
clusters: [wiki-tooling]
---

## Relations

- @sources/eval-multi-wiki-discord-link-2026-06-28.md — sibling Discord batch

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Cemini Repo Evaluation Plan 2 |
| **Type** | DOCX (Gemini Deep Research RUNTIME v9) |
| **sha256** | `35caa81ade2782cb3236d6a4cf000be775e26b56b6316518d28c24e2f8d3131f` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Cemini Repo Evaluation Plan 2.docx` |
| **Retrieved** | 2026-06-28 |
| **Read status** | read |

## Narrative

K133 batch — **18 URLs**: DiscordAlerts dead links, tipdrop name collisions (404), StockTips forks, UWB drone localization.

### Tier distribution

| Tier | Count | Repos |
|------|-------|-------|
| **Reject** | 2 | lijx10/uwb-localization, icharm/StockTips |
| **UNAVAILABLE** | 16 | tipdrop/* forks, StockTips/* 404 |

### Rejects — rationale

| Repo | License | Why reject |
|------|---------|------------|
| icharm/StockTips | **NOT FOUND** | No CFTC 4.41 / NFA disclaimers; raw alert broadcast liability |
| lijx10/uwb-localization | **Apache-2.0** (verified) | ROS/C++ drone EKF — zero TipDrop overlap; math reference → game-dev brief only |

### Thesis

Open-source retail alerting repos are **ephemeral** (404 attrition ~89%). TipDrop compliance + UW upstream must stay **in-house**; do not adopt legacy StockTips/DiscordAlerts forks for core routing.

## Snippets

> icharm/StockTips lacks SPDX license and regulatory disclaimers — categorical reject for TipDrop. [Source: eval docx URL 8, 2026-06-28]
