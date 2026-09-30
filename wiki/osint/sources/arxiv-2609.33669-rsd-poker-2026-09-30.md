---
title: "RSD-Poker: risk-utility certification for residual policies (2609.33669)"
type: source
tags: [source, k276, ood, certification, imperfect-information]
keywords: [k276, rsd-poker, calibration, frozen-split, FILE]
related:
  - concepts/k276-ood-stub-wave.md
maturity: draft
created: 2026-09-30
updated: 2026-09-30
read_status: skimmed
---

## Relations

- @concepts/k276-ood-stub-wave.md

## Raw Concept

| File | `arxiv-2609.33669-rsd-poker-structure-adaptive-and-shift-robust-ri.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.33669-rsd-poker-structure-adaptive-and-shift-robust-ri.pdf` |
| Archive | egress-fi 2026-09-30 |
| Retrieved | 2026-09-30 |
| Dual-ID | **OSINT K276** |
| sha256 | `e65cd89cac2d85f714fca119e7d438149965e30f08729dbacefb396dff1737de` |
| arXiv | 2609.33669 |
| Authors | Miaobo Hu, Shuhao Hu, Xiaobo Guo, Xin Wang, Bokun Wang, Peng Zhang, Daren Zha, Jun Xiao (UCAS; IIE CAS) |

## Narrative

The paper certifies a residual policy that corrects a frozen reference policy in imperfect-information games. The failure mode it names: a shared scale and a fixed subgroup split hide heterogeneous degradation. When the deployment mixture of information states changes, the split becomes fragile.

The method freezes a bank of residual candidates and scales. It learns a policy-visible partition on a separate structure split. It freezes that partition before the calibration labels are joined. Each candidate-group pair gets a weighted simultaneous upper certificate for risk and a lower certificate for utility. The final map is selected over a declared uncertainty set of deployment group proportions.

The numbers: on the 24-state fixture, empirical-zero selects alpha = 0.08 and lifts the weak-response proxy from 4.2082 to 4.2889, with 0 of 12 held-out threshold crossings. On stratified held-out states the learned-partition selector lifts weak utility from 4.4074 to 4.4936 and lowers held-out violation from 0.0215 to 0.0078. The mixture-robust variant reaches 0.0059.

The authors admit the fixture is small. Their spec says the protocol does not prove that maximum calibration utility is an unbiased population estimate. That is why they certify utility with a simultaneous lower bound.

The reusable pattern is the seal order: construct candidates, learn the partition, seal both, then join the oracle labels. That matches the commit-authority pattern we already filed in K275.

Poker as a product is retired (2026-09-13). No code URL found. No clone. Do not wire it.
