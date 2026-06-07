---
title: "Nuts detection spec — river unbeatable (v1)"
type: brief
tags: [brief, poker, cemini-decide, hand-evaluation, spec]
created: 2026-06-05
status: SHIPPED — prod `CEMINI_NUTS_DETECT=1` since 2026-06-06; no regressions through HL R22
target: examples/hand_nuts.py → examples/cemini_decide.py
---

## Problem

Prod `cemini_decide.py` uses **Monte Carlo equity** (treys, ~200–500 sims vs **one random** villain hand) plus **HL leak heuristics**. It does **not** compute whether hero **cannot lose** on the current board.

Mis-implementing “nuts” logic and deploying would cause catastrophic folds (e.g. folding quads) or spewy calls (treating turn nut flush as unbeatable before a board pair ships a full house).

**Goal (v1):** Detect **river unbeatable** hands with **provable enumeration**, not MC guesswork. Use only to **prevent folds** and **allow value** — never to widen preflop trash or override bankroll locks.

---

## Definitions (precise)

| Term | Meaning | v1 deploy? |
|------|---------|------------|
| **MC equity** | P(win) + 0.5×P(chop) vs one random hand, random runouts on incomplete boards | Already live |
| **Strict nuts** | Hero’s best 5-card score equals the **best score any player could hold** on this board | Info only |
| **Unbeatable (river)** | On a **complete 5-card board**, **no** villain hole-card pair produces a **strictly better** treys score than hero | **Yes — v1 gate** |
| **Nut high (draw)** | Best made hand *type* so far; can still lose on later streets | **No — do not auto-commit** |

### treys scoring convention [CONFIRMED in repo]

- `Evaluator.evaluate(board, hand)` → integer **1…7462**
- **Lower score = stronger hand** (1 = royal flush)
- Villain **beats** hero iff `villain_score < hero_score`
- **Chop** iff `villain_score == hero_score`

Hero is **unbeatable** on river iff:

\[
\forall (c_1, c_2) \in \text{RemainingDeck}:\quad \text{evaluate}(\text{board}, [c_1,c_2]) \geq \text{hero\_score}
\]

Equivalently: **no** remaining pair yields `score < hero_score`.

**Important:** This is “cannot **lose**” (may chop). That is the safe property for “never fold.”

**RemainingDeck** = 52-card deck minus `{hero hole} ∪ {board}` — **5 + 2 = 7 cards removed**, **45 cards left**, **C(45,2) = 990** villain combos. At ~990 treys evals, runtime ≪ 10s deadline.

---

## What v1 does NOT claim

1. **Flop / turn “nuts”** — e.g. nut-flush **draw** or top set can be outdrawn; **v1 runs only when `len(board) == 5` and street is River** (or board complete).
2. **Unique nuts** — hero may chop (e.g. board plays, both have same boat). Still **unbeatable**.
3. **Multiway range modeling** — enumeration assumes villain may hold **any** remaining pair; conservative for “can I lose?”
4. **Known folded cards** — v1 ignores other mucked cards (slight over-estimate of villain strength → fewer false “unbeatable”; acceptable). v2 may subtract visible dead cards from `recentEvents`.
5. **ICM / tournament** — Playground is chip EV; chops still fine.

---

## Algorithm (reference implementation)

New module: `examples/hand_nuts.py` (pure functions, unit-tested; no decide() side effects).

```python
def river_unbeatable(hole: list[str], board: list[str]) -> tuple[bool, int | None, str]:
    """
    Returns (unbeatable, hero_score, hero_class_str).
    False if board incomplete, treys missing, or invalid cards.
    """
```

### Steps

1. **Guard inputs**
   - `len(hole) == 2`, `len(board) == 5`
   - Convert Arena cards → treys via existing `_to_treys()` from `agent.py`
   - If conversion fails or treys unavailable → `(False, None, "unknown")`

2. **Build dead set**
   - `dead = {hero_card_treys…} | {board_card_treys…}`
   - Assert `|dead| == 7` (no duplicate card strings)

3. **Hero score**
   - `hero_score = evaluator.evaluate(board_t, hero_t)`
   - `hero_class = evaluator.class_to_string(evaluator.get_rank_class(hero_score))`

4. **Enumerate villain combos**
   - `remaining = [c for c in full_deck if c not in dead]`
   - For each `(c1, c2) in combinations(remaining, 2)`:
     - if `evaluator.evaluate(board_t, [c1, c2]) < hero_score`: return `(False, hero_score, hero_class)`
   - Return `(True, hero_score, hero_class)`

5. **Singleton evaluator** — reuse one `TreysEvaluator()` per process (module level).

### Complexity

- 990 evaluations × ~50µs ≈ 50ms typical — safe within `deadline_s >= 2`

### Fast path (optional, must match enumeration)

Keep existing `_hero_made_royal_flush()` as early exit **or** fold into enumeration (royal → score 1 → always unbeatable). Property test: royal path ⇒ `river_unbeatable` True.

---

## Integration into `cemini_decide.py` (conservative)

### Feature flag

```bash
CEMINI_NUTS_DETECT=1   # default OFF in prod until checklist done
```

When `0` or unset: **zero behavior change**.

### When unbeatable == True (river only)

| Situation | Allowed override | Forbidden |
|-----------|------------------|-----------|
| Facing any bet / raise | **Never fold** | — |
| Free to act (check/bet) | Prefer **value bet** (reuse `_royal_made_action` sizing or 66–85% pot) | Do not shove 100% stack if `max_playable` / stagger lock caps apply |
| HL leak rules (J2o paired, weak pair, etc.) | **Skipped** if unbeatable | — |
| MC equity low | Ignore for fold decision | — |
| Preflop | **No effect** | — |
| Turn / flop | **No effect** | — |
| `qualification_protect` / stagger lock | May still cap **bet size**; must not force fold | — |
| Clock `deadline_s < 2` | Skip enumeration (too tight); fall back to current behavior | — |

### Order in `decide()`

Place **after** hole/board parse, **before** HL leak folds:

```
if nuts_enabled and street == "River" and len(board) == 5:
    unbeatable, score, cls = river_unbeatable(hole, board)
    if unbeatable:
        if facing_bet: return fold-forbidden value line (call or raise)
        else: return value bet / check trap (same as royal branch)
# existing royal flush block may merge here
# ... existing HL leak guards ...
```

### Reasoning YAML

Add tag e.g. `ke: "nuts riv"` or `bf: [unbeatable]` for postmortem — max 150 chars unchanged.

---

## Verified test matrix (must pass before deploy)

Prototype enumeration run 2026-06-05 against treys 0.1.8:

| Case | Hole | Board | Expected unbeatable | Notes |
|------|------|-------|---------------------|-------|
| Royal | Qh Jh | Ah Kh Th 5d 2c | **True** | score=1 |
| Quads | Ac Ah | As Ad 7c 2h 3s | **True** | |
| Full house (vulnerable) | Ac 3h | As Ad 7c 7h 2s | **False** | villain boats/quads exist |
| Board straight | Tc 2d | 9s 8h 7d 6c 5s | **False** | villain J-T beats |
| Nut straight | Jc Th | 9s 8h 7d 6c 2s | **True** | score=1603 |
| Lower straight | 9c 8d | 9s 8h 7d 6c 5s | **False** | J-T exists |
| Nut flush | Ah Qh | Jh Th 5h 2h 3c | **True** | |
| Second nut flush | Kh Qd | Jh Th 5h 2h 3c | **False** | Ah live |
| A-high flush (SF possible) | Ah 2c | Jh Th 5h 7h 3c | **False** | Qh8h etc. |
| High card on flush board | Ad Kc | Qh Jh 2h 7h 3c | **False** | many flushes beat |
| Board quad chop | 3d 4c | 2c 2d 2h 2s Ac | **True** | all play quads; no beater |
| Vulnerable full house | 7c 2d | 7s 7h Kd 3c 2s | **False** | villain 7x → quads |

Additional **regression spots** (add to `tests/fixtures/regression_spots.py`):

1. `prod_nuts_river_value` — nut straight, must **bet** or **raise**, not check-fold
2. `prod_nuts_river_never_fold` — quads facing pot-size bet, must **call** or **raise**, forbidden **fold**
3. `prod_not_nuts_river_fold_ok` — second nut flush, existing leak logic may fold — **must not** mark unbeatable
4. `prod_board_plays_chop` — board four deuces + Ace, hero 3d 4c — unbeatable **True** (quad chop), must not fold

Property tests (hypothesis or loop):

- For all 990 villain combos when `unbeatable=True`, assert no `v_score < hero_score`
- `unbeatable=True` ⇒ `hero_score <= best_possible_score_on_board` (best possible = min over all pairs)

---

## Failure modes (why wrong deploy loses stack)

| Bug | Symptom | Loss mode |
|-----|---------|-----------|
| Treat turn flush as unbeatable | Call/shove before board pairs | Full house disaster |
| Inverted treys compare (`>` instead of `<`) | Fold nuts, call with trash | Catastrophic |
| Duplicate card in dead set not caught | Wrong enumeration | False unbeatable → call off |
| `len(board) < 5` enabled | “Nuts” on flop | Overcommit |
| Override stagger **fold** incorrectly | Ignore bankroll cap | Less common if only blocks fold |
| Skip treys on prod | Silent fallback False | Miss value (OK) not loss |
| Force 100% pot shove on every unbeatable | Overcommit vs nit | Stack volatility |

---

## Rollout checklist (mandatory)

- [x] `examples/hand_nuts.py` + `tests/test_hand_nuts.py` — full matrix green
- [x] Regression spots frozen (4+ cases above) + all-in-only shove menu
- [x] `CEMINI_NUTS_DETECT=0` default; prod `.env` enables only after review
- [x] `./scripts/cemini_anti_profiling_audit.py` pass (2026-06-06 — 376 spot-runs OK)
- [x] `./scripts/cemini_preflight.sh` pass — 147/147 (2026-06-06; audit timeout 360s)
- [ ] Manual review: 10 live replays where hero had strong hand — confirm no false unbeatable
- [x] Deploy with flag **OFF**, then enable on prod `.env` only — **enabled 2026-06-06**
- [x] HL analyze post-enable (~50 hands) — **2090+ hands**, no false-unbeatable pattern in R22 analyze

**Do not merge royal + nuts into one branch until tests prove equivalence on all royal cases.**

---

## v2 (out of scope for first deploy)

- Turn: **nut draw** detection (nut flush draw ≠ unbeatable)
- Subtract **known dead cards** from `recentEvents` / shown muck
- **Strict nuts** vs **unbeatable** split for sizing (thin value when chop possible)
- Multiway: tighten only when side pots isolated
- Wiki ingest after v1 validated on prod

---

## Relation to existing code

| File | Role today |
|------|------------|
| `agent.py` `estimate_equity()` | MC vs 1 random — keep |
| `cemini_decide.py` `_hero_made_royal_flush()` | Special-case value — merge after v1 proven |
| `pokerskill_prompt.py` `nut_high` | Text parse from library — not enumeration |
| HL leak guards | Must yield to **river unbeatable** only |

---

## Sources

- treys: lower score = stronger [ihendley/treys](https://github.com/ihendley/treys)
- @wiki/entities/bots/cemini-devfun-poker-agent.md — layer stack
- Prototype validation: local treys 0.1.8, 2026-06-05
