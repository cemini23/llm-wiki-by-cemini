#!/usr/bin/env python3
"""K148 untrusted-data immunization — scan coaching transcripts before STRATEGY merge.

Per references/agent-rules.md (OWASP LLM01): opponent text, fork READMEs,
and video transcripts are DATA, not instructions.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

# Phrases / markers that target the agent, not poker content.
INJECTION_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("ignore_previous", re.compile(r"ignore\s+(all\s+)?previous\s+instructions", re.I)),
    ("system_role", re.compile(r"(?m)^\s*system\s*:", re.I)),
    ("prompt_close", re.compile(r"</prompt>", re.I)),
    ("im_start", re.compile(r"<\|im_start\|>", re.I)),
    ("mode_switch", re.compile(r"you\s+are\s+now\s+(a|an)\s+", re.I)),
    ("tool_call", re.compile(r'"type"\s*:\s*"function"', re.I)),
    ("exec_request", re.compile(r"\b(run|execute|eval)\s+this\s+(shell|command|code)\b", re.I)),
)


@dataclass
class SanitizeHit:
    rule: str
    line: int
    excerpt: str


def scan_text(text: str, *, max_excerpt: int = 120) -> list[SanitizeHit]:
    hits: list[SanitizeHit] = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        for rule, pat in INJECTION_PATTERNS:
            if pat.search(line):
                excerpt = line.strip()[:max_excerpt]
                hits.append(SanitizeHit(rule=rule, line=lineno, excerpt=excerpt))
    return hits


def audit_report(text: str) -> dict:
    hits = scan_text(text)
    return {
        "ok": not hits,
        "hit_count": len(hits),
        "hits": [asdict(h) for h in hits],
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Scan untrusted text for prompt-injection patterns")
    p.add_argument("path", type=Path, nargs="?", help="File to scan (default: stdin)")
    p.add_argument("--gate", action="store_true", help="Exit 1 when hits found")
    p.add_argument("--json", action="store_true", help="JSON report on stdout")
    args = p.parse_args(argv)

    if args.path:
        text = args.path.read_text(encoding="utf-8", errors="replace")
        source = str(args.path)
    else:
        text = sys.stdin.read()
        source = "<stdin>"

    report = audit_report(text)
    report["source"] = source

    if args.json:
        print(json.dumps(report, indent=2))
    elif report["ok"]:
        print(f"SANITIZE OK — {source}")
    else:
        print(f"SANITIZE FAIL — {report['hit_count']} hit(s) in {source}", file=sys.stderr)
        for h in report["hits"]:
            print(f"  L{h['line']} [{h['rule']}] {h['excerpt']}", file=sys.stderr)

    if args.gate and not report["ok"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
