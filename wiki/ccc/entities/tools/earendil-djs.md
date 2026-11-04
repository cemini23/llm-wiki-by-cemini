---
title: "earendil-works/djs — snapshottable JS/TS-to-WASM engine (Watch: no licence)"
type: entity
tags: [tool, wasm, javascript, sandbox, watch, game-time]
keywords: [djs, wasm, bytecode, snapshot, contiguous heap, fuel metering, deterministic gc]
related:
  - "@osint-wiki/sources/eval-multi-wiki-link-revenue-v10.11-2026-11-03.md"
maturity: draft
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

Surfaced by @osint-wiki/sources/eval-multi-wiki-link-revenue-v10.11-2026-11-03.md, URL 18, **Watch** tier. Routed to game-time scripting and CCC codemode.

The question this page answers: **can a JS/TS engine be paused, serialised, and resumed mid-instruction?**

## Narrative

### What it does

A single-pass JS/TS-to-bytecode engine compiled to WASM.

The distinguishing property: **the entire heap lives in one contiguous byte array**, addressed by `u32` offsets rather than pointers. Consequences that follow:

- **No pointers.** Nothing to fix up when the heap moves.
- **Deterministic compacting GC.** Same inputs, same collection, every time.
- **Suspend and snapshot between any two bytecode instructions.** The whole machine state is one buffer.
- **Fuel metering**, so execution can be bounded.

That combination is unusual. Most engines cannot snapshot mid-execution because their state is spread across native pointers.

### Why it would matter for game-time

The design brief's core invention is a **warp-to-next-event clock**. Implementing that correctly means advancing a simulation by an arbitrary amount without running a renderer.

An engine that can snapshot at instruction granularity would let a game simulate forward and store the resulting state as bytes — which is close to what SQLite-WASM on OPFS already does for persistence. The two ideas are adjacent.

### Why it is Watch, not Extract

The report's own blockers are the right ones and this page adds nothing:

- **18-hour prototype maturity.**
- **An empty README.**
- **No licence file.**

An engine that holds a game's simulation and has no declared licence cannot be adopted, and at 18 hours old it has no evidence behind it. The snapshot property is a claim, not a measurement.

### What would change the verdict

A licence. A non-trivial test suite. A documented snapshot/restore round-trip with a benchmark. Any one of those would move it to Extract.

### Status

Watch. Nothing to do.

## Snippets

> "Provides a single-pass JS/TS-to-bytecode WASM engine whose entire heap lives in one contiguous byte array using u32 offsets (zero pointers) with a deterministic compacting GC and ability to suspend/snapshot between any two bytecode instructions." — report, URL 18

## Dead Ends

- **Adopting an 18-hour-old engine with no licence as a game's scripting layer.** It would be the dependency the whole simulation rests on.
