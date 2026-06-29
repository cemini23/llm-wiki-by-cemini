---
title: vercel-labs/deepsec — agent-powered AppSec scanner
type: entity
tags: [entity, tool, cybersec, appsec, k134]
keywords: [deepsec, vercel, sast, llm-security, apache-2.0]
related:
  - sources/eval-github-repos-plan-multi-wiki-2026-06-29.md
  - entities/tools/anthropic-cybersecurity-skills.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-06-29
updated: 2026-06-29
---

## Relations

- @sources/eval-github-repos-plan-multi-wiki-2026-06-29.md — K134 URL 3 Adopt
- @concepts/wiki-tooling-evaluation.md — Phase-0 GO 2026-06-29

## Raw Concept

Phase-0 from K134 **GitHub Repository Evaluation Plan.docx** — [vercel-labs/deepsec](https://github.com/vercel-labs/deepsec).

## Narrative

**Deepsec** — LLM-assisted vulnerability scanner: regex/heuristic **scan** triage → Claude Opus/Codex **investigate** pass → optional git-history verification. Runs investigations in **Vercel Sandbox** microVMs. Apache-2.0.

**Phase-0 (2026-06-29):** **GO** — 4.7k★, active push 2026-06-22, 35 open issues. Failure-mode audit: not a drop-in for prod trading stack; cybersec-wiki + pre-commit optional scan on federation repos. High token cost on investigate pass — gate to CI nightly, not every commit.

**Steal:** INFO.md threat-model injection pattern for context-dense AppSec prompts.

**Do not:** Mount as default OSINT ingest gate — license posture already covered by `wiki_lint.py` + hooks.

## Snippets

> "Bifurcated pipeline: rapid heuristic scan, then LLM investigation filtering false positives." [Source: eval docx URL 3 (retrieved 2026-06-29)]
