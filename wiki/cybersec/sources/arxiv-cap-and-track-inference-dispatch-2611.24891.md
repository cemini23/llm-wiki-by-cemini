---
title: "Cap-and-Track — LLM inference dispatch across shifting capacity (2611.24891)"
type: source
maturity: draft
related:
  - concepts/inference-dispatch-capacity-tracking.md
  - concepts/bluestar-tiered-agentic-cyber-defense.md
updated: 2026-11-22
---

## Raw Concept

- **Title:** Cap-and-Track: Optimizing LLM Inference Request Dispatch Across Shifting Capacity
- **Authors:** Benjamin Novotny, Doug Szeto, Chang Wang, Shicheng Chen, George Zhihua Yuan, Bob Kamma, Michael Ge, John Xin Zhou, Andrea Olgiati (Meta)
- **Type:** arXiv preprint (cs.LG)
- **Location:** `research to be indexed/cybersec/arxiv-2611.24891-cap-and-track-optimizing-llm-inference-request-d.pdf`
- **Retrieved:** 2026-11-19
- **arXiv:** 2611.24891v1, 18 November 2026
- **Read status:** read — 8 of 20 pages extracted 2026-11-22

## Narrative

A fixed dispatch rate for LLM inference goes stale. Serving fleets resize, request sizes change, and shared provider pools lose capacity. Output length is unknown at admission.

Cap-and-Track is a dispatch design. Two parts:

- **CAP** is a fail-fast admission check at the saturated resource. It refuses work before a long wait, and it surfaces overload as a refusal (HTTP 429).
- **TRACK** is a dispatch loop per capacity domain. It learns the current ceiling from CAP refusals only. It probes upward and backs off, so it follows the ceiling with no output-length prediction and no fleet-level rate to retune.

Durable priority queues hold excess work outside execution, including refused requests for retry. Each engine keeps a short queue behind its running batch, just long enough to fill batches.

Production signal: Meta's traffic shaper runs this for post and live-video understanding. In a concurrent same-traffic A/B, it served a classifier on 43% fewer H100s than its fixed-rate queued precursor. In steady-capacity replay, TRACK ran within 1% of a well-tuned fixed rate's goodput, with about a quarter of that rate's refusal share. The shaper carries more than 300 million online requests a day. It handled 1.1 billion requests in its busiest 24 hours during a backfill.

The security relevance is availability. A refusal is an admission signal, not a failure. An operator who treats 429s as errors may over-provision, and an attacker who understands the ceiling can time load to it. Logging refusal share per identity is the detector side.

[Source: arxiv-2611.24891-cap-and-track-optimizing-llm-inference-request-d.pdf]

## Snippets

> "Refusals signal the backend's current admission ceiling. ... TRACK learns the ceiling ... only from the CAP's refusals."
[Source: arXiv:2611.24891v1 abstract]
