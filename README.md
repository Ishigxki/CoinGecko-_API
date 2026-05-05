# CoinGecko API

A simple Python-based crypto data ingestion and API service powered by CoinGecko.

This project fetches live cryptocurrency prices on a schedule, stores them in PostgreSQL, and exposes a small FastAPI application to retrieve the latest and historical price data.

## Features

- scheduled price collection from the CoinGecko API
- SQL storage in PostgreSQL
- REST API with endpoints for current and historical coin prices
- supports Bitcoin, Ethereum, and Solana by default

## How it works

- `collector.py` retrieves USD prices from CoinGecko every 60 seconds
- each price is inserted into the `crypto_prices` PostgreSQL table
- `main.py` exposes API endpoints with FastAPI
- `database.py` manages a single database connection using `psycopg2`

## Requirements

- Python 3.8+
- PostgreSQL database
- Python dependencies from `requirements.txt`

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Create a PostgreSQL database and user if needed.

3. Create the `crypto_prices` table:

   ```sql
   CREATE TABLE crypto_prices (
       id SERIAL PRIMARY KEY,
       coin TEXT NOT NULL,
       price NUMERIC NOT NULL,
       timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

4. Update the database credentials in `database.py` to match your local PostgreSQL setup.

## Running the collector

Start continuous ingestion from CoinGecko:

```bash
python collector.py
```

This script fetches prices every 60 seconds and stores them in the database.

## Running the API

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

By default, the server runs at `http://127.0.0.1:8000`.

## API Endpoints

- `GET /latest` – latest price for each tracked coin
- `GET /latest/{coin}` – latest price for a specific coin
- `GET /history/{coin}` – historical price records for a coin

Example:

```bash
curl http://127.0.0.1:8000/latest/bitcoin
```

## Notes

- `collector.py` currently tracks `bitcoin`, `ethereum`, and `solana`.
- The database connection is configured directly in `database.py`; for production use, move credentials to environment variables or a `.env` file.

## Future improvements

- add environment-based configuration
- support dynamic coin lists
- improve API error handling and response structure
- add automated tests
