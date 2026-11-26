---
title: "inference-optimisation-skill — measure a serving stack against its physics ceiling (MIT)"
type: entity
related:
  - "@osint-wiki/sources/2026-11-26-deep-research-batch-audit.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
updated: 2026-11-26
---

## Raw Concept

Surfaced by
@osint-wiki/sources/2026-11-26-deep-research-batch-audit.md, URL 12, **Extract** tier.
Routed to Collectibles.

The question this page answers: **is this serving configuration actually fast, or does
it only feel fast?**

## Narrative

### What it is

An MIT-licensed methodology in three layers:

1. **An agent procedure** (`SKILL.md`, `PROMPT.md`) — blocked by the Workstation
   Harness Freeze.
2. **Five playbooks** — `ceilings.md`, `methodology.md`, `levers.md`, `gotchas.md`,
   `publishing.md` — covering vLLM, SGLang, llama.cpp, ExLlamaV3, and MLX across
   NVIDIA, Apple, AMD, and Intel.
3. **A zero-dependency harness** — `scripts/bench.py` (~262 lines), `ceiling.py`,
   `queue.sh`, `mem.sh`, all Python 3 standard library plus Bash, targeting any
   OpenAI-compatible HTTP server.

Layer 3 is the extract. Layers 1 and 2 are reading.

### The measurement discipline

Four rules do the work, and all four are about rejecting false wins:

**Physics first.** Compute the bandwidth-bound decode ceiling and the compute-bound
prefill ceiling for the hardware, then measure against them. A configuration that
doubles throughput while sitting at 20% of ceiling has not been optimised; it has been
measured badly.

**Interleaved A/B.** Run control, candidate, control — not candidate then control. Take
the median of at least six trials. This defeats the ±5–10% drift that makes a single
before/after pair meaningless on a laptop that is also running a browser.

**Server-reported usage.** Take token counts from the server response, not from a local
estimate, and write them to `ledger.jsonl`. Estimated tokens hide the exact regression
the bench exists to find.

**Soak and context probes.** A long-context exact-match needle test and a full-KV
concurrent soak. Throughput that collapses when the KV cache fills is not throughput.

### Why it fits Collectibles

Collectibles reads card images through a local OpenAI-compatible server — `vlm_backend.py`
restricts local calls to `127.0.0.1`, `localhost`, and `::1`. [CONFIRMED — repository
check 2026-11-26]

There is no bench harness. Any claim that a local model is fast enough to replace a
RunPod pod is currently an impression, not a measurement. `bench.py` against the local
endpoint turns that into a number, and the ceiling comparison says whether the remaining
gap is configuration or hardware.

The stdlib-only constraint holds: the harness is Python 3 standard library and Bash.

### Phase-0, 2026-11-26

| Check | Result |
|-------|--------|
| Licence | MIT [CONFIRMED — GitHub API] |
| Maturity | 2.8k stars, created 2026-11-16, pushed 2026-11-16, 26 open issues |
| Cloud requirement | none — measures a local endpoint |
| Local gap | collectibles ships no bench harness [CONFIRMED] |

Two cautions from the report, both fair:

- The upstream speedup claims (2.1x prefill on an Intel Arc B390, 4x H200 stability) are
  hardware- and quantisation-specific and unverified here.
- `queue.sh` depends on Linux `flock`, which needs a small change on macOS.

### Status

Extract. Queued for Collectibles. Take the harness and the four rules; skip the skill
wrapper.

## Snippets

> Enforces physics-first ceilings (bandwidth-bound decode, compute-bound prefill, KV
> sizing), interleaved control -> candidate -> control A/B runs (median of >=6 trials
> defeating ±5–10% drift), and true server-reported usage token accounting.
> [Source: Cemini Multi-Wiki Batch Audit.docx, URL 12]

## Dead Ends

- **A single before/after benchmark.** Drift on a busy machine is larger than the win.
- **Estimated token counts.** They hide the regression.
- **Installing the SKILL.md wrapper.** Gate 3 blocks it, and the harness is the value.
