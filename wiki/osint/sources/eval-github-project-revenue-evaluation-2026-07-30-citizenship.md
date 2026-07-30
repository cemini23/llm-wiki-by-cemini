---
title: GitHub Project Revenue Evaluation — citizenship / migration URLs (2026-07-30)
type: source
tags: [source, tool-evaluation, revenue, atto, k214, docx, citizenship]
keywords: [USCIS API, austrian-58c, citizenship-gov-data, Ocelot-Social]
related:
  - entities/tools/uscis-api-evangelist.md
  - entities/tools/austrian-58c-citizenship-kit.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/gpuology-genealogy-agent-kit.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-07-30
updated: 2026-07-30
read_status: deep-read
---

## Relations

- @entities/tools/uscis-api-evangelist.md — eval Extract → NO-GO (no SPDX)
- @entities/tools/austrian-58c-citizenship-kit.md — live exists; eval UNAVAILABLE; Watch no-clone
- @concepts/wiki-tooling-evaluation.md
- @concepts/gpuology-genealogy-agent-kit.md
- @concepts/cemini-license-posture.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | GitHub Project Revenue Evaluation (citizenship / migration) |
| Filename | `GitHub Project Revenue Evaluation.docx` |
| sha256 | `ecbfbb27566b620385843939eb67a6b180d451a87c43b47ceb24144724e1eafc` |
| Retrieved | 2026-07-30 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/GitHub Project Revenue Evaluation.docx` |
| Digest | `.local/reports/k214-tool-eval-digest.md` |

## Narrative

20-URL batch; Gemini returned **15 UNAVAILABLE**, 2 Pass, 2 Context, **1 Extract**. Live `gh api` overrides:

| Repo | Eval | Live | Cemini |
|------|------|------|--------|
| `api-evangelist/us-citizenship-and-immigration-services` | Extract | **null SPDX** | **NO-GO** — USCIS API docs/agentic-access notes only; no Phase-0 |
| `yanowitz/austrian-58c-citizenship-kit` | UNAVAILABLE | exists, null SPDX | **Watch** — §58c skill kit; no clone |
| `anika-kum/citizenship-gov-data` | UNAVAILABLE | exists, null SPDX | wiki-only stub note |
| `grainne-b/visa-processing-times` | UNAVAILABLE | exists, null SPDX | wiki-only |
| `Ocelot-Social-Community/Ocelot-Social` | Pass | NOASSERTION ~132MB | Pass confirmed |
| `eurosky-social/eu-haul` | Context | MIT | Context — no Phase-0 |
| `HunterSpence/enterprise-ai-accelerator` | Context | MIT | Context — no Phase-0 |

Remaining UNAVAILABLE confirmed dead or irrelevant (DOSAR radar, etc.). **No Phase-0 adopts** this batch (<500MB budget unused).

## Snippets

> USCIS… Sandbox → Production requires ≥5 consecutive days of simulated API traffic…

[Source: GitHub Project Revenue Evaluation.docx]
