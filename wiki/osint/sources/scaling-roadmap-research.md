---
title: "Cemini Internal — Operational Blueprint & Scaling Roadmap (5-Section, 2026-02-25)"
type: source
tags: [docx, deep-read, legal-structuring, devops, infrastructure, tooling, scaling, compliance, soc2, finra, sec, trade-secrets, docker-security, rate-limiting, mlops, founder-operations, k-series]
keywords: [delaware-c-corp, florida-fintech-sandbox, trade-secret-vs-patent, sec-reg-s-p, finra-16-21-series-57, finra-15-09-wsp, soc2-type-ii, questdb-tiered-architecture, redis-acl, docker-mtls-zero-trust, trivy-sarif, microsoft-presidio-pii, terraform-opentofu, spacelift-opa, rate-limiting-algorithms, api-gateway-kong-tyk, weights-biases-mlflow, qwak-new-relic, stripe-atlas, legalon-spellbook, quickbooks-ramp, implementation-checklist]
clusters:
  - cemini-internal
  - rl-marl
  - quant-finance
related:
  - sources/3-26-b.md
  - sources/3-26-link-re-3.md
  - concepts/market-microstructure.md
  - concepts/quant-finance.md
  - concepts/rl-marl-research.md
  - concepts/ip-sale-corporate-structure.md
  - concepts/ip-sale-readiness.md
  - concepts/cryptographic-audit-trail.md
  - concepts/irc-1235-capital-gains-safe-harbor.md
  - concepts/florida-fintech-sandbox.md
  - entities/infrastructure/hetzner.md
  - entities/infrastructure/redis.md
  - concepts/scatter-gather-topology.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-04-30
---

## Relations

- @sources/3-26-b.md — sibling Cemini-internal audit (~1 month later, 2026-03-26). Scaling Roadmap is the legal+DevOps+tooling layer; 3-26-b is the agent-runtime architecture layer. Complementary: one covers *what legal structure and infrastructure*, the other covers *how the agents execute*.
- @sources/3-26-link-re-3.md — sibling Cemini-internal link-evaluation audit (~1 month later). Scaling Roadmap covers commercial/enterprise tooling (Terraform, Kong, W&B); link-re-3 covers OSS repos for the same functional areas.
- @concepts/ip-sale-corporate-structure.md — **Divergence**: this doc recommends Delaware C-Corp for IP sale; K5/K6/K7 recommend Wyoming HoldCo + Florida OpCo. The divergence is reconcilable (C-Corp = venture-backed exit path; Wyoming LLC = asset-sale exit path), but the doc doesn't acknowledge the dual-entity alternative.
- @concepts/ip-sale-readiness.md — the doc's SEC/FINRA compliance framework (Series 57, FINRA 15-09 WSP, SOC 2 Type II) fills a gap in the current IP-sale-readiness page which focuses on licensing/code, not securities-law compliance
- @concepts/cryptographic-audit-trail.md — the doc's CI/CD-as-compliance-artifact framing (Trivy SARIF → GitHub Security tab as SOC 2 evidence) extends the audit-trail concept from code/data → CI/CD pipeline
- @concepts/irc-1235-capital-gains-safe-harbor.md — the doc recommends trade secrets over patents for algorithmic IP — directly relevant to §1235's "property" definition
- @concepts/florida-fintech-sandbox.md — the doc endorses the Florida Fintech Sandbox (Ch. 559.952) as a regulatory safe harbor — cross-reference to the existing sandbox concept page
- @entities/infrastructure/hetzner.md — **Divergence**: the doc recommends QuestDB as the time-series database; K8 server probe found TimescaleDB deployed (no QuestDB container). The 128GB RAM figure in the doc matches the K8 stale-snapshot finding.
- @entities/infrastructure/redis.md — Redis ACLs + rate limiting algorithms (Sliding Window Counter, Token Bucket with Lua scripts)
- @concepts/scatter-gather-topology.md — the doc's MLOps tooling recommendations (W&B + MLflow + Qwak + New Relic) provide observability for the RL training loop that feeds the scatter-gather topology

## Raw Concept

- **Original title**: Operational Blueprint and Scaling Roadmap for AI-Driven Algorithmic Trading Architectures
- **Author(s)**: Cemini internal (comprehensive technical + legal + operational scaling blueprint)
- **Type**: DOCX — 5,812 words, 5 major sections, ~300+ works cited
- **Location**: cemini-librarian:/opt/cemini-bulk/research/Scaling Roadmap Research.docx
- **Retrieved**: 2026-04-23 (filename date; internal date ~2026-02-25 per works-cited retrieval dates)
- **Read status**: deep-read (full 5,812 words, 2026-04-30)
- **Primary cluster**: cemini-internal

## Narrative

Cemini-internal operational blueprint — the earliest of the three K10 docs (2026-02-25, predating 3-26-b and 3-26-link-re-3 by ~1 month). Five major sections spanning the full enterprise-readiness surface: legal structuring, DevOps security, infrastructure tooling, founder automation, and a prioritized 4-phase implementation checklist.

### §1 — Legal Structuring & Compliance

**Corporate formation**: Recommends **Delaware C-Corporation** over LLC — for preferred stock issuance, employee stock option pools, and VC compatibility. **Diverges from K5/K6/K7**: those audits recommend Wyoming HoldCo + Florida OpCo dual-entity. The divergence is reconcilable by exit path (C-Corp = venture-backed raise-and-scale; Wyoming LLC = asset-sale to single acquirer), but the doc doesn't acknowledge the dual-entity alternative.

**IP protection**: Recommends **Trade Secret** over Patent for algorithmic IP — patents require public disclosure of RL reward functions and are difficult to obtain for "abstract mathematical algorithms" post-Alice. Trade secrets require Zero Trust access controls, no single developer with full stack access, and rigorous NDA/IP-assignment contracts. **Aligned with K5/K6/K7**: all three audits converge on trade-secret-as-primary-IP-vehicle.

**SEC/FINRA compliance** (strongest section, fills wiki gaps):
- **FINRA Regulatory Notice 16-21**: any person designing/modifying algorithmic trading strategies for equities must register as a Securities Trader, passing the **Series 57** exam. Even off-the-shelf algorithm monitors must be registered.
- **FINRA Regulatory Notice 15-09**: firms must implement Written Supervisory Procedures (WSPs) + cross-disciplinary risk committees. The CI/CD pipeline becomes a legally discoverable compliance artifact.
- **SEC Regulation S-P**: written policies for protecting customer PII.
- **FINRA Rule 4370**: Business Continuity Plans for ransomware/DoS.
- **SOC 2 Type II**: mandatory for institutional client onboarding. Type II = operational effectiveness over 3-12 months (vs Type I = single-point-in-time design). Five Trust Services Criteria: Security (mandatory), Availability, Processing Integrity, Confidentiality, Privacy.

### §2 — Technical Scaling & DevOps Security

**Database tiering**: Recommends **QuestDB** as the exclusive time-series store (raw tick data, OHLCV, macro streams) + **PostgreSQL** for relational state (accounts, portfolios, compliance logs) + **Redis** as connective tissue (cache, message broker, rate limiter). **Divergence**: K8 server probe found TimescaleDB deployed, not QuestDB. The doc's argument for QuestDB is ingestion latency + native SAMPLE BY SQL extension for on-the-fly time bucketing.

**Docker Zero Trust**: Three-tier network segmentation — Edge/DMZ (API gateways), Application (ingestors + RL models), Data (databases). mTLS for all inter-service communication. Redis ACLs: disable default user, per-microservice credentials with command-scoped permissions (e.g., rate-limiter gets only +INCR +EXPIRE).

**CI/CD as compliance gate**: Trivy (container CVE scanning → SARIF → GitHub Security tab as SOC 2 evidence) + Microsoft Presidio (NLP-based PII/API-key detection in commits → block merges per SEC Reg S-P). GitHub branch protections mandate passing scans + human peer review (FINRA Rule 3110).

### §3 — AI/Infrastructure Tooling

**IaC**: Terraform/OpenTofu + Spacelift (OPA-governed deployment orchestration). **Rate limiting**: Sliding Window Counter (general-purpose external APIs) vs Token Bucket (bursty traffic at market open), both Redis-backed with Lua scripts. **API Gateway**: Kong (NGINX/Lua, sub-ms latency) or Tyk (Go, lighter footprint) over Apigee (Java, heavy). **MLOps**: W&B (RL training tracking — epsilon decay, cumulative returns, WandbCallback for Stable Baselines3/RLlib) + MLflow (model/artifact versioning) + Qwak (production drift detection) + New Relic AI (full-stack MCP-trace observability).

### §4 — Founder Automation

Stripe Atlas (Delaware C-Corp formation + bank account), LegalOn/Spellbook (AI contract review), QuickBooks + Ramp (AI expense management), Gatekeeper (vendor lifecycle), GitHub Copilot (code generation) + Panto AI (SOC 2 compliance checking at PR) + Mintlify (auto-generated documentation).

### §5 — Prioritized Implementation Checklist (4 phases, 60+ days)

| Phase | Timeline | Key actions |
|---|---|---|
| 1: Legal Scaffolding | Immediate | Stripe Atlas → Delaware C-Corp; Florida Fintech Sandbox application; QuickBooks+Ramp+Gatekeeper |
| 2: Infrastructure Security | Days 15-30 | Terraform+Spacelift; Docker 3-tier networking + mTLS; Redis ACLs; Trivy+Presidio in CI/CD |
| 3: Data & ML Pipeline | Days 30-60 | Redis rate limiter; W&B+MLflow integration; QuestDB SAMPLE BY optimization |
| 4: Scaling & Observability | Days 60+ | Kong/Tyk API Gateway; New Relic+Qwak monitoring; AI legal assistants |

### Prescribed-vs-deployed divergence notes

| Component | Doc prescribes | K8 actual (2026-04-28) | Gap |
|---|---|---|---|
| Time-series DB | QuestDB | TimescaleDB (deployed) | Different engine; both PostgreSQL-wire-compatible |
| Corporate structure | Delaware C-Corp | Wyoming HoldCo + Florida OpCo (per K5/K6/K7) | Different exit-path assumption |
| RAM | 128 GB (matches stale snapshot) | 7 GB (K8 probe) | ~18× overstatement |
| Redis ACLs | Per-service credentials, default user off | Unknown (K8 didn't probe Redis config) | Likely not configured |
| CI/CD security scanning | Trivy + Presidio in GitHub Actions | Unknown | Likely not configured |
| MLOps (W&B/MLflow) | Integrated into RL training loop | Not deployed (per K8 container manifest) | Prescribed, not built |
| API Gateway (Kong/Tyk) | Deployed for internal routing + external exposure | Not deployed (per K8 container manifest) | Prescribed, not built |

### Cross-K-series timeline

This is the **earliest** of the three K10 docs (2026-02-25), predating 3-26-b and 3-26-link-re-3 (both 2026-03-26) by one month. The three docs form a layered architecture:
1. **Scaling Roadmap** (Feb 25) = legal + infrastructure + tooling layer
2. **3-26-b** (Mar 26) = agent-runtime architecture layer (mobile HITL, hybrid routing, circuit breakers)
3. **3-26-link-re-3** (Mar 26) = 9-repo integration evaluation layer

Together, they span the full Cemini enterprise-readiness surface. The Feb→Mar progression reflects increasing specificity: from "what tools should we use?" (Feb) → "how should we architect the agent runtime?" (Mar) → "which specific OSS repos fill integration gaps?" (Mar).

## Snippets

> "Traditional intellectual property mechanisms often fail when applied to abstract algorithms and predictive models. While patents provide a twenty-year monopoly on an invention, they require the public disclosure of the invention's exact mechanics and underlying logic. Furthermore, under recent judicial doctrines regarding abstract ideas, pure mathematical algorithms and artificial intelligence models are notoriously difficult to patent. Consequently, Trade Secret protection is the optimal legal vehicle for predictive trading models, reinforcement learning reward functions, and algorithmic execution logic." [Source: Scaling Roadmap Research.docx §1]

> "FINRA Regulatory Notice 16-21 mandates that any associated person primarily responsible for the design, development, or significant modification of an algorithmic trading strategy relating to equity, preferred, or convertible debt securities must register as a Securities Trader, passing the Series 57 examination. Even if an algorithm is purchased off-the-shelf and not significantly modified, the personnel responsible for monitoring its performance must be registered. This regulatory reality dictates that the engineering team cannot operate in a vacuum; their code commits carry direct legal liability." [Source: Scaling Roadmap Research.docx §1]

> "Unlike a Type I report, which evaluates the design of security controls at a single point in time, a Type II report measures the operational effectiveness of those security controls over a continuous observation period, typically ranging from three to twelve months. [...] Preparing for SOC 2 Type II compliance must begin at the architectural inception of the platform." [Source: Scaling Roadmap Research.docx §1]

> "A pervasive architectural vulnerability in scaling containerized environments is the reliance on flat network topologies, where all Docker containers can communicate freely with one another. In a financial environment, this architecture violates the principle of least privilege; if a public-facing API container is compromised, the attacker gains unrestricted lateral movement to the underlying databases." [Source: Scaling Roadmap Research.docx §2]

> "Unlike traditional deterministic software, reinforcement learning models do not fail via immediate stack traces or syntax errors; they fail silently through performance degradation, concept drift, and reward hacking over time. Specialized Machine Learning Operations (MLOps) observability tools are absolutely mandatory." [Source: Scaling Roadmap Research.docx §3]

> "The CI/CD pipeline effectively becomes a legally discoverable compliance artifact, requiring auditable trails of peer reviews, automated testing, and risk assessments." [Source: Scaling Roadmap Research.docx §1]

> "The yfinance library relies on undocumented web scraping of Yahoo Finance; it was not designed for high-frequency use and is highly susceptible to aggressive rate limiting and sudden API structure changes. It should be reserved strictly for non-critical batch processing and historical backfilling." [Source: Scaling Roadmap Research.docx §3]
