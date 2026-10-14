---
title: Inbox arXiv reject batch — 2026-09-24 (5 rejects + 6 ingests)
type: source
tags: [source, triage, reject, arxiv, ingest]
keywords: [arxiv, triage, reject, digest, astro-ph, robotics, mirage, opinion-games]
related:
  - sources/inbox-arxiv-reject-batch-2026-09-19.md
  - sources/arxiv-2609.21562-gamelogicbench-runtime-logic-2026-09-24.md
  - meta/cross-wiki-routing.md
  - concepts/game-dev-wiki-scope.md
read_status: read
source_type: operator-triage
maturity: validated
created: 2026-09-24
updated: 2026-09-24
---

## Raw Concept

Eleven PDFs from `2026-09-21-daily.md` … `2026-09-24-daily.md`. **6 ingest** (game agent eval + narrative/NPC guardrails); **5 reject** (astrophysics mis-route, robotics HRI, general LLM reasoning, social-norm sociology, opinion-game theory). Preingest: 11× NEW.

## Narrative

| arXiv ID | Title (short) | Verdict | Route |
|----------|---------------|---------|-------|
| 2609.21562 | GameLogicBench tick-level game logic | **Ingest** | @sources/arxiv-2609.21562-gamelogicbench-runtime-logic-2026-09-24.md |
| 2609.23043 | Narrative reliability detective games | **Ingest** | @sources/arxiv-2609.23043-narrative-reliability-detective-games-2026-09-24.md |
| 2609.23142 | CraftBench-UE deterministic UE agent eval | **Ingest** | @sources/arxiv-2609.23142-craftbench-ue-deterministic-eval-2026-09-24.md |
| 2609.26629 | PersonaWeaver procedural character diversity | **Ingest** | @sources/arxiv-2609.26629-personaweaver-procedural-characters-2026-09-24.md |
| 2609.27585 | Unity Insight code–asset index | **Ingest** | @sources/arxiv-2609.27585-unity-insight-code-asset-index-2026-09-24.md |
| 2609.27606 | State-Grounded Conditioning (SGC) | **Ingest** | @sources/arxiv-2609.27606-state-grounded-conditioning-2026-09-24.md |
| 2609.21554 | MIRAGE multi-perspective LLM reasoning | **Reject** | cs.CL general reasoning — @ccc-wiki |
| 2609.23148 | Surveying the Universe in 4D (WFSS) | **Reject** | astro-ph — `llm-agent-game-paper` false positive |
| 2609.24055 | Human-in-the-loop robot failure recovery | **Reject** | cs.RO HRI — not game-dev |
| 2609.26481 | Social norm emergence in LLM societies | **Reject** | cs.MA mechanism eval — @ccc-wiki |
| 2609.27639 | Hybrid coevolutionary opinion games | **Reject** | cs.GT/cs.MA — not castle/RTS |

**Phase-0:** GameLogicBench repo **NO-GO clone** (no LICENSE); CraftBench-UE **MIT CONDITIONAL-GO** (UE shelf only). See entity pages.

**Action:** Archive 11 PDFs; clear inbox. Tighten `llm-agent-game-paper` with `ANDNOT astro-ph`.

**Location:** egress under `cemini-egress-fi:/opt/cemini-bulk/research/game-dev/` (per archived filename).
