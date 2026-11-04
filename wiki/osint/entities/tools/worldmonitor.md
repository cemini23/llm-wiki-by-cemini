---
title: "World Monitor (AGPL)"
type: entity
tags: [entity, tool, k182, k220, watch]
keywords: [worldmonitor, agpl-3-0, k182, k220]
related:
  - concepts/wiki-tooling-evaluation.md
  - sources/eval-url-revenue-opportunity-analysis-2026-07-22.md
  - sources/eval-url-revenue-cyber-agent-harness-2026-08-03.md
  - concepts/k261-eval-github-wave.md
  - sources/eval-multi-wiki-stack-revenue-2026-09-15.md
  - sources/eval-multi-wiki-repository-revenue-2026-11-04.md
maturity: draft
created: 2026-07-22
updated: 2026-11-04
harness_verb: FILE
wire_status: wont_wire
---

## Relations

- @concepts/wiki-tooling-evaluation.md — AGPL Watch
- @sources/eval-url-revenue-opportunity-analysis-2026-07-22.md — K182 eval
- @sources/eval-url-revenue-cyber-agent-harness-2026-08-03.md — K220 reaffirm Context/Watch
- @concepts/k261-eval-github-wave.md — K261 AGPL Watch reaffirm
- @sources/eval-multi-wiki-stack-revenue-2026-09-15.md — K261 eval; no re-clone

## Raw Concept

Phase-0 K182 Watch. Repo: https://github.com/koala73/worldmonitor

## Narrative

| Field | Value |
|-------|-------|
| **License** | AGPL-3.0 `[CONFIRMED]` (LICENSE file; gh API may show NOASSERTION) |
| **Tier** | Watch / Context |
| **Local** | `.local/adopts/(removed AGPL)` — do not re-clone |
| **Note** | K182 Integrate overturned — AGPL product NO-GO. **K220 reaffirm** (2026-08-03): still Watch; weak GuruWatcher news-feed hypothesis only — no Integrate. **K261 reaffirm** (2026-09-15): AGPL-3.0 Watch; **no re-clone.** Extract-only. |

### Fourth evaluation — 2026-11-04, and what is new

`@sources/eval-multi-wiki-repository-revenue-2026-11-04.md` URL 13 rates it **Extract** and routes it to GuruWatcher and pm-canary. This is the **fourth** time this repository has been evaluated: K182, K220, K261, now here. Each time the verdict lands on AGPL-3.0, no-bundle, weak feed hypothesis only.

**Two things this pass adds that the earlier ones did not have.**

**1. The licence line in the report is wrong in the permissive direction.** It says "AGPL-3.0 for non-commercial use; commercial license required for commercial SaaS or rebranding." The README says the opposite: *"Commercial use is permitted under the AGPL when you comply with its copyleft and source-availability terms."* A separate commercial or trademark agreement covers **private proprietary use or official branding**, not commercial use as such.

The verdict does not change — AGPL-3.0-only still means never bundle it. But the reason sharpens: it is not *licence-blocked*, it is **consume-as-an-external-service**.

**2. The MCP tools cost money to call.** The report presents a 100-tool MCP server. Phase-0:

| Surface | Access |
|---------|--------|
| `tools/list` | **Public**, no key |
| Running the app | No environment variables needed |
| **`tools/call`** | **Requires `X-WorldMonitor-Key` or OAuth**; keys at `worldmonitor.app/pro` |
| Feature data sources | "May require credentials" |

So the catalogue is free and the data is not. **Every prior evaluation of this repo assumed a free feed.** That assumption is now retired, and it is the first concrete reason the GuruWatcher hypothesis has stayed weak for four passes.

**Recommendation: stop re-evaluating this.** If a future batch surfaces it again, the answer is in this section. The only thing that would change it is a decision to pay for a key and test the churnpoint/FRED endpoints against what GuruWatcher already consumes.
