---
title: Corpus Overflow — Out-of-Scope Research Stubs
type: concept
tags: [concept, corpus-hygiene, out-of-scope, research-index, librarian-bookkeeping]
keywords: [corpus inventory, out of scope, research overflow, academic ml, hardware accelerator, mathematical foundations]
related:
  - sources/3-29-20.md
  - sources/ai-10-4-3.md
  - sources/wasertein-1-4-3.md
maturity: draft
created: 2026-04-26
updated: 2026-04-26
---

## Relations

- @sources/3-29-20.md — *DVM: Real-Time Kernel Generation for Dynamic AI Models* (Fang et al., Huawei) — academic ML systems / GPU kernel codegen; not aligned with Cemini's trading-stack research agenda
- @sources/ai-10-4-3.md — *GTA: a new General Tensor Accelerator with Better Area Efficiency and Data Reuse* (Ai et al., Peking University) — academic chip architecture; outside Cemini's software-only stack scope
- @sources/wasertein-1-4-3.md — *Uniform optimal-order Wasserstein quantisation* (Gwóźdź) — pure-mathematics measure-theory paper; no foreseeable Cemini-side application path

## Raw Concept

Hub for source stubs that were ingested during the corpus-bootstrap pass but, on D′ triage (2026-04-26), were judged **not aligned with any active Cemini research thread**. Listing them here keeps the inventory honest (we have the PDFs, we know they exist) while removing them from the lint orphan-flag without forcing them into a wrong-fit hub.

This page is **librarian bookkeeping**, not a research index. If a future Cemini-side question makes one of these load-bearing — for example, if hardware-acceleration economics become relevant to a self-hosted LLM-inference cost model — the corresponding stub should graduate to a real cluster hub and be removed from this page's `related:` list.

## Narrative

### Inclusion criteria

A source lands here if **all three** of the following hold:

1. The PDF is in `research for cemini/` (so it's part of the inventory) and the stub was created by the bootstrap first-page extract pass.
2. The cluster classifier left it as `clusters: [uncategorized]` and human (Opus) triage could not identify a thematic fit with any of the existing cluster hubs (`llm-agent-systems`, `rl-marl-research`, `ai-ethics-and-governance`, `cryptographic-audit-trail`, `kelly-cvar-risk-engine`, `ticker-watchlist`, `gdelt`, `crypto-asset-taxonomy`, `kalshi`, `langgraph`, `hetzner`, `ip-sale-readiness`).
3. There is **no foreseeable Cemini-side question** that would make the source load-bearing within the next 12 months on the current research roadmap.

If criterion (3) shifts (roadmap pivots, new thread opens), the source graduates out of this page.

### Why not just delete?

Deleting the stubs would lose the inventory record of which PDFs were already triaged-and-rejected, leading to duplicate effort on the next sweep. Keeping them under this hub is a librarian's "we looked, we passed" marker.

### Current contents (3 sources, 2026-04-26)

| Stub | Topic | Why out-of-scope |
|---|---|---|
| @sources/3-29-20.md | DVM real-time kernel generation for dynamic AI models | GPU/ML systems infrastructure; Cemini does not run model training, only API-call inference |
| @sources/ai-10-4-3.md | GTA tensor accelerator chip architecture | Hardware design; Cemini is a pure software stack on commodity Hetzner CPUs |
| @sources/wasertein-1-4-3.md | Uniform optimal-order Wasserstein quantisation (pure math) | Measure-theory foundations; no current quant-finance application path identified |

## Snippets

*(None — bookkeeping page.)*
