---
title: Agent Setup-Instruction Supply Chain
type: concept
tags: [concept, security, agents, k173]
keywords: [README, pip, npm, supply-chain, coding-agent]
related:
  - sources/arxiv-2607.15143-setup-instruction-weaponization.md
  - sources/substack-rss-secpro-2026-07-17-243-entrepreneurial-adversary.md
  - entities/tools/kimi-cli.md
  - sources/newsletter-rss-latent-space-2026-07-18-ainews-not-much-happened.md
maturity: draft
created: 2026-07-18
updated: 2026-07-18
---

## Relations

- @sources/arxiv-2607.15143-setup-instruction-weaponization.md
- @sources/substack-rss-secpro-2026-07-17-243-entrepreneurial-adversary.md

## Raw Concept

How AI coding agents turn project docs into install-time code execution without verifying package names, registries, or known vulns.

## Narrative

Attack surface: edit README / requirements / Makefile → redirect to untrusted registry, vulnerable pin, or typo-squat. Mitigations for Cemini/TipDrop/CCC: allowlist registries, pin hashes, refuse blind install from untrusted repos, require human gate on new deps, prefer lockfiles + `npm audit`/`pip-audit` before agent install steps.
