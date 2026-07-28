---
title: "Transcription → Semantic Corpus Analysis (arXiv 2607.24542)"
type: source
tags: [source, arxiv, genealogy, htr, atto, k198]
keywords: [TSDAE, CSE, sentence embeddings, Latin, Ancient Greek, HTR noise]
related:
  - concepts/historical-document-kg-query-inference.md
  - concepts/computational-genealogy-archival-automation.md
  - concepts/gpuology-genealogy-agent-kit.md
maturity: draft
read_status: read
created: 2026-07-28
updated: 2026-07-28
clusters: [k198-ingest]
---

## Relations

- @concepts/historical-document-kg-query-inference.md
- @concepts/computational-genealogy-archival-automation.md
- @concepts/gpuology-genealogy-agent-kit.md

## Raw Concept

| Field | Value |
|-------|-------|
| **Filename** | `arxiv-2607.24542-from-transcription-to-semantic-corpus-analysis-u.pdf` |
| **sha256** | `382c20f690b74a9d19745fff6487edf74aef992e17de98099aeff35b15392cc2` |
| **arXiv** | [2607.24542](https://arxiv.org/abs/2607.24542) |
| **Tool** | Paraphrasis (online) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.24542-from-transcription-to-semantic-corpus-analysis-u.pdf` |

## Narrative

Unsupervised TSDAE + contrastive sentence embeddings adapt token LMs for Latin/Ancient Greek reuse detection (2,935 expert parallels). CSE optimum at 4–8k in-domain sentences (~laptop GPU tens of seconds); transfers to noisy post-ATR text when retrained on it.

**Steal (Atto):** unsupervised sentence encoders on Antenati/parish HTR dumps for fuzzy reuse / parallel search — no LLM-NAS; keep Transkribus/HTR + embedding layer.

## Snippets

> "CSE … reaches its optimum with as few as 4–8k raw in-domain sentences"
