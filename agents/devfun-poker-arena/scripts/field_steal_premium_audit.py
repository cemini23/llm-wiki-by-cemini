#!/usr/bin/env python3
"""Premium-model steal/adopt audit on fresh competition export + HL analyze."""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIELD_PATH = ROOT / "reports/hl-loop/field_report_prod_2026-06-07.txt"
ANALYZE_PATH = ROOT / "reports/hl-loop/latest_analyze.txt"
BASELINE_PATH = ROOT / "reports/hl-loop/field-report-2026-06-07.md"
OUT_DIR = ROOT / "reports/hl-loop/premium-steal-audit"
PROMPT_PATH = OUT_DIR / "premium_steal_prompt.txt"


def _load_env() -> None:
    for p in (
        Path.home() / ".cemini" / "llm-routing.env",
        Path("/Users/claudiobarone/Desktop/OSINT WORKSPACE/.env"),
    ):
        if not p.is_file():
            continue
        for line in p.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            k, v = k.strip(), v.strip().strip('"').strip("'")
            if k and k not in os.environ:
                os.environ[k] = v


def _build_prompt() -> str:
    field = FIELD_PATH.read_text()
    analyze = ANALYZE_PATH.read_text()
    baseline = BASELINE_PATH.read_text() if BASELINE_PATH.is_file() else ""
    return f"""You are a poker bot strategist auditing dev.fun Playground S1 for **steal-from / adopt** candidates.

Goal: identify what to **copy or exploit** from rival archetypes and named villains — NOT generic leak fixes (those come from HL analyze).

CRITICAL CONSTRAINTS:
- Zero LLM calls at runtime. Output env toggles, HUD archetype rules, nemesis lists, preflop/postflop guard ideas, regression spots only.
- Hero is **#1** (138,699 chips, 2,203 hands, 10.8% VPIP / 3.7% PFR) under **first_protect** — do NOT recommend widening for vanity.
- KO tournament has NO rebuy — preservation beats exploit EV until user explicitly switches pace.
- API export has NO street actions — infer from stats labels, pots-won-vs-hero, showdown outcomes, HL analyze worst hands only.

ALREADY WIRED (do not re-recommend unless upgrade):
- Nemesis handles: hunterguy102, thaddius (CEMINI_NEMESIS_HANDLES)
- Maniac HUD lane (Grok 64–77% VPIP cluster) — fold trash, value-call wider
- first_protect: open_steal_equity=0.99, chart-only EP, SB premium-only vs opens
- HL R24 shipped: OOP weak top pair fold on three-flush boards
- Cold-start no-steal, anti-profiling mix/sanitize, stagger locks

BASELINE STEAL QUEUE (human analyst — validate/refute/extend):
{baseline}

FIELD REPORT (top-200 export, prod Jun 7):
{field}

HL ANALYZE (latest 100-hand sample, worst 15):
{analyze}

DELIVERABLE — structured markdown:

## 1. Steal-from rivals (exploit, do not mimic width)
For each candidate: handle/cluster | stat signal | exploit action | chip-risk | first_protect OK?

## 2. Adopt-from rivals (structural patterns worth copying)
Only patterns that fit a tight-passive #1 bot (e.g. float_engine balanced line, fefou tight-measured survival). Reject LAG mimicry.

## 3. Nemesis / prefix targets (ranked)
Table: priority | handle/prefix | evidence | env vs code patch | HL round suggestion

## 4. HUD archetype gaps
What rival styles in top-20 are misclassified or under-exploited? Grok cluster, jagoan_neon, 0xJeff_ai, v12 fleet, v_16.

## 5. Do NOT steal (variance traps)
3–5 styles/behaviors that look +EV on leaderboard but would bust a nit under KO rules.

## 6. Merged patch backlog
Single ranked table merging field intel + HL analyze + your audit:
| Priority | Type (steal/adopt/fix) | Target | Mechanism | Regression spot idea | Deploy gate |

## 7. Conflicts with baseline queue
Where you disagree with the human baseline steal queue — explain.

Be specific for Python heuristic bot (cemini_decide.py + opponent_hud_exploit.py + nemesis_seed.py).
"""


def _call_openai_compat(
    *,
    base_url: str,
    api_key: str,
    model: str,
    prompt: str,
    extra: dict | None = None,
    max_tokens: int = 12000,
) -> str:
    import httpx

    url = base_url.rstrip("/") + "/chat/completions"
    body: dict = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "Expert poker bot strategist. Steal/adopt audit only. Concise tables.",
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.25,
        "max_tokens": max_tokens,
    }
    if extra:
        body.update(extra)
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    if "openrouter.ai" in base_url:
        headers["HTTP-Referer"] = os.environ.get(
            "OPENROUTER_HTTP_REFERER", "https://github.com/cemini"
        )
        headers["X-Title"] = os.environ.get(
            "OPENROUTER_APP_TITLE", "devfun-poker steal audit"
        )
    r = httpx.post(url, headers=headers, json=body, timeout=360.0)
    r.raise_for_status()
    data = r.json()
    return (data["choices"][0]["message"]["content"] or "").strip()


def main() -> int:
    _load_env()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if not FIELD_PATH.is_file():
        print(f"Missing {FIELD_PATH}", file=sys.stderr)
        return 1
    prompt = _build_prompt()
    PROMPT_PATH.write_text(prompt)

    grok_key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    ds_key = os.environ.get("DEEPSEEK_API_KEY")
    if not grok_key:
        print("OPENROUTER_API_KEY missing", file=sys.stderr)
        return 1
    if not ds_key:
        print("DEEPSEEK_API_KEY missing", file=sys.stderr)
        return 1

    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%MZ")
    results: dict[str, str] = {}

    print("Calling x-ai/grok-4.3 via OpenRouter (reasoning=high)...")
    try:
        results["grok-4.3"] = _call_openai_compat(
            base_url=os.environ.get("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1"),
            api_key=grok_key,
            model="x-ai/grok-4.3",
            prompt=prompt,
            extra={"reasoning": {"effort": "high"}},
        )
        (OUT_DIR / f"grok-4.3_{ts}.md").write_text(results["grok-4.3"])
        print(f"  grok OK ({len(results['grok-4.3'])} chars)")
    except Exception as e:
        print(f"  grok failed: {e}", file=sys.stderr)
        results["grok-4.3"] = f"ERROR: {e}"

    print("Calling deepseek-reasoner...")
    try:
        results["deepseek-reasoner"] = _call_openai_compat(
            base_url=os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com/v1"),
            api_key=ds_key,
            model="deepseek-reasoner",
            prompt=prompt,
        )
        (OUT_DIR / f"deepseek-reasoner_{ts}.md").write_text(results["deepseek-reasoner"])
        print(f"  deepseek OK ({len(results['deepseek-reasoner'])} chars)")
    except Exception as e:
        print(f"  deepseek failed: {e}", file=sys.stderr)
        results["deepseek-reasoner"] = f"ERROR: {e}"

    meta = {"timestamp": ts, "models": list(results.keys()), "prompt_chars": len(prompt)}
    (OUT_DIR / f"meta_{ts}.json").write_text(json.dumps(meta, indent=2))
    print(json.dumps(meta, indent=2))
    return 0 if all(not v.startswith("ERROR:") for v in results.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
