---
title: "Twin — test-time world model (arXiv 2608.14490) — OSINT stub"
type: source
tags: [arxiv, stub, k240, ccc-k283, dual-id, game-dev]
keywords: [twin, validate-before-act, CEGIS, ARC-AGI-3]
related:
  - sources/arxiv-2608.14380-agentrewind-2026-08-17.md
  - sources/arxiv-2608.14527-fault-injection-llm-modernization-2026-08-17.md
  - concepts/agent-steering-action-boundary.md
maturity: draft
created: 2026-08-17
updated: 2026-08-17
read_status: read
---

## Relations

- Canon: CCC **K283** Twin ingest (same PDF). OSINT does not duplicate the CCC page.
- @sources/arxiv-2608.14380-agentrewind-2026-08-17.md — CCC K282 stub
- @sources/arxiv-2608.14527-fault-injection-llm-modernization-2026-08-17.md — CCC K284 stub
- @concepts/agent-steering-action-boundary.md — harness gate, not agent discretion

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.14490, Twin — playing an unknown game with a test-time world model |
| File | `arxiv-2608.14490-twin-playing-an-unknown-game-with-a-test-time-di.pdf` |
| sha256 | `ea425e1ffde0403aba56b55f1d74866b8c88c2028eaaededd36c9361de440e0c` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.14490-twin-playing-an-unknown-game-with-a-test-time-di.pdf` |
| Dual-ID | **OSINT K240** stub. **CCC K283** = canon. **CCC K240** = robotics solver (old). Poker skip (ARC/game-dev, not IIG/HU). |
| OSINT clone | `.local/adopts/TWIN-ARC-AGI-3` (MIT, 6.7MB) REFERENCE shelf |

## Narrative

OSINT stub. Game-dev cross-wiki brief preferred over a second wiki stub.

**Steal:** validate-before-act is a **harness gate**, not agent discretion. Block every scored/env action until the twin replays the full interaction log; a mismatch is a counterexample that invalidates the twin until repair (CEGIS). Fit (`∀` logged transitions) is the hard precondition; reachability is pursued only through search.

## Snippets

> Canon: CCC K283. OSINT shelf copy only. Twin is ARC-AGI-3 / game-dev, not poker IIG.
