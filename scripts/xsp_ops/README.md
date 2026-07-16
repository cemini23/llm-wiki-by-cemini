# XSP Ops Loop MVP

Cemini-native ops loop: **Macro Charts sensor → `.local` JSON brain → filesystem work queue → 7 thin CLI roles**.

No Notion. No Linear. No Robinhood. Packets never auto-write under `briefs/` or `wiki/`.

## Paths

| Path | Role |
|------|------|
| `.local/ops/xsp/state/brain.json` | Pull audit, parsed/landed sets |
| `.local/ops/xsp/state/posts/<slug>.json` | Per-post structured record |
| `.local/ops/xsp/queue/{pending,running,done,failed}/` | Work queue |
| `.local/ops/xsp/packets/` | Staging markdown packets |
| `.local/ops/xsp/events/` | Scale/escalate events |
| `~/Library/Logs/cemini-xsp-ops.log` | Orchestrator log |

## CLI roles

```bash
# Preferred entry
python3 scripts/xsp_ops/cli.py <role> [--dry-run]

# Or with scripts/ on PYTHONPATH
python3 -m xsp_ops.cli <role> [--dry-run]
```

| Role | What it does |
|------|----------------|
| `sensor` | Macro Charts RSS via `substack_rss_poller.poll_all(feed_id="macrocharts")`. Dry-run skips network; still appends brain `pull_log` with `dry_run=true`. |
| `parse` | Scan `research to be indexed/` for `macro-charts-*.md` / `substack-rss-macrocharts-*.md`; emit structured signals + regime tags. |
| `land` | Write `state/posts/<slug>.json`; update brain `post_ids` / `known_paths`. |
| `enqueue` | For landed posts without a queue job → `queue/pending/<slug>.json`. |
| `triage` | pending→running; rule-based XSP keywords → `priority` + `action` (`packet`\|`skip`\|`watch`); →done. |
| `packet` | For `action=packet` without a packet file → `.local/ops/xsp/packets/YYYY-MM-DD_<slug>.md`. |
| `scale` | If pending ≥ `XSP_OPS_SCALE_PENDING` (default 5) or failed ≥ 1 → event JSON + Discord or macOS notify. |
| `loop` | Run roles 1→7 in order; propagates `--dry-run`. |

## Orchestrator shell

```bash
bash scripts/run_xsp_ops_loop.sh
bash scripts/run_xsp_ops_loop.sh --dry-run
```

Log: `~/Library/Logs/cemini-xsp-ops.log`

## Human promote ritual (packets → briefs)

Packets are **staging only**. After human review:

1. Open `.local/ops/xsp/packets/YYYY-MM-DD_<slug>.md`
2. Confirm XSP relevance / edit Summary + Body
3. **Manually** copy to `briefs/xsp-YYYY-MM-DD_<slug>.md` (never auto)
4. Route via normal post_ingest / CeminiSuite brief workflow

Do **not** `scp` packets directly; do **not** invent wiki pages from packets without an ingest decision.

## Env

| Variable | Default | Meaning |
|----------|---------|---------|
| `XSP_OPS_SCALE_PENDING` | `5` | Pending queue size that triggers escalate |
| `XSP_OPS_ROOT` | (unset) | Override ops root (tests) |

Discord uses existing `intel.core.discord` / `cemini_discord_notify` webhook resolution. If no webhook: macOS `osascript` notification.

## LaunchAgent (optional — Cursor wires after green)

Do **not** edit `install_workflow_launchagents.sh` in the Grok MVP pass.

Suggested agent:

- **Label:** `com.cemini.xsp-ops-loop`
- **StartInterval:** `3600`
- **ProgramArguments:** `bash`, `/path/to/scripts/run_xsp_ops_loop.sh`

## Tests

```bash
python3 -m pytest scripts/tests/test_xsp_ops_*.py -q --tb=line
```

## Hard constraints

- No Notion / Linear / Robinhood clients
- No writes under `wiki/` or `briefs/xsp-*` from this loop
- No secrets in repo
- No LLM calls in triage
- No `/opt/cemini` edits
