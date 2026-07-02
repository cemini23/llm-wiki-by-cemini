---
title: K131b finish + sandbox ops P0 — post GLM/Kimi audit
type: brief
created: 2026-07-02
target: CeminiSuite / cemini-prod
agentVersion: researcher-s2.cemini-k131b-finish.2026-07-02
activeSubmissionId: 3b48d01d-3f33-4467-a108-8111d03c2163
---

## Target

cemini-prod — Researcher S2 sandbox. **Do not replace** live PvP until season completes; next bundle ships K131b finish on fresh submit only.

## Summary

Implemented all GLM 5.2 + Kimi 2.7 audit fixes: **ops P0** (pin self-heal, `replace:false`, closed-set PvP finish, retry guard, timer rev+verify) and **bot P0** (K131b A3 BTN trim, B2 LAG thin value, S2 nemesis handles) plus bundle manifest + cemini asset whitelist.

## Body

### Ops (shipped)
| Item | Change |
|------|--------|
| Pin self-heal | `researcher_sandbox_auto_submit.py` writes pin on detect + submit |
| replace | **false** — volume on `3b48d01d` |
| pvp_is_finished | paused/queued in-flight; closed finished set |
| Retry script | Refuses replace when `0 < ch < th` |
| Timer | git rev vs pin + bundle layout verify |
| Season tracking | `finalizedSeasons` / `cumulativeHands` in auto-submit state |

### Bot (shipped — next bundle)
| Item | File |
|------|------|
| A3 BTN trim | `research_static_chart.py` — 8 combos removed |
| B2 LAG thin value | `gin_v2_exploits.py` — floor 0.55 vs LAG |
| S2 nemesis | `nemesis_seed.py` — range_ledger, arjun_c, rvkkv1, damon |
| Manifest | `assets/manifest.json` in bundle |
| Whitelist | cemini bundle omits gin_hu004_bridge, ai_pokergame_villain |

### Prod posture
- **NO `--replace`** until `3b48d01d` completes 5k
- Fresh submit after finish picks up K131b finish automatically
- `CEMINI_SUBMIT_SKIP_REV_CHECK=1` only for emergency hotfix with pin bump

## Sources

- `briefs/2026-07-02_postfix-cursor-audit-synthesis-glm-kimi.md`
- `briefs/2026-06-26_k131b-bb-lag-tune-plan.md`
- Live TS: cemini +19 @ 5k vs gin +7.3 @ 5k
