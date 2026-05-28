"""Re-export shared metrics (compat)."""
from backtest_common.metrics import compute_metrics, per_segment_summary, trades_to_equity

__all__ = ["compute_metrics", "per_segment_summary", "trades_to_equity"]
