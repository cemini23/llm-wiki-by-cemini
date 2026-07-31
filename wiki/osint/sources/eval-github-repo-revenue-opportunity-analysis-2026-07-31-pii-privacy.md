---
title: GitHub Repo Revenue Opportunity Analysis — PII redaction cluster (2026-07-31)
type: source
tags: [source, tool-evaluation, revenue, atto, cybersec, k215, docx, pii]
keywords: [pii-redaction, privacy-filter, openredaction, datafog, phileas, Sublist3r]
related:
  - sources/eval-github-repo-revenue-analysis-2026-07-31-panel-vibe.md
  - sources/eval-revenue-analyst-url-evaluation-2026-07-31-mineru.md
  - entities/tools/pii-redaction.md
  - entities/tools/privacy-filter.md
  - entities/tools/openredaction.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/gpuology-genealogy-agent-kit.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-07-31
updated: 2026-07-31
read_status: deep-read
---

## Relations

- @sources/eval-github-repo-revenue-analysis-2026-07-31-panel-vibe.md
- @sources/eval-revenue-analyst-url-evaluation-2026-07-31-mineru.md
- @entities/tools/pii-redaction.md — MIT Extract
- @entities/tools/privacy-filter.md — MIT Extract
- @entities/tools/openredaction.md — MIT Extract
- @concepts/wiki-tooling-evaluation.md
- @concepts/gpuology-genealogy-agent-kit.md — vault PII strip
- @concepts/cemini-license-posture.md

## Raw Concept

| Field | Value |
|-------|--------|
| Filename | `GitHub Repo Revenue Opportunity Analysis.docx` |
| sha256 | `4f7ffad6be22840b4e0218e66d220689b372f85ada86fb3e7718a782345e17d5` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/GitHub Repo Revenue Opportunity Analysis.docx` |

## Narrative

| Repo | Eval | Live | Cemini |
|------|------|------|--------|
| `OpenPipe/pii-redaction` | Extract | **MIT** | **GO Extract** ~600KB |
| `packyme/privacy-filter` | Integrate | **MIT** | **GO Extract** ~464KB |
| `sam247/openredaction` | Extract | **MIT** | **GO Extract** ~5.9MB |
| `DataFog/datafog-python` | Integrate | **MIT** | **Watch** — ~83MB tree; skip Phase-0 this batch |
| `philterd/phileas` | Watch | **Apache-2.0** | **Watch** — ~38MB; skip clone |
| `distil-labs/distil-open-claw-pii` | Extract | null | **NO-GO** |
| `gh0stkey/opf-privacy-filter` | Watch | null | **NO-GO** |
| `aboul3la/Sublist3r` | Extract | **GPL-2.0** | cyber **patterns-only** |

Phase-0 script: `scripts/adopt_k215_phase0.sh`.

## Snippets

> PII redaction… Atto vault secret-strip…

[Source: GitHub Repo Revenue Opportunity Analysis.docx]
