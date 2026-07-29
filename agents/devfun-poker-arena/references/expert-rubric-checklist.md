# Expert rubric checklist (K193)

**arXiv pattern:** BusinessCaseBench / expert-anchored rubrics (2607.16057) —
explode a solver or expert reference into checklist criteria; report partial
vs all-criteria; human-gate money decisions.  
**Pairs with:** `references/turn-street-scores.md` (K191 street tallies)  
**Shelf date:** 2026-07-20

## Steal (pattern only)

Subjective “good play” writeups and LLM judges need **expert-anchored**
criteria, not vibe scores.

1. Take a solver / expert reference line (chart, TexasSolver bucket, yardstick).
2. **Explode** into atomic checklist items (one claim per criterion).
3. Grade **partial** (k of n) and **all-criteria** (pass only if all met).
4. **Human-gate** any money / pin / submit decision — checklist is advisory.

No BusinessCaseBench install. No auto-submit from rubric scores alone.

## Checklist shape

```text
criterion_id | description | source_ref | weight | pass?
preflop_open | open BTN 2.5x with A9s+ chart | STRATEGY.md §preflop | 1 | yes/no
facing_fold  | fold <35% equity facing 75% pot | solver bucket X | 1 | yes/no
river_value  | value-bet thin rivers ≥1/2 pot when … | yardstick | 1 | yes/no
```

## Reporting

| Mode | Rule |
|------|------|
| Partial | Count pass / total; list failed criterion ids |
| All-criteria | Binary pass only if every required id passes |
| Money / pin | Requires human GO — checklist never auto-replaces Active |

## Diagnosis handoff (K195)

Failed criterion ids feed
`capability_tree.diagnose_rubric_failures` — cluster under weakest clear
capability-tree nodes before rewriting prompts or collecting SFT.

See `references/capability-tree-routing.md` § K195.

## Operator rules

1. Prefer criterion-level diagnosis over category averages (“weak on river”).
2. Do not mix diagnostic rubric spots into held-out TrueSkill benches.
3. After new training trajectories, risk-filter before SFT.
