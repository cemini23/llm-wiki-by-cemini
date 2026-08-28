---
title: "The Framing Gap — IPI exfiltration via reframing (arXiv 2608.27092)"
type: source
tags: [arxiv, k248, cyber, ipi, llm-security]
keywords: [Framing-Gap, indirect-prompt-injection, exfiltration, SecAlign, allow-list]
related:
  - concepts/k248-cyber-agent-security-wave.md
maturity: draft
created: 2026-08-28
updated: 2026-08-28
read_status: read
---

## Relations

- @concepts/k248-cyber-agent-security-wave.md — K248 cyber IPI / harness privilege cluster

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.27092, The Framing Gap: Indirect Prompt Injection Exfiltration |
| Retrieved | 2026-08-28 |
| File | `arxiv-2608.27092-the-framing-gap-indirect-prompt-injection-exfilt.pdf` |
| sha256 | `5e90325a195c120b11761d855d01069d5897fed099ae990ffa82d219d1d5bae6` |
| Dual-ID | **OSINT K248** → cybersec wiki brief |

## Narrative

The Framing Gap paper studies **indirect prompt injection (IPI)** that exfiltrates data by **reframing** tool or content context rather than classic jailbreak strings. Headline result: **gpt-4o** moves from **0% → 100%** attack success when the same intent is reframed. Mitigations that close the gap in their setting: **destination allow-list** and **planner–reader split**. **SecAlign** does **not** close the gap. For Cemini / cyber lab: treat allow-lists and planner-reader separation as higher-priority harness controls than alignment-only patches. No attack PoC reproduced in this wiki.

## Snippets

> "gpt-4o 0%→100% via reframing; destination allow-list / planner-reader split close gap; SecAlign does not." [Source: arxiv-2608.27092-the-framing-gap-indirect-prompt-injection-exfilt.pdf (retrieved 2026-08-28)]
