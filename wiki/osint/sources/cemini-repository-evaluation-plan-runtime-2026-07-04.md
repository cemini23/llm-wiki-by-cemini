---
title: "Cemini Repository Evaluation Plan.docx — runtime / Fable harness batch (2026-07-04)"
type: source
tags: [tool-evaluation, runtime, agent-harness, context-compression, k143, docx]
keywords: [obsidian-mind, headroom, free-llm-api-resources, system_prompts_leaks, deo-harness, fable5-orchestrator]
related:
  - concepts/wiki-tooling-evaluation.md
  - entities/tools/obsidian-mind.md
  - entities/tools/headroom.md
maturity: draft
read_status: read
created: 2026-07-04
updated: 2026-07-04
clusters: [wiki-tooling, agent-harness]
---

## Relations

- @concepts/wiki-tooling-evaluation.md — runtime/tooling register updated with K143 findings
- @entities/tools/obsidian-mind.md — new Phase-0 Steal-from page
- @entities/tools/headroom.md — Phase-0 refresh; Adopt reaffirmed

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Cemini Multi-Wiki Link Evaluation — RUNTIME (v9) |
| **Type** | DOCX |
| **sha256** | `1c40871e86b13127f49ac0075083c743dcb927c22030b5509494483745c630d2` |
| **URLs** | 20 GitHub/runtime/tooling URLs |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Cemini Repository Evaluation Plan.docx` |
| **Retrieved** | 2026-07-04 |
| **Read status** | read; GitHub license metadata spot-checked 2026-07-04 |

## Narrative

K143 runtime batch focused on Claude Fable 5 orchestration harnesses, context compression utilities, zero-cost LLM API routing, and agent-memory/vault tooling.

### Tier distribution after Phase-0

| Tier | Count | Notes |
|------|-------|-------|
| **Adopt** | 1 reaffirmed | `headroomlabs-ai/headroom` — existing K129 Adopt; refreshed maturity/risk evidence |
| **Steal-from** | 7 | `breferrari/obsidian-mind` downgraded from docx Adopt; plus Fable/harness references such as `deo-harness`, `fable5-orchestrator`, and related prompt/context-pack patterns |
| **Reference-only** | 5 | Free LLM API indexes and broad runtime references; no direct production ingest |
| **Reject / unavailable** | 7 | Generic primers, broad indexes, unavailable repos, and GodMode-style packages without a safe Cemini surface |

### Corrections vs docx

- `breferrari/obsidian-mind` is **not** a TipDrop/David adoption candidate. Phase-0 found a mature MIT repo, but wholesale install would duplicate OSINT's filesystem-first wiki and Obsidian layer while adding lifecycle hooks and vault-layout assumptions. Verdict: **Steal-from** manifest/QMD/hook-test patterns.
- `headroomlabs-ai/headroom` is already in the wiki from K129. Phase-0 refresh reaffirmed **Adopt** for laptop/CCC context compression, with TTL/reversibility/cache-hygiene caveats. No new brief needed unless implementing a runbook.
- `cheahjs/free-llm-api-resources` has no GitHub license metadata; keep Reference-only. `open-free-llm-api/awesome-freellm-apis` is MIT and active, but remains Steal/Reference config inspiration, not production routing.

### Routing

No `cemini-prod` scp. No David/TipDrop adoption brief from this batch. Optional CCC handoff can summarize `obsidian-mind` hook-test/QMD patterns and `headroom` CCR caveats; OSINT owns the source/entity records.

## Snippets

> "Adopt: 2 — [breferrari/obsidian-mind, headroomlabs-ai/headroom]" [Source: Cemini Repository Evaluation Plan.docx aggregate summary (retrieved 2026-07-04); revised by Phase-0 2026-07-04]

> "headroom revolutionizes token efficiency by executing localized context compression for tool outputs, logs, and files immediately before transmission to the LLM." [Source: Cemini Repository Evaluation Plan.docx URL 20 (retrieved 2026-07-04)]

## Dead Ends

- Docx TipDrop claim for `obsidian-mind` was too strong: TipDrop M4 needs OCR/OKF extraction and safe local ingest, not a wholesale multi-agent memory vault with `.claude`/`.codex`/`.gemini` hook surfaces.
