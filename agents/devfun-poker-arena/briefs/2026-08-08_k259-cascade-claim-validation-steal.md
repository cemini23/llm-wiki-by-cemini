---
title: CCC→Poker K259 — MCP claim validation + parameter grounding
type: brief
tags: [brief, poker, k259]
created: 2026-08-08
---

## Target

Poker Arena

## Summary

Light steal from CASCADE (bio OOD): when Arena helpers surface solver/tool reports, validate the claim those reports repeat; harden NL→tool arg grounding.

## Regime disclosure

Paper metrics are not poker EV.

## Steal

1. Solver/helper reports: membership ("looks like a known line") ≠ validating the directional claim the agent will repeat.
2. Ambiguous tool args (seat, street, solver id): clarify/refuse — do not silent-default.
3. Prefer server-side alias maps for informal names over trusting model strings.

## Skip

CASCADE install / cancer genomics runtime.

## Sources

- CCC wiki `concepts/mcp-claim-validation-and-parameter-grounding.md` (federation K259 policy wire)
- `@concepts/judgment-consequence-gap-agent-ethics.md` — related HITL / no silent-default (K227)
