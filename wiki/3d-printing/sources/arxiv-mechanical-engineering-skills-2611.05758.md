---
title: "Mechanical Engineering Skills — An Open Library of Agent Skills for Design, Analysis and Manufacturing (arXiv:2611.05758)"
type: source
related:
  - entities/tools/mechanical-engineering-skills.md
  - concepts/agent-skill-libraries-mechanical-engineering.md
  - concepts/self-improving-cad-generation-agents.md
  - concepts/extrusion-control.md
maturity: draft
read_status: read
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Mechanical Engineering Skills: An Open Library of Agent Skills for Design, Analysis and Manufacturing |
| Author | Achuth Chandrasekhar, Jesse Barkley, Peter Pak, Rumi Loghmani, Aakash Oza, Amir Barati Farimani (Carnegie Mellon University) |
| Type | arXiv preprint (cs.MA) |
| Location | `research to be indexed/3d-printing/arxiv-2611.05758-mechanical-engineering-skills-an-open-library-of.pdf` |
| Retrieved | 2026-11-10 |
| File | `arxiv-2611.05758-mechanical-engineering-skills-an-open-library-of.pdf` |
| Read status | read |

## Narrative

The paper presents a library of **33 agent skills** for mechanical engineering work. Nineteen skills package published work from the Barati Farimani laboratory. Fourteen cover core engineering tasks. Each skill is a directory with a `SKILL.md` file, a `scripts/` folder, `references/`, and `tests/`.

The library installs with one command (`npx skills add BaratiLab/mechanical-engineering-skills`). It runs in Claude Code, Claude.ai, and other hosts that accept the Agent Skills format. The agent sees only a one-line description per skill until a request matches. This keeps breadth cheap: about one hundred tokens per idle skill.

### Design principles

| Principle | What it means |
|---|---|
| Model orchestrates, tools compute | Every consequential number comes from an executable calculation with declared inputs and units, never from model arithmetic |
| Every result travels with its check | An FEA run returns with a hand calculation; a lattice with the exact laminate solution; a CAD edit with a kernel validity check |
| Reproduction is kept apart from adaptation | Each skill records which parts keep the source protocol and which use a replacement model |
| Boundaries are stated in the skill | Elastic homogenization is not crash performance; a defect classifier on one machine family is not a process qualification |
| Ask few grouped inputs | Instructions name only the inputs that change the decision, with defaults for the rest |

### Five case studies with independent reruns

- Lattice homogenization agrees exactly with the analytical laminate solution.
- Rocket apogee falls within **4%** of stored OpenRocket references.
- A recovered equation fit is **nine times** more accurate than a cubic polynomial at an unseen temperature.
- A porosity-monitoring pipeline runs end to end on rehearsal data.
- Polymer process optimization runs batch by batch.

The authors state that a controlled comparison of agents **with and without** skills is left to future work. No speed or accuracy gain from the skill format is measured here. [TENTATIVE] The claim that breadth costs almost nothing rests on the token argument, not on a benchmark.

### Skills that touch FDM and additive manufacturing

| Skill | Ask | Source paper |
|---|---|---|
| `agentscad-fdm-dfam` | Make a STEP part printable: reorientation, teardrop holes, chamfers | [51] |
| `image2gcode` | Photo or sketch to printer-ready G-code for 2D and 2.5D parts | [31] |
| `lattice-inverse-design` | Target stiffness to a printable TPMS or hybrid cell with a tiled STL | [30] |
| `llm-3d-print-monitor` | Per-layer camera inspection and bounded in-print correction on Klipper printers | [9] |
| `sls-process-optimization` | Polymer SLS results to the next batch settings | [8] |
| `lpbf-defect-prediction` | Laser power and speed to keyholing, lack of fusion, or balling | [6] |
| `meltpool-geometry` | Melt-pool depth, width, length and mode | [34] |
| `thermal-porosity` | Thermal images to pore count and location per layer | [35] |
| `am-literature-rag` | Page-cited answers from a local additive-manufacturing paper library | [23] |
| `dfm-review` | Design-for-manufacture review across four process families | — |

The library falls back when a dependency is missing. A missing OpenFOAM or licensed thermodynamic database means the skill returns a validator, an analytical alternative, or rehearsal data, and it says so. This is the important limit for a print-farm user: installation copies folders, but it does not install or license the underlying solvers.

## Snippets

> "Each skill packages operating instructions, executable tools and verification procedures: the language model understands the request, selects the skill and coordinates the workflow, while deterministic tools do the computation and results are returned with the checks that support them." [Source: arxiv-2611.05758-mechanical-engineering-skills-an-open-library-of.pdf p.1]

> "A controlled comparison of agents with and without skills is left to future work." [Source: arxiv-2611.05758-mechanical-engineering-skills-an-open-library-of.pdf p.1]

> "if a check fails or cannot run, the result is reported as unverified together with its inputs, assumptions and software versions" [Source: arxiv-2611.05758-mechanical-engineering-skills-an-open-library-of.pdf p.4]
