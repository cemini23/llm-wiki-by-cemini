---
title: Genealogy App Threat Model (Gemini DR — Atto local-first / MCP / share)
type: source
tags: [source, docx, genealogy, atto, security, threat-model, mcp, k185]
keywords: [AttoVault, AES-256-GCM, STRIDE, Shai-Hulud, Cloudflare Access, SSN strip, suggest-only, GDPR household]
clusters: [k185-ingest]
related:
  - concepts/atto-local-first-threat-model.md
  - concepts/atto-macos-gtm-gumroad.md
  - concepts/gpuology-genealogy-agent-kit.md
  - sources/gemini-atto-macos-gtm-2026-07-22.md
maturity: draft
read_status: read
created: 2026-07-22
updated: 2026-07-22
---

## Relations

- @concepts/atto-local-first-threat-model.md — synthesized control checklist + privacy FAQ
- @concepts/atto-macos-gtm-gumroad.md — marketing privacy claims must match this model
- @concepts/gpuology-genealogy-agent-kit.md — vault / MCP / Cloudflare share architecture
- @sources/gemini-atto-macos-gtm-2026-07-22.md — companion GTM claims

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Threat Model and Security Architecture Analysis for Atto: A Local-First Genealogy Application |
| **Author / origin** | Gemini Deep Research (Atto threat-model prompt → inbox) |
| **Type** | Word docx |
| **Filename** | `Genealogy App Threat Model.docx` |
| **sha256** | `5d7341f7c1a036ed62140e525c8aae8e7ae2335ba3c8f14f29b70af055e94643` |
| **Size** | 36,452 bytes |
| **Retrieved** | 2026-07-22 (inbox) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Genealogy App Threat Model.docx` |
| **read_status** | read |

## Narrative

STRIDE-style threat model for Atto’s local-first posture (`~/AttoVault/`), optional Cloudflare Pages/Access share, and MCP/on-device AI. Primary shift vs SaaS: endpoint compromise, supply chain, and prompt-injected tool calls — not central cloud breach of millions.

**Actors:** snooping relative · device thief · supply-chain worm (npm/uv lifecycle hooks; Shai-Hulud-class) · malicious MCP host / intake prompt injector · inadvertent user (open Access policy; paste PII into consumer LLMs).

**Must-have controls (v1):** AES-256-GCM vault encryption; passphrase UX (15+ chars, spaces OK); strip SSN/`_PRIV` from Topola export and LLM payloads; human Approve with rotating tokens before MCP tool exec; Cloudflare Access fail-closed on custom + `*.pages.dev`; supply chain `min-release-age=7d`, `npm ci`, `--ignore-scripts`.

**Out of scope for 2-person indie:** full GDPR program (household exemption framing); immutable crypto audit of every click (attacker owns disk).

**Citation quality:** mixes NIST/Cloudflare docs with 2025–2026 worm narratives and CVE references — verify CVE IDs and Cloudflare default-policy claims before SECURITY.md hard requirements. [OPEN QUESTION 2026-07-22]

**Wiki scope:** product security checklist. Align with `atto/SECURITY.md`; no Barone vault contents.

## Snippets

> Actors: Snooping Relative · Device Thief · Supply Chain Attacker · Malicious MCP Host / Prompt Injector · Inadvertent User. [Source: Genealogy App Threat Model.docx]

> Must-Have: AES-256-GCM for ~/AttoVault/; SSN strip before LLM; human-in-the-loop MCP approval; Access fail-closed; min-release-age=7d + ignore-scripts. [Source: Genealogy App Threat Model.docx]

> Out of Scope: Full GDPR compliance program … household exemption; immutable cryptographic audit logging of every UI click. [Source: Genealogy App Threat Model.docx]

> The AI has no ability to alter your files without your direct, human confirmation. [Source: Genealogy App Threat Model.docx]
