---
title: "When Context Gets Root — instruction privilege escalation in LLM harnesses (arXiv 2608.27299)"
type: source
tags: [arxiv, k248, cyber, harness, privilege-escalation]
keywords: [context-root, instruction-privilege, LLM-harness, escalation]
related:
  - concepts/k248-cyber-agent-security-wave.md
maturity: draft
created: 2026-08-28
updated: 2026-08-28
read_status: read
---

## Relations

- @concepts/k248-cyber-agent-security-wave.md — K248 cyber privilege-escalation cluster

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.27299, When Context Gets Root: Privilege Escalation in LLM Harnesses |
| Retrieved | 2026-08-28 |
| File | `arxiv-2608.27299-when-context-gets-root-privilege-escalation-in-l.pdf` |
| sha256 | `477c338f0ec5fe574bc15c5e622c95daa1ace16acd8081be555584d451263222` |
| Dual-ID | **OSINT K248** → cybersec wiki brief |

## Narrative

This paper frames **instruction privilege escalation** inside LLM agent harnesses: untrusted or lower-privilege context content can climb into **root**-equivalent tool or system authority. Evaluation covers **13 objectives × 6 harnesses**. Operational steal for CCC/cyber: treat context channels (files, MCP, web, memory) as privilege domains with explicit demotion, not as flat prompt paste. Pair with Framing Gap allow-list / planner-reader controls. Wiki stores methodology notes only — **no exploit PoC**.

## Snippets

> "13 objectives × 6 harnesses — when context gets root." [Source: arxiv-2608.27299-when-context-gets-root-privilege-escalation-in-l.pdf (retrieved 2026-08-28)]
