# Playground S1 — season end snapshot (2026-06-08)

## Target

Archive + operator record before S1 rollover.

## Summary

Final capture **2026-06-08T11:51:40Z** while competition still **Active** (`cmpy2qy65002ud9ej6b7jjq0l`).

| Metric | Value |
|--------|-------|
| Chip rank | **#1** |
| Chips / hands | **139,946 / 2,361** |
| VPIP / PFR | **10.4% / 3.5%** (tight-passive) |
| Protect | first + lead + qual ON, lock tier **dominant** |
| UI adjusted bb/100 | **+2,820** (#3 EV at ≥400h — Jeff +3,670, Jagoan +2,828) |
| Eval S1 overnight | **−17.45** adjusted bb/100 (500h vs panel) |

## Body

Canonical JSON: `tests/fixtures/s1a_season_end_snapshot_2026-06-08.json`

Prod copies:
- `/opt/devfun-poker-arena/reports/exports/playground-s1-live/s1a_season_end_snapshot.json`
- `s1a_season_end_analyze.txt` (last 100-hand analyze)
- `metrics_report.json`

Laptop archive: `reports/exports/playground-s1-live-archive/` (rsync ongoing for full export).

**Top-3 chips at close:** hero 139,946 · Jeff 124,748 · grok_trips 104,475 (jagoan #4 at 94,335).

## Sources

- Prod export `agents.jsonl` + `qualification_guard`
- UI bb/100 screenshots (2026-06-08 AM)
- Eval match `cmq4p7m0l9evq92s9q1kcqodr`
