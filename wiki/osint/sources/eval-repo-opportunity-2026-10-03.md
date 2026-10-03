---
title: "Repository Revenue Opportunity Analysis — 20 rows (2026-10-03)"
type: source
tags: [source, k279, eval, testing, tooling]
keywords: [k279, eval-docx, property-testing, hypothesis, xxhash]
related:
  - concepts/k279-dfs-parlays-wave.md
  - concepts/k279-harness-wave.md
  - concepts/k279-ood-stub-wave.md
maturity: draft
created: 2026-10-03
updated: 2026-10-03
read_status: skimmed
---

## Relations

- @concepts/k279-dfs-parlays-wave.md
- @concepts/k279-harness-wave.md
- @concepts/k279-ood-stub-wave.md

## Raw Concept

| File | `Repository Revenue Opportunity Analysis.docx` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Repository Revenue Opportunity Analysis.docx` |
| Archive | egress-fi 2026-10-03 |
| Retrieved | 2026-10-03 |
| Dual-ID | **OSINT K279** |
| sha256 | `e7a9ad3db058eb541f4bfec4f35e35d5f33803b4849a21f98c9e8816c89cf36a` |
| Batch theme | Developer tooling, agent orchestration, verification harnesses, high-throughput hashing, security evaluation |

## Narrative

Twenty rows. Same directive: extract the technique, skip the license audit.

### The row worth acting on — property-based testing of the maths

**`HypothesisWorks/hypothesis`** — tier Extract, combo-with-ceminiparlays.

The technique: **property-based testing with automatic failure shrinking.** You state an invariant, the library generates inputs that try to break it, and when it finds a failure it shrinks it to the smallest counterexample.

Where it applies in **CeminiParlays**:

| Target | Property to assert |
|--------|-------------------|
| De-vig functions | The de-vigged probabilities sum to exactly 1.0, for any valid two-way or three-way book |
| De-vig monotonicity | Raising a single leg's implied price cannot lower its de-vigged probability |
| Gaussian copula | The joint hit rate is bounded above by the minimum marginal, and below by the product |
| Student-t copula | As the degrees-of-freedom parameter goes large, it converges toward the Gaussian case |
| Correlation matrix | Any generated matrix is positive semi-definite |

This is the highest-value row in either docx. The copula and de-vig code is the part of the stack where a silent numerical bug converts directly into mispriced tickets, and it is exactly the kind of code that unit tests with hand-picked inputs miss. Property tests find the input nobody thought of.

The docx also notes the same library covers genealogical date-parser edge cases for Atto — leap years, month boundaries, the calendar reform.

### The two Integrate rows

**`Cyan4973/xxHash`** — Integrate, high-throughput non-cryptographic hashing (XXH3, XXH128, up to 30 GB/s). The use case named in the docx is replacing cryptographic hashing where it is only used for identity, not security. Worth checking whether any of our scripts hash large files with SHA-256 purely for dedupe. The wiki's own `preingest_check.py` does exactly this on every inbox drop.

**`pingdotgg/t3code`** — Integrate, CCC. An open-source control surface that supervises local CLI coding agents, isolating runs inside git worktrees with remote approval before merge or push. That is the same shape as the `/route` lane, with a review gate we do not have.

### Extract rows for other surfaces

| Repo | Surface | Technique |
|------|---------|-----------|
| `Effect-TS/effect` | CCC | Typed error channels, fiber-structured concurrency, managed resources |
| `earendil-works/pi` | CCC | Minimalist coding-agent loop with incremental diff review |
| `Mr-xn/Penetration_Testing_POC` | Operator lab | Curated PoC library as a detection benchmark. **No PoC in the wiki** |
| `sh377c0d3/AppSec-Payloads` | Cybersec | Structured injection dictionaries for a local fuzz harness |

### Pass rows

`pyresttest`, `Hello-Python`, `testing-python-apps`, `kunchenguid/firstmate` — all Pass. The last one is Pass because it duplicates Cursor CLI, Claude Code, and T3 Code.

### Not adopted

Nothing is vendored from this docx. `hypothesis` would be a dependency if adopted; that is a decision for the CeminiParlays repo, not this wiki.

**Cemini posture:** FILE. Zero clones.
