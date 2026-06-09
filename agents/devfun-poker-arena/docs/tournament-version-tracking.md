# Tournament version tracking

Main KO uses **S1-shaped scoring** (eval panel / bb/100), not playground chip rank. This doc is the operator loop to **track bot versions**, **log performance**, and **pick what to deploy** at lock-in.

## Three metrics (do not conflate)

| Track | Metric | Where logged | Tournament relevance |
|-------|--------|--------------|----------------------|
| **Playground** | Chip rank, buffer vs #20 | `playground_timeseries.jsonl` | Qualification only (S1a-style seasons) |
| **Eval panel** | `adjustedBbPer100` vs DeepCFR | `eval_timeseries.jsonl` + live benchmark | **Primary** for main KO |
| **Local gate** | Self-play bb/100 (`eval_panel_mode`) | `preflight_metrics.json` | Deploy gate before prod |

## Artifact layout (`reports/hl-loop/`)

| File | Purpose |
|------|---------|
| `deploys.jsonl` | Every prod deploy: commit, HL round, hands, env digest, preflight eval |
| `eval_timeseries.jsonl` | Eval smoke/full runs (`run_eval_smoke.sh`) |
| `playground_timeseries.jsonl` | Live rank/chips/replay delta (lobby, every poll) |
| `multi_comp_config.json` | S1 primary + S2 secondary comp IDs (`drives_deploy` flags) |
| `multi_comp_timeseries.jsonl` | Oracle snapshots per comp (hands, chip_delta, rank) |
| `preflight_metrics.json` | Last full preflight: local eval-panel bb/100 |
| `state.json` | HL round, hands, commit |
| `tournament_candidate.json` | Locked pick for main KO (operator or `--lock`) |
| `tournament_candidates.jsonl` | History of lock decisions |

### Multi-comp oracle (S1 priority)

- **Primary** (`s1_tournament`): drives analyze, export (`s1-tournament-live`), HL loop `--match`, deploy gate.
- **Secondary** (`s2_playground`): intel only in oracle — **never** authorizes deploy.
- Prod: `cemini-devfun-poker-multi-comp-snapshot.timer` (30 min) exports **primary only**.
- Laptop: `./scripts/run_multi_comp_snapshot.sh` or `./scripts/run_s1_tournament_hl_cycle.sh`

Schemas: `devfun.deploy_record.v1`, `devfun.eval_timeseries.v1`, `devfun.tournament_candidate.v1`.

## Daily operator loop

### 1. Patch + deploy (unchanged)

```bash
./examples/cemini_hl_loop.sh --deploy --round N
```

Full preflight now includes **eval-panel gate** (150 hands default, `CEMINI_EVAL_GATE_HANDS`).

### 2. Eval smoke after meaningful patches

```bash
./scripts/run_eval_smoke.sh          # 50h smoke → eval_timeseries.jsonl
./scripts/run_eval_smoke.sh --full   # 500h if smoke ≥ −12
```

### 3. Sync prod artifacts to laptop

```bash
./scripts/sync_hl_artifacts.sh
# state.json stays on laptop (canonical). Prod copy updates on each HL deploy.
# Only pull prod state if you know it is newer: ./scripts/sync_hl_artifacts.sh --pull-state
```

### 4. Rank candidates for tournament

```bash
uv run python scripts/pick_deploy_for_tournament.py
uv run python scripts/pick_deploy_for_tournament.py --min-eval-bb100 -15
```

### 5. Lock tournament deploy (when ready)

```bash
uv run python scripts/pick_deploy_for_tournament.py \
  --lock --label s1b-final --commit abc1234 \
  --rationale "eval −12.5 smoke, stable 400h playground buffer"
```

Writes `tournament_candidate.json` — ship **that commit** to prod before main KO.

## Improvement workflow (eval track)

Per `briefs/2026-06-08_eval-vs-playground-posture.md`:

1. **Baseline** — note `eval_panel_bb100` in `preflight_metrics.json` before patch.
2. **One leak fix** — HL round, preflop −100 cluster priority.
3. **Eval smoke** — did `adjustedBbPer100` move toward −10 (smoke) / −5 (stretch)?
4. **Playground check** — did rank/buffer hold? (`playground_timeseries.jsonl` rows tagged with `commit`).
5. **Only widen** when eval gate passes floor (`CEMINI_EVAL_PANEL_BB100_FLOOR`, default −17.45).

Targets (directional):

| Stage | Eval smoke | Eval full |
|-------|------------|-----------|
| Now | −17 → −12 | −17 → −10 |
| Tournament-ready | ≥ −10 | ≥ −5 (stretch) |

## Env versioning

Each `deploys.jsonl` row stores:

- `commit` — git SHA on deploy
- `env_digest` — hash of `CEMINI_*` / `JACKPOT_*` flags
- `env_flags` — full snapshot (prod `.env` on server deploys)

Compare two deploys: same commit + different `env_digest` = config-only change.

## What we cannot infer from submissions alone

`payout_chips` ≠ chip delta. True bb/100 on playground requires replay `chipDelta` or API benchmark — see `playground_timeseries.py` and `docs/s1b-v2-v3-data-capture.md`.

## Related

- `DEPLOY.md` — HL deploy convention
- `docs/TESTING-CEMINI.md` — regression + self-play gates
- `briefs/2026-06-08_eval-vs-playground-posture.md` — why playground #1 ≠ tournament strength
