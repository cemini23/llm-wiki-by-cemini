"""Data structures for Conductor pipeline inter-module communication."""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Any


@dataclass
class Query:
    text: str
    source: str  # "analyst", "cli", "mcp"
    session_id: str
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass
class TaxonomyClass:
    name: str  # e.g. "options_analysis"
    confidence: float  # 0.0-1.0
    reasoning: str = ""


@dataclass
class ModelPool:
    taxonomy_class: str
    models: list[str]  # ordered cheapest-first
    default_model: str


@dataclass
class RoutingDecision:
    query: Query
    taxonomy: TaxonomyClass
    selected_model: str
    cascade_path: list[str] = field(default_factory=list)
    confidence_scores: list[float] = field(default_factory=list)
    tool_calls: list[str] = field(default_factory=list)
    final_model: str = ""
    outcome: str = ""  # "accepted", "escalated", "rejected"
    cost_estimate: float = 0.0
    latency_ms: float = 0.0


@dataclass
class ConductorResponse:
    query: Query
    routing: RoutingDecision
    content: str
    sources: list[str] = field(default_factory=list)
    tool_results: list[dict[str, Any]] = field(default_factory=list)


@dataclass
class EvalScores:
    correctness: float
    routing_quality: float
    cost_efficiency: float
    tool_appropriateness: float
    reasoning: str = ""


@dataclass
class EvalReport:
    period_start: str
    period_end: str
    total_decisions: int
    evaluated: int
    gold_standard_sample: int
    scores: dict[str, dict[str, float]]  # dimension -> {mean, std}
    judge_bias_correction: dict[str, float]
    escalation_rate: float
    avg_cost_per_query: float
    baseline_cost_per_query: float
    cost_savings_pct: float
