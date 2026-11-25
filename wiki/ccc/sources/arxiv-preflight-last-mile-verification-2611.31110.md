---
title: "Preflight — agentic last-mile verification for software supply chains (2611.31110)"
type: source
related:
  - concepts/program-scoped-dependency-verification.md
  - concepts/agent-completion-verification-gates.md
  - concepts/agent-vm-sandboxing.md
updated: 2026-11-25
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Preflight: Agentic Last-Mile Verification for AI Software Supply Chains |
| Author | Yaman Jandali, Nojan Sheybani, Farinaz Koushanfar, Tara Javidi (UC San Diego) |
| Type | arXiv preprint (cs.AI), accepted at the AI for Science workshop, NeurIPS 2026 |
| ID | 2611.31110v1, 23 Nov 2026 |
| Location | research to be indexed/ccc/arxiv-2611.31110-preflight-agentic-last-mile-verification-for-ai.pdf |
| Retrieved | 2026-11-25 |
| File | `arxiv-2611.31110-preflight-last-mile-verification-for-ai.pdf` |
| Pages | unknown (read p.1 only) |
| Read status | read (abstract, intro) |

## Narrative

Package checks answer a different question than the one that matters. Provenance and static analysis tell you what a package is. They do not tell you what it does inside program A.

Preflight makes dependency verification **program-scoped**. It extracts the symbols that the application actually references. It synthesizes function-level harnesses, validates them, and runs the resolved artifact in a restricted environment. It records behavioral fingerprints. When a baseline exists, it compares the new behavior against the prior version, for the same application surface.

Evaluation:

- Four real supply-chain incidents across five application contexts.
- Malicious verdicts in four incident contexts. A clean verdict for the LiteLLM client context, where the affected proxy path is not exercised.
- 100 benign packages: all clean, zero observed false positives.
- Ablation on Ultralytics and ctx: function-level harnesses expose the malicious behavior in both. Import-only probing exposes neither.

**Why it matters.** This is a harness that generates harnesses to test code. The ablation is the useful result: import-time checks miss behavior that only fires on a specific function path. Any pre-install gate in this workspace that only imports a package will miss the same class of behavior.

Not a routing paper. Off the `/route` lane. [TENTATIVE]
