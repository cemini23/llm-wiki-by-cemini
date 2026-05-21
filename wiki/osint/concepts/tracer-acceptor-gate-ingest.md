---
title: TRACER Acceptor Gate — ML Surrogate Routing for LLM Cost Reduction in OSINT Ingest
type: concept
tags: []
keywords: []
related:
  - entities/tools/tracer.md
maturity: draft
created: 2026-05-15
updated: 2026-05-15
cross-wiki-source: "@osint-wiki/entities/tools/tracer.md"
---

# TRACER Acceptor Gate — ML Surrogate Routing for LLM Cost Reduction in OSINT Ingest

## Relations

- @osint-wiki/entities/tools/tracer.md  (cross-wiki source)

## Raw Concept

Cross-wiki stub routed from `@osint-wiki/entities/tools/tracer.md` during ingest.
What prompted this page + which sources synthesize into it — fill in on next
ingest pass.

## Narrative

TRACER uses fast traditional ML surrogates (LightGBM, logistic regression) with a calibrated Acceptor Gate to deflect 90%+ of routine classification tasks away from expensive LLM calls. The Acceptor Gate provides a statistical parity guarantee: when the surrogate is confident, route to cheap ML; when uncertain, escalate to LLM.

In the OSINT wiki ingest pipeline context, this pattern directly reduces token costs during mass ingestion of unstructured threat-actor data streams. The continual learning flywheel autonomously expands surrogate coverage over time as more classification examples accumulate.

Key extraction: (1) train a LightGBM surrogate on past ingest classification decisions (entity vs concept vs source, maturity tier, cross-wiki routing target), (2) deploy the Acceptor Gate with a calibrated confidence threshold, (3) escalate to LLM only when the surrogate is uncertain, (4) log LLM decisions to expand the surrogate's training set. Expected cost reduction: 90% on routine classification during batch ingest.

MIT license, grounded in a 2026 arXiv paper. Source: @osint-wiki/entities/tools/tracer.md (K45 multi-wiki tool eval v3, Steal-from tier, PASS 100).
