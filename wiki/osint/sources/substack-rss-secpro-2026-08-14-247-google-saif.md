---
title: "SecPro #247 — Google Secure AI Framework in practice (K239)"
type: source
tags: [source, substack, rss, cyber, saif, k239]
keywords: [SAIF, Google, Model Armor, agent observability, Zero Trust, prompt injection]
related:
  - concepts/intent-not-form-refusal.md
  - sources/arxiv-2608.12821-hiroute-2026-08-15.md
  - concepts/agent-steering-action-boundary.md
maturity: draft
created: 2026-08-15
updated: 2026-08-15
read_status: read
---

## Relations

- @concepts/intent-not-form-refusal.md — SAIF input/output sanitization + intent-level refusal
- @sources/arxiv-2608.12821-hiroute-2026-08-15.md — routed safety vs one global prompt
- @concepts/agent-steering-action-boundary.md — agents get HITL on high-impact tools

## Raw Concept

| Field | Value |
|-------|--------|
| URL | https://secpro.substack.com/p/247-putting-googles-secure-ai-framework |
| Published | 2026-08-14 |
| sha256 | `d9f1eed571d12631f596b6d5ba535adf451416c0291f5915b4e8b4a41023d702` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-secpro-2026-08-14-247-putting-googles-secure-ai-framework-into-pra.md` |
| retrieved | 2026-08-14 |
| Feed | secpro |

## Narrative

Packt SecPro #247 translates Google **SAIF** (Secure AI Framework) into SOC practice. SAIF is not a new discipline: identity, least privilege, VM, detection, IR, red team, monitoring — applied to **data + infrastructure + model + application**, plus agent tool use.

Practical checklist (vendor-neutral):

1. **AI inventory** — model, owner, purpose, data sources, env, APIs, users, perms, criticality. Shadow SaaS/API adoption is the gap.
2. **Protect training/inference data** — provenance, sanitization, PET, change-tracking (poisoning persists after the write).
3. **Models as production assets** — version, provenance, weight access control.
4. **Zero Trust on AI apps** — identity propagation; no broad service-account for agents. Agent authority ≤ user+task.
5. **Input/output controls** — prompt injection via docs/web; Model Armor as one vendor example.
6. **Narrow agent tools** — SOC agent: read logs, not delete accounts. Containment = HITL + separate privileged workflow.
7. **SOC visibility** — auth, model access, tool calls, unusual prompts, sensitive-data access.
8. **Red-team the system**, not just the model (authz/segmentation failures look like "the model leaked").
9. **IR playbooks** — revoke agent creds, map poisoned model versions, scope exfil.

### Cemini steal (cyber lab + CCC)

- Inventory Cemini/Atto/lab models and MCP tools the same way.
- Pair with SteerBench: high-impact tool calls **hold**.
- Pair with HiRoute/WIFA: don't train a new refusal model; apply least-privilege + intent-not-form at the wrapper/policy layer.
- **No jailbreak PoC** in the wiki.

**Brief:** `../Cybersecurity wiki/briefs/2026-08-15_k239-cyber-hiroute-wifa-saif.md`.
