---

title: "omlx (Apple Silicon local LLM)"
type: entity
tags: [entity, tool, k182, integrate]
keywords: [omlx, apache-2-0, k182]
related:
  - concepts/polymarket-bot-architecture.md
  - sources/eval-revenue-opportunity-analysis-2026-07-25.md
  - concepts/gpuology-genealogy-agent-kit.md
  - concepts/wiki-tooling-evaluation.md
  - sources/eval-url-revenue-opportunity-analysis-2026-07-22.md
  - sources/eval-local-agent-infra-2026-08-19.md
  - entities/tools/decision-3-0.md
maturity: draft
created: 2026-07-22
updated: 2026-08-19
harness_verb: FILE
wire_note: local LLM stack REFERENCE; no runtime wire
---

## Relations

- @concepts/polymarket-bot-architecture.md — K195 PM local shadow
- @entities/tools/decision-3-0.md

- @sources/eval-revenue-opportunity-analysis-2026-07-25.md — K195 Extract refresh

- @concepts/gpuology-genealogy-agent-kit.md — Atto local LLM candidate

- @concepts/wiki-tooling-evaluation.md

- @sources/eval-url-revenue-opportunity-analysis-2026-07-22.md — K182 eval
- @sources/eval-local-agent-infra-2026-08-19.md — K242 Extract refresh; skip clone; keep `wont_wire`

## Raw Concept

Phase-0 K182 Integrate. Repo: https://github.com/jundot/omlx

## Narrative

| Field | Value |
|-------|-------|
| **License** | Apache-2.0 `[CONFIRMED]` |
| **Tier** | Integrate |
| **Local** | `.local/adopts/omlx` |
| **Note** | Atto local inference; no HF weight fetch this session |


## K195 note

Eval reaffirms Extract for PM canary / Atto local shadow — keep `.local/adopts/omlx`; no new weight downloads.
