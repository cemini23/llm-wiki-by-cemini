---
title: "Probabilistic agent policy verification — arXiv 2606.20510"
type: source
tags: [source, arxiv, verifier, security, agents, k125]
keywords: [2606.20510, Datalog, probabilistic verification, reference monitor, distributionally robust, agent safety]
related:
  - concepts/probabilistic-agent-policy-verification.md
  - concepts/generator-verifier-inference-time-steering.md
  - sources/arxiv-veritas-visual-verification-2606.18247-2026-06-18.md
  - concepts/code-as-agent-harness.md
  - concepts/devfun-poker-agent-challenge-2026.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/llm-agent-systems.md
maturity: draft
read_status: read
created: 2026-06-21
updated: 2026-06-21
clusters: [llm-agents, security]
---

## Relations

- @concepts/probabilistic-agent-policy-verification.md — K125 synthesis
- @concepts/generator-verifier-inference-time-steering.md — VERITAS/K123 sibling (inference steering vs trajectory risk bounds)
- @sources/arxiv-veritas-visual-verification-2606.18247-2026-06-18.md — generator-verifier cluster

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Efficient and Sound Probabilistic Verification for AI Agents |
| **Authors** | Alaia Solko-Breslin, Pramod Kaushik Mudrakarta, Mihai Christodorescu, Somesh Jha, Krishnamurthy Dj Dvijotham |
| **Affiliation** | Google DeepMind / Google / UPenn / UW–Madison |
| **arXiv** | 2606.20510 (18 Jun 2026) |
| **sha256** | `ebd8fdac70d30bdf54cefaa373180691840cbffe370703a92e6fcaadca63847c` |
| **Repo** | none public at ingest |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.20510-2606-20510v1-efficient-and-sound-probabilistic-v.pdf` |
| **Retrieved** | 2026-06-21 (daily digest inbox) |
| **Read status** | read (abstract + §3 derivation graph + DRO framing) |

## Narrative

Extends **reference-monitor** agent defenses from deterministic Datalog policies to **probabilistic predicates** (e.g., PII detectors with per-call error rates). Prior threshold-on-marginal approaches discard correlation structure across multi-step trajectories; this work compiles execution traces into a **derivation graph** (Propagate / Merge / Declassify / CreateClean / CreateTainted transitions) and computes a **sound upper bound** on global unsafe-state probability via **distributionally robust optimization** — valid even when predicate failures are correlated.

**Reported gains [TENTATIVE — paper claims]:** on terminal and tool-calling agent benchmarks, improves security–utility trade-off vs deterministic monitors and prior probabilistic baselines while preserving rigorous violation-probability bounds.

**Cemini posture:** **REFERENCE / steal-from pattern** — poker analog: treat legality oracle + axis gates + MC equity as **noisy predicates**; bound cumulative **exploitability / policy-violation risk** over a hand trajectory before Arena submit (complements K123 Best-of-N pointwise verifier). No public code → Phase-0 REFERENCE only.

## Snippets

> "We address this by introducing a sound and efficient framework for such verification based on distributionally robust optimization, computing sound upper bounds on the probability of policy violation regardless of possible correlations between predicates." [Source: arXiv:2606.20510 abstract (retrieved 2026-06-21)]

> "Probabilistic verification must preserve this context … the monitor should evaluate the current trajectory … to compute a conservative upper bound on the global probability of the agent entering an unsafe state." [Source: arXiv:2606.20510 §1 (retrieved 2026-06-21)]

## Dead Ends

- Datalog / terminal taint semantics ≠ poker action grammar — steal is **trajectory-level conservative risk bound**, not literal Datalog install.
- Google © paper — no OSS license to Adopt until code ships.
