---
title: CeminiSuite architecture — open gaps (prod)
type: concept
date: 2026-06-01
updated: 2026-06-01
tags: [architecture, cemini-suite, prod-handoff, gap-close]
keywords: [Cemini-Financial-Suite, /opt/cemini, de5ad93]
deploy-root: /opt/cemini
scanned-commit: de5ad93
provenance: prod-briefs-out-architecture-2026-06-01-gap-close
ai-first: true
related:
  - projects/cemini-financial-suite/Cemini Financial Suite.md
  - projects/cemini-financial-suite/Architecture/Architecture - Overview.md
  - projects/cemini-financial-suite/Architecture/Architecture - Index.md
  - projects/osint-workspace/Architecture/Architecture - Overview.md
  - concepts/cemini-repository-topology.md
  - entities/infrastructure/cemini-stack.md
  - concepts/librarian-server-architecture.md
maturity: validated
---

## Relations

- @projects/cemini-financial-suite/Cemini Financial Suite.md — project hub
- @projects/cemini-financial-suite/Architecture/Architecture - Overview.md
- @projects/cemini-financial-suite/Architecture/Architecture - Index.md — MOC
- @projects/cemini-financial-suite/Architecture/OPEN-GAPS.md — deferred doc areas
- @projects/osint-workspace/Architecture/Architecture - Overview.md — parallel OSINT laptop pass
- @concepts/cemini-repository-topology.md
- @entities/infrastructure/cemini-stack.md
- @concepts/librarian-server-architecture.md
- @projects/cemini-financial-suite/Architecture/Architecture - Overview.md

## For future Claude

Explicit deferred architecture areas after prod gap-close P0–P2 @ de5ad93. Prevents re-discovering the same holes; closed items listed at bottom.

# Open gaps (after P0–P2 close-out)

Items **intentionally not** documented in depth in this handoff pack. Use this file so laptop ingest and future agents do not re-discover the same holes.

| Area | Path / topic | What's missing | Suggested next step |
|------|----------------|----------------|---------------------|
| Tools | `tools/` (~129 py) | Phase-0 clone inventory, adoption status | Brief + link `tools/README-phase0-clones.md` |
| Database | `db/` (~85 py) | Schema ERD, dbmate migration flow, table ownership | Dedicated `Architecture - db.md` from `db/README.md` + migrations |
| UI | `ui/`, `design/` | Streamlit vs static HTML desk map | Merge `design/README.md` into `Architecture - ui.md` |
| Strategies | `strategies/` | vs `trading_playbook/` boundary | Doc `strategy_logic_versions` + playbook catalog |
| Debate | `debate_protocol/` | Rubric + memory service flow | Cross-link librarian conductor + `services/debate_memory.py` |
| Logit pricing | `logit_pricing/` | Rover fair-value pipeline | Tie to `rover_scanner` + `intel:logit_assessments` |
| Conductor | `conductor/` (in-repo) | vs librarian conductor host | `concepts/librarian-server-architecture.md` on wiki |
| Shared | `shared/` | Feature helpers used by RL/intelligence | Scan imports from `check_imports.py` consumers |
| Runtime matrix | prod | Which compose profiles are **actually** up | Operator runbook snapshot (not architecture prose) |
| Data science plane | ArcticDB, Deephaven volumes | Read paths from EMS/UI | Trace `arcticdb_data`, `deephaven` compose only |
| Automation | `@generated` blocks | Scan JSON vs markdown tables | Extend `scripts/architect_refresh_handoff.sh` to patch census tables |
| CI | docs-only PRs | Broken wikilinks in handoff | Optional `markdown-link-check` on `briefs/out/` |
| Wiki federation | OSINT ingest | Obsidian links point to GitHub, not ingested wiki paths | Re-link after `wiki/projects/cemini-financial-suite/Architecture/` commit |
| MCP tier-2 | `notify_operator` | Destructive tier — operator alerts | Document alert channels in ops runbook |
| Cemini-Suite | laptop-only dir | N/A on prod | No action on prod tree |

## Closed in this pass (do not re-open without new evidence)

- Stale `scanned-commit` / MCP tool count
- Missing pages: contracts, services, playbook, Docker catalog, Polymarket, systemd, Index
- Overview signal bus (`trade_signals`, `intel:playbook_snapshot`)
- Import layer summary in Overview

See [briefs/2026-06-01_architecture-handoff-gap-close.md](../../2026-06-01_architecture-handoff-gap-close.md) for full checklist.
