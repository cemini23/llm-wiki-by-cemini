---
title: K191 — Agreement blindness + programmatic memory light steal
type: brief
target: poker-arena
created: 2026-07-23
updated: 2026-07-23
---

## Target

dev.fun Poker Arena — researcher sandbox.

## Summary

Multi-agent agreement is not safety (ARAT). Long HU trajectories need queryable logs (PRO-LONG), not summary-only memory.

## Body

1. Do not treat ensemble/consensus decide() as validation — keep claimed-auth + pin gates.
2. Prefer structured trajectory logs searchable for HL brief / TrueSkill postmortems.
3. Light steal only — no new training run this brief.

## Sources

- osint-wiki: arxiv-2607.19899, arxiv-2607.20064; concepts code-as-agent-harness
