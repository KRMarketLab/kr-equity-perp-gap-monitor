from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Candle:
    """Minimal normalized OHLCV candle.

    All timestamps should be timezone-aware UTC datetimes in production adapters.
    """

    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float = 0.0


@dataclass(frozen=True)
class GapPoint:
    timestamp: datetime
    reference_close: float
    market_close: float
    reference_return_pct: float
    market_return_pct: float
    gap_pct: float
