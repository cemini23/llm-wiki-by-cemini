## Target

Researcher Round **S2 HU sandbox** — static-agent bundle via `submit_sandbox_pvp.py` (Option A: vendored **gin/poker-bot v3 `hu004`**).

## Summary

Competitor recon + local HU benchmarks showed gin `hu004` ahead of our partial v008 steal on **single-regime** toy selfplay (fixed opponent pool — see Body). **Option A shipped 2026-07-01:** vendored `hu004` → `gin_hu004_bridge.py` → `harness/strategy.py` (default `CEMINI_SANDBOX_ENGINE=gin_hu004`). Active PvP **`8545120c`** on S2 comp **`cmr0jmqlt08bi13n8neory9xb`**. Public S2 LB remains **empty until >20k hands** — poll agent page / `--poll` until then.

## Update (2026-07-02)

**Live engine reverted to cemini (K131b).** Gin submission `8545120c` finalized +7.3 TS @ 5k vs cemini `5f6f3aec` +19 TS — pin now `CEMINI_SANDBOX_ENGINE=cemini`, `replace: true`, active submission `41651659`. Vendored `hu004` remains in-repo for local gate villain; bundle **omits** `_vendor/gin_hu004` when engine=cemini.

## Body

### Why Option A (not more v008 patches)

**Regime disclosure (local selfplay — not Arena TrueSkill):**

| Dimension | Local gate | Arena S2 live |
|-----------|------------|---------------|
| Opponent pool | Fixed toy bots (`profiled_counter_adaptive`, `tight`) | Scheduler-matched field (unknown mix) |
| Hands | 2,000 HU, seed 42 | 5k target/season; LB gate ~20k+ |
| Metric | Raw adj bb/100 | TrueSkill μ−3σ on finalized bot |
| Engine parity | Same PokerKit table adapter | static-agent bundle only |

| Engine | vs profiled_counter_adaptive (2k HU, seed 42) | Notes |
|--------|-----------------------------------------------|-------|
| gin `hu004` | **+39.5 bb/100** | Luigi v4 #1 S1 sandbox links gin v3 |
| gin `auto_research_v008` | **−12.1 bb/100** | Only layer we ported into `gin_style.py` |
| `cemini_decide` | +18–22 vs `tight` (different opponent) | S2 finalized **`5f6f3aec`**: +19 TS @ 5k — **not comparable row to hu004 local row** |

S1 LB leaders show **21k–31k hands**; our first S2 cemini run **`5f6f3aec`** finished **5k/5k** (+19 TS, +47 adj bb/100) — early **109 @ 1.6k** was sample inflation, not finalized score.

### Live posture (poll 2026-07-01)

| Field | Value |
|-------|-------|
| Agent | `cmpy4lcyi001y11vnekn1zlo3` (`cemini_wiki_poker`, claimed) |
| Competition | `cmr0jmqlt08bi13n8neory9xb` — `[poker] heads-up sandbox — beta S2` |
| Active submission | `8545120c-e3cd-4c1a-bb3c-d2d5254f18ca` |
| Bundle SHA | `415e10c829940609888f1fe8ccd0ab821d9193e43fd3ebc2dc260fb7971f2bc9` |
| PvP | Active — track via poll (target 5k hands/season; S2 may resume toward 20k LB) |
| Pin | `config/researcher_sandbox_submit.pin.json` |

### Env / engine switch

```
CEMINI_SANDBOX_ENGINE=gin_hu004   # default in harness/strategy.py
POKER_BOT_STRATEGY=hu004          # reasoning YAML label
CEMINI_SANITIZE_OUTPUT=0          # hand-specific trajectory reasoning
```

Rollback to cemini stack:

```
CEMINI_SANDBOX_ENGINE=cemini
# rebuild bundle; submit --replace
```

### Pre-submit checklist (gin path)

1. `bash scripts/sync_gin_hu004.sh` (upstream gin/poker-bot **v3**, no LICENSE — algorithm port only)
2. `CEMINI_SANDBOX_ENGINE=gin_hu004 bash scripts/verify_sandbox_bundle_layout.sh`
3. `uv run pytest tests/test_gin_hu004_bridge.py -q`
4. `CEMINI_SANDBOX_ENGINE=gin_hu004 CEMINI_TABLE_FORMAT=hu ./scripts/run_hu_sandbox_gate.sh --hands 200` → M8/M9 PASS
5. Prod: `submit_sandbox_pvp.py --build --replace --competition-id cmr0jmqlt08bi13n8neory9xb`
6. Poll until PvP progresses; **do not trust public LB** until operator confirms >20k gate lifted

### Bundle layout (gin)

| Path | Role |
|------|------|
| `harness/strategy.py` | Routes to `gin_hu004_bridge.decide()` when `CEMINI_SANDBOX_ENGINE=gin_hu004` |
| `assets/gin_hu004_bridge.py` | Table normalize + Arena payload + reasoning YAML |
| `assets/_vendor/gin_hu004/hu004.py` | Vendored gin v3 HU brain (~290KB, stdlib-only) |
| `assets/cemini_decide.py` | Retained for rollback / mixed bundles |

**Do not** set `CEMINI_BUNDLE_INCLUDE_SKILLS=1` — Arena rejects `skills/` in zip.

### Ops

```bash
# Poll (prod)
ssh cemini-prod 'cd /opt/devfun-poker-arena && ./venv/bin/python examples/submit_sandbox_pvp.py --poll 8545120c-e3cd-4c1a-bb3c-d2d5254f18ca'

# Re-sync vendor + rsync to prod
bash scripts/sync_gin_hu004.sh
rsync -avz vendor/gin_hu004/ cemini-prod:/opt/devfun-poker-arena/vendor/gin_hu004/
```

Auto-submit timer: `cemini-researcher-sandbox-submit.timer` on prod (respects pin; no replace while PvP active).

### K138 brief follow-ups (not Option A — next steals)

| Brief | P0 action | Status |
|-------|-----------|--------|
| `2026-07-01_k138-ai-pokergame-opponent-steal.md` | YAML + optional selfplay villain | **P0 done** — `config/villain_ai_pokergame_hard.yaml` + `examples/ai_pokergame_villain.py`. **No gate/live merge:** 800h HU seed 42 — hero +67.9 bb/100 vs ai_pokergame_hard vs +39.2 vs `tight` (weaker opponent; inflates metrics) |
| `2026-07-01_k138-deal-games-ppo-solver-steal.md` | `solver_family=` + exploitability on toy JSON | **Skip perf** — already on `research/kuhn3p_ped_spike.json`; literacy/OpenSpiel P1 does not touch NLHE decide() |

### Risks / expectations

- gin upstream **no LICENSE** — vendored copy + sync script only; do not merge Flask/server code
- Option A improves **arena TS vs partial steal**; not guaranteed top-of-board vs full gin stack + field
- S2 scoring differs from S1; compare runs on **same comp** only

## Sources

- @wiki/concepts/devfun-poker-competitor-github-recon-2026-06.md
- https://github.com/gin/poker-bot/tree/v3 (`hu004.py`)
- `briefs/2026-06-26_k131b-researcher-submit-ready.md`
- `briefs/2026-07-01_k138-ai-pokergame-opponent-steal.md`
- `briefs/2026-07-01_k138-deal-games-ppo-solver-steal.md`
- Discord #researcher-track — S2 infinite hands; LB >20k hands gate [TENTATIVE operator 2026-07-01]
