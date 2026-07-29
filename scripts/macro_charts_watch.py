#!/usr/bin/env python3
"""Macro Charts parameter watches → Discord webhook when levels hit.

Alert-only (no orders). Tickets are armed explicitly — propose mode extracts
candidates from newsletter text; you confirm with ``add`` or ``propose --arm``.

Usage:
  python3 scripts/macro_charts_watch.py list
  python3 scripts/macro_charts_watch.py propose --file path/to/paid.md
  python3 scripts/macro_charts_watch.py add --symbol ^VIX --op gt --level 20 \\
      --note "MC: VIX sustain >20" --source-url https://www.macrocharts.com/p/...
  python3 scripts/macro_charts_watch.py check
  python3 scripts/macro_charts_watch.py check --dry-run
  python3 scripts/macro_charts_watch.py test-discord
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.parse
import uuid
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import yaml

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

try:
    from cemini_discord_notify import post_discord  # noqa: E402
except ImportError:  # prod thin install
    post_discord = None  # type: ignore[assignment]

REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = REPO_ROOT / "config" / "macro-charts-watch.yaml"

OPS = ("gt", "gte", "lt", "lte", "cross_above", "cross_below")
UW_BASE = "https://api.unusualwhales.com/api"
UW_ENV_KEY = "UNUSUAL_WHALES_API_KEY"
UW_ENV_FILE_CANDIDATES = (
    "/opt/tipdrop-scanner/.env",
    "/opt/tipdrop/.env",
    "/opt/institutional-shadow/.env",
)


@dataclass
class Condition:
    op: str
    level: float
    sustain_checks: int = 1


@dataclass
class Watch:
    id: str
    symbol: str
    condition: Condition
    note: str = ""
    source_url: str = ""
    source_title: str = ""
    status: str = "armed"  # armed | triggered | expired | cancelled
    created_at: str = ""
    triggered_at: str | None = None
    expires_at: str | None = None
    last_price: float | None = None
    hold_count: int = 0
    instrument: str = ""
    meta: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        return d

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> Watch:
        cond_raw = raw.get("condition") or {}
        cond = Condition(
            op=str(cond_raw.get("op", "gt")),
            level=float(cond_raw["level"]),
            sustain_checks=int(cond_raw.get("sustain_checks") or 1),
        )
        return cls(
            id=str(raw["id"]),
            symbol=str(raw["symbol"]),
            condition=cond,
            note=str(raw.get("note") or ""),
            source_url=str(raw.get("source_url") or ""),
            source_title=str(raw.get("source_title") or ""),
            status=str(raw.get("status") or "armed"),
            created_at=str(raw.get("created_at") or ""),
            triggered_at=raw.get("triggered_at"),
            expires_at=raw.get("expires_at"),
            last_price=raw.get("last_price"),
            hold_count=int(raw.get("hold_count") or 0),
            instrument=str(raw.get("instrument") or ""),
            meta=dict(raw.get("meta") or {}),
        )


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def iso_now() -> str:
    return utc_now().strftime("%Y-%m-%dT%H:%M:%SZ")


def expand_home(path_str: str) -> Path:
    return Path(os.path.expanduser(path_str)).resolve()


def load_config(path: Path | None = None) -> dict[str, Any]:
    cfg_path = path or CONFIG_PATH
    if not cfg_path.is_file():
        raise SystemExit(f"Missing config: {cfg_path}")
    return yaml.safe_load(cfg_path.read_text(encoding="utf-8")) or {}


def watches_path(cfg: dict[str, Any]) -> Path:
    env_path = os.environ.get("MC_WATCH_STATE", "").strip()
    if env_path:
        return Path(env_path)
    rel = (cfg.get("state") or {}).get("watches") or ".local/state/macro-charts-watches.json"
    p = Path(rel)
    if not p.is_absolute():
        p = REPO_ROOT / p
    return p


def load_watches(path: Path) -> list[Watch]:
    if not path.is_file():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []
    return [Watch.from_dict(w) for w in (data.get("watches") or [])]


def save_watches(path: Path, watches: list[Watch]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "updated_at": iso_now(),
        "watches": [w.to_dict() for w in watches],
    }
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def resolve_symbol(name: str, aliases: dict[str, str]) -> str:
    key = name.strip().upper().lstrip("$")
    if key in aliases:
        return aliases[key]
    # already a yfinance ticker
    return name.strip()


def resolve_webhook(cfg: dict[str, Any]) -> str | None:
    wh = cfg.get("webhook") or {}
    env_var = str(wh.get("env_var") or "MACRO_CHARTS_DISCORD_WEBHOOK_URL")
    env = os.environ.get(env_var, "").strip()
    if env:
        return env
    primary = expand_home(str(wh.get("file") or "~/.cemini/macro-charts-discord-webhook.url"))
    if primary.is_file():
        url = primary.read_text(encoding="utf-8").strip()
        if url:
            return url
    # shared fallbacks (not recorder — wrong channel)
    for path in (
        expand_home(str(wh.get("fallback_file") or "~/.cemini/inbox-webhook.url")),
        Path.home() / ".cemini/inbox-webhook.url",
    ):
        if path.is_file():
            url = path.read_text(encoding="utf-8").strip()
            if url:
                return url
    env_generic = os.environ.get("DISCORD_WEBHOOK_URL", "").strip()
    return env_generic or None


def _strip_env_value(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def load_uw_api_key() -> str | None:
    """Load Unusual Whales key from env or TipDrop prod .env (never print it)."""
    env = os.environ.get(UW_ENV_KEY, "").strip()
    if env:
        return env
    explicit = os.environ.get("MC_WATCH_UW_ENV_FILE", "").strip()
    candidates = [explicit] if explicit else list(UW_ENV_FILE_CANDIDATES)
    for candidate in candidates:
        if not candidate:
            continue
        path = Path(candidate)
        if not path.is_file():
            continue
        try:
            for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
                stripped = line.strip()
                if not stripped or stripped.startswith("#"):
                    continue
                if stripped.startswith("export "):
                    stripped = stripped[7:].strip()
                if not stripped.startswith(f"{UW_ENV_KEY}="):
                    continue
                value = _strip_env_value(stripped.split("=", 1)[1])
                if value:
                    return value
        except OSError:
            continue
    return None


def uw_ticker_for_symbol(symbol: str, cfg: dict[str, Any]) -> str | None:
    """Map yfinance-style symbols to UW equity tickers; None = skip UW."""
    mapping = {str(k).upper(): str(v) for k, v in (cfg.get("uw_symbol_map") or {}).items()}
    key = symbol.strip().upper()
    if key in mapping:
        mapped = mapping[key]
        return mapped or None
    # plain equity/ETF tickers only
    if re.fullmatch(r"[A-Z]{1,5}", key):
        return key
    return None


def fetch_last_price_uw(uw_ticker: str, api_key: str) -> float:
    import urllib.error
    import urllib.request

    url = f"{UW_BASE}/stock/{urllib.parse.quote(uw_ticker)}/ohlc/1d"
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
            "User-Agent": "cemini-macro-charts-watch/1.0",
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")[:200]
        raise RuntimeError(f"UW HTTP {exc.code} for {uw_ticker}: {body}") from exc
    rows = payload.get("data") if isinstance(payload, dict) else None
    if not isinstance(rows, list) or not rows:
        raise RuntimeError(f"UW empty OHLC for {uw_ticker}")
    last = rows[-1]
    close = last.get("close") if isinstance(last, dict) else None
    if close is None:
        raise RuntimeError(f"UW missing close for {uw_ticker}")
    return float(close)


def fetch_last_price_yfinance(symbol: str) -> float:
    import yfinance as yf

    t = yf.Ticker(symbol)
    try:
        fi = t.fast_info
        price = getattr(fi, "last_price", None) or getattr(fi, "lastPrice", None)
        if price is None and isinstance(fi, dict):
            price = fi.get("last_price") or fi.get("lastPrice")
        if price is not None and float(price) > 0:
            return float(price)
    except Exception:
        pass
    hist = t.history(period="5d", interval="1d")
    if hist is None or hist.empty:
        raise RuntimeError(f"No price for {symbol}")
    return float(hist["Close"].iloc[-1])


def fetch_last_price(symbol: str, cfg: dict[str, Any] | None = None) -> float:
    """Prefer Unusual Whales OHLC when key+ticker available; else yfinance."""
    cfg = cfg or {}
    provider = (
        os.environ.get("MC_WATCH_PRICE_PROVIDER")
        or str(cfg.get("price_provider") or "auto")
    ).strip().lower()
    errors: list[str] = []

    if provider in ("auto", "uw"):
        uw_ticker = uw_ticker_for_symbol(symbol, cfg)
        key = load_uw_api_key() if uw_ticker else None
        if uw_ticker and key:
            try:
                return fetch_last_price_uw(uw_ticker, key)
            except Exception as exc:
                errors.append(f"uw:{exc}")
                if provider == "uw":
                    raise RuntimeError("; ".join(errors)) from exc

    if provider in ("auto", "yfinance"):
        try:
            return fetch_last_price_yfinance(symbol)
        except Exception as exc:
            errors.append(f"yfinance:{exc}")
            raise RuntimeError("; ".join(errors) or str(exc)) from exc

    raise RuntimeError(f"Unknown price provider: {provider}")


def post_discord_safe(
    webhook_url: str,
    *,
    content: str = "",
    embeds: list[dict[str, Any]] | None = None,
    username: str | None = "Macro Charts Watch",
) -> None:
    if post_discord is not None:
        post_discord(webhook_url, content=content, embeds=embeds, username=username)
        return
    import urllib.error
    import urllib.request

    payload: dict[str, Any] = {}
    if content:
        payload["content"] = content[:2000]
    if embeds:
        payload["embeds"] = embeds[:10]
    if username:
        payload["username"] = username[:80]
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        webhook_url,
        data=data,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "cemini-macro-charts-watch/1.0",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            if resp.status >= 400:
                raise RuntimeError(f"Discord webhook HTTP {resp.status}")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")[:500]
        raise RuntimeError(f"Discord webhook failed ({exc.code}): {body}") from exc


def condition_holds(op: str, price: float, level: float, prev: float | None) -> bool:
    if op == "gt":
        return price > level
    if op == "gte":
        return price >= level
    if op == "lt":
        return price < level
    if op == "lte":
        return price <= level
    if op == "cross_above":
        if prev is None:
            return price > level
        return prev <= level < price
    if op == "cross_below":
        if prev is None:
            return price < level
        return prev >= level > price
    raise ValueError(f"Unknown op: {op}")


def eval_watch(watch: Watch, price: float) -> tuple[bool, Watch]:
    """Update hold_count; return (should_fire, updated_watch)."""
    if watch.status != "armed":
        return False, watch
    if watch.expires_at:
        try:
            exp = datetime.fromisoformat(watch.expires_at.replace("Z", "+00:00"))
            if utc_now() >= exp:
                watch.status = "expired"
                return False, watch
        except ValueError:
            pass

    prev = watch.last_price
    holds = condition_holds(watch.condition.op, price, watch.condition.level, prev)
    watch.last_price = price
    if holds:
        watch.hold_count += 1
    else:
        watch.hold_count = 0

    need = max(1, int(watch.condition.sustain_checks))
    if watch.hold_count >= need:
        return True, watch
    return False, watch


def post_watch_alert(
    webhook_url: str,
    watch: Watch,
    price: float,
    *,
    username: str = "Macro Charts Watch",
) -> None:
    op = watch.condition.op
    level = watch.condition.level
    title = watch.instrument or watch.symbol
    desc_parts = [
        f"**{title}** `{watch.symbol}` hit **{op} {level:g}** (last={price:g}).",
    ]
    if watch.note:
        desc_parts.append(watch.note)
    if watch.source_url:
        desc_parts.append(f"[Source]({watch.source_url})")
    embeds = [
        {
            "title": "Macro Charts watch triggered",
            "description": "\n".join(desc_parts)[:4000],
            "color": 0xF39C12,
            "fields": [
                {"name": "Symbol", "value": watch.symbol, "inline": True},
                {"name": "Condition", "value": f"{op} {level:g}", "inline": True},
                {"name": "Last", "value": f"{price:g}", "inline": True},
                {"name": "Watch id", "value": watch.id[:64], "inline": False},
            ],
            "footer": {"text": "Alert-only — no orders placed"},
        }
    ]
    content = f"**MC watch** {title}: {op} {level:g} (last {price:g})"
    post_discord_safe(webhook_url, content=content, embeds=embeds, username=username)


# --- propose: heuristic extraction from newsletter prose ---

# "VIX ... >20", "sustain >20", "above 100.50", "below ~$12k", "testing ~100.50"
_LEVEL_RE = re.compile(
    r"(?P<name>\b(?:VIX|SPX|SPY|SOX|SMH|DXY|WTI|GOLD|SILVER|GDX|COPPER|USDJPY|YEN|"
    r"KOSPI|QQQ|EWZ|BIDU|BABA|MU|TSM|TY)\b)"
    r".{0,80}?"
    r"(?:(?:sustain\s+)?(?:>|above|over|north\s+of)\s*"
    r"|(?:<|below|under|south\s+of)\s*"
    r"|(?:testing|defend(?:ing)?|near|around|~)\s*)"
    r"\$?(?P<level>\d{1,5}(?:,\d{3})*(?:\.\d+)?)\s*(?P<k>k)?",
    re.IGNORECASE | re.DOTALL,
)

_DIR_ABOVE = re.compile(r"(?:sustain\s+)?(?:>|above|over|north\s+of)", re.I)
_DIR_BELOW = re.compile(r"(?:<|below|under|south\s+of)", re.I)


def _parse_level(num: str, k_suffix: str | None) -> float:
    v = float(num.replace(",", ""))
    if k_suffix:
        v *= 1000.0
    return v


def propose_from_text(
    text: str,
    *,
    aliases: dict[str, str],
    source_url: str = "",
    source_title: str = "",
    sustain_checks: int = 1,
) -> list[dict[str, Any]]:
    """Extract candidate watches from Macro Charts prose (heuristic, not LLM)."""
    seen: set[tuple[str, str, float]] = set()
    out: list[dict[str, Any]] = []
    for m in _LEVEL_RE.finditer(text):
        name = m.group("name").upper()
        level = _parse_level(m.group("level"), m.group("k"))
        window = m.group(0)
        if _DIR_ABOVE.search(window):
            op = "gt"
        elif _DIR_BELOW.search(window):
            op = "lt"
        else:
            # "testing / defending / near" → treat as level watch both sides is noisy;
            # default to cross_above for support defense language, else skip soft mentions
            if re.search(r"defend", window, re.I):
                op = "lt"  # break below support
            elif re.search(r"testing", window, re.I):
                op = "lte"
            else:
                continue
        key = (name, op, level)
        if key in seen:
            continue
        seen.add(key)
        symbol = resolve_symbol(name, aliases)
        out.append(
            {
                "instrument": name,
                "symbol": symbol,
                "condition": {
                    "op": op,
                    "level": level,
                    "sustain_checks": sustain_checks,
                },
                "note": f"Heuristic from text: {window.strip()[:120]}",
                "source_url": source_url,
                "source_title": source_title,
                "confidence": "heuristic",
            }
        )
    return out


def extract_source_meta(md_text: str) -> tuple[str, str]:
    url = ""
    title = ""
    for pat in (
        r"https?://(?:www\.)?macrocharts\.com/p/[a-zA-Z0-9_-]+",
        r"https?://macrocharts\.substack\.com/p/[a-zA-Z0-9_-]+",
        r"https?://open\.substack\.com/pub/macrocharts/p/[a-zA-Z0-9_-]+",
    ):
        m = re.search(pat, md_text)
        if m:
            url = m.group(0).split("?")[0]
            break
    m2 = re.search(r"^title:\s*[\"']?(.+?)[\"']?\s*$", md_text, re.M)
    if m2:
        title = m2.group(1).strip()
    return url, title


def new_watch_id(symbol: str, op: str, level: float) -> str:
    stamp = utc_now().strftime("%Y%m%d")
    slug = re.sub(r"[^\w]+", "-", f"{symbol}-{op}-{level:g}").strip("-").lower()[:40]
    return f"mc-{stamp}-{slug}-{uuid.uuid4().hex[:6]}"


def make_watch(
    *,
    symbol: str,
    op: str,
    level: float,
    note: str = "",
    source_url: str = "",
    source_title: str = "",
    instrument: str = "",
    sustain_checks: int = 1,
    ttl_days: int = 21,
) -> Watch:
    if op not in OPS:
        raise SystemExit(f"op must be one of {OPS}")
    expires = None
    if ttl_days > 0:
        expires = (utc_now() + timedelta(days=ttl_days)).strftime("%Y-%m-%dT%H:%M:%SZ")
    return Watch(
        id=new_watch_id(symbol, op, level),
        symbol=symbol,
        condition=Condition(op=op, level=level, sustain_checks=sustain_checks),
        note=note,
        source_url=source_url,
        source_title=source_title,
        status="armed",
        created_at=iso_now(),
        expires_at=expires,
        instrument=instrument or symbol,
    )


def cmd_list(cfg: dict[str, Any], *, status: str | None) -> int:
    path = watches_path(cfg)
    watches = load_watches(path)
    if status:
        watches = [w for w in watches if w.status == status]
    if not watches:
        print("(no watches)")
        return 0
    for w in watches:
        lvl = w.condition.level
        print(
            f"{w.status:10} {w.symbol:12} {w.condition.op:12} {lvl:<10g} "
            f"hold={w.hold_count}/{w.condition.sustain_checks}  {w.id}"
        )
        if w.note:
            print(f"           {w.note[:100]}")
    return 0


def cmd_add(cfg: dict[str, Any], args: argparse.Namespace) -> int:
    aliases = {k.upper(): v for k, v in (cfg.get("symbol_aliases") or {}).items()}
    symbol = resolve_symbol(args.symbol, aliases)
    ttl = int(args.ttl_days if args.ttl_days is not None else cfg.get("default_ttl_days") or 21)
    sustain = int(
        args.sustain
        if args.sustain is not None
        else cfg.get("default_sustain_checks") or 1
    )
    watch = make_watch(
        symbol=symbol,
        op=args.op,
        level=float(args.level),
        note=args.note or "",
        source_url=args.source_url or "",
        source_title=args.source_title or "",
        instrument=args.instrument or args.symbol,
        sustain_checks=sustain,
        ttl_days=ttl,
    )
    path = watches_path(cfg)
    watches = load_watches(path)
    watches.append(watch)
    save_watches(path, watches)
    print(f"armed {watch.id}  {watch.symbol} {watch.condition.op} {watch.condition.level:g}")
    return 0


def cmd_propose(cfg: dict[str, Any], args: argparse.Namespace) -> int:
    path = Path(args.file)
    if not path.is_file():
        raise SystemExit(f"File not found: {path}")
    text = path.read_text(encoding="utf-8", errors="replace")
    url, title = extract_source_meta(text)
    if args.source_url:
        url = args.source_url
    aliases = {k.upper(): v for k, v in (cfg.get("symbol_aliases") or {}).items()}
    sustain = int(cfg.get("default_sustain_checks") or 1)
    candidates = propose_from_text(
        text,
        aliases=aliases,
        source_url=url,
        source_title=title,
        sustain_checks=sustain,
    )
    if not candidates:
        print("No heuristic level candidates found.")
        return 0
    print(json.dumps(candidates, indent=2))
    if not args.arm:
        print("\n# Review above, then re-run with --arm to store watches (or use add).")
        return 0
    ttl = int(cfg.get("default_ttl_days") or 21)
    store = watches_path(cfg)
    watches = load_watches(store)
    for c in candidates:
        w = make_watch(
            symbol=c["symbol"],
            op=c["condition"]["op"],
            level=float(c["condition"]["level"]),
            note=c.get("note") or "",
            source_url=c.get("source_url") or "",
            source_title=c.get("source_title") or "",
            instrument=c.get("instrument") or "",
            sustain_checks=int(c["condition"].get("sustain_checks") or 1),
            ttl_days=ttl,
        )
        watches.append(w)
        print(f"armed {w.id}")
    save_watches(store, watches)
    return 0


def cmd_cancel(cfg: dict[str, Any], watch_id: str) -> int:
    path = watches_path(cfg)
    watches = load_watches(path)
    found = False
    for w in watches:
        if w.id == watch_id or w.id.startswith(watch_id):
            w.status = "cancelled"
            found = True
            print(f"cancelled {w.id}")
    if not found:
        raise SystemExit(f"No watch matching id: {watch_id}")
    save_watches(path, watches)
    return 0


def cmd_check(cfg: dict[str, Any], *, dry_run: bool) -> int:
    path = watches_path(cfg)
    watches = load_watches(path)
    armed = [w for w in watches if w.status == "armed"]
    if not armed:
        print("No armed watches.")
        return 0

    webhook = None if dry_run else resolve_webhook(cfg)
    if not dry_run and not webhook:
        print(
            "No Discord webhook. Run:\n"
            "  bash scripts/setup_macro_charts_discord_webhook.sh",
            file=sys.stderr,
        )
        return 2

    username = str((cfg.get("webhook") or {}).get("username") or "Macro Charts Watch")
    fired = 0
    errors = 0
    for w in watches:
        if w.status != "armed":
            continue
        try:
            price = fetch_last_price(w.symbol, cfg)
        except Exception as exc:
            print(f"PRICE_FAIL {w.symbol}: {exc}", file=sys.stderr)
            errors += 1
            continue
        should_fire, w = eval_watch(w, price)
        print(
            f"{'FIRE' if should_fire else 'ok  '} {w.symbol:12} "
            f"{w.condition.op} {w.condition.level:g}  last={price:g}  "
            f"hold={w.hold_count}/{w.condition.sustain_checks}"
        )
        if should_fire:
            if dry_run:
                print(f"  (dry-run) would Discord: {w.note or w.id}")
            else:
                assert webhook is not None
                post_watch_alert(webhook, w, price, username=username)
                print(f"  Discord sent: {w.id}")
            w.status = "triggered"
            w.triggered_at = iso_now()
            fired += 1

    save_watches(path, watches)
    print(f"Done. fired={fired} errors={errors} dry_run={dry_run}")
    return 1 if errors and not fired else 0


def cmd_test_discord(cfg: dict[str, Any]) -> int:
    webhook = resolve_webhook(cfg)
    if not webhook:
        print(
            "No Discord webhook. Run:\n"
            "  bash scripts/setup_macro_charts_discord_webhook.sh",
            file=sys.stderr,
        )
        return 2
    username = str((cfg.get("webhook") or {}).get("username") or "Macro Charts Watch")
    post_discord_safe(
        webhook,
        content="Macro Charts watch — Discord webhook test OK.",
        embeds=[
            {
                "title": "MC watch armed",
                "description": (
                    "You will get pinged here when an armed parameter watch triggers. "
                    "Alert-only — no orders. Prod timer: cemini-macro-charts-watch.timer"
                ),
                "color": 0x2ECC71,
            }
        ],
        username=username,
    )
    print("Test ping sent.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Macro Charts watches → Discord")
    p.add_argument("--config", type=Path, default=CONFIG_PATH)
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("list", help="List watches")
    sp.add_argument("--status", choices=("armed", "triggered", "expired", "cancelled"))

    sp = sub.add_parser("add", help="Arm a watch")
    sp.add_argument("--symbol", required=True, help="yfinance symbol or alias (VIX, SPX, …)")
    sp.add_argument("--op", required=True, choices=OPS)
    sp.add_argument("--level", required=True, type=float)
    sp.add_argument("--note", default="")
    sp.add_argument("--instrument", default="")
    sp.add_argument("--source-url", default="")
    sp.add_argument("--source-title", default="")
    sp.add_argument("--sustain", type=int, default=None)
    sp.add_argument("--ttl-days", type=int, default=None)

    sp = sub.add_parser("propose", help="Heuristic extract from newsletter markdown")
    sp.add_argument("--file", required=True)
    sp.add_argument("--arm", action="store_true", help="Store candidates as armed watches")
    sp.add_argument("--source-url", default="")

    sp = sub.add_parser("cancel", help="Cancel a watch by id prefix")
    sp.add_argument("watch_id")

    sp = sub.add_parser("check", help="Poll prices; Discord on trigger")
    sp.add_argument("--dry-run", action="store_true")

    sub.add_parser("test-discord", help="Send a test webhook ping")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    cfg = load_config(args.config)
    if args.cmd == "list":
        return cmd_list(cfg, status=args.status)
    if args.cmd == "add":
        return cmd_add(cfg, args)
    if args.cmd == "propose":
        return cmd_propose(cfg, args)
    if args.cmd == "cancel":
        return cmd_cancel(cfg, args.watch_id)
    if args.cmd == "check":
        return cmd_check(cfg, dry_run=args.dry_run)
    if args.cmd == "test-discord":
        return cmd_test_discord(cfg)
    raise SystemExit(f"Unknown cmd: {args.cmd}")


if __name__ == "__main__":
    raise SystemExit(main())
