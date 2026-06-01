---
title: Architecture — Key decisions (prod)
type: architecture-overview
date: 2026-06-01
updated: 2026-06-01
tags: [architecture, cemini-suite, prod-handoff, wave4]
keywords: [Cemini-Financial-Suite, /opt/cemini, e8fd49f]
deploy-root: /opt/cemini
scanned-commit: e8fd49f
provenance: prod-briefs-out-architecture-2026-06-01-wave4
ai-first: true
related:
  - projects/cemini-financial-suite/Cemini Financial Suite.md
  - projects/cemini-financial-suite/Architecture/Architecture - Overview.md
  - projects/cemini-financial-suite/Architecture/Architecture - Index.md
  - concepts/cemini-repository-topology.md
  - concepts/cemini-deployment.md
maturity: validated
---

## Relations

- @projects/cemini-financial-suite/Cemini Financial Suite.md
- @projects/cemini-financial-suite/Architecture/Architecture - Overview.md
- @projects/cemini-financial-suite/Architecture/Architecture - Index.md
- @concepts/cemini-repository-topology.md
- @concepts/cemini-deployment.md

## For future Claude

Decisions @ e8fd49f.

# Key decisions — git signals & governing briefs

## Mined commits (`mine_commit_decisions.py`)

<!-- @generated:start -->
| Date | SHA | Subject | Signal |
|------|-----|---------|--------|
| 2026-05-29 | `3d72a0a` | Remove stale pytest count from dashboard hero subtitle. | remove |
| 2026-05-25 | `e3ee892` | docs(ui): rename PM↔KL sidebar labels to clarify scanner vs ops | rename |
| 2026-05-24 | `f9e11f8` | Add TAF intraday layer (T1-T3) and EMOS promote switch to systemd. | switch to |
| 2026-05-22 | `17cf48e` | feat(contracts): accept 'decision' field on TradeSignalEnvelope | decision |
| 2026-05-22 | `39f6e81` | refactor(orchestrator): dedupe paper_adapter writes — drop redundant call site | drop |
| 2026-05-21 | `fe22656` | feat(brain): exit-decision agent + paper-adapter BUY migration (#56) | decision |
<!-- @generated:end -->

## Topology decisions (compose / README)

| Decision | Evidence |
|----------|----------|
| QuantOS `signal_generator` disabled vs `brain` | `docker/compose.intelligence.yml` 2026-02-24 comment |
| Paper default for brokers | Root `README.md` |
| Compose split into 11 includes | `docker-compose.yml` header |
| Import boundaries enforced in CI | `scripts/check_imports.py`, `deploy.yml` `import-boundary-check` |
| Architecture handoff under `briefs/out/` | `e8fd49f`, gap-close `2026-06-01_architecture-handoff-gap-close.md` |

## Governing briefs (architectural — not mined)

| Brief | Topic |
|-------|-------|
| `briefs/2026-06-01_cemini-suite-obsidian-architect.md` | Initial prod architect pass |
| `briefs/2026-06-01_architecture-handoff-gap-close.md` | Gap analysis + P0–P2 close-out |
| `briefs/2026-05-30_autots-analyst-node-adoption-cemini.md` | AutoTS MCP sidecar + Redis overlay |
| `briefs/2026-05-26_k69-pm-shared-wallet-strategy-capital-ledger-cemini.md` | PM capital ledger |

## @user notes
