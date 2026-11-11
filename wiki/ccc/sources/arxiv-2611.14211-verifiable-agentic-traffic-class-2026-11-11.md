---
title: "Agentic traffic is not human web traffic — and routers have no class for it"
type: source
tags: [source, arxiv, agents, networking, qos, infrastructure]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-11
updated: 2026-11-11
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Verifiable Agentic Traffic Class: A Policed Quality-of-Service Mechanism for Agentic AI Traffic, Evaluated from Simulation to Real-Kernel Adversarial Testing |
| Authors | Naveen Babu Narayanan Nair, Sajay Kurup (Comcast) |
| arXiv | 2611.14211 |
| Pages | 20 |
| Read status | skimmed (abstract) |

## Narrative

Software agents built on LLMs **generate traffic unlike human web traffic**, yet routers have no class for it and cannot verify what they are carrying.

The paper proposes a **verifiable agentic traffic class** — a policed QoS mechanism, evaluated from simulation through **real-kernel adversarial testing**.

### Why the gap is real

Human web traffic has a shape: a page load is bursty, then quiet; a video stream is steady. An agent's traffic is a different animal — long thinking pauses, then a burst of tool calls, then a large context upload. From the network's side it looks like either an idle connection or an anomaly, depending on the moment.

QoS classes are built for the shape of traffic they know. An unclassified pattern gets default treatment, which for an agent means unpredictable latency on the calls that matter.

### The verifiable part

The interesting word is **verifiable**. A traffic class that a client merely *declares* can be spoofed. One that the network can *check* cannot. That is the same claim-versus-evidence distinction this workspace keeps encountering.

**Relevance here.** Marginal for a laptop workflow. Relevant if CeminiSuite ever puts an agent behind a network path with QoS rules — and relevant as another instance of "the thing being declared is not the thing being verified".

**Caveat.** Abstract only; no policing accuracy or latency figures.

## Snippets

> "Software agents built on large language models generate traffic unlike human web traffic, yet routers have no class for it and cannot verify what they are carrying." [Source: arxiv-2611.14211 p.1]

## Dead Ends

- **Reading this as relevant to a local workflow.** It is a network-layer concern.
