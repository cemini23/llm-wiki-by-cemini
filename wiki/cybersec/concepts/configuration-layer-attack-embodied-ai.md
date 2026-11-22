---
title: "Configuration-layer attack on embodied AI — the interface under the model"
type: concept
maturity: draft
related:
  - sources/arxiv-network-exposed-config-attacks-social-robots-2611.22761.md
  - concepts/physical-vs-content-danger-embodied-agents.md
  - concepts/zero-trust-mission-critical-robotic-fleets.md
  - concepts/network-security.md
  - concepts/agent-runtime-guardrails.md
updated: 2026-11-22
---

## Raw Concept

What this page answers: where is the security boundary on a cloud-LLM robot, and what happens when an attacker changes the system prompt without touching the chat channel? From 2611.22761.

## Narrative

A cloud-LLM robot needs constant network connectivity. Consumer deployments use WiFi, on a shared local network. The robotics stack usually runs a local companion app, on Gradio or FastAPI, so an operator can configure behaviour from a browser. If that app binds to all interfaces without authentication, the network adjacency becomes an attack surface.

The measured case is the Pollen Robotics Reachy Mini Lite. Two personality-management endpoints on `0.0.0.0:7860` accept unauthenticated POST requests. Two requests rewrite the personality configuration, including the system prompt sent to the cloud LLM. The attack takes under two seconds, needs no credentials, and survives restart in the local case.

The contrast matters. Eleven direct prompt-injection attempts across five categories were resisted at the LLM layer. Both configuration-layer paths worked. Inference-layer alignment does not cover unauthorized modification of the instructions.

Mapping: CWE-306 (missing authentication for a critical function), CWE-1327 (binding to an unrestricted IP address), CVSS 6.5. One endpoint also answers cross-origin without a CORS preflight (CWE-352, CSRF, 6.5).

Prevalence caveat: 10 of 11 source-verifiable public apps show the same missing-authentication pattern. That is a developer-mechanism finding, not a commercial-product prevalence measure.

**Harm model for a co-located agent.** The robot has a camera and a microphone. A changed prompt can become passive surveillance. The same channel can socially engineer the trusted humans around the robot, in a nursing home, school, or hospital.

**Control checklist.** Bind management interfaces to loopback or a private management network. Require authentication on every configuration endpoint. Send CORS preflight and reject cross-origin writes. Enforce the memory store's stated restrictions in code. Treat the system prompt as a protected configuration asset with change logging.

[Source: arxiv-2611.22761-network-exposed-configuration-attacks-on-llm-con.pdf]

## Snippets

> "Network adjacency on its own is not the vulnerability; it becomes an attack surface only because that companion interface is bound to the network without authentication."
[Source: arXiv:2611.22761v1 §1]
