# Federated daily research digest — install kit

Copy this directory's Python modules into a sibling wiki repo's `scripts/` folder, then run `install_federated_daily_digest.sh` from that repo root.

**Keep in sync:** `bash scripts/federation/daily_digest/sync_federation_digest_bundle.sh` (OSINT canonical → all federation wikis + `~/.cemini/launchagent/osint/`).

**Canonical reference:** OSINT `scripts/daily_research_digest_run.py` + `daily_research_fetch.py` (keep in sync manually until shared package exists).

## Quick install (per wiki)

```bash
WIKI_ROOT="/path/to/wiki-repo"
bash "/Users/claudiobarone/Desktop/OSINT WORKSPACE/scripts/federation/daily_digest/install_federated_daily_digest.sh" "$WIKI_ROOT" "<wiki-id>"
```

`<wiki-id>`: `ccc` | `seo` | `image-gen` | `gambling` | `game-dev` | `cybersec` | `3d-printing`

Creates:

- `scripts/daily_research_config.yaml` from template (if missing)
- `wiki/meta/daily-research-digest-cadence.md` stub (if missing)
- LaunchAgent `com.cemini.daily-research-digest.<wiki-id>` @ 08:10+ (staggered +3min via `reinstall_morning_launchagents.sh`; federation summary after last sibling)

## Operator loop

1. Morning: review `wiki/sweeps/YYYY-MM-DD-daily.md`
2. Say **full ingest** in Cursor for that wiki folder
3. Weekly: optional Monokern pipeline (`monokern_pipeline.enabled` in config)

## Raw source archive (all federation wikis)

After ingest, archive immutables to egress-fi (replaces laptop `raw-sources/` / `.local/archives/research/`):

```bash
bash "/Users/claudiobarone/Desktop/OSINT WORKSPACE/scripts/archive_raw_to_egress.sh" --wiki-id <wiki-id> "research to be indexed/<file>"
```

Remote: `cemini-egress-fi:/opt/cemini-bulk/research/<wiki-id>/`. See `@osint-wiki/meta/librarian-decommission-2026-06-14.md`.
