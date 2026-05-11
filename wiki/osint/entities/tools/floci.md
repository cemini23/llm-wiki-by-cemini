---
title: "Floci — LocalStack-Replacement AWS Emulator (REJECTED — Domain Mismatch)"
type: entity
tags: [tool, rejected, domain-mismatch, aws-emulator, localstack-replacement, graalvm]
keywords: [Floci, LocalStack replacement, AWS emulator, GraalVM native, 46 AWS services, S3, DynamoDB, Lambda]
related:
  - sources/evaluating-code-for-trading-stacks.md
  - concepts/tool-evaluation-framework.md
maturity: validated
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@sources/evaluating-code-for-trading-stacks.md` — source evaluation brief (URL 16)

## Raw Concept

Open-source ultra-fast local infrastructure emulator — drop-in replacement for the sunsetting LocalStack Community edition. GraalVM native binary in a Docker image, emulates 46 AWS services (S3, DynamoDB, Lambda, RDS, MSK, EKS). ~24 ms startup, ~13 MiB idle.

- **Repo**: `github.com/floci-io/floci`
- **License**: not verified — irrelevant given domain mismatch
- **Stack**: GraalVM native binary, Docker
- **Services emulated**: 46 (S3, DynamoDB, Lambda, RDS, MSK, EKS, etc.)
- **Port**: 4566 (mirrors AWS endpoints exactly, zero SDK modifications required)

## Narrative

**Recommendation: REJECT. Domain mismatch — solves a problem Cemini deliberately doesn't have.**

Cemini infrastructure intentionally rejected AWS-native architectures (DynamoDB, Elasticsearch, etc.) in favor of straightforward Hetzner bare-metal Linux + raw PostgreSQL + standard Redis. The Python stack does not use `boto3` or AWS CLI anywhere.

### Three-surface fit

- **Cemini prod (❌)**: zero `boto3`/AWS-CLI surface. Floci's purpose is irrelevant.
- **Wiki server**: same — no AWS dependencies anywhere.
- **Workflow laptop**: no AWS dev surface.

### Why blocking (engineering merit acknowledged)

Floci is objectively well-engineered (24 ms startup, 13 MiB idle, 46-service coverage). But the architectural mismatch is structural: adding a comprehensive AWS emulator introduces massive internal routing complexity + abstraction for zero operational benefit on a deliberately bare-metal stack.

### Secondary risk

Floci's "real mode" features (k3s, Redpanda for Kafka, real PostgreSQL for RDS) consume gigabytes of memory in sidecar containers — would annihilate the 7 GB EPYC envelope if accidentally enabled.

### Status

**Closed.** No further verification required. Rejection is on fundamental architectural choice (Hetzner bare-metal vs cloud-native), not missing technical data.

[Source: Evaluating Code for Trading Stacks.docx, URL 16]
