---
title: "apktool-mcp-server — Android Reverse Engineering via MCP"
type: entity
tags: [security, android, reverse-engineering, mcp-server, apktool, apache, adopted-tier, laptop-only]
keywords: [apktool-mcp, android-re, smali, mcp-server, mobile-analysis, apk-decompile]
related:
  - sources/multi-wiki-tool-evaluation-v3.md
maturity: draft
created: 2026-05-14
updated: 2026-05-14
---

## Relations
- @cybersecurity-wiki/entities/apktool-mcp-server.md  (cross-wiki stub)

- @sources/multi-wiki-tool-evaluation-v3.md — v3 batch eval: Adopt tier, Cybersec wiki primary fit

## Raw Concept

From the Cemini Multi-Wiki Link Evaluation Report v3 (May 2026). Apache-2.0 licensed v3.0.1, independently audited by MseeP.ai. Wraps Apktool functionality (decode_apk, get_smali_file, modify_smali_file) inside an MCP server for Claude Code-native Android reverse engineering.

## Narrative

apktool-mcp-server eliminates context-window copying overhead for Android analysis by exposing Apktool operations as MCP tools. Claude Code can autonomously decode APKs, modify smali code, manage resources, and rebuild APKs — all within the agent loop.

**Tier: Adopt** — Apache-2.0, safe for IP perimeter. Cross-wiki routing: register this MCP server in CCC wiki's central SKILL.md spec for native Android RE workflows.

**NEEDS VERIFICATION:** Reliability of `build_apk()` when LLM-driven modifications introduce smali syntax errors during compilation.
