---
title: "GitHub repositories revenue evaluation — 20 rows: dev tools, agent harnesses, local RAG, CAD, concurrency (2026-10-06)"
type: source
tags: [source, k283, eval, agent-harness, local-rag, ccc, atto, guruwatcher]
keywords: [k283, open-notebook, tester-army-e2e, agency-agents, ralph-claude-code, background-agents, hotpath-rs, keyed-lock, deepgemm, outreachr, text-to-cad]
related:
  - concepts/k283-eval-wave.md
  - concepts/active-project-research-routing.md
  - entities/tools/open-notebook.md
  - entities/tools/tester-army-e2e.md
  - entities/tools/agency-agents.md
  - entities/tools/ralph-claude-code.md
  - entities/tools/background-agents.md
  - entities/tools/keyed-lock.md
  - entities/tools/hotpath-rs.md
  - entities/tools/deepgemm.md
  - entities/tools/outreachr.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
read_status: read
---

## Relations

- @concepts/k283-eval-wave.md
- @concepts/active-project-research-routing.md
- @entities/tools/open-notebook.md

## Raw Concept

| File | `GitHub Repositories Revenue Evaluation.docx` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/GitHub Repositories Revenue Evaluation.docx` |
| Retrieved | 2026-10-06 |
| Dual-ID | **OSINT K283** |
| Batch theme | Developer tools, agent harnesses, local RAG, CAD generation, concurrency and emulation |
| Rows | 20 URLs |
| sha256 | `1035b72e2df1262b…` |

## Narrative

A 20-row eval batch. The theme mixes agent harnesses, a self-hosted local-RAG tool, a CAD generator, concurrency primitives, and several emulators. The eval ran the v10.7 prompt: every row scores `atto`, `guruwatcher` and `basgiath` overlap.

### Tier spread

| Tier | Count |
|------|-------|
| Integrate | 1 |
| Extract | 6 |
| Watch | 2 |
| Context | 6 |
| Pass | 5 |
| UNAVAILABLE | 0 |

**One Integrate GO: `lfnovo/open-notebook`.** This is the first product Integrate in four waves.

### The Integrate row

| URL | Why | Route |
|-----|-----|-------|
| `lfnovo/open-notebook` | MIT. Self-hosted multi-modal RAG with REST APIs, PDF/audio/image ingestion, and vector search over local Ollama models. A private NotebookLM alternative. Scores `atto high`, `genealogy high`, `local-abliterated-lab high` | Atto Concierge research dossiers; private family archive |

Verified 2026-10-06 with WebFetch: the repo exists, is MIT, and shows 39.9k stars. The star count agrees with the eval. `open-notebook` already has an entity page here (@entities/tools/open-notebook.md).

### The Extract rows

| URL | Technique | Route |
|-----|-----------|-------|
| `tester-army/e2e` | Hybrid agentic + deterministic test harness: an agent explores a web/iOS/Android UI once, then **replays the cached action trace** for later CI runs — no repeated LLM tokens | Atto share-portal CI (CCC pattern) |
| `msitarzewski/agency-agents` | 140+ Claude Code / Cursor agent persona definitions with explicit boundaries and success criteria | CCC; Atto engineering briefs |
| `frankbria/ralph-claude-code` | The **Ralph loop**: outer loop feeds test failures and linter output back to Claude Code until all validation passes | Atto parser fixes; CCC |
| `ColeMurray/background-agents` | Asynchronous worker structure for detached long-running agent jobs | GuruWatcher newsletter pollers |
| `pawurb/hotpath-rs` | Lightweight Rust hot-path profiler | CeminiParlays copula engine |
| `ldm0/keyed-lock` | Per-key mutex: lock distinct keys independently, not one global mutex | GuruWatcher concurrent claim ingestion |

The two GuruWatcher rows are the useful pairing: `background-agents` gives detached workers, `keyed-lock` gives per-ticker concurrency. Together they close the race-condition gap when parallel newsletter ingests touch the same watch ledger.

### The Watch rows

- `deepseek-ai/DeepGEMM` — FP8 GEMM/MoE kernels. **Blocked: needs Hopper (H100/H800) or Blackwell.** The operator laptop (Apple Silicon / RTX 4090) cannot run it. Watch until GPUs change.
- `lalalune/outreachr` — B2B lead discovery and cold-email sequencing. Watch: blocked on domain warmup, SPF/DKIM/DMARC, and deliverability risk. Not a code problem.

### What was rejected

Five Pass rows: `boykopovar/AnyPS5` (unverified PS5 binary translation — high legal risk), `morluto/rea` (undocumented CLI), `DuarteSantos8/openGym` (consumer fitness app), `maurodesouza/profile-readme-generator` (profile badges), `kunchenguid/firstmate` (terminal copilot — duplicates Claude Code). Six Context rows are reference-only (text-to-cad, jarvis, ppsspp, decky-lsfg-vk, hex-dev, fluffychat).

### License notes

- Docx claims Apache-2.0 for `tester-army/e2e`, MIT for `agency-agents` and `open-notebook`. **`open-notebook` MIT is confirmed** (WebFetch 2026-10-06).
- `hrydgard/ppsspp` is GPL-2.0-or-later and `krille-chan/fluffychat` is AGPL-3.0 — both copyleft, reference-only. **Do not vendor either.**
- All other rows show `NOT FOUND` license in the docx. Treat as unverified.

### Eval-quality warning

The docx reports `NOT FOUND` for stars / last-commit / issues on **17 of 20 rows**. Several stack strings are `CLAIMED (unverified)`. Unlike K281/K282, this batch has no confirmed 404 rate — but the metadata gaps mean per-row claims are leads, not facts. Only `open-notebook` was independently verified.

### Boundary

**Zero clones in this session (bash has no network). Nothing vendored. One product Integrate GO (`open-notebook`), human-gated.** Atto privacy perimeter applies to any Atto-side wiring: local-only inference, no client PII to cloud models, no automated write to `truth.ged`.

### Distribution

- `open-notebook` + Atto RAG → `../atto/briefs/2026-10-06_k283-open-notebook-local-rag.md`
- GuruWatcher concurrency pair → `../GuruWatcher/briefs/2026-10-06_k283-guruwatcher-concurrency.md`
- CCC harness rows (e2e, agency-agents, ralph, hex-dev) → `../Cemini claude code CCC/briefs/2026-10-06_k283-agent-harness.md`
- CeminiParlays row → `../Gambling wiki/briefs/2026-10-06_k283-hotpath-rs.md`
- 3D-printing / Game-dev CAD + emulator rows → `../3d printing/briefs/2026-10-06_k283-cad-emulation.md`
- Cybersec rows (DeepGEMM, fluffychat) → wiki-only, no brief.

## Snippets

> "Deploying this self-hosted stack locally allows Atto Concierge operators to query thousands of pages of archival evidence securely without leaking client PII to third-party cloud models." [Source: GitHub Repositories Revenue Evaluation.docx]

> "The repository provides a caching layer that executes AI agent browser workflows once and replays them deterministically for subsequent CI runs, eliminating token overhead on UI testing." [Source: GitHub Repositories Revenue Evaluation.docx]

> "Applying keyed locks per ticker or watch ID prevents race conditions when updating ledger records while allowing high-throughput concurrent reconciliation." [Source: GitHub Repositories Revenue Evaluation.docx]

> "These custom kernels require NVIDIA Hopper (H100/H800) or Blackwell hardware architectures, rendering them unusable on typical operator consumer hardware." [Source: GitHub Repositories Revenue Evaluation.docx]
