---
title: ProtocolBench — LLM multi-agent protocol selection — 2026-06-24
type: source
tags: [source, harness, multi-agent, research, defer]
keywords: [protocolbench, multi-agent, llm, protocol, openreview]
related:
  - concepts/agent-harness-castle-project.md
  - concepts/ccgs-workflow-extraction.md
  - sources/inbox-arxiv-reject-batch-2026-07-01.md
  - meta/cross-wiki-routing.md
read_status: read
source_type: research-paper
source_url: https://openreview.net/forum?id=GZRiXE2zBe
maturity: draft
created: 2026-07-01
updated: 2026-07-01
---

## Raw Concept

Digest paper lane (2026-06-24): **ProtocolBench** — benchmark for choosing **LLM multi-agent communication protocols**. OpenReview — not arXiv; PDF not auto-fetched.

## Narrative

### Pattern [TENTATIVE — title + digest placement only]

| Layer | Notes |
|-------|-------|
| Problem | Which multi-agent protocol (message passing, tool handoff, etc.) fits a task |
| Audience | Agent orchestration / harness design — not game mechanics |
| castle-sim | Indirect: Codex swarm handoff patterns @concepts/agent-harness-castle-project.md |

### Routing

| Extract | Route |
|---------|-------|
| Protocol selection methodology for planner→executor swarms | **Primary:** @ccc-wiki (harness primitives) |
| Game-specific content | None |

**Verdict:** **DEFER (@ccc-wiki stub)** — game-dev wiki holds pointer only; no Phase-0; no castle-sim brief.

## Dead Ends

- Implementing ProtocolBench inside Godot runtime
- Replacing CCGS role graph with protocol benchmark scores without operator review
