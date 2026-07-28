---
title: "Harvey — Scaling Document Processing (X Article via @lamgary)"
type: source
tags: [source, x-article, harvey, document-processing, atto, k199]
keywords: [Harvey, Vault, OCR, UDF, Arrow IPC, Job Framework, vector DB migration]
related:
  - concepts/document-processing-pipeline-scale-patterns.md
  - concepts/historical-document-kg-query-inference.md
  - concepts/gpuology-genealogy-agent-kit.md
  - concepts/computational-genealogy-archival-automation.md
  - concepts/code-as-agent-harness.md
maturity: draft
read_status: read
created: 2026-07-28
updated: 2026-07-28
clusters: [k199-ingest]
---

## Relations

- @concepts/document-processing-pipeline-scale-patterns.md
- @concepts/historical-document-kg-query-inference.md
- @concepts/gpuology-genealogy-agent-kit.md
- @concepts/computational-genealogy-archival-automation.md
- @concepts/code-as-agent-harness.md

## Raw Concept

| Field | Value |
|-------|-------|
| **Tweet** | https://x.com/lamgary/status/2081787028891394186 |
| **Article** | https://x.com/i/article/2081784796863254528 |
| **Authors** | Tom McCormick, Jin Zhang, Shunrang Cao, Jinfeng Zhuang, Anna Zhang, Adam Shen, Gary Lam |
| **Posted** | 2026-07-27 (Gary Lam / @lamgary) |
| **Filename** | `x-lamgary-harvey-scaling-document-processing-2026-07-27.md` |
| **sha256** | `eb5d02051a276ec51bcf15fad7fd3e1f7a15240d3bb08c60ec12084fdb43c31b` |
| **Retrieved** | opencli `twitter article` 2026-07-28 |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/x-lamgary-harvey-scaling-document-processing-2026-07-27.md` |

## Narrative

Harvey engineering post on scaling legal-document processing under Vault/Assistant: ~1M docs/busy-week → tens of millions/week (**26× documents, 39× data**; ~3.5M docs/day recent). Growth driven by Vault + DMS connectors (iManage, SharePoint, Box, Drive, NetDocuments, on-prem) and harder file mix (scanned PDFs, email archives, eDiscovery).

**Architecture steals:** (1) durable Job Framework — resume mid-batch, file-level failure isolation; (2) split extract / chunk-embed / index by bottleneck with independent queues/retries; (3) **UDF** (Unified Document Format) typed pieces vs monolithic Pydantic object — p50 −19% / p90 −17% / p99 −11% extract latency, "no observed output-quality regression"; (4) live vector-DB migration via dual-write + shadow reads; (5) **Arrow IPC** embed→index handoff vs JSON; (6) backpressure/fallback chains (OCR primary→Harvey→local) instead of collapse; (7) next: metrics-driven autoscaling on backlog / rate-limit headroom.

**Atto fit:** Antenati/parish bulk HTR dumps need the same extract≠embed≠index split, durable resume, typed intermediate format, and quality gates that are not self-authored (pair with verifier–deployment gap / regression tax). Reply on thread asked how "no quality regression" is measured — still open.

## Snippets

> "At this scale, document processing stops being one pipeline and starts behaving like several different systems."

> "UDF changed that into a versioned internal format with typed pieces of the document… p50 fell by about 19%"

> "replace the heavy JSON serialization/deserialization with Arrow IPC in the embed-to-index handoff"
