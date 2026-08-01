---
title: "Eval — GitHub Repo Revenue Analysis (HTR / HTTP) 2026-08-01"
type: source
tags: [tool-eval, htr, atto, guruwatcher, k217]
keywords: [SimpleHTR, htrflow, htrace, kurrentschrift, HTRPipeline, CTC]
related:
  - concepts/wiki-tooling-evaluation.md
  - concepts/cemini-license-posture.md
  - concepts/gpuology-genealogy-agent-kit.md
  - entities/tools/transkribus.md
  - entities/tools/simplehtr.md
  - entities/tools/htrflow.md
  - entities/tools/kurrentschrift.md
  - entities/tools/htrace-sh.md
  - entities/tools/franken-ocr.md
maturity: draft
created: 2026-08-01
updated: 2026-08-01
read_status: deep-read
---

## Relations

- @concepts/wiki-tooling-evaluation.md
- @concepts/cemini-license-posture.md
- @concepts/gpuology-genealogy-agent-kit.md
- @entities/tools/transkribus.md
- @entities/tools/simplehtr.md
- @entities/tools/htrflow.md
- @entities/tools/kurrentschrift.md
- @entities/tools/htrace-sh.md
- @entities/tools/franken-ocr.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | GitHub Repo Revenue Analysis.docx |
| sha256 | `5d4108779fb2ae41720b2ca68cbe2f1ff7333aba510e4232b98741c64c8f6546` |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/osint/GitHub Repo Revenue Analysis.docx |
| URLs | ~19 HTR / HTTP / dataset repos |
| read_status | deep-read |

## Narrative

| Repo | Eval tier | SPDX (`gh api` 2026-08-01) | Cemini verdict |
|------|-----------|----------------------------|----------------|
| githubharald/SimpleHTR | Extract | **MIT** | **GO Extract** CTC / lexicon decode REFERENCE — Phase-0 (~1.5MB) |
| MarkusNeusinger/kurrentschrift | Extract | **MIT** | **GO Extract** ductus methodology — Phase-0 (~82MB); 0★ CONDITIONAL |
| AI-Riksarkivet/htrflow | Integrate | **EUPL-1.2** | **Reference-only** (EUPL poison) — Phase-0 (~40MB); no product link |
| trimstray/htrace.sh | Integrate | **GPL-3.0** | **GPL isolate REFERENCE** GuruWatcher HTTP debug — Phase-0 (~1.4MB); never link proprietary |
| githubharald/HTRPipeline | Extract | **NULL** | **NO-GO** no LICENSE |
| Nexdata-AI/1000-People-Italian-Handwriting-OCR-Data | Extract | **NULL** | **NO-GO** null SPDX / commercial dataset risk |
| Dicklesworthstone/franken_ocr | — | **MIT + OpenAI/Anthropic rider** | **GO Extract** CPU Unlimited-OCR path — Phase-0 (~219MB; operator OK over prior 500MB cap) |
| HiwinCN/HTran | Watch | NOT FOUND | **NO-GO** APT-adjacent risk |
| Remaining stub HTR demos | Reject | UNAVAILABLE / NOT FOUND | Aggregate on this page |

## Snippets

Eval Integrate set: htrace.sh + htrflow. Both blocked from product link by copyleft (GPL / EUPL). Patterns OK. [Source: GitHub Repo Revenue Analysis.docx]
