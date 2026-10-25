---
title: Experiential Labs — zero-retention LLM gateway and uncensored overflow
type: entity
tags: [tool, cybersec, gateway, llm-routing, guruwatcher]
keywords: [experiential labs, exp CLI, glm-5.3-flash-uncensored, deepseek-v4.1-flash, zero retention]
related:
  - ../../osint/sources/eval-multi-wiki-link-revenue-v10.9-2026-10-25.md
maturity: draft
created: 2026-10-25
updated: 2026-10-25
phase_0_verdict: CONDITIONAL-GO
wire_status: pending
wire_note: Pin glm-5.3-flash-uncensored for sensitive work. deepseek-v4.1-flash-uncensored is NOT zero retention.
---

## Raw Concept

Phase-0 on experientiallabs.ai and its open-source gateway, 2026-10-25. Source: v10.9 multi-wiki link evaluation, URL 15, scored Extract (Cybersec primary) for local-abliterated-lab, guruwatcher, atto.

## Narrative

| Field | Value |
|-------|-------|
| **Site** | https://www.experientiallabs.ai/ |
| **Gateway repo** | https://github.com/experientiallabs/experiential |
| **License** | Apache-2.0 (gateway). Hosted tiers commercial. |
| **Last commit** | 2026-10-09 (gateway clone, verified) |
| **Size** | 35 MB / 1536 files |
| **Verdict** | CONDITIONAL-GO |

### Two separate offers

**1. The gateway.** `exp` CLI, Apache-2.0, openai/anthropic-compatible, loopback data plane. Verified present in the clone. Adds per-customer cost tagging (`X-Explabs-Tags`) and synthetic trace replay.

**2. Hosted models.** Flat-rate routing. The two that matter here:

| Model | Context | Retention | Use |
|-------|---------|-----------|-----|
| `glm-5.3-flash-uncensored` | 1M tokens | **zero on every route** | security audits that exceed local VRAM |
| `deepseek-v4.1-flash` | — | **not zero retention** | claim and parameter extraction only |

### The trap in the source report

The report pairs these two models in one combo play. They do not share a retention guarantee. Treating them as interchangeable would send confidential audit material to a retaining endpoint.

**Rule:** local-abliterated-lab pins `glm-5.3-flash-uncensored` or local weights. Never `deepseek-v4.1-flash-uncensored`.

### Where it lands

- **local-abliterated-lab** — 1M-context overflow when a codebase exceeds local VRAM.
- **GuruWatcher** — newsletter claim extraction. Report claims a trace-replay judge scored deepseek-v4.1-flash at 0.93 against claude-sonnet-5.5 at 0.94 across 1,200 replayed tickets. [TENTATIVE] vendor claim, not independently verified.
- **Atto** — gateway benchmarking on synthetic Rossi fixtures only.

### Unverified

Hosted SLA and latency under 15-minute polling from cemini-egress-fi. Nobody has measured it.

## Snippets

> "glm-5.3-flash-uncensored specifies 'Zero on every route' for provider retention, deepseek-v4.1-flash-uncensored explicitly notes 'Not zero retention'" — source report, URL 15

## Dead Ends

- Treating the two `-uncensored` models as equivalent on retention. They are not.
- Sending real `~/AttoVault/` PII to a hosted trace-replay endpoint. Synthetic fixtures only.
