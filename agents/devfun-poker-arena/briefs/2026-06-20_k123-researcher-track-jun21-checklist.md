## Target

`agents/devfun-poker-arena/` — Researcher HU sandbox closed beta (Jun 21).

## Summary

Operator checklist from gambling-wiki K123 — automated gates via `run_researcher_jun21_checklist.sh`; prod flip via `researcher_jun21_beta_apply.sh` when `ARENA_RESEARCHER_COMP_ID` is pinned.

## Body

### P0 — before first sandbox hand

| Item | Status | Automation |
|------|--------|------------|
| Accept invite / cohort access | Operator | dev.fun dashboard |
| Starter kit smoke | Operator | `devfun-org/poker-arena-starter-kit` → `./pokerkit test` |
| K118 PFR gate | **DONE** | 500h HU gate PFR ~21%; `cemini_selfplay_audit.py --gate` |
| HU `decide()` fork | **DONE** | `_HU_OPEN_CHART`, 29+ HU regressions |
| OSINT preflight | **DONE** | `run_hu_sandbox_gate.sh`, `run_researcher_jun21_checklist.sh` |
| Competition secrecy | Operator | no public wiki ranks/patches during live event |

### P1 — beta day (Jun 21)

| Item | Status | Automation |
|------|--------|------------|
| Read `skillFile` + axis rubric | On comp drop | `run_researcher_comp_recon.sh --competition-id <id>` |
| Pin `competitionId` | **WAITING API** | `pick_researcher_competition.py` / daily `list_arena_competitions.sh` |
| Legal actions + clock safety | **DONE** | `cemini_decide.py` deadline fallbacks |
| SDK / Kaggle URL | Operator | email/Discord |
| Trajectory + axis before submit | **DONE** | `export_researcher_trajectory.sh` + `researcher_trajectory_summary.py --gate` |

### P2 — before Jun 25 public

- Kaggle rules + submit path — hold until materials drop
- HU selfplay aggressive mix — `run_hu_sandbox_gate.sh` maniac/lag audit
- Dual objective (TrueSkill + style rep) — hold `CEMINI_RESEARCHER_STYLE_TARGET` until rules confirm

### Metric discipline

| Optimize | Do not use as primary |
|----------|----------------------|
| TrueSkill / match W/L | Playground chips |
| Live ANALYZE worst hands | Selfplay bb/100 alone |
| HU freq + sizing gates | 6-max VPIP/PFR table |

### Prod env (Jun 21 beta apply)

`researcher_jun21_beta_apply.sh` sets: `CEMINI_PRIMARY_TRACK=researcher`, `CEMINI_TABLE_FORMAT=hu`, `CEMINI_MAFP_CHART=1`, gin + S1B + session memory + mix postflop. Flips `CEMINI_RESEARCHER_MODE=1` when `ARENA_RESEARCHER_COMP_ID` is set.

## Sources

- Gambling wiki: `wiki/sources/brief-k123-researcher-jun21-checklist-2026-06-20.md` (public stub)
- OSINT: `wiki/concepts/devfun-researcher-track-readiness-2026-06.md`
- `briefs/2026-06-19_k122-validation-execution-plan.md`
