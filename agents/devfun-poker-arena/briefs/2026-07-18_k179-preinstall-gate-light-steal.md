---
title: K179 pre-install gate — light steal for poker agent deps
type: brief
tags: [brief, poker, supply-chain, k179]
created: 2026-07-18
---

## Target

devfun-poker-arena agent / bake sessions that install Python or Node deps

## Summary

arXiv 2607.15143: coding agents that install from README/setup docs can be compromised via typosquats and registry redirects. Poker bake that `pip install` / `npm install` from untrusted forks needs the same gate.

## Do

1. Pin versions; allowlist PyPI/npm hosts only.
2. Never auto-approve package installs from untrusted repos in agent sessions.
3. Treat install as Prebind-class before any bake escalates to solver deps.

## Sources

- https://arxiv.org/abs/2607.15143
