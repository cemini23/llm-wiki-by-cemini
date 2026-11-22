#!/usr/bin/env python3
"""License gate — block copyleft and non-commercial licenses from revenue code.

The gate answers one question: may this license enter a Cemini revenue product?

Three modes:
  integrate   — vendor the code into a revenue product. Copyleft and
                non-commercial licenses BLOCK.
  extract     — read the code for ideas, reimplement from scratch. Blocked
                licenses REVIEW.
  paper-only  — cite the work in a research note. Blocked licenses REVIEW but
                do not fail the run.

Classification:
  blocked — GPL-2.0, GPL-3.0, AGPL, SSPL, EUPL, BSL, Elastic-2.0 (ELv2),
            Commons-Clause, CC-BY-NC, NonCommercial, Non-Commercial, NC-,
            research-only, MiniMax-M2
  review  — LGPL, unknown, empty, or "not found" strings. LGPL is weak copyleft:
            it is not blocked, but the operator must read it before reuse.
  allowed — everything else (MIT, Apache-2.0, BSD, ISC, MPL-2.0, CC-BY, ...)

This module is importable (`classify`, `gate`) and runnable as a CLI. It makes
no network calls.

CLI:
  python3 scripts/license_gate.py --license "AGPL-3.0" --mode integrate
  python3 scripts/license_gate.py --repo owner/name --mode integrate
  python3 scripts/license_gate.py --license "MIT" --json

Exit codes:
  0 — ALLOW, or REVIEW in paper-only mode
  1 — REVIEW (read the license before reuse)
  2 — BLOCK
  3 — usage error
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass

MODES = ("integrate", "extract", "paper-only")

# Exact-or-prefix matches, case-insensitive. `LGPL` is removed from the probe
# before the GPL patterns run, so LGPL-3.0 is not read as GPL-3.0.
BLOCKED_PATTERNS = (
    "GPL-2.0",
    "GPL-3.0",
    "AGPL",
    "SSPL",
    "EUPL",
    "BSL",
    "ELASTIC-2.0",
    "ELV2",              # common short id for Elastic License 2.0
    "COMMONS-CLAUSE",
    "CC-BY-NC",
    "NONCOMMERCIAL",
    "NON-COMMERCIAL",
    "NC-",
    "RESEARCH-ONLY",
    "MINIMAX-M2",
)

# Blocked families that are non-commercial rather than copyleft. These hits must
# carry the non-commercial note.
NONCOMMERCIAL_MARKERS = (
    "COMMONS-CLAUSE",
    "CC-BY-NC",
    "NONCOMMERCIAL",
    "NON-COMMERCIAL",
    "NC-",
    "RESEARCH-ONLY",
    "MINIMAX-M2",
)

REVIEW_MARKERS = ("LGPL", "LESSER GENERAL PUBLIC")

# Strings that mean "nobody has read the license yet".
UNKNOWN_VALUES = {
    "",
    "?",
    "-",
    "NONE",
    "NULL",
    "UNKNOWN",
    "NOASSERTION",
    "NOT FOUND",
    "NOTFOUND",
    "UNLICENSED",
    "API-ERROR",
    "N/A",
}

COPYLEFT_REASON = "GPL/AGPL family cannot be vendored into a revenue product"
NONCOMMERCIAL_REASON = "non-commercial model license — excluded from revenue repos"
REVIEW_REASON = "license is ambiguous or weak copyleft — read it before reuse"
ALLOW_REASON = "no blocking term found — reuse permitted under the license terms"


@dataclass
class GateResult:
    verdict: str        # BLOCK | REVIEW | ALLOW
    exit_code: int
    license: str
    mode: str
    reason: str


def _normalize(license_str: str | None) -> str:
    if not license_str:
        return ""
    return " ".join(str(license_str).split()).upper()


def _matched_pattern(norm: str) -> str | None:
    """Return the blocking pattern that matches, or None."""
    # Strip LGPL first: "LGPL-3.0" contains "GPL-3.0" as a substring.
    probe = norm.replace("LGPL", "")
    for pattern in BLOCKED_PATTERNS:
        if probe == pattern or probe.startswith(pattern):
            return pattern
    return None


def classify(license_str: str | None) -> str:
    """Return 'blocked' | 'review' | 'allowed' for one license string."""
    norm = _normalize(license_str)
    if norm in UNKNOWN_VALUES:
        return "review"
    if _matched_pattern(norm):
        return "blocked"
    if any(marker in norm for marker in REVIEW_MARKERS):
        return "review"
    return "allowed"


def is_noncommercial(license_str: str | None) -> bool:
    """True when the license is non-commercial rather than merely copyleft."""
    probe = _normalize(license_str).replace("LGPL", "")
    return any(marker in probe for marker in NONCOMMERCIAL_MARKERS)


def _reason(classification: str, norm: str) -> str:
    if classification == "blocked":
        if is_noncommercial(norm):
            return NONCOMMERCIAL_REASON
        return COPYLEFT_REASON
    if classification == "review":
        return REVIEW_REASON
    return ALLOW_REASON


def gate(license_str: str | None, mode: str) -> GateResult:
    """Return the gate decision for one license string in one mode."""
    if mode not in MODES:
        raise ValueError(f"mode must be one of {MODES}, got {mode!r}")
    norm = _normalize(license_str)
    classification = classify(license_str)
    reason = _reason(classification, norm)

    if classification == "blocked":
        if mode == "integrate":
            return GateResult("BLOCK", 2, license_str or "", mode, reason)
        if mode == "extract":
            return GateResult("REVIEW", 1, license_str or "", mode, reason)
        return GateResult("REVIEW", 0, license_str or "", mode, reason)

    if classification == "review":
        return GateResult("REVIEW", 1, license_str or "", mode, reason)

    return GateResult("ALLOW", 0, license_str or "", mode, ALLOW_REASON)


def render_line(result: GateResult) -> str:
    """One-line rendering: `<VERDICT>  <license>  <mode>  — <reason>`."""
    return f"{result.verdict}  {result.license}  {result.mode}  — {result.reason}"


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="License gate for Cemini revenue products.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--license", default=None, help="SPDX id or license text to classify")
    p.add_argument(
        "--repo",
        default=None,
        help="owner/name of a repository. Prints a reminder that the license must "
        "be read first. Never calls the network.",
    )
    p.add_argument(
        "--mode",
        choices=MODES,
        default="integrate",
        help="Where the code would land (default: integrate, the strictest mode)",
    )
    p.add_argument("--json", action="store_true", help="Emit a JSON object")
    return p


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if not args.license and not args.repo:
        print(
            "ERROR: give --license STR or --repo owner/name",
            file=sys.stderr,
        )
        parser.print_usage(sys.stderr)
        return 3

    if args.repo and not args.license:
        # A repo name is not a license. No network call: the operator reads it.
        result = GateResult(
            verdict="REVIEW",
            exit_code=1,
            license=args.repo,
            mode=args.mode,
            reason="license not read yet — fetch the LICENSE file first (no network call made)",
        )
    else:
        result = gate(args.license, args.mode)

    if args.json:
        print(json.dumps(asdict(result), indent=2))
    else:
        print(render_line(result))
    return result.exit_code


if __name__ == "__main__":
    sys.exit(main())
