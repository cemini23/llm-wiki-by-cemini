---
title: SBOM (Software Bill of Materials)
type: concept
tags: [concept, security, supply-chain, standard]
keywords: []
related:
  - sources/3-17-competition-research.md
  - sources/3-19-compliance-research.md
  - sources/3-19-ip-sale-research.md
  - sources/github-action-and-workflow-research.md
  - concepts/ip-sale-readiness.md
  - entities/security/syft.md
  - entities/security/cyclonedx.md
maturity: retracted
created: 2026-04-23
updated: 2026-04-24
---

## Relations

- @sources/3-17-competition-research.md
- @sources/3-19-compliance-research.md — the deep-read pass surfaced this source's explicit framing of automated SBOM as the cryptographic-proof deal-killer mitigation; sharpens the P1 wire-up ticket below
- @sources/3-19-ip-sale-research.md
- @sources/github-action-and-workflow-research.md
- @concepts/ip-sale-readiness.md
- @entities/security/syft.md
- @entities/security/cyclonedx.md

## Raw Concept

Synthesized across 3 source(s) in the Cemini research corpus that reference this concept directly or by equivalent terminology.

## Narrative

**[RETRACTED — 2026-04-24 Track C audit]** SBOM generation is **not implemented**. `.github/workflows/` has 4 files (`deploy.yml`, `drift_check.yml`, `pr-review.yml`, `production-smoke-test.yml`); `grep -iE "syft|cyclonedx|sbom|cosign"` → 0 hits across all four. What IS in `deploy.yml`: Trivy filesystem scan (Step 34d) + SARIF upload to GitHub Security tab — vuln scanning is adjacent to but **is not** an SBOM. No SBOM artifact upload step, no `cosign sign`, no release-attachment workflow, no `docs/SBOM*` or `sbom/` directory. Model-weight hashing: not visible in any SBOM-generation path. Ticket (**P1**): *Add Syft-generated CycloneDX SBOM to `deploy.yml`* — low-effort wire-up; cosign signing as a second ticket. High value-per-hour for IP-sale-readiness. Gap memo: `briefs/track-c-walk-results.md`.

Original claimed narrative retained below as retracted-claim-of-record.

---

A **Software Bill of Materials (SBOM)** is the structured inventory of
every component (libraries, containers, models, licenses) that makes
up a shipped software artifact. Cemini auto-generates a CycloneDX-
format SBOM with Syft on every CI build and attaches it alongside
the release binary + cosign signature.

### Why SBOMs are non-optional for Cemini
The institutional-buyer archetype for the IP-sale thesis has a
supply-chain-security team that will demand SBOMs as a due-diligence
artifact — NIST SSDF, EO 14028, and the equivalent European CRA
regulations all explicitly require them for procurement. Turning up
to the diligence call without SBOMs signals "handmade IP", which is
a de-valuation trigger.

### What's in Cemini's SBOM
- Python dependency graph via Syft's pip scanner.
- Container base-image provenance (pinned digest).
- Model-weight provenance — for whichever ML models ship in the
  release (FinBERT, TorchRL policy checkpoints, the MiniLM embedding
  model used for `wiki_search`) — with their upstream licenses noted.
  `[RETRACTED 2026-04-24]` Earlier phrasing cited "DeepSeek-R1-14B
  checkpoint hash" as a line-item; DeepSeek/Ollama are not deployed
  (see @entities/infrastructure/deepseek-r1-14b.md), so the SBOM
  model-weight row-set should not include it.
- Custom Cemini components flagged as `proprietary` with their
  own version + git-commit provenance.

## Snippets

*(populate as source stubs are deep-read.)*
