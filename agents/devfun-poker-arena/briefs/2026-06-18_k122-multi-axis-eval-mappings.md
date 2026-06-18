## Target

`agents/devfun-poker-arena/` — Researcher Round sandbox (Jun 21 beta).

## Summary

Map Raeth **nine-axis cognitive profile** (arXiv 2606.13815) onto Cemini **trajectory export + axis_summary.json** so Researcher submits surface *how* we play, not only chip delta. Prioritize deterministic axes M₄–M₉ before judge-scored M₂–M₃.

## Body

### Scope / regime disclosure

| Dimension | Raeth paper (2606.13815) | Cemini Researcher target |
|-----------|--------------------------|---------------------------|
| Table size | 7-max tournament | **6-max** sandbox [TENTATIVE operator] |
| Hands | 50 sessions × 20 hands (1,000 total) | Multi-day season — length TBD |
| Models | 7 frontier LLMs (frozen weights) | Single agent (`cemini_wiki_poker`) |
| Memory | 3-layer Raeth ablation (L1/L2/L3) | F6 session memory (+ optional cross-session) |

Axis **definitions** (M₁–M₉) are portable; **absolute scores are not comparable** across regimes without **regime-conditioned** recalibration on dev.fun sandbox data.

### Raeth axes → Cemini proxies

| Raeth axis | Deterministic proxy in `researcher_trajectory_summary.py` | Gate |
|------------|-----------------------------------------------------------|------|
| M₁ Bet sizing | Bet-ratio histogram vs reference (per street) | P1 |
| M₄ Composure | VPIP/AF delta in 7-hand windows post bad-beat | P1 |
| M₅ Adaptability | Seat-level strategy drift vs session start | P2 |
| M₇ Strategic mixing | Action entropy by (street, position) bucket | P2 |
| M₈ Factual accuracy | Card/pot consistency checks in reasoning YAML | **P0** — block submit on hallucination |
| M₉ Positional awareness | Preflop VPIP rank by seat (6-max matrix) | **P0** — Kimi-loss analog |

M₂ (bluffing) and M₃ (opponent reading) need LLM judges — skip unless dev.fun publishes judge spec.

### Memory ablation discipline

Raeth: memory **helps GPT, hurts Kimi, neutral Claude**. Before enabling F6 cross-session seed for Researcher:

1. Run paired submits: F6 on vs empty session notebook (same seed if sandbox supports).
2. Log chip swing + axis deltas in `deploys.jsonl`.
3. Do not assume memory always improves LB rank.

### Submit checklist (Jun 21)

- [ ] `run_hu_sandbox_gate.sh` green (6-max regression + trajectory bundle)
- [ ] `export_researcher_trajectory.sh` → `axis_summary.json` attached to channel post
- [ ] M₈/M₉ thresholds documented in `references/researcher-track-sandbox.md`
- [ ] `list_arena_competitions.sh` pins Researcher `competitionId`

### Key Raeth finding to internalize

> Claude #1 chips, #5 mean axis — **cross-axis consistency** beats peak specialty.

Optimize for **no salient axis holes** (bet sizing + positional awareness floor) before chasing aggression spikes — a **regime-conditioned** goal on our 6-max sandbox, not a claim to replicate Raeth 7-max rankings.

## Sources

- [Source: arXiv:2606.13815 (retrieved 2026-06-18)]
- @wiki/concepts/poker-arena-multi-axis-cognitive-profile.md
- @wiki/sources/arxiv-poker-arena-multi-axis-2606-13815-2026-06-18.md
- @wiki/concepts/devfun-poker-agent-challenge-2026.md
