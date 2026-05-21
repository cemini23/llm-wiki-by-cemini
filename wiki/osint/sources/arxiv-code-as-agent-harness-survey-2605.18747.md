---
title: "Code as Agent Harness — survey (arXiv:2605.18747)"
type: source
tags: [source, arxiv, agent-harness, coding-agents, survey, k48]
keywords: [code-as-agent-harness, executable-agents, verifiable-agents, stateful-agents, harness-interface, harness-mechanisms, multi-agent-coordination]
clusters: [llm-agents]
related:
  - concepts/code-as-agent-harness.md
  - concepts/llm-agent-systems.md
  - sources/agentic-harness-engineering.md
  - concepts/cemini-ai-assistant.md
  - sources/arxiv-grep-agent-harness-2605-15184.md

maturity: validated
read_status: skimmed
created: 2026-05-21
updated: 2026-05-21
---

## Relations

- @concepts/code-as-agent-harness.md — concept hub synthesized from this survey
- @concepts/llm-agent-systems.md — parent cluster for agent architecture research
- @sources/agentic-harness-engineering.md — complementary: observability-driven harness *evolution* (AHE)
- @concepts/cemini-ai-assistant.md — Cemini user-facing agent should map to harness-interface + verification layers

## Raw Concept

- **Title**: Code as Agent Harness: Toward Executable, Verifiable, and Stateful Agent Systems
- **Authors**: Xuying Ning et al. (UIUC, Meta, Stanford — core contributors listed on title page)
- **Type**: arXiv preprint — arXiv:2605.18747v1 [cs.CL]
- **Submitted**: 2026-05-19
- **Retrieved**: 2026-05-21 (Tier-2 sweep `@sweeps/2026-05-21.md`, Tier-A)
- **Pages**: 102
- **Read status**: skimmed (abstract + §1 framing; full taxonomy deferred)
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/2605.18747_code-as-agent-harness-survey.pdf`

## Narrative

102-page survey framing **code as the operational substrate** for agentic systems — not merely generated output. Three layers: (1) **harness interface** linking reasoning, action, and environment modeling; (2) **harness mechanisms** (planning, memory, tools, feedback control); (3) **scaling the harness** to multi-agent coordination via shared code artifacts.

**Cemini relevance [CONFIRMED against prior harness work]**: Aligns with conductor + MCP tool surface, kb-server reads, stash episodic state, skill_audit/MCPT verification gates, and server-Claude vs laptop curator split. Open problems named in source (evaluation beyond success bit, partial-feedback verification, regression-free harness edits, multi-agent shared state, human oversight) map directly to Cemini AI proposal constraints in `@concepts/cemini-ai-assistant.md`.

## Snippets

> "In emerging agentic systems, code is no longer only a target output. It increasingly serves as an operational substrate for agent reasoning, acting, environment modeling, and execution-based verification."
> — [Source: 2605.18747_code-as-agent-harness-survey.pdf p.1]

> "We frame this shift through the lens of agent harnesses and introduce code as agent harness: a unified view that centers code as the basis for agent infrastructure."
> — [Source: 2605.18747_code-as-agent-harness-survey.pdf p.1]
