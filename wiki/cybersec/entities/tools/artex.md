---
title: "ARTEX — AI-native penetration-testing framework"
type: entity
related:
  - sources/newsletter-rss-tldrsec-2026-11-12-tldr-sec-354---artex-agentic-hacking-in-the-wild.md
  - concepts/agentic-offensive-security-kill-chain.md
  - entities/tools/hexstrike-ai.md
  - concepts/llm-pentest-automation.md
  - concepts/ai-for-cybersecurity.md
  - concepts/owned-target-whitehat-lab.md
updated: 2026-11-14
---

## Raw Concept

What prompted this page: Datadog and Google Threat Intelligence Group reporting in November 2026 described ARTEX as a framework used in real intrusions. This page documents the tool for defensive detection. It does not describe how to obtain or operate it.

## Narrative

ARTEX is an AI-native penetration-testing framework. It appeared in public reporting as an open-source project, and threat actors have used it against cloud environments `[TENTATIVE]`.

### Architecture as reported

| Component | Reported behaviour |
|---|---|
| Planner | One LLM plans the operation |
| Workers | Sub-agents execute individual steps |
| Blackboard | Workers record findings on a shared graph |

The design is a standard planner-worker split with shared state. It lets the framework iterate on results without a human step.

### Observed use `[TENTATIVE]`

- Entry with compromised long-term IAM access keys.
- CloudWatch log searches for financial data, file paths and secret material such as `AKIA` keys.
- Automated Active Directory reconnaissance, Kerberoasting and DCSync.
- Cloud profiling to harvest Azure storage keys.
- Unauthenticated abuse of public Amazon Cognito user pools: anonymous sign-up, token collection, then account enumeration.

Reported speed is initial access to deep access in about 15 minutes. The same reporting notes heavy forensic noise.

### Detection opportunities

These signatures come from the Datadog write-up and are useful as hunting hypotheses, not as stable indicators:

| Signal | Value |
|---|---|
| HTTP user agent | Characteristic string in the original report |
| S3 probe object | Placeholder names such as `zzz_nonexistent_abc.txt` |
| CloudWatch API shape | `FilterLogEvents` with a consistent 1000-event limit |
| Error profile | Many permission-denied responses during enumeration |
| Identity pattern | Burst of API calls from one key across services |
| Exposure | Internet-facing ARTEX consoles, often hosted in Singapore or Hong Kong |

`[NEEDS VERIFICATION 2026-11-14]` — confirm each signature against the vendor write-ups before adding it to a production rule.

### Defensive controls

1. Remove long-term static access keys. Move to short-lived workload credentials.
2. Restrict control-plane access to trusted networks.
3. Detect identity velocity anomalies and API bursts, not only tool strings.
4. Harden public Cognito user pools: disable self-registration where it is not needed, and monitor anonymous sign-up.
5. Keep continuous vulnerability scanning, because the framework iterates on exposed weaknesses.

### Why it matters for this workspace

ARTEX is evidence that agentic attack tooling has left the lab. The local whitehat lab can use the same architecture class to test detections, inside an authorised and isolated environment only. See @concepts/agentic-offensive-security-kill-chain.md and @concepts/owned-target-whitehat-lab.md.

### Open questions

- `[OPEN QUESTION 2026-11-14]` Which reported behaviours are framework defaults and which are operator choices? Detection priority depends on the answer.
- `[NEEDS VERIFICATION 2026-11-14]` Is the project still maintained, and under which licence?
