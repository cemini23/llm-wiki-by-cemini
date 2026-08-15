---
title: "Latent Space — React for Agents: Flue 2 hooks + Pi harness (K239)"
type: source
tags: [source, newsletter, rss, ccc, agent-harness, k239]
keywords: [Flue, Fred Schott, Astro, Agent Hooks, Pi harness, eve, meta-harness]
related:
  - concepts/practical-loop-engineering.md
  - concepts/code-as-agent-harness.md
  - concepts/agent-steering-action-boundary.md
maturity: draft
created: 2026-08-15
updated: 2026-08-15
read_status: read
---

## Relations

- @concepts/practical-loop-engineering.md — hooks/re-render vs /goal /loop
- @concepts/code-as-agent-harness.md — "no agent without a harness"
- @concepts/agent-steering-action-boundary.md — dynamic tool attach still needs a proceed/hold gate

## Raw Concept

| Field | Value |
|-------|--------|
| URL | https://www.latent.space/p/flue-2 |
| Published | 2026-08-15 |
| sha256 | `4eec24d91652e4e4d2a984083ff8b677991e9987b11132688b0c76267d2f2113` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/newsletter-rss-latent-space-2026-08-15-react-for-agents-astro-creator-brings-hooks-to-h.md` |
| retrieved | 2026-08-15 |
| Feed | latent-space |

## Narrative

Fred Schott (Astro; Cloudflare after Jan acquisition) shipped **Flue 2**, first stable release. Foundation is React-style **Agent Hooks**. An agent is a JS function that **re-renders every turn** (before every model call). 16 built-in hooks including `useSkill()`, `useTool()`, `useSubagent()`; custom hooks allowed.

Schott recanted the "Astro/Next for agents" file-routing metaphor: big customers run **one agent**, not five file-routes. Composability > routing. Flue sits on **Pi** (minimal open harness); Schott: **"There is no agent without a harness."** Closest competitor: Vercel **eve** (also built-in harness). Older AI SDK / Cloudflare Agents SDK / Mastra are adding harnesses as a feature; Flue/eve treat the harness as the product.

Host-portable (open source, not Cloudflare-only); a Flue agent has been deployed on Vercel. Managed-agents product is **not** on the Flue roadmap. Meta-harness (Omnigent / Exo) is a different problem than hosted agents.

### Cemini steal (CCC)

- Steal the **hook/re-render** mental model: config (tools, skills, subagents) can change mid-conversation after a verification step — not a static SKILL.md dump.
- **File-based agent = antipattern** when the company is one agent (matches Cemini `/route` + one policy file).
- Do **not** install Flue this batch (no Phase-0 SPDX/size audit of the Flue repo). Awareness only.
- Dynamic `useTool()` still needs SteerBench **HITL at the action boundary**.

**Brief:** `../Cemini claude code CCC/briefs/2026-08-15_k239-ccc-steerbench-flue-loop.md`.
