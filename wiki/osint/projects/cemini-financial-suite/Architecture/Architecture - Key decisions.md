---
title: Architecture - Key decisions (prod)
type: architecture-overview
date: 2026-06-01
updated: 2026-06-01
tags: [architecture, cemini-suite, prod-handoff]
keywords: [Cemini-Financial-Suite, /opt/cemini, deploy-monorepo]
deploy-root: /opt/cemini
scanned-commit: e3674e4
provenance: prod-briefs-out-architecture-2026-06-01
ai-first: true
related:
  - projects/cemini-financial-suite/Cemini Financial Suite.md
  - projects/cemini-financial-suite/Architecture/Architecture - Overview.md
  - concepts/cemini-repository-topology.md
  - concepts/cemini-deployment.md
maturity: validated
---

## Relations

- @projects/cemini-financial-suite/Cemini Financial Suite.md
- @projects/cemini-financial-suite/Architecture/Architecture - Overview.md
- @concepts/cemini-repository-topology.md
- @concepts/cemini-deployment.md

## For future Claude

Commit-mined decision signals from prod `/opt/cemini` @ e3674e4; subjects only in generated table.

# Key decisions — recent git signals

Mined via `mine_commit_decisions.py --repo /opt/cemini` (obsidian-second-brain). **Anti-fabrication:** subjects only; no inferred design rationale beyond commit message text.

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

## Themes (human summary — verify in diffs before citing as policy)

1. **Contract evolution** — `TradeSignalEnvelope` gained explicit `decision` field (`17cf48e`).
2. **Brain exits** — exit-decision agent + paper BUY path (`fe22656`); orchestrator dedupe (`39f6e81`).
3. **Weather ops** — TAF layers + EMOS promote wired to systemd (`f9e11f8`).
4. **Operator UI** — PM/Kalshi sidebar naming clarity (`e3ee892`).

## Deploy topology decisions (from README / compose — not commit-mined)

| Decision | Source |
|----------|--------|
| `signal_generator` (QuantOS) disabled vs `brain` | `docker/compose.intelligence.yml` comment 2026-02-24 |
| Paper mode default for broker adapters | Root `README.md` |
| Compose split into 11 included files | `docker-compose.yml` header |

## @user notes

_Add prod-only operator decisions here after review._
