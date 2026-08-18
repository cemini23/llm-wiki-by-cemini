---
title: "Sovereign Agent Mesh + Biscuit tokens"
type: concept
tags: [concept, atto, mcp, authorization, k241]
keywords: [biscuit, libp2p, least-privilege, MCP-sidecar, SAM]
related:
  - entities/tools/google-sam.md
  - sources/eval-multi-wiki-revenue-plan-2026-08-18.md
  - concepts/atto-genealogy-agent-kit.md
  - concepts/intent-bound-tool-gates.md
  - concepts/agent-authorization-stack.md
  - entities/tools/llm-as-a-verifier.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
---

## Relations

- @entities/tools/google-sam.md — Apache-2.0 Extract
- @sources/eval-multi-wiki-revenue-plan-2026-08-18.md — K241 eval
- @concepts/atto-genealogy-agent-kit.md — atto-mcp allowlist
- @concepts/intent-bound-tool-gates.md — tool may fire only inside a bound
- @concepts/agent-authorization-stack.md — authorization primitives
- @entities/tools/llm-as-a-verifier.md — verify claims after a scoped call

## Raw Concept

What this page answers: how a genealogy (or any local-first) agent kit should dispatch tools so a compromised or hallucinating model cannot reach every MCP. Synthesized from google/sam (OSINT K241) and existing atto-mcp allowlist practice. Pairs CCC K278 AIC (authorization-in-the-loop) when that wave is read — do not collapse dual-IDs.

## Narrative

A mesh of agents that can all call every tool is not a product; it is a blast radius. google/sam's Sovereign Agent Mesh puts an MCP sidecar on libp2p and gates each call with a **Biscuit** token: the token carries attenuation (this agent, this tool, this argument shape, this TTL). The model proposes a call; the sidecar checks the biscuit; a failed check is not a retry hint, it is a structural no. That is the same perimeter instinct as K240 structural abstention (the generative shell may pick the question, never the value) applied to *actions*.

Cemini already has an atto-mcp allowlist. SAM is not a reason to replace it. It is a reason to make the allowlist **attenuable at runtime**: a FIND lookup biscuit that cannot write `truth.ged`; a share biscuit that cannot see unredacted civil scans; a verifier biscuit that sees claim text and exhibit hashes, not living-person vitals. Least privilege is not a policy PDF. It is a token the sidecar can refuse without asking the model to "be careful."

Do not stand up a public mesh. Do not put Barone PII in demo biscuits. HITL before any sidecar is more than a local Extract clone. Pair with llm-as-a-verifier so a scoped call still has to survive a claim-vs-exhibit check. Toxic debt (K241 strategic-debt paper) is an unscoped MCP; strategic debt is a narrow biscuit you can throw away if the experiment fails.

## Snippets

> google/sam: Apache-2.0 Extract; Biscuit-scoped MCP sidecar. [Source: `.local/reports/license-k241-2026-08-18.md`]
