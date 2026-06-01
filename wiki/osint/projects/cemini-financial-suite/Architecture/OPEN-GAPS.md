---
title: CeminiSuite architecture — open gaps (prod)
type: concept
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
  - projects/cemini-financial-suite/Architecture/Architecture - Index.md
  - projects/cemini-financial-suite/Architecture/Architecture - Overview.md
  - projects/cemini-financial-suite/Architecture/tool-adopt-matrix.generated.md
  - projects/osint-workspace/Architecture/Architecture - Overview.md
  - concepts/cemini-repository-topology.md
  - entities/infrastructure/cemini-stack.md
  - concepts/librarian-server-architecture.md
maturity: validated
---

## Relations

- @projects/cemini-financial-suite/Cemini Financial Suite.md
- @projects/cemini-financial-suite/Architecture/Architecture - Index.md
- @projects/cemini-financial-suite/Architecture/Architecture - Overview.md
- @projects/cemini-financial-suite/Architecture/tool-adopt-matrix.generated.md
- @projects/osint-workspace/Architecture/Architecture - Overview.md
- @concepts/cemini-repository-topology.md
- @entities/infrastructure/cemini-stack.md
- @concepts/librarian-server-architecture.md

## For future Claude

Deferred areas after wave 4 @ e8fd49f; db ERD + tools adopt matrix closed.

# Open gaps (after wave 4 — ERD + adopt matrix)

## Still open

| Area | Why | Next step |
|------|-----|-----------|
| **Runtime snapshot** | `docker compose ps` goes stale | Dated `Architecture - prod-snapshot-YYYY-MM-DD.md` in ops runbook |
| **`@generated` auto-patch** | Refresh script checks SHA only | Extend `architect_refresh_handoff.sh` to patch census + adopt matrix |
| **CI link check** | No markdown CI on handoff | `markdown-link-check` on `briefs/out/` |
| **Deephaven app wiring** | Compose only | Trace when queries run in prod |
| **octotools on prod** | `tools/octotools-phase0/` committed | Operator: remove or gitignore; use `/tmp` per policy |
| **Unset adopt verdicts (—)** | 3 k63 weather repos | License audit → update manifest |
| **conviction.yaml / gates** | User-gated | Ops runbook only |
| **Cemini-Suite/** | Laptop-only | N/A |

## Closed in wave 4

- @projects/cemini-financial-suite/Architecture/Architecture - db ERD.md — 52 tables, logical domain diagram
- @projects/cemini-financial-suite/Architecture/Architecture - tools.md — K71 manifest matrix (43 entries) + `scripts/export_tool_adopt_matrix.py`
- `tool-adopt-matrix.generated.md` — regenerable artifact

## Closed in wave 3

See @projects/cemini-financial-suite/Architecture/OPEN-GAPS.md history in `briefs/2026-06-01_architecture-handoff-gap-close.md`.

## Wiki re-sync

```bash
scp -r cemini-prod:/opt/cemini/briefs/out/architecture-2026-06-01/ \
  "<wiki>/projects/cemini-financial-suite/Architecture/"
```

Target commit after pull: check `RETURN-STUB.txt`.
