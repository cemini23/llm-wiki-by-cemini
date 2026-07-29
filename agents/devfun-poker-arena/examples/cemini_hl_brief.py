#!/usr/bin/env python3
"""Assemble HL analyst brief from Arena analyze report (OSINT brief shape).

Used by `examples/cemini_hl_loop.sh` step 2. Output is paste-ready for Cursor.

Usage:
    uv run python examples/cemini_hl_brief.py --report reports/analyze/latest.txt
    uv run python examples/cemini_hl_brief.py --report /tmp/analyze.txt --round 3
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
from datetime import date
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parent
_AGENT_DIR = _EXAMPLES.parent
_PROMPT = _AGENT_DIR / "prompts" / "cemini_hl_analyst_prompt.md"
_FIXTURES = _AGENT_DIR / "tests" / "fixtures" / "regression_spots.py"
_DEFAULT_OUT = _AGENT_DIR / "reports" / "hl-loop" / "latest_brief.md"


def segment_select_cap(
    segments: list[dict],
    query_tags: list[str],
    cap: int | None = None,
) -> tuple[list[dict], list[dict]]:
    """K144 MaRA-style rank + cap before HL brief expansion (advisory only).

    Each segment: ``{"id": str, "tags": [...], "text": str}``.
    Returns ``(kept, dropped)`` sorted by tag/keyword overlap score.
    """
    if cap is None:
        cap = int(os.environ.get("CEMINI_HL_SEGMENT_CAP", "8"))
    cap = max(1, cap)

    norm_tags = [t.strip().lower() for t in query_tags if str(t).strip()]
    tag_set = set(norm_tags)

    def _score(seg: dict) -> float:
        seg_tags = {str(t).strip().lower() for t in (seg.get("tags") or [])}
        overlap = len(tag_set & seg_tags)
        text = str(seg.get("text") or "").lower()
        keyword_hits = sum(1 for t in norm_tags if t and t in text)
        return float(overlap * 2 + keyword_hits)

    ranked = sorted(segments, key=_score, reverse=True)
    kept = ranked[:cap]
    dropped = ranked[cap:]

    if os.environ.get("CEMINI_HL_SEGMENT_AUDIT") == "1" and dropped:
        dropped_ids = [str(s.get("id") or "?") for s in dropped]
        print(
            f"[hl-brief] segment_select_cap dropped {len(dropped)} "
            f"(cap={cap}): {', '.join(dropped_ids)}",
            file=sys.stderr,
        )
    return kept, dropped


def _report_segments(report_text: str) -> list[dict]:
    """Split analyze report into candidate segments (delta / loss lines)."""
    segments: list[dict] = []
    for i, line in enumerate((report_text or "").splitlines()):
        s = line.strip()
        if not s:
            continue
        tags: list[str] = []
        if "delta=" in s.lower():
            tags.append("delta")
        if "loss" in s.lower():
            tags.append("loss")
        if s.startswith("#"):
            tags.append("headline")
        segments.append({"id": f"report_line_{i}", "tags": tags, "text": s})
    return segments


def _segments_from_report(report_text: str, query_tags: list[str]) -> tuple[str, list[dict], list[dict]]:
    """Apply segment_select_cap to report lines; return joined kept text."""
    segs = _report_segments(report_text)
    if not segs:
        return report_text, [], []
    kept, dropped = segment_select_cap(segs, query_tags)
    kept_text = "\n".join(str(s.get("text") or "") for s in kept)
    if len(kept) < len(segs):
        kept_text += (
            f"\n\n(segment_select_cap: kept {len(kept)}/{len(segs)} lines — advisory K144)"
        )
    return kept_text, kept, dropped


def _git_short_sha() -> str:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=str(_AGENT_DIR),
            stderr=subprocess.DEVNULL,
            text=True,
        )
        return out.strip()
    except Exception:
        return "unknown"


def _regression_inventory() -> str:
    if not _FIXTURES.is_file():
        return "(regression_spots.py not found)\n"
    text = _FIXTURES.read_text(encoding="utf-8")
    lines: list[str] = []
    spot_id = ""
    notes = ""
    for raw in text.splitlines():
        s = raw.strip()
        if s.startswith('id="'):
            spot_id = s.split('"')[1]
        elif s.startswith("notes="):
            val = s.split("=", 1)[1].strip()
            if val.startswith('"'):
                end = val.rfind('"')
                notes = val[1:end] if end > 0 else val.strip('"')
        elif s.startswith("RegressionSpot(") and spot_id:
            lines.append(f"- `{spot_id}` — {notes}")
            spot_id = ""
            notes = ""
    if not lines:
        return "(parse regression_spots manually)\n"
    return "\n".join(lines) + "\n"


def _spot_fail_count_from_report(report: str) -> int:
    """Heuristic: count loss markers / repeated #delta lines as fail count."""
    n = 0
    for line in (report or "").splitlines():
        s = line.strip().lower()
        if "delta=" in s or s.startswith("#") and "loss" in s:
            n += 1
        elif "chip_delta" in s and "-" in s:
            n += 1
    return max(1, n) if report.strip() else 1


def _stigmergy_section(*, top_leak_hint: str, fail_count: int) -> str:
    """K141: advisory spot-class shortlist after K161 eligibility."""
    try:
        from stigmergy_spot_scores import StigmergySpotScores, stigmergy_brief_section

        store = StigmergySpotScores()
        # Seed pressure from this round's leak so the brief shows ranking intent.
        leak_key = (top_leak_hint or "unknown_leak").strip()[:80] or "unknown_leak"
        if fail_count >= 2:
            store.update_score(leak_key, "pressure", float(min(fail_count, 5)))
            store.update_score(leak_key, "block", 1.0)
        elif top_leak_hint:
            store.update_score(leak_key, "pressure", 1.0)
        classes = [leak_key, "default_regression_mix"]
        return stigmergy_brief_section(classes, scores=store)
    except Exception:
        return (
            "### Stigmergic spot shortlist (K141 — advisory)\n\n"
            "(stigmergy helper unavailable — use K161 filter order)\n"
        )


def _scaffold_and_reflection_sections(
    *,
    report_text: str,
    top_leak_hint: str,
    fail_count: int,
) -> str:
    """K139: four-field scaffold + staged reflection strength + K141 stigmergy."""
    try:
        from researcher_trajectory_summary import (
            load_deepsearch_trajectory_filter_config,
            staged_reflection_hint,
            scaffold_block_for_brief,
        )

        cfg = load_deepsearch_trajectory_filter_config()
        scaffold = scaffold_block_for_brief(
            report_text=report_text,
            leak_hint=top_leak_hint,
            fail_count=fail_count,
            config=cfg,
        )
        hint = staged_reflection_hint(fail_count, config=cfg)
    except Exception:
        scaffold = {
            "completed_list": ["(fill verified facts: stack, board class, HUD tag)"],
            "todo_list": ["(next decide() checks / regression spot)"],
            "experience": "" if fail_count < 2 else "(required: prior same-spot lessons)",
            "information": ["(evidence tokens: cards/street/action)"],
        }
        strength = "soft" if fail_count < 2 else "strong_grounded"
        hint = (
            "recheck sizing vs HUD"
            if strength == "soft"
            else "cite concrete board/street leak or veto (grounded)"
        )

    exp = scaffold.get("experience") or ""
    exp_note = (
        "REQUIRED after ≥2 same-spot fails"
        if fail_count >= 2
        else "optional on first fail"
    )
    stig_md = _stigmergy_section(top_leak_hint=top_leak_hint, fail_count=fail_count)
    return f"""### DeepSearch scaffold (K139 / K161 delta)

Four-field memory before mix (advisory). Map: completed_list / todo_list /
experience / information. Drop units lacking `experience` after ≥2 same-spot fails.

| Field | Content |
|-------|---------|
| completed_list | {scaffold.get("completed_list")} |
| todo_list | {scaffold.get("todo_list")} |
| experience ({exp_note}) | {exp or "(empty)"} |
| information | {scaffold.get("information")} |

Staged reflection (fail_count≈{fail_count}): **{hint}**

{stig_md}
### Belief audit (K167)

See auto-appended block below when parse succeeds. Tags:
`harmful_mistake` | `justified_override` | `strategic`. Batch-improve only.
"""

def build_brief(
    *,
    report_text: str,
    round_n: int,
    match_id: str,
    top_leak_hint: str,
    cap_slice: str = "(capability tree slice unavailable)",
    belief_audit_md: str = "",
) -> str:
    today = date.today().isoformat()
    sha = _git_short_sha()
    prompt_body = ""
    if _PROMPT.is_file():
        prompt_body = _PROMPT.read_text(encoding="utf-8")
    else:
        prompt_body = "(prompt template missing — see prompts/cemini_hl_analyst_prompt.md)\n"

    reg = _regression_inventory()
    summary_leak = top_leak_hint or "See analyze worst-hands section — pick #1 leak."
    fail_count = _spot_fail_count_from_report(report_text)
    scaffold_md = _scaffold_and_reflection_sections(
        report_text=report_text,
        top_leak_hint=summary_leak,
        fail_count=fail_count,
    )
    belief_section = belief_audit_md or (
        "### Belief audit (K167)\n\n"
        "(no belief/taken pair parsed — fill manually from analyze)\n"
    )

    return f"""---
title: "Cemini HL analyst round {round_n} — cemini_decide patch"
type: brief
tags: [brief, poker, hl-loop, cemini-decide, devfun-arena]
created: {today}
target: examples/cemini_decide.py
---

## Target

`agents/devfun-poker-arena/examples/cemini_decide.py` — prod decide() on cemini-prod.
**Not** `examples/agent.py`.

## Summary

HL analyst round **{round_n}**: patch **one** leak from Arena analyze (competition
`{match_id}`), gate with pytest + regression spots + EP VPIP self-play audit, then
deploy. Self-play thousands of hands is **verification only**, not the trainer.

Primary leak candidate: {summary_leak}

## Body

### Workflow (this round)

```
analyze → LLM patch (this brief) → cemini_preflight.sh → deploy (optional)
```

### Gate requirements (mandatory before deploy)

| Gate | Command | Pass criteria |
|------|---------|---------------|
| Unit + regression | `pytest tests/` | All green |
| EP VPIP + trash | `cemini_selfplay_audit.py --gate` | EP VPIP ≤ 22%, 0 trash opens |
| Lobby smoke | `agent.py --dry-run` | 15 hands, no crash |

Self-play bb/100 is **informational** — do not optimize decide() for self-play scores.

### Patch scope (ONE leak)

- Edit `cemini_decide.py` only; smallest diff.
- If leak repeats after a prior fix, add/update `tests/fixtures/regression_spots.py`.
- Do not widen EP opens to "fix" maniac tables — tighten trash, fix HUD cold-start.

{scaffold_md}

{belief_section}

### GenomeDiff (K155 — required before ship)

Fill before deploy. Task co-location ≠ lineage — name the **driver mechanism**.
See `references/patch-genome-diff.md`.

| Field | Value |
|-------|-------|
| Parent mechanism | (named heuristic/guard being extended) |
| Delta | `mutate` \\| `novel` |
| Inherited | … |
| Mutated | … |
| Lost | … (and why) |
| Novel | … |
| Verification | regression spot id / pytest / gate command |

Compositional gate: parent + delta + verification must agree
(`examples/patch_genome_diff.py` → `validate_genome_diff`).

### Capability tree (K164 — lazy tools)

Do **not** dump the full tool/schema registry into the analyst prompt. Route through
one active domain (`table` / `policy` / `memory` / `eval` / `submit`) with LIFO
push/pop for nested MAFP vs exploit work. Submit requires Prebind.
See `references/capability-tree-routing.md`.

Active slice (example after nested return):

```
{cap_slice}
```

### Frozen regression spots (must stay green)

{reg}

### Arena analyze report

```
{report_text.strip()}
```

### Analyst prompt (paste block below into Cursor if not auto-loaded)

{prompt_body}

## Sources

- @wiki/concepts/poker-hl-analyst-loop.md
- @wiki/entities/bots/cemini-devfun-poker-agent.md
- `docs/TESTING-CEMINI.md`
- @osint-wiki/concepts/cemini-knowledge-application-architecture.md — brief→verify→deploy pattern
- `references/deepsearch-trajectory-filter.md` — K161 + K139 scaffold delta
- `references/stigmergy-spot-scores.md` — K141 advisory shortlist after K161
- `references/play-adequacy-gates.md` — K158 play vs transition ship gates
- `examples/belief_deviation_audit.py` — K167 belief audit

## Implementation status

| Field | Value |
|-------|-------|
| Status | NOT_STARTED |
| Implemented by | (HL analyst / operator) |
| Git SHA (pre-patch) | `{sha}` |
| Verified | — |
| Proof | `./scripts/cemini_preflight.sh` exit 0 |
| Follow-up | Re-analyze after ~50 live hands; freeze top new leak |
"""


def _top_leak_from_report(report: str) -> str:
    for line in report.splitlines():
        s = line.strip()
        if s.startswith("#") and "delta=" in s:
            return s.lstrip("#").strip()
    return ""


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Build HL analyst brief from analyze report")
    p.add_argument("--report", required=True, help="Path to failure analyze .txt")
    p.add_argument("--out", default=str(_DEFAULT_OUT), help="Output brief path")
    p.add_argument("--round", type=int, default=1, help="HL iteration number")
    p.add_argument("--match", default="", help="Arena competitionId")
    args = p.parse_args(argv)

    report_path = Path(args.report)
    if not report_path.is_file():
        print(f"ERROR: report not found: {report_path}", file=sys.stderr)
        return 2

    report_text = report_path.read_text(encoding="utf-8")
    hint = _top_leak_from_report(report_text)

    query_tags = [t for t in (hint or "").replace("#", " ").split() if t.strip()]
    if hint:
        query_tags.extend(["delta", "loss", "leak"])
    report_text, kept_segs, dropped_segs = _segments_from_report(report_text, query_tags)
    if kept_segs or dropped_segs:
        print(
            f"[hl-brief] segment_select_cap kept={len(kept_segs)} "
            f"dropped={len(dropped_segs)} cap={os.environ.get('CEMINI_HL_SEGMENT_CAP', '8')}",
            file=sys.stderr,
        )

    belief_audit_md = ""
    belief_block: dict | None = None
    try:
        from belief_deviation_audit import (
            append_belief_deviation_jsonl,
            build_belief_audit,
            extract_belief_from_report,
            format_belief_audit_markdown,
        )

        parsed = extract_belief_from_report(report_text)
        belief_block = build_belief_audit(
            belief_action=parsed.get("belief_action") or "unknown",
            taken_action=parsed.get("taken_action") or "unknown",
            belief_source="chart_or_hud",
            outcome="loss",
            note=hint or "",
            hand_id=f"hl-round-{args.round}",
        )
        belief_audit_md = format_belief_audit_markdown(belief_block)
        jpath = append_belief_deviation_jsonl(belief_block)
        print(f"wrote belief_deviation jsonl → {jpath}")
    except Exception as exc:  # pragma: no cover
        print(f"[hl-brief] belief-audit skip: {exc}", file=sys.stderr)

    cap_slice = "(capability tree slice unavailable)"
    try:
        from capability_tree import (
            CapabilityFrameStack,
            load_capability_tree_config,
            simulate_hu_researcher_nested_session,
        )
        import json as _json

        stack = CapabilityFrameStack(config=load_capability_tree_config())
        stack.push("eval", focus="researcher_round", label="hl_root")
        stack.push("policy", focus="postflop_heuristic", label="leak_lane")
        stack.push("memory", focus="genome_diff", label="lineage_check")
        stack.pop()  # return to leak_lane
        cap_slice = _json.dumps(stack.visible_slice(), indent=2)
        # Persist nested-session smoke beside brief (operator checklist)
        session = simulate_hu_researcher_nested_session(prebind_ok=True)
        session_path = Path(args.out).with_suffix(".capability-session.json")
        session_path.parent.mkdir(parents=True, exist_ok=True)
        session_path.write_text(
            _json.dumps(session, indent=2) + "\n", encoding="utf-8"
        )
        print(f"wrote capability nested-session → {session_path}")
    except Exception as exc:  # pragma: no cover
        print(f"[hl-brief] capability-tree skip: {exc}", file=sys.stderr)

    brief = build_brief(
        report_text=report_text,
        round_n=args.round,
        match_id=args.match or "(from env ARENA_LOBBY_COMPETITION_ID)",
        top_leak_hint=hint,
        cap_slice=cap_slice,
        belief_audit_md=belief_audit_md,
    )

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(brief, encoding="utf-8")
    print(f"wrote → {out}")

    # K163: HL failure trace as message DAG (messages stored once, nodes ref)
    try:
        from message_dag_trace import build_hl_failure_dag
        import json as _json

        turns = [
            {
                "role": "system",
                "content": "HL analyst brief scaffold",
                "tag": "harness",
            },
            {
                "role": "user",
                "content": report_text.strip()[:4000],
                "tag": "analyze",
            },
            {
                "role": "assistant",
                "content": f"round={args.round} leak={hint or 'TBD'}",
                "tag": "hl",
            },
        ]
        if belief_block is not None:
            turns.append(
                {
                    "role": "system",
                    "content": _json.dumps({"belief_audit": belief_block}),
                    "tag": "belief_audit",
                }
            )
        dag = build_hl_failure_dag(turns, layer="harness")
        dag_path = out.with_suffix(".dag.json")
        dag.save(dag_path)
        print(f"wrote message-DAG → {dag_path}")
    except Exception as exc:  # pragma: no cover — optional sibling artifact
        print(f"[hl-brief] message-DAG skip: {exc}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
