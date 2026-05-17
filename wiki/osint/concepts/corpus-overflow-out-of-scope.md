---
title: Corpus Overflow — Out-of-Scope Research Stubs
type: concept
tags: [concept, corpus-hygiene, out-of-scope, research-index, librarian-bookkeeping]
keywords: [corpus inventory, out of scope, research overflow, academic ml, hardware accelerator, mathematical foundations]
related:
  - sources/3-29-20.md
  - sources/ai-10-4-3.md
  - sources/wasertein-1-4-3.md
  - sources/counterexamples-cycle-factors.md
  - sources/leetcode-maang-prep-siagian.md
  - sources/protocol-2-3-29.md
  - sources/protocol-7-3-29.md
  - sources/3-29-4.md
  - sources/bayesuan-perspectives.md
  - sources/ligo.md
  - sources/gdelt-3-3-29.md
  - sources/crypto-4-11.md
  - sources/crypto-4-4-11.md
  - sources/crypto-5-4-11.md
  - sources/agent3.md
  - sources/agents5.md
  - sources/agents8.md
  - sources/3-29-2.md
  - sources/3-29-7.md
  - sources/3-29-14.md
  - sources/3-29-19.md
  - sources/3-29-5.md
maturity: draft
created: 2026-04-26
updated: 2026-05-16
---

## Relations

- @sources/3-29-20.md — *DVM: Real-Time Kernel Generation for Dynamic AI Models* (Fang et al., Huawei) — academic ML systems / GPU kernel codegen; not aligned with Cemini's trading-stack research agenda
- @sources/ai-10-4-3.md — *GTA: a new General Tensor Accelerator with Better Area Efficiency and Data Reuse* (Ai et al., Peking University) — academic chip architecture; outside Cemini's software-only stack scope
- @sources/wasertein-1-4-3.md — *Uniform optimal-order Wasserstein quantisation* (Gwóźdź) — pure-mathematics measure-theory paper; no foreseeable Cemini-side application path
- @sources/counterexamples-cycle-factors.md — *Counterexamples to an Extremal Conjecture for Random Cycle-Factors* (Gajjala) — pure extremal-combinatorics paper; no Cemini-side application path
- @sources/leetcode-maang-prep-siagian.md — *60 Popular LeetCode Problems & Solution for MAANG Coding Interview Preparation* (Siagian) — off-domain personal coding-interview reference; not research material for the trading stack
- @sources/protocol-2-3-29.md — *Reinforcement Learning for Quantum Processes with Memory* (Lumbreras et al., NTU Singapore) — quantum-information-theory RL; no path to classical financial-market modeling
- @sources/protocol-7-3-29.md — *Optimized Control Protocols for Stable Skyrmion Creation Using Deep RL* (Song et al., KAIST) — condensed-matter spintronics device physics; no trading-stack application path
- @sources/3-29-4.md — *A Robust and Efficient MARL Framework for Traffic Signal Control* (Huang et al., NYCU) — urban traffic-signal optimization; traffic-specific framework with no direct trading-stack transfer
- @sources/bayesuan-perspectives.md — *Some Bayesian Perspectives on Clinical Trials* (Sokolova, Sokolov, Polson) — biostatistics / Bayesian clinical-trial design; medical-trial domain with no path to financial-market modeling
- @sources/ligo.md — *Evaluating Deep Learning Models for Multiclass Classification of LIGO Gravitational Wave Glitches* (Manoharan & Cleaver, Baylor) — astrophysics detector-characterization ML; no transfer path to the trading stack
- @sources/gdelt-3-3-29.md — *Shifting Narratives: A Longitudinal Analysis of Media Trends and Public Attitudes on Homelessness* (Irudayaraj, Ye, Chainani) — media-framing / social-policy study; uses GDELT but no trading-stack application path
- @sources/crypto-4-11.md — *MARVEL: Multimodal Adaptive Reasoning-intensiVe Expand-rerank and retrievaL* (Kasem et al.) — vision-language multimodal retrieval benchmark; outside Cemini's text-only retrieval path
- @sources/crypto-4-4-11.md — *CREBench: Evaluating Large Language Models in Cryptographic Binary Reverse Engineering* (Chen, Wang, Zhou et al.) — cybersecurity-adjacent binary RE benchmark; not financial research
- @sources/crypto-5-4-11.md — *The Quantum-Cryptographic Co-evolution* (Kundu & Kompella, Cisco Research) — post-quantum-cryptography migration framework; infrastructure policy, not finance
- @sources/agent3.md — *Agent Factories for High Level Synthesis* (Bhandwaldar et al., IBM) — coding agents optimizing hardware designs (HLS); hardware-design domain with no software-only trading-stack transfer
- @sources/agents5.md — *Large Language Models as Optimization Controllers: Adaptive Continuation for SIMP Topology Optimization* (Yang et al., Santa Clara University) — LLM controller for structural/mechanical topology optimization; no trading-stack application path
- @sources/agents8.md — *Sketch2Simulation: Automating Flowsheet Generation via Multi-Agent LLMs* (Bahamdan et al., Imperial College London) — chemical process engineering flowsheet generation; no financial/OSINT transfer path
- @sources/3-29-2.md — *Hetero-Net: Energy-Efficient Resource Allocation and 3D Placement in Heterogeneous LoRa Networks via Multi-Agent Optimization* (Ahmed et al., UM6P) — IoT/telecom LPWAN network planning; no trading-stack application path
- @sources/3-29-7.md — *Safe Multi-Agent Deep RL for Privacy-Aware Edge-Device Collaborative DNN Inference* (Wang et al.) — edge-computing DNN inference offloading; no path to financial-market modeling
- @sources/3-29-14.md — *Modernising RL-Based Navigation for Embodied Semantic Scene Graph Generation* (Küble et al., University of Augsburg) — embodied-robotics navigation / computer vision; no trading-stack transfer
- @sources/3-29-19.md — *Sparton: Fast and Memory-Efficient Triton Kernel for Learned Sparse Retrieval* (Nguyen et al.) — GPU Triton-kernel systems optimization; Cemini runs no GPU inference of its own
- @sources/3-29-5.md — *COHORT: Hybrid RL for Collaborative Large DNN Inference on Multi-Robot Systems* (Anwar et al., UMBC) — multi-robot edge DNN-inference orchestration; no financial/OSINT transfer path

## Raw Concept

Hub for source stubs that were ingested during the corpus-bootstrap pass but, on D′ triage (2026-04-26), were judged **not aligned with any active Cemini research thread**. Listing them here keeps the inventory honest (we have the PDFs, we know they exist) while removing them from the lint orphan-flag without forcing them into a wrong-fit hub.

This page is **librarian bookkeeping**, not a research index. If a future Cemini-side question makes one of these load-bearing — for example, if hardware-acceleration economics become relevant to a self-hosted LLM-inference cost model — the corresponding stub should graduate to a real cluster hub and be removed from this page's `related:` list.

## Narrative

### Inclusion criteria

A source lands here if **all three** of the following hold:

1. The PDF is in `research for cemini/` (so it's part of the inventory) and the stub was created by the bootstrap first-page extract pass.
2. The cluster classifier left it as `clusters: [uncategorized]` and human (Opus) triage could not identify a thematic fit with any of the existing cluster hubs (`llm-agent-systems`, `rl-marl-research`, `ai-ethics-and-governance`, `cryptographic-audit-trail`, `kelly-cvar-risk-engine`, `ticker-watchlist`, `gdelt`, `crypto-asset-taxonomy`, `kalshi`, `langgraph`, `hetzner`, `ip-sale-readiness`).
3. There is **no foreseeable Cemini-side question** that would make the source load-bearing within the next 12 months on the current research roadmap.

If criterion (3) shifts (roadmap pivots, new thread opens), the source graduates out of this page.

### Why not just delete?

Deleting the stubs would lose the inventory record of which PDFs were already triaged-and-rejected, leading to duplicate effort on the next sweep. Keeping them under this hub is a librarian's "we looked, we passed" marker.

### Current contents (22 sources, 2026-05-16)

| Stub | Topic | Why out-of-scope |
|---|---|---|
| @sources/3-29-20.md | DVM real-time kernel generation for dynamic AI models | GPU/ML systems infrastructure; Cemini does not run model training, only API-call inference |
| @sources/ai-10-4-3.md | GTA tensor accelerator chip architecture | Hardware design; Cemini is a pure software stack on commodity Hetzner CPUs |
| @sources/wasertein-1-4-3.md | Uniform optimal-order Wasserstein quantisation (pure math) | Measure-theory foundations; no current quant-finance application path identified |
| @sources/counterexamples-cycle-factors.md | Random cycle-factor extremal conjecture counterexamples (pure math) | Extremal combinatorics / graph theory; no quant-finance or trading-stack application path |
| @sources/leetcode-maang-prep-siagian.md | 60 LeetCode problems for MAANG interview prep (Java) | Personal coding-interview reference; not a research / tool / market source |
| @sources/protocol-2-3-29.md | RL for quantum processes with memory (quantum-information theory) | Quantum-physics RL with regret bounds; no path to classical financial-market modeling |
| @sources/protocol-7-3-29.md | Deep RL for stable skyrmion creation (condensed-matter physics) | Spintronics device physics; RL applied to micromagnetic simulation, no trading-stack transfer |
| @sources/3-29-4.md | MARL framework for traffic signal control | Urban traffic-signal optimization; traffic-specific framework/action space, no direct trading transfer |
| @sources/bayesuan-perspectives.md | Bayesian analysis of three landmark clinical trials (pure biostatistics) | Medical clinical-trial design; shares Bayesian machinery but no path to financial-market modeling |
| @sources/ligo.md | Deep-learning glitch classification for LIGO gravitational-wave detectors | Astrophysics detector characterization; generic tabular ML but domain has no trading-stack transfer |
| @sources/gdelt-3-3-29.md | Media-framing analysis of homelessness coverage (GDELT + X sentiment) | Social-policy / media-framing study; uses GDELT but no quant-finance or trading-stack application path |
| @sources/crypto-4-11.md | MARVEL multimodal vision-language retrieval pipeline + benchmark | Multimodal (image+text) retrieval; Cemini's retrieval path is text-only, and the work is not finance |
| @sources/crypto-4-4-11.md | CREBench: LLM benchmark for cryptographic binary reverse engineering | Cybersecurity-adjacent (software RE / vuln discovery); not financial research, no trading-stack transfer |
| @sources/crypto-5-4-11.md | Quantum-Cryptographic Co-evolution coordinate framework (Cisco Research) | Post-quantum-cryptography migration strategy / infrastructure policy; not finance |
| @sources/agent3.md | Agent factories: general-purpose coding agents for HLS hardware optimization (IBM) | Hardware-design / High-Level-Synthesis domain; Cemini is a software-only stack with no HLS transfer |
| @sources/agents5.md | LLM as online adaptive controller for SIMP topology optimization | Structural/mechanical engineering topology optimization; no trading-stack application path |
| @sources/agents8.md | Sketch2Simulation: multi-agent LLMs converting diagrams into Aspen HYSYS flowsheets | Chemical process systems engineering; no financial/OSINT trading-stack transfer |
| @sources/3-29-2.md | Hetero-Net: multi-agent resource allocation + 3D placement in heterogeneous LoRa networks | IoT/telecom LPWAN network planning; no transfer path to financial-market modeling or OSINT |
| @sources/3-29-7.md | Safe MARL for privacy-aware edge-device collaborative DNN inference | Edge-computing DNN inference offloading; no application path to financial-market modeling |
| @sources/3-29-14.md | RL-based navigation for embodied semantic scene graph generation | Embodied-robotics navigation / computer vision; no trading-stack transfer |
| @sources/3-29-19.md | Sparton: Triton GPU kernel for the LM-head of learned sparse retrieval | GPU systems / kernel optimization; Cemini runs no GPU inference of its own |
| @sources/3-29-5.md | COHORT: hybrid RL for collaborative DNN inference on multi-robot systems | Multi-robot edge DNN-inference orchestration; no financial/OSINT transfer path |

## Snippets

*(None — bookkeeping page.)*
