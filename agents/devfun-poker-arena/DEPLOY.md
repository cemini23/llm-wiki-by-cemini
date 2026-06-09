# devfun-poker-arena — prod deploy (Cursor agent)

The Cursor agent owns deploys to `cemini-prod` after each HL round.

## Standard command

```bash
cd agents/devfun-poker-arena
./examples/cemini_hl_loop.sh --deploy --round N
```

Preflight (pytest + self-play gate + dry-run) runs first, then rsync + systemd restart.

## Defaults (do not override unless rotating creds/env)

| Variable | Default | Why |
|----------|---------|-----|
| `CEMINI_SKIP_ENV=1` | on | Prod `.env` (NUTS_DETECT, stagger, etc.) stays on server |
| `CEMINI_SKIP_CREDS=1` | on | Prod `agentId` / API key unchanged |

Set in `deploy/deploy_to_cemini_prod.sh` — no need to pass flags manually.

## SSH hang recovery

If deploy exits 255 during remote systemd (SSH reset), code may already be rsync'd:

```bash
ssh cemini-prod 'systemctl restart cemini-devfun-poker-lobby.service && systemctl is-active cemini-devfun-poker-lobby.service'
```

Export timer failures are non-critical; lobby service is the gate.

## Verify

```bash
ssh cemini-prod 'grep -c _hero_made_hand_exempt /opt/devfun-poker-arena/examples/cemini_decide.py'
ssh cemini-prod 'journalctl -u cemini-devfun-poker-lobby.service -n 5 --no-pager'
```

## HL state

`cemini_hl_loop.sh --deploy` updates `reports/hl-loop/state.json` (round, hands, commit).

## Version + tournament tracking

Every deploy appends to `reports/hl-loop/deploys.jsonl` (commit, env digest, preflight eval).

```bash
./scripts/sync_hl_artifacts.sh
uv run python scripts/pick_deploy_for_tournament.py
```

Full operator guide: `docs/tournament-version-tracking.md`.
