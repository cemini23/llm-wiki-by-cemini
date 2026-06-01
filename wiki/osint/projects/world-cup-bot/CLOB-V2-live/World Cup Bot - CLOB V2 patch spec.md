---
title: World Cup Bot - CLOB V2 patch spec
type: brief
date: 2026-06-01
updated: 2026-06-01
tags: [world-cup-bot, clob-v2, patch-spec]
ai-first: true
related:
  - projects/world-cup-bot/CLOB-V2-live/Index.md
  - projects/world-cup-bot/World Cup Bot.md
  - projects/world-cup-bot/CLOB-V2-live/OPEN-GAPS.md
  - entities/tools/world-cup-bot.md
  - projects/world-cup-bot/CLOB-V2-live/World Cup Bot - egress live layout.md
maturity: validated
---

# World Cup Bot — CLOB V2 patch spec

Polymarket **CLOB V2** cutover (Apr 28, 2026) archived `py-clob-client` V1. Production rejects V1-signed orders with:

```json
{"error": "order_version_mismatch"}
```

**Fix:** migrate `[live]` extra to **`py-clob-client-v2`** and update `clob_live.py` + preflight + tests.

References:

- [Polymarket V2 migration](https://docs.polymarket.com/v2-migration)
- GitHub issues `#335`–`#337` on archived `Polymarket/py-clob-client`

---

## P0 — Dependency swap

### `pyproject.toml`

```toml
[project.optional-dependencies]
live = [
    "websockets>=12.0",
    "py-clob-client-v2>=1.0.0",
    "eth-account>=0.13.0",
    "cryptography>=42.0",
]
```

- Remove `py-clob-client>=0.34.0`.
- Pin minimum v2 after first green CI run (suggest `>=1.0.0`).

### Install verification

```bash
pip install -e ".[live]"
python -c "from py_clob_client_v2.client import ClobClient; print('ok')"
```

---

## P0 — `world_cup_bot/clob_live.py`

### Import path

| V1 | V2 |
|----|-----|
| `py_clob_client.client.ClobClient` | `py_clob_client_v2.client.ClobClient` |
| `py_clob_client.clob_types.*` | `py_clob_client_v2.clob_types.*` |
| `py_clob_client.order_builder.constants` | `py_clob_client_v2.order_builder.constants` |

V2 `ClobClient.__init__` (verified on egress-fi 2026-06-01):

```python
ClobClient(
    host: str,
    chain_id: int,
    key: Optional[str] = None,
    creds: Optional[ApiCreds] = None,
    signature_type: Optional[int] = None,
    funder: Optional[str] = None,
    builder_config: Optional[BuilderConfig] = None,
    use_server_time: bool = False,
    retry_on_error: bool = False,
    fee_slippage: float = 0,
)
```

### `build_clob_client(settings)`

1. Keep `load_clob_auth()` — L2 HMAC creds unchanged for API auth.
2. Map `POLYMARKET_BUILDER_CODE` env → `BuilderConfig` (V2 replaces HMAC builder headers with signed `builderCode` on order). Cemini prod `.env-polymarket` already sets `POLYMARKET_BUILDER_CODE`.
3. Pass `use_server_time=True` or `retry_on_error=True` if recommended by v2 docs for clock skew / version retry.
4. Unset proxy env before client init when running on bare metal (Cemini `wc_run.sh` already unsets; document for standalone CLI).

### `post_quote_intent` / `post_exit_intent` / `post_arb_order`

**Do not hardcode** `PartialCreateOrderOptions(tick_size="0.01", neg_risk=False)`.

Plan flow already hits:

- `GET /tick-size?token_id=…`
- `GET /neg-risk?token_id=…`

Extract helper:

```python
def order_options_for_token(client, token_id: str) -> PartialCreateOrderOptions:
    tick = client.get_tick_size(token_id)  # or existing REST helper
    neg = client.get_neg_risk(token_id)    # verify v2 method name
    return PartialCreateOrderOptions(tick_size=tick, neg_risk=neg)
```

Pass options into `client.create_order(order_args, options)` then `client.post_order(order, post_only=…)`.

### Error surface

Map `PolyApiException` with `order_version_mismatch` to `LiveClobPostError` with actionable message pointing to V2 install.

---

## P0 — `world_cup_bot/preflight.py`

Replace:

```python
import py_clob_client  # noqa: F401
```

with:

```python
import py_clob_client_v2  # noqa: F401
```

Rename check id to `py_clob_client_v2` (keep alias `py_clob_client` in JSON for one release if UI depends on it).

Optional **P1** enhancement: when `not settings.dry_run`, run minimal signed order dry-run or `client.get_version()` and assert V2.

---

## P1 — Tests

| Test | Intent |
|------|--------|
| `tests/test_clob_live_v2.py` (new) | Mock `ClobClient.create_order` / `post_order`; assert `build_clob_client` passes builder + funder |
| Update `tests/test_quoter.py` | Patch `world_cup_bot.clob_live.build_clob_client` (unchanged path) |
| `tests/test_preflight.py` | Live mode requires v2 import |
| CI | `pip install -e ".[live]"` picks v2 |

Regression fixture: saved `PolyApiException` body with `order_version_mismatch` → must not occur after patch (integration test optional, manual on egress).

---

## P1 — Docs

Update in repo root:

- `SETUP.md` — `pip install -e ".[live]"` installs **v2**; link Polymarket wallet migration
- `SHADOW.md` Phase 3 — `py_clob_client_v2` check replaces v1
- `CLAUDE.md` — auth layers table + `clob_live.py` V2 note
- `.env.example` — add `POLYMARKET_BUILDER_CODE=` comment

---

## P1 — CI (`.github/workflows/ci.yml`)

- `[live]` install in CI job that runs preflight-related tests
- Add `scripts/check_clob_v2_import.py` (optional): fail if `py_clob_client` (v1) imported from `clob_live.py`

---

## P2 — Geoblock probe accuracy

Observed on egress-fi (Helsinki, ipinfo `FI`):

```json
{"blocked": true, "country": "DE", "ip": "204.168.139.190"}
```

Yet CLOB POST returns **400** (not **403**). Suggest:

- In `preflight.py`, when `geo.blocked` and `dry_run=false`, optionally probe `POST /order` with intentionally invalid payload — if response is not geoblock 403, downgrade to WARN with note "API country label unreliable".

---

## Wallet / collateral operator steps (not code)

Before first live POST on a wallet:

1. Complete Polymarket **Exchange V2 wallet migration** (UI trade ≥5 shares per V2 docs).
2. Confirm **pUSD** collateral if required post-cutover (check Polymarket account balance token).
3. Derive L2 creds once; store in Cemini `.env-polymarket`.

---

## Acceptance (egress-fi)

```bash
WC_LOAD_POLYMARKET_ENV=1 WC_DRY_RUN=false /opt/cemini/scripts/wc_run.sh preflight
# Expect: clob_auth PASS, py_clob_client_v2 PASS

WC_DRY_RUN=false /opt/cemini/scripts/wc_run.sh plan --record --liquidity-gate
# Expect: quote_intent rows in wc_ledger.jsonl, NO order_version_mismatch

systemctl enable --now cemini-wc-live-plan.timer   # operator GO
```

---

## Files touched (checklist)

- [ ] `pyproject.toml`
- [ ] `world_cup_bot/clob_live.py`
- [ ] `world_cup_bot/preflight.py`
- [ ] `tests/test_preflight.py`
- [ ] `tests/test_quoter.py`
- [ ] `tests/test_clob_live_v2.py` (new)
- [ ] `SETUP.md`, `SHADOW.md`, `CLAUDE.md`, `.env.example`
- [ ] `.github/workflows/ci.yml` (if live extra not already installed)

## Callers of `build_clob_client` (do not break)

- `quoter.submit_quotes`
- `order_manager` (cancel batch)
- `fill_handler` (exit POST)
- `__main__.py` (`cross-venue-exec` → `LivePmArbClient`)
