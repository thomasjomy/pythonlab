quotes = [
    {"symbol": "EURUSD", "bid": 1.0810, "ask": 1.0812},
    {"symbol": "USDJPY", "bid": 149.8, "ask": 149.82},
]

mids = {q["symbol"]: (q["bid"] + q["ask"]) / 2 for q in quotes}
print(mids)