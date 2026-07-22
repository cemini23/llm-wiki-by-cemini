---
title: Topola Viewer (PeWu)
type: entity
tags: [tool, genealogy, visualization, k157, extract]
keywords: [GEDCOM, fan chart, hourglass, D3, Apache-2.0]
related:
  - sources/eval-genealogy-repository-revenue-evaluation-2026-07-22.md
  - concepts/gpuology-genealogy-agent-kit.md
  - sources/gemini-gpuology-genealogy-business-analysis-2026-07-20.md
  - sources/eval-multi-wiki-link-evaluation-genealogy-agent-2026-07-10.md
  - concepts/computational-genealogy-archival-automation.md
maturity: draft
created: 2026-07-10
updated: 2026-07-22
---

## Relations

- @sources/eval-genealogy-repository-revenue-evaluation-2026-07-22.md — K190 reinforce
- @sources/gemini-gpuology-genealogy-business-analysis-2026-07-20.md — K176 GPUOLOGY business DR
- @concepts/gpuology-genealogy-agent-kit.md — product strategy concept

- @concepts/computational-genealogy-archival-automation.md — visualization gap-fill
- @sources/eval-multi-wiki-link-evaluation-genealogy-agent-2026-07-10.md — K157 Extract

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | [PeWu/topola-viewer](https://github.com/PeWu/topola-viewer) |
| **License** | Apache-2.0 (~328★) [CONFIRMED Phase-0] |
| **Verdict** | **Extract** — static GEDCOM fan/hourglass viewer (no backend) |
| **Deploy** | Family sprint / GPUOLOGY: static GEDCOM or **`.gdz` (GEDZIP)** on Cloudflare Pages + Access [Source: K176 DR] |
| **K176** | Enabler for private share site — client-side only; fork + GH Actions → Pages in 90-day MVP |

Frictionless relational charting missing from Gramps desktop UI. Self-hosted viewer mounts directly on exported GEDCOM files.

## Snippets

> "frictionless, interactive visual exploration of deeply complex historical networks" [Source: eval docx URL 14]

> Ideal client-side visualization for Cloudflare deployment; `.gdz` bundling. [Source: @sources/gemini-gpuology-genealogy-business-analysis-2026-07-20.md]
