---
title: "ExecCritic: Learn to Test, Test to Improve for Coding Agents (arXiv:2609.09133)"
type: source
tags: [arxiv, source, k258, harness]
keywords: [k258, ExecCritic, SWE-bench, fail-closed]
related:
  - concepts/k258-harness-evolution-wave.md
  - entities/tools/execcritic.md
maturity: draft
created: 2026-09-09
updated: 2026-09-09
read_status: skimmed
---

## Relations

- @concepts/k258-harness-evolution-wave.md
- @entities/tools/execcritic.md

## Raw Concept

| File | `arxiv-2609.09133-execcritic-learn-to-test-test-to-improve-for-cod.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.09133-execcritic-learn-to-test-test-to-improve-for-cod.pdf` |
| Retrieved | 2026-09-09 |
| Dual-ID | **OSINT K258** |
| sha256 | `edf8f36b8c370f3617a349be0657b8aeb7854f62c89655ef4ef734b236aa3099` |

## Narrative

Microsoft Research: split Test agent from Repair agent. Fail-closed harness freezes tests. Same-trajectory patch+test can agree on a wrong contract (false confidence). SWE-bench Verified: bad tests drop resolve 61.2 to 57.3; GPT-5.6-sol tests raise to 65.3; post-trained Qwen pair 72.6. Repo MSR-Orchard/execcritic Apache-2.0 GO REFERENCE. CCC FILE. 0 Integrate GO.

## Snippets

> When the same trajectory writes both the patch and the test, their errors can agree and create false confidence. Code is publicly available at https://github.com/MSR-Orchard/execcritic [Source: arxiv-2609.09133-execcritic-learn-to-test-test-to-improve-for-cod.pdf]
