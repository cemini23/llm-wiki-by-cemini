---
title: "QomolangmaH/SpikeHTR"
type: entity
tags: [tool, phase-0, k222, atto, htr]
keywords: [Spike-HTR, Apache-2.0, SNN, InkCoder, Transkribus]
related:
  - sources/arxiv-2608.01646-spike-htr.md
  - entities/tools/transkribus.md
  - entities/tools/simplehtr.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/cemini-license-posture.md
  - concepts/gpuology-genealogy-agent-kit.md
maturity: draft
created: 2026-08-04
updated: 2026-08-04
harness_verb: FILE
---

## Relations

- @sources/arxiv-2608.01646-spike-htr.md
- @entities/tools/transkribus.md — sole product HTR (this repo is REFERENCE)
- @entities/tools/simplehtr.md — CTC / blank-reduce kinship
- @concepts/wiki-tooling-evaluation.md
- @concepts/cemini-license-posture.md
- @concepts/gpuology-genealogy-agent-kit.md

## Narrative

| Field | Value |
|-------|--------|
| **Repo** | https://github.com/QomolangmaH/SpikeHTR |
| **License** | **Apache-2.0** [CONFIRMED gh 2026-08-04] |
| **Verdict** | **GO REFERENCE** (Atto) |
| **Local** | `.local/adopts/SpikeHTR` (~8.3MB shallow) |
| **Route** | Atto — efficiency / InkCoder / CTC length-reducer patterns only |
| **wire_status** | `policy_wired` |

Spiking neural transformer HTR from arXiv 2608.01646. **Do not** replace Transkribus as product HTR. No Barone PII in SpikeHTR fixtures; Magika still sniffs vault blobs before any local experiment.
