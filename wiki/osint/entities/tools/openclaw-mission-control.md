---
title: OpenClaw Mission Control — multi-agent ops dashboard
type: entity
tags: [entity, tool, openclaw, observability, k137]
keywords: [mission-control, abhi1693, fleet orchestration, RBAC, audit, MIT]
related:
  - sources/eval-multi-wiki-openclaw-ecosystem-2026-06-30.md
  - concepts/xsp-lane-trading-framework.md
  - entities/tools/openclaw.md
  - concepts/xsp-lane-trading-framework.md
maturity: draft
created: 2026-06-30
updated: 2026-06-30
---

## Relations

- @entities/tools/openclaw.md — fleet governance for OpenClaw gateways
- @concepts/xsp-lane-trading-framework.md — xsp-killer fleet monitoring steal target

## Raw Concept

K137 Phase-0 on [abhi1693/openclaw-mission-control](https://github.com/abhi1693/openclaw-mission-control) — MIT TypeScript/Python dashboard for multi-agent approval workflows and activity audit.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `abhi1693/openclaw-mission-control` |
| **License** | **MIT** (`gh api` 2026-06-30) |
| **Stars / pushed** | ~4.1k★; pushed 2026-04-06 |
| **Verdict** | **Steal-from** — RBAC + activity timeline modules |
| **Prod brief** | Fleet audit patterns for xsp-killer / PM bots (not full dashboard Adopt) |

SQLite default mode vs cemini Postgres scale `[OPEN QUESTION 2026-06-30]`.

Brief: `briefs/2026-06-30_k137-mission-control-fleet-audit-steal.md`

## Snippets

> "Centralized operations, detailed activity timelines, and stringent approval-driven governance for multi-agent frameworks." [Source: eval docx URL 17, 2026-06-30]
