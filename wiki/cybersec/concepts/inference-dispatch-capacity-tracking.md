---
title: "Inference dispatch by capacity, not by a fixed rate — refusals as the admission signal"
type: concept
maturity: draft
related:
  - sources/arxiv-cap-and-track-inference-dispatch-2611.24891.md
  - concepts/bluestar-tiered-agentic-cyber-defense.md
  - concepts/docker-agent-sandbox-allowlist-proxy.md
updated: 2026-11-22
---

## Raw Concept

What this page answers: how does a large LLM serving fleet dispatch work when capacity shifts? From 2611.24891 (Meta Cap-and-Track).

## Narrative

A fixed dispatch rate for LLM inference becomes stale. Fleets resize, request size changes because output length is unknown at admission, and shared provider pools lose capacity. A rate set above capacity causes timeouts. A rate below capacity idles GPUs.

Cap-and-Track has two parts:

- **CAP** — a fail-fast admission check at the saturated resource. It refuses work before a long wait and reports overload as an HTTP 429.
- **TRACK** — a dispatch loop per capacity domain. It learns the ceiling from CAP refusals alone. It probes up and backs off. It needs no output-length prediction and no rate to retune.

Durable priority queues hold excess work outside execution, including refused requests for retry. Each engine keeps a short queue behind its running batch, just long enough to fill batches.

**Production figures.** Meta's traffic shaper runs this for post and live-video understanding. In a same-traffic A/B, it served a classifier on 43% fewer H100s than its fixed-rate precursor. In steady-capacity replay, it ran within 1% of a well-tuned fixed rate's goodput, with about a quarter of that rate's refusal share. Over 300 million online requests a day, and 1.1 billion in its busiest 24 hours.

**Security and operations reading.**

- A refusal here is an admission signal, not an error. An operator who counts 429s as failures will over-provision.
- A sustained rise in refusal share per identity is a load signal. Log it per identity, not only fleet-wide.
- A short queue bounds the blast radius of a traffic spike. Unbounded queues turn load into timeouts and dropped connections.
- Capacity ceilings are knowable from outside by timing. Treat load shape as observable metadata.

**Caveat.** Meta's workloads are their own. The failure modes are generic; the numbers are not transferable.

[Source: arxiv-2611.24891-cap-and-track-optimizing-llm-inference-request-d.pdf]

## Snippets

> "The shaper carries more than 300 million online requests and hundreds of terabytes of media a day. During a backfill, it handled 1.1 billion requests in its busiest 24 hours."
[Source: arXiv:2611.24891v1 abstract]
