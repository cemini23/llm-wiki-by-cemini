---
title: "Chaosblade — Chaos Engineering Toolkit for Docker Compose"
type: entity
tags: [tool, chaos-engineering, resilience, docker, testing, infrastructure]
keywords: [chaosblade, chaos engineering, Docker, fault injection, resilience testing, Alibaba]
related:
  - sources/project-link-evaluation-brief-5_10.md
  - concepts/tool-evaluation-framework.md
maturity: draft
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@sources/project-link-evaluation-brief-5_10.md` — source evaluation brief (URL 12)

## Raw Concept

Chaosblade is a versatile chaos engineering toolkit that injects targeted faults into distributed systems without requiring Kubernetes. Supports OS-level (CPU/memory/network), JVM, C++, and Docker container fault injection.

- **Repo**: `github.com/chaosblade-io/chaosblade`
- **License**: Apache-2.0
- **Stack**: Go 77.2%, Shell 8.9%
- **Maturity**: 6.3k stars, v1.8.0 (Oct 2025)

## Narrative

Unlike Kubernetes-bound alternatives (Chaos Mesh, Litmus), Chaosblade uses a flexible execution model targeting raw Docker containers, OS resources, and application-level agents. The `blade` CLI dynamically simulates CPU spikes, memory exhaustion, network latency, and disk I/O faults.

### Integration vectors

- **Cemini prod (Adopt)**: Schedule `blade` CLI chaos experiments during non-critical market hours (e.g., weekend maintenance windows). Test how Polygon ingest and FastMCP orchestrator handle sudden WebSocket drops, database latency spikes, and CPU throttling.
- **Workflow (Adopt)**: Use Claude Code to draft automated `blade` execution scripts for local backtesting resilience validation.

### Risks

- **Production safety**: Executing `tc` (traffic control) or `iptables` network fault injection on a live trading machine during active hours could trigger cascading timeouts in Hyperliquid/Alpaca execution paths → financial loss. Must be strictly time-gated.
- **Not K8s-native**: If Cemini ever migrates to Kubernetes, the K8s-specific chaos tools (Chaos Mesh, Litmus) would need re-evaluation.

### Cemini significance

The only chaos engineering tool that passed all evaluation gates. Docker Compose-native, Apache-2.0, Go binary with minimal footprint. Provides resilience validation for the 40-container trading infrastructure without the Kubernetes dependency that eliminated all alternatives.

[Source: Project Link Evaluation Brief 5_10.docx, URL 12]
