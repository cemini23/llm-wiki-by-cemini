# Stigmergic spot scores (K141)

**arXiv pattern:** [2607.15182](https://arxiv.org/abs/2607.15182) (SGM — stigmergic graph memory; ranking which goals enter the planner)  
**Code:** `examples/stigmergy_spot_scores.py`  
**Config:** `config/hu_stigmergy_spot_scores.json`  
**Shelf date:** 2026-07-17

## Steal (pattern only)

Decaying **environment** memory that ranks which candidate goals / spot
classes enter the HL planner — not only how to play after a spot is chosen.

Complements K161 hierarchical session memory + DeepSearch trajectory filter
(eligibility tags). Flow:

1. Filter eligible failure units (K161 `required_tags` / scaffold rules)
2. **Then** rank by stigmergic spot-class scores
3. Only then expand scaffold / GenomeDiff brief

**Advisory only** — never a hard submit gate. No warehouse MAPF / PBS code.

## Channels

| Channel | Update on |
|---------|-----------|
| `pressure` | Recent losses / veto fails in class |
| `completion` | Recent wins / clean folds that matched plan |
| `block` | Spots that caused planner/HL thrash |

Decay each epoch: \(M \leftarrow \rho M\) (then optional \(\Delta\) via `update_score`).

Default rank scalar:

```
score = 1.0·pressure + 1.0·block − 0.25·completion
```

Higher score → earlier in the HL shortlist (prefer pressure/block thrash).

## Config knobs

| Field | Default | Role |
|-------|---------|------|
| `rho` | `0.9` | Epoch decay |
| `cap` | `10.0` | Per-channel clamp |
| `scores` | `{}` | Seed map `class → {pressure, completion, block}` |
| `advisory_only` | `true` | Must stay true for submit paths |

## API

```python
from stigmergy_spot_scores import StigmergySpotScores, apply_stigmergy_to_deepsearch_filter

s = StigmergySpotScores()
s.update_score("btn_vs_bb_river", "pressure", 2.0)
s.update_score("btn_vs_bb_river", "block", 1.0)
s.decay_all()
s.rank_classes(["safe_spot", "btn_vs_bb_river"])
# → ["btn_vs_bb_river", "safe_spot"]  (higher pressure/block first)

# After K161 filter:
ranked = apply_stigmergy_to_deepsearch_filter(filter_out)
```

## Wire

- `config/hu_hierarchical_memory.json` → `long_term_refs` includes this page
- `examples/cemini_hl_brief.py` → optional stigmergy shortlist section
- DeepSearch helper: `apply_stigmergy_to_deepsearch_filter` (does not change eligibility)

## Related

- K161 filter: `references/deepsearch-trajectory-filter.md`
- Hierarchical memory: `references/hierarchical-session-memory.md`
- Briefs: `briefs/2026-07-17_k141-stigmergic-execution-memory-delta.md`

## Check

```bash
uv run pytest tests/test_stigmergy_spot_scores.py -q --tb=line
```
