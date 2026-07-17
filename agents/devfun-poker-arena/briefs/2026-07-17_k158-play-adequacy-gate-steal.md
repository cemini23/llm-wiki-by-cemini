---
title: K158 — play-adequacy ship gates (poker sandbox)
type: brief
target: Poker Arena
created: 2026-07-17
updated: 2026-07-17
---

## Target

`agents/devfun-poker-arena/` — HL preflight / sandbox eval / opponent sims.

## Summary

arXiv 2607.14169: a world model (or sim) that passes **transition-accuracy** sampling can still lose at play when the omitted rule is rare under random trajectories but pivotal under competent search. Steal **play-adequacy gates** and the danger law for Arena ship checks.

## Body

### P0 — play-adequacy over transition accuracy

- Do not treat "matches hand log / transition accuracy 1.0" alone as ship criteria.
- Prefer: regression spots on **search-visited / competent-play** distributions + head-to-head play vs known baselines.
- Rare pivotal leaks (blinds, ICM cliffs, specific board textures) need **adversarial or targeted** samples — random gates miss them with probability `(1−rarity)^N`.

### P1 — specification over more examples

- If a rule is omitted from the coded heuristic/spec, more trajectory dumps won't teach it (paper: translation ≠ inference).
- Fix by completing the decide()/spot checklist, not by flooding the analyzer with similar hands.

### P2 — imperfect-info belief coverage

- When modeling opponent beliefs / info-set inference, verify coverage of the **competent-relevant** info-set subset — Kuhn-sized games may be covered; Leduc-scale need explicit bounds.

### Out of scope

- Shipping CWM+MCTS as runtime decide()
- Vendoring code while LICENSE TBD
- Full multi-model synthesis API burns

### Operator checklist

- [ ] Audit preflight: which gates are transition/match vs play/search
- [ ] Add ≥1 pivotal rare-spot fixture that random logs rarely hit
- [ ] Revisit when `code-world-models` adds SPDX

## Sources

- arXiv 2607.14169
- Gambling wiki entity: `entities/tools/code-world-models.md`
- Gambling wiki source: `sources/arxiv-2607.14169-play-adequacy-code-world-models-2026-07-17.md`
  (plain paths because `skill_audit` does not resolve cross-wiki aliases)
