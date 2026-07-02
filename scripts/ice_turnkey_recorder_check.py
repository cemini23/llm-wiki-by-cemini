#!/usr/bin/env python3
"""County recorder deed-index sweep for ICE turnkey facility sale signals.

Outputs a dated markdown report under .local/reports/ice-turnkey-recorder/.
Uses Playwright when available (--browser); otherwise prints manual checklist.

Usage:
  python3 scripts/ice_turnkey_recorder_check.py
  python3 scripts/ice_turnkey_recorder_check.py --browser
  python3 scripts/ice_turnkey_recorder_check.py --browser --lookback-days 90
  python3 scripts/ice_turnkey_recorder_check.py --browser --portal-timeout 120
  python3 scripts/ice_turnkey_recorder_check.py --notify
  python3 scripts/ice_turnkey_recorder_check.py --test-discord
"""

from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import json
import re
import signal
import sys
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore
except ImportError:
    yaml = None  # type: ignore


SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
CONFIG_PATH = ROOT / "config" / "ice-turnkey-recorder-sites.yaml"
REPORT_DIR = ROOT / ".local" / "reports" / "ice-turnkey-recorder"
STATE_PATH = REPORT_DIR / "last_run_state.json"

if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from cemini_discord_notify import (  # noqa: E402
    post_recorder_sale_alert,
    post_test_ping,
    resolve_webhook_url,
)

SALE_KEYWORDS_DEFAULT = [
    "DEED",
    "GRANT DEED",
    "WARRANTY DEED",
    "QUIT CLAIM",
    "TRUSTEE",
    "BARGAIN",
    "CONVEY",
]


def load_config() -> dict[str, Any]:
    if yaml is None:
        sys.exit("PyYAML required: pip install pyyaml")
    with CONFIG_PATH.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def parse_doc_rows_kern(html: str) -> list[dict[str, str]]:
    """Parse Kern oresultg01 docdetail HTML table rows."""
    rows: list[dict[str, str]] = []
    # Links like: 225068193 ... Lis Pendens ... in flattened text
    for m in re.finditer(
        r"(\d{9,})\s+(\d{2}/\d{2}/\d{4})\s+(\d+)\s+([^R]+?)\s+(?:R|E)\s",
        re.sub(r"<[^>]+>", " ", html),
    ):
        rows.append(
            {
                "doc_number": m.group(1),
                "doc_date": m.group(2),
                "pages": m.group(3),
                "description": m.group(4).strip(),
            }
        )
    return rows


def is_sale_signal(description: str, keywords: list[str]) -> bool:
    upper = description.upper()
    if "LIS PEND" in upper or "LISP" in upper:
        return False
    return any(k in upper for k in keywords)


class PortalWAFBlocked(Exception):
    """Raised when a recorder portal blocks headless access (WAF / Access Denied)."""


class PortalCaptchaBlocked(Exception):
    """Raised when a portal requires CAPTCHA (reCAPTCHA / Turnstile) before search."""


@contextlib.contextmanager
def portal_batch_timeout(seconds: float):
    """Wall-clock timeout for a single portal batch (Unix only; harmless on Windows)."""
    if seconds <= 0 or sys.platform == "win32":
        yield
        return

    def _alarm(_sig, _frame):
        raise TimeoutError(f"Portal batch exceeded {seconds:.0f}s")

    old_handler = signal.signal(signal.SIGALRM, _alarm)
    old_alarm = signal.alarm(int(seconds))
    try:
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old_handler)
        if old_alarm:
            signal.alarm(old_alarm)


def launch_browser(p: Any) -> tuple[Any, Any]:
    """Launch headless Chromium with stealth args and a realistic context."""
    browser_args = [
        "--no-sandbox",
        "--disable-setuid-sandbox",
        "--disable-blink-features=AutomationControlled",
        "--disable-features=IsolateOrigins,site-per-process",
        "--disable-web-security",
        "--disable-dev-shm-usage",
        "--window-size=1920,1080",
    ]
    user_agent = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    )
    browser = p.chromium.launch(headless=True, args=browser_args)
    context = browser.new_context(
        user_agent=user_agent,
        locale="en-US",
        timezone_id="America/Los_Angeles",
        viewport={"width": 1920, "height": 1080},
        extra_http_headers={
            "Accept-Language": "en-US,en;q=0.9",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Upgrade-Insecure-Requests": "1",
        },
    )
    return browser, context


def load_state() -> dict[str, Any]:
    if STATE_PATH.is_file():
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    return {}


def hit_key(hit: dict[str, Any]) -> str:
    doc = hit.get("doc_number") or str(hash(hit.get("description") or hit.get("raw_line", "")))
    return f"{hit.get('site_id', '?')}|{doc}|{hit.get('doc_date', '')}"


def notify_new_sales(
    config: dict[str, Any],
    sale_hits: list[dict[str, Any]],
    report_path: Path,
    notified_hits: set[str],
) -> tuple[int, list[str]]:
    webhook_url = resolve_webhook_url()
    if not webhook_url:
        return 0, ["No Discord webhook — run: bash scripts/setup_recorder_discord_webhook.sh"]

    site_by_id = {s["id"]: s for s in config.get("sites", [])}
    sent = 0
    errors: list[str] = []

    for hit in sale_hits:
        key = hit_key(hit)
        if key in notified_hits:
            continue
        site_ids = hit.get("portal_site_ids") or [hit.get("site_id", "")]
        site = site_by_id.get(site_ids[0], {})
        site_label = " / ".join(
            site_by_id.get(s, {}).get("label", s) for s in site_ids
        )
        try:
            post_recorder_sale_alert(
                webhook_url,
                site_label=site_label,
                county=site.get("county", "?"),
                state=site.get("state", "?"),
                doc_number=str(hit.get("doc_number", "—")),
                doc_date=str(hit.get("doc_date", "")),
                description=hit.get("description") or hit.get("raw_line", ""),
                party_searched=str(hit.get("party_searched", "")),
                report_path=str(report_path),
            )
            notified_hits.add(key)
            sent += 1
        except Exception as exc:  # noqa: BLE001
            errors.append(str(exc))

    return sent, errors


def parse_acclaim_rows(page: Any) -> list[dict[str, str]]:
    """Parse Tyler Acclaim grid/table rows into structured index lines."""
    rows: list[dict[str, str]] = []
    for tr in page.locator("tr").all():
        text = re.sub(r"\s+", " ", tr.inner_text()).strip()
        if not re.search(r"\d{2}/\d{2}/\d{4}", text) or len(text) < 20:
            continue
        if text.upper().startswith("VIEW ROW"):
            continue
        doc_date = ""
        m_date = re.search(r"(\d{2}/\d{2}/\d{4})", text)
        if m_date:
            doc_date = m_date.group(1)
        doc_number = ""
        m_fee = re.search(r"(\d{4}-\d{6,})", text)
        if m_fee:
            doc_number = m_fee.group(1)
        rows.append(
            {
                "raw_line": text,
                "doc_date": doc_date,
                "doc_number": doc_number,
                "description": text,
            }
        )
    return rows


def acclaim_accept_terms(page: Any) -> None:
    """Accept disclaimer / terms. Handles checkbox + button variants (Pinal, SB, SD)."""
    blocked = _portal_blocked(page)
    if blocked and "reCAPTCHA" in blocked:
        raise PortalCaptchaBlocked(blocked)

    # San Bernardino — scroll disclaimer, then click I Accept when enabled
    sb_accept = page.locator("#submitDisclaimerAccept")
    if sb_accept.count():
        with contextlib.suppress(Exception):
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            page.wait_for_timeout(1500)
        if sb_accept.first.get_attribute("disabled") is not None:
            raise PortalCaptchaBlocked("reCAPTCHA on SB disclaimer (I Accept disabled)")
        sb_accept.first.click()
        page.wait_for_timeout(2000)
        return
    for chk in (
        "#chkDisclaimer",
        'input[name="chkDisclaimer"]',
        'input[id*="Disclaimer"]',
        'input[type="checkbox"]',
    ):
        loc = page.locator(chk)
        if loc.count():
            try:
                if not loc.is_checked():
                    loc.check()
                # Look for a submit/continue button tied to the disclaimer
                for submit in (
                    'input[type="submit"]',
                    'button[type="submit"]',
                    'button:has-text("Continue")',
                    'button:has-text("Submit")',
                    'input[value*="Agree"]',
                ):
                    sub = page.locator(submit)
                    if sub.count():
                        sub.first.click()
                        page.wait_for_timeout(2000)
                        break
                break
            except Exception:
                continue

    # Pinal / generic Acclaim accept button
    for sel in (
        'input[value="I accept the conditions above."]',
        'input[value="I Accept"]',
        'button:has-text("I Accept")',
        'button:has-text("Accept")',
        'input[type="submit"]:has-text("Accept")',
    ):
        loc = page.locator(sel)
        if loc.count():
            loc.first.click()
            page.wait_for_timeout(1500)
            break


def acclaim_goto_name_search(page: Any, portal: str) -> None:
    """Navigate to the name search page per portal."""
    portal = portal.rstrip("/")
    if "pinalcountyaz.gov" in portal:
        page.goto(
            f"{portal}/search/SearchTypeName",
            wait_until="domcontentloaded",
            timeout=120_000,
        )
        acclaim_accept_terms(page)
        return

    if "sdcounty.ca.gov" in portal:
        # SD may block direct /search/SearchTypeName in headless; start at base, accept terms, then navigate.
        try:
            page.goto(
                f"{portal}/search/SearchTypeName",
                wait_until="domcontentloaded",
                timeout=120_000,
            )
        except Exception:
            page.goto(portal, wait_until="domcontentloaded", timeout=120_000)
        acclaim_accept_terms(page)
        if page.get_by_text("Name", exact=True).count():
            page.get_by_text("Name", exact=True).first.click()
            page.wait_for_timeout(1500)
        return

    if "sbcounty.gov" in portal:
        page.goto(
            f"{portal.rstrip('/')}/user/disclaimer",
            wait_until="domcontentloaded",
            timeout=120_000,
        )
        acclaim_accept_terms(page)
        page.wait_for_timeout(1500)
        if page.get_by_text("Name", exact=True).count():
            page.get_by_text("Name", exact=True).first.click()
            page.wait_for_timeout(2000)
        return

    # Generic Acclaim
    page.goto(portal, wait_until="domcontentloaded", timeout=120_000)
    acclaim_accept_terms(page)
    page.wait_for_timeout(1000)


def _body_text(page: Any) -> str:
    try:
        return page.inner_text("body")
    except Exception:
        return ""


def _portal_blocked(page: Any) -> str | None:
    """Return a short reason if the page is WAF- or CAPTCHA-gated."""
    body = _body_text(page)
    html = ""
    try:
        html = page.content()
    except Exception:
        pass
    lower = (body + html).lower()
    if "access denied" in lower or "errors.edgesuite.net" in lower:
        return "WAF / Access Denied"
    if "cf-turnstile" in lower and "#name" not in lower and 'id="name"' not in lower:
        if page.locator("#Name:visible, input[name='Name']:visible").count() == 0:
            return "Cloudflare Turnstile (no search form)"
    if "g-recaptcha" in lower or "recaptcha" in lower:
        btn = page.locator("#submitDisclaimerAccept")
        if btn.count() and btn.first.get_attribute("disabled") is not None:
            return "reCAPTCHA on disclaimer (I Accept disabled)"
    return None


def acclaim_name_search(
    page: Any,
    portal: str,
    party: str,
    start: dt.date,
    end: dt.date,
    mode: str = "Both",
) -> list[dict[str, str]]:
    """Tyler Acclaim name search — mode: Direct (grantor), Reverse (grantee), Both.

    Waits for the results grid, handles pagination, and raises PortalWAFBlocked
    if the portal returns Access Denied / WAF page.
    """
    page.set_default_timeout(60_000)
    page.set_default_navigation_timeout(60_000)
    try:
        acclaim_goto_name_search(page, portal)
        blocked = _portal_blocked(page)
        if blocked:
            if "reCAPTCHA" in blocked:
                raise PortalCaptchaBlocked(blocked)
            raise PortalWAFBlocked(f"{portal}: {blocked}")
        mode_radio = page.locator(f'input[value="{mode}"]')
        if mode_radio.count():
            mode_radio.first.click()
        name_box = page.locator("#Name:visible, input#Name:visible, input[name='Name']:visible")
        if name_box.count() == 0:
            name_box = page.locator("input[type='text']:visible").filter(
                has_not=page.locator("[name='PartyType'], [id='PartyType']")
            )
        if name_box.count() == 0:
            blocked = _portal_blocked(page)
            if blocked:
                if "reCAPTCHA" in blocked:
                    raise PortalCaptchaBlocked(blocked)
                raise PortalWAFBlocked(f"{portal}: {blocked}")
            raise PortalWAFBlocked(f"{portal}: name search form not available")
        name_box.first.fill(party)
        start_s = f"{start.month}/{start.day}/{start.year}"
        end_s = f"{end.month}/{end.day}/{end.year}"
        for label in ("From Record Date", "From"):
            loc = page.get_by_label(label)
            if loc.count():
                loc.fill(start_s)
                break
        for label in ("To Record Date", "To"):
            loc = page.get_by_label(label)
            if loc.count():
                loc.fill(end_s)
                break
        search = page.locator('input[value="Search"]')
        if search.count():
            search.click()
        else:
            page.get_by_role("button", name=re.compile("Search", re.I)).first.click()

        page.wait_for_load_state("networkidle", timeout=30_000)
        body_text = _body_text(page)
        if "Access Denied" in body_text or "blocked" in body_text.lower():
            raise PortalWAFBlocked(f"{portal}: headless access blocked")
        if "No Results to Display" in body_text or "no documents found" in body_text.lower():
            return []

        page.wait_for_timeout(2000)
        all_rows = parse_acclaim_rows(page)
        if not all_rows:
            # Grid may render hidden (Kendo); one more parse after short settle
            page.wait_for_timeout(1500)
            all_rows = parse_acclaim_rows(page)

        # Paginate through Kendo grid pages if present
        while True:
            next_selectors = (
                'a[title="Go to the next page"]',
                '.k-pager-nav-next',
                'button:has-text("Next")',
                'a:has-text("Next")',
            )
            next_btn = None
            for sel in next_selectors:
                candidate = page.locator(sel)
                if candidate.count() and candidate.first.is_visible():
                    cls = candidate.first.get_attribute("class") or ""
                    if "disabled" not in cls and "k-state-disabled" not in cls:
                        next_btn = candidate.first
                        break
            if next_btn is None:
                break
            next_btn.click()
            page.wait_for_load_state("networkidle", timeout=30_000)
            all_rows.extend(parse_acclaim_rows(page))

        return all_rows
    except PortalWAFBlocked:
        raise
    except PortalCaptchaBlocked:
        raise
    except Exception as exc:
        body_text = _body_text(page)
        if "Access Denied" in body_text or "blocked" in body_text.lower():
            raise PortalWAFBlocked(f"{portal}: headless access blocked") from exc
        raise


def kern_search_party(
    page: Any, party: str, start: dt.date, end: dt.date, grantee: bool = True
) -> list[dict[str, str]]:
    """Kern County legacy CGI — grantor (D) or grantee (E) name search."""
    page.goto("https://recorderonline.co.kern.ca.us/cgi-bin/osearchg.mbr/input")
    page.wait_for_timeout(1000)
    role_val = "E" if grantee else "R"
    page.locator(f'input[type="radio"][value="{role_val}"]').first.check()
    page.locator('input[type="text"]').first.fill(party)
    inputs = page.locator('input[type="text"]')
    inputs.nth(1).fill(f"{start.month:02d}")
    inputs.nth(2).fill(f"{start.day:02d}")
    inputs.nth(3).fill(str(start.year))
    inputs.nth(4).fill(f"{end.month:02d}")
    inputs.nth(5).fill(f"{end.day:02d}")
    inputs.nth(6).fill(str(end.year))
    page.get_by_role("button", name="Search By Name").click()
    page.wait_for_timeout(2000)
    link = page.get_by_role("link", name=re.compile(re.escape(party[:12]), re.I))
    if link.count() == 0:
        return []
    link.first.click()
    page.wait_for_timeout(2000)
    return parse_doc_rows_kern(page.content())


def manual_checklist(config: dict[str, Any], start: dt.date, end: dt.date) -> str:
    lines = [
        "## Manual recorder checklist",
        f"Window: **{start.isoformat()}** → **{end.isoformat()}**",
        "",
        "For each site, search **grantor** (CXW/GEO legal names) and **grantee** (UNITED STATES / DHS):",
        "",
    ]
    for site in config.get("sites", []):
        rec = site["recorder"]
        lines.append(f"### {site['label']} ({site['county']} County, {site['state']})")
        lines.append(f"- Portal: {rec['portal']}")
        if rec.get("owner_alert"):
            lines.append(f"- Owner Alert: {rec['owner_alert']}")
        lines.append(f"- Address: {site['address']}")
        lines.append("")
    lines.append("**Sale signal:** grant deed / warranty deed / quit claim with grantee = United States.")
    lines.append("**Not a sale:** lis pendens, easement-only, financing, ops leases.")
    return "\n".join(lines)


def run_browser_sweep(
    config: dict[str, Any],
    start: dt.date,
    end: dt.date,
    portal_timeout_s: float = 90.0,
) -> tuple[list[dict[str, Any]], list[str]]:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as e:
        raise SystemExit(
            "Playwright not installed. Run: pip install playwright && playwright install chromium"
        ) from e

    keywords = config.get("sale_doc_keywords", SALE_KEYWORDS_DEFAULT)
    findings: list[dict[str, Any]] = []
    errors: list[str] = []

    parties = config.get("party_names", {})
    grantees = parties.get("grantees", ["UNITED STATES OF AMER"])
    grantors = parties.get("grantors", ["CORECIVIC", "GEO GROUP"])

    site_by_id = {s["id"]: s for s in config.get("sites", [])}

    # Dedupe acclaim portals (Pinal serves Florence + Eloy)
    acclaim_portals: dict[str, list[str]] = {}
    for site in config.get("sites", []):
        if site["recorder"]["backend"] == "tyler_acclaim":
            portal = site["recorder"]["portal"]
            acclaim_portals.setdefault(portal, []).append(site["id"])

    with sync_playwright() as p:
        browser, context = launch_browser(p)
        page = context.new_page()

        for site in config.get("sites", []):
            backend = site["recorder"]["backend"]
            site_id = site["id"]
            if backend != "kern_legacy":
                continue
            try:
                with portal_batch_timeout(portal_timeout_s):
                    for party in grantees[:4]:
                        for grantee in (True, False):
                            rows = kern_search_party(page, party, start, end, grantee=grantee)
                            role = "grantee" if grantee else "grantor"
                            for row in rows:
                                row["site_id"] = site_id
                                row["party_searched"] = f"{party} ({role})"
                                row["sale_signal"] = is_sale_signal(
                                    row.get("description", ""), keywords
                                )
                            findings.extend(rows)
                    for party in grantors[:3]:
                        rows = kern_search_party(page, party, start, end, grantee=False)
                        for row in rows:
                            row["site_id"] = site_id
                            row["party_searched"] = f"{party} (grantor)"
                            row["sale_signal"] = is_sale_signal(
                                row.get("description", ""), keywords
                            )
                        findings.extend(rows)
            except Exception as exc:  # noqa: BLE001
                errors.append(f"{site_id}: {exc}")

        for portal, site_ids in acclaim_portals.items():
            label = "+".join(site_ids)
            try:
                with portal_batch_timeout(portal_timeout_s):
                    searches: list[tuple[str, str, list[str]]] = [
                        ("grantee", "Reverse", grantees[:2]),
                        ("grantor", "Direct", grantors[:2]),
                    ]
                    seen_rows: set[tuple[str, str, str]] = set()
                    for role, mode, names in searches:
                        for party in names:
                            rows = acclaim_name_search(page, portal, party, start, end, mode=mode)
                            for row in rows:
                                dedupe_key = (
                                    row.get("doc_number", ""),
                                    row.get("doc_date", ""),
                                    row.get("raw_line", ""),
                                )
                                if dedupe_key in seen_rows:
                                    continue
                                seen_rows.add(dedupe_key)
                                tagged = dict(row)
                                tagged["site_id"] = site_ids[0]
                                tagged["portal_site_ids"] = site_ids
                                tagged["party_searched"] = f"{party} ({role}/{mode})"
                                tagged["sale_signal"] = is_sale_signal(
                                    tagged.get("description") or tagged.get("raw_line", ""),
                                    keywords,
                                )
                                findings.append(tagged)
            except (PortalWAFBlocked, PortalCaptchaBlocked) as exc:
                errors.append(f"acclaim:{label}: {exc}")
                for sid in site_ids:
                    rec = site_by_id.get(sid, {}).get("recorder", {})
                    owner_alert = rec.get("owner_alert")
                    manual_url = owner_alert or rec.get("portal", portal)
                    findings.append(
                        {
                            "site_id": sid,
                            "doc_date": "",
                            "doc_number": "",
                            "description": (
                                f"Automation blocked ({exc}) — manual index check: {manual_url}"
                            ),
                            "sale_signal": False,
                            "party_searched": "",
                        }
                    )
            except Exception as exc:  # noqa: BLE001
                errors.append(f"acclaim:{label}: {exc}")

        browser.close()

    return findings, errors


def write_report(
    config: dict[str, Any],
    start: dt.date,
    end: dt.date,
    findings: list[dict[str, Any]],
    errors: list[str],
    manual: bool,
    notified_hits: set[str] | None = None,
    discord_sent: int = 0,
) -> Path:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    today = dt.date.today().isoformat()
    out = REPORT_DIR / f"{today}-recorder-sweep.md"

    sale_hits = [f for f in findings if f.get("sale_signal")]
    lines = [
        f"# ICE turnkey recorder sweep — {today}",
        "",
        f"**Window:** {start.isoformat()} → {end.isoformat()}",
        f"**Mode:** {'manual checklist' if manual else 'playwright browser'}",
        f"**Config:** `{CONFIG_PATH.relative_to(ROOT)}`",
        "",
        "## Verdict",
        "",
    ]
    if sale_hits:
        lines.append(
            f"**{len(sale_hits)} potential sale-signal hit(s)** — verify grantor/grantee on index lines."
        )
    else:
        lines.append(
            "**No grant-deed sale signals** in automated/manual sweep window (lis pendens / unrelated federal index rows may still appear)."
        )

    lines.extend(["", "## Findings", ""])
    if findings:
        for f in findings:
            desc = f.get("description") or f.get("raw_line", "")
            flag = " **SALE?**" if f.get("sale_signal") else ""
            site_ids = f.get("portal_site_ids")
            site_label = "+".join(site_ids) if site_ids else f.get("site_id", "?")
            lines.append(
                f"- `{site_label}` | {f.get('doc_date', '?')} | "
                f"{f.get('doc_number', '—')} | {desc}{flag}"
            )
    else:
        lines.append("_No indexed rows returned (portal error, Cloudflare, or zero hits)._")

    if errors:
        lines.extend(["", "## Errors", ""])
        for e in errors:
            lines.append(f"- {e}")

    if discord_sent:
        lines.extend(["", "## Discord", "", f"Sent **{discord_sent}** new sale-signal alert(s)."])

    lines.extend(["", manual_checklist(config, start, end), ""])
    out.write_text("\n".join(lines), encoding="utf-8")

    prev = load_state()
    STATE_PATH.write_text(
        json.dumps(
            {
                "last_run": today,
                "window_start": start.isoformat(),
                "window_end": end.isoformat(),
                "finding_count": len(findings),
                "sale_signal_count": len(sale_hits),
                "notified_hits": sorted(notified_hits or prev.get("notified_hits", [])),
                "last_discord_sent": discord_sent,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--browser",
        action="store_true",
        help="Run Playwright automation (needs playwright + chromium)",
    )
    parser.add_argument(
        "--lookback-days",
        type=int,
        default=None,
        help="Override config default_lookback_days",
    )
    parser.add_argument(
        "--notify",
        action="store_true",
        help="Discord alert on new sale-signal hits (deduped via state file)",
    )
    parser.add_argument(
        "--test-discord",
        action="store_true",
        help="Send a test ping to the configured Discord webhook and exit",
    )
    parser.add_argument(
        "--portal-timeout",
        type=float,
        default=90.0,
        help="Max seconds per portal batch (default: 90)",
    )
    args = parser.parse_args()

    if args.test_discord:
        webhook_url = resolve_webhook_url()
        if not webhook_url:
            sys.exit(
                "No Discord webhook configured.\n"
                "  bash scripts/setup_recorder_discord_webhook.sh '<url>'"
            )
        post_test_ping(webhook_url)
        print("Discord test OK")
        return

    config = load_config()
    lookback = args.lookback_days or config.get("default_lookback_days", 120)
    end = dt.date.today()
    start = end - dt.timedelta(days=lookback)

    findings: list[dict[str, Any]] = []
    errors: list[str] = []

    if args.browser:
        findings, errors = run_browser_sweep(
            config, start, end, portal_timeout_s=args.portal_timeout
        )
        manual = False
    else:
        manual = True
        # Baseline Kern probe (2026-07-02): no recent CXW grant deeds in index
        findings = [
            {
                "site_id": "cal_city_cxw",
                "doc_date": "2000-09-14",
                "doc_number": "200114627",
                "description": "LisP (legacy CORRECTIONS CORP OF AMER INC — not Cal City facility)",
                "sale_signal": False,
            },
            {
                "site_id": "cal_city_cxw",
                "doc_date": "2025-06-16",
                "doc_number": "225068193",
                "description": "Lis Pendens — UNITED STATES OF AMER grantee (not fee-simple deed)",
                "sale_signal": False,
            },
        ]

    sale_hits = [f for f in findings if f.get("sale_signal")]
    prev = load_state()
    notified_hits = set(prev.get("notified_hits", []))
    discord_sent = 0
    notify_errors: list[str] = []

    if args.notify and sale_hits:
        discord_sent, notify_errors = notify_new_sales(
            config, sale_hits, REPORT_DIR / f"{dt.date.today().isoformat()}-recorder-sweep.md", notified_hits
        )
        errors.extend(notify_errors)

    out = write_report(
        config,
        start,
        end,
        findings,
        errors,
        manual,
        notified_hits=notified_hits,
        discord_sent=discord_sent,
    )
    print(out)


if __name__ == "__main__":
    main()
