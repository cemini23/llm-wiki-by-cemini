---
title: "AI-Trader (HKUDS) — Brokerage API Agent Bridge"
type: entity
tags: [tool, trading-agent, fastapi, ibkr, steal-from, k38]
keywords: [ai, trader, hkuds, steal-from, three-surface-eval]
related:
  - sources/link-evaluation-brief-trading-stack.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/link-evaluation-brief-trading-stack.md` — source evaluation brief (URL 10)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `github.com/HKUDS/AI-Trader`
- **Tier (per source brief)**: **Steal-from**
- **License**: [NEEDS VERIFICATION 2026-05-11] License needs verification.

## Narrative

Multi-layer trading app: FastAPI Python backend + React frontend. Background workers decouple user-facing latency from settlement/intelligence tasks. Bridges Claude Code / OpenClaw to major brokerage APIs (incl. Interactive Brokers).

### Integration vector

Steal-from: extract Python FastAPI **Interactive Brokers integration logic** and **background-worker isolation pattern**. Discard the React frontend (Cemini is headless).

### Risks

Brokerage APIs are notoriously volatile — IBKR integration must be cross-checked against current official IBKR API docs before any port.

[Source: Link Evaluation Brief Trading Stack.docx, URL 10]
