---
title: Arabic HTR as evidence review — Athar/Phoenix steal for Atto
type: concept
tags: [htr, atto, evidence, continual-learning]
keywords: [greedy_text, unique-ambiguous-abstain, forgetting-guards, human-only-GT, no-silent-LM]
related:
  - sources/arxiv-2608.19385-phoenix-athar-arabic-htr.md
  - concepts/computational-genealogy-archival-automation.md
  - concepts/gpuology-genealogy-agent-kit.md
maturity: draft
created: 2026-08-21
updated: 2026-08-21
---

## Relations
- @sources/arxiv-2608.19385-phoenix-athar-arabic-htr.md
- @concepts/computational-genealogy-archival-automation.md
- @concepts/gpuology-genealogy-agent-kit.md

## Raw Concept
Scholarly / genealogical HTR is not a text-replacement API. A compact visual recognizer (Phoenix-class CNN–BiLSTM–CTC) can be multi-domain if replay + forgetting guards select checkpoints. Remaining error is often *in the N-best list already* (Athar oracle gap ~2.15 CER) and learned rerankers do not close it. Therefore the product is an evidence panel: preserve greedy visual reading, expose bounded alternatives, retrieve with unique/ambiguous/abstain, export only human-approved GT.

## Narrative
Atto should steal the *workflow invariants*, not the Baghdad checkpoint as a drop-in (CC BY-NC-SA 2.0; Arabic-manuscript specialist).

Invariants:
1. **`greedy_text` is sacred.** Store the visual CTC greedy even when a domain LM or human accepts another reading. Reversible. Hashes bind model, image, polygon, decoder.
2. **Retrieval is three-state.** unique / ambiguous / abstain. Truncation forbids uniqueness. A repeated formula is not provenance.
3. **Human-only training export.** Unreviewed model output and source matches never become GT. Avoids a self-training loop.
4. **Replay + forgetting guards.** New-domain gain with a budgeted regression cap on prior domains. Do not route a zoo of specialists for 0.07–0.44 pp.
5. **No silent LM overwrite.** Domain-matched LM can help; mismatched LM harms. LM is labelled evidence.

Fits computational-genealogy archival automation (PAGE-XML/TEI, human review queue) and GPU-light local kits (4.99M, 20 MB). Candidate-selection research is future work, not a phase-0 clone.

## Snippets
See @sources/arxiv-2608.19385-phoenix-athar-arabic-htr.md for sealed CER 19.98%→14.93%, Oracle@25 gap, and licence.
