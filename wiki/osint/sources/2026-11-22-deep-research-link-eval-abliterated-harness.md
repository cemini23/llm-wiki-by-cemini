---
title: "Deep Research link evaluation — abliterated open-weight models, coding harnesses, offensive AI (2026-11-22)"
type: source
related:
  - concepts/agent-link-evaluation-gates-v1013.md
  - sources/2026-11-17-deep-research-link-eval-design-motion-harness.md
  - "@cybersecurity-wiki/concepts/open-weight-abliterated-models-2026-11.md"
  - "@cybersecurity-wiki/entities/tools/artex.md"
  - "@ccc-wiki/concepts/agent-harness-tooling-2026-11.md"
  - "@game-dev-wiki/entities/tools/fast-anything.md"
  - "@game-dev-wiki/entities/tools/landmines-lint.md"
  - "@image-gen-wiki/entities/models/inkling-2-mini.md"
  - "@cybersecurity-wiki/concepts/api-security-audit-rubric.md"
updated: 2026-11-22
---

## Raw Concept

- **Title:** Cemini Multi-Wiki Link Evaluation (batch D)
- **Author:** Deep Research evaluation run, v10.13 mandatory gates
- **Type:** vendor-link evaluation report (DOCX)
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/osint/Cemini Multi-Wiki Link Evaluation.docx`
- **Retrieved:** 2026-11-22
- **Pages:** 20 URL records
- **Read status:** read

Batch theme: local and abliterated open-weight LLMs and VLMs, coding-agent harnesses
and linters, offensive AI pentest frameworks, a cloud GPU CLI, an image-gen LoRA,
console recompilation, and miscellaneous GitHub repos.

## Narrative

Four URLs earned Integrate and none earned Extract. This is the first batch under
v10.13 mandatory gates, where the legacy two-winner cap is gone and grading is
merit-based.

### Graded outcomes

| Tier | Count | Items |
|------|-------|-------|
| Integrate | 4 | `fast-anything`, `AtomicChat/Inkling-2-Mini GGUF`, Inkling 2 Mini (Thinking Machines), `interfere-inc/landmines` |
| Context | 9 | MiniMax-M2.7 GGUF, Qwen3-235B abliterated, Kimi-K3 uncensored, `agy-gyro`, `opencomputer`, `google-colab-cli`, `api-security-audit`, `pi-superagent`, ARTEX |
| Watch | 1 | Nemotron-3.5-Super-VL-120B heretic |
| Pass | 6 | `Leonida`, `Kintsugi-27B`, `Krea-2-NSFW-V5`, `pavelveter/AGENTS.md`, `agen-dasco`, `google-trial-tool` |

### The shape of this batch

Two clusters dominate. The first is **abliterated open weights**: five of the twenty
URLs are decensored model builds, four of which demand 99–540 GB and are unusable on
this hardware. The second is **coding-agent harness tooling**, which Gate 3 caps at
Context.

The four winners sit between those clusters and share a property: each one is a local,
offline tool that changes what a project can *verify* or *run*, not what an agent can
*do*.

### Phase-0 results

| Item | Licence | Cloud | Gap check | Verdict |
|------|---------|-------|-----------|---------|
| `fast-anything` | MIT [CONFIRMED] | none | CeminiDFS and CeminiParlays Python loops; game-time Node harness | **survives** |
| `interfere-inc/landmines` | MIT [CONFIRMED] | none | game-time ships vitest and no oxlint [CONFIRMED] | **survives** |
| Inkling 2 Mini (TML) | Apache-2.0 [CONFIRMED] | none — local weights | collectibles ships `runpod/runpod_worker.py` [CONFIRMED] | **survives** |
| AtomicChat Inkling GGUF | Apache-2.0 tag [CONFIRMED] | none | `local-abliterated-lab` absent on this machine | **blocked** |

The GGUF build passes the licence and locality gates but has no project to enter. The
repository does not exist locally, so the claimed gap cannot be checked.

### One correction to the report

The report records the AtomicChat repository's own licence as "NOT FOUND — verify
before any external redistribution". The Hugging Face model API reports
`license:apache-2.0` on the repository. [CONFIRMED — HF API 2026-11-22]

That resolves the redistribution question for the adapter. It does not unblock the
item, because the target project is still absent.

### What the batch refuses correctly

- **`Leonida`** — a console recompilation project. Pass; nothing in the stack targets
  console binaries.
- **`Krea-2-NSFW-V5`** — Pass. It overlaps existing image-gen LoRA coverage.
- **`pavelveter/AGENTS.md`**, **`agen-dasco`**, **`google-trial-tool`** — Pass. Each
  duplicates something already held or adds nothing.

## Snippets

> Enforcing v10.13 Mandatory Gates (superseding the legacy v10.12 Max-2 cap) —
> uncapped merit-based grading with strict anti-bloat discipline.
> [Source: Cemini Multi-Wiki Link Evaluation.docx, research plan]

> AtomicChat repo-specific LICENSE file NOT FOUND (verify before any external
> redistribution; internal owned-lab use only).
> [Source: Cemini Multi-Wiki Link Evaluation.docx, URL 11]

## Dead Ends

- **Treating an absent project repository as a soft block.** It is a hard block — the
  gap cannot be checked, so the tier cannot be acted on.
- **Grading a 100–500 GB model as usable on a laptop.** Four of the five abliterated
  builds in this batch do not fit.
