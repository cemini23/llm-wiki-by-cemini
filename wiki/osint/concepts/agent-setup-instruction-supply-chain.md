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
  - sources/newsletter-rss-tldrsec-2026-08-13-tldr-sec-341---hugging-face-incident-black-hat-t.md
  - sources/arxiv-2608.12851-skill-misevolution-2026-08-14.md
  - concepts/skill-misevolution.md
  - concepts/self-evolving-runtime-defense.md
  - sources/substack-rss-wublock-2026-10-06-september-blockchain-tech.md
  - concepts/k283-feeds-wave.md
maturity: draft
created: 2026-07-18
updated: 2026-10-06
---

## Relations

- @sources/arxiv-2607.15143-setup-instruction-weaponization.md
- @sources/substack-rss-secpro-2026-07-17-243-entrepreneurial-adversary.md
- @sources/newsletter-rss-tldrsec-2026-08-13-tldr-sec-341---hugging-face-incident-black-hat-t.md — promptware: memory-file poisoning of coding assistants extends the install-gap model

## Raw Concept

How AI coding agents turn project docs into install-time code execution without verifying package names, registries, or known vulns.

## Narrative

Attack surface: edit README / requirements / Makefile → redirect to untrusted registry, vulnerable pin, or typo-squat. Mitigations for Cemini/TipDrop/CCC: allowlist registries, pin hashes, refuse blind install from untrusted repos, require human gate on new deps, prefer lockfiles + `npm audit`/`pip-audit` before agent install steps.

**K283 — MemTensor agent-memory compromise (2026-10-06).** A fresh case in the **agent-memory** sub-surface: `MemoryOS` 2.0.34 on **PyPI**, and the npm plugin `memtensor/memos-cloud-openclaw-plugin` (0.1.21, 0.1.23, 0.1.25) used with the OpenClaw runtime, shipped a **cross-platform Go binary that executed on load/import**. The npm plugin may also **leak prompt content**. Mitigation per SlowMist: uninstall or downgrade to known-safe versions, kill related processes, review network activity, rotate exposed credentials. The lesson for this wiki: an **agent's long-term-memory package is install-time code**, and compromise there leaks the agent's entire context, not just one tool call. [Source: @sources/substack-rss-wublock-2026-10-06-september-blockchain-tech.md]
