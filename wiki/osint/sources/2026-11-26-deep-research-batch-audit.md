---
title: "Deep Research batch audit — inference serving, agent frameworks, prompt teardowns (2026-11-26)"
type: source
related:
  - concepts/agent-link-evaluation-gates-v1013.md
  - sources/2026-11-24-deep-research-link-eval-runtime-tooling.md
  - "@ccc-wiki/entities/tools/inference-optimisation-skill.md"
  - "@ccc-wiki/concepts/prompt-engineering-evidence-discipline.md"
  - "@ccc-wiki/concepts/multi-agent-framework-landscape-2026-11.md"
  - "@image-gen-wiki/entities/models/minimax-h3-pose-transfer-lora.md"
  - "@cybersecurity-wiki/concepts/indirect-prompt-injection-boundary.md"
  - "@cybersecurity-wiki/concepts/open-weight-abliterated-models-2026-11.md"
updated: 2026-11-26
---

## Raw Concept

- **Title:** Cemini Multi-Wiki Batch Audit (batch F)
- **Author:** Deep Research evaluation run, v10.13 gates
- **Type:** mixed evaluation report — 12 URLs plus 8 uploaded prompt screenshots
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/osint/Cemini Multi-Wiki Batch Audit.docx`
- **Retrieved:** 2026-11-26
- **Pages:** 20 items
- **Read status:** read

Batch theme: local LLM inference engines and serving-speed hill-climbing, abliterated
multimodal checkpoints, multi-agent orchestration and memory frameworks, web-platform
standards and paid scraping MCPs, territorially encumbered diffusion LoRAs, and
prompt-engineering teardowns.

## Narrative

Twenty items: twelve URLs and eight uploaded prompt screenshots. Three earned a tier
above Context.

### Graded outcomes

| Tier | Count | Items |
|------|-------|-------|
| Integrate | 1 | `AtomicChat/Inkling-2-Mini-Uncensored-GGUF` |
| Extract | 2 | `sybil-solutions/inference-optimisation-skill`, Image 8 (Self-Improving Loop) |
| Context | 6 | `modern-web-guidance`, `crewAI`, `smolagents`, `agno`, `letta`, Image 1–3, Image 6 |
| Watch | 2 | `magnitude`, `oxylabs/web-api-mcp` |
| Pass | 1 | `microsoft/autogen` |
| UNAVAILABLE | 1 | `osinttools.beacon.host` |

The eight screenshots are prompt teardowns. None is a product; the report reads them
for reusable prompt mechanics. Five of the eight are cropped below the interesting
part, which caps what can be learned from them.

### The UNAVAILABLE verdict is wrong for the third batch running

The report grades `osinttools.beacon.host` UNAVAILABLE and skips it.

Direct checks on 2026-11-26 return **HTTP 200**. [CONFIRMED]

That is the third consecutive batch with a false UNAVAILABLE verdict — four in the
2026-11-17 batch, one in 2026-11-24, one here. The pattern is now established, and Gate
0 in @concepts/agent-link-evaluation-gates-v1013.md exists to catch it.

### Phase-0 results

| Item | Licence | Cloud | Gap check | Verdict |
|------|---------|-------|-----------|---------|
| `Inkling-2-Mini GGUF` | Apache-2.0 | local | `local-abliterated-lab` **absent** | **blocked** |
| `inference-optimisation-skill` | MIT [CONFIRMED] | local only | collectibles has no bench harness | **survives** |
| Image 8 (Self-Improving Loop) | prompt, not code | local | `local-abliterated-lab` **absent** | **blocked** |

Two of three winners have no project to enter. The lab repository does not exist on
this machine, so the gap cannot be checked and the tier cannot be acted on.

### The licensing trap

`supermansundies/Minimax-H3-Image-Pose-Transfer-Lora` lists **apache-2.0** on its
adapter card. The adapter is useless without its base model,
`MiniMaxAI/MiniMax-H3-Image`, whose Community License **excludes the United States,
the European Union, the United Kingdom, and South Korea** without a written waiver.

A permissive adapter over a territorially restricted base is not permissive. This is
the cleanest example yet of why Gate 1 must check the whole dependency chain, not the
artifact that happens to carry the licence line. See
@image-gen-wiki/entities/models/minimax-h3-pose-transfer-lora.md.

### Licence notes

MIT: `inference-optimisation-skill`, `crewAI`. Apache-2.0: `magnitude`, `smolagents`,
`agno`, `letta`, `AtomicChat` GGUF. `autogen` is MIT and graded Pass.
`oxylabs/web-api-mcp` is a paid commercial service — Watch only.

## Snippets

> Adapter card claims apache-2.0, HOWEVER required base model MiniMaxAI/MiniMax-H3-Image
> Community License explicitly excludes the United States, European Union, United
> Kingdom, and South Korea.
> [Source: Cemini Multi-Wiki Batch Audit.docx, URL 11]

> Direct navigation to https://osinttools.beacon.host returned an inaccessible response.
> [Source: Cemini Multi-Wiki Batch Audit.docx, URL 1 — contradicted by HTTP 200 on
> 2026-11-26]

## Dead Ends

- **Trusting an UNAVAILABLE verdict.** Three batches, six false verdicts.
- **Reading a licence off the artifact you plan to ship.** Check the base model too.
- **Queueing items whose target repository does not exist.** Two winners here have no
  destination.
