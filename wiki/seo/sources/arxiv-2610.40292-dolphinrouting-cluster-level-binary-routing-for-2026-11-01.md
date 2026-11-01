---
title: "DolphinRouting: cluster-level binary routing for disaggregated LLM serving"
type: source
tags: [source, arxiv, llm-serving, prefill-decode, latency]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | DolphinRouting: Cluster-Level Binary Routing for Disaggregated LLM Inference Serving |
| Authors | Yishuo Yuan et al., Nanjing University |
| arXiv | 2610.40292 |
| File | `arxiv-2610.40292-dolphinrouting-cluster-level-binary-routing-for.pdf` |
| Retrieved | 2026-11-01 |
| URL | https://arxiv.org/abs/2610.40292 |
| Read status | skimmed (abstract + intro) |

## Narrative

Prefill-decode (PD) disaggregation places the two phases of large language model (LLM) serving on separate worker pools. Prefill reads the full prompt in one compute-heavy pass and produces the first token. Its latency is the time-to-first-token (TTFT). Decode then emits one token at a time while the KV cache grows in GPU memory. Its latency is the time-per-output-token (TPOT). The paper says co-location on one GPU causes mutual interference, because prefill is compute-bound and decode is memory-bound.

The remaining choice is the path for each request under a fixed P/D allocation. A request can run both phases on a decode worker (local prefill). Or it can run prefill on a prefill worker and then decode on a decode worker (remote prefill). The path must account for prefill work, cache reuse, and decode demand. NVIDIA Dynamo exposes this choice through rules on effective input length, the effective-to-raw input-length ratio, and prefill load. The evaluated baseline uses Dynamo's length-based rule.

DolphinRouting learns the local-or-remote choice from end-to-end SLO feedback under a given P/D resource allocation. It clusters requests by raw prompt length, cache-adjusted input lengths on both worker pools, and output-length information. Offline policy search learns one binary action per cluster. Online, feature extraction, cluster assignment, and a table lookup select local or remote prefill.

The paper evaluates DolphinRouting on a real PD-disaggregated cluster with three public benchmarks, a mixed workload, and real data. Across the mixed workload and real data, DolphinRouting with k-means reduces P90 TTFT by 5.7–7.9% and P90 TPOT by 2.6–10.1% relative to Dynamo. These two ranges are single-source claims from this paper.

The same paper reports a TaiChi simulated arXiv workload at 12 requests/s. With TTFT/TPOT targets of 5 s/250 ms, aggregation and disaggregation reach SLO attainment of 97% and 42%. With targets of 16 s/60 ms, the rates are 7% and 98%. At 6 s/100 ms, they are 16% and 50%. These rates are single-source figures that this paper cites from TaiChi.

A local-SEO or digital-marketing team that calls an LLM for copy, replies, or briefs waits on TTFT and TPOT. The paper claims a cluster-level route can cut the slow tail of both times versus Dynamo when prefill and decode already sit on separate pools. It does not test marketing pages or a public content product.

## Snippets

> "We present DolphinRouting, which learns this choice from end-to-end SLO feedback under a given P/D resource allocation. Across the mixed workload and real data, DolphinRouting with k-means reduces P90 TTFT by 5.7–7.9% and P90 TPOT by 2.6–10.1% relative to Dynamo." [Source: `arxiv-2610.40292-dolphinrouting-cluster-level-binary-routing-for.pdf` p.1 (arXiv 2610.40292), retrieved 2026-11-01]
