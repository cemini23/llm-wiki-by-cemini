# K122 validation + execution plan (2026-06-19)

## Target

CeminiSuite / OSINT — validate gambling-wiki K122 against shipped Researcher HU posture; execute remaining pre-Jun 21 gaps.

## Summary

K122 synthesis **matches** OSINT code + gates. This brief tracks shipped vs gap items (PFR, series match W/L, prod intel) for operator execution.

**Verdict:** Gambling-wiki K122 synthesis is **TRUE** — matches OSINT posture + code audit.

## Already shipped

| Item | Status |
|------|--------|
| HU fork (`CEMINI_TABLE_FORMAT`, `_HU_OPEN_CHART`, 29 spots) | ✅ |
| MC equity + chart + HUD + F6 session memory | ✅ |
| Offline HL (auto-analyst **off** on prod Researcher PRIMARY) | ✅ |
| Trajectory + M₁–M₉ gates | ✅ |
| Prod Researcher PRIMARY, Playground intel-only | ✅ |
| `devfun-org/poker-arena-starter-kit` documented (gambling entity) | ✅ |
| K118 partial (rock steal, chart PFR order, F7 multiway, audit gate) | ✅ partial |

## Gaps (execute now, pre-Jun 21)

| Gap | Evidence | Target |
|-----|----------|--------|
| **K118 HU PFR / limp gap** | 400h HU audit: PFR 9.4%, VPIP−PFR **29.3%** (gate fail) | PFR ≥15% HU; gap ≤10% |
| **TrueSkill proxy** | Selfplay reports bb/100 only | Match W/L + optional series gate |
| **HU 3-bet / defend** | Chart wide open but passive completes | Jungleman-band 3-bet defense path |
| **Jun 21 docs** | SDK/Kaggle URL pending | Recon script + wiki stub on arrival |

## Do NOT (K122 agrees)

- Runtime LLM `decide()`
- CFR weights before Jun 25
- Optimize selfplay bb/100 as training objective
- Playground HL auto-patches on 6-max analyze
- Style emulation code until rules land (hold `CEMINI_RESEARCHER_STYLE_TARGET`)

## Parallel workstreams (this session)

1. **W-PFR** — HU preflop raise-first; tighten limp-complete; HU audit thresholds
2. **W-MATCH** — `selfplay.py` / audit: match win rate, HU gate hook
3. **W-DOC** — OSINT readiness K122 validation table + gambling cross-links

## Jun 21 gate (operator)

- Pin `competitionId`, Kaggle URL, TrueSkill docs
- First sandbox submit after `run_hu_sandbox_gate.sh --hands 500`

## Sources

- Gambling wiki K122 paper landscape + HU arena strategy (cross-wiki ingest, 2026-06-19)
- `@concepts/devfun-researcher-track-readiness-2026-06.md`
