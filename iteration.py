symbols = ["AAPL", "MSFT", "GOOG"]
prices = [180.0, 350.0, 140.0]

for i, (sym, px) in enumerate(zip(symbols, prices), start=1):
    print(f"{i}. {sym} -> {px}")