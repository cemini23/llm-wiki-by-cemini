---
title: Rampart — client-side PII redaction (ONNX)
type: entity
tags: [entity, tool, compliance, tipdrop, pii, k141]
keywords: [rampart, nationaldesignstudio, ONNX, Transformers.js, PII, TipDrop M2]
related:
  - sources/eval-huggingface-models-v2-2026-07-03.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-07-03
updated: 2026-07-03
---

## Relations

- @sources/eval-huggingface-models-v2-2026-07-03.md — K141 Adopt row

## Raw Concept

K141 eval of [nationaldesignstudio/rampart](https://huggingface.co/nationaldesignstudio/rampart) — 14.7MB ONNX PII scrubber for browser.

## Narrative

| Field | Value |
|-------|-------|
| **HF** | `nationaldesignstudio/rampart` |
| **License** | **CC-BY-4.0** (docx); gh **NOASSERTION** — verify HF model card |
| **Verdict** | **CONDITIONAL-GO** — TipDrop M2 pre-LLM redaction layer |
| **Caveat** | Low recall on non-Latin scripts per eval `[OPEN QUESTION 2026-07-03]` |

Brief: `../projects/tipdrop-workspace-kit/briefs/2026-07-03_k141-rampart-pii-redaction-adopt.md`

## Snippets

> "Deterministic, client-side PII redaction directly within the browser ecosystem." [Source: Hugging Face Model Evaluation 2.docx URL 12 (retrieved 2026-07-03)]
