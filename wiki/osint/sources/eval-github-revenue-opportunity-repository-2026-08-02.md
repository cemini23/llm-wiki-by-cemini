---
title: "Eval — Revenue Opportunity Repository Analysis 2026-08-02"
type: source
tags: [tool-eval, atto, guruwatcher, xsp, k218]
keywords: [decimen-optical-transfer, pdf-inspector, last30days-skill, TencentDB-Agent-Memory, ds4]
related:
  - concepts/wiki-tooling-evaluation.md
  - concepts/cemini-license-posture.md
  - concepts/gpuology-genealogy-agent-kit.md
  - entities/tools/decimen-optical-transfer.md
  - entities/tools/pdf-inspector.md
  - entities/tools/tencentdb-agent-memory.md
  - entities/tools/last30days-skill.md
  - sources/last30days-skill-mvanhorn.md
maturity: draft
created: 2026-08-02
updated: 2026-08-02
read_status: deep-read
---

## Relations

- @concepts/wiki-tooling-evaluation.md
- @concepts/cemini-license-posture.md
- @concepts/gpuology-genealogy-agent-kit.md
- @entities/tools/decimen-optical-transfer.md
- @entities/tools/pdf-inspector.md
- @entities/tools/tencentdb-agent-memory.md
- @entities/tools/last30days-skill.md
- @sources/last30days-skill-mvanhorn.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Revenue Opportunity Repository Analysis.docx |
| sha256 | `0ef78555fdf284a03fcc5ed0578654c1eee6f65cb9b83d5445b6ac65c61ac91b` |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/osint/Revenue Opportunity Repository Analysis.docx |
| URLs | 20 (agent infra / PDF / memory / optical transfer) |
| read_status | deep-read |

## Narrative

Batch theme: agentic infra, local inference, PDF extraction, memory graphs, optical transfer. Priority #1 Atto / #2 GuruWatcher.

| Repo | Eval tier | SPDX (`gh` 2026-08-02) | Cemini verdict |
|------|-----------|------------------------|----------------|
| bashalarmistalt/decimen-optical-transfer | Extract | **MIT** | **GO Extract** Atto air-gapped PII share — Phase-0 (~6MB) |
| firecrawl/pdf-inspector | Extract | **MIT** | **GO Extract** scanned-vs-text PDF routing — Phase-0 (~25MB) |
| TencentCloud/TencentDB-Agent-Memory | Extract | **MIT** (LICENSE file; API NOASSERTION) | **GO Extract** agent memory patterns → xsp — Phase-0 (~73MB) |
| mvanhorn/last30days-skill | Integrate | **MIT** | **GO Extract** GuruWatcher alert research skill — Phase-0 (~57MB); prior source `@sources/last30days-skill-mvanhorn.md` |
| antirez/ds4 | Watch | **MIT** | **Watch** DeepSeek local inference — no clone this batch |
| semantica-agi/semantica | Watch | **MIT** | **Watch** graph infra cost — no clone |
| iv-org/invidious | Context | **AGPL-3.0** | **NO-GO** AGPL |
| HF abliterated DeepSeek forks | Context | inherited / unclear | **NO-GO** abliterated forks |
| Remaining Context/UNAVAILABLE | — | mixed | Aggregate on this page — no stub farm |

## Snippets

Eval Integrate: last30days-skill for GuruWatcher Polymarket/Reddit sentiment — **alert-only**, never orders. [Source: Revenue Opportunity Repository Analysis.docx]
