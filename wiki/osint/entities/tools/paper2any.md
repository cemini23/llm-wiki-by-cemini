---
title: "Paper2Any — Multimodal PDF Ingestion Framework"
type: entity
tags: [tool, pdf-ingestion, multimodal, gpu-bound, k37]
keywords: [paper2any, reference-only, three-surface-eval]
related:
  - sources/evaluating-urls-system-integration.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/evaluating-urls-system-integration.md` — source evaluation brief (URL 7)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `github.com/OpenDCAI/Paper2Any`
- **Tier (per source brief)**: **Reference-only**
- **License**: [NEEDS VERIFICATION 2026-05-11] License unknown in brief.

## Narrative

AI-driven multimodal framework for ingesting academic PDFs / screenshots / raw text and reconstructing them into editable formats (e.g. Draw.io diagrams). Integrates GPT-4o + Qwen-VL for inverse parsing.

### Integration vector

Reference-only — GPU dependencies + vLLM preclude Hetzner deployment. Inverse-parsing methodology (raster diagram → semantic structure) is worth monitoring for future ingest workflows.

### Risks

Roadmap: Paper2PPT 70% complete, Paper2Video 40% complete — codebase highly unstable.

[Source: Evaluating Urls System Integration.docx, URL 7]
