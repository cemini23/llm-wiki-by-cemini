---
title: "Program-scoped dependency verification — check behavior where the app uses it"
type: concept
related:
  - sources/arxiv-preflight-last-mile-verification-2611.31110.md
  - concepts/agent-completion-verification-gates.md
  - concepts/agent-vm-sandboxing.md
updated: 2026-11-25
maturity: draft
---

## Raw Concept

Question this page answers: how do you tell whether a Python dependency is dangerous for this program, not for the ecosystem in general? Synthesised from `@sources/arxiv-preflight-last-mile-verification-2611.31110.md` (2611.31110).

## Narrative

Package scanners answer an ecosystem question. They ask what a package is, who published it, and what it contains. They do not answer the program question: what does this artifact do when program A calls it.

The gap matters for two reasons. Malicious behavior may fire only on a specific function, constructor, plugin path, or argument pattern. And program A may use only a small part of the package API surface. Import-time and install-time checks miss both cases.

**Program-scoped verification has four steps.**

1. Extract the symbols the application actually references.
2. Synthesize function-level harnesses and validate them.
3. Run the artifact in a restricted environment and record behavioral fingerprints.
4. Compare against a prior version of the same surface, when a baseline exists.

**The ablation is the key result.** On Ultralytics and ctx, function-level harnesses expose the malicious behavior in both. Import-only probing exposes neither. A pre-install gate built on `import pkg` is a weak check.

**False-positive discipline.** Preflight gave clean verdicts to all 100 benign packages. That matters more than the detections: a gate that fires on good packages gets turned off.

**Why it matters here.** This workspace installs third-party skills, MCP servers, and CLIs. Any vetting step that only imports the package tests a fraction of the attack surface. Pair this page with the Phase-0 audit pattern, and with sandbox isolation at run time.

**Status.** One paper, 100 benign packages, four incidents. [TENTATIVE]
