---
title: Librarian decommission (2026-06-14)
type: concept
tags: [meta, infrastructure, decommission, cost-cut, fleet-posture]
keywords: [cemini-librarian, kb-server, stash, decommission, prod-only, egress-fi]
related:
  - concepts/librarian-server-architecture.md
  - entities/infrastructure/cemini-stack.md
  - entities/infrastructure/cemini-egress-fi.md
  - concepts/laptop-prod-research-split.md
  - concepts/cemini-deployment.md
  - entities/tools/arcticdb.md
  - entities/tools/lazy-tool.md
  - meta/equity-signal-backtest-cadence.md
  - meta/internal-benchmark-deployment-map.md
  - sources/arxiv-wikikv-hierarchical-kv-2606.14275-2026-06-17.md
  - entities/tools/wikikv.md
  - concepts/wiki-tooling-evaluation.md
maturity: core
created: 2026-06-14
updated: 2026-06-17
---

## Relations

- @concepts/librarian-server-architecture.md — prior 24/7 serving design; **superseded for live ops**
- @entities/infrastructure/cemini-stack.md — current fleet topology
- @entities/infrastructure/cemini-egress-fi.md — HL + PM order egress (still required)
- @concepts/laptop-prod-research-split.md — where research steps run post-decommission
- @concepts/cemini-deployment.md — prod install path unchanged
- @entities/tools/arcticdb.md — Arctic canon moved to laptop refresh path
- @entities/tools/lazy-tool.md — kb_search/conductor via librarian **unavailable** until restored
- @meta/equity-signal-backtest-cadence.md — backtest no longer requires `ssh cemini-librarian`

## Raw Concept

`[DECISION 2026-06-14]` Operator deleted the Hetzner host `cemini-librarian`. Trading stack no longer needs 24/7 wiki RAG or brain→kb-server queries (Lane A / prod-first posture). Fleet reduced to **cemini-prod** + **cemini-egress-fi**.

## Narrative

### Current fleet (authoritative)

| Host | Role | Status |
|------|------|--------|
| **cemini-prod** | CeminiSuite trading, Lane A, streams, Redis `intel:*` | **ON** |
| **cemini-egress-fi** | Finnish egress for HL + PM `POST /order` | **ON** |
| **cemini-librarian** | kb-server, stash, Ollama, Arctic LMDB, wiki sync target | **DELETED** |
| **Laptop** | Canonical git wiki, raw ingest, briefs, local backtests | On-demand |

### What changed

| Before | After |
|--------|-------|
| Raw PDFs → `cemini-librarian:/opt/cemini-bulk/research/` | **`cemini-egress-fi:/opt/cemini-bulk/research/<wiki-id>/`** via `scripts/archive_raw_to_egress.sh` (federation-wide; laptop copy removed on success) |
| Wiki sync hourly → kb-server | **No sync.** Laptop `wiki/` + sibling wiki repos are canonical |
| `lazy-tool` → kb_search / conductor_query | **Fails** — use Read/grep on local wikis; Exa for gaps |
| Global **stash** MCP (`localhost:8088` tunnel) | **Offline** — disable tunnel LaunchAgent or expect red MCP |
| Equity backtest via librarian Arctic | `scripts/refresh_arctic_equity_bars.py` + `.local/arctic-market-dataset/` on laptop |
| Ingest step 9 scp to librarian | **`archive_raw_to_egress.sh`** — scp to egress-fi per wiki id |

### Raw-source cold store (2026-06-15)

Federation wikis archive ingested files to **`cemini-egress-fi:/opt/cemini-bulk/research/<wiki-id>/`** (`osint`, `ccc`, `seo`, `image-gen`, `gambling`, `game-dev`, `cybersec`, `3d-printing`). Run from any wiki root:

```bash
bash /path/to/OSINT\ WORKSPACE/scripts/archive_raw_to_egress.sh --wiki-id <id> "<local-file>"
```

Bulk is **read-only cold storage** on the egress box (~65 GB free as of 2026-06-15). It does not participate in order routing (`sshd` tunnel only). Historical librarian bulk on the deleted host is not recoverable unless restored from snapshot.

### Historical provenance on source pages

Hundreds of `wiki/sources/*.md` pages cite `cemini-librarian:/opt/cemini-bulk/research/<file>` as **ingest-time location**. Those strings are **immutable provenance** — do not bulk-edit. They record where the file lived when indexed; bulk data on the deleted host is **not recoverable** unless restored from a Hetzner snapshot the operator retained.

### Scripts deprecated (do not run)

- `scripts/sync_wiki_to_librarian.sh`
- `scripts/librarian_healthcheck.sh`
- `scripts/post-commit.sh` — no-op (was git hook → librarian sync)

### Laptop cleanup (done 2026-06-14)

- Crontab: only `cemini_prod_healthcheck.sh` @ 05:00 remains
- LaunchAgents disabled: `com.cemini.stash-tunnel`, `com.cemini.wiki-sync-verify` (`.plist.disabled`)
- `scripts/verify_wiki_sync.sh`, `scripts/launchagent_wrappers/cemini-wiki-sync-verify.sh`
- `scripts/install_hermes_librarian_gateway.sh`, `scripts/sync_hermes_profile_to_librarian.sh`
- `scripts/install_flox_phase2_librarian.sh`, `scripts/sync_pmxt_football_to_librarian.sh`

### Prod briefs (context)

- `2026-06-14_librarian-graceful-shutdown-cemini-prod.md` — shutdown checklist (executed)
- `2026-06-14_xsp-lane-a-overnight-swing-monitor-cemini-prod.md` — prod-only; no librarian dependency

### Restore path (if ever needed)

1. Provision new Hetzner box; restore from snapshot if available
2. Reinstall kb-server + stash + Ollama; rsync wikis from laptop
3. Re-enable sync cron; update `.local/server.md`; mute rollback in Prometheus

## Snippets

> "Lane A does not query the wiki 24/7 — librarian uptime is not a trading dependency." [Source: operator decision 2026-06-14]
