---
title: harvo — harness-adapter evolution for domain specialization
type: entity
related:
  - sources/arxiv-beyond-weight-updates-evolving-agent-harnesses-2611.25380.md
  - concepts/harness-adapter-frozen-policy-specialization.md
maturity: draft
updated: 2026-11-22
---

## Raw Concept

Entity page for Harvo. Prompted by `@sources/arxiv-beyond-weight-updates-evolving-agent-harnesses-2611.25380.md`.

## Narrative

- **Repo:** https://github.com/bhaochen/harvo
- **Weights/artifacts:** https://huggingface.co/bhaochen/harvo
- **Author:** BoHao Chen (independent).
- **Scope:** harness adapters produced by GEPA, a reflective evolutionary optimizer. The policy stays frozen; the adapter edits the system prompt, tool schemas, skill library and planning scaffolding per vertical domain.

### Reported results

Tested with Codev, a Claude Code-style coding agent, on SWE-bench Verified, OfficeBench and Terminal-Bench. Harness evolution recovers most of a weight update's gain at a small fraction of the compute; both together are best. [TENTATIVE] single independent author.

### Fit for Cemini

WATCH. The cheap experiment is a harness adapter per `/route` lane, before any fine-tune. [OPEN QUESTION 2026-11-22] Licence not checked; run a Phase-0 audit before use. See `@concepts/harness-adapter-frozen-policy-specialization.md`.
