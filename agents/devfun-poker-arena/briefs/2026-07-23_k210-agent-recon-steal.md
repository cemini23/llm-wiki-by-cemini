---
title: K210 poker steal — recon before exploit in multi-agent verify
type: brief
tags: [brief, poker, k210, steal]
created: 2026-07-23
---

## Target

dev.fun poker arena — multi-agent / verifier chains

## Summary

Steal KYA lesson: profile the agent (tools, policies, defenses) before crafting attacks. Single-shot payload mutation underperforms recon-driven loops by up to 67pp ASR in paper domain — same shape for opponent-model / tool-schema probing.

## Body

1. Before expensive solver calls, recon available tools and failure modes
2. Do not assume static opponent policy — update profile between streets
3. Minimize gratuitous capability disclosure in agent tool descriptions

## Sources

- Cybersecurity wiki: `concepts/agent-reconnaissance-ipi-pentesting.md`
- [Source: https://arxiv.org/abs/2607.19837 (retrieved 2026-07-23)]
