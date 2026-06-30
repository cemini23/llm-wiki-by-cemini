---
title: ClawHub — official OpenClaw skill registry
type: entity
tags: [entity, tool, openclaw, skills, k137]
keywords: [clawhub, openclaw, skill-format, yaml, supply-chain, MIT]
related:
  - sources/eval-multi-wiki-openclaw-ecosystem-2026-06-30.md
  - entities/tools/openclaw.md
  - concepts/openclaw-security-taxonomy.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-06-30
updated: 2026-06-30
---

## Relations

- @entities/tools/openclaw.md — official registry for OpenClaw gateway skills
- @concepts/openclaw-security-taxonomy.md — K20 malicious ClawHub plugin corpus

## Raw Concept

K137 Phase-0 on [openclaw/clawhub](https://github.com/openclaw/clawhub) — MIT skill marketplace/registry (TypeScript, Next.js, Convex).

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `openclaw/clawhub` |
| **License** | **MIT** (`gh api` 2026-06-30) |
| **Stars / pushed** | ~9k★; active 2026-06-30 |
| **Verdict** | **Steal-from** — skill frontmatter schema + static scan patterns |
| **Risk** | K20 yahoofinance malicious skill (GHSA-5675) — registry is attack surface; steal **validation**, not blind install |

**Steal targets:** `docs/skill-format.md`, moderation/static analysis modules → CCC harness + TipDrop ingest compliance.

Briefs: `briefs/ccc-2026-06-30_k137-clawhub-skill-format-scan-steal.md`; TipDrop `2026-06-30_k137-clawhub-ingest-compliance-steal.md`

## Snippets

> "Skill registry ecosystem … schemas and frontmatter parsing logic necessary to execute third-party agent skills safely." [Source: eval docx URL 15, 2026-06-30]
