---
title: "AWS ABAC authorization traps — alterable guards, evaluation semantics, action-key mismatch"
type: concept
maturity: draft
related:
  - sources/newsletter-rss-tldrsec-2026-11-19-tldr-sec-355---cyber-chaos-monkey-offsec-harness.md
  - concepts/cloud-pentest.md
  - concepts/intent-governed-tool-authorization.md
updated: 2026-11-22
---

## Raw Concept

What this page answers: how do AWS Attribute-Based Access Control policies fail in practice? From Itay Saraf's DEF CON 2026 talk, summarized in tl;dr sec #355.

## Narrative

Attribute-Based Access Control (ABAC) grants or denies by tags and condition keys, not by fixed resource names. That flexibility creates three trap classes. `[TENTATIVE]` `[NEEDS VERIFICATION 2026-11-22]` against the talk and AWS advisories.

1. **Alterable guards.** A policy trusts a tag as a security boundary, and the user can change that tag. A principal that can edit its own `team` or `env` tag can move itself into a broader role.
2. **Evaluation semantics.** Case sensitivity and similar rules differ between services. A tag value that a policy treats as matched may not match at enforcement time, or the reverse.
3. **Action-key incompatibility.** A condition key is applied to an action that does not support it. The condition silently does not apply, and the policy is wider than the author intended.

The speaker reports that AWS's own managed policies have shown these issues, which makes the classes a review checklist, not only a customer error.

**Defensive checklist.**

- Do not use a tag as a trust boundary if the principal can write that tag. Separate tagging permission from tag consumption.
- Test evaluation semantics per service. Write a deny test that would fail if the condition were ignored.
- Confirm that each condition key is supported by each action it guards. Treat a key that AWS lists as unsupported as absent.
- Review managed policies as inputs, not as ground truth.

**Link to agent authorization.** The same trap appears in agent tool authorization. A guard that reads a field the agent can set is not a guard. This is the intent-governed authorization problem in one sentence.

[Source: newsletter-rss-tldrsec-2026-11-19-tldr-sec-355---cyber-chaos-monkey-offsec-harness.md]

## Snippets

> "Alterable guards (where users can modify tags to bypass restrictions), evaluation semantics (like case-sensitivity differences), and action-key incompatibility (where actions don't support specified condition keys)."
[Source: tl;dr sec #355]
