---
title: "Tool eval — Multi-Wiki Repository Link Evaluation (20 URLs, 2026-10-16)"
type: source
tags: [eval, tool-evaluation, licence-verification, phase-0, k292]
keywords: [tool eval, licence NOT FOUND, leantoken, flameox, jacobian, smokinggun, xerj, parallel-cc, Cap, Ultramarine, tier]
related:
  - concepts/k292-osint-wave.md
  - entities/tools/leantoken.md
  - entities/tools/flameox.md
  - entities/tools/jacobian.md
  - entities/tools/smokinggun.md
  - entities/tools/xerj.md
  - entities/tools/parallel-cc.md
  - entities/tools/cap-screen-recorder.md
  - concepts/tool-evaluation-framework.md
  - sources/eval-url-multi-wiki-link-2026-10-14.md
maturity: draft
read_status: read
created: 2026-10-16
updated: 2026-10-16
---

## Relations

- @concepts/k292-osint-wave.md — K292 osint wave hub
- @entities/tools/leantoken.md
- @entities/tools/flameox.md
- @entities/tools/jacobian.md
- @entities/tools/smokinggun.md
- @entities/tools/xerj.md
- @entities/tools/parallel-cc.md
- @entities/tools/cap-screen-recorder.md
- @concepts/tool-evaluation-framework.md
- @sources/eval-url-multi-wiki-link-2026-10-14.md — the previous batch of this docx type

## Raw Concept

Title: Multi-Wiki Repository Link Evaluation
Type: Tool evaluation docx, 20 URLs
Batch theme (as written): "Agentic knowledge-work harnesses and non-verifiable reinforcement learning (Ultramarine / Feather), token-bounded code intelligence, symbolic mathematics, and runtime profiling MCP servers (morluto, N0zoM1z0, xerj), parallel Claude Code worktree orchestration (frankbria), open-source screen capture (Cap), high-throughput LLM inference (TokenSpeed), and vertical RAG/analytics applications"
Location: `cemini-egress-fi:/opt/cemini-bulk/research/osint/Multi-Wiki Repository Link Evaluation.docx`
Retrieved: 2026-10-16
sha256: `b3e0599ad3890ae9…`
Read status: read

## Narrative

**Docx tiers: Integrate 2 · Extract 6 · Watch 1 · Context 5 · Pass 6 · UNAVAILABLE 0.**

This batch is **not a duplicate** of the K291 docx of the same family — no repository overlaps.

### The finding: both Integrate rows sit on an unresolved licence

| Repo | Tier | Licence the docx claims | Claimed payoff |
|---|---|---|---|
| `morluto/leantoken` | **Integrate** | **NOT FOUND** | 20.1-37.6% input-token reduction |
| `morluto/flameox` | **Integrate** | **NOT FOUND** | performance-engineering loop |

The docx tiers both at its top level, at "high, now" revenue priority, **while recording the licence as not found**. Its own implementation-friction section says the rule out loud: *"morluto/jacobian, morluto/leantoken, and morluto/flameox have unverified root SPDX strings … (verify before commercial redistribution)."* **An Integrate decision was being made on a licence nobody had read.** This is the same defect class as the previous four waves in a sharper form: not a wrong SPDX claim, but a missing one treated as harmless.

**Phase-0 then read all ten. The licences are fine, and the tiers hold.** `leantoken` is **Apache-2.0** and `flameox` is **MIT** — both permissive, both correct as Integrate. `jacobian` is **MIT** where the docx also said NOT FOUND. So **the defect is procedural, not a wrong decision**: the eval reached a defensible tier without doing the check that would justify it, and the same method on a copyleft repo would have shipped a silent licence problem. **Six of the ten `NOT FOUND` or mismatched claims resolve permissive.** The one that does not is `Cap`, which GitHub reports as **NOASSERTION** for its AGPL-3.0 plus MIT split — the docx read that one correctly.

`Extract` tier has the same problem in `morluto/jacobian` (symbolic-math MCP over SymPy, NetworkX, Z3 and FLINT — needs Python) and partly in Ultramarine, where the tier is Extract but the core API is proprietary and only the helper libraries are open.

### The 20 entries

| # | Repo | What it does | Licence claimed | Tier |
|---|---|---|---|---|
| 1 | paperinstruments.com (Ultramarine 1 Flash) | GLM-5.3-Flash post-trained with non-verifiable RL; "Feather" Python harness | NOT FOUND (API proprietary) | Extract |
| 2 | `xerj-org/xerj` | Rust local Elasticsearch-compatible passage indexer for code/PDF/logs | Apache-2.0 | Extract |
| 3 | `lightseekorg/tokenspeed` | C++/Python high-throughput LLM inference | MIT | Watch |
| 4 | `richiemcilroy/Tov` | TypeScript-subset → native compiler | MIT (vendored BoringSSL, brotli, zstd) | Context |
| 5 | `CapSoftware/Cap` | Open-source screen recorder, local captioning, BYO-S3 | **AGPL-3.0** + MIT parts; commercial desktop licence separate | Extract |
| 6 | `richiemcilroy/chippytea` | macOS disk-cleanup menu-bar app | MIT | Pass |
| 7 | `frankbria/auto-author` | Q&A-guided book authoring | MIT | Context |
| 8 | `frankbria/auto-modeler-evolve` | Claude-driven autonomous code-evolve experiment | NOT FOUND | Pass |
| 9 | `frankbria/sprintforge` | Monte Carlo agile sprint forecasting | NOT FOUND | Pass |
| 10 | `frankbria/parallel-cc` | **Git-worktree isolation for concurrent Claude Code sessions** | MIT | Extract |
| 11 | `frankbria/codeframe` | Multi-agent coding wrapper | NOT FOUND | Context |
| 12 | `N0zoM1z0/vocaloid-mcp` | MCP server for VOCALOID singing-synth projects | NOT FOUND | Pass |
| 13 | `N0zoM1z0/th08` | C++ source reconstruction of Touhou 8 | NOT FOUND | Context |
| 14 | `N0zoM1z0/th095` | Touhou 9.5 reconstruction + **hash-attested byte-comparison harness** | NOT FOUND | Context |
| 15 | `MakazhanAlpamys/Kaspi-Analytics-Platform` | Kazakh marketplace analytics dashboard | NOT FOUND | Pass |
| 16 | `MakazhanAlpamys/Permit-Forge` | Dubai building-code RAG chatbot | NOT FOUND | Pass |
| 17 | `morluto/jacobian` | Symbolic-math MCP (SymPy/NetworkX/Z3/FLINT) | NOT FOUND | Extract |
| 18 | `morluto/leantoken` | Token-bounded code-intelligence MCP, hash-receipt dedup | NOT FOUND | **Integrate** |
| 19 | `morluto/smokinggun` | Static complexity scanner + agent skill (SARIF/pprof) | MIT | Extract |
| 20 | `morluto/flameox` | Runtime profiler / GPU-trace MCP server | NOT FOUND | **Integrate** |

### The on-topic core is small

Genuinely relevant: the **morluto MCP cluster** (#17-20), `xerj` (#2, token reduction for code and PDF retrieval), `parallel-cc` (#10, worktree isolation — directly applicable to how this workspace runs concurrent sessions), `Cap` (#5, AGPL friction noted correctly), and **Ultramarine's Feather harness** (#1, non-verifiable RL for document generation).

Off-topic for this wiki: `vocaloid-mcp` (music synthesis, self-described "just for fun"), `th08` and `th095` (Touhou game reconstruction — only the verification technique travels), `Permit-Forge` (Dubai building code), `chippytea` (macOS cache cleaner), `Kaspi-Analytics-Platform` (Kazakh retail).

**One technique worth naming:** `th095`'s **hash-attested byte-comparison harness** is a reconstruction-verification pattern — decompose, reconstruct, and prove equivalence by hash against the original. It echoes the K290 VEPA shape: deterministic evidence before any model judgement.

### Phase-0 status — RUN 2026-10-16

`bash scripts/adopt_k292_phase0.sh` ran in the Terminal panel. **All ten licences were read with `gh api` before any clone**, and **7 shallow clones landed** in `.local/adopts/k292/` (gitignored).

| Repo | Docx licence | **`gh api` reading** | Tier |
|------|--------------|----------------------|------|
| `morluto/leantoken` | NOT FOUND | **Apache-2.0** | Integrate |
| `morluto/flameox` | NOT FOUND | **MIT** | Integrate |
| `morluto/jacobian` | NOT FOUND | **MIT** | Extract |
| `morluto/smokinggun` | MIT | MIT | Extract |
| `xerj-org/xerj` | Apache-2.0 | Apache-2.0 | Extract |
| `frankbria/parallel-cc` | MIT | MIT | Extract |
| `CapSoftware/Cap` | AGPL-3.0 | **NOASSERTION** (AGPL-3.0 + MIT split) | Extract |
| `lightseekorg/tokenspeed` | MIT | MIT | Watch |
| `richiemcilroy/Tov` | MIT | MIT | Context |
| `frankbria/auto-author` | MIT | MIT | Context |

**Clone footprint 745,404 KB against a 500,000 KB budget — over by 50%.** `xerj` (275 MB) and `Cap` (324 MB) dominate; the budget was set before those two were sized. **Pruning is the operator's call** — the clones are REFERENCE data, not installs.

**Nothing became an install.** The clones are read-only reference under a gitignored path, and **0 Integrate GO** still stands: adopting any of them into a product needs its own brief.

## Snippets

> morluto/jacobian, morluto/leantoken, and morluto/flameox have unverified root SPDX strings … (verify before commercial redistribution) [Source: Multi-Wiki Repository Link Evaluation.docx, implementation friction]

> Integrate 2, Extract 6, Watch 1, Context 5, Pass 6, UNAVAILABLE 0 [Source: Multi-Wiki Repository Link Evaluation.docx, aggregate summary]
