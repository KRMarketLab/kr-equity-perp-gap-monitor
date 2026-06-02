from __future__ import annotations

from collections.abc import Sequence


def pct_return(current: float, base: float) -> float:
    """Return percentage change from base to current."""
    if base == 0:
        raise ValueError("base must not be zero")
    return (current / base - 1.0) * 100.0


def premium_pct(market_price: float, reference_price: float) -> float:
    """Return percentage premium/discount of market_price versus reference_price."""
    if reference_price == 0:
        raise ValueError("reference_price must not be zero")
    return (market_price / reference_price - 1.0) * 100.0


def return_spread_pct(
    market_current: float,
    market_base: float,
    reference_current: float,
    reference_base: float,
) -> float:
    """Return market return minus reference return, in percentage points."""
    return pct_return(market_current, market_base) - pct_return(reference_current, reference_base)


def max_drawdown(values: Sequence[float]) -> float:
    """Return max drawdown in percent for a sequence of prices or ratios."""
    if not values:
        raise ValueError("values must not be empty")
    peak = values[0]
    worst = 0.0
    for value in values:
        peak = max(peak, value)
        if peak != 0:
            worst = min(worst, (value / peak - 1.0) * 100.0)
    return worst
