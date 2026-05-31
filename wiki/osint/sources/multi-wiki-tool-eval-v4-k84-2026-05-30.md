---
title: "Multi-Wiki Tool Evaluation (v4 prompt, K84 batch — 24 URLs)"
type: source
tags: [source, gemini-deep-research, tool-eval, v4-prompt, license-corrections, k84]
keywords: [pageindex, poly-maker, hivemind, agent-laboratory, quantstats, superclaude, addyosmani-agent-skills, polymarket-agents]
related:
  - sources/tool-eval-50urls-polymarket-kalshi-license-false-negative-2026-05-21.md
  - sources/multi-wiki-tool-eval-19url-2026-05-20.md
  - concepts/cemini-license-posture.md
  - concepts/wiki-tooling-evaluation.md
  - entities/tools/pageindex.md
  - entities/tools/warproxxx-poly-data.md
  - entities/tools/polymarket-agents.md
  - entities/tools/n8n-workflows.md
  - concepts/cemini-workflow-tooling-audit-2026-05-30.md
  - sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md
maturity: draft
read_status: deep-read
created: 2026-05-30
updated: 2026-05-30
---

## Relations

- @sources/tool-eval-50urls-polymarket-kalshi-license-false-negative-2026-05-21.md — same v4 prompt family; license false-negative pattern reproduced
- @concepts/cemini-license-posture.md — post-run `gh api` corrections recorded here
- @entities/tools/pageindex.md — eval Adopt **overturned** by prior Phase-0 NO-GO (2026-05-05)
- v4 prompt frozen at `Cemini claude code CCC/prompts/deep-research-multi-wiki-eval-v4-2026-05-21.md`; v5 supersedes for new runs

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Tool Evaluation for Cemini Wiki Integration |
| **Author** | Gemini Deep Research (v4 multi-wiki eval prompt) |
| **Type** | docx |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/Tool Evaluation for Cemini Wiki Integration.docx` |
| **Retrieved** | 2026-05-30 |
| **URLs** | 24 evaluated (+ ancillary links) |
| **Read status** | deep-read + GitHub license spot-check |

## Narrative

K84 v4 batch spanning agent skills, PageIndex/RAG, Polymarket bot repos, cybersec skills, and local inference (Step-3.7-Flash). **Prompt gap:** v4 does not know **world-cup-bot** (public OSS, modules 1–7, `wc_advance_lp_v4`) — evals Polymarket/agents and poly-maker without naming Cemini’s shipped WC vertical or conviction-LP safety workflow.

### Gemini aggregate (as reported)

| Tier | Count | Notable |
|------|-------|---------|
| Adopt | 6 | Step-3.7-Flash, AlphaGBM/skills, Polymarket/agents, Anthropic-Cybersecurity-Skills, PageIndex, (partial) |
| Steal-from | 6 | quantstats, scale-agentex, forge-skills, SuperClaude, addyosmani/agent-skills, freephdlabor |
| Defer | 1 | Patter |
| Reference-only | 2 | Markov Medium, Agenvoy |
| Reject | 8+ | NO LICENSE cluster, MHDDoS, gitnexus (claimed PolyForm) |
| UNAVAILABLE | 1 | PythTerminalCSV |

### License corrections after `gh api` spot-check [CONFIRMED 2026-05-30]

| URL | Gemini license | Verified | Verdict adjustment |
|-----|----------------|----------|-------------------|
| warproxxx/poly-maker | NO LICENSE FOUND | **MIT** | Reference-only (K30 steal-from pattern exists) — false negative |
| warproxxx/poly_data | NO LICENSE FOUND | **GPL-3.0** | Reject for IP-sale surfaces (confirms existing entity) |
| activeloopai/hivemind | NO LICENSE FOUND | **Apache-2.0** | Defer — verify PR-review bot fit vs lazy-tool |
| SamuelSchmidgall/AgentLaboratory | NO LICENSE FOUND | **MIT** | Reference-only academic agent lab |
| CL-ML/open-collider | NO LICENSE FOUND | **MIT** | Reference-only |
| tintinweb/pi-gitnexus | PolyForm claim | **MIT** | Steal-from (Solidity graph tooling) — eval license wrong |
| MatrixTM/MHDDoS | NO LICENSE FOUND | **MIT** | **Stay Reject** — offensive DDoS; license ≠ fit |
| VectifyAI/PageIndex | MIT Adopt | MIT | **NO-GO upheld** — Phase-0 audit 2026-05-05 (single-file API, wiki mismatch) |
| Polymarket/agents | MIT Adopt | MIT | Reference — already `@entities/tools/polymarket-agents.md` |

### v4 prompt improvement requirements (for v5)

1. Add **evaluation surface 1b**: `world-cup-bot` public OSS + Cemini WC module (`concepts/world-cup-advance-market-bot-v1.md`) — avoid re-Adopt-ing poly-maker/agents as if greenfield.
2. Mandate **`gh api` license lookup in prompt** (not post-run only) — K53/K54/K55/K84 false-negative rate ~30% on NO LICENSE FOUND.
3. Cross-check **prior Phase-0 NO-GO** list (PageIndex, SwarmVault, Claude-OSINT) before Adopt tier.
4. Flag **time-volatile sports LP** evals with `[NEEDS RE-RUN]` date — squad/injury context stale in ≤7d pre-tournament.

## Snippets

> "NO LICENSE FOUND: N" — recurring v4 failure mode; `gh api repos/{owner}/{repo} --jq .license.spdx_id` overturned 6/8 checked Rejects in this batch alone. [Source: ingest spot-check 2026-05-30]
