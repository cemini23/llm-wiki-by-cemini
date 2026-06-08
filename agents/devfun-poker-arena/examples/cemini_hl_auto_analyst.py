#!/usr/bin/env python3
"""DeepSeek HL auto-analyst — leak guards, style tweaks, kill switch.

Called from arena_monitor.py after each analyze pass (~30 min on prod).
Uses DEEPSEEK_API_KEY (+ OpenRouter failover) via llm_routing_client.
Prefetches gambling-wiki context from librarian kb-server (``project=gambling-wiki``).

Usage:
    uv run python examples/cemini_hl_auto_analyst.py --report reports/hl-loop/latest_analyze.txt
    uv run python examples/cemini_hl_auto_analyst.py --dry-run
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from hl_runtime_config import (  # noqa: E402
    AUTO_ANALYST_STATE_PATH,
    activate_kill_switch,
    apply_style_overrides,
    clear_kill_switch,
    is_kill_switch_active,
    kill_switch_status,
    load_runtime_guards,
    load_style_overrides,
    merge_runtime_guards,
)
from gambling_wiki_kb import fetch_gambling_wiki_briefing, load_librarian_env  # noqa: E402
from llm_routing_client import chat_json  # noqa: E402

_AGENT_DIR = _EXAMPLES.parent
_HL_DIR = _AGENT_DIR / "reports" / "hl-loop"
_DEFAULT_REPORT = _HL_DIR / "latest_analyze.txt"
_OUT_JSON = _HL_DIR / "auto_analyst_latest.json"
_OUT_MD = _HL_DIR / "auto_analyst_latest.md"

_SYSTEM = """You are the Cemini dev.fun poker HL auto-analyst (heuristic bot, zero runtime LLM).

Output ONLY valid JSON matching this schema:
{
  "severity": "info|leak|critical|catastrophic",
  "kill_switch": false,
  "kill_reason": "",
  "clear_kill_switch": false,
  "style_tweaks": {
    "fold_slack_delta": 0.0,
    "call_margin_delta": 0.0,
    "open_steal_equity_min": null,
    "join_retry_multiplier": 1.0,
    "notes": ""
  },
  "runtime_guards": [
    {
      "id": "unique_snake_case",
      "street": "Preflop|Flop|Turn|River",
      "positions": ["SB","BB","UTG","MP","CO","BTN"],
      "hand_classes": ["72o","Kh2h mapped as hand class like 72o"],
      "when_facing_bet": true,
      "when_opening": false,
      "action": "fold|check",
      "reason": "analyze row reference"
    }
  ],
  "patch_summary": "one line",
  "operator_note": "2-4 sentences for human"
}

Rules:
- Prefer runtime_guards (JSON rules) over editing Python source.
- kill_switch=true ONLY for catastrophic bugs (e.g. calling off 100bb with trash repeatedly,
  obvious infinite bleed pattern in analyze, logic that can zero stack in one orbit).
- Do NOT kill_switch for normal variance or single -100 hands.
- clear_kill_switch=true only if kill is active AND you believe prior alarm was false.
- Under first_protect / rank #1: tighten trash folds; do NOT widen steals.
- Max 3 runtime_guards per response; smallest targeted guards only.
- style_tweaks deltas are small (0.0-0.08); join_retry_multiplier 1.0-3.0 only when chip bleed from table intake.
- severity catastrophic => kill_switch must be true.
"""


def _load_osint_routing_env() -> None:
    root = os.environ.get("CEMINI_OSINT_ROOT", str(Path.home() / "Desktop/OSINT WORKSPACE"))
    script = Path(root) / "scripts" / "source_llm_routing_env.sh"
    env_file = Path.home() / ".cemini" / "llm-routing.env"
    if env_file.is_file():
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            k, v = k.strip(), v.strip().strip('"').strip("'")
            if k and k not in os.environ:
                os.environ[k] = v
    _ = script  # shell source not run from Python; .env file is enough on prod


def _metrics_tail(reports_dir: Path, n: int = 3) -> list[dict]:
    hist = reports_dir / "analyze" / "history.jsonl"
    if not hist.is_file():
        return []
    lines = hist.read_text(encoding="utf-8").splitlines()
    out: list[dict] = []
    for line in lines[-n:]:
        try:
            out.append(json.loads(line))
        except Exception:
            continue
    return out


def _build_user_prompt(
    *,
    report_text: str,
    metrics: dict | None,
    metrics_history: list[dict],
    qual_summary: str,
    wiki_briefing: str = "",
) -> str:
    guards = load_runtime_guards()
    style = load_style_overrides()
    ks = kill_switch_status()
    wiki_block = ""
    if wiki_briefing.strip():
        wiki_block = f"""
## Gambling wiki context (kb-server, project=gambling-wiki)
{wiki_briefing.strip()}

Use for HL discipline (survival vs exploit, guard patterns). Do not contradict first_protect / rank #1 posture.
"""
    return f"""{wiki_block}## Arena analyze report
{report_text.strip()}

## Latest metrics (this pass)
{json.dumps(metrics or {}, indent=2)}

## Recent history (last passes)
{json.dumps(metrics_history, indent=2)}

## Qualification / posture
{qual_summary.strip() or "(unknown)"}

## Kill switch state
{json.dumps(ks, indent=2)}

## Active runtime guards ({len(guards)})
{json.dumps(guards[:10], indent=2)}

## Style overrides
{json.dumps(style, indent=2)}

Analyze worst hands + position breakdown. Propose guards/style OR kill_switch if catastrophic.
"""


def _validate_response(data: dict[str, Any]) -> dict[str, Any]:
    sev = str(data.get("severity") or "info").lower()
    if sev not in ("info", "leak", "critical", "catastrophic"):
        sev = "info"
    data["severity"] = sev
    data["kill_switch"] = bool(data.get("kill_switch"))
    if sev == "catastrophic":
        data["kill_switch"] = True
    guards = data.get("runtime_guards")
    if not isinstance(guards, list):
        data["runtime_guards"] = []
    else:
        data["runtime_guards"] = [g for g in guards if isinstance(g, dict)][:3]
    tweaks = data.get("style_tweaks")
    if not isinstance(tweaks, dict):
        data["style_tweaks"] = {}
    return data


def _heuristic_catastrophe(metrics: dict | None) -> tuple[bool, str]:
    """Fast path: activate kill without LLM if recent sample is extreme."""
    if not metrics:
        return False, ""
    hands = int(metrics.get("hands") or 0)
    net = int(metrics.get("net_delta") or 0)
    losses = int(metrics.get("losses") or 0)
    if hands >= 50 and net <= -7000 and losses >= hands * 0.85:
        return True, (
            f"heuristic: {hands} hands net_delta={net} losses={losses} "
            "(>85% loss rate, extreme bleed)"
        )
    return False, ""


def apply_response(data: dict[str, Any], *, dry_run: bool = False) -> dict[str, Any]:
    data = _validate_response(data)
    actions: list[str] = []

    if data.get("clear_kill_switch") and is_kill_switch_active() and not dry_run:
        clear_kill_switch(reason=data.get("operator_note") or "auto_analyst clear", source="hl_auto_analyst")
        actions.append("cleared_kill_switch")

    if data.get("kill_switch"):
        reason = (data.get("kill_reason") or data.get("patch_summary") or "catastrophic leak").strip()
        if not dry_run:
            activate_kill_switch(
                reason=reason,
                severity=str(data.get("severity") or "catastrophic"),
                source="hl_auto_analyst",
            )
        actions.append("activated_kill_switch")

    guards = data.get("runtime_guards") or []
    if guards and os.environ.get("CEMINI_HL_AUTO_APPLY", "1").strip().lower() not in ("0", "false", "no"):
        if not dry_run:
            merge_runtime_guards(guards, source="hl_auto_analyst")
        actions.append(f"merged_guards:{len(guards)}")

    tweaks = data.get("style_tweaks") or {}
    if tweaks and any(tweaks.get(k) for k in ("fold_slack_delta", "call_margin_delta", "join_retry_multiplier")):
        if not dry_run:
            apply_style_overrides(tweaks, source="hl_auto_analyst")
        actions.append("applied_style_tweaks")

    data["actions_taken"] = actions
    return data


def run_auto_analyst(
    *,
    report_text: str,
    metrics: dict | None = None,
    metrics_history: list[dict] | None = None,
    qual_summary: str = "",
    dry_run: bool = False,
) -> dict[str, Any]:
    if metrics and os.environ.get("CEMINI_HL_HEURISTIC_KILL", "1").strip().lower() not in ("0", "false"):
        trip, reason = _heuristic_catastrophe(metrics)
        if trip:
            if not dry_run:
                activate_kill_switch(reason=reason, severity="catastrophic", source="hl_heuristic")
            return {
                "severity": "catastrophic",
                "kill_switch": True,
                "kill_reason": reason,
                "runtime_guards": [],
                "style_tweaks": {},
                "patch_summary": "heuristic kill switch",
                "operator_note": reason,
                "actions_taken": ["activated_kill_switch"],
                "_source": "heuristic",
            }

    wiki_meta = fetch_gambling_wiki_briefing(
        report_text=report_text,
        qual_summary=qual_summary,
    )
    user = _build_user_prompt(
        report_text=report_text,
        metrics=metrics,
        metrics_history=metrics_history or [],
        qual_summary=qual_summary,
        wiki_briefing=wiki_meta.get("text") or "",
    )
    raw = chat_json(system=_SYSTEM, user=user, max_tokens=4096)
    llm_meta = {k: raw.pop(k) for k in list(raw.keys()) if k.startswith("_llm")}
    result = apply_response(raw, dry_run=dry_run)
    result.update(llm_meta)
    result["_wiki_kb"] = {
        "char_count": wiki_meta.get("char_count", 0),
        "wiki_hits": wiki_meta.get("wiki_hits") or [],
        "queries": wiki_meta.get("queries") or [],
        "skipped": wiki_meta.get("skipped"),
        "error": wiki_meta.get("error"),
    }
    return result


def _write_artifacts(result: dict[str, Any]) -> None:
    _HL_DIR.mkdir(parents=True, exist_ok=True)
    _OUT_JSON.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    md = [
        "# HL auto-analyst (latest)",
        "",
        f"**Severity:** {result.get('severity')}",
        f"**Kill switch:** {result.get('kill_switch')} — {result.get('kill_reason', '')}",
        f"**Summary:** {result.get('patch_summary', '')}",
        "",
        result.get("operator_note") or "",
        "",
        f"**Actions:** {', '.join(result.get('actions_taken') or [])}",
        "",
        f"LLM: {result.get('_llm_provider')} / {result.get('_llm_model')}",
    ]
    wiki_kb = result.get("_wiki_kb") or {}
    if wiki_kb.get("wiki_hits"):
        md.append("")
        md.append(f"**Wiki hits:** {', '.join(wiki_kb['wiki_hits'][:8])}")
    _OUT_MD.write_text("\n".join(md) + "\n", encoding="utf-8")
    state = {
        "last_run": result.get("updated_at") or "",
        "severity": result.get("severity"),
        "kill_switch": result.get("kill_switch"),
        "actions": result.get("actions_taken"),
    }
    AUTO_ANALYST_STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    AUTO_ANALYST_STATE_PATH.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")


def maybe_run_after_analyze(
    *,
    report_path: Path,
    metrics: dict | None,
    reports_dir: Path,
    qual_summary: str = "",
) -> dict[str, Any] | None:
    if os.environ.get("CEMINI_HL_AUTO_ANALYST", "1").strip().lower() in ("0", "false", "no"):
        print("[hl-auto-analyst] disabled (CEMINI_HL_AUTO_ANALYST=0)")
        return None
    if not os.environ.get("DEEPSEEK_API_KEY") and not os.environ.get("OPENROUTER_API_KEY"):
        print("[hl-auto-analyst] skip: no DEEPSEEK_API_KEY or OPENROUTER_API_KEY")
        return None
    report_text = report_path.read_text(encoding="utf-8")
    history = _metrics_tail(reports_dir, 3)
    print("[hl-auto-analyst] calling LLM (DeepSeek primary → OpenRouter fallback on quota/outage)...")
    result = run_auto_analyst(
        report_text=report_text,
        metrics=metrics,
        metrics_history=history,
        qual_summary=qual_summary,
    )
    from datetime import datetime, timezone
    result["updated_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    _write_artifacts(result)
    print(
        f"[hl-auto-analyst] severity={result.get('severity')} "
        f"kill={result.get('kill_switch')} actions={result.get('actions_taken')}"
    )
    return result


def main(argv: list[str] | None = None) -> int:
    load_dotenv()
    _load_osint_routing_env()
    load_librarian_env()
    p = argparse.ArgumentParser(description="HL auto-analyst (DeepSeek + failover)")
    p.add_argument("--report", default=str(_DEFAULT_REPORT))
    p.add_argument("--dry-run", action="store_true", help="LLM only; do not write guards/kill")
    p.add_argument("--reports-dir", default=str(_AGENT_DIR / "reports"))
    args = p.parse_args(argv)

    report_path = Path(args.report)
    if not report_path.is_file():
        print(f"ERROR: report not found: {report_path}", file=sys.stderr)
        return 2

    reports_dir = Path(args.reports_dir)
    history = _metrics_tail(reports_dir, 3)
    metrics = history[-1] if history else None
    result = run_auto_analyst(
        report_text=report_path.read_text(encoding="utf-8"),
        metrics=metrics,
        metrics_history=history,
        dry_run=args.dry_run,
    )
    from datetime import datetime, timezone
    result["updated_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if not args.dry_run:
        _write_artifacts(result)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
