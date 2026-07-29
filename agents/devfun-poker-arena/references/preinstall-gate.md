# Pre-install gate (K179 — light steal)

**arXiv pattern:** [2607.15143](https://arxiv.org/abs/2607.15143) (coding agents compromised via README/setup install paths — typosquats, registry redirects)  
**Brief:** `briefs/2026-07-18_k179-preinstall-gate-light-steal.md`  
**Shelf date:** 2026-07-18

## Steal (pattern only)

Agent and bake sessions that run `pip install` / `npm install` from untrusted
forks or README copy-paste are a supply-chain surface. Gate installs **before**
solver/binary bake escalates. Pattern only — no new package manager.

## Rules

1. **Pin versions.** Prefer lockfiles / exact pins (`pyproject.toml`,
   `uv.lock`, exact wheel URLs). No floating `latest` for solver-adjacent deps.
2. **Allowlist registries only.** Default: official **PyPI** and **npm** hosts
   (and whatever this repo already pins). Do not add third-party indexes or
   git+https deps from untrusted forks without human GO.
3. **Never auto-approve installs** from untrusted repos in agent or bake
   sessions. Stop and ask the operator before any new install.
4. **Prebind before solver bake deps.** Treat solver binary / console_solver /
   AGPL tooling install as **Prebind-class** standing (same posture family as
   privileged intents in `references/claimed-authorization-guard.md`):
   operator/prebind confirmation first, then bake. Bake scripts do not
   auto-download untrusted packages at runtime.

## Applies to

| Surface | Examples |
|---------|----------|
| Bake / offline solver | `examples/bake_texassolver_buckets.py`, TexasSolver binary under `.local/` |
| Agent sessions | any `uv add` / `pip install` / `npm install` while iterating Arena glue |
| Optional extras | `[llm]` extras (`anthropic`, `openai`) — still pinned; still not auto-approved from forks |

## Does not apply to

- Pure local edits with existing locked deps (`uv sync` of known lockfile after human pin change is fine)
- Arena HTTP evaluate/submit (separate network allowlist: `references/network-policy.md`)

## Operator checklist

- [ ] New dep? Pin + allowlist host + human GO before install
- [ ] Solver binary path set via env / local path only — never pull from a random README URL mid-session
- [ ] Bake escalate only after prebind-class confirmation of binary + grid
- [ ] Do not weaken `pyproject.toml` pins without asking

## Related

- Bake entrypoint: `examples/bake_texassolver_buckets.py` (module docstring points here)
- Claimed authorization / prebind: `references/claimed-authorization-guard.md`
- Network allowlist: `references/network-policy.md`
- Researcher sandbox: `references/researcher-track-sandbox.md`

## Check

```bash
test -f references/preinstall-gate.md
rg -n "preinstall-gate" examples/bake_texassolver_buckets.py
```
