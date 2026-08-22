---
title: Inadvertent context leakage — refusal is not confidentiality
type: concept
tags: [privacy, agents, safety, covert-channel]
keywords: [suppression, predicate-inference, third-party-visible-generation, SSN-stego, capability-correlation]
related:
  - sources/arxiv-2608.19857-inadvertent-context-leakage.md
  - concepts/agent-safety-executable-evaluation.md
  - concepts/agent-runtime-identity-adr.md
  - sources/arxiv-2608.18628-safety-overrides-vision.md
  - sources/newsletter-rss-tldrsec-2026-08-20-tldr-sec-342.md
maturity: draft
created: 2026-08-21
updated: 2026-08-21
---

## Relations
- @sources/arxiv-2608.19857-inadvertent-context-leakage.md
- @concepts/agent-safety-executable-evaluation.md
- @concepts/agent-runtime-identity-adr.md

## Raw Concept
Secrets that share a context window with generation leave statistical fingerprints in *benign* outputs even when the model correctly refuses extraction. Linguistic leakage judges are insufficient. Suppression (avoiding the protected value) *correlates* with leakage (ρ=0.95). Stronger models leak more. Active adversaries can engineer an encoding channel (e.g. punctuation counts) on top of the passive one.

## Narrative
Policy for local abliterated lab / cybersecurity wiki — not an attack cookbook.

- **Treat agent outputs as covert channels.** Anything a third party sees (email, Slack, PR description, “write a paragraph with numbers”) is an observation of in-context secrets.
- **Do not put secrets in context with third-party-visible generation.** PIN, SSN, health, credentials, USER.md dumps. If the agent must act, use a tool that never returns the secret to the model (1Password grant pattern).
- **Refusal ≠ privacy.** Verbose “never reveal X” instructions can *increase* suppression and therefore leakage.
- **Capability is the risk factor.** Frontier instruction-following amplifies the channel; small/resistant models leak less at N≥4.
- **Eval:** executable safety tests should include *benign-output* predicate inference, not only jailbreak strings. Pair with ADR telemetry (did the secret appear in traces?) and SPIFFE `act=agent` so a leaked completion is attributable.

No scp. No production copy of attack prompts.

## Snippets
See @sources/arxiv-2608.19857-inadvertent-context-leakage.md (2-digit near-perfect, 4-digit 82% Opus, SSN via `!` encoding).
