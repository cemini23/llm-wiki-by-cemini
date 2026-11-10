---
title: "A cloud LLM quarantine is a deny-list, and deny-lists lag new surfaces"
type: concept
related:
  - sources/newsletter-rss-tldrsec-2026-11-05-tldr-sec-353---a-thousand-fewer-paths-to-root-ku.md
updated: 2026-11-10
---

## Raw Concept

Question: **when a cloud provider quarantines a compromised credential, does that stop model inference?** From tl;dr sec #353, reporting Plerion's finding on the AWS Bedrock Mantle service.

## Narrative

AWS publishes `AWSCompromisedKeyQuarantineV3`. The policy blocks a set of actions with an explicit deny. The reported finding is that the policy blocks `bedrock:InvokeModel` and does not block `bedrock-mantle:CreateInference`.

The result is a documented quarantine that does not stop model inference. An attacker holding a quarantined key can still reach DeepSeek, Qwen and 36 other open-weight models through the Mantle endpoint.

### Why this is a class of problem, not one bug

A quarantine policy is a **deny-list**. A deny-list enumerates known surfaces. A cloud provider keeps shipping new services and new action namespaces. Between the new service and the policy update, exposure exists.

The same shape appears in other cloud guardrails: a block on one compute action that misses a second one, a log filter on one resource type that misses a sibling type, a service control policy scoped to a service name that a new endpoint does not use.

### Why detection failed too

The calls appear only as CloudTrail **data events**. Data events are off by default in most accounts. So the traffic produces no default-visible record. The activity is authorised by the key, allowed by the quarantine, and absent from the default log.

### Controls the report recommends

| Control | Effect |
|---|---|
| Enable CloudTrail data events for `AWS::BedrockMantle::Project` | makes the calls visible |
| Service control policy to deny the service when unused | closes the gap at the organisation boundary |
| Wait for AWS to extend the quarantine policy | closes the gap at the provider |

The middle control is the one a defensive team can apply today without waiting on the provider. An unused service should be denied, not merely quarantined.

### The reusable rule

**Enumerate the action namespaces, not the service names.** For each cloud AI service in scope, record the exact API action that produces output. Then confirm the own-policy or quarantine covers that action and not only its predecessor. Treat "we blocked the model call" as a claim to verify against the action string.

A second rule: **assume default logging does not cover the new service.** Check whether the event is a management event or a data event, and confirm the data-event selector exists before an incident.

### Verification status

The specific finding is a vendor-research report relayed by a newsletter. No independent test is recorded here.

Confidence: `[TENTATIVE]` — one researcher's report. The policy behaviour should be re-tested against the current AWS policy version before it is written into a control document. `[NEEDS VERIFICATION 2026-11-10]`

## Snippets

> "AWS's AWSCompromisedKeyQuarantineV3 policy fails to block LLM inference through the newer bedrock-mantle service, which uses bedrock-mantle:CreateInference instead of the blocked bedrock:InvokeModel action." [Source: newsletter-rss-tldrsec-2026-11-05-tldr-sec-353---a-thousand-fewer-paths-to-root-ku.md]

> "Daniel makes a good point regarding AWS' deny list approach not being ideal here, as it's reactive by design and AWS keeps shipping new surfaces, so there'll be exposure until the policy catches up with new features." [Source: newsletter-rss-tldrsec-2026-11-05-tldr-sec-353---a-thousand-fewer-paths-to-root-ku.md]
