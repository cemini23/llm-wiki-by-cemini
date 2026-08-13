---
title: smolvm — portable hardware-isolated microVMs for agents
type: entity
tags: [entity, tool, microvm, sandbox, cyber, k235, integrate-conditional]
keywords: [smolvm, microVM, KVM, WHP, smolmachine, agent-sandbox, ssh-agent]
related:
  - sources/deep-research-url-evaluation-2026-08-13.md
  - entities/tools/benchflow-artifacts.md
maturity: draft
created: 2026-08-13
updated: 2026-08-13
---

## Relations

- @sources/deep-research-url-evaluation-2026-08-13.md — K235 eval: Integrate (local-abliterated-lab)
- @entities/tools/benchflow-artifacts.md — combo: repo-scrub inside microVM before agent ingest

## Raw Concept

Repo `smol-machines/smolvm` (Rust/C++, Linux KVM/WHP). Sub-200ms, stateful, hardware-virtualized environments packaged as portable `.smolmachine` files — VM-grade isolation with container-grade speed, designed for AI coding agents. License: **NOT FOUND** (docx) — unverified this session → no clone.

## Narrative

**Verdict: Integrate-conditional (local-abliterated-lab) — license blocked.** The use case is strong (untrusted agent execution on lab hardware; the docx combo of benchflow repo-scrub + smolvm sanitizing untrusted payloads before Claude/Cursor ingest). But: no SPDX verification possible → **no clone, no wiring** until license is pinned; then HITL. Two hard constraints regardless: (1) **disable `--ssh-agent` forwarding** — guest signing with host credentials is the critical risk called out in the docx; (2) virtio-gpu stability for intensive workloads unverified.

[Source: smol-machines/smolvm (retrieved 2026-08-13); Deep Research URL Evaluation.docx]
