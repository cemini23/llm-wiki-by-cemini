---
title: "Tool Evaluation Framework — Three-Surface Architecture & Compliance Audit"
type: concept
tags: [methodology, tool-evaluation, architecture, licensing, cemini-stack]
keywords: [tool evaluation, three-surface, Cemini prod, Wiki server, Workflow, license audit, RAM footprint, integration vector]
related:
  - sources/project-link-evaluation-brief.md
  - sources/evaluating-links-trading-wiki-stacks.md
  - sources/project-link-evaluation-brief-5_10.md
  - concepts/rlhf-critic-bias.md
  - sources/rlhf-critic-bias-al-zawahreh-2026.md
  - sources/tool-evaluation-multi-wiki-audit-may-2026.md
  - sources/multi-wiki-tool-eval-v5-k113-2026-06-12.md
  - sources/multi-wiki-gemini-eval-prompt-2026-05-12.md
maturity: validated
hub: true
created: 2026-05-10
updated: 2026-06-12
---

## Relations
- `@sources/project-link-evaluation-brief.md` — first evaluation brief applying this framework
- `@sources/evaluating-links-trading-wiki-stacks.md` — second evaluation brief
- `@sources/project-link-evaluation-brief-5_10.md` — third evaluation brief
- `@concepts/rlhf-critic-bias.md` — **structural justification for Phase-0 audit discipline** (K40). The mirror failure mode of RLHF Critic Bias applies to eval briefs: when an LLM is prompted "evaluate this project for adoption," the asymmetric penalty for "I said skip and it was useful" exceeds "I said adopt and it was unfit." This is the structural reason behind K28+K30+K38's 6 mischaracterization catches. Phase-0 audit is the human-in-the-loop counterweight; the 6-category Rhetorical Catalog + 5-tell scorecard generalize to detection of formulaic LLM eval briefs.
- `@sources/rlhf-critic-bias-al-zawahreh-2026.md` — RLHF Critic Bias source (Al-Zawahreh April 2026, draft maturity, Reference/Steal-from). Follow-up brief candidate: port 5-tell scorecard into `scripts/skill_audit.py` as opt-in `--rlhf-tell-mode` flag (deferred until user-gated).
- `@sources/multi-wiki-gemini-eval-prompt-2026-05-12.md` — v2 prompt archive (7 surfaces, pre-gambling-wiki)
- `@ccc-wiki/concepts/deep-research-evaluation-prompt.md` — v1→v6 lineage; canonical copy-paste at `prompts/deep-research-multi-wiki-eval-v6-2026-05-31.md`

## Raw Concept

The three-surface evaluation methodology used across all three May 10 briefs. Each tool/repository is scored against three distinct deployment surfaces with different constraints.

## Narrative

### The three surfaces

| Surface | Host | RAM | Key constraints |
|---------|------|-----|-----------------|
| **Cemini production stack** | Hetzner AMD EPYC | 7 GB | Docker Compose, 40 containers, CPU-only, 24/7 trading uptime, IP-sale ready license required |
| **Wiki / librarian server** | Hetzner CPX21 | 4 GB | Node.js + Ollama embeddings, rsync-synced, text-compilation only |
| **Workflow** | macOS laptop | Variable | Claude Code, Obsidian, manual curation, solo developer |

### Evaluation dimensions

Each tool is scored on:

1. **Concrete integration vector** — Exact installation/configuration steps; where does it physically run?
2. **RAM / disk / compute footprint** — Does it fit within the surface's resource envelope?
3. **License compatibility** — Is it on the clean list (MIT, Apache-2.0, BSD) or reject list (AGPL, GPL-3.0, PolyForm, Commons Clause, SSPL)?
4. **Architectural fit** — Does the tool's paradigm match the surface's operational model?
5. **Security posture** — Attack surface, data egress risk, credential handling
6. **Maturity signals** — Stars, commits, release cadence, bus factor

### Verdict taxonomy

| Tier | Meaning | Action |
|------|---------|--------|
| **Adopt** | Passes all gates | Install/deploy immediately |
| **Steal-from** | Architecture passes, deployment blocked (usually RAM/license) | Extract patterns, algorithms, or design; discard binary |
| **Defer** | Passes gates but gated on external verification | Re-evaluate when gate clears |
| **Reference-only** | Valuable patterns but no integration target | Study, don't install |
| **Reject** | Fails one or more hard gates | Document reason, don't revisit without changed circumstances |

### Rejection patterns observed across 55 evaluations

1. **License poison pill** (~20% of rejections): AGPL-3.0, GPL-3.0, PolyForm, Commons Clause
2. **Kubernetes dependency** (~15%): Tool hard-requires K8s; Cemini uses Docker Compose
3. **Hardware incompatibility** (~15%): GPU requirement, RAM >7GB, VRAM
4. **Domain mismatch** (~10%): Robotics simulators, theorem provers in quant finance context
5. **Architectural mismatch** (~10%): Electron apps on headless servers, Telegram-as-storage
6. **Archived/abandoned** (~5%): Dead repos with unpatched CVEs

[Source: Project Link Evaluation Brief.docx, Evaluating Links for Trading and Wiki Stacks.docx, Project Link Evaluation Brief 5_10.docx]
