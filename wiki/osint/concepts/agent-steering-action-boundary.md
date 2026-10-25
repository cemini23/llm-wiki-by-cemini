---
title: "Agent steering at the action boundary — proceed vs hold (K239)"
type: concept
tags: [concept, hitl, agent-safety, ccc, k239]
keywords: [SteerBench, proceed, hold, over-refusal, under-refusal, HITL, dual-id]
related:
  - sources/arxiv-2608.12654-steerbench-work-2026-08-15.md
  - sources/arxiv-2608.13304-wifa-intent-not-form-2026-08-15.md
  - sources/arxiv-2608.12821-hiroute-2026-08-15.md
  - sources/substack-rss-addy-osmani-2026-08-14-practical-loop-engineering.md
  - sources/newsletter-rss-latent-space-2026-08-15-react-for-agents-flue.md
  - sources/substack-rss-secpro-2026-08-14-247-google-saif.md
  - concepts/practical-loop-engineering.md
  - concepts/intent-not-form-refusal.md
  - sources/arxiv-2608.14380-agentrewind-2026-08-17.md
  - sources/arxiv-2608.14490-twin-2026-08-17.md
  - concepts/trading-strategy-autopsy-loop.md
maturity: draft
created: 2026-08-15
updated: 2026-10-25
---

## Relations

- @sources/arxiv-2608.12654-steerbench-work-2026-08-15.md — 106-scenario benchmark
- @sources/arxiv-2608.13304-wifa-intent-not-form-2026-08-15.md — over-refusal on wrapped benign
- @sources/arxiv-2608.12821-hiroute-2026-08-15.md — routed vs global safety
- @sources/substack-rss-addy-osmani-2026-08-14-practical-loop-engineering.md — don't delegate judgment
- @sources/newsletter-rss-latent-space-2026-08-15-react-for-agents-flue.md — dynamic tools still need a gate
- @sources/substack-rss-secpro-2026-08-14-247-google-saif.md — HITL on high-impact agent tools
- @concepts/practical-loop-engineering.md
- @concepts/intent-not-form-refusal.md
- @sources/arxiv-2608.14380-agentrewind-2026-08-17.md — K240/CCC K282 stub: resume-from-checkpoint
- @sources/arxiv-2608.14490-twin-2026-08-17.md — K240/CCC K283 stub: validate-before-act

## Raw Concept

What this page answers: when should an agent **proceed** with a state-changing tool call vs **hold** for a human? Synthesized from SteerBench-Work (2608.12654) plus Osmani/SAIF/Flue.

## Narrative

The action boundary is the last steerable moment. After commit (merge, `scp` to prod, Discord LIVE, rewrite `watches.json`, auto-evolve a skill), the consequence is in the world.

SteerBench-Work scores that binary. Headline `[TENTATIVE]`: models **over-refuse** authorized work (~28%) far more than they **under-refuse** unsafe work (~1%). Famous-incident priors beat evidence-reversed mirrors (98.5% vs 63.8%). Capability does not calibrate the gate.

### Operating rule (OSINT / CCC)

| Action class | Default |
|--------------|---------|
| Read-only wiki/query | proceed |
| Local non-secret write (wiki page, brief) | proceed with lint |
| Prod `scp` of `xsp-*`/`pm-*` | hold — skill_audit + operator |
| Discord LIVE, order placement, watch-file clobber | hold |
| `.cursor/skills/*` evolution | **hold always** this batch |
| AGPL/GPL vendor into Atto | hold / refuse |

**Dual-ID:** OSINT **K239** = this SteerBench/HITL wire. CCC **K239** = Datumpont / execution-fidelity. Resolve by file+wiki, not bare K#.

Do not auto-loosen the gate because a bigger model arrived.
