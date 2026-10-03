---
title: "PACE: provenance-aware capability enforcement for tool-using agents (2610.01349)"
type: source
tags: [source, k279, agents, security, harness]
keywords: [k279, pace, provenance, capability, FILE]
related:
  - concepts/k279-security-wave.md
maturity: draft
created: 2026-10-03
updated: 2026-10-03
read_status: skimmed
---

## Relations

- @concepts/k279-security-wave.md

## Raw Concept

| File | `arxiv-2610.01349-pace-provenance-aware-capability-enforcement-for.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.01349-pace-provenance-aware-capability-enforcement-for.pdf` |
| Archive | egress-fi 2026-10-03 |
| Retrieved | 2026-10-03 |
| sha256 | `d03ed2c8f63790a594a97795e0247e65b1bd000668bac1d9c22fd163791223e1` |
| Dual-ID | **OSINT K279** |
| arXiv | 2610.01349 |
| Authors | Fengpeng Li, Qizhou Wang, Yuke Hu, Kemou Li, Jun Liu, Haiwei Wu, Jiantao Zhou, Di Wang (KAUST PRADA Lab; RIKEN AIP; Univ. of Macau; NII; UESTC) |
| Pages | 38 |

## Narrative

The paper opens with a result that matters for every allowlist we run.

Vetting a tool or a schema **before** it runs does not settle safety. A safe variant and a leaking variant can produce **identical admission evidence**. So a sound gate cannot relax mediation for either one. Admission-time review is not a substitute for call-time enforcement.

PACE therefore mediates every tool call at the last enforceable boundary. Four phases: freeze the call and extend a provenance graph; cut a min-cut over influence paths and certify nine obligations against the capabilities compiled from the request; enforce; finalise.

### Numbers

| Setting | Result |
|---------|--------|
| Lowest attack-success rate | PACE-P lowest in 62 of 79 eligible per-group columns; tied lowest in 14; higher in 3 |
| Native utility cost | at most 2.92 points down versus undefended |
| Adaptive search, 30 attempts | **0 of 30** against PACE-P, versus **21 of 30 (70%)** undefended |
| Boundary calls blocked before dispatch | all 157 |
| One benchmark, three models | attack success dropped from 48.0/99.84/100.0 to 0.0/5.09/8.11 |

The ablation is the useful part. **Effect verification carries most of the security gain.** Boundary adaptation is what prevents indiscriminate refusal — it lowers the refusal rate on a tool-poisoning benchmark rather than raising it.

That tension is worth naming: a gate can be secure and useless if it blocks everything. The paper's answer is to enforce the boundary precisely and adapt it, not to widen it.

### The scope limits the authors state

This is a carefully bounded claim. Guarantees cover only **represented chains** — the flows the schema exposes. Paraphrase, translation, and fragmentation fall outside the re-encoding family. Model-recomposed strings, unexposed effects, tool-internal secondary calls, and unversioned writes are excluded. No noninterference claim is made; the refusal channel remains unbound. Minimality is declared, not proven, and the key premises are deployment declarations rather than automatic checks. The evaluated configuration does not retain the certified guarantee in general.

Read that list as the honest boundary of what any such gate can promise.

No public code URL; the abstract says the source is in supplemental material. No clone.
