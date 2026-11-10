---
title: Agent Skill Libraries for Engineering — Verification-First Design
type: concept
related:
  - sources/arxiv-mechanical-engineering-skills-2611.05758.md
  - entities/tools/mechanical-engineering-skills.md
  - concepts/self-improving-cad-generation-agents.md
  - concepts/fdm-printing.md
  - sources/arxiv-2605-17448-self-improving-cad-agents.md
maturity: draft
updated: 2026-11-10
---

## Raw Concept

Opened on the 2026-11-10 ingest of @sources/arxiv-mechanical-engineering-skills-2611.05758.md. The question this page answers: when an agent does engineering work, what stops it from returning a confident wrong number?

## Narrative

An agent that writes CAD scripts, sets up simulations, and reads sensor data makes the errors an engineer cannot accept. It slips on arithmetic. It mixes units. It uses a correlation outside its range. It answers without evidence.

The Mechanical Engineering Skills library answers with a small set of rules. Each rule is a check on the agent, not a promise about the model.

| Rule | Effect |
|---|---|
| Tools compute, the model orchestrates | No consequential number comes from model arithmetic; each one comes from an executable script with declared inputs and units |
| Every result travels with its check | FEA returns with a hand calculation; a lattice returns with the exact laminate solution; a CAD edit returns with a kernel validity check |
| A failed check is reported, not hidden | The result leaves as unverified, with its inputs, assumptions, and software versions |
| Agreement between tools is not validation | Two tools that share assumptions confirm consistency only |
| Reproduction is separated from adaptation | A working implementation is not a reproduction of a paper's headline number |
| Validity limits are stated where the agent repeats them | An elastic homogenization is not crash performance; a defect classifier from one machine family is not a process qualification |

### Why the format matters more than the skills

The portable part is not the 33 skills. It is the packaging rule. A skill is a directory with a short routing description, a workflow, tested scripts, and tests. The agent loads the description always and the rest only on demand, so a large library costs little context until a task matches. That property is what makes a library of thirty tools usable in one conversation.

### Where this sits against the CAD-agent work

@sources/arxiv-2605-17448-self-improving-cad-agents.md runs a self-improving loop: propose geometry, evaluate with a solver, keep the best. That loop is one skill in this library (`llm-mechanical-designer`). The difference is scope. The CAD-agent paper optimizes a design. This library packages a breadth of methods behind one interface, with a verification rule attached to each.

### What is still open

- The authors name a controlled comparison as future work. No measured gain from the skill format exists yet. [OPEN QUESTION 2026-11-10]
- The fallback path is the risk. When a solver is missing, a skill returns an analytical estimate or rehearsal data. A user who does not read the fallback note can mistake a rehearsal for a result. [TENTATIVE]
- Whether a print farm gains from the FDM skills (`agentscad-fdm-dfam`, `image2gcode`, `lattice-inverse-design`) is untested on consumer hardware. [OPEN QUESTION 2026-11-10]

## Snippets

> "The first is that the model orchestrates while tools compute: instructions require each consequential number to come from an executable calculation with declared inputs and units, never from the model's own arithmetic" [Source: arxiv-2611.05758-mechanical-engineering-skills-an-open-library-of.pdf p.4]
