## Target

`agents/devfun-poker-arena/` — prod auto-submit for Researcher HU sandbox.

## Summary

When Arena `sandbox_daily_limit` blocks manual submit, a **systemd oneshot + timer** builds the pinned bundle (`config/researcher_sandbox_submit.pin.json`) and POSTs `--replace` via `submit_sandbox_pvp.py --tolerate-daily-limit`.

## Body

### Pin file (git)

`config/researcher_sandbox_submit.pin.json` — competition id, `agentVersion`, `gitCommit`, `build` + `replace` intent. Updated by `scripts/pin_researcher_sandbox_submit.sh` on each `researcher_jun21_beta_apply.sh` deploy.

### Auto-submit

```bash
bash scripts/run_researcher_sandbox_auto_submit.sh          # prod / manual
bash scripts/run_researcher_sandbox_auto_submit.sh --dry-run
```

State: `reports/researcher-round/auto-submit-state.json` + `auto-submit.log` (prod, gitignored).

### systemd (prod)

| Unit | Role |
|------|------|
| `cemini-researcher-sandbox-submit.service` | oneshot → auto-submit script |
| `cemini-researcher-sandbox-submit.timer` | 00:12 / 06:12 / 12:12 / 18:12 UTC + 45m after boot |

Enable: `researcher_jun21_beta_apply.sh` when `ARENA_RESEARCHER_COMP_ID` is pinned.

### K131 briefs status (2026-06-26)

| Brief | Status |
|-------|--------|
| K131 sandbox improvement (A/B/C) | **Shipped** — HU widen, gin_v2, LAG gate, harvest venv |
| K131b submit-ready | **Shipped** — harness SANITIZE=0, v008, bundle layout |
| ToolBench-X arena-tool steal | **Defer** — hazard dry-run tests |
| Relaxed NFL verifier steal | **Defer** — DecideTrace schema offline |

## Sources

- @wiki/sources/devfun-researcher-sandbox-researcher-guide-2026-06-08.md
- `briefs/2026-06-26_k131-sandbox-improvement-plan.md`
