# Korea Equity Perp Gap Monitor

Korea Equity Perp Gap Monitor is a small, keyless Python toolkit for comparing cross-venue price gaps between Korean equity-linked market exposure and crypto/perpetual markets.

The first research use case is semiconductor exposure related to **Samsung Electronics** and **SK Hynix**, especially where global crypto venues trade outside Korean stock-market hours. The project is designed for public-market-data research, not trade execution.

## Why this exists

Korean equity-linked crypto and perpetual markets can move when the Korean cash market is closed. Developers and researchers often need a simple, transparent way to:

- normalize public market data from multiple venues,
- align candles by timestamp,
- calculate return spreads and price gaps,
- export reproducible CSV outputs,
- test gap-calculation logic without private API keys.

This project keeps analysis separate from execution. It does **not** place orders, manage accounts, or provide financial advice.

## Features

- Public, keyless market-data adapters
- Binance public kline helper
- Hyperliquid public candle helper
- Candle alignment by timestamp
- Return-spread and premium/discount calculations
- CLI-friendly CSV workflow
- Unit tests for core math and alignment logic

## Installation

```bash
git clone https://github.com/KRMarketLab/kr-equity-perp-gap-monitor.git
cd kr-equity-perp-gap-monitor
python -m pip install -e ".[dev]"
```

## Example

```bash
python examples/samsung_skhynix_gap_demo.py
```

This example uses small sample data so the methodology can be reviewed without external credentials.

## CLI

```bash
kr-gap sample --out sample_gap.csv
```

## Methodology

The core gap metric compares normalized return paths:

```text
gap_pct = crypto_return_pct - reference_return_pct
```

Premium/discount can also be calculated when the two instruments are directly comparable:

```text
premium_pct = (market_price / reference_price - 1) * 100
```

See [`docs/methodology.md`](docs/methodology.md).

## Safety and scope

This repository is for research and educational tooling only. It does not include private API-key handling, live trading, leverage management, or automated order execution.

## Maintainer use of Codex

Codex can help maintain this project by reviewing data-normalization logic, generating regression tests, improving exchange adapters, drafting release notes, and checking security issues in local CLI workflows.

## License

MIT
