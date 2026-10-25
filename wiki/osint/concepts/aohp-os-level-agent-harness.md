---
title: AOHP — agent-native OS harness patterns (AOSP)
type: concept
tags: [concept, agent-harness, mobile, security, k127]
keywords: [AOHP, agent-native OS, information flow tracking, service composition, structured agent UI]
related:
  - sources/arxiv-aohp-os-agent-harness-2606.23449-2026-06-23.md
  - concepts/code-as-agent-harness.md
  - concepts/openclaw-security-taxonomy.md
  - concepts/llm-agent-systems.md
  - entities/tools/aohp-os.md
  - concepts/self-compacting-language-model-agents.md
maturity: draft
created: 2026-06-23
updated: 2026-10-25
---

## Relations

- @sources/arxiv-aohp-os-agent-harness-2606.23449-2026-06-23.md — primary source
- @concepts/code-as-agent-harness.md — laptop harness taxonomy
- @entities/tools/aohp-os.md — Apache-2.0 repo entity

## Raw Concept

Prompted by arXiv **2606.23449** (K127). Conventional OSes assume **app-centric** interaction; agents need cross-app composition, structured interfaces, and **information-flow security**.

## Narrative

**Three AOHP mechanisms (steal patterns for CCC / MCP hardening):**

1. **Service composition** — task-level entrances assembled from heterogeneous providers (analog: federation morning summary aggregating wikis)
2. **Efficient agent interfaces** — structured events/text over pixel scraping (analog: lazy-tool proxy vs raw Playwright)
3. **Secure information flow** — track sensitive values across agent context + tool calls (analog: stash tunnel + MCP allowlist)

**Posture:** REFERENCE for laptop Cursor stack — do not deploy AOSP images on prod. Repo **CONDITIONAL-GO** (Apache-2.0) for architecture study only.

## Snippets

> "Permission mechanisms enforce protections at app boundaries but fail to track sensitive data across an agent's context and tool calls." [Source: arXiv:2606.23449 §1 (retrieved 2026-06-23)]
