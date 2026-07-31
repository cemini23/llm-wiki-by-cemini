---
title: Tournament S10 climb widen — gin ON after #2→#46 bleed
type: brief
tags: [brief, poker, tournament, s10, climb, gin]
created: 2026-07-31
target: agents/devfun-poker-arena
---

## Target

Live Tournament S10 lobby — restore chip climb after peak #2 → ~#46 @ ~740.

## Summary

12h action mix ~79% fold / ~7% raise while CHASE zone was on. Leaders ~5–7k chips; we bled blinds under gin-OFF + nemesis_tight + survival ratchet. Go-live brief already allowed gin widen when KO analyze shows too-nitty — this ships that.

## Changes (deployed)

| Knob | Was | Now |
|------|-----|-----|
| Gin / V008 / V2 | OFF | **ON** |
| KO survival | ON | **OFF** |
| Nemesis tight | 1 | **0** |
| Cold-start no-steal | 1 | **0** |
| Survival stack | 350 | **200** |
| Chase margins | −0.02 | **−0.04** + equity 0.38 |
| Chase MP/SB steals | modest | wider |
| Join pace | 25/60 | **12/25** |

Code: chase ignores stack `survival_tight` when `placement_chase`; posture block no longer forces gin OFF.

## Today briefs (Jul 31) — actionable?

| Brief | T10 action now? |
|-------|-----------------|
| K230/K233 model-when radio | Policy only — session prompts; no decide patch |
| K231 secure-codegen confidence | Advisor gating — N/A (no side veto on decide) |
| K232 AISPA system-prompt audit | Follow-up inventory — not a climb lever |

## Verify

```bash
# journal should show CHASE + more raise/bet share over next 1–2h
timeout 20 journalctl -u cemini-devfun-poker-lobby.service -n 30 --no-pager
./scripts/cemini_playground_status.sh --competition cms7hr1il20ya13wjj29s1o8h
```

## Risk

Gin widen can bust faster. If stack <400 and rank worsening after 200 hands, re-evaluate; do not re-enable nemesis_tight first — dial gin_postflop off instead.

## Sources

- `briefs/2026-07-28_tournament-s10-go-live.md` (gin widen when KO analyze too-nitty)
- Live prod journal 2026-07-31 (~79% fold / 12h; rank #2 best → #46 @ ~741)
- T9 winner intel: halloran VPIP ~0.26
