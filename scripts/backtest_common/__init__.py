"""Shared backtest metrics and utilities."""

from .metrics import compute_metrics, per_segment_summary, trades_to_equity

__all__ = ["compute_metrics", "per_segment_summary", "trades_to_equity"]
