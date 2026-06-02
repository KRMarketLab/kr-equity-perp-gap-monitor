# Methodology

This project focuses on transparent, reproducible gap analysis.

## Candle alignment

Market data from different venues is normalized into a common `Candle` model and then aligned by timestamp. The initial implementation uses an inner join on exact timestamps. Future versions may add tolerance-based alignment and market-session calendars.

## Return gap

The default gap metric compares normalized return paths:

```text
reference_return_pct = (reference_close / reference_base - 1) * 100
market_return_pct = (market_close / market_base - 1) * 100
gap_pct = market_return_pct - reference_return_pct
```

This is useful when the instruments are not directly priced in the same unit but are intended to represent similar exposure.

## Premium / discount

When two instruments are directly comparable, use:

```text
premium_pct = (market_price / reference_price - 1) * 100
```

## Non-goals

- No live trading
- No private API keys
- No account access
- No leverage or liquidation logic
- No financial advice
