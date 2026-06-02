from __future__ import annotations

from datetime import datetime, timezone

from kr_gap.align import calculate_gap_points, gap_points_to_frame
from kr_gap.models import Candle


# Synthetic demo data.
# Replace these with real public-market data when building a research notebook.
sk_hynix_reference = [
    Candle(datetime(2026, 1, 1, 0, tzinfo=timezone.utc), 100, 101, 99, 100),
    Candle(datetime(2026, 1, 1, 1, tzinfo=timezone.utc), 100, 102, 99, 101),
    Candle(datetime(2026, 1, 1, 2, tzinfo=timezone.utc), 101, 104, 100, 103),
]

hl_or_binance_proxy = [
    Candle(datetime(2026, 1, 1, 0, tzinfo=timezone.utc), 10, 10.1, 9.9, 10),
    Candle(datetime(2026, 1, 1, 1, tzinfo=timezone.utc), 10, 10.5, 10, 10.4),
    Candle(datetime(2026, 1, 1, 2, tzinfo=timezone.utc), 10.4, 10.9, 10.3, 10.8),
]

points = calculate_gap_points(sk_hynix_reference, hl_or_binance_proxy)
print(gap_points_to_frame(points).to_string(index=False))
