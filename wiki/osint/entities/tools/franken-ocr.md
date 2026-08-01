---
title: "Dicklesworthstone/franken_ocr"
type: entity
tags: [tool, phase-0, k217, atto]
keywords: [franken-ocr, Unlimited-OCR, rust]
related:
  - sources/eval-github-repo-revenue-analysis-htr-2026-08-01.md
  - entities/tools/unlimited-ocr.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-08-01
updated: 2026-08-01
wire_status: policy_wired
wire_target: .cursor/rules/osint-phase1-adopt-wires.mdc
---

## Relations

- @sources/eval-github-repo-revenue-analysis-htr-2026-08-01.md
- @entities/tools/unlimited-ocr.md
- @concepts/wiki-tooling-evaluation.md

## Narrative

| Field | Value |
|-------|--------|
| **Repo** | https://github.com/Dicklesworthstone/franken_ocr |
| **License** | **MIT + OpenAI/Anthropic rider** [CONFIRMED LICENSE file 2026-08-01] |
| **Verdict** | **GO Extract** — CPU Unlimited-OCR path REFERENCE |
| **Local** | `.local/adopts/franken_ocr` (~219MB shallow; operator OK over prior 500MB batch cap) |

Pure-Rust CPU path for Baidu Unlimited-OCR. Not a Transkribus HTR replace — offline CPU OCR REFERENCE for Atto vault when GPU/Python stack is unwanted. Rider blocks OpenAI/Anthropic entities only; Cemini use OK.
