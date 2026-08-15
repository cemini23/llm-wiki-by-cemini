---
title: "WIFA — refuse intent, not form (arXiv 2608.13304, K239)"
type: source
tags: [arxiv, llm-safety, cyber, ccc, k239]
keywords: [WIFA, intent-group, wrapper, over-refusal, A-GCRT, OR-Bench]
related:
  - concepts/intent-not-form-refusal.md
  - concepts/agent-steering-action-boundary.md
  - sources/arxiv-2608.12821-hiroute-2026-08-15.md
  - sources/arxiv-2608.12654-steerbench-work-2026-08-15.md
  - concepts/skill-misevolution.md
maturity: draft
created: 2026-08-15
updated: 2026-08-15
read_status: read
---

## Relations

- @concepts/intent-not-form-refusal.md — synthesized refusal unit = intent group
- @concepts/agent-steering-action-boundary.md — over-refusal is the same error class as SteerBench hold-on-safe
- @sources/arxiv-2608.12821-hiroute-2026-08-15.md — complementary safety routing
- @sources/arxiv-2608.12654-steerbench-work-2026-08-15.md
- @concepts/skill-misevolution.md — do not auto-evolve skills; wrappers must not become the label

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.13304, "Refusing Intent, Not Form: Wrapper-Based Intent-Group Supervision for LLM Safety" |
| Author | Ping Wu, Haibo Tong, Feifei Zhao, Han Shen, Yu Shi, Yilin Zhao, Sicheng Shen, Guobin Shen, Yun Luo, Yi Zeng (BrainCog Lab, CAS / Ant Group) |
| Retrieved | 2026-08-15 |
| File | `arxiv-2608.13304-refusing-intent-not-form-wrapper-based-intent-gr.pdf` |
| sha256 | `946a4d85295a7a4fc35e35191548d3df57d503b6cbbbff7ab8fdbf7a52b19b7c` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.13304-refusing-intent-not-form-wrapper-based-intent-gr.pdf` |
| Type | cs.CL preprint, 23pp, Aug 2026 |

## Narrative

Safety-tuned models learn **surface-form shortcuts**: wrapped harmful prompts bypass the refusal, while similarly wrapped benign prompts are over-refused. WIFA (Wrapper-Based Intent-Form Augmentation) builds **matched intent groups** — the same underlying intent under many wrappers, paired with structurally matched benign counterexamples. No external teacher; no per-wrapper manual labels.

Two training routes on that data layer:

- **WIFA-Boost** — two-stage safety-first (stronger transformed-harmful refusal). Qwen SORRY-Bench mutation-average refusal 22.1 → 63.7 `[TENTATIVE]`.
- **A-GCRT** (Anchored Group-Consistent Refusal Training) — regularizes decision scores across wrappers; harmful/benign groups anchored on opposite sides of a margin. Qwen OR-Bench over-refusal 25.7% → 17.4% `[TENTATIVE]`.

Desired behavior: refuse harmful **intent** under wrapper variation; comply with benign **intent** under the same wrappers.

### Cemini steal (cyber + CCC; pairs K259/K274)

- **Policy, not a trainer.** Do not add jailbreak wrappers or WIFA datasets to the wiki.
- Skill / system-prompt gates must key off **intent + tool effect**, not phrasing ("research this exploit" vs "authorized lab recon of owned host").
- Over-refusal on wrapped benign work is the same class as SteerBench holding cleared actions — HITL should be able to **proceed** when evidence is signed.
- **No auto-evolve** of skills: misevolution + wrapper-as-label is how refusals rot.

**Brief:** folded into `../Cybersecurity wiki/briefs/2026-08-15_k239-cyber-hiroute-wifa-saif.md`.

## Snippets

> "Our goal is to refuse harmful intent under wrapper variation while preserving benign compliance under matched forms." [Source: arxiv-2608.13304 p.1]

> "Adding wrapped harmful prompts alone can therefore teach a wrapper-as-refusal shortcut." [Source: arxiv-2608.13304 p.1]
