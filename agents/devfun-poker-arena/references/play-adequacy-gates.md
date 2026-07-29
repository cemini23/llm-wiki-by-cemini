# Play-adequacy gates (K158)

**arXiv pattern:** [2607.14169](https://arxiv.org/abs/2607.14169) (code world models — play-adequacy vs transition accuracy)  
**Shelf date:** 2026-07-17  
**Brief:** `briefs/2026-07-17_k158-play-adequacy-gate-steal.md`

## Steal (pattern only)

A sim / policy that passes **transition-accuracy** sampling (legal moves, log
replay match) can still lose at **play** when the omitted rule is rare under
random trajectories but pivotal under competent search. Ship gates must include
**play / search-visited** regressions — not only transition/match checks.

**No CWM+MCTS runtime** in this repo — gate taxonomy + rare-spot fixtures only.

## Two gate classes

| Class | What it proves | Arena examples |
|-------|----------------|----------------|
| **Transition / match** | Legal action shape, schema, hand-log fidelity, mechanical invariants | `test_sandbox_mechanical_invariants.py`, allowed-action parse, trajectory format, many selfplay “did not crash / transitioned” smokes |
| **Play / search** | Competent-play decision quality on spots random logs rarely hit | `tests/test_play_adequacy_spots.py`, HU ladder guards that assert **fold/check** (not mere non-crash), yardstick H2H bb/100 |

Existing HU ladder tests in `tests/test_cemini_hu_ladder_guards.py` that assert
`decide() == fold` are **play-class** (labeled here for audit). Pure transition
tests must not be rebranded as play-adequate.

## Verifier–deployment gap (K198)

Agents that author both policy and accept tests create a **verifier–deployment
gap** (arXiv 2607.24300). Play-class fixtures + frozen yardsticks are the
external accept surface — see `references/verifier-deployment-gap.md`. Do not
promote on transition-class self-tests alone.

## Danger law

If a pivotal leak has rarity \(r\) under random sampling, the probability that
\(N\) random logs miss it is approximately:

\[
(1 - r)^{N}
\]

Example: \(r = 0.001\), \(N = 500\) → miss probability \(\approx 0.61\). Random
selfplay gates alone cannot ship rare board textures / ICM cliffs / overbet
underpairs.

**Implication:** add **adversarial or targeted** fixtures for search-visited
spots; do not treat “transition accuracy 1.0 / 200 random hands green” as
enough for replace.

## Arena checklist (operator)

- [ ] Preflight lists which gates are **transition/match** vs **play/search**
- [ ] ≥1 rare pivotal HU fixture asserts safe action (`fold` / `check`) — see
      `tests/test_play_adequacy_spots.py`
- [ ] Existing transition tests stay green (do not remove)
- [ ] Head-to-head / yardstick play remains the outer ship bar (`run_hu_sandbox_gate.sh`)
- [ ] Specification first: if a rule is missing from `decide()`, add the rule +
      fixture — not more similar random trajectories

## Fixture inventory (play-class, non-exhaustive)

| Spot | Assert | File |
|------|--------|------|
| IP underpair on paired board facing river overbet | `fold` | `test_play_adequacy_spots.py` (K158 rare pivotal) |
| 88 underpair on trip nines | `fold` | `test_cemini_hu_ladder_guards.py` |
| QTo air on four-straight river | `fold` | `test_cemini_hu_ladder_guards.py` |
| AQo ace-high paired river | `fold` | `test_cemini_hu_ladder_guards.py` |
| K7 boat on trip nines | **not** fold | `test_cemini_hu_ladder_guards.py` |

## Related

- Gate script: `scripts/run_hu_sandbox_gate.sh` (header notes transition vs play)
- Hierarchical memory / DeepSearch filter: K161 (which units enter HL — not play adequacy)
- Brief: `briefs/2026-07-17_k158-k185-k141-master-plan.md`
- Eval claim ceiling (K220): `references/eval-claim-ceiling.md`

## Refresh — 2026-07-18 (arXiv 2607.14169 / K173)

**Brief:** `briefs/2026-07-18_k173-play-adequacy-gate-refresh.md`  
**Paper:** [arXiv 2607.14169](https://arxiv.org/abs/2607.14169) (full PDF ingest → OSINT concept `play-adequacy-vs-prediction-accuracy`)

Reinforces K158; **does not weaken** any gate above.

| Hold | Rationale |
|------|-----------|
| **Play-adequacy ahead of log-match** | Transition-accuracy / hand-log fidelity alone remains the **wrong** ship criterion for sandbox replace. Prefer play / search-visited regressions over “did not crash / transitioned.” |
| **Rare pivotal leaks** | Still need **adversarial or competent-play** samples — random selfplay miss-rate law unchanged. |
| **Spec completeness** | If a rule is missing from coded heuristics, add the rule + targeted fixture; do not burn more similar random dumps. |

**Still out of scope:** vendoring CWM planners as runtime `decide()`; full multi-model synthesis burns.

Existing transition/match tests stay green and stay labeled transition-class. Existing play-class fixtures (`test_play_adequacy_spots.py`, HU ladder fold/check asserts) stay mandatory for ship.

## Check

```bash
uv run pytest tests/test_play_adequacy_spots.py tests/test_cemini_hu_ladder_guards.py -q --tb=line
test -f references/play-adequacy-gates.md
rg -n "2607.14169|2026-07-18" references/play-adequacy-gates.md
```
