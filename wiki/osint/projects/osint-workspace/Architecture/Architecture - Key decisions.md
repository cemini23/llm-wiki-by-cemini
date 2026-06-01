---
title: Architecture — OSINT Workspace key decisions
type: architecture-overview
date: 2026-06-01
updated: 2026-06-01
project: "[[projects/osint-workspace/OSINT Workspace]]"
scanned-commit: b960aae
tags: [architecture, adr, decisions]
ai-first: true
related:
  - projects/osint-workspace/OSINT Workspace.md
  - projects/osint-workspace/Architecture/Architecture - Overview.md
  - concepts/cemini-repository-topology.md
maturity: validated
---

## Relations

- @concepts/cemini-repository-topology.md — full federation framework (validated concept page)
- @projects/osint-workspace/OSINT Workspace.md

## For future Claude

ADR-style list for **this repo's evolution**, seeded from `mine_commit_decisions.py` (6 candidates) plus the validated topology concept. Inferred rationale marked `confidence: speculation` unless tied to a wiki concept or commit subject.

<!-- @generated:start -->

## Decisions

### D1 — Keep research wiki separate from deploy monorepo

| | |
| --- | --- |
| **Decision** | `llm-wiki-by-cemini` (this repo) stays separate from `cemini23/Cemini-Financial-Suite` |
| **Context** | IP, cadence, and editor role differ: laptop curates; prod executes |
| **Evidence** | @concepts/cemini-repository-topology.md (2026-05-28, commit `48d776b` subject: "Add Cemini repository topology decision framework") |
| **Confidence** | high |

### D2 — Retire gbrain as redundant retrieval

| | |
| --- | --- |
| **Decision** | Retire gbrain — adopted but unused |
| **Context** | Duplicate retrieval layer vs kb-server / existing stack |
| **Evidence** | git `d76c560` (2026-05-18): "Retire gbrain — adopted but unused, redundant retrieval layer" |
| **Confidence** | stated (commit subject) |

### D3 — Script-first workflow automations (K84)

| | |
| --- | --- |
| **Decision** | Adopt K84 script-first workflow automations on laptop |
| **Context** | Reduce manual cadence friction (digest, lint gates, inbox) |
| **Evidence** | git `3f3865c` (2026-05-30) |
| **Confidence** | stated |

### D4 — K92 Phase-0 GO adoptions on laptop

| | |
| --- | --- |
| **Decision** | Adopt selected Phase-0 tools (obsidian-second-brain, trading skills, rlcard venv, etc.) |
| **Context** | Tool eval v7; license-verified clones only |
| **Evidence** | git `770cb0d` (2026-06-01); wiki log entry `adopt | K92 Phase-0 laptop adoptions` |
| **Confidence** | stated |

### D5 — obsidian-second-brain on wiki vault (Cemini init, not stock)

| | |
| --- | --- |
| **Decision** | Activate obsidian-second-brain with **custom** `wiki/_CLAUDE.md`; skip stock `/obsidian-init` |
| **Context** | Preserve `index.md` + `log.md`; disable bg agent |
| **Evidence** | `wiki/log.md` 2026-06-01 `activate | obsidian-second-brain`; `wiki/_CLAUDE.md` |
| **Confidence** | high |

### D6 — Phase-0 audits before external tool adoption

| | |
| --- | --- |
| **Decision** | Run Phase-0 source audits for Adopt-tier tools (license, layout lock-in, domain fit) |
| **Context** | Pattern rejected SwarmVault, PageIndex, Claude-OSINT misfits |
| **Evidence** | git `0409a45` (2026-05-16); root `CLAUDE.md` Phase-0 section |
| **Confidence** | high |

## Not decisions (boundaries)

- Splitting QuantOS/Kalshi into separate GitHub repos — **deferred** per topology framework unless release/ownership gates met (confidence: high, @concepts/cemini-repository-topology.md).

<!-- @generated:end -->

## Refresh

Re-run `mine_commit_decisions.py --repo <path> --json` and merge new ADRs; keep human rationale in `<!-- @user:start -->` blocks outside generated sentinels.
