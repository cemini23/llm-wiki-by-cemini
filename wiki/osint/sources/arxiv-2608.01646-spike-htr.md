---
title: "arXiv 2608.01646 — Spike-HTR (spiking neural transformer HTR)"
type: source
tags: [arxiv, htr, genealogy, atto, k222]
keywords: [Spike-HTR, SNN, CTC, IAM, InkCoder, Transkribus]
related:
  - entities/tools/spike-htr.md
  - entities/tools/transkribus.md
  - entities/tools/simplehtr.md
  - concepts/gpuology-genealogy-agent-kit.md
maturity: draft
created: 2026-08-04
updated: 2026-08-04
read_status: deep-read
---

## Relations

- @entities/tools/spike-htr.md — Phase-0 Apache REFERENCE clone
- @entities/tools/transkribus.md — sole product HTR (Spike-HTR does not replace)
- @entities/tools/simplehtr.md — CTC / length-reduce kinship
- @concepts/gpuology-genealogy-agent-kit.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Spike-HTR: Spiking Neural Transformer for Handwritten Text Recognition |
| Authors | Xiubo Liang et al. (Zhejiang / NetEase) |
| arXiv | 2608.01646 |
| Code | https://github.com/QomolangmaH/SpikeHTR (Apache-2.0) |
| sha256 | `49707682f29c688472b4de74ace015499c3d9f58abbe97a5e56d2e632211e5d5` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.01646-spike-htr-spiking-neural-transformer-for-handwri.pdf` |
| retrieved | 2026-08-04 |
| read_status | deep-read |

## Narrative

Hybrid SNN HTR: **InkCoder** turns a static page into a short coarse-to-fine spike stream; a CTC-guided length reducer drops blank-dominated width positions before deep mixing. With T=2, no LM/lexicon, reported CERs IAM 3.5/5.4, LAM 2.3/2.5, READ2016 4.2/3.9 (val/test).

**Atto:** Phase-0 ADOPT **REFERENCE** only (`.local/adopts/SpikeHTR` ~8.3MB). Steal efficiency / blank-compression ideas for correction UX research — **Transkribus remains sole product HTR**.

## Snippets

> Codes are available at https://github.com/QomolangmaH/SpikeHTR. [Source: arXiv 2608.01646]
