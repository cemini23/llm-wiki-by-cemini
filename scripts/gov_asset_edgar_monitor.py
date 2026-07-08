#!/usr/bin/env python3
"""Backward-compatible entrypoint — see scripts.intel.monitors.edgar_fulltext."""
from scripts.intel.monitors.edgar_fulltext import main

if __name__ == "__main__":
    raise SystemExit(main())
