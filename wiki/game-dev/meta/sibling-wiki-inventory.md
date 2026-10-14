---
title: Sibling wiki inventory — castle-sim cross-links
type: concept
tags: [meta, federation, routing, inventory]
keywords: [ccc-wiki, image-gen-wiki, cybersecurity-wiki, cross-wiki, castle-sim]
related:
  - concepts/game-dev-wiki-scope.md
  - meta/cross-wiki-routing.md
  - concepts/art-pipeline-v0-requirements.md
  - concepts/agent-harness-castle-project.md
  - entities/projects/castle-sim.md
  - sources/exa-deep-research-batch-2026-06-13.md
maturity: validated
created: 2026-06-13
updated: 2026-06-15
---

## Relations

- @concepts/game-dev-wiki-scope.md — boundary rules
- @ccc-wiki/index.md — harness primary
- @image-gen-wiki/index.md — art pipeline primary
- @cybersecurity-wiki/index.md — agent/MCP security
- @osint-wiki/concepts/game-dev-wiki-federation.md — federation hub

## Raw Concept

Curated map of sibling wikis for the castle-sim hobby project — what to pull, what stays elsewhere, and known gaps. Scanned 2026-06-13.

## Narrative

### Summary

| Wiki | ~Pages | Castle-sim relevance | Linked from game-dev? |
|------|--------|----------------------|------------------------|
| **game-dev-wiki** | 56+ | Primary home + AI gamedev workflows/tools | — |
| **ccc-wiki** | ~349 | Agent harness, subagents, verification gates | Partial (3 pages) |
| **image-gen-wiki** | ~264 | ComfyUI, LoRA, GPU — no game-art recipes yet | Index only |
| **cybersecurity-wiki** | ~500 | MCP/skill security when swarms go live | **None** |
| **osint-wiki** | Large | Federation sync, eval surface 8 (game-dev) | Yes (K115) |

---

### @ccc-wiki — use early (W2 harness)

| Page | Why for castle-sim |
|------|-------------------|
| @ccc-wiki/concepts/subagent-orchestration.md | When/how to delegate Codex per subsystem |
| @ccc-wiki/entities/tools/claude-code-game-studios.md | Planner → implementer → reviewer role graph |
| @ccc-wiki/concepts/ship-subagent-writer-reviewer-tester.md | Parallel writer + tester → reviewer → human gate |
| @ccc-wiki/concepts/agent-completion-verification-gates.md | “Done” = tests + lint + playtest artifact |
| @ccc-wiki/entities/patterns/scatter-gather.md | Fan-out for multi-file Godot features |
| @ccc-wiki/concepts/code-as-agent-harness.md | Interface / mechanisms / verification layers |
| @ccc-wiki/concepts/skill-vetting.md | Phase-0 before installing game-dev skills |
| @ccc-wiki/concepts/deep-research-evaluation-prompt.md | Eval surface 8 = game-dev primary fit |
| @ccc-wiki/entities/skills/cursor-audit.md | Multi-model review; Fable withdrawal note |

**Gap:** Wire ship-subagent + verification-gates into `@concepts/agent-harness-castle-project.md` before first Codex swarm on `castle-sim`. General patterns now in `@concepts/ai-assisted-game-dev-workflows.md`.

---

### @image-gen-wiki — use for placeholder art (W3)

| Page | Why for castle-sim |
|------|-------------------|
| @image-gen-wiki/entities/uis/comfyui.md | Node-graph T2I for tiles/sprites |
| @image-gen-wiki/runbooks/zimage-setup-runbook.md | Local Mac-friendly ComfyUI setup |
| @image-gen-wiki/runbooks/runpod-comfyui-setup.md | Cloud GPU when batch-generating tile sheets |
| @image-gen-wiki/concepts/two-pass-generation-workflow.md | Composition + detail for building sprites |
| @image-gen-wiki/concepts/lora-taxonomy.md | Style-consistent tile sets |
| @image-gen-wiki/entities/hardware/gpu-guide.md | VRAM budget for batch gen |

**Gap:** No isometric tile, Godot `TileSet`, or spritesheet pages in **either** wiki. Bridge spec: `@concepts/art-pipeline-v0-requirements.md`.

---

### @cybersecurity-wiki — use when agents get tools (W2+)

| Page | Why for castle-sim |
|------|-------------------|
| @cybersecurity-wiki/concepts/mcp-security-posture.md | MCP admission before game-dev MCP servers |
| @cybersecurity-wiki/concepts/agent-skill-injection.md | Malicious SKILL.md when pulling community skills |
| @cybersecurity-wiki/concepts/agentic-containment-principles.md | P1–P6 containment for autonomous runs |
| @cybersecurity-wiki/concepts/docker-agent-sandbox-allowlist-proxy.md | Sandboxed Codex with egress allowlist |
| @cybersecurity-wiki/entities/tools/defenseclaw.md | MCP/skill scanner (Apache-2.0) |

**Gap:** Add security checklist to harness before `castle-sim` gets write MCP or untrusted skills.

---

### @osint-wiki — federation only

| Page | Role |
|------|------|
| @osint-wiki/concepts/game-dev-wiki-federation.md | Scope split, ingest routing |
| @osint-wiki/concepts/federated-daily-research-digest.md | Daily digest `game-dev` wiki-id |

Operator infra — not game design.

## Snippets

> Pull harness patterns from CCC; pull art technique from image-gen; pull security from cybersec when swarms run with MCP. Never duplicate ComfyUI runbooks here — stub + link.
