---
title: "fast-anything — profile, port, and prove parity for hot functions (MIT)"
type: entity
related:
  - "@osint-wiki/sources/2026-11-22-deep-research-link-eval-abliterated-harness.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
  - "@ccc-wiki/concepts/agent-verification-patterns.md"
updated: 2026-11-22
maturity: draft
---

## Raw Concept

Surfaced by
@osint-wiki/sources/2026-11-22-deep-research-link-eval-abliterated-harness.md, URL 8,
**Integrate** tier. Routed to game-time, CeminiDFS, and CeminiParlays.

The question this page answers: **how do you move a hot function to Rust without
silently changing its numbers?**

## Narrative

### What it does

A local CLI that automates the whole port:

1. **`scan`** — finds hot functions by profiling a real run.
2. **`port`** — records up to 500 real calls as fixtures, then scaffolds a
   single-function Rust crate.
3. **`verify`** — replays the captured calls and asserts exact behavioural parity.
4. **`bench`** — interleaved before/after runs, so cache state does not favour either.
5. **Kill switch** — `FAST_ANYTHING_DISABLE=1` removes the ported path in one block.

Targets: Python 3.10+ via PyO3, Node 22+/Bun/Deno 2+ via napi-rs, plus Ruby, Java,
Kotlin, Go, PHP, C/C++, and C#.

### The parity check is the product

Everything except `verify` is scaffolding. `verify` is why this is worth using:

- floats within **1e-9**
- `NaN`, `±inf`, `-0.0`, zero, `±1`
- non-ASCII input
- inputs larger and smaller than any captured call

A hand-written PyO3 binding that "looks right" can drift on `-0.0` or on an empty
input, and a simulation will not notice for weeks. Captured real calls plus edge cases
is the differential-oracle pattern described in
@ccc-wiki/concepts/agent-verification-patterns.md, applied to a port instead of a
refactor.

### Where it fits

**CeminiDFS** — contest and ownership simulations are Python loops. A PyO3 port of the
inner loop raises simulation volume before lock, which is the input to sharper contest
selection.

**CeminiParlays** — the copula EV ranker converges in Python. Faster convergence means
more candidate slips evaluated.

**game-time** — the offline Node balancing harness. A napi-rs port speeds iteration on
economy and raid tuning.

### Where it does not fit

**Collectibles** is Python 3.12 stdlib-only by hard rule. Bringing in a Rust extension
breaks that constraint for a project that does not need the throughput.

### Phase-0, 2026-11-22

| Check | Result |
|-------|--------|
| Licence | MIT [CONFIRMED — GitHub API] |
| Maturity | 1.7k stars, pushed the day of the check, 5 open issues |
| Cloud requirement | none — local Rust and Node toolchains |
| Local gap | Python hot loops in CeminiDFS and CeminiParlays; Node batch runners in game-time |

An agent can port a function itself. What it cannot do reliably is prove the port is
numerically identical — which is the failure this tool closes.

### Status

**SHIPPED — game-time `298c8a1` (2026-11-24), on top of `ee02e58`.** All three balancing
loops have a native batch call. Parity holds on **8,127 real cases at zero difference**
(`maxAbsDiff=0`).

**The speedups are not uniform, and two of three lost.** Recorded so the losing defaults
are never re-attempted:

| Loop | TypeScript | Rust | Speedup | Backend |
|------|-----------|------|---------|---------|
| Economy | 178.16 ms | 92.80 ms | **1.92x** | native (default) |
| Raid | 0.213 ms | 4.277 ms | **0.050x** | TypeScript, flag-gated |
| AI | 116.70 ms | 143.01 ms | **0.816x** | TypeScript, flag-gated |

`BALANCE_NATIVE_BY_LOOP` promotes a loop to native only at **speedup >= 1.10**, and the
compare bench fails when the recorded default and the measured decision disagree. A
function too small to amortise the boundary crossing gets slower, not faster.

`resolveCombat` was ported earlier in `ee02e58`; CeminiDFS shipped its own port in
`36b1e6f`; CeminiParlays measured 0.63–0.85x and stayed on Python (`83bcc97`).

## Snippets

> Verifies exact behavioral parity (floats within 1e-9 plus NaN, ±inf, -0.0, zero,
> ±1, non-ASCII, larger/shrunk edge cases).
> [Source: Cemini Multi-Wiki Link Evaluation.docx, URL 8]

## Dead Ends

- **Porting a hot loop without capturing real calls.** Synthetic inputs miss the cases
  that break.
- **Porting Collectibles hot code.** It is stdlib-only by rule.
