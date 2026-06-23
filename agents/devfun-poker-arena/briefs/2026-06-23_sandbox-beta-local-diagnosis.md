# Sandbox beta S1 — local diagnosis (no resubmit)

## Target

claude.ai / operator — interpret early ladder rank vs live sandbox metrics.

## Summary

Arena ladder rank **9/10** is **not** evidence the Cemini bundle is broken. Early PvP metrics on the real submission look **positive**; rank is dominated by **hand count** (386/10k vs leaders at 10k complete). Local HU gates **pass**. The **always_fold** smoke submission is still Active and should be treated as dead weight, not the primary bot.

**No Arena resubmit** until explicit operator GO, daily window allows, and `--replace` clears the dual-active state.

## Live Arena snapshot (poll 2026-06-23)

| Submission | Bot | PvP | Hands | TrueSkill | adj BB/100 |
|------------|-----|-----|-------|-----------|------------|
| `1a945a9e…` | Cemini bundle + vendored deps | Active | 386/10000 | **6.08** | **+59.7** |
| `308fdcbc…` | always_fold smoke | Active | 353/10000 | -3.04 | -32.4 |

Leaderboard: `cemini_wiki_poker` rank **9**, score **6.08** (top ~24.9 at 10k hands complete).

**Claim:** `GET /agent/me` → `claimed: null`. Prize eligibility needs owner X claim (site route may differ from `GET /auth/claim/status`).

## Local gate (200h HU, researcher posture)

`CEMINI_TABLE_FORMAT=hu CEMINI_RESEARCHER_MODE=1 CEMINI_MAFP_CHART=1 bash scripts/run_hu_sandbox_gate.sh --hands 200`

- **GATE PASS** — trajectory M₈/M₉ pass, M8 hallucination 0%
- Series win rates: rock 60%, lag **100%**, maniac **20%** (advisory &lt;38% target)
- Selfplay VPIP proxy ~21%, BTN−BB gap ~15%

Report: `reports/researcher-round/gate-hu-20260623T223442Z/`

## Bundle static check

Unzipped `dist/sandbox-pvp-bundle.zip`:

- `harness/strategy.py` sets researcher HU env via `setdefault` (MAFP, trajectory bound, gin, S1B exploit) — **matches prod researcher intent**
- Premium-nit spot Q♦T♠ facing 3× → **call**; 7♣2♦ → **fold**

## Why rank looks bad vs Discord screenshots

1. **Sample size** — TrueSkill and ladder position need thousands of hands; we are ~4% of season target.
2. **Dual Active submissions** — smoke `always_fold` still running; only one LB row per agent (Cemini entry), but smoke wastes daily/submission slot policy and operator attention.
3. **Field leaders finished 10k** — comparison to +77 adj BB/100 screenshots is other players at full sample, not apples-to-apples at 386h.

## Gaps before any resubmit

| Item | Action |
|------|--------|
| Maniac series win rate | Local advisory 20% vs ≥38% — tune S1B / open chart vs hyper-aggressive pool |
| Dual Active bots | Next submit must use `--replace` after smoke is abandoned or season policy allows |
| Daily submission cap | Respect UTC window if capped |
| Local proof | `run_hu_sandbox_gate.sh --hands 500` green |
| X claim | Owner completes claim flow for prizes |
| Commit tooling | `arena_client` base URL, submit script, harness, apply/gate fixes still uncommitted on laptop |

## Recommended operator sequence (when ready to resubmit)

1. `bash scripts/run_hu_sandbox_gate.sh --hands 500`
2. Rebuild bundle if `cemini_decide` changed
3. `uv run python examples/submit_sandbox_pvp.py --replace` (explicit GO only)
4. Poll Cemini submission only; ignore always_fold

## Sources

- Arena API `https://arena.dev.fun/api/arena` (credentials `.arena-credentials`)
- Local gate report `gate-hu-20260623T223442Z`
