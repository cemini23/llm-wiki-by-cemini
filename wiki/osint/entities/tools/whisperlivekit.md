---
title: "WhisperLiveKit — streaming STT (Apache-2.0 Extract)"
type: entity
tags: [tool, atto, k243, apache, extract]
keywords: [WhisperLiveKit, STT, oral-history, Transkribus]
related:
  - sources/eval-multi-repo-revenue-2026-08-20.md
  - sources/arxiv-2608.17915-computational-prosopography-2026-08-20.md
  - concepts/atto-genealogy-agent-kit.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-08-20
updated: 2026-08-20
wire_status: policy_wired
wire_target: .cursor/rules/osint-phase1-adopt-wires.mdc
wire_note: STT not HTR; no Barone audio in git
---

## Relations

- @sources/eval-multi-repo-revenue-2026-08-20.md — OSINT K243 eval
- @sources/arxiv-2608.17915-computational-prosopography-2026-08-20.md — oral-history vs graph methodology
- @concepts/atto-genealogy-agent-kit.md — Transkribus remains sole product HTR
- @concepts/cemini-license-posture.md

## Raw Concept

OSINT K243 Phase-0 Extract. Clone `.local/adopts/WhisperLiveKit`. https://github.com/QuentinFuxa/WhisperLiveKit

## Narrative

| Field | Value |
|-------|--------|
| License | **Apache-2.0** [CONFIRMED gh 2026-08-20] |
| Local | `.local/adopts/WhisperLiveKit` (~43MB) |
| Verdict | **Extract** |
| wire_status | `policy_wired` |

Streaming speech-to-text wrapper around Whisper-class models for live / oral-history capture. **Not handwriting recognition.** Atto may steal local STT for interview notes; Transkribus remains sole product HTR. Never commit family or living-person audio to git or Atto fixtures.

## Snippets

> WhisperLiveKit Apache-2.0 Extract. Oral-history STT ≠ Transkribus HTR. [Source: `.local/reports/license-k243-2026-08-20.md`]
