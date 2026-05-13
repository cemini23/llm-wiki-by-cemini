---
title: claude-obsidian — Markdown-vault autoresearch loop (DO NOT ADOPT — parallel-impl confirmed)
type: entity
tags: [tool, claude-code, obsidian, markdown-vault, autoresearch, do-not-adopt, parallel-impl-confirmed, dead-end]
keywords: [claude-obsidian, obsidian, markdown vault, autoresearch, contradiction flag, librarian, claude-mem, hook-collision]
related:
  - sources/evaluating-urls-cemini-project-2026-05-13.md
  - concepts/tool-evaluation-framework.md
  - entities/tools/claude-mem.md
maturity: draft
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- `@sources/evaluating-urls-cemini-project-2026-05-13.md` — origin source (Doc 1, K42), Adopt-tier
- `@concepts/tool-evaluation-framework.md` — methodology
- `@entities/tools/claude-mem.md` — **parallel-impl risk**: claude-mem (v13.0.1, Phase-2 PASS 2026-05-12) already adopted laptop-side for session-memory; claude-obsidian's autoresearch + `[!contradiction]` syntax overlaps partially

## Raw Concept

Stub created from Doc 1 K42 eval (2026-05-13). Adopt-tier; cross-routed to OSINT (3-round autoresearch loop) + Cybersec (`[!contradiction]` syntax for pentest report cross-ref).

## Narrative

- **Eval claim**: `/autoresearch` 3-round autonomous loop integrated into Obsidian markdown vault; `[!contradiction]` syntax for cross-referencing conflicting reports.
- **Use case**: continuous threat-actor profiling (OSINT) or pentest report contradiction surfacing (Cybersec).
- **Parallel-impl decision required**: claude-mem covers session memory (semantic injection, observation indexing). claude-obsidian appears to target vault-side reasoning across markdown documents — different scope, potentially additive rather than substitutive.

### Phase-0 audit (COMPLETE 2026-05-13) — Verdict: DO NOT ADOPT

**Repo verified**: `github.com/AgriciDaniel/claude-obsidian` (MIT)

| Load-bearing question | Finding |
|------------------------|---------|
| License | MIT verified |
| Vault scope | Obsidian-vault-only (Obsidian-Desktop required) — does NOT work on plain markdown trees |
| Nesting respect | Partial; designed around Obsidian's flat-folder convention; nested entity subdirectories not first-class |
| 3-round autoresearch cost | Unbounded per-query; no cost cap; would compete with K37 reviewer-agent and K39 verbalized-sampling for budget |
| `[!contradiction]` syntax | **CONFLICTS** with Cemini's `[NEEDS VERIFICATION YYYY-MM-DD]` convention; 200+ existing wiki files would need migration |
| Hook overlap | **COLLISION CONFIRMED**: SessionStart hook collides with already-adopted claude-mem v13.0.1 SessionStart hook; both write to the same hook surface; coexistence non-trivial |

### Dead Ends — why this was rejected

**Decision date**: 2026-05-13
**Decision**: DO NOT ADOPT
**Brief**: NOT WARRANTED (this Dead Ends entry replaces a full adoption brief)

**Root cause of rejection**: parallel-implementation with claude-mem v13.0.1 (already in production laptop-side as of K38, Phase-2 PASS 2026-05-12). The two tools target overlapping problem surfaces:

| Surface | claude-mem v13.0.1 (adopted) | claude-obsidian (rejected) |
|---------|-------------------------------|-----------------------------|
| Session memory | ✅ semantic injection + observation indexing | ✅ autoresearch loop |
| Markdown vault scope | works on any directory tree | Obsidian-Desktop required |
| SessionStart hook | ✅ owns this surface | would collide |
| Contradiction marker | uses Cemini's `[NEEDS VERIFICATION YYYY-MM-DD]` | uses `[!contradiction]` (would force 200+ file migration) |
| Cost discipline | bounded by session-context | unbounded autoresearch |

**Specific failure modes documented**:

1. **Hook collision**: SessionStart hook is single-handler-per-surface. Adopting both would require hook-chaining work that doesn't exist upstream. claude-mem wins by being adopted first and passing Phase 2.
2. **Obsidian-Desktop lock-in**: Cemini wiki is intentionally Obsidian-free (Markdown + YAML frontmatter + git; rendered by kb-server REST API on Hetzner). Adopting Obsidian-Desktop as a runtime dependency reintroduces a GUI requirement we deliberately avoided.
3. **`[!contradiction]` migration cost**: 200+ existing wiki files use `[NEEDS VERIFICATION YYYY-MM-DD]` convention; migration is the work that motivates the adoption, not the prize from it.
4. **3-round autoresearch redundancy**: K37 reviewer-agent + K37 trajectory triage + K39 verbalized sampling already provide inference-time + post-hoc quality envelope at the Conductor layer. Adding autoresearch at the vault layer doesn't compose with the Conductor stack.

**What we'd revisit this for**: if upstream claude-obsidian (a) decouples from Obsidian-Desktop, (b) adopts `[NEEDS VERIFICATION YYYY-MM-DD]` style or makes the contradiction-marker configurable, AND (c) provides a hook-chaining strategy for SessionStart coexistence, this decision should be re-opened. None of those are on the upstream roadmap as of 2026-05-13.

[Source: Evaluating URLs for Cemini Project.docx (retrieved 2026-05-13); github.com/AgriciDaniel/claude-obsidian Phase-0 audit (2026-05-13)]
