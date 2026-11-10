---
title: "jkrup/jeveryword — numbered-token span extraction (local code, remote model)"
type: entity
tags: [tool, extraction, pii, quoting, guruwatcher, atto, immature]
keywords: [jeveryword, jev, numbered tokens, span extraction, pii detection, verbatim quote, typesafe]
related:
  - sources/eval-multi-wiki-link-revenue-v10.10-batch-b-2026-11-01.md
  - entities/tools/liquidai-d1-2b.md
  - entities/tools/jevals.md
maturity: draft
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

Surfaced by @sources/eval-multi-wiki-link-revenue-v10.10-batch-b-2026-11-01.md, URL 4, **Extract** tier. Routed to Atto, Collectibles, and GuruWatcher.

The question this page answers: **how do you extract a field from text and guarantee the extracted value is verbatim?**

## Narrative

### The pattern

Number every word in the input. Give the model a multiple-choice question over those numbers instead of a generation task. Turn the chosen numbers back into a substring.

The invariant the package documents is:

```
text.slice(start, end) === value
```

Every returned field is a literal slice of the source, with a character offset and a probability. A model that can only answer multiple-choice cannot invent text, because every answer is an index.

Three functions:

| Function | Purpose |
|----------|---------|
| `extractSpans` | Named fields from free text. |
| `classifyChunks` / `mergeChunks` | A label per word, for example PII. |
| `tokenize` | The lower-level core. |

### Why the pattern is worth having

This is the direct answer to quote drift. If a claim must be quoted exactly — a newsletter line in a GuruWatcher ledger, a field from a civil record — then an index into the source is a stronger guarantee than a prompt instruction. The invariant holds **regardless of which model runs**, because it is enforced by the slice, not by the model's good behaviour.

That is the part to copy. The package is not the part to depend on.

### Phase-0, 2026-11-01 — two findings, both limiting

**1. The model is remote.** The report's implementation note says this must run "strictly on local model paths … rather than external cloud endpoints" for Atto vault records and `Desktop/family/` data. That instruction cannot be followed with this package. Its bundled `createJevClient` requires `TYPESAFE_API_KEY`. The hosted endpoint uses USDC payments with 25 free calls per day per IP. No local model path is documented anywhere in the README.

The library code is local and dependency-free. The **model call is not**. So the text still leaves the machine.

**2. It is four stars.** The report itself logs "4 stars (listed as 0–1 in earlier snapshots)". A repository at that size is a sketch, not a dependency.

The licence is MIT. The package has zero dependencies and runs on Node 20+, Cloudflare Workers, Deno, and Bun.

### Verdict

**Extract the pattern. Do not adopt the package.**

| Surface | Use |
|---------|-----|
| GuruWatcher | **Yes.** Newsletter text is public. Exact-quote extraction with a remote model is acceptable, and quote drift is the problem this solves. |
| Collectibles | **Yes**, for sold-comp titles, which are public listing text. |
| Atto | **No** for vault records and `Desktop/family/`. The text leaves the machine. Revisit only if a local model can fill the `evaluate` slot. |

The `stubEvaluate` export allows tests with no network and no key. A local model can in principle occupy the same slot, because `evaluate` is an injected function. That is the path to a local version — write the injection, not the dependency.

### Status

Extract, **pattern only**, maturity very low.

## Snippets

> "export TYPESAFE_API_KEY=…" — required for the bundled `createJevClient`; "On Vercel no key is needed, because AI Gateway accepts the project's own identity token." [README, fetched 2026-11-01]

> "dependencies: 0" — the package itself. [README, fetched 2026-11-01]

> "MIT license" — the whole licence section. [README, fetched 2026-11-01]

## Dead Ends

- **Using it on Atto vault records or `Desktop/family/`.** The model is remote. The text leaves the machine, which is the boundary Atto exists to hold.
- **Depending on the package rather than the pattern.** Four stars. Copy the numbered-token idea and the slice invariant into a local implementation.
