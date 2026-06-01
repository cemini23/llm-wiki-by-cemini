---
title: CeminiSuite architecture — open gaps (prod)
type: concept
date: 2026-06-01
updated: 2026-06-01
tags: [architecture, cemini-suite, prod-handoff, wave5]
keywords: [Cemini-Financial-Suite, /opt/cemini, 8faf94e]
deploy-root: /opt/cemini
scanned-commit: 8faf94e
provenance: prod-briefs-out-architecture-2026-06-01-wave5
ai-first: true
related:
  - projects/cemini-financial-suite/Cemini Financial Suite.md
  - projects/cemini-financial-suite/Architecture/Architecture - Index.md
  - projects/cemini-financial-suite/Architecture/Architecture - Overview.md
  - projects/cemini-financial-suite/Architecture/Architecture - prod-snapshot-2026-06-01.md
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
- @projects/cemini-financial-suite/Architecture/Architecture - prod-snapshot-2026-06-01.md
- @projects/cemini-financial-suite/Architecture/tool-adopt-matrix.generated.md
- @projects/osint-workspace/Architecture/Architecture - Overview.md
- @concepts/cemini-repository-topology.md
- @entities/infrastructure/cemini-stack.md
- @concepts/librarian-server-architecture.md

## For future Claude

Remaining gaps after wave 5 @ 8faf94e.

# Open gaps (after wave 5)

## Still open

| Area | Why | Next step |
|------|-----|-----------|
| **EMS container down** | `ems` not in `docker compose ps` @ 2026-06-01 | Operator: `docker compose up -d ems` when execution path needed |
| **octotools tracked files** | `.gitignore` has `tools/octotools-phase0/` but tree still tracked | `git rm -r --cached tools/octotools-phase0` when operator GO |
| **conviction.yaml / gates** | User-gated | Ops runbook only |
| **Cemini-Suite/** | Laptop-only | N/A |

## Closed in wave 5

- @projects/cemini-financial-suite/Architecture/Architecture - prod-snapshot-2026-06-01.md — live `docker compose ps` + systemd timers
- `scripts/generate_prod_snapshot.py` — regenerate dated snapshots
- `scripts/architect_patch_handoff.py` + extended `architect_refresh_handoff.sh` (@generated census + adopt matrix)
- `.github/workflows/docs-handoff-check.yml` + `scripts/check_handoff_links.py`
- Deephaven wiring in @projects/cemini-financial-suite/Architecture/Architecture - data plane.md
- k63 weather tools: `—` → **DEFER** in `tool_adopt_registry.py`

## Wiki re-sync

```bash
scp -r cemini-prod:/opt/cemini/briefs/out/architecture-2026-06-01/ \
  "<wiki>/projects/cemini-financial-suite/Architecture/"
```

See `RETURN-STUB.txt` for prod commit.
