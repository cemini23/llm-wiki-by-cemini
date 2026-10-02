---
title: "Global coherence: when every agent is right and the team is wrong (2610.02036)"
type: source
tags: [source, k278, agents, multi-agent, harness]
keywords: [k278, coherence, state-ownership, aliasing, FILE]
related:
  - concepts/k278-harness-wave.md
maturity: draft
created: 2026-10-02
updated: 2026-10-02
read_status: skimmed
---

## Relations

- @concepts/k278-harness-wave.md

## Raw Concept

| File | `arxiv-2610.02036-global-coherence-when-every-agent-is-right-and-t.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.02036-global-coherence-when-every-agent-is-right-and-t.pdf` |
| Archive | egress-fi 2026-10-02 |
| Retrieved | 2026-10-02 |
| sha256 | `ffdef8d4d3d26707b837ef3516cdb385694b34ceced8c0cc45111e416efd06c4` |
| Dual-ID | **OSINT K278** |
| arXiv | 2610.02036 |
| Author | Xin Heng (Tote AI) |
| Pages | 60 |

## Narrative

The paper names a failure class: every agent in a team acts correctly on its own view, and the team is still wrong. The author argues this is a **state** problem, not an intelligence problem, and that a stronger model cannot fix it.

Two failure modes are defined. **Observation aliasing** is when two worlds look identical to an agent but need different actions. **Non-gluing** is when locally consistent pieces fit into no global state. The first is bounded by an impossibility theorem. The second is described with a topological framework.

The measurements are the useful part.

| Setting | Result |
|---------|--------|
| Aliasing task, deciding event visible | 40 of 40 solved |
| Aliasing task, event hidden | Compatible with chance (1 in 3) |
| Aliasing task, one restoring sentence added | Back to 40 of 40 |
| Team budget 20 calls, plain | Overspent 5 of 5 runs |
| Same, with a visible live counter | Still overspent 4 of 5 |
| Same, with commit enforcement | 0 of 5 overspent |
| Ontology networks with invisible identity collisions | 23 of 45 |
| τ²-bench panel, committed change silently undone | Policy-checked agent 0.07, harness 1.00 |

The counter result is the sharp one. Showing the team a live count of remaining budget did **not** fix the overspend. Enforcing the commitment did. Visibility is not enforcement.

The author admits the limits. Agent evidence uses one model family on modest panels. The finite panel supports the predicted contrast but does not establish equivalence to chance. The escrow comparisons are descriptive.

**The transferable rule: the harness must own the state.** When a run goes wrong with every step looking locally correct, look for missing or unowned state before you blame the model. This is a third form of the K276 and K277 evidence finding.

No code URL. The paper states code and run records will be released. No clone.
