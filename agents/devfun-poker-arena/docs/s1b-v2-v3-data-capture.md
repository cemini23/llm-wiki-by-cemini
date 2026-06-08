# S1b V2/V3 data capture plan

Research posture for the **Jun 7–11 playground (S1b)** — not live HL ops. Goal: collect everything needed to calibrate the bot when scoring may switch to all-in EV / AIVAT.

---

## Day 0 — rollover (gap window)

```bash
# On prod after new competitionId drops
PLAYGROUND_ROLLOVER_RESTART=1 ./scripts/playground_rollover_preflight.sh <NEW_COMP_ID> playground-s1b-live

# Research harvest (not hourly top-200)
CEMINI_SKIP_ENV=1 CEMINI_SKIP_CREDS=1 ./deploy/deploy_to_cemini_prod.sh
ssh cemini-prod 'cd /opt/devfun-poker-arena && nohup ./venv/bin/python scripts/research_harvest.py run-all \
  --out-dir reports/exports/playground-s1b-live --batch-size 500 --sleep 0.03 \
  >> /tmp/s1b-harvest.log 2>&1 &'

# Laptop archive (run during gap + nightly during S1b)
./scripts/sync_export_archive.sh playground-s1b-live
```

Update export service paths to `playground-s1b-live` before enabling timers.

---

## What to capture (by scoring mode)

| Signal | S1a (chips) | S1b if still chips | S1b if V2/V3 live |
|--------|-------------|--------------------|-------------------|
| `detect_scoring_mode.py` | ✅ day 0 | ✅ every 6h | ✅ every 6h |
| Full-field crawl (`submissions-all`) | ✅ gap archive | ✅ week 1 complete | ✅ week 1 complete |
| Full-field stats (`agents-all`) | ✅ | ✅ | ✅ |
| Top-500 snapshot | ✅ gap | optional | optional |
| Hero replays (50 cap) | HL worst-15 queue | daily HL queue | **priority** — chipDelta for EV |
| `competition_metrics_report` | chip proxy only | chip proxy | **track adjustedBbPer100** |
| Participant status polling | rank/chips/hands | same | + eval fields if present |
| **UI bb/100 snapshot** | ✅ S1a screenshots | screen record if column returns | merge via `import_bb100_snapshot.py` |

### Ephemeral UI column (S1a lesson)

dev.fun **briefly** showed **Adjusted BB/100** on the leaderboard — **not sortable**, removed same session, **no API field**. Canonical log:

- `tests/fixtures/bb100_ui_snapshot_s1a_2026-06-08.json`
- `briefs/2026-06-08_s1a-adjusted-bb100-ui-snapshot.md`

When you see the column again:

1. **Screen record** while scrolling (sort may stay broken)
2. Transcribe visible rows into JSON (`schema: devfun.bb100_ui_snapshot.v1`)
3. `uv run python examples/import_bb100_snapshot.py --snapshot path.json --export-dir reports/exports/<comp>/ --install --metrics`
4. `detect_scoring_mode.py --export-dir …` will report `ui_snapshot_only` until API catches up


## Timers (research, not live ops)

| Timer | Cadence | Command |
|-------|---------|---------|
| Export crawl | **Daily 03:15 UTC** | `export_field_crawl.py --batch-size 500 --until-complete --no-tables` |
| Scoring detect | **Every 6h** | `detect_scoring_mode.py --json-out …/scoring_mode.json` |
| Metrics snapshot | **Daily after crawl** | `competition_metrics_report.py` |
| Replay queue | **After HL analyze** | `export_hl_replay_queue.py` |

Disable or widen hourly top-200 export during S1b unless you need live steal queue — research harvest replaces it.

---

## S1b experiment protocol (from gap audit backlog)

1. Import gap audit **Ranked patch backlog** — max **one** HL round per 250 hands  
2. Track side-by-side: chip rank vs eval metric (if V2 visible)  
3. L5 probe handles optional — never widen main agent for vanity  
4. End of S1b: `prepare_gap_audit_pack.py` + `run_gap_premium_audit.py` → KO brief  

---

## V2/V3-specific artifacts to add when eval scoring appears

- [ ] Log `adjustedBbPer100` / `allInEvBbPer100` / `aivatBbPer100` from status API to `eval_timeseries.jsonl`  
- [ ] Compare hero eval bb/100 vs chip-proxy bb/100 weekly  
- [ ] Replay queue **all** worst EV hands (not just chip losers)  
- [ ] Self-play gate weighted to eval metric if benchmark comp exposes it  

---

## Archive layout

```
reports/exports/playground-s1b-live/
  submissions-all.jsonl      # full field hands
  agents-all.jsonl           # full field stats
  crawl_state.json
  metrics_report.json
  scoring_mode.json
  bb100_ui_snapshot.json       # manual UI capture when API lacks field
  agents_bb100_enriched.jsonl  # export agents merged with snapshot
  bb100_snapshot_meta.json
reports/gap-audit/pack/      # audit inputs (generated)
reports/gap-audit/premium/   # 3-model outputs
```

Laptop mirror: `reports/exports/playground-s1b-live-archive/` (gitignored).

---

## Related

- `scripts/research_harvest.py` — four harvest strategies  
- `scripts/prepare_gap_audit_pack.py` — audit pack builder  
- `scripts/run_gap_premium_audit.py` — 3-model audit  
- `prompts/s1a_gap_retrospective_audit.md` — prompt template  
- `scripts/playground_rollover_preflight.sh` — new comp setup  
