---
title: "Robust cross-lingual RAG over OCR-degraded legislative archives"
type: source
tags: [source, arxiv, rag, ocr, document-ai]
related: []
maturity: draft
read_status: skimmed
created: 2026-10-27
updated: 2026-10-27
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Reading Beyond OCR Noise: Robust Cross-Lingual RAG for Legislative Archives |
| Authors | Radha Krishna Deshpande, Ajoy Mondal, Akash Manna, C V Jawahar — CVIT, International Institute of Information Technology, Hyderabad |
| arXiv | 2610.35240 |
| File | `arxiv-2610.35240-reading-beyond-ocr-noise-robust-cross-lingual-ra.pdf` |
| Retrieved | 2026-10-27 |
| URL | https://arxiv.org/abs/2610.35240 |
| Read status | skimmed (abstract + intro) |

## Narrative

India's historical public archives survive as degraded scanned pages. Decades of parliamentary records are multi-column, mixed-script, and dense with visual noise. The authors state that OCR failure is the primary obstacle to retrieval over this material.

The paper presents an end-to-end framework with three stages. First, a vision model segments the page layout. Second, a multi-script OCR layer extracts text from each segment. Third, an agentic retrieval-augmented generation pipeline answers questions over the extracted text.

The design point is the placement of the agent loop. The agent iterates before it generates an answer. It navigates around OCR noise and layout ambiguity instead of consuming a single noisy transcription. Errors therefore do not propagate unchecked into the answer.

The system is evaluated on the 200,000-page Punjab Vidhan Sabha archive, which mixes Hindi, Punjabi, and English. It outperforms standard text-only baselines. The abstract gives no numeric margin, so the size of the gain is unknown from this page.

The relevance to research work is direct. The same failure pattern appears in genealogy and archival OSINT: bad OCR, mixed scripts, and fragmented layout. Treating OCR as an upstream cleanup step loses information. Treating it as a retrieval-time problem, with an agent that can re-read, keeps more of the record.

All claims are single-source. The 200,000-page figure and the baseline comparison are not independently verified here.

## Snippets

> "where OCR failure is the primary obstacle to information retrieval. We present an end-to-end framework that couples vision-based layout segmentation and multi-script OCR with an agentic retrieval-augmented generation (RAG) pipeline." [Source: `arxiv-2610.35240-reading-beyond-ocr-noise-robust-cross-lingual-ra.pdf` p.1 (arXiv 2610.35240), retrieved 2026-10-27]

> "Evaluated on the 200,000-page Punjab Vidhan Sabha archive, our system demonstrates robust handling of historical document degradation, outperforming standard text-only baselines." [Source: `arxiv-2610.35240-reading-beyond-ocr-noise-robust-cross-lingual-ra.pdf` p.1 (arXiv 2610.35240), retrieved 2026-10-27]
