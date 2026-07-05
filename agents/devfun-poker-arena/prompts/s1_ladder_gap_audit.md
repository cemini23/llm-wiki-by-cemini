# S1 heads-up ladder — premium gap audit (3-model cursor-audit)

You are auditor **{{MODEL_SLOT}}** in a multi-model **gap retrospective audit** for **cemini_wiki_poker** on the public **heads-up ladder S1** (`cmr3n8tft01nilecm1u5jlny7`).

**Mode:** `brief-plan` + poker bot strategy · **Readonly** — output markdown only; no runtime LLM in production bot.

---

## Mission

We are **rank ~100/130**, TrueSkill **μ−3σ ≈ −84** at **~3.6k hands** with **+44 adj bb/100** but negative μ. We will **`--replace`** soon — need structural patches in `cemini_decide.py` that move **μ upward**, not micro-tune bb on weak pairings.

Deliver:

1. **Root-cause clusters** from replay/analyze data (preflop vs postflop vs HU SB OOP)
2. **Ranked P0/P1 patch backlog** — env toggles, guard rules, function names in `cemini_decide.py`
3. **Regression spot IDs** (hand class + board + position + action)
4. **Replace vs engine-swap** verdict (`CEMINI_SANDBOX_ENGINE=gin_hu004` vs more cemini patches)
5. **Do-not-ship** list (over-fold traps)

**Zero LLM at runtime.**

---

## Already shipped (do not re-recommend unless upgrade)

- `_preflop_pot_committed_should_call` — A6o/A2s −950 fold leak (Jul 2026)
- Optional finale imports for bundle startup
- K131b cemini engine (gin hu004 lost on live S2 TS vs cemini)

---

## Live posture

```json
{live_posture}
```

## Hero agent-stats (925+ sample)

```json
{hero_stats}
```

## Failure analyze (50 recent, Jul 2026)

```
{failure_analyze}
```

## Replay chip deltas (50 recent vs cosmometrics/Caravan)

```json
{replays}
```

## Worst-hand clusters (derived)

```
{worst_clusters}
```

---

## Output format (cursor-audit)

### Verdict
REPLACE / PATCH-AND-REPLACE / ENGINE-SWAP — one line + confidence

### P0 patches (ship blockers)
| # | Patch | File | Trigger | Expected EV |

### P1 patches
(same table)

### Regression spots
| id | hole | board | pos | street | action | why |

### Conflicts / risks
…

### Consensus notes for synthesis
…
