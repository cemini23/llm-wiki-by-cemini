---
title: mkcert — local trusted TLS certificates
type: entity
tags: [entity, tool, tls, k202, extract]
keywords: [mkcert, BSD-3-Clause, local CA, Atto vault]
related:
  - sources/eval-github-revenue-browser-automation-2026-07-28.md
  - concepts/gpuology-genealogy-agent-kit.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-07-28
updated: 2026-07-28
---

## Relations

- @sources/eval-github-revenue-browser-automation-2026-07-28.md — K202 Extract
- @concepts/gpuology-genealogy-agent-kit.md — vault UI HTTPS
- @concepts/wiki-tooling-evaluation.md

## Raw Concept

K202 on [FiloSottile/mkcert](https://github.com/FiloSottile/mkcert).

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `FiloSottile/mkcert` |
| **License** | **BSD-3-Clause** (`gh api` 2026-07-28) |
| **Stars** | ~59k★ |
| **Verdict** | **Extract** into Atto kit install scripts for localhost HTTPS |
| **Risk** | `rootCA-key.pem` must never sync into Access share / git |
| **Install** | `brew install mkcert` when Homebrew available |

## Snippets

> Zero-config local CA for Atto vault UI — exclude root key from share perimeter. [Source: @sources/eval-github-revenue-browser-automation-2026-07-28.md]
