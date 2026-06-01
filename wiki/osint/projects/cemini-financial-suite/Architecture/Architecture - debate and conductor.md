---
title: Architecture - debate and conductor (prod)
type: architecture-module
date: 2026-06-01
updated: 2026-06-01
tags: [architecture, cemini-suite, prod-handoff, wave4]
keywords: [Cemini-Financial-Suite, /opt/cemini, e8fd49f]
deploy-root: /opt/cemini
scanned-commit: e8fd49f
provenance: prod-briefs-out-architecture-2026-06-01-wave4
ai-first: true
module: debate and conductor
path: debate_protocol/
related:
  - projects/cemini-financial-suite/Cemini Financial Suite.md
  - projects/cemini-financial-suite/Architecture/Architecture - Overview.md
  - projects/cemini-financial-suite/Architecture/Architecture - Index.md
maturity: validated
---

## Relations

- @projects/cemini-financial-suite/Cemini Financial Suite.md
- @projects/cemini-financial-suite/Architecture/Architecture - Overview.md
- @projects/cemini-financial-suite/Architecture/Architecture - Index.md

## For future Claude

Prod `debate and conductor` @ e8fd49f.

# debate_protocol & conductor — Multi-agent governance

## debate_protocol/ (in-repo)

| Module | Role |
|--------|------|
| `state_machine.py`, `evaluator.py` | Debate flow |
| `byzantine_gate.py`, `coalition.py` | Consensus gates |
| `blackboard.py`, `debate_logger.py` | Shared state + audit |
| `reasoning.py`, `models.py` | Rubric / types |

Imports allowed: `cemini_contracts`, `shared`, `services` (`check_imports.py`). Pairs with `services/debate_memory.py` and `cemini_contracts/debate_rubric.py`.

MCP read surface: `get_debate_summary` in @projects/cemini-financial-suite/Architecture/Architecture - cemini_mcp.md.

## conductor/ (in-repo — Phase 0 substrate)

`conductor/reviewer/` — offline tool-call reviewer (DeepSeek-R1 rubric). **Phase 0:** no live insertion; replay harness only (`conductor/reviewer/README.md`).

## Librarian conductor (external)

Live **Conductor** macro overlay: `agents/orchestrator.py` optional `ConductorClient` from `services/llm_analyst/conductor_client.py`. Hosted on **librarian**, not deployed from `/opt/cemini`.

Wiki (post-ingest): `concepts/librarian-server-architecture.md` in OSINT federation.

## Related

- @projects/cemini-financial-suite/Architecture/Architecture - agents.md
- @projects/cemini-financial-suite/Architecture/Architecture - services.md

## @user notes
