---
title: "Agent Audit: A Security Analysis System for LLM Agent Applications"
type: source
tags: [pdf, llm-agents, audit-security]
clusters: [llm-agents, audit-security]
related:
  - concepts/llm-agent-systems.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26
---

## Relations

- @concepts/llm-agent-systems.md — cluster hub for LLM agent-systems research in the Cemini corpus

## Raw Concept

- Original title: Agent Audit: A Security Analysis System for LLM Agent Applications
- Authors: Haiyue Zhang et al.
- Affiliation: University of Southern California
- Type: PDF, research paper (preprint/conference)
- Location: research for cemini/protocol 10 3:29.pdf
- Length: ~20 pages
- Retrieved: 2026-04-23
- Publication date: 2025
- Read status: deep-read
- Primary cluster: audit-security
- All clusters: llm-agents, audit-security

## Narrative

Agent Audit is a static analysis system for LLM agent applications. The authors build a dataflow analyzer that traces prompt-to-tool-call flows in agent code, identifying vulnerabilities like prompt injection leaking to tool arguments, tool-output feedback loops, and missing validation on LLM-generated SQL/shell/code. Evaluated on a curated set of 42 real agent-application vulnerabilities, Agent Audit catches 40 (95% recall) with a manageable false-positive rate.

The rigor is solid for a systems-security paper: real vulnerability dataset, controlled recall/precision evaluation, documented comparison to naive regex/grep-based baselines. The approach is static (no runtime instrumentation), making it suitable for pre-deployment auditing of agent code. The paper also includes a taxonomy of vulnerability classes that is more useful than most AI-security taxonomies (it's derived from actual bugs, not conjectured threats).

For Cemini: **directly adoptable**. The taxonomy can be applied to the existing agent codebase, and if the tool itself is open-sourced it's worth running against the Cemini agent layer before IP sale due diligence. USC affiliation gives it a reasonable peer-review floor. This is one of the more operationally applicable papers in the batch.

## Key findings

- Static analysis of LLM agent applications; traces prompt → tool-call dataflow.
- 40/42 real-world vulnerabilities caught (95% recall); low false-positive rate.
- Taxonomy of agent-app vulnerability classes derived from real bugs, not conjecture.
- No runtime instrumentation — fits pre-deployment CI/CD auditing.
- Directly applicable to Cemini agent-layer audit.

## Snippets

- **abstract** — "We present Agent Audit, a static analysis system that traces prompt-to-tool-call flows in LLM agent code" — the system.
- **evaluation** — "40 of 42 vulnerabilities in our curated dataset are detected" — concrete recall number.
- **deployment** — Static-only analysis makes the tool CI/CD-friendly — pre-deployment audit fits Cemini workflow.
