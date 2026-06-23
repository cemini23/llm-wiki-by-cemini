---
title: "AOHP — OS-level agent harness on AOSP (arXiv 2606.23449)"
type: source
tags: [source, arxiv, agent-harness, mobile, security, k127]
keywords: [2606.23449, AOHP, Android Open Harness Project, AOSP, information flow, agent-native OS, OpenClaw]
related:
  - concepts/aohp-os-level-agent-harness.md
  - concepts/code-as-agent-harness.md
  - concepts/openclaw-security-taxonomy.md
  - concepts/llm-agent-systems.md
  - entities/tools/aohp-os.md
  - sources/arxiv-agentic-time-machine-2606.21013-2026-06-23.md
maturity: draft
read_status: read
created: 2026-06-23
updated: 2026-06-23
clusters: [llm-agents, audit-security]
---

## Relations

- @concepts/aohp-os-level-agent-harness.md — K127 synthesis
- @concepts/code-as-agent-harness.md — harness taxonomy sibling
- @entities/tools/aohp-os.md — GitHub entity (Apache-2.0 confirmed Phase-0)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | AOHP: An Open-Source OS-Level Agent Harness for Personalized, Efficient and Secure Interaction |
| **Authors** | Shanhui Zhao, Jiacheng Liu, Guohong Liu, et al. (Tsinghua / PKU / HKU) |
| **arXiv** | 2606.23449 (22 Jun 2026) |
| **sha256** | `f880dbbb8f481a10c19890bdbb0df8c0b0a9a8a04e428d1c2b7a14dd7894251a` |
| **Repo** | https://github.com/aohp-os/aohp |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.23449-2606-23449v1-aohp-an-open-source-os-level-agent.pdf` |
| **Retrieved** | 2026-06-23 (inbox) |
| **Read status** | read (abstract + §1–3 design principles) |

## Narrative

**Problem:** Personal OSes are app-centric — fixed UIs, app-boundary permissions, pixel-oriented GUIs — creating overhead and security gaps for **agent-mediated** cross-app workflows.

**AOHP (Android Open Harness Project):** AOSP fork treating **agents as first-class OS actors** with three mechanisms:

1. **Personalized service composition** — task-level entrances (e.g., unified shopping) assembled from app/GUI/CLI/API capabilities
2. **Efficient agent interfaces** — parallel background execution, structured UI, event streams (text > pixels)
3. **Secure information flow** — sandbox sensitive values via information-flow tracking across agent context + tool calls

**Reported gains vs stock Android on OpenClaw mobile tasks [TENTATIVE]:** +21.12% completion rate (54.44% → 75.56%), −51.55% LLM tokens, −44.21% execution time; security case studies block private plaintext exfiltration.

**Cemini posture:** **REFERENCE** — laptop Cursor/MCP harness is not AOSP; steal **information-flow tracking** + **structured agent interfaces** patterns for CCC wiki and `@concepts/openclaw-security-taxonomy.md`. **CONDITIONAL-GO** on repo (Apache-2.0, ~43★, active Jun 2026) — do not flash phone images; study architecture docs only.

## Snippets

> "The core design principle of AOHP is to treat agents as first-class OS actors, enabling adaptive user interfaces and agent-friendly runtime environments." [Source: arXiv:2606.23449 abstract (retrieved 2026-06-23)]

> "AOHP raises the average completion rate from 54.44% to 75.56%, reduces LLM token consumption by 51.55% and accelerates task execution by 44.21%." [Source: arXiv:2606.23449 abstract (retrieved 2026-06-23)]

> Source Code: https://github.com/aohp-os/aohp [Source: arXiv:2606.23449 title block (retrieved 2026-06-23)]

## Dead Ends

- Mobile AOSP fork ≠ cemini-prod Linux stack — no prod scp.
- OpenClaw eval substrate may differ from Cursor MCP — pattern steal only.
