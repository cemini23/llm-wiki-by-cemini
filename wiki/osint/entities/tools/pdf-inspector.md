---
title: "firecrawl/pdf-inspector"
type: entity
tags: [tool, phase-0, k218, atto]
keywords: [pdf-inspector, firecrawl, scanned-pdf]
related:
  - sources/eval-github-revenue-opportunity-repository-2026-08-02.md
  - entities/tools/transkribus.md
  - entities/tools/google-magika.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/gpuology-genealogy-agent-kit.md
maturity: draft
created: 2026-08-02
updated: 2026-08-02
wire_status: policy_wired
wire_target: .cursor/rules/osint-phase1-adopt-wires.mdc
---

## Relations

- @sources/eval-github-revenue-opportunity-repository-2026-08-02.md
- @entities/tools/transkribus.md
- @entities/tools/google-magika.md
- @concepts/wiki-tooling-evaluation.md
- @concepts/gpuology-genealogy-agent-kit.md

## Narrative

| Field | Value |
|-------|--------|
| **Repo** | https://github.com/firecrawl/pdf-inspector |
| **License** | **MIT** [CONFIRMED gh/LICENSE 2026-08-02] |
| **Verdict** | **GO Extract** |
| **Local** | `.local/adopts/pdf-inspector` (~25MB) |
| **Route** | atto |

Rust PDF inspect: scanned vs text routing before OCR/HTR. Pair with Magika; Transkribus remains sole HTR.
