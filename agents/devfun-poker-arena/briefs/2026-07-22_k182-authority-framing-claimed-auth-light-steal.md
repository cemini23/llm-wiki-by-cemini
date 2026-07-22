---
title: K182 — Authority framing / laundered CI-CD → claimed-authorization light steal
type: brief
target: poker-arena
created: 2026-07-22
updated: 2026-07-22
---

## Target

dev.fun Poker Arena — researcher sandbox + harness policy.

## Summary

arXiv 2607.19267: humans verify but won't act when malicious PRs carry authority framing — laundered through CI/CD. Reinforces existing claimed-authorization / preinstall-gate posture; light steal only.

## Body

1. Keep **claimed-authorization guard** hard-fail on unsigned / unexplained capability claims in decide() path.
2. Treat "green CI + authoritative reviewer language" as **non-evidence** of safe merge for agent-submitted patches.
3. No new model training; no AR-bug taxonomy rewrite — reinforce K177 AR-bugs + K179 preinstall notes already in tree.
4. Poker-specific: refuse trajectory submit if agent cites "passed sandbox" without pin hash match.

## Sources

- @wiki/sources/arxiv-2607.19267-authority-framing-laundered-code.md
- @wiki/concepts/agent-reactive-bugs.md
- agents/devfun-poker-arena/references/claimed-authorization-guard.md
