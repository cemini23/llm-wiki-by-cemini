# Federated daily research digest — install kit

Copy this directory's Python modules into a sibling wiki repo's `scripts/` folder, then run `install_federated_daily_digest.sh` from that repo root.

**Canonical reference:** OSINT `scripts/daily_research_digest_run.py` + `daily_research_fetch.py` (keep in sync manually until shared package exists).

## Quick install (per wiki)

```bash
WIKI_ROOT="/path/to/wiki-repo"
bash "/Users/claudiobarone/Desktop/OSINT WORKSPACE/scripts/federation/daily_digest/install_federated_daily_digest.sh" "$WIKI_ROOT" "<wiki-id>"
```

`<wiki-id>`: `ccc` | `seo` | `image-gen` | `gambling` | `cybersec` | `3d-printing`

Creates:

- `scripts/daily_research_config.yaml` from template (if missing)
- `wiki/meta/daily-research-digest-cadence.md` stub (if missing)
- LaunchAgent `com.cemini.daily-research-digest.<wiki-id>` @ 08:15 (staggered)

## Operator loop

1. Morning: review `wiki/sweeps/YYYY-MM-DD-daily.md`
2. Say **full ingest** in Cursor for that wiki folder
3. Weekly: optional Monokern pipeline (`monokern_pipeline.enabled` in config)
