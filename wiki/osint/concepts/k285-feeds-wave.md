---
title: K285 Feeds Wave — cloud-native harnesses, resilience, options sizing (Oct 2026)
type: concept
tags: [k285, feeds, agents, harness, resilience, options, kelly]
keywords: [k285, stacklok, mecatl, toolhive, sam-newman, module-boundaries, llm-causality, moontower, kelly, vertical-spread]
related:
  - concepts/k285-eval-wave.md
  - concepts/k285-arxiv-wave.md
  - concepts/agentic-code-quality-gates.md
  - sources/substack-rss-moontower-2026-10-07-vibey-vs-discrete-trades.md
  - sources/newsletter-rss-latent-space-2026-10-07-cloud-native-harness.md
  - sources/newsletter-rss-pragmatic-engineer-2026-10-07-sam-newman-resilience.md
maturity: draft
created: 2026-10-08
updated: 2026-10-08
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k285-eval-wave.md
- @concepts/k285-arxiv-wave.md
- @concepts/agentic-code-quality-gates.md

## Raw Concept

K285 feeds cluster hub. **3 feeds:** Latent Space, Pragmatic Engineer, Moontower. Dual-ID **OSINT K285**.

## Narrative

### Latent Space — the cloud-native harness (Stacklok / Mecatl)

Two Kubernetes creators (**McLuckie, Beda**) argue today's harnesses are desktop-bound because the **agent loop, execution, and session state share one process** and state sits as **JSONL on disk**. **Mecatl** separates the loop from execution and state; **ToolHive** governs MCP servers on Kubernetes. Their routing view: **semantic model choice belongs in the harness, not the gateway**, because the context is there. Transferable idea: **separate the loop from sensitive execution** (same as K283's interpreter-over-tool-loop and K284's coding-native player). **No `/route` swap.**

### Pragmatic Engineer — resilience and the limit of guardrails

Sam Newman's strongest point: **"LLMs are not world models … they have no concept of causality."** So *why did the LLM delete my database? Because it has no concept that if I do A, B happens.* He argues **guardrails are not the right long-term solution.** Paired with an incident: **Opus 5.5 formatted a dev's C: drive under `--dangerously-skip-permissions`.** Also: **module boundaries first, then let the AI roam freely only inside them**; **hedge vendors** (multi-model) and swap LLM functions for deterministic code where cheaper; **resist "cognitive surrender."** The three rules of distributed systems, and: **most outages come from resource exhaustion.**

This is the sharpest available framing for the wiki's **deterministic-gate** doctrine — hard gates and sandboxes beat prompt-level guardrails. Pairs with K284's code-review-theater finding.

### Moontower — options as surgical tools (a Kelly worked example)

**"vibey vs discrete trades."** A vague view belongs in stock (delta 1.00, constant); a **specific terminal-value** view belongs in options. Worked example (NKE, pre-earnings): the **38.5/39 call spread at $0.12 → $0.50 (3-to-1)** versus the outright 36 call at **1-to-1**. Sizing via Kelly `f* = p − q/b` → 20% of $5,000, taken at **half-Kelly (40 contracts)**. The heuristic: the straddle ≈ **80% of one σ**, so a 3-to-1 bet needs **p > 25%** to be +EV. The honest postscript: **NKE fell**; the bull trade lost, the symmetric put spread also expired worthless. **No trade, no scp.**

### Distribution

- Stacklok / Sam Newman → `../Cemini claude code CCC/briefs/2026-10-08_k285-harness-resilience.md`
- Moontower → wiki-only (xsp method illustration); **no xsp scp.**
