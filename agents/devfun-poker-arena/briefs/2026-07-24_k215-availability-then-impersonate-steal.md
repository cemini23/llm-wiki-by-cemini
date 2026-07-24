---
title: K215 poker steal — availability gap then identity reuse
type: brief
tags: [brief, poker, k215, steal]
created: 2026-07-24
---

## Target

dev.fun poker arena — session / auth / LIVE reconnect

## Summary

Steal drone-FL chain: knock a legitimate party offline, then reuse credentials to occupy the seat. For poker agents: treat disconnect/reconnect as a high-risk identity event — re-attest before LIVE actions resume.

## Body

1. On reconnect, re-verify session binding — do not trust join-once tokens
2. Alert if identity resumes immediately after forced disconnect
3. Do not auto-resume LIVE tables after unexplained drop

## Sources

- Cybersecurity wiki: `concepts/drone-fl-chained-deauth-impersonation.md`
- [Source: https://arxiv.org/abs/2607.20280 (retrieved 2026-07-24)]
