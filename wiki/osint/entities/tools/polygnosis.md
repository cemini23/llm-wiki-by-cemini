---
title: PolyGnosis 2.0 — PM anomaly + GDELT perspective-mismatch harness
type: entity
tags: [tool, reference-only, polymarket, gdelt, agent-harness, arxiv, k93-adjacent]
keywords: [polygnosis, perspective-mismatch, gdelt, polymarket-alerts, research-harness]
related:
  - sources/polygnosis-2-polymarket-osint-2026-06-01.md
  - entities/platforms/polymarket.md
  - entities/data-sources/gdelt.md
  - entities/tools/polymarket-websocket-api.md
  - entities/tools/polymarket-agents.md
  - entities/tools/revfactory-harness.md
  - concepts/polymarket-bot-architecture.md
  - concepts/polymarket-wallet-alpha-pipeline.md
  - concepts/sports-prediction-consensus-agent.md
  - "@gambling-wiki/sources/polygnosis-2-polymarket-osint-2026-06-01.md"
  - "@gambling-wiki/concepts/pm-perspective-mismatch-trading.md"
maturity: draft
created: 2026-06-01
updated: 2026-06-01
phase_0_verdict: REFERENCE 2026-06-01 — arxiv harness; no public repo; map to existing PM WebSocket + GDELT + conductor; retail narrative on gambling-wiki
adoption_status: STUB-ONLY
---

## Relations

- @sources/polygnosis-2-polymarket-osint-2026-06-01.md — arxiv 2605.25958 deep-read
- @entities/data-sources/gdelt.md — media leg of mismatch score
- @entities/tools/polymarket-websocket-api.md — alert ingress
- @gambling-wiki/concepts/pm-perspective-mismatch-trading.md — consumer definition of mismatch

## Raw Concept

- **Paper:** [arxiv:2605.25958](https://arxiv.org/abs/2605.25958) (2026)
- **License / repo:** No adoptable open-source release identified at stub time — **reference architecture only**
- **Prompted by:** `@gambling-wiki` daily digest PolyGnosis ingest + federated routing rule (prod harness → osint-wiki)

## Narrative

PolyGnosis 2.0 is a **multi-agent research harness** that turns Polymarket **anomaly alerts** into GDELT-backed **Perspective Mismatch** scores (PM vs global media narrative). It is **not** a sportsbook odds tool and **not** a drop-in Cemini executor.

### Phase-0 (2026-06-01)

| Check | Result |
|-------|--------|
| Public repo / license | **None found** — cannot Adopt code |
| Overlap with stack | **High** — WebSocket PM + GDELT already in Cemini architecture |
| Latency | GDELT harvest ≠ tick-level PM — research tier, not HFT |
| Retail wagering | Routed to `@gambling-wiki` — discipline + pairing with StakeBench / line divergence |

**Verdict: REFERENCE** — reuse **patterns** (partitioned agents, no unconstrained reflection) when building PM OSINT playbooks; wire alerts through existing `@entities/tools/polymarket-websocket-api.md` and GDELT paths before any new package.

### Proposed Cemini shape (prescriptive stub)

```
PM WebSocket / whale alert
  → event cluster (batch job or conductor sub-agent)
  → GDELT keyword query (@entities/data-sources/gdelt.md)
  → mismatch scorer (structured JSON; no terminal reflection loop)
  → human or brain review → optional trade via polymarket-agents
```

Do **not** duplicate implementation notes on `@gambling-wiki/entities/tools/` — cross-link only.

## Snippets

> "REFERENCE for alert→OSINT research workflows." [Source: @sources/polygnosis-2-polymarket-osint-2026-06-01.md Phase-0 table]

## Dead Ends

- Treating mismatch score as Kalshi sports +EV without separate fee/CLV model
- Expecting arxiv PDF to include production API keys or CLOB signing
