---
title: "Bedrock protocol and runtime evaluation — 19 rows (2026-10-04)"
type: source
tags: [source, k281, basgiath, minecraft, protocol]
keywords: [k281, bedrock, mcpelauncher, protocol, mcp]
related:
  - concepts/k281-basgiath-wave.md
maturity: draft
created: 2026-10-04
updated: 2026-10-04
read_status: skimmed
---

## Relations

- @concepts/k281-basgiath-wave.md

## Raw Concept

| File | `Repository Revenue Opportunity Evaluation.docx` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Repository Revenue Opportunity Evaluation.docx` |
| Archive | egress-fi 2026-10-04 |
| Retrieved | 2026-10-04 |
| Dual-ID | **OSINT K281** |
| Batch theme | Bedrock protocol engineering, client runtimes, anticheat proxies, MCP automation |
| sha256 | see the archive record |

## Narrative

Nineteen rows. Almost all are `bedrock-mc/*` — a single umbrella of Bedrock protocol work.

### Tier spread

| Tier | Count |
|------|-------|
| Integrate | 1 |
| Extract | 6 |
| Context | 5 |
| Watch | 2 |
| Pass | 3 |

### The Integrate row

**`bedrock-mc/mcpelauncher-agent`.** An MCP automation layer over the Bedrock launcher. This is the row with the most leverage for Basgiath: it is the piece that would let an agent **drive a running Bedrock client headlessly** — which is what makes unattended verification of dragon-flight behaviour and entity synchrony possible without a human at the keyboard.

Pair it with the modding batch's headless container and LevelDB tooling and the shape of a test bench appears.

### The Extract rows

| Repo | Technique |
|------|-----------|
| `Daniel-Ric/Bedrock-Persona` | Persona and skin identity handling |
| `bedrock-mc/bedrock-data` | Packet and protocol data definitions — the reference index |
| `bedrock-mc/cinnabar` | Protocol layer |
| `bedrock-mc/mcbe-macos` | macOS Bedrock runtime |
| `bedrock-mc/vanilla-gen` | Vanilla world generation |
| `bedrock-mc/lens` | Inspection tooling |

`bedrock-data` is the one to read first. A packet-definition set is the substrate everything else in this list builds on.

### Watch and Context

`zuri` and `mcpelauncher-client` are Watch. The Context rows (`Void`, `libc-shim`, `game-window`, `Rust-LCE`, `protocolgen`) are architecture references — `libc-shim` in particular is a known technique for running a client without a full native toolchain.

### What was rejected

`Jenny-Mod` is Pass. **`minecraft-bedrock-hacked-client-2026-pvp-toolkit` is Pass, and nothing from it belongs in this wiki** — no technique, no configuration, no code. `php-grpc` is Pass as redundant.

### Boundary

**Zero clones. No client-modification code recorded.** The protocol work here is for our own add-on's test bench, not for attacking anyone's client. **0 product Integrate GO.**
