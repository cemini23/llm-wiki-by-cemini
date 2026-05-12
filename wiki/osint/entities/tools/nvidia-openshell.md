---
title: "NVIDIA OpenShell — Containerized Agent Sandbox Runtime"
type: entity
tags: [tool, agent-sandbox, container, security, nvidia, steal-from, k39, phase-0-pending]
keywords: [nvidia openshell, agent sandbox, docker policy, network isolation, declarative policy, apache-2.0]
related:
  - sources/evaluating-project-links-stacks.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/evaluating-project-links-stacks.md` — source evaluation brief (URL 4)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL** (per source brief): `github.com/NVIDIA/OpenShell` (release v0.0.37)
- **Tier (per source brief)**: **Steal-from**
- **License** (per source brief): Apache-2.0
- **Stack**: Python CLI (`uv tool install openshell`), Docker container runtime, declarative YAML policies, optional NVIDIA GPU acceleration
- **Maturity** (per source brief): v0.0.37; Copyright 2025-2026 NVIDIA Corporation

## Narrative

Containerized runtime for safely executing autonomous AI agents in restricted, transient sandboxes. Declarative YAML policies restrict file access, network egress, and outbound API activity. Predefined sandboxes (Ollama, OpenClaw, base). Apache-2.0 with explicit patent retaliation clauses (favorable for enterprise acquirers).

### Integration vector

**Steal-from**: extract the declarative-policy schemas (file-access + network-egress rules) and manually port to harden existing FastMCP Python Docker containers. **Do not deploy** OpenShell wholesale — Docker-in-Docker abstraction is too fragile for 24/7 trading; 40-container Hetzner host already at file-descriptor / inode pressure.

### NEEDS VERIFICATION

- Confirm this is the real NVIDIA-published repo (v0.0.37 only — verify on `github.com/NVIDIA/OpenShell` directly)
- Execution-latency overhead per FastMCP tool call when wrapped in a transient OpenShell sandbox
- Whether declarative-policy schemas can be lifted standalone without the runtime

### Phase-0 audit status

Not yet performed. Phase-0 priority MEDIUM — confirm repo authenticity + license file before any policy-schema extraction.

[Source: Evaluating Project Links for Stacks.docx URL 4; retrieved 2026-05-11]
