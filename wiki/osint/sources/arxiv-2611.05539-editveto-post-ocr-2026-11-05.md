---
title: "EditVeto — a gate that reverts the corrections an LLM got wrong"
type: source
tags: [source, arxiv, ocr, historical-documents, correction, atto]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-05
updated: 2026-11-05
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Rewrite, Then Veto: Rewriter-Agnostic Edit Gating for LLM-Based Post-OCR Correction |
| Author | Jorge Ramón Fonseca Cacho (University of Nevada, Las Vegas) |
| arXiv | 2611.05539 |
| Pages | 26 |
| Read status | skimmed (abstract) |

## Narrative

**The most directly useful paper in this batch for Atto.**

### The problem, stated precisely

LLMs can repair noisy OCR transcripts of **historical documents** — but they also **change text that was already correct**. That is the exact failure that makes generative post-OCR unusable for archival work: a correction that silently alters a correct name is worse than the error it was trying to fix.

### The design

**EditVeto** places a veto gate **after** a full-context LLM rewrite.

1. The rewrite is **character-aligned** to the OCR input.
2. Its differences are split into **blocks**.
3. A **0.6B-parameter gate** keeps or reverts each block.

The gate is rewriter-agnostic — it does not care which model produced the rewrite.

### The oracle finding that motivates it

Given the true error locations, **per-span generation is worse than no correction at all**, whereas **vetoing a full rewrite's edits helps**.

That is a sharp result and it explains the whole design. Asking a model to correct only what is wrong performs badly, because it cannot see enough context to judge. Letting it rewrite everything and then **removing the edits that look wrong** works better, because the gate judges a proposed change against a full-context rewrite rather than generating in isolation.

### Results

Trained on rewrites from two Qwen3 models, evaluated frozen on eight HIPE-OCRepair-2026 test sets. The gate improves **all five rewriters tested, two of them unseen in training**: weighted cMER falls by **0.0026–0.0044**, preference score rises **0.15–0.25** (paired bootstrap, p ≈ 0.0002).

**The honest negative:** on published competition outputs it lowers cMER for three of four teams but **raises it for the winning run** (0.0050 → 0.0065). The best system is the one it hurts.

### Why the negative matters

A veto gate fixes the common case and can over-veto a system that was already good. That is the trade: it protects against corruption at the cost of occasionally reverting a correct edit.

**Caveat.** Abstract only; per-dataset figures not reproduced.

## Snippets

> "LLMs can repair noisy OCR transcripts of historical documents, but they also change text that was already correct." [Source: arxiv-2611.05539 p.1]

> "Given the true error locations, per-span generation is worse than no correction, whereas vetoing a full rewrite's edits helps." [Source: arxiv-2611.05539 p.1]

## Dead Ends

- **Assuming a veto gate is free.** It raised cMER for the strongest competitor system.
