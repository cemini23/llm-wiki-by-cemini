"""RecursiveLink-inspired token-prior optimization.

Translates four RecursiveLink design principles to Path B (API-only) token priors:

1. Residual alignment: prior = base_prior + delta_branch
   - The base prior preserves accumulated calibration knowledge
   - The delta branch captures distribution shifts from recent decisions
   - Mirrors RecursiveLink's Rin(h) = h + W2 σ(W1 h)

2. Cosine similarity → alignment scoring
   - Cheap DeepSeek-chat call scores whether a routing path was appropriate
   - Uses a lightweight prompt (~50 tokens) to emulate embedding-space alignment
   - Mirrors Lin = 1 - cos(Rin(H), Emb(y))

3. Distribution-shift-only → per-stage attribution
   - Each decision attributes outcome to the specific stage that influenced it
   - Only priors for drifted stages are updated; stable stages keep their prior
   - Mirrors RecursiveLink's residual branch learning only the shift

4. Shared gradient credit → joint prior optimization
   - Failed routes are analyzed to find the bottleneck stage
   - Successful routes distribute credit across all stages
   - Mirrors outer-loop backprop through the full recursive unrolling
"""

from __future__ import annotations

import json
import logging
from typing import Any

logger = logging.getLogger(__name__)

# Incremented each time priors are rebuilt. Logged with every decision so
# we know which prior version guided a given routing path.
PRIOR_VERSION_KEY = "__prior_version__"


class ResidualPriorBuilder:
    """Build token priors using RecursiveLink-inspired residual composition.

    Instead of rewriting priors from scratch, computes deltas against the
    previous version and preserves stable knowledge in the base branch.
    """

    def __init__(self, api) -> None:
        self._api = api  # DeepSeekClient — used for alignment scoring

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def build(
        self,
        decisions: list[dict[str, Any]],
        previous_priors: dict[str, str] | None = None,
    ) -> dict[str, str]:
        """Build (or rebuild) token priors from routing decisions.

        If previous_priors is provided, operates in residual mode: extracts
        the base from the previous prior and adds a delta branch capturing
        recent distribution shifts.
        """
        if not decisions:
            return {"taxonomy": "", "cascade_judge": "", "tool_routing": ""}

        prev = previous_priors or {}
        return {
            "taxonomy": self._build_residual(
                "taxonomy", decisions, prev.get("taxonomy", "")
            ),
            "cascade_judge": self._build_residual(
                "cascade_judge", decisions, prev.get("cascade_judge", "")
            ),
            "tool_routing": self._build_residual(
                "tool_routing", decisions, prev.get("tool_routing", "")
            ),
        }

    def score_alignment(self, decision: dict[str, Any]) -> float:
        """Score how well a prior-guided routing aligned with the query intent.

        Uses a lightweight prompt (~50 tokens) on the cheapest model to emulate
        what cosine similarity would measure if we had embedding access.

        Returns a score 0.0–1.0 where:
        - 1.0: routing path was perfectly appropriate for the query
        - 0.0: routing path was wrong for this query type
        """
        query_text = decision.get("query", "")[:200]
        taxonomy = decision.get("taxonomy_class", "unknown")
        model = decision.get("final_model", "unknown")
        tools = decision.get("tool_calls", [])
        outcome = decision.get("outcome", "unknown")

        prompt = (
            f"Query: {query_text}\n"
            f"Classified as: {taxonomy}\n"
            f"Routed to: {model}\n"
            f"Tools: {', '.join(tools) if tools else 'none'}\n"
            f"Outcome: {outcome}\n\n"
            "Rate routing appropriateness 0.0-1.0. Output only the number."
        )

        try:
            raw, _ = self._api.complete(
                prompt,
                model="deepseek-chat",
                temperature=0.0,
                max_tokens=8,
            )
            # Parse float from response
            import re
            match = re.search(r"(\d+\.?\d*)", raw)
            if match:
                return max(0.0, min(1.0, float(match.group(1))))
        except Exception:
            pass
        # Fallback heuristic: accepted = higher alignment
        return 0.8 if outcome == "accepted" else 0.4

    def attribute_stages(
        self, decisions: list[dict[str, Any]]
    ) -> dict[str, list[dict[str, Any]]]:
        """Attribute routing outcomes to individual pipeline stages.

        For each decision, determines which stage was the primary driver
        of the outcome. This enables targeted prior updates — only the
        stage that drifted gets a delta, stable stages retain their prior.

        Returns a dict mapping stage → list of decisions where that stage
        was the primary contributor.
        """
        attribution: dict[str, list[dict[str, Any]]] = {
            "taxonomy": [],
            "cascade_judge": [],
            "tool_routing": [],
        }

        for d in decisions:
            primary = self._find_primary_stage(d)
            if primary in attribution:
                attribution[primary].append(d)

        return attribution

    # ------------------------------------------------------------------
    # Residual prior composition
    # ------------------------------------------------------------------

    def _build_residual(
        self,
        stage: str,
        decisions: list[dict[str, Any]],
        previous_prior: str,
    ) -> str:
        """Build a residual prior for one stage.

        If previous_prior is empty: full bootstrap from scratch (first run).
        If previous_prior exists: extract BASE, compute DELTA from recent
        decisions, combine as BASE + DELTA.
        """
        if not previous_prior:
            return self._bootstrap_prior(stage, decisions)

        # Split previous prior into base and delta components
        base = self._extract_base(previous_prior)

        # Compute delta from decisions since last build
        delta = self._compute_delta(stage, decisions)

        if not delta:
            return previous_prior  # no drift, preserve existing

        version = self._next_version(previous_prior)
        return f"{base}\n\n[RESIDUAL DELTA v{version}]\n{delta}"

    def _bootstrap_prior(self, stage: str, decisions: list[dict[str, Any]]) -> str:
        """First-run prior construction from scratch."""
        builders = {
            "taxonomy": self._build_taxonomy_body,
            "cascade_judge": self._build_judge_body,
            "tool_routing": self._build_tool_body,
        }
        body = builders.get(stage, lambda d: "")(decisions)
        if not body:
            return ""
        return f"[BASE PRIOR v1]\n{body}"

    def _extract_base(self, prior: str) -> str:
        """Extract the base component from a residual prior.

        Splits on the first [RESIDUAL DELTA ...] marker. Everything before
        it is the base (accumulated stable knowledge). Deltas are recomputed
        from fresh data each build.
        """
        marker = "[RESIDUAL DELTA v"
        idx = prior.find(marker)
        if idx == -1:
            # No delta component yet; entire prior is base
            return prior
        return prior[:idx].rstrip()

    def _compute_delta(self, stage: str, decisions: list[dict[str, Any]]) -> str:
        """Compute the distribution-shift delta from recent decisions.

        Only captures changes since the last build — not the full distribution.
        This is the "MLP branch" that learns alignment shifts while the base
        (residual path) preserves accumulated knowledge.
        """
        # Use only recent, high-alignment decisions
        recent = [d for d in decisions if d.get("alignment_score", 0.5) > 0.6]
        if not recent:
            return ""

        builders = {
            "taxonomy": self._build_taxonomy_delta,
            "cascade_judge": self._build_judge_delta,
            "tool_routing": self._build_tool_delta,
        }
        return builders.get(stage, lambda d: "")(recent)

    def _next_version(self, prior: str) -> int:
        """Extract the next version number from existing prior."""
        import re
        versions = re.findall(r"v(\d+)", prior)
        if not versions:
            return 2
        return max(int(v) for v in versions) + 1

    # ------------------------------------------------------------------
    # Body builders — full bootstrap (first run)
    # ------------------------------------------------------------------

    def _build_taxonomy_body(self, decisions: list[dict[str, Any]]) -> str:
        class_counts: dict[str, int] = {}
        class_avg_conf: dict[str, list[float]] = {}
        for d in decisions:
            tc = d.get("taxonomy_class", "general_question")
            class_counts[tc] = class_counts.get(tc, 0) + 1
            class_avg_conf.setdefault(tc, []).append(float(d.get("taxonomy_confidence", 0.0)))

        if not class_counts:
            return ""

        total = sum(class_counts.values())
        top = sorted(class_counts.items(), key=lambda x: -x[1])[:5]
        lines = [
            "[ROUTING PRIOR — built from calibration data]",
            f"Based on {total} historical queries, the most common query types are:",
        ]
        for cls, count in top:
            pct = count / total * 100
            avg_c = (sum(class_avg_conf.get(cls, [0])) / len(class_avg_conf[cls])
                     if class_avg_conf.get(cls) else 0.0)
            lines.append(f"  {cls}: {count} queries ({pct:.0f}%, avg confidence {avg_c:.2f})")
        lines.append("Prefer the most specific applicable class. Default to ticker_lookup "
                      "for symbol queries, not general_question.")
        return " ".join(lines)

    def _build_judge_body(self, decisions: list[dict[str, Any]]) -> str:
        if not decisions:
            return ""
        accepted = sum(1 for d in decisions if d.get("outcome") == "accepted")
        escalated = sum(1 for d in decisions if d.get("outcome") == "escalated")
        total = len(decisions)
        escalations = [d for d in decisions if d.get("outcome") == "escalated"]
        model_counts: dict[str, int] = {}
        for d in escalations:
            fm = d.get("final_model", "unknown")
            model_counts[fm] = model_counts.get(fm, 0) + 1

        return (
            f"[JUDGE PRIOR — built from {total} evaluations] "
            f"First model accepted {accepted}/{total} queries ({accepted/total*100:.0f}%). "
            f"When escalation was needed ({escalated} cases), final model distribution: "
            + ", ".join(f"{m}: {c}" for m, c in model_counts.items())
            + ". Prefer accepting responses that are factually grounded and cite sources. "
            "Be more strict for options_analysis and quantitative_methods queries."
        )

    def _build_tool_body(self, decisions: list[dict[str, Any]]) -> str:
        if not decisions:
            return ""
        tool_benefit: dict[str, list[float]] = {}
        for d in decisions:
            tools = d.get("tool_calls", [])
            outcome = d.get("outcome", "")
            for t in tools:
                tool_benefit.setdefault(t, []).append(
                    1.0 if outcome == "accepted" else 0.5
                )
        lines = [
            "[TOOL PRIOR — built from calibration data]",
            "Tool effectiveness from historical routing:",
        ]
        for tool, scores in sorted(tool_benefit.items()):
            avg = sum(scores) / len(scores) if scores else 0.0
            lines.append(f"  {tool}: effectiveness {avg:.2f} ({len(scores)} uses)")
        lines.append("Use kb_search for factual lookups and ticker queries. "
                      "Use stash_recall for research synthesis and options analysis "
                      "where prior context helps.")
        return " ".join(lines)

    # ------------------------------------------------------------------
    # Delta builders — distribution-shift-only updates
    # ------------------------------------------------------------------

    def _build_taxonomy_delta(self, decisions: list[dict[str, Any]]) -> str:
        """Taxonomy delta: new query patterns not covered by base prior."""
        class_counts: dict[str, int] = {}
        for d in decisions:
            tc = d.get("taxonomy_class", "general_question")
            class_counts[tc] = class_counts.get(tc, 0) + 1

        if not class_counts:
            return ""
        total = sum(class_counts.values())
        top = sorted(class_counts.items(), key=lambda x: -x[1])[:3]
        parts = [f"Recent shift ({len(decisions)} high-alignment queries):"]
        for cls, count in top:
            pct = count / total * 100
            parts.append(f"  {cls}: {pct:.0f}% of recent traffic")
        return " ".join(parts)

    def _build_judge_delta(self, decisions: list[dict[str, Any]]) -> str:
        """Judge delta: changes in escalation patterns."""
        if not decisions:
            return ""
        accepted = sum(1 for d in decisions if d.get("outcome") == "accepted")
        escalated = sum(1 for d in decisions if d.get("outcome") == "escalated")
        total = len(decisions)
        rate = accepted / total * 100 if total else 0

        delta_str = (
            f"Recent shift ({total} high-alignment queries): "
            f"first-try accept rate now {rate:.0f}%"
        )
        # Flag classes where escalation increased
        esc_by_class: dict[str, int] = {}
        for d in decisions:
            if d.get("outcome") == "escalated":
                tc = d.get("taxonomy_class", "unknown")
                esc_by_class[tc] = esc_by_class.get(tc, 0) + 1
        if esc_by_class:
            worst = sorted(esc_by_class.items(), key=lambda x: -x[1])[:3]
            delta_str += ". Escalation hot spots: " + ", ".join(
                f"{c}: {n}" for c, n in worst
            )
        return delta_str

    def _build_tool_delta(self, decisions: list[dict[str, Any]]) -> str:
        """Tool delta: shifts in tool effectiveness."""
        if not decisions:
            return ""
        tool_scores: dict[str, list[float]] = {}
        for d in decisions:
            tools = d.get("tool_calls", [])
            outcome = d.get("outcome", "")
            for t in tools:
                tool_scores.setdefault(t, []).append(
                    1.0 if outcome == "accepted" else 0.5
                )
        if not tool_scores:
            return ""
        parts = [f"Recent shift ({len(decisions)} high-alignment queries):"]
        for tool, scores in sorted(tool_scores.items()):
            avg = sum(scores) / len(scores) if scores else 0.0
            parts.append(f"  {tool}: recent effectiveness {avg:.2f} ({len(scores)} uses)")
        return " ".join(parts)

    # ------------------------------------------------------------------
    # Stage attribution
    # ------------------------------------------------------------------

    def _find_primary_stage(self, decision: dict[str, Any]) -> str:
        """Determine which pipeline stage was the primary outcome driver.

        Heuristic (no gradient access):
        - If taxonomy confidence < 0.5: taxonomy was the bottleneck
        - If first model rejected (escalated): cascade_judge
        - If tools used and outcome accepted: tool_routing
        - Default: cascade_judge (it makes the final accept/reject call)
        """
        conf = float(decision.get("taxonomy_confidence", 0.0))
        if conf < 0.5:
            return "taxonomy"

        outcome = decision.get("outcome", "")
        tools = decision.get("tool_calls", [])

        if outcome == "escalated":
            # Cascade judge made the call to escalate — it's the primary
            return "cascade_judge"

        if tools and outcome == "accepted":
            # Tools contributed to a successful first-try accept
            cascade_path = decision.get("cascade_path", [])
            if len(cascade_path) == 1:
                return "tool_routing"

        return "cascade_judge"
