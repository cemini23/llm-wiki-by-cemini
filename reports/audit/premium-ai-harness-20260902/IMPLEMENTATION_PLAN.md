# Implementation plan — Phase-0/Phase-1 de-confusion + rule de-bloat

**Source:** `SYNTHESIS.md` (super-audit 2026-09-02, verdict REWORK).
**Architect:** Fable 5.1. **Implementer:** Grok via `/route` (hard lane). **Operators:** Claudio + David.
**Repos touched:** CCC (`~/Projects/Cemini claude code CCC`, `cemini23/cemini-claude-code-CCC`), OSINT (`~/Projects/OSINT WORKSPACE`, `cemini23/llm-wiki-by-cemini`). Sibling wiki repos get rule-file deletions only.

Facts the implementer must know before starting:

- `~/.cursor/rules/*.mdc` **is** loaded by Cursor in every window. Project `.cursor/rules/` copies of the same files load again → duplicate tokens. Today the 770-line `cemini-phase1-policy-wires.mdc` loads twice (global + project).
- `sync_federation_cursor_skills.sh` auto-discovers `federation: true` **only under CCC `.cursor/skills/`**. OSINT-canon skills need a `DOMAIN_SKILL_DIRS` entry (like `i-have-adhd`).
- Cybersecurity wiki keeps a project copy of `cemini-phase1-policy-wires.mdc` with an overlay (`scripts/restore_cybersec_dual_id.py` + `.cursor/rules/overlays/`). **Do not delete that one copy in Phase A.**
- Grok failure is **HTTP 402 "Grok Build usage balance exhausted"** (`~/Library/Logs/cemini-wiki-ingester.log`). It is a balance/quota problem, not a login problem.
- `ollama` is not installed. `grok` 1.0.13 is on PATH.
- wiki frontmatter today: `wire_status` = 145 `policy_wired` · 40 `wont_wire` · 8 `pending` · 2 `runtime_wired` (`entities/tools/chrome-devtools-mcp.md`, `entities/tools/mcp-legal-it.md`) · misc.

---

## Phase A — same session (implement now via `/route`)

Order matters: **1 → 2 → 3** before any prune (Conflicts note in SYNTHESIS: invariants first, then prune copies).

### A1. Create `cemini-invariants.mdc`; demote the 770-line catalog

**Repo:** CCC.

1. Create `.cursor/rules/cemini-invariants.mdc` (target 35–45 lines including frontmatter). Frontmatter:

   ```yaml
   ---
   description: Cemini federation hard invariants — HITL on irreversible effects, no skill/harness auto-evolve, no prod writes, license + secrets, claim + locator
   alwaysApply: true
   ---
   ```

   Body = one `#` title, one line of intro, then **≤ 12 bullets** extracted from `cemini-phase1-policy-wires.mdc`. Each bullet ends with the source id in parentheses (arXiv id or slug, never a bare K#). Required bullets:

   - Irreversible effects (LIVE Discord, trading egress, `scp` to `cemini-prod`, `watches.json`, stash/GitHub writes): preview → confirm → pre-state → act → post-state. No phantom success. Verify-then-retry. One reservation while ambiguous. (execution-fidelity / AID-Guard)
   - Never auto-evolve `.cursor/skills/*`, `.cursor/rules/*`, prompts, or hooks. HITL before any harness self-write. Skills can get worse with practice. (2608.12851 misevolution / SHE / StarHarness / HCL)
   - Never rewrite `## Verify` or pass criteria mid-run. External eval contract is authoritative. (AutoDesign / Task-CoEvolve / AutoSciRub)
   - Gate the tool step, not only the answer. Enforcement is external and fail-closed; model self-arbitration is not a boundary. (StepGuard / external-reference-monitor / Mandato)
   - `.local/adopts/*` = REFERENCE. Runtime wire needs a `wire-ledger.yaml` entry. No `curl | sh`, no upstream `install.sh`, no HF weight downloads by default.
   - License: no clone without SPDX or LICENSE file. AGPL / GPL = extract-only; never into Atto or proprietary kits.
   - Secrets never in rules, handoffs, or free-tier models. No production private keys in agent-readable env for LIVE agents. (hardware-keystore)
   - Claim + source locator or `NO_EVIDENCE`. Never invent fields to fill a schema in durable artifacts. (Traceable Scholarship / ResidencyRL)
   - Solvers, not LLM recall, for tabular prediction, distance, containment, lifecycle order. (MultiGlobeQA / CordisBench)
   - No PoCs, jailbreak text, or attack templates in wiki or briefs.
   - `/opt/cemini` is read-only from laptops. Briefs to `/opt/cemini/briefs/` only, after HITL.
   - IDs: key rules and ledger rows by arXiv id / slug. K# is a batch label in `log.md` only.

   Last line: `Full catalog (on demand): cemini-phase1-policy-wires.mdc · canon: @ccc-wiki/concepts/phase1-adopt-wire.md · verbs: @osint-wiki/concepts/file-keep-wire-harness.md`

2. Edit `.cursor/rules/cemini-phase1-policy-wires.mdc` frontmatter only: `alwaysApply: true` → `alwaysApply: false`. Keep `description`. Do not touch the body.

3. Edit `scripts/post-commit.sh` case list: add `.cursor/rules/cemini-invariants.mdc` next to `cemini-phase1-policy-wires.mdc`.

**Verify:**

```bash
cd "/Users/claudiobarone/Projects/Cemini claude code CCC"
wc -l .cursor/rules/cemini-invariants.mdc | awk '$1<=45{print "PASS lines="$1} $1>45{print "FAIL lines="$1; exit 1}'
rg -c "^alwaysApply: true" .cursor/rules/cemini-invariants.mdc            # 1
rg -c "^alwaysApply: false" .cursor/rules/cemini-phase1-policy-wires.mdc  # 1
rg -n "cemini-invariants.mdc" scripts/post-commit.sh                       # 1 hit
```

### A2. Sync script: federation rules → `~/.cursor/rules/` only; skills still per project

**Repo:** CCC. **File:** `scripts/sync_federation_cursor_skills.sh`.

1. Add `SRC_INV_RULE="${REPO_ROOT}/.cursor/rules/cemini-invariants.mdc"` and `USER_INV_RULE="${HOME}/.cursor/rules/cemini-invariants.mdc"`.
2. In `install_workspace()`: **delete** every `copy_file "${SRC_*_RULE}" "${rules_dir}/..."` line, the `mkdir -p "${rules_dir}"`, and the `restore_cybersec_dual_id.py` call. Keep the two skill loops unchanged.
3. In `verify_workspace()`: delete the four `[[ -f "${dest}/.cursor/rules/..." ]]` checks and the `SRC_PHASE1_RULE` block. Keep skill checks.
4. User-global block: add `copy_file "${SRC_INV_RULE}" "${USER_INV_RULE}"`. **Remove** the line that writes `${HOME}/.cursor/rules/tipdrop-route-outsource.mdc` (byte-identical alias of `cemini-route-outsource.mdc`). Then `rm -f "${HOME}/.cursor/rules/tipdrop-route-outsource.mdc"` once in the script (idempotent).
5. Add flag `--prune-project-rules` (default off). When set, for each `WORKSPACES[@]` **except** `${REPO_ROOT}`: delete `.cursor/rules/{cemini-goal-skill,cemini-cursor-security-preflight,cemini-route-outsource,tipdrop-route-outsource,cemini-phase1-policy-wires}.mdc`. **Exception:** skip `cemini-phase1-policy-wires.mdc` when `${ws}` matches `*/Cybersecurity wiki`. Print one `PRUNED <ws> <file>` line per deletion.
6. Update header comment (lines 10–11): rules are user-global only; skills are per-workspace + user-global.
7. In CCC repo: `git rm .cursor/rules/tipdrop-route-outsource.mdc` (CCC keeps canon `cemini-route-outsource.mdc`). Grep CCC + agent-toolkit for `tipdrop-route-outsource` and update text references to `cemini-route-outsource`.
8. Update `.cursor/rules/cemini-federation-skill-sync.mdc` (CCC): replace "sync to all workspaces + `~/.cursor/skills/`" with: skills → all workspaces + `~/.cursor/skills/`; shared rules → `~/.cursor/rules/` **only**. Add one line: "Do not copy `cemini-*.mdc` rules into project `.cursor/rules/` (double-load)."
9. Run: `bash scripts/sync_federation_cursor_skills.sh` then `bash scripts/sync_federation_cursor_skills.sh --prune-project-rules`.
10. Commit deletions in sibling repos that track `.cursor/rules/` (OSINT, Gambling, Game Dev, Cybersecurity, Image gen, SEO, 3D printing, federation-hub). Loop:

    ```bash
    for r in "OSINT WORKSPACE" "Gambling wiki" "Game Dev wiki" "Cybersecurity wiki" "Image gen" "SEO:GEO B&M Business" "3D printing" "cemini-federation-hub"; do
      d="/Users/claudiobarone/Projects/$r"; [ -d "$d/.git" ] || continue
      git -C "$d" add -A .cursor/rules && git -C "$d" diff --cached --quiet || git -C "$d" commit -m "rules: drop federation rule copies (global-only sync, super-audit 2026-09-02)"
    done
    ```

    Push OSINT + CCC only in this session. Other repos push when their owner next commits.

**Verify:**

```bash
bash "/Users/claudiobarone/Projects/Cemini claude code CCC/scripts/sync_federation_cursor_skills.sh"   # exit 0
ls ~/.cursor/rules/cemini-invariants.mdc ~/.cursor/rules/cemini-phase1-policy-wires.mdc
test ! -f ~/.cursor/rules/tipdrop-route-outsource.mdc && echo PASS
test ! -f "/Users/claudiobarone/Projects/OSINT WORKSPACE/.cursor/rules/cemini-phase1-policy-wires.mdc" && echo PASS
test ! -f "/Users/claudiobarone/Projects/Gambling wiki/.cursor/rules/cemini-goal-skill.mdc" && echo PASS
test -f "/Users/claudiobarone/Projects/Cybersecurity wiki/.cursor/rules/cemini-phase1-policy-wires.mdc" && echo PASS  # overlay kept
test -f "/Users/claudiobarone/Projects/Gambling wiki/.cursor/skills/route/SKILL.md" && echo PASS   # skills still sync
```

### A3. OSINT alwaysApply flips

**Repo:** OSINT.

1. `.cursor/rules/osint-phase1-adopt-wires.mdc`: `alwaysApply: false` → `alwaysApply: true`. Keep description. (Note: 336 lines. Net turn cost after A2 still drops ≈ 800 lines because the 770-line duplicate and the 45-line tipdrop alias leave. Split into ≤40-line hard gates is Phase B.)
2. `.cursor/rules/osint-k246-k253-phase1-wires.mdc`: `alwaysApply: true` → `alwaysApply: false`. Replace description with:
   `OSINT K246–K253 wire index (2026-08-25 → 09-01) — wave → surface → sibling rule-file lookup table. Read when resolving a K246–K253 dual-ID or finding which repo rule wires a batch. Not policy; invariants live in cemini-invariants.mdc.`
3. `scripts/adopt_k246_k253_phase1.sh` line 26: change the echo text `(alwaysApply)` → `(on-demand index)`.
4. `.cursor/README.md` (already modified in tree): add one row for `osint-phase1-adopt-wires.mdc` (`alwaysApply: true`) and note that `cemini-*.mdc` rules now come from `~/.cursor/rules/`.

**Verify:**

```bash
cd "/Users/claudiobarone/Projects/OSINT WORKSPACE"
rg -n "^alwaysApply:" .cursor/rules/osint-phase1-adopt-wires.mdc .cursor/rules/osint-k246-k253-phase1-wires.mdc
# expect: adopt-wires → true ; k246-k253 → false
bash scripts/adopt_k246_k253_phase1.sh   # PASS
```

### A4. Wiki concept `wiki/concepts/file-keep-wire-harness.md`

**Repo:** OSINT.

Frontmatter (schema-exact):

```yaml
---
title: FILE · KEEP · WIRE — three-verb harness ingest vocabulary
type: concept
tags: [concept, workflow, harness, federation, ingest, audit]
keywords: [file-keep-wire, phase-0, phase-1, policy_wired, wire-ledger, super-audit]
related:
  - concepts/cemini-wiki-ingest-workflow.md
  - concepts/multi-wiki-eval-doc-level-vs-phase-0.md
  - concepts/harness-updating-vs-benefit-nonmonotonic.md
maturity: draft
created: 2026-09-02
updated: 2026-09-02
---
```

Sections: `## Relations` (the three `@concepts/...` + `@ccc-wiki/concepts/phase1-adopt-wire.md`), `## Raw Concept` (prompted by super-audit `reports/audit/premium-ai-harness-20260902/SYNTHESIS.md`, 5 auditors, REWORK), `## Narrative`:

- Definitions: **FILE** = wiki page exists with claim + locator (replaces `policy_wired`, `wont_wire`, `watch`). **KEEP** = a clone under `.local/adopts/` with SPDX check (replaces Phase-0 audit). **WIRE** = an executable change shipped (script / skill / hook / rule / MCP) with a `wiki/meta/wire-ledger.yaml` row (replaces Phase-1 + `runtime_wired`).
- Operator card table Old → New (copy from SYNTHESIS §Simplify).
- Daily flow: digest → triage → FILE → KEEP if clone worth it → WIRE if executable changed → one `log.md` line. Session ends FILEd or wired; "Phase-1 leftover" is forbidden.
- ID rule: arXiv id / slug in rules and ledger; K# only in `log.md`.
- Rule budget: alwaysApply = invariants only (`cemini-invariants.mdc` ≤45 lines + per-wiki hard gates); catalogs are on-demand (`alwaysApply: false` + good description); canon is the wiki page.
- Migration status table: `wire_status` value → verb (policy_wired→FILE, wont_wire→FILE, watch→FILE, extract/extract_only/reference→KEEP, runtime_wired/integrate→WIRE, pending/deferred→must close).

`## Snippets`: one YAML ledger row example. `## Dead Ends`: "27 duplicate K# ids (K237 ×7) forced dual-ID footnotes across 5 rule files — a symptom of keying by batch label."

Backlinks (bidirectional rule):

- Add `- concepts/file-keep-wire-harness.md` to `related:` of the three OSINT pages above; bump their `updated: 2026-09-02`.
- CCC `wiki/concepts/phase1-adopt-wire.md`: add `@osint-wiki/concepts/file-keep-wire-harness.md` in `## Relations` and one Narrative line "Vocabulary simplified to FILE / KEEP / WIRE 2026-09-02"; bump `updated`.
- `wiki/index.md`: add row under concepts:
  `- [FILE · KEEP · WIRE — three-verb harness ingest vocabulary](concepts/file-keep-wire-harness.md) — \`[DRAFT 2026-09-02]\` Replaces Phase-0/Phase-1/policy_wired vocabulary; ledger contract. — concept, workflow, harness, federation`

**Verify:**

```bash
cd "/Users/claudiobarone/Projects/OSINT WORKSPACE"
python3 scripts/wiki_lint.py 2>&1 | tail -5     # no new orphan / bidirectional / dangling for file-keep-wire-harness
rg -c "file-keep-wire-harness" wiki/index.md    # 1
```

### A5. `wiki/meta/wire-ledger.yaml` stub + `scripts/wire_ledger_check.py`

**Repo:** OSINT. PyYAML 6.0.2 is installed (`python3 -c "import yaml"`).

1. Create `wiki/meta/wire-ledger.yaml`:

   ```yaml
   # WIRE ledger — every executable harness change. Key by slug; arXiv id optional.
   # Check: python3 scripts/wire_ledger_check.py
   version: 1
   updated: 2026-09-02
   repos:
     osint: /Users/claudiobarone/Projects/OSINT WORKSPACE
     ccc: /Users/claudiobarone/Projects/Cemini claude code CCC
     home: /Users/claudiobarone
   wires:
     - id: cemini-invariants-rule
       verb: WIRE
       kind: rule
       repo: ccc
       path: .cursor/rules/cemini-invariants.mdc
       wiki_page: "@ccc-wiki/concepts/phase1-adopt-wire.md"
       since: 2026-09-02
       verify: "rg -c '^alwaysApply: true' .cursor/rules/cemini-invariants.mdc"
     - id: federation-rules-global-only
       verb: WIRE
       kind: script
       repo: ccc
       path: scripts/sync_federation_cursor_skills.sh
       wiki_page: "@osint-wiki/concepts/file-keep-wire-harness.md"
       since: 2026-09-02
       verify: "bash scripts/sync_federation_cursor_skills.sh"
     - id: step-gate-pretooluse-hook
       arxiv: "StepGuard"
       verb: WIRE
       kind: hook
       repo: osint
       path: scripts/claude_pretooluse_step_gate.py
       wiki_page: "@ccc-wiki/concepts/phase1-adopt-wire.md"
       since: 2026-08-31
       verify: "python3 scripts/claude_pretooluse_step_gate.py --help"
     - id: scout-tool-search-bm25
       verb: WIRE
       kind: script
       repo: osint
       path: scripts/scout_tool_search.py
       wiki_page: "@ccc-wiki/concepts/phase1-adopt-wire.md"
       since: 2026-08-31
       verify: "python3 scripts/scout_tool_search.py --help"
     - id: aid-guard-commit
       verb: WIRE
       kind: script
       repo: osint
       path: scripts/aid_guard_commit.py
       wiki_page: "@ccc-wiki/concepts/phase1-adopt-wire.md"
       since: 2026-08-25
       verify: "python3 scripts/aid_guard_commit.py selftest"
     - id: chrome-devtools-mcp
       verb: WIRE
       kind: mcp
       repo: osint
       path: .cursor/mcp.json
       wiki_page: entities/tools/chrome-devtools-mcp.md
       since: 2026-09-02
       verify: "rg -c chrome-devtools .cursor/mcp.json"
     - id: mcp-legal-it
       verb: WIRE
       kind: mcp
       repo: osint
       path: .cursor/mcp.json
       wiki_page: entities/tools/mcp-legal-it.md
       since: 2026-09-02
       verify: "rg -c legal .cursor/mcp.json"
   ```

   Implementer: before writing the last two rows, run `rg -n "^wire_target:" wiki/entities/tools/chrome-devtools-mcp.md wiki/entities/tools/mcp-legal-it.md` and set `path` to the real target the page names. If the page names no executable path, set `path: wiki-only` and `verb: FILE` and downgrade that page's `wire_status` to `policy_wired` (it was never a runtime wire). Also verify the three `scripts/*.py` paths exist before listing them (`ls scripts/claude_pretooluse_step_gate.py scripts/scout_tool_search.py scripts/aid_guard_commit.py`); drop any row whose path is missing.

2. Create `scripts/wire_ledger_check.py` (stdlib + `yaml`, imports at top, ≤150 lines):

   - `--ledger` (default `wiki/meta/wire-ledger.yaml`), `--selftest`, `--quiet`.
   - Checks: (a) YAML parses, `version == 1`, `wires` is a list; (b) `id` unique, slug regex `^[a-z0-9][a-z0-9-]+$`, no `^k\d+` bare-K ids; (c) `verb ∈ {WIRE}` in this file (FILE/KEEP rows are rejected — they belong in the wiki); (d) `kind ∈ {rule,script,skill,hook,mcp}`; (e) `repo` key exists in `repos`; `repos[repo]/path` exists unless `path == wiki-only`; (f) `wiki_page` exists — local paths resolve under `wiki/`, `@osint-wiki/...` → `wiki/`, `@ccc-wiki/...` → CCC `wiki/`; (g) **coverage**: every `wiki/**/*.md` with `wire_status: runtime_wired` or `wire_status: integrate` must appear as a `wiki_page` in the ledger; (h) `since` is ISO date.
   - `--selftest`: write a temp ledger with one good row + one bad row (missing path, bare K id) to `tempfile`, assert PASS then FAIL. No repo writes.
   - Output: `PASS wires=N` or `FAIL` + one line per finding. Exit 0 / 1.
   - Does **not** execute `verify:` commands (that is `--run-verify`, Phase B).

3. Add one line to `CLAUDE.md` § Lint: "`python3 scripts/wire_ledger_check.py` — every `runtime_wired` page has a ledger row."

**Verify:**

```bash
cd "/Users/claudiobarone/Projects/OSINT WORKSPACE"
python3 scripts/wire_ledger_check.py --selftest   # PASS
python3 scripts/wire_ledger_check.py              # PASS wires=N
```

### A6. Federation-sync the two OSINT skills

**Repos:** OSINT (skill frontmatter) + CCC (sync script).

1. OSINT `.cursor/skills/cemini-wiki-ingest/SKILL.md` and `.cursor/skills/notebooklm-osint-bridge/SKILL.md`: add `federation: true` as the last frontmatter key (before closing `---`).
2. CCC `scripts/sync_federation_cursor_skills.sh` `DOMAIN_SKILL_DIRS`: append
   `"cemini-wiki-ingest|${OSINT_ROOT}/.cursor/skills/cemini-wiki-ingest"` and
   `"notebooklm-osint-bridge|${OSINT_ROOT}/.cursor/skills/notebooklm-osint-bridge"`.
   Update the `case` skip list in `discover_federation_skills()` and the echo line "Domain skills: …" to list all four.
3. Re-run the sync script.

**Verify:**

```bash
ls ~/.cursor/skills/cemini-wiki-ingest/SKILL.md ~/.cursor/skills/notebooklm-osint-bridge/SKILL.md
ls "/Users/claudiobarone/Projects/Cemini claude code CCC/.cursor/skills/cemini-wiki-ingest/SKILL.md"
cursor-security-preflight --quick   # no CRITICAL
```

### A7. ROADMAP + `wiki/log.md`

**Repo:** OSINT.

1. `ROADMAP.md` — insert above `## Current state (2026-09-02 — K254)`:

   ```markdown
   ## Current state (2026-09-02 — super-audit AI harness · REWORK)

   - **Audit** — `reports/audit/premium-ai-harness-20260902/SYNTHESIS.md` (5 auditors, REWORK). Plan: `IMPLEMENTATION_PLAN.md` same folder.
   - **Rules** — `cemini-invariants.mdc` (CCC, alwaysApply) replaces the 770-line catalog in every turn; catalog demoted to on-demand. Federation `cemini-*.mdc` rules now sync to `~/.cursor/rules/` only; project copies pruned (Cybersec overlay copy kept).
   - **OSINT** — `osint-phase1-adopt-wires.mdc` alwaysApply **true** (hard gates); `osint-k246-k253-phase1-wires.mdc` on-demand index.
   - **Vocabulary** — FILE · KEEP · WIRE (`wiki/concepts/file-keep-wire-harness.md`). `wiki/meta/wire-ledger.yaml` + `scripts/wire_ledger_check.py` PASS.
   - **Grok** — failure is **HTTP 402 "Grok Build usage balance exhausted"** (balance), **not** login. `grok login` will not fix it. `com.cemini.wiki-ingester` LaunchAgent unloaded until balance restored + HITL review. `/route` mid lane falls back to Flash per rule.
   - **Open:** Ollama not installed (free 6th audit slot). GuruWatcher 53-rule collapse. OSINT hard-gate split (≤40 lines). HL funding backtest overdue.
   ```

   In the K254 block, change `Grok login for /route` → `Grok Build balance (402) for /route`.

2. `wiki/log.md` — prepend:

   ```markdown
   ## [2026-09-02] audit | super-audit AI harness → REWORK → Phase A shipped

   - **Synthesis:** `reports/audit/premium-ai-harness-20260902/SYNTHESIS.md`. ~47% rule tokens duplicate; 770-line alwaysApply catalog; 27 duplicate K# ids.
   - **CCC:** `cemini-invariants.mdc` (alwaysApply, ≤45 lines); `cemini-phase1-policy-wires.mdc` → `alwaysApply: false`; sync script rules → `~/.cursor/rules/` only + `--prune-project-rules`; `tipdrop-route-outsource.mdc` alias removed.
   - **OSINT:** adopt-wires alwaysApply true; k246-k253 index alwaysApply false; concept `file-keep-wire-harness`; `wiki/meta/wire-ledger.yaml` + `wire_ledger_check.py`; `cemini-wiki-ingest` + `notebooklm-osint-bridge` federation-synced.
   - **Grok:** 402 = Grok Build balance exhausted (not auth). wiki-ingester LaunchAgent unloaded. Operator checklist `briefs/2026-09-02_harness-operator-checklist.md`.
   - **Verify:** `wire_ledger_check.py` PASS · `wiki_lint.py` clean · sync exit 0 · preflight no CRITICAL.
   ```

**Verify:**

```bash
cd "/Users/claudiobarone/Projects/OSINT WORKSPACE"
rg -n "402" ROADMAP.md | head -3
head -3 wiki/log.md | rg "super-audit"
python3 scripts/ingest_session_gate.py
```

### A8. Operator checklist brief (Claudio + David)

**Repo:** OSINT (`briefs/` is gitignored — copy to `~/Projects/cemini-federation-hub/hub/briefs/` too so David sees it).

File: `briefs/2026-09-02_harness-operator-checklist.md`. Sections `## Target` (operators) · `## Summary` · `## Body` · `## Sources`. Body checklist:

1. **Grok (SuperGrok / Grok Build)**
   - `grok -p "ping"` → if output contains `402` or `usage balance exhausted`: top up / reset the **Grok Build** balance in the xAI console (Settings → Billing). This is not fixed by `grok login`.
   - If output is an **auth** error: `grok login` (or `export XAI_API_KEY=…`), then re-test.
   - Confirm `/usage` inside `grok` shows the plan.
   - Until balance is restored: `launchctl bootout gui/$(id -u)/com.cemini.wiki-ingester` and `mv ~/Library/LaunchAgents/com.cemini.wiki-ingester.plist{,.disabled-402-20260902}`. Re-enable only after a HITL dry run of `scripts/run_wiki_ingester_grok_cli.sh`.
   - Do not attach the 22 MCP servers to Grok CLI (keep `tradingview` disabled in `~/.grok`).
2. **Ollama (free local slot)**
   - `brew install ollama` (operator-named package, brew registry — allowed by supply-chain rule) → `brew services start ollama`.
   - `ollama pull qwen3.5` `[NEEDS VERIFICATION 2026-09-02: exact tag; fallback ollama pull qwen3-coder]`.
   - Test: `curl -s localhost:11434/api/tags | head -c 200`. Then `super-audit` Ollama slot stops skipping.
3. **Cursor**
   - Reload window. Settings → Rules: `cemini-invariants` appears once (global). No `cemini-phase1-policy-wires` in project rule lists.
   - `cursor-security-preflight --quick` → no CRITICAL.
4. **David's machine**
   - `git -C ~/Projects/Cemini\ claude\ code\ CCC pull && bash scripts/sync_federation_cursor_skills.sh --prune-project-rules`.
   - Confirm `~/.cursor/skills/cemini-wiki-ingest/SKILL.md` exists.
5. **Do not** add ChatGPT Plus / Perplexity / SuperGrok Heavy (subscription matrix).

Run `python3 scripts/skill_audit.py briefs/2026-09-02_harness-operator-checklist.md` → PASS or WARN.

### A9. Commit + push

```bash
cd "/Users/claudiobarone/Projects/Cemini claude code CCC" && git add -A .cursor/rules scripts wiki/concepts/phase1-adopt-wire.md && git commit -m "harness: cemini-invariants alwaysApply; demote phase1 catalog; federation rules global-only; OSINT ingest skills domain-sync (super-audit 2026-09-02)" && git push
cd "/Users/claudiobarone/Projects/OSINT WORKSPACE" && git add .cursor/rules .cursor/README.md .cursor/skills/cemini-wiki-ingest .cursor/skills/notebooklm-osint-bridge wiki/concepts/file-keep-wire-harness.md wiki/concepts/cemini-wiki-ingest-workflow.md wiki/concepts/multi-wiki-eval-doc-level-vs-phase-0.md wiki/concepts/harness-updating-vs-benefit-nonmonotonic.md wiki/meta/wire-ledger.yaml wiki/index.md wiki/log.md scripts/wire_ledger_check.py scripts/adopt_k246_k253_phase1.sh ROADMAP.md CLAUDE.md reports/audit/premium-ai-harness-20260902/IMPLEMENTATION_PLAN.md && git commit -m "harness: FILE/KEEP/WIRE concept + wire ledger; alwaysApply flips; super-audit REWORK Phase A" && git push
```

Do **not** `git add -A` in OSINT — the tree holds unrelated K254 / poker / audit-pack changes.

---

## Phase B — next week (list only; do not implement now)

1. **OSINT hard-gate split** — `osint-invariants.mdc` (≤40 lines: Atto PII strip, GW alert-only, AGPL/GPL isolate, no xsp/pm scp) alwaysApply; demote `osint-phase1-adopt-wires.mdc` (336 lines) to on-demand.
2. **GuruWatcher** — collapse 53 rule files → `guruwatcher-invariants.mdc` + optional `guruwatcher-levels.mdc` (SYNTHESIS fix #4).
3. **Cybersec overlay retirement** — fold `overlays/cybersec-k-dual-id.fragment.mdc` into `cemini-cybersec-k-dual-id.mdc`; delete the project copy of `cemini-phase1-policy-wires.mdc`; retire `restore_cybersec_dual_id.py`.
4. **CCC double-load** — move federation rule canon to `CCC/federation/rules/` so an open CCC folder does not load global + project copies.
5. **`wire_status` migration** — script that maps 145 `policy_wired` / 40 `wont_wire` / etc. → `verb: FILE|KEEP|WIRE` frontmatter; close 8 `pending` + 1 `deferred`; then retire `wire_status` field.
6. **Retire per-wave adopt scripts** — `adopt_k*_phase0.sh` (≈100 files) → one `scripts/adopt.sh --manifest wiki/meta/adopt-manifest.yaml`; `wire_ledger_check.py --run-verify` executes `verify:` rows.
7. **Six wiki→skills** — eval-first-rubric, last30days, pii-redact, claim-ledger, vault-dedupe, osint-catalog (skill only where a daily-use executable exists).
8. **LaunchAgent health doc** — `wiki/meta/launchagent-health.md`; fix claude-mem zod error; wiki-ingester stays off until HITL.
9. **OpenRouter free ranker** — `agent-toolkit/scripts/select-openrouter-free-model.ps1`: prefer Qwen / GLM / Kimi coding models over Nemotron 550B on easy lane.
10. **Dual-ID footnote purge** — after A1 ships, delete "Dual-ID note" paragraphs from `ccc-k*-phase1-wires.mdc` and re-key headings by arXiv id.
11. **File SYNTHESIS → wiki** — `wiki/sources/super-audit-ai-harness-2026-09-02.md` source page + `wiki/concepts/cemini-harness-rule-budget.md`.

---

## Verify block (all must pass after Phase A)

```bash
CCC="/Users/claudiobarone/Projects/Cemini claude code CCC"
OSINT="/Users/claudiobarone/Projects/OSINT WORKSPACE"

# A1 invariants + demotion
test "$(wc -l < "$CCC/.cursor/rules/cemini-invariants.mdc")" -le 45 && echo "PASS A1 size"
rg -q "^alwaysApply: true"  "$CCC/.cursor/rules/cemini-invariants.mdc"          && echo "PASS A1 alwaysApply"
rg -q "^alwaysApply: false" "$CCC/.cursor/rules/cemini-phase1-policy-wires.mdc" && echo "PASS A1 demoted"

# A2 sync global-only
bash "$CCC/scripts/sync_federation_cursor_skills.sh" >/dev/null && echo "PASS A2 sync"
test -f ~/.cursor/rules/cemini-invariants.mdc && echo "PASS A2 global rule"
test ! -f ~/.cursor/rules/tipdrop-route-outsource.mdc && echo "PASS A2 alias gone"
test ! -f "$OSINT/.cursor/rules/cemini-phase1-policy-wires.mdc" && echo "PASS A2 OSINT pruned"
test ! -f "/Users/claudiobarone/Projects/Gambling wiki/.cursor/rules/cemini-goal-skill.mdc" && echo "PASS A2 Gambling pruned"
test -f "/Users/claudiobarone/Projects/Cybersecurity wiki/.cursor/rules/cemini-phase1-policy-wires.mdc" && echo "PASS A2 cyber overlay kept"
test -f "/Users/claudiobarone/Projects/Gambling wiki/.cursor/skills/route/SKILL.md" && echo "PASS A2 skills still sync"

# A3 flips
rg -q "^alwaysApply: true"  "$OSINT/.cursor/rules/osint-phase1-adopt-wires.mdc"     && echo "PASS A3 gates on"
rg -q "^alwaysApply: false" "$OSINT/.cursor/rules/osint-k246-k253-phase1-wires.mdc" && echo "PASS A3 index off"
(cd "$OSINT" && bash scripts/adopt_k246_k253_phase1.sh >/dev/null) && echo "PASS A3 adopt script"

# A4 + A5 wiki
(cd "$OSINT" && python3 scripts/wiki_lint.py 2>&1 | rg -q "file-keep-wire-harness" && echo "FAIL A4 lint mentions page" || echo "PASS A4 lint")
rg -q "file-keep-wire-harness" "$OSINT/wiki/index.md" && echo "PASS A4 index"
(cd "$OSINT" && python3 scripts/wire_ledger_check.py --selftest >/dev/null) && echo "PASS A5 selftest"
(cd "$OSINT" && python3 scripts/wire_ledger_check.py) && echo "PASS A5 ledger"

# A6 skills
test -f ~/.cursor/skills/cemini-wiki-ingest/SKILL.md && test -f ~/.cursor/skills/notebooklm-osint-bridge/SKILL.md && echo "PASS A6"
cursor-security-preflight --quick 2>&1 | rg -q "CRITICAL" && echo "FAIL A6 preflight CRITICAL" || echo "PASS A6 preflight"

# A7 + A8
rg -q "usage balance exhausted|402" "$OSINT/ROADMAP.md" && echo "PASS A7 roadmap"
head -3 "$OSINT/wiki/log.md" | rg -q "super-audit" && echo "PASS A7 log"
(cd "$OSINT" && python3 scripts/ingest_session_gate.py) && echo "PASS A7 gate"
(cd "$OSINT" && python3 scripts/skill_audit.py briefs/2026-09-02_harness-operator-checklist.md | rg -q "PASS|WARN") && echo "PASS A8 brief"

# token budget sanity: alwaysApply lines seen in an OSINT turn (global + project)
cat ~/.cursor/rules/*.mdc "$OSINT"/.cursor/rules/*.mdc | wc -l   # expect < 1500 (was ~2500)
```

---

## NEVER

- Never auto-evolve, refine, or promote `.cursor/skills/*`, `.cursor/rules/*`, hooks, or prompts without HITL — this plan edits harness files; Grok implements exactly the listed edits and nothing more.
- Never `scp` or write to `cemini-prod:/opt/cemini/**` or `cemini-egress-fi`. No `xsp`/`pm` briefs move in this task.
- Never delete the Cybersecurity wiki copy of `cemini-phase1-policy-wires.mdc` or its `overlays/` in Phase A.
- Never edit the **body** of `cemini-phase1-policy-wires.mdc` (frontmatter flip only). Never rewrite `## Verify` sections or pass criteria.
- Never `git add -A` in OSINT; never force-push; never commit `briefs/`, `hot.md`, `.local/`, or `.wrangler/cache/`.
- Never run `grok login` as a "fix" for the 402 — it is a balance problem. Never store `XAI_API_KEY` or any secret in rules, handoffs, or the ledger.
- Never `curl | sh`, never run an upstream `install.sh`, never `pip install` / `npm i` — the only install is operator-named `brew install ollama` in the checklist (operator runs it, not the agent).
- Never post LIVE Discord. Never re-enable `com.cemini.wiki-ingester` without HITL.
- Never key a new rule, ledger row, or heading by bare K#; use arXiv id or slug.
- Never add ChatGPT Plus, Perplexity, or SuperGrok Heavy; never replace DeepSeek Flash with OpenCode in the route chain.
- Never attach the full MCP server set to Grok CLI.
