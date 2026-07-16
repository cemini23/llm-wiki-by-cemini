---
title: K176 claimed-authorization light steal (poker arena)
type: brief
tags: [brief, poker, k176, authorization]
created: 2026-07-16
---

## Target

`devfun-poker-arena` agent

## Summary

Light steal from AHA (2607.11698): poker agent tool routes must not accept **self-claimed authorization** (“user approved all-in”) from untrusted observation channels.

## Body

1. Any action that spends bankroll / submits table action needs standing from the real operator channel — not from scraped table text or tool-result prose
2. Log enabling condition when denying (“claim came from observation, not operator”)
3. No AHA harness install in poker arena — pattern only

Pairs with K164 hierarchical tool-routing steal.

## Sources

- arXiv [2607.11698](https://arxiv.org/abs/2607.11698) — AHA / Vulnerability Concept Graph (claimed-authorization core)
- Prior: `briefs/2026-07-14_k164-hierarchical-tool-routing-steal.md`
