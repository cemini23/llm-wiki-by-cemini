# Agent-Reach Wrapper

Local OSINT intake for Agent-Reach-style social snapshots. This wrapper does **not** launch upstream Agent-Reach, import browser cookies, copy browser profiles, call live networks, or hand data to prod. It validates operator-provided JSON snapshots into local DRY_RUN output for review.

## Command

```bash
python3 -m scripts.agent_reach_wrapper \
  --snapshot fixtures/agent_reach_wrapper/benign_snapshot.json \
  --allowlist config/agent_reach_sources.example.json \
  --out .local/agent-reach-wrapper/normalized-social-items.json \
  --audit .local/agent-reach-wrapper/audit.jsonl
```

Outputs stay under `.local/agent-reach-wrapper/`:

- `normalized-social-items.json` — accepted items with provenance, hash, raw text, sanitized text, and `operator_review: true`
- `audit.jsonl` — connector, snapshot path, counts, accepted hashes, and rejected reasons without raw text or secrets

## P0 Controls

- Secret/session deny scan rejects fields such as `cookies`, `session`, `auth_token`, `bearer`, `password`, and `secret`.
- Source allowlist blocks unknown platforms, domains, redirects, and non-allowlisted authors/channels.
- Prompt-injection patterns are rejected before any text can feed wiki synthesis, briefs, or prod handoffs.
- Output paths are confined to the workspace and default to gitignored `.local/`.
- Tests cover accepted snapshots, schema validation, cookie rejection, allowlist failures, prompt-injection rejection, duplicate/empty capture handling, audit writing, and output confinement.

## Tests

```bash
python3 -m unittest scripts.tests.test_agent_reach_wrapper
```

OSINT adopts this wrapper only. Upstream Agent-Reach direct integration remains blocked.
