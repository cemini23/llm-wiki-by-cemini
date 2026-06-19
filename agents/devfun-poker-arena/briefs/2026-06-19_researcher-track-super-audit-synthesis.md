## Target

Researcher Round prep — 5-model super audit synthesis for `cemini_wiki_poker`.

## Summary

**Overall: SHIP-WITH-FIXES.** Strong 6-max leak discipline; **not positioned to win** until trajectory/multi-axis eval surface and format fork are real. Jun 25 public launch requires P0 pipeline fixes before Jun 21 beta.

## Body

### Auditor verdicts

| Slot | Channel | Role | Model | Verdict |
|------|---------|------|-------|---------|
| 1 | cursor | agentic-reasoning | claude-opus | WARN |
| 2 | cursor | code-implementation | gpt-5.4-medium | FAIL |
| 3 | cursor | third-lens | gemini-3.1-pro | WARN |
| 4 | api | api-adversarial | grok-4.3 | WARN |
| 5 | api | api-deep-reasoning | deepseek-reasoner | WARN |

Pack: `reports/audit/pack-researcher-track/`

### Strong consensus (≥4 auditors)

1. **Multi-axis eval is the prize** — trajectory + cognitive profile, not Playground chips.
2. **`axis_summary.json` is not a real M₁–M₉ scorecard yet** — must implement K122 proxies + gates.
3. **HU vs 6-max unresolved** — dual-stack or toggle required before Jun 21; HU is smoke-only today.
4. **6-max policy core is a genuine strength** — regression depth, gin v008, stack-off discipline.
5. **Do not optimize Playground rank / Eval 500h / selfplay bb/100** as Researcher targets.

### Unique high-signal findings (single auditor — still investigate)

| Topic | Auditor | Issue |
|-------|---------|-------|
| `eval_panel_mode` forced on benchmark `pokerkit run` | Slot 2 | Wrong posture for Researcher submit |
| `export_researcher_trajectory.sh --top-agents 1` | Slot 2 | May omit hero `submissions.jsonl` rows |
| Reasoning `pp` seat-parity vs correct `sk:@pos` | Slot 1 | Self-inflicted M₈ penalty |
| `return base[:150]` blind slice | Slot 1 | Breaks YAML / AGENTS.md rule |
| Inject controlled mixing for M₇ proxy | Slot 3 | Rubric-hacking vs rigid gin lane |

### Ranked P0 patch backlog (fix order)

| P | Patch | Status |
|---|-------|--------|
| P0 | Researcher runtime profile (no eval_panel, no chase, sanitize off) | **DONE** 2026-06-19 |
| P0 | Trajectory export hero + `hero_submissions` gate | **DONE** |
| P0 | M₁–M₉ proxies + gate thresholds | **DONE** (schema v2) |
| P0 | Reasoning honesty (`pp`, `vr`, no `[:150]`) | **DONE** |
| P0 | `CEMINI_TABLE_FORMAT` + HU fork (29 spots, HU chart) | **DONE** |
| P1 | `run_hu_sandbox_gate.sh` + preflight wire | **DONE** |
| P1 | F6 memory ablation harness | **DONE** (`run_researcher_memory_ablation.sh`) |
| P1 | Long-run soak + `deploys.jsonl` | **DONE** (`run_researcher_soak.sh`) |
| P1 | M₇ controlled mixing in Researcher profile | **DONE** (`researcher_mix`) |

**Remaining before submit:** pin `ARENA_RESEARCHER_COMP_ID` from `skillFile` (Jun 21); confirm whether **challenge lane** is HU vs sandbox stays 6-max; prod deploy + `AGENT_VERSION` bump **done** (`researcher-prep.8d633f3.2026-06-19`).

### Where we will do well

- Leak prevention / bust avoidance (regression corpus)
- Deterministic policy layer (PR-aligned, reproducible trajectories)
- TAG + exploit lanes vs loose sandbox field
- Trajectory **plumbing** (selfplay JSONL → export script) already exists
- Competitor steal (gin v008) already ported and gated

### HU vs 6-max decision tree (Jun 21)

| `skillFile` says | Action |
|----------------|--------|
| **6-max** | Ship current stack after P0 pipeline fixes; keep gin + seat matrix |
| **HU** | Enable HU fork; widen BTN/SB opens; 25+ HU regressions; fix button labeling |
| **Unknown / both** | `CEMINI_TABLE_FORMAT=auto` + parallel gates for 2 and 6 seats |

## Sources

- Super-audit pack `reports/audit/pack-researcher-track/`
- Premium legs `reports/audit/premium-researcher-track/`
- Wiki hub: `wiki/concepts/devfun-researcher-track-readiness-2026-06.md`
