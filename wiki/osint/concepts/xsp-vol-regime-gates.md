---
title: XSP Vol-Regime Gates
type: concept
tags: [concept, xsp, options, vol-regime, k233]
keywords: [xsp, vol-regime, green-playbook, entry-gate]
related:
  - sources/arxiv-2608.10693-fed-speaks-vol-surface-2026-08-12.md
  - concepts/xsp-lane-trading-framework.md
  - concepts/fomc-iv-surface-dynamics.md
  - concepts/high-iv-collar-shopping.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
---

## Relations

- @concepts/xsp-lane-trading-framework.md
- @concepts/fomc-iv-surface-dynamics.md
- @sources/arxiv-2608.10693-fed-speaks-vol-surface-2026-08-12.md
- @concepts/high-iv-collar-shopping.md — high-IV financed hedges (K234)

## Raw Concept

What this page answers: the regime-conditioning gates that gate XSP/killer-bot long-call entries (GREEN playbook_snapshot and similar).

## Narrative

Vol-regime gates condition XSP lane entries on the prevailing vol regime. K233 refines this: the FOMC pre-announcement IV elevation is **stronger in high-vol regimes**, so the regime gate and the FOMC calendar interact — high-vol regime + approaching FOMC favors earlier long-call entry to capture the IV bid-up. See `@concepts/fomc-iv-surface-dynamics.md` and `@concepts/xsp-lane-trading-framework.md`.

[Source: arXiv:2608.10693; workspace XSP framework]
