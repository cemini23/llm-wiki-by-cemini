---
title: Post-fix sandbox cursor audit — GLM 5.2 + Kimi 2.7 synthesis
type: brief
created: 2026-07-02
models: [glm-5.2-high, kimi-k2.7-code]
active_submission: 3b48d01d-3f33-4467-a108-8111d03c2163
status: ACTIVE
---

## Target

Operator — Researcher S2 sandbox after cemini revert audit fixes + live replace submit.

## Summary

**Overall: SHIP-WITH-FIXES (WARN/WARN).** Cemini replace **live** (`3b48d01d`, PvP in flight). Tooling fixes landed; **two P0 classes remain:** (1) **ops/pin safety** — auto-submit must reconcile pin, flip `replace:false`; (2) **bot strategy** — finish K131b A3/B2 + refresh nemesis list before chasing volume to 20k.

## Live evidence

| Submission | Engine | Hands | TS @ checkpoint |
|------------|--------|-------|-----------------|
| 5f6f3aec | cemini | 5k | +19.0 |
| 8545120c | gin hu004 | 5k | +7.3 |
| 3b48d01d | cemini replace | ~206/5k early | high σ (normal) |

## Consensus (both auditors)

- Cemini revert **correct** — do not re-ship gin as live engine
- **Pin/version discipline broken** — prod pin updated by retry script; laptop was stale; `replace:true` dangerous now
- **K131b incomplete** — BTN trim + LAG thin value still open
- **Nemesis list stale** vs S2 Tier-0 field snapshot
- Volume to **20k** requires ~4× 5k seasons — need season tracking + safe auto-submit

## Unique angles

| Model | Insight |
|-------|---------|
| GLM 5.2 | Pin is one-way artifact; auto-submit never writes back → timer can destroy active season |
| Kimi 2.7 | Finish half-merged K131b beats more gin/competitor work |

## Recommended fix order

### Ops (before next timer tick)
1. Pin self-heal in `researcher_sandbox_auto_submit.py` (IDs + metadata on submit/detect)
2. **`replace: false`** in pin now that cemini is live
3. Tighten `pvp_is_finished` (closed-set + `ch >= th`)
4. Retire or guard `retry_cemini_replace_submit.sh`

### Bot (next code wave — K131b finish)
5. A3: trim 12 BTN combos in `research_static_chart.py`
6. B2: LAG thin-value floor in `gin_v2_exploits.py`
7. Append S2 nemesis handles in `nemesis_seed.py`
8. Bundle `manifest.json` + bump `agentVersion` on next replace

### Backlog
9. Bundle whitelist (omit gin_* from cemini zip)
10. Season-count / cumulative 20k tracking in auto-submit state

## Verdict rollup

| Model | Verdict |
|-------|---------|
| glm-5.2-high | WARN |
| kimi-k2.7-code | WARN |

**Overall:** SHIP-WITH-FIXES — run volume on `3b48d01d`; implement ops P0 before timer; schedule K131b finish for next bundle.
