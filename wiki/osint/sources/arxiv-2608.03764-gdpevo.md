---
title: "arXiv 2608.03764 — GDPevo agent self-evolution benchmark"
type: source
tags: [arxiv, agents, ccc, atto, k223]
keywords: [GDPevo, rule hybridization, PrismShadow, self-evolution]
related:
  - entities/tools/gdpevo.md
  - concepts/llm-agent-failure-telemetry-monitors.md
  - sources/arxiv-2608.02287-skt-skill-use-training.md
  - concepts/gpuology-genealogy-agent-kit.md
maturity: draft
created: 2026-08-05
updated: 2026-08-05
read_status: deep-read
---

## Relations

- @entities/tools/gdpevo.md
- @concepts/llm-agent-failure-telemetry-monitors.md
- @sources/arxiv-2608.02287-skt-skill-use-training.md
- @concepts/gpuology-genealogy-agent-kit.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | GDPevo: Evaluating Agent Self-Evolution on Real Business Tasks |
| arXiv | 2608.03764 |
| Code | https://github.com/Prism-Shadow/GDPevo (Apache-2.0) |
| sha256 | `06d5391e998206251e50a1234fe9a622cc10b19fbce0b18be5ce8044a96f61f5` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.03764-gdpevo-evaluating-agent-self-evolution-on-real-b.pdf` |
| read_status | deep-read |

## Narrative

Evolution-native benchmark on GDP-like enterprise workflows (CRM/ERP/finance/legal/…). **Rule hybridization** splits atomic business rules across train tasks and recombines on held-out tests so gains are attributable (anti-contamination). V1: 120 tasks / 12 groups. Self-evolution +16.44 pp held-out; still far below 91.6% oracle.

**CCC/Atto:** clone `.local/adopts/GDPevo` (~76MB) REFERENCE for harness eval — no Barone PII in tasks; not a product trainer.
