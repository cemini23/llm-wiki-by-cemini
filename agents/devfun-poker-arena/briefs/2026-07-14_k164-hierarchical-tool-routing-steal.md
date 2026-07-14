---
title: K164 — hierarchical tool routing (poker sandbox)
type: brief
target: Poker Arena
created: 2026-07-14
updated: 2026-07-14
---

## Target

`agents/devfun-poker-arena/` — HL analyst loop / Researcher Round tool surface.

## Summary

Steal **capability tree + lazy child manifests** from arXiv 2607.11138 (hierarchical skill stack): stop dumping flat tool/schema menus into `decide()` / analyst prompts as N grows. Route through mutually exclusive top domains (e.g. HUD / spot-memory / verifier / submit) with LIFO nested frames.

**Shipped (2026-07-14):** exclusive domain tree + lazy children; `CapabilityFrameStack` push/pop; HU nested-session smoke (MAFP → exploit → return → prebind submit); HL brief injects active slice only. Advisory — submit leaf still requires Prebind.

## Body

### P0 — domain fence

1. List current poker session tools/skills; partition into **non-overlapping** top domains.
2. Cap per-call visible children to local branching factor (no mega-registry).
3. Nested sub-analysis (e.g. MAFP vs exploit lane) uses explicit push/pop return — not unbounded chat.

### P1 — leaf governance

Any leaf that binds sandbox submit / live decide gates through existing Prebind / verifier steals (K151 / VERITAS cluster) — hierarchy does not bypass them.

### Out of scope

- Porting the paper’s UPI Help product code (REFERENCE only; no public repo)
- Flattening tools back into one prompt “for simplicity” when schema count grows

### Operator checklist

- [x] Tool inventory partitioned (`config/hu_capability_tree.json`: table / policy / memory / eval / submit)
- [x] Flat dump removed from default HL prompt path (lazy children via `examples/capability_tree.py`; advisory)
- [x] Nested frame return tested on one HU Researcher Round session

## Shipped

| Artifact | Notes |
|----------|-------|
| `config/hu_capability_tree.json` | Domains + `max_frame_depth` |
| `examples/capability_tree.py` | `CapabilityFrameStack` + `simulate_hu_researcher_nested_session` |
| `examples/cemini_hl_brief.py` | Active slice + `*.capability-session.json` |
| `references/capability-tree-routing.md` | Operator spec |
| `tests/test_k164_capability_tree.py` | Exclusive domains + push/pop + session smoke |

```bash
uv run pytest tests/test_k164_capability_tree.py -q
```

## Sources

- CCC `@sources/arxiv-hierarchical-skill-stack-lazy-orchestration-2607.11138.md`
- Prod brief `cemini-prod:/opt/cemini/briefs/2026-07-14_k164-hierarchical-skill-stack-lazy-orchestration-prod.md`
- TipDrop David: `tipdrop-workspace-kit/briefs/2026-07-14_k164-hierarchical-skill-tree-adopt.md`
