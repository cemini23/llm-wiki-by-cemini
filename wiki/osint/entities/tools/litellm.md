---
title: LiteLLM — second gateway (NO-GO)
type: entity
tags: [tool, gateway, llm, k287, no-go]
keywords: [litellm, BerriAI, gateway, openai-compatible, k287]
related:
  - sources/eval-multi-repo-revenue-2026-10-09.md
maturity: draft
created: 2026-10-09
updated: 2026-10-09
phase_0_verdict: NO-GO
harness_verb: FILE
wire_status: wont_wire
wire_note: Second gateway. A local proxy already listens on 127.0.0.1 port 8791. No install.
---

## Relations

- @sources/eval-multi-repo-revenue-2026-10-09.md — K287 eval. Docx tier Integrate. Phase-0 verdict NO-GO.

## Raw Concept

K287 Phase-0 on [BerriAI/litellm](https://github.com/BerriAI/litellm). Clone path `/tmp/k287-phase0/litellm`. No install.

## Narrative

LiteLLM is an OpenAI-compatible gateway for many model APIs. It adds cost tracking, fallback, and load balancing.

### Phase-0 (2026-10-09)

| Field | Value |
|-------|-------|
| Repo | `BerriAI/litellm` |
| Stars | 60,615 |
| Last push | 2026-10-09 |
| gh api licence | **NOASSERTION** |
| File licence | MIT for code outside `enterprise/`. The `enterprise/` tree has its own licence. |
| Verdict | **NO-GO** |
| wire_status | `wont_wire` |

The docx said MIT. Do not trust that column. The API id is NOASSERTION because the repository splits the licence. The `LICENSE` file grants MIT only outside `enterprise/`.

### Policy note

A local proxy already listens on **127.0.0.1 port 8791**. The default for a second gateway is **NO-GO**. Do not install LiteLLM. Do not point Atto, GuruWatcher, or the lab at a new gateway. The existing proxy stays the only local route.

### Failure mode

A second gateway splits spend records and key handling. The enterprise directory is not the MIT grant. A combo with `open-code-review` does not change the NO-GO.

## Snippets

> "Content outside of the above mentioned directories or restrictions above is available under the MIT license as defined below." [Source: BerriAI/litellm LICENSE, gh api 2026-10-09]
