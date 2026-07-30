# Super audit — Tournament S10 prod posture

**Mode:** prod-ship · **Auditors:** 3 Cursor (+ API attempted) · **Tier:** default-5-model → **degraded API** (OpenRouter 402)

| Slot | Channel | Role | Model | Verdict |
|------|---------|------|-------|---------|
| 1 | cursor | security/prod-risk | premium | REWORK |
| 2 | cursor | strategy/exploit | premium | REWORK |
| 3 | cursor | correctness/config | premium | REWORK |
| 4 | api | api-adversarial | openrouter/fusion | FAIL 402 |
| 5 | api | api-deep-reasoning | z-ai/glm-5.2 | FAIL 402 |

## Consensus (≥3 Cursor)

1. **P0:** `_ko_survival_lane` set both `ko_survival_lane` and `survival_mode` → hard survival_tight; placement_chase never widens.
2. **P0:** `CEMINI_SURVIVAL_STACK_CHIPS=800` ≈ 40bb ratchet after one pot — too high.
3. **P1:** Nemesis missing T9 winner `halloran` (+ reaper/vigilate); `NEMESIS_TIGHT=0` gated named tight path.
4. **P1:** `PRIZE_CUTOFF_RANK=10` enters protect too early for win chase — prefer top-3.
5. **Keep gin OFF** (unanimous).

## Winner intel (T9)

`halloran` ~90k / 5563 hands · VPIP ~0.26 · PFR ~0.11 · AF ~1.05 · ~+16 chip/hand — balanced volume, not pure nit.

## Patches applied 2026-07-30

| Fix | Status |
|-----|--------|
| Drop `survival_mode` from KO lane | shipped + rsynced |
| `placement_chase` margins before mild KO | shipped + rsynced |
| Villain mem during KO when chasing | shipped + rsynced |
| `_apply_competition_posture` forced `PRIZE=10` → **3** | shipped + rsynced (was clobbering .env) |
| `SURVIVAL_STACK_CHIPS` 800→350 | prod + posture |
| `KO_SURVIVAL_HANDS` 60→20 | prod + posture |
| `NEMESIS_TIGHT=1` + halloran/reaper/… | prod |
| Gin OFF | confirmed |
| Lobby restart | **active** — `CHASE zone (need top 3 for prize)` ~rank 28 / ~810 chips |

## Overall

**REWORK → patched on prod.** Do not enter S11 until T10 deep run. Local commit pending operator ask.
