---
title: K245 — GuruWatcher Talon HITL levels · Klement polarisation no-arm
type: brief
tags: [brief, guruwatcher, k245]
created: 2026-08-22
updated: 2026-08-22
---

## Target

GuruWatcher (Priority #2). Alert-only; never order placement. No prod scp. Dual-ID: **OSINT / GW K245** = this Talon-level HITL note. Do not collapse onto CCC harness K245.

## Summary

Verdict: **HITL candidates only; 0 new watches.json writes.** Talon 24–28 Aug names SPXW / VXX / VIX / SMH / IWM levels. Klement Tinbergen polarisation has no ticker. Effort: 10 min.

## Body

1. **Talon dashboard (HITL, operator supplies symbol+op+level before arm):**
   - SPXW invalidation $7,573.50
   - VXX OTE $18.50 / warn $19.50
   - VIX accept $15.50
   - SMH $555–550
   - IWM fail $299 / reclaim $302–304
2. **Klement 21 Aug polarisation.** Social circle > news diet. **No auto-arm.**
3. Never auto-rewrite `watches.json`. Dashboards that print a number stay structurally abstentive.
4. XSP Lane rewrite is **not** this brief (see `briefs/xsp-k245-glitchspx-talon-aug24.md`).

## Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| Order placement from alert bot | High | Alert-only invariant |
| Auto-arm from AI-analyst levels | High | Operator-supplied symbol+op+level only |

## Phasing

- **Phase 1:** policy only.
- Success: no new `watches.json` arm from K245 unless the operator names a level.

## Sources

- @sources/substack-rss-glitchspx-2026-08-22-talon-weekly.md
- @sources/substack-rss-klement-2026-08-21-polarisation.md
- @concepts/guruwatcher-macro-watches.md
