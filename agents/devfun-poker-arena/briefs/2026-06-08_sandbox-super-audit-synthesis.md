# Super audit synthesis — sandbox beta S1

## Target

claude.ai / operator — GO/NO-GO on sandbox HU bot after 5-model super-audit.

## Summary

Five auditors WARNed on structural maniac passivity and bundle gaps; patches shipped; post-fix gate shows **40% series win vs maniac and LAG**; live submission `59e6c951…` Active. LAG-tuned resubmit blocked by daily Arena cap until UTC reset.

**Mode:** prod-ship · **Pack:** `pack-sandbox-beta-s1` · **Built:** 2026-06-23

| Slot | Channel | Role | Model | Verdict |
|------|---------|------|-------|---------|
| 1 | cursor | agentic-reasoning | claude-opus-4-8-thinking-high | WARN |
| 2 | cursor | code-implementation | gpt-5.3-codex | WARN |
| 3 | cursor | third-lens | gemini-3.1-pro | WARN |
| 4 | api | api-adversarial | z-ai/glm-5.2 | WARN |
| 5 | api | api-deep-reasoning | openrouter/fusion | WARN |

## Strong consensus (≥4 auditors)

- Structural passivity vs maniac/LAG (maniac series ~20%, −72.5 bb/100 local)
- `harness/strategy.py` env posture OK but bundle must include trajectory config + parity fixes
- Dual Active `always_fold` smoke — next submit must `--replace`
- gin_style intercepting HU BB defend before S1B chart lane
- s1b 3-bet sizing inflated (`pot + call_chips` × mult)

## Ranked patch backlog (implemented)

| P | Patch | Status |
|---|-------|--------|
| P0 | Bundle `trajectory_bound_config.json` | ✅ |
| P0 | gin HU BB defer to chart/S1B | ✅ |
| P0 | HU 3-bet sizing fix | ✅ |
| P1 | maniac margins + postflop raise_bar | ✅ |
| P1 | 3-bet cap 32%, LAG mult fix, iso BB/SB | ✅ |
| P2 | harness deadline + sanitize | ✅ |

## Post-fix gate (200h)

- maniac series_win **40%** (≥38% advisory) — was 20%
- maniac bb/100 **−23.4** — was −72.5
- lag series_win **40%** after LAG/maniac split tune (was 20%)
- GATE PASS, trajectory M₈/M₉ PASS

## Post-fix re-audit (GLM 5.2 + Fusion)

Gate 200h after patches: maniac series_win **40%** (≥38%), maniac bb/100 −23.4 (was −72.5), GATE PASS.

**Submitted:** `59e6c951-95ac-44f2-92ae-2794b9ed08ab` with `--replace` + rebuilt bundle (`bundleSha256` a50c3d9a…). Poll: `uv run python examples/submit_sandbox_pvp.py --poll 59e6c951-95ac-44f2-92ae-2794b9ed08ab`

**Overall:** SHIP — fixes landed; run season harvest at 10k hands.

## Sources

- [Source: agents/devfun-poker-arena/reports/audit/pack-sandbox-beta-s1/]
- [Source: agents/devfun-poker-arena/reports/researcher-round/gate-hu-20260623T225411Z/]

