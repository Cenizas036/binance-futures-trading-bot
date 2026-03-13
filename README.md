# Binance Futures Testnet Trading Bot

## Overview

This project is a simple Python CLI trading bot that places **MARKET** and **LIMIT** orders on the **Binance Futures Testnet (USDT-M)**.

The application demonstrates a clean project structure, logging, input validation, and error handling while interacting with the Binance Futures API.

---

## Features

* Place **MARKET orders**
* Place **LIMIT orders**
* Supports **BUY and SELL**
* CLI-based user input
* Input validation
* Structured project architecture
* Logging of API requests, responses, and errors

---

## Project Structure

trading_bot/
│
├── bot/
│   ├── client.py        # Binance API client
│   ├── orders.py        # Order execution logic
│   ├── validators.py    # Input validation
│   └── logging_config.py
│
├── cli.py               # CLI entry point
├── requirements.txt
├── README.md
└── logs/                # API request and response logs
## Setup Instructions

### 1. Clone the repository

git clone https://github.com/yourusername/binance-futures-trading-bot.git

cd trading_bot

---

### 2. Create virtual environment

python -m venv venv

Activate:

Windows

venv\Scripts\activate

---

### 3. Install dependencies

pip install -r requirements.txt

---

### 4. Add Binance Testnet API Keys

Create a `.env` file in the project root.

Example:

BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret

Testnet URL used:

https://testnet.binancefuture.com

---

## Running the Bot

### Example MARKET Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.003

---

### Example LIMIT Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.003 --price 70000

---

## Example Output

Order Request Summary
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.003

Order Response
Order ID: 12345678
Status: FILLED
Executed Qty: 0.003

---

## Logs

All API requests and responses are logged in:

logs/trading_bot.log

Example log entry:

Order request -> BTCUSDT BUY MARKET qty=0.003
Order response -> {...}

---

## Assumptions

* Binance Futures Testnet account is active
* API keys have Futures permissions enabled
* Minimum order notional requirements are satisfied

---

## Requirements

Python 3.x

Libraries:

python-binance
python-dotenv
