---
title: "K294 skipped — no lane for these inbox PDFs"
type: source
related:
  - concepts/k294-osint-wave.md
maturity: draft
read_status: skimmed
updated: 2026-10-23
---

## Raw Concept

Type: reject record for inbox PDFs with no Cemini lane
arXiv: 2610.27395, 2610.30863, 2610.29477, 2610.31427, 2610.28589, 2610.30043, 2610.28610, 2610.30114, 2610.30072, 2610.31158
Inbox basenames (all archived under osint):
- `arxiv-2610.27395-counting-who-counts-black-women-mathematicians-i.pdf`
- `arxiv-2610.30863-cross-spectral-feature-fusion-for-multispectral.pdf`
- `arxiv-2610.29477-tenetbench-a-clause-anchored-russian-corpus-for.pdf`
- `arxiv-2610.31427-fastharness-experience-driven-review-scheduling.pdf`
- `arxiv-2610.28589-agenticroborl-bringing-coding-agent-post-trainin.pdf`
- `arxiv-2610.30043-tarsphere-a-robot-oriented-full-stack-framework.pdf`
- `arxiv-2610.28610-interwebcoder-learning-interactive-webpage-gener.pdf`
- `arxiv-2610.30114-the-end-of-consensus-research.pdf`
- `arxiv-2610.30072-charts-as-epistemic-actions-for-experience-drive.pdf`
- `arxiv-2610.31158-beyond-watching-and-searching-benchmarking-agent.pdf`

Location: `cemini-egress-fi:/opt/cemini-bulk/research/osint/<basename>`
Retrieved: 2026-10-23
Read status: skimmed (title and abstract only)

## Narrative

These PDFs are in the inbox because the digest query is global and the inbox is per domain. They do not get a concept page.

| arXiv | Why |
|---|---|
| 2610.27395 | Dataset of 147 Black women with US doctorates in the mathematical sciences. No market, harness, or safety method. |
| 2610.30863 | Multispectral document binarization. Best reported mean F1 is 0.7916. No lane. |
| 2610.29477 | TenetBench. Russian professional codes. 11 of 14 model settings produce conflicting content on most such requests. No Cemini code to wire. |
| 2610.31427 | FastHarness. A robot vision-language-action review scheduler. Not a coding-agent harness. Success 80% to 97.19%. Reviewer tokens -57.2%. Episode time 85.5 to 52.0 minutes. Do not wire the name. |
| 2610.28589 | AgenticRoboRL. A robot planner. 18.1% to 71.0% on LIBERO-PRO, near Codex with memory at 72.1%. Not this stack. |
| 2610.30043 | TARSphere. A robot simulator. 360 episodes, 30 scenes. Not this stack. |
| 2610.28610 | InterWebCoder. Interactive webpage generation. A 9B model scores 48.54 and 48.42. Not local SEO. |
| 2610.30114 | A-GREEMENT. Geo-replicated consensus for a key-value store. Not a prediction market. Mean latency -12.2% on write-heavy and -33.3% on read-heavy versus the fastest baseline. Do not wire the word consensus to Kalshi. |
| 2610.30072 | ChartMind. Charts as steps inside a data agent. The abstract gives no headline percent. Agents can read a chart and still not choose to draw one. |
| 2610.31158 | OmniDR-Bench. Video-centered research reports. 50 tasks across 19 subcategories and 6,414 criteria. The best of 18 agent configurations scores 63.3 of 100. Presentation averages 81.8. Content averages 45.4. Citation averages 47.8. Not a finance, harness, or safety decision. Do not clone the paper's code repository. |

Filing the ids here makes the next preingest call them duplicates. **No install. No trade.**
