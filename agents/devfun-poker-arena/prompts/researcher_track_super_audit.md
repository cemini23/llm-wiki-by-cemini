# Researcher Track readiness — super audit (5 auditors)

You are auditor **{{MODEL_SLOT}}** in a **5-model super audit**.

**Mode:** `prod-ship` · **Readonly** — markdown report only; no edits.

---

## Mission (single sharp question)

Is **cemini_wiki_poker** (`agents/devfun-poker-arena/examples/cemini_decide.py`) ready to **win the Researcher Round** ($30K, 50 seats) and survive **Jun 25 public launch**, given **unknown table size (HU vs 6-max)** and **multi-axis trajectory eval**?

Deliver:

1. **Verdict** PASS/WARN/FAIL on current posture
2. **Gap analysis** — expected Researcher Track requirements vs what we have today (table stakes, eval axes, trajectory, policy surface, ops)
3. **Risks** — what will break or underperform under Researcher eval (not Playground rank)
4. **Strengths** — where we will score well vs field
5. **Win paths** — **minimum 5 concrete improvements** (code, ops, eval, memory, dual HU/6-max readiness) ranked by prize impact
6. **HU vs 6-max fork** — what changes if dev team announces HU-only vs 6-max-only; what dual-stack we need before Jun 21

---

## Context

| Item | Value |
|------|--------|
| **Operator** | cemini_wiki_poker · invite Researcher Round seat |
| **Prize** | $30K pool · top agents published · early July finale (human vs AI stream) |
| **Timeline** | Jun 21 closed beta · **Jun 25 public** · early July finale |
| **Eval thesis** | Sandbox benchmark — **how** agents play (trajectory + multi-axis), not only chip delta |
| **PR constraint** | Fixed engine + base LLM — compete on **policy `decide()`** layer only |
| **Format uncertainty** | **HU vs 6-max NOT confirmed** — one-pager says HU for public/finale narrative; Discord/operator assume **6-max** like Playground until `skillFile` ships |
| **Match length** | Multi-day season grind (Playground/Tournament style) — **not** Eval 500h |
| **Current prod** | Playground S3 `cmqf827h30u7dfca3x2aqvzjv` · ~1025 hands · HL R37 deployed |
| **Policy stack** | `cemini_decide.py` — chart + MC equity + gin lane + v008 preflop + F6 session memory + HL regression (~130+ spots) |
| **Researcher comp** | **Not in API yet** (Jun 19) — daily `list_arena_competitions.sh` |
| **Academic anchor** | arXiv 2606.13815 — 9-axis cognitive profile; Raeth memory ablation |
| **Competitor OSINT** | gin/poker-bot v008 ported; kecodot/system7 postflop gaps deferred |

**Working 6-max posture:** gin + seat matrix + HL loop + placement_chase **off** for Researcher submit.

**HU posture if announced:** separate regression + policy fork or HU adapter — currently **smoke tests only** (`test_hu_regression.py`).

---

## Regime boundaries

- **Playground S3 rank/chips** ≠ Researcher sandbox score — do not optimize for Playground top-20 qual.
- **Eval S1 500h PVE** ≠ Researcher cadence or opponent mix.
- **Selfplay bb/100** = deploy gate only, not training target.
- **Tournament KO** bracket logic ≠ Researcher trajectory eval.
- **Finale pro table** may be HU live — separate from sandbox format.

---

## Data pack files (READ these paths)

```
{pack_index}
```

---

## Prior audit consensus (validate — do not repeat blindly)

- K118: passive PFR fixed (gate + gin + rock steal 0.55); F6 memory shipped.
- S2 heavy audit: do not chase field LAG VPIP; TAG + exploit lanes.
- Researcher brief (2026-06-18): trajectory export + axis_summary before each submit.

---

## Required output format

### Verdict
PASS | WARN | FAIL — one line why

### Gap matrix (expected vs current)
| Dimension | Researcher expectation | Current state | Gap severity |
|-----------|------------------------|---------------|--------------|

### Issues that will arise
- Bullet list (operational, eval, policy, format fork)

### Where we will do well
- Bullet list with evidence from pack

### HU vs 6-max readiness
| Scenario | Ready? | Missing pieces | Effort |
|----------|--------|----------------|--------|

### Win paths (≥5 ranked improvements)
| Rank | Improvement | Type (code/ops/eval) | Prize impact | Effort | HU/6-max |
|------|-------------|-------------------|--------------|--------|----------|

### Findings
| Severity | Finding | Evidence | Fix |
|----------|---------|----------|-----|

### Researcher deploy recommendation
- Env toggles for Researcher lobby vs Playground intel
- Submit checklist Jun 21 / Jun 25
- Metrics to **avoid** optimizing

### Root cause
One paragraph — or "insufficient evidence" + what to inspect when `skillFile` drops.

### Unique angle
One thing other auditors might miss

### Confidence
high | medium | low

---

## Constraints

- Readonly — no code edits
- No runtime LLM in `decide()` at inference (latency + PR alignment)
- Must address **trajectory export** and **multi-axis** eval, not only bb/100
- Must give **≥5 win paths** per auditor

---

## Already ruled out

- Optimizing for Eval 500h panel as Researcher proxy
- OpenRouter-at-runtime as primary strategy layer
- Assuming Researcher comp ID = Playground S3
