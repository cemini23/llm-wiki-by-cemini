---
title: "Network-exposed configuration attacks on LLM-controlled social robots (2611.22761)"
type: source
maturity: draft
related:
  - concepts/configuration-layer-attack-embodied-ai.md
  - concepts/physical-vs-content-danger-embodied-agents.md
  - concepts/zero-trust-mission-critical-robotic-fleets.md
  - concepts/network-security.md
updated: 2026-11-22
read_status: read
---

## Raw Concept

- **Title:** Network-Exposed Configuration Attacks on LLM-Controlled Social Robots
- **Authors:** Stanley Akingbola, Ugbede Ibrahim, Yan Lin Aung, Quang Dan Le, Hong Qing Yu (University of Derby)
- **Type:** arXiv preprint (cs.CR)
- **Location:** `research to be indexed/cybersec/arxiv-2611.22761-network-exposed-configuration-attacks-on-llm-con.pdf`
- **Retrieved:** 2026-11-18
- **arXiv:** 2611.22761v1
- **PoC and survey:** https://bit.ly/reachypi
- **Read status:** read — 8 pages extracted 2026-11-22

## Narrative

The paper studies a class of attack that does not touch the model's chat input. It attacks the infrastructure under the model.

The target is the Pollen Robotics Reachy Mini Lite. The robot host runs a companion application on Gradio, bound to 0.0.0.0:7860. Two personality-management endpoints are unauthenticated. Any device on the same network can send two HTTP POST requests and rewrite the system prompt that the cloud LLM receives. The attack takes under two seconds, needs no credentials, and persists across restart in the local case.

The contrast with the chat channel is the finding. Eleven direct prompt-injection attempts across five categories were resisted at the LLM layer. Both configuration-layer paths succeeded and produced visible behaviour changes on the physical hardware.

The authors map the flaws to CWE-306 (missing authentication for a critical function) and CWE-1327 (binding to an unrestricted IP address). The CVSS v3.1 score is 6.5 (Medium). One endpoint is also reachable cross-origin without a CORS preflight (CWE-352, CSRF, also 6.5). The robot's persistent-memory sink stores content without enforcing its own stated restrictions.

A source-verified survey of 59 public repositories finds the same missing-authentication pattern in 10 of 11 genuinely source-verifiable applications, or 11 of 11 counting a framework-default case. The authors are careful: this shows the mechanism recurs among developers, not commercial-product prevalence.

The harm is physical and social. A co-located robot has a camera and a microphone, so a changed prompt can become passive surveillance. It can also be used to socially engineer the humans who trust it.

[Source: arxiv-2611.22761-network-exposed-configuration-attacks-on-llm-con.pdf]

## Snippets

> "Inference-layer refusal does not compensate for unauthorised modification of the model's instructions."
[Source: arXiv:2611.22761v1 abstract]

## Dead Ends

- None recorded.
