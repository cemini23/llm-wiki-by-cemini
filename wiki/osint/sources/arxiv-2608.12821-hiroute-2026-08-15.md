---
title: "HiRoute — hierarchical routed prompt-tuning for LLM safety (arXiv 2608.12821, K239)"
type: source
tags: [arxiv, llm-safety, cyber, ccc, k239]
keywords: [HiRoute, hierarchical router, prompt-tuning, over-refusal, category-specific safety]
related:
  - concepts/intent-not-form-refusal.md
  - concepts/agent-steering-action-boundary.md
  - sources/arxiv-2608.13304-wifa-intent-not-form-2026-08-15.md
  - sources/arxiv-2608.12654-steerbench-work-2026-08-15.md
  - sources/substack-rss-secpro-2026-08-14-247-google-saif.md
maturity: draft
created: 2026-08-15
updated: 2026-08-15
read_status: read
---

## Relations

- @concepts/intent-not-form-refusal.md — category-agnostic boundary + fine-grained experts
- @concepts/agent-steering-action-boundary.md — same hold/proceed decision, prompt-side
- @sources/arxiv-2608.13304-wifa-intent-not-form-2026-08-15.md — WIFA intent groups vs HiRoute routers
- @sources/arxiv-2608.12654-steerbench-work-2026-08-15.md — proceed/hold twin of routed safety
- @sources/substack-rss-secpro-2026-08-14-247-google-saif.md — SAIF ops translation

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.12821, "HiRoute: Hierarchical Routed Prompt Tuning for Safety Alignment of Large Language Models" |
| Author | Fangzhou Chen, Shiji Zhao, Mengyang Wang, Qihui Zhu, Ranjie Duan, Maoxun Yuan, Xingxing Wei (Beihang) |
| Retrieved | 2026-08-15 |
| File | `arxiv-2608.12821-hiroute-hierarchical-routed-prompt-tuning-for-sa.pdf` |
| sha256 | `3eb3fc36a01ee1bb7cb524af4214583db2338d5d92ef11e769c51efabe94304e` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.12821-hiroute-hierarchical-routed-prompt-tuning-for-sa.pdf` |
| Type | cs.LG preprint, 17pp, Aug 2026 |

## Narrative

Parameter-efficient safety that does **not** rely on one global refusal prompt. HiRoute trains a lightweight **hierarchical router** on frozen-LLM representations to (1) detect harmful intent and (2) predict multi-label risk scores. Then it freezes backbone + router and preference-optimizes a **shared coarse safety prompt** plus **fine-grained prompt experts**. At inference, benign inputs bypass the safety branch; risky inputs get the shared prompt plus a router-weighted expert mix.

Claimed win vs a single global safety prompt: fewer generic unconstructive refusals, more risk-specific lawful alternatives, less over-refusal on benign inputs. `[TENTATIVE]` — single paper; no independent replication.

### Cemini steal (cyber + CCC)

- **Policy pattern only.** Do not train a jailbreak/defense model in this workspace. **No jailbreak PoC in the wiki.**
- Routing idea is portable to `/route` and lab assist: coarse "is this a state-changing / out-of-scope request" plus a small set of domain experts (Atto PII, prod orders, cyber authorized-scope).
- Pairs WIFA (intent groups, not wrapper form) and SAIF (inventory, least privilege, HITL on high-impact tool calls).

**Brief:** `../Cybersecurity wiki/briefs/2026-08-15_k239-cyber-hiroute-wifa-saif.md`.

## Snippets

> "HiRoute first trains a lightweight hierarchical router on representations extracted from a frozen LLM to jointly detect harmful intent and predict multi-label risk scores." [Source: arxiv-2608.12821 abstract]
