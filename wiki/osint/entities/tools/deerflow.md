---
title: "DeerFlow — ByteDance Long-Horizon SuperAgent Harness"
type: entity
tags: [tool, agent-orchestration, sandbox, docker, research-automation]
keywords: [DeerFlow, ByteDance, superagent, Docker sandbox, multi-agent, orchestration, MIT]
related:
  - sources/project-link-evaluation-brief.md
  - concepts/tool-evaluation-framework.md
maturity: draft
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@sources/project-link-evaluation-brief.md` — source evaluation brief (URL 1)

## Raw Concept

DeerFlow 2.0 is ByteDance's open-source orchestration harness for deploying autonomous AI sub-agents in isolated Docker sandboxes for long-horizon, high-complexity tasks.

- **Repo**: `github.com/bytedance/deer-flow`
- **License**: MIT
- **Stack**: Docker Desktop, Python, sandbox-based agent execution
- **Footprint**: 4 vCPU, 8 GB RAM minimum (16 GB recommended)

## Narrative

DeerFlow provides an orchestration layer that gives AI agents isolated computational environments via Docker sandboxes, with persistent memory, tool access, skill definitions, subagent dispatch, and a central message gateway. Unlike conversational agents that merely generate text, DeerFlow agents execute long-horizon research and coding tasks in sandboxed environments.

### Integration vectors

- **Workflow (Steal-from)**: The architectural patterns — organizing agent capabilities as isolated skill files, orchestrating through a central message gateway, and using sandboxed execution for safety — should be extracted and applied to the local Claude Code research workflow.
- **Cemini prod (No)**: The Hetzner host operates at 7 GB RAM with 40 Docker containers. Adding DeerFlow's 8-16 GB requirement is physically impossible.
- **Wiki server (No)**: CPX21 at 4 GB RAM falls drastically below the 8 GB minimum.

### Steal-from specifics

Extract these patterns without deploying the full harness:
1. **Skill-as-file architecture**: Agent capabilities defined as isolated, composable Markdown skill files
2. **Sandbox discipline**: Research and code execution in Docker boundaries with explicit tool gating
3. **Message gateway pattern**: Central routing layer for multi-agent communication

### Risks

- **Transitive dependency audit**: The extensive Python dependency tree must be audited for AGPL/SSPL contamination before any code patterns are ported to production
- **State synchronization**: Async memory queue has been observed to stutter during rapid operations, causing context fragmentation

[Source: Project Link Evaluation Brief.docx, URL 1]
