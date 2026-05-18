---
title: "chandra — vision-language document-parsing model (OCR → structured HTML/JSON)"
type: entity
tags: [entity, tool, ocr, document-parsing, vision-language-model, ingest-pipeline, adopt, k50]
keywords: [chandra, datalab-to, vlm, ocr, document-parsing, pdf-to-json, vllm, olmocr, apache-2.0, openrail-m, ingest-pipeline]
related:
  - sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md
maturity: draft
created: 2026-05-17
updated: 2026-05-17
phase_0_verdict: ADOPT (doc-level) 2026-05-17 — Apache-2.0 code verified in report; Phase-0 clone audit + deployment-feasibility check (4B model needs vLLM/GPU) pending before integration
---

## Relations

- @sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md — evaluated in the 56-repo multi-wiki tool eval (Adopt tier, OSINT primary fit)

## Raw Concept

Promoted from the 2026-05-17 "Multi-Wiki Tool Evaluation & IP-Sale Risk Assessment" 56-repo eval. Tier: **Adopt**. Primary fit: OSINT-wiki. Cross-route noted: CCC (local vLLM API integration pattern), Cemini-financial (parsing unstructured financial statements).

- URL: https://github.com/datalab-to/chandra
- License: **Apache-2.0** (inference code) / **OpenRAIL-M** (model weights — use-restricted)
- Stars / last commit / open issues: 10.7k / ~3 weeks ago / NOT FOUND (per report)
- Stack: Python / Hugging Face / vLLM

## Narrative

**chandra** is a ~4B-parameter open-source **vision-language model** built to convert unstructured visual data — complex tables, cursive handwriting, PDFs — into cleanly structured **HTML or JSON**. The report cites state-of-the-art benchmark performance (85.9% on olmOCR) and heavy community adoption (10.7k stars, active development).

**Cemini fit**: an OCR / document-parsing front-end for the **ingest pipeline** — turning scanned filings, screenshots, and PDF reports into structured text the wiki and kb-server REST API can consume (the report's example: parsed financial statements / threat-actor financial profiles). The inference code is Apache-2.0 — clean for the IP sale. The model **weights** carry a modified **OpenRAIL-M** license: use-restricted but compliant for self-hosting under the report's stated <$2M-revenue threshold.

**Deployment caveat**: chandra is a 4B VLM and runs via **vLLM** — it wants a GPU. The cemini-librarian is a small CPU-only Hetzner box, so chandra is **not** a drop-in librarian adoption; it would need a GPU host or batch/offline runs. Treat it as a candidate ingest-pipeline enhancement, not an immediate install.

- `[NEEDS VERIFICATION 2026-05-17]` Phase-0 clone audit: confirm the Apache-2.0 LICENSE file + the OpenRAIL-M weight-license terms; benchmark a realistic deployment path (GPU host vs offline batch) given the no-GPU librarian.

## Snippets

> "Chandra is a formidable 4B-parameter open-source vision-language model explicitly engineered to transform unstructured visual data—including complex tables, cursive handwriting, and PDFs—into perfectly structured HTML or JSON outputs ... The underlying inference code is fully licensed under Apache-2.0 ... The model weights utilize a modified OpenRAIL-M license, which remains compliant for self-hosting and entities generating under $2M in revenue." [Source: Multi-Wiki Tool Evaluation.docx — URL 10]
