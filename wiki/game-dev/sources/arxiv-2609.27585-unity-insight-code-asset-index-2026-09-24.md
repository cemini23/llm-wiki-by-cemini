---
title: Unity Insight — production code–asset index for LLM agents (2026-09-24)
type: source
tags: [source, arxiv, unity, harness, mcp, shelf]
keywords: [unity-insight, guid, prefab, scriptableobject, retrieval]
related:
  - concepts/ai-game-dev-tool-stack-2026.md
  - entities/tools/godot-mcp-landscape.md
  - entities/tools/hi-godot-ai.md
  - sources/inbox-arxiv-reject-batch-2026-09-24.md
  - entities/engines/godot-4.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2609.27585
maturity: validated
created: 2026-09-24
updated: 2026-09-24
---

## Raw Concept

**arXiv:2609.27585** — **Unity Insight** indexes Unity **C# + serialized assets** (prefabs, scenes, ScriptableObjects) via `.meta` GUID relationships — code-only indexes miss cross-asset gameplay edits.

## Narrative

### Godot contrast [CONFIRMED]

| Unity Insight | Godot hobby path |
|---------------|------------------|
| GUID + YAML asset graph | `.tscn` / `.tres` + UID; @entities/tools/hi-godot-ai.md scene tools |
| Production Unity repos | Fork B castle-sim — **no Unity** |

**STEAL-FROM** — MCP retrieval should span **scenes + resources**, not scripts-only (W2 hi-godot read-only hierarchy first).

### Phase-0

Paper-only — **NO-GO** Unity tool install on Godot project.

## Dead Ends

- Adopting Unity Insight inside castle-sim repo
