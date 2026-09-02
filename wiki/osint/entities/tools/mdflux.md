---
title: "mdflux — local MarkItDown + RapidOCR (MIT Extract)"
type: entity
tags: [tool, atto, k242, mit, extract]
keywords: [mdflux, rapidocr, markitdown, transkribus]
related:
  - sources/eval-local-agent-infra-2026-08-19.md
  - concepts/cemini-license-posture.md
  - concepts/atto-genealogy-agent-kit.md
maturity: draft
created: 2026-08-19
updated: 2026-08-19
harness_verb: FILE
wire_note: Local OCR wrapper Extract; Transkribus remains sole product HTR
---

## Relations

- @sources/eval-local-agent-infra-2026-08-19.md — K242 eval
- @concepts/cemini-license-posture.md
- @concepts/atto-genealogy-agent-kit.md — air-gapped ingest; no cloud HTR

## Raw Concept

K242 Phase-0 Extract. Clone `.local/adopts/mdflux` (~38MB). Repo https://github.com/ibrahimqureshae/mdflux

## Narrative

| Field | Value |
|-------|--------|
| License | **MIT** [CONFIRMED gh 2026-08-19] |
| Local | `.local/adopts/mdflux` (~38MB) |
| Verdict | **Extract REFERENCE** |
| wire_status | `policy_wired` |

Rust/Tauri desktop wrapper around MarkItDown with RapidOCR / pypdfium2 sidecars for image-only PDFs. Steal: offline batch folder streaming so Antenati scans never leave the laptop. **Transkribus remains sole product HTR** — do not treat RapidOCR as a handwriting model for Italian civil records. No Barone PII in fixtures. First-launch Python sidecar must not phone home on client vaults.

## Snippets

> mdflux MIT Extract. Transkribus sole HTR. [Source: `.local/reports/license-k242-2026-08-19.md`]
